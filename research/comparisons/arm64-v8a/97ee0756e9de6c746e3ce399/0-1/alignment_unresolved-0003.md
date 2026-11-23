# v15.7.2 → v15.7.3 · 命令位置の検査未完了 (3)

[一覧の目次](README.md)

<a id="compare-e8b38eefb06c60312f2690c9c4cd1e8c"></a>

### [`00b0ee2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ee2c.md) → [`00b0eef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0eef4.md) _ZN11flatbuffers6Parser5ErrorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdf8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.79% / 新版 78.79%

CFGの説明率　旧版 60.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ee30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ee34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ee34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0ee30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0ee34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0ee38",
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
      "00b0eef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b0eefc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b0ef00",
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

- 旧版 [`00b0ee30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ee2c.md#insn-00b0ee30) · [`00b0ee34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ee2c.md#insn-00b0ee34) · [`00b0ee38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ee2c.md#insn-00b0ee38)

~~~diff
- 00b0ee30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b0ee30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b0ee30 bytes f51300f9
- 00b0ee34 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0ee34 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0ee34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b0ee34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0ee34 bytes f44f03a9
- 00b0ee38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0ee38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0ee38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b0ee38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0ee38 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-904fdb8c6ef757e4ed8bcdd041875373"></a>

### [`00b0efe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0efe4.md) → [`00b0f0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f0ac.md) _ZNK11flatbuffers9Namespace21GetFullyQualifiedNameERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb70.md) · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdfc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc20.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.50% / 新版 79.50%

CFGの説明率　旧版 40.30% / 新版 40.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f014"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b0f0dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f0a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0f014",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f0a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0f2c0"
      ]
    ],
    [
      "00b0f17c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0f0d0"
      ]
    ]
  ],
  "added": [
    [
      "00b0f0dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b0f170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0f2c0"
      ]
    ],
    [
      "00b0f17c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0f198"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0efe4.md#insn-00b0f014) · [`00b0f0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0efe4.md#insn-00b0f0a8) · [`00b0f0c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0efe4.md#insn-00b0f0c8)

~~~diff
- 00b0f014 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00b0f014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0f014 bytes e82f00f9
- 00b0f0a8 ["CBRANCH", null, ["local:b32:8", "register:102:1"]]
- 00b0f0a8 bytes 820a0054
- 00b0f0c8 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00b0f0c8 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3053ade4eaf74356db7b24b76bce4b41"></a>

### [`00b17014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17014.md) → [`00b170dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b170dc.md) _ZNK11flatbuffers7EnumDef13ReverseLookupElb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b17030"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b170f8"
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
      "unmatched:00b17030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b17114"
      ]
    ]
  ],
  "added": [
    [
      "00b170f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b17114"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b17030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17014.md#insn-00b17030) · [`00b1702c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17014.md#insn-00b1702c)
- 新版 [`00b170f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b170dc.md#insn-00b170f8)

~~~diff
- 00b17030 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b17030 bytes e0000054
+ 00b170f8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b170f8 bytes e0000054
- 00b1702c ["INT_LESSEQUAL", "register:105:1", ["register:4040:8", "register:4048:8"]]
- 00b1702c ["INT_SBORROW", "register:106:1", ["register:4048:8", "register:4040:8"]]
- 00b1702c ["INT_SUB", "tmp:0:8", ["register:4048:8", "register:4040:8"]]
- 00b1702c ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00b1702c bytes 3f0108eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a3457aae63922799305445e2bd280a2"></a>

### [`00b19b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19b50.md) → [`00b19c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19c18.md) _ZN11flatbuffers6Parser9ParseHashERNS_5ValueEPNS_8FieldDefE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf910.md) · 呼出先 11件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md) [`00bdf0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0a0.md) [`00bdf0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0b0.md)
- 新版 呼出元 1件 [`00bdf9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9c0.md) · 呼出先 11件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md) [`00bdf160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf160.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.52% / 新版 50.52%

CFGの説明率　旧版 15.94% / 新版 16.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 20件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19f64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b1a02c"
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
      "00b19cb4",
      "DATA",
      [
        "storage",
        "002f8507",
        "switchD_00b19bf4::switchdataD_002f8507",
        "byte"
      ]
    ],
    [
      "00b19cbc",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b19c58"
      ]
    ],
    [
      "00b19cbc",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b19c30"
      ]
    ]
  ],
  "added": [
    [
      "00b19cb4",
      "DATA",
      [
        "storage",
        "002f8507",
        "switchD_00b19cbc::switchdataD_002f8507",
        "byte"
      ]
    ],
    [
      "00b19cbc",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b19d20"
      ]
    ],
    [
      "00b19cbc",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b19cf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b19bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19b50.md#insn-00b19bcc) · [`00b19c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19b50.md#insn-00b19c24) · [`00b19c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b19b50.md#insn-00b19c38)
- 新版 [`00b19c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19c18.md#insn-00b19c94)

~~~diff
- 00b19bcc ["INT_ADD", "register:40f0:8", ["const:b19bcc:8", "const:4:8"]]
- 00b19bcc ["CALL", null, ["callee:00bdb010:8"]]
+ 00b19c94 ["INT_ADD", "register:40f0:8", ["const:b19c94:8", "const:4:8"]]
+ 00b19c94 ["CALL", null, ["callee:00bdb010:8"]]
- 00b19bcc bytes e5040394
+ 00b19c94 bytes df040394
- 00b19c24 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b19c24 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b19c24 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b19c24 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b19c24 bytes e9020037
- 00b19c38 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b19c38 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b19c38 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b19c38 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b19c38 bytes e9030037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccf0e243f3af4984d5ca6b74209aed6a"></a>

### [`00b1f4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f4cc.md) → [`00b1f594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f594.md) _ZNK11flatbuffers7EnumDef8AllFlagsEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdf0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0c0.md) [`00bdf0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdf170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf170.md) [`00bdf180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf180.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 64.71% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f538"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b1f600"
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
      "unmatched:00b1f538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f5e4"
      ]
    ]
  ],
  "added": [
    [
      "00b1f600",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f5e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1f538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f4cc.md#insn-00b1f538) · [`00b1f4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f4cc.md#insn-00b1f4f8)
- 新版 [`00b1f600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f594.md#insn-00b1f600) · [`00b1f5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f594.md#insn-00b1f5c0)

~~~diff
- 00b1f538 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b1f538 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b1f538 bytes 21ffff54
+ 00b1f600 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b1f600 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b1f600 bytes 21ffff54
- 00b1f4f8 ["BRANCH", null, ["local:b9:8"]]
+ 00b1f5c0 ["BRANCH", null, ["local:b7:8"]]
- 00b1f4f8 bytes 14000014
+ 00b1f5c0 bytes 14000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef8804a386eac533a33bedf78a68376f"></a>

### [`00b23138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23138.md) → [`00b23200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23200.md) _ZN11flatbuffers6Parser13MarkGeneratedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 27.27% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b23180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b23184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b23224"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2315c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b23194"
      ]
    ],
    [
      "unmatched:00b23188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b23174"
      ]
    ],
    [
      "unmatched:00b23190",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b23270"
      ]
    ]
  ],
  "added": [
    [
      "00b23224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2325c"
      ]
    ],
    [
      "00b23250",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2323c"
      ]
    ],
    [
      "00b23258",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b23270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2315c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23138.md#insn-00b2315c) · [`00b23180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23138.md#insn-00b23180) · [`00b23184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23138.md#insn-00b23184)

~~~diff
- 00b2315c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b2315c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b2315c ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b2315c bytes c9010054
- 00b23180 ["COPY", "tmp:0:4", ["register:4060:4"]]
- 00b23180 ["INT_ADD", "tmp:1:8", ["register:4078:8", "const:78:8"]]
- 00b23180 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b23180 bytes ece10139
- 00b23184 ["COPY", "tmp:0:4", ["register:4060:4"]]
- 00b23184 ["INT_ADD", "tmp:1:8", ["register:4080:8", "const:78:8"]]
- 00b23184 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b23184 bytes 0ce20139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5e873fe06c5e1fa7a6744eb58e085f"></a>

### [`00b2506c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b2506c.md) → [`00b25134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25134.md) _ZN11flatbuffers6Parser24ParseProtoCurliesOrIdentEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdf870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf870.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 90.00% / 新版 81.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2509c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b25164"
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
      "unmatched:00b2509c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b251b8"
      ]
    ]
  ],
  "added": [
    [
      "00b25164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b251b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2509c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b2506c.md#insn-00b2509c) · [`00b25088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b2506c.md#insn-00b25088)
- 新版 [`00b25164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25134.md#insn-00b25164) · [`00b25150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b25134.md#insn-00b25150)

~~~diff
- 00b2509c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2509c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b2509c bytes a1020054
+ 00b25164 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b25164 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b25164 bytes a1020054
- 00b25088 ["INT_ADD", "register:40f0:8", ["const:b25088:8", "const:4:8"]]
- 00b25088 ["CALL", null, ["callee:00bdf920:8"]]
+ 00b25150 ["INT_ADD", "register:40f0:8", ["const:b25150:8", "const:4:8"]]
+ 00b25150 ["CALL", null, ["callee:00bdf920:8"]]
- 00b25088 bytes fae90294
+ 00b25150 bytes f4e90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39cd820d1ddff3903a2b7562eba5e141"></a>

### [`00b25108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25108.md) → [`00b251d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf130.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1e0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 83.33% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2516c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b25234"
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
      "unmatched:00b2516c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b25260"
      ]
    ]
  ],
  "added": [
    [
      "00b25234",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b25260"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2516c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25108.md#insn-00b2516c) · [`00b25234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b25108.md#insn-00b25234)
- 新版 [`00b252fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md#insn-00b252fc) · [`00b25234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b251d0.md#insn-00b25234)

~~~diff
- 00b2516c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b2516c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b2516c bytes 6a0100b5
- 00b25234 ["INT_ADD", "register:40f0:8", ["const:b25234:8", "const:4:8"]]
- 00b25234 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b252fc ["INT_ADD", "register:40f0:8", ["const:b252fc:8", "const:4:8"]]
+ 00b252fc ["CALL", null, ["callee:00bde6e0:8"]]
- 00b25234 bytes ffe40294
+ 00b252fc bytes f9e40294
+ 00b25234 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b25234 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b25234 bytes 6a0100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65738ddba8231a2baed5e43151fb8af8"></a>

### [`00b261c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b26/00b261c4.md) → [`00b2628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md) _ZN11flexbuffers7Builder6FinishEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfa30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa30.md) · 呼出先 4件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdfa50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa50.md) [`00bdffd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffd0.md) [`00bdffe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md)
- 新版 呼出元 1件 [`00bdfae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfae0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdfb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb00.md) [`00be0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0080.md) [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.96% / 新版 98.96%

CFGの説明率　旧版 75.00% / 新版 68.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b26328"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b263f0"
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
      "unmatched:00b26328",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b26408"
      ]
    ]
  ],
  "added": [
    [
      "00b263f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b26408"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b26260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b26/00b261c4.md#insn-00b26260) · [`00b26328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b26/00b261c4.md#insn-00b26328)
- 新版 [`00b26328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md#insn-00b26328) · [`00b263f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md#insn-00b263f0)

~~~diff
- 00b26260 ["BRANCH", null, ["local:b8:8"]]
+ 00b26328 ["BRANCH", null, ["local:b9:8"]]
- 00b26260 bytes 04000014
+ 00b26328 bytes 04000014
- 00b26328 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b26328 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b26328 bytes c1000054
+ 00b263f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b263f0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00b263f0 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22658b49289b53b5f3f75ced9b4e4a17"></a>

### [`00b2b6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2b6b0.md) → [`00b2b778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b778.md) _ZN11flatbuffers7RPCCall11DeserializeERNS_6ParserEPKN10reflection7RPCCallE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf990.md) · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdf050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf050.md)
- 新版 呼出元 1件 [`00bdfa40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa40.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdf100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf100.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 55.26% / 新版 53.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b71c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b740"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b740"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2b7d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b2b728"
      ]
    ],
    [
      "unmatched:00b2b71c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2b720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b2b748"
      ]
    ]
  ],
  "added": [
    [
      "00b2b7d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2b7f0"
      ]
    ],
    [
      "00b2b7e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b2b7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2b810"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2b6b0.md#insn-00b2b71c) · [`00b2b720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2b6b0.md#insn-00b2b720) · [`00b2b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2b6b0.md#insn-00b2b734)

~~~diff
- 00b2b71c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b2b71c ["COPY", "tmp:1:8", ["register:8:8"]]
- 00b2b71c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2b71c bytes e8030039
- 00b2b720 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:4", "const:0:4"]]
- 00b2b720 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b2b720 bytes 56010035
- 00b2b734 ["INT_ADD", "register:40f0:8", ["const:b2b734:8", "const:4:8"]]
- 00b2b734 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b2b734 bytes 03be0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e949d7890b453f4a0596fb4970fdaea"></a>

### [`00b2c49c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c49c.md) → [`00b2c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md) _ZN10reflection13CreateEnumValERN11flatbuffers17FlatBufferBuilderENS0_6OffsetINS0_6StringEEElNS3_INS_6ObjectEEENS3_INS_4TypeEEENS3_INS0_6Vec

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf030.md) · 呼出先 7件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf390.md) [`00bdf410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf410.md) [`00bdf420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf420.md) [`00bdf430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf430.md)
- 新版 呼出元 1件 [`00bdf0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0e0.md) · 呼出先 7件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md) [`00bdf4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4c0.md) [`00bdf4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4d0.md) [`00bdf4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf4e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2c4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2c4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2c574"
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
      "unmatched:00b2c4ac",
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
      "00b2c574",
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

- 旧版 [`00b2c4ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c49c.md#insn-00b2c4ac) · [`00b2c574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c49c.md#insn-00b2c574)
- 新版 [`00b2c63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md#insn-00b2c63c) · [`00b2c574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md#insn-00b2c574)

~~~diff
- 00b2c4ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b2c4ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b2c4ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b2c4ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2c4ac bytes fd7b04a9
- 00b2c574 ["INT_ADD", "register:40f0:8", ["const:b2c574:8", "const:4:8"]]
- 00b2c574 ["CALL", null, ["callee:00bdf4d0:8"]]
+ 00b2c63c ["INT_ADD", "register:40f0:8", ["const:b2c63c:8", "const:4:8"]]
+ 00b2c63c ["CALL", null, ["callee:00bdf4d0:8"]]
- 00b2c574 bytes abcb0294
+ 00b2c63c bytes a5cb0294
+ 00b2c574 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b2c574 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b2c574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 00b2c574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b2c574 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c87719055e68e27727fdf3cc6da0a4f"></a>

### [`00b2df28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2d/00b2df28.md) → [`00b2dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dff0.md) _ZN11flatbuffers11EqualByNameERKNS_4TypeES2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf090.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdf140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf140.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.54% / 新版 63.54%

CFGの説明率　旧版 39.13% / 新版 41.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 10件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2df28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2df28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2df2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2df28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2df2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2df98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2e144"
      ]
    ]
  ],
  "added": [
    [
      "00b2dff0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b2dff4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b2e060",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2e144"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2df28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2d/00b2df28.md#insn-00b2df28) · [`00b2df2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2d/00b2df28.md#insn-00b2df2c) · [`00b2df88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2d/00b2df28.md#insn-00b2df88)

~~~diff
- 00b2df28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b2df28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b2df28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b2df28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b2df28 bytes f44fbea9
- 00b2df2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b2df2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b2df2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b2df2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2df2c bytes fd7b01a9
- 00b2df88 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b2df88 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b2df88 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b2df88 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b2df88 bytes 02018d9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2b919bd9f7c026652d6ec165a957af7"></a>

### [`00b2e0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e0a8.md) → [`00b2e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e170.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEmc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 88.89% / 新版 84.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2e170"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b2e238"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b2e170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e0a8.md#insn-00b2e170) · [`00b2e114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e0a8.md#insn-00b2e114)
- 新版 [`00b2e238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e170.md#insn-00b2e238) · [`00b2e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e170.md#insn-00b2e1dc)

~~~diff
- 00b2e170 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2e170 ["RETURN", null, ["register:0:8"]]
- 00b2e170 bytes c0035fd6
+ 00b2e238 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b2e238 ["RETURN", null, ["register:0:8"]]
+ 00b2e238 bytes c0035fd6
- 00b2e114 ["INT_ADD", "register:40f0:8", ["const:b2e114:8", "const:4:8"]]
- 00b2e114 ["CALL", null, ["callee:00bdda40:8"]]
+ 00b2e1dc ["INT_ADD", "register:40f0:8", ["const:b2e1dc:8", "const:4:8"]]
+ 00b2e1dc ["CALL", null, ["callee:00bdda40:8"]]
- 00b2e114 bytes 1fbe0294
+ 00b2e1dc bytes 19be0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60405c6c2dae52a37ad94104262cdacc"></a>

### [`00b2e3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e3ac.md) → [`00b2e474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e474.md) _ZN11flatbuffers9HashFnv1aImEET_PKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2e3c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e3ac.md#insn-00b2e3c4) · [`00b2e3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e3ac.md#insn-00b2e3d0) · [`00b2e3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e3ac.md#insn-00b2e3e4)
- 新版 [`00b2e48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e474.md#insn-00b2e48c) · [`00b2e4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e474.md#insn-00b2e4ac)

~~~diff
- 00b2e3c4 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b2e3c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b2e48c ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b2e48c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b2e3c4 bytes 29010034
+ 00b2e48c bytes 29010034
- 00b2e3d0 ["INT_AND", "register:4050:8", ["register:4050:8", "const:ffff0000ffffffff:8"]]
- 00b2e3d0 ["INT_OR", "register:4050:8", ["register:4050:8", "const:10000000000:8"]]
- 00b2e3d0 bytes 0a20c0f2
- 00b2e3e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b2e3e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b2e4ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b2e4ac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b2e3e4 bytes 89ffff35
+ 00b2e4ac bytes 89ffff35
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63b9efb4fd5d11ea8516df8ed951621c"></a>

### [`00b2ed90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2ed90.md) → [`00b2ee58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md) _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4e0.md) · 呼出先 2件 [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb650.md)
- 新版 呼出元 1件 [`00bdf590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf590.md) · 呼出先 2件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb700.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 74.36% / 新版 72.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2edb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b2ee7c"
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
      "unmatched:00b2edb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2eea0"
      ]
    ]
  ],
  "added": [
    [
      "00b2ee7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2eea0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2edb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2ed90.md#insn-00b2edb4) · [`00b2edbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2ed90.md#insn-00b2edbc)
- 新版 [`00b2ee7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md#insn-00b2ee7c) · [`00b2ee84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md#insn-00b2ee84)

~~~diff
- 00b2edb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b2edb4 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00b2edb4 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00b2edb4 bytes 2d010054
+ 00b2ee7c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b2ee7c ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00b2ee7c ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 00b2ee7c bytes 2d010054
- 00b2edbc ["INT_RIGHT", "tmp:0:4", ["register:4098:4", "const:0:4"]]
- 00b2edbc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b2edbc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b2edbc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b2ee84 ["INT_RIGHT", "tmp:0:4", ["register:4098:4", "const:0:4"]]
+ 00b2ee84 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b2ee84 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b2ee84 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b2edbc bytes 73000036
+ 00b2ee84 bytes 73000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52b1b5804e0293a6318d291fbe35c14b"></a>

### [`00b31394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31394.md) → [`00b3145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3145c.md) _ZTv0_n24_NSt6__ndk113basic_istreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00b31394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31398"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31394",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31398",
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
      "00b3145c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b31460",
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

- 旧版 [`00b31394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31394.md#insn-00b31394) · [`00b31398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31394.md#insn-00b31398)
- 新版 [`00b3145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3145c.md#insn-00b3145c)

~~~diff
- 00b31394 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b31394 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b31394 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b31394 bytes f30f1ef8
- 00b31398 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b31398 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b31398 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b31398 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b31398 bytes fd7b01a9
+ 00b3145c ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00b3145c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b3145c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b3145c bytes f30f1ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1f5a20fa79d7a4fb3b2dc7b49ab3ad"></a>

### [`00b316f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b316f0.md) → [`00b317b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b317b8.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 84.91% / 新版 88.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b317d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b317d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b31898"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b317d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b316f0.md#insn-00b317d0) · [`00b3172c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b316f0.md#insn-00b3172c)
- 新版 [`00b31898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b317b8.md#insn-00b31898) · [`00b317f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b317b8.md#insn-00b317f4)

~~~diff
- 00b317d0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b317d0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b317d0 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00b317d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b317d0 bytes 09a001a9
+ 00b31898 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b31898 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00b31898 ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
+ 00b31898 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b31898 bytes 09a001a9
- 00b3172c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b3172c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b317f4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b317f4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b3172c bytes 280100b4
+ 00b317f4 bytes 280100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ff5519859dbd998807d658801e4d02d"></a>

### [`00b31aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31aa4.md) → [`00b31b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31b6c.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE8overflowEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 91.49% / 新版 87.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b31d60"
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
      "unmatched:00b31c90",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31cbc",
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
      "00b31d58",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b31d84",
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

- 旧版 [`00b31bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31aa4.md#insn-00b31bd0) · [`00b31c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31aa4.md#insn-00b31c98)
- 新版 [`00b31c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31b6c.md#insn-00b31c98) · [`00b31d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31b6c.md#insn-00b31d60)

~~~diff
- 00b31bd0 ["INT_ADD", "register:40f0:8", ["const:b31bd0:8", "const:4:8"]]
- 00b31bd0 ["CALL", null, ["callee:00bdef70:8"]]
+ 00b31c98 ["INT_ADD", "register:40f0:8", ["const:b31c98:8", "const:4:8"]]
+ 00b31c98 ["CALL", null, ["callee:00bdef70:8"]]
- 00b31bd0 bytes bcb40294
+ 00b31c98 bytes b6b40294
- 00b31c98 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b31c98 ["RETURN", null, ["register:0:8"]]
- 00b31c98 bytes c0035fd6
+ 00b31d60 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b31d60 ["RETURN", null, ["register:0:8"]]
+ 00b31d60 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-487edb7f3b4774d0010ac49cd407e30e"></a>

### [`00b31cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31cc8.md) → [`00b31d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31d90.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) · 呼出先 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b31cd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b31d9c"
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
      "unmatched:00b31ccc",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b31cd4",
      "DATA",
      [
        "storage",
        "00c11120",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "unmatched:00b31cd8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3f0"
      ]
    ]
  ],
  "added": [
    [
      "00b31d94",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00b31d9c",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b31da0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb3f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b31cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31cc8.md#insn-00b31cd4) · [`00b31cc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31cc8.md#insn-00b31cc8)
- 新版 [`00b31d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31d90.md#insn-00b31d9c)

~~~diff
- 00b31cd4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b31cd4 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b31cd4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b31cd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b31cd4 bytes 088400f8
+ 00b31d9c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b31d9c ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b31d9c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00b31d9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b31d9c bytes 088400f8
- 00b31cc8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 00b31cc8 bytes 480700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eb00934ea7611c7454fe34269bffb54"></a>

### [`00b31d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31d40.md) → [`00b31e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31e08.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdbfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfa0.md) · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdbfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfa0.md) [`00be00f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00f0.md)
- 新版 呼出元 1件 [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdc050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 23.08% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31d60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31d9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31e04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31d60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31ee8"
      ]
    ],
    [
      "unmatched:00b31d9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31e80"
      ]
    ],
    [
      "unmatched:00b31e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31ee8"
      ]
    ]
  ],
  "added": [
    [
      "00b31e28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31ee8"
      ]
    ],
    [
      "00b31e64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31e80"
      ]
    ],
    [
      "00b31ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b31ee8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b31d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31d40.md#insn-00b31d60) · [`00b31d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31d40.md#insn-00b31d9c) · [`00b31dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31d40.md#insn-00b31dfc)

~~~diff
- 00b31d60 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b31d60 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b31d60 bytes 000600b4
- 00b31d9c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b31d9c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b31d9c bytes e1000054
- 00b31dfc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b31dfc ["INT_ADD", "register:40f0:8", ["const:b31dfc:8", "const:4:8"]]
- 00b31dfc ["CALLIND", null, ["register:0:8"]]
- 00b31dfc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9446bf2ce798fadf80130a052c058de1"></a>

### [`00b31e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31e30.md) → [`00b31ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31ef8.md) _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.20% / 新版 54.20%

CFGの説明率　旧版 30.00% / 新版 26.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31e30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31e34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b31e34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b31e30",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31e34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b31e38",
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
      "00b31ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b31efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b31f00",
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

- 旧版 [`00b31e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31e30.md#insn-00b31e30) · [`00b31e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31e30.md#insn-00b31e34) · [`00b31e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b31e30.md#insn-00b31e38)

~~~diff
- 00b31e30 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b31e30 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b31e30 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b31e30 bytes f70f1cf8
- 00b31e34 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b31e34 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b31e34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b31e34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b31e34 bytes f65701a9
- 00b31e38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b31e38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b31e38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b31e38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b31e38 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c39a69889b39943638c041bc3a98b3c"></a>

### [`00b32a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b32/00b32a18.md) → [`00b32ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32ae0.md) _ZNSt6__ndk17__sort3IRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEjT0_S9_S9_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0040.md) · 呼出先 1件 [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 1件 [`00be00f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00f0.md) · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.15% / 新版 69.15%

CFGの説明率　旧版 9.09% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b32a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b32a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b32a20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b32a1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b32a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b32a24",
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
      "00b32ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b32ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b32aec",
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

- 旧版 [`00b32a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b32/00b32a18.md#insn-00b32a1c) · [`00b32a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b32/00b32a18.md#insn-00b32a20) · [`00b32a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b32/00b32a18.md#insn-00b32a24)

~~~diff
- 00b32a1c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b32a1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b32a1c bytes f91300f9
- 00b32a20 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b32a20 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b32a20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b32a20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b32a20 bytes f85f03a9
- 00b32a24 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b32a24 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b32a24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b32a24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b32a24 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26edc3285becacf5bddb90ad863a634"></a>

### [`00b331b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b331b0.md) → [`00b33278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33278.md) _ZN11flexbuffers7Builder8WriteAnyERKNS0_5ValueEh

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfa50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa50.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdffe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md)
- 新版 呼出元 1件 [`00bdfb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb00.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.18% / 新版 70.18%

CFGの説明率　旧版 31.82% / 新版 30.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b331b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b331b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b331b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b331b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b331b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b331c8",
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
      "00b3327c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b33280",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b33290",
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

- 旧版 [`00b331b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b331b0.md#insn-00b331b4) · [`00b331b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b331b0.md#insn-00b331b8) · [`00b331c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b331b0.md#insn-00b331c8)

~~~diff
- 00b331b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b331b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b331b4 bytes f30b00f9
- 00b331b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b331b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b331b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b331b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b331b8 bytes fd7b02a9
- 00b331c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b331c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b331c8 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38d9d2d32c1f9fd407d7254a1140643f"></a>

### [`00b33600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33600.md) → [`00b336c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdffe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 41.33% / 新版 40.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33608"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b33604",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33608",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3360c",
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
      "00b336cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b336d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b336d4",
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

- 旧版 [`00b33604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33600.md#insn-00b33604) · [`00b33608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33600.md#insn-00b33608) · [`00b3360c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33600.md#insn-00b3360c)

~~~diff
- 00b33604 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b33604 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b33604 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b33604 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33604 bytes fc6f01a9
- 00b33608 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b33608 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b33608 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b33608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33608 bytes fa6702a9
- 00b3360c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3360c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3360c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b3360c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3360c bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3735dd11a80511be403371698da3bf75"></a>

### [`00b33c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33c70.md) → [`00b33d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33d38.md) FUN_00b33d38

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b255d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b255d8.md) [`00b33b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33b54.md) [`00b44200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44200.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 3件 [`00b256a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b256a0.md) [`00b33c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md) [`00b442c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.76% / 新版 75.76%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33c74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b33c74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b33c70",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33c74",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b33c78",
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
      "00b33d38",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b33d3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b33d40",
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

- 旧版 [`00b33c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33c70.md#insn-00b33c70) · [`00b33c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33c70.md#insn-00b33c74) · [`00b33c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33c70.md#insn-00b33c78)

~~~diff
- 00b33c70 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b33c70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b33c70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b33c70 bytes f90f1bf8
- 00b33c74 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b33c74 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b33c74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b33c74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33c74 bytes f85f01a9
- 00b33c78 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b33c78 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b33c78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b33c78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b33c78 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af0a2ad485478813efe26c0ad68f9ecd"></a>

### [`00b34c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34c04.md) → [`00b34ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md) _ZN10reflection12FieldBuilder14add_deprecatedEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf010.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 66.67% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b34cb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b34d78"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b34cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34c04.md#insn-00b34cb0) · [`00b34c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34c04.md#insn-00b34c1c)
- 新版 [`00b34d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md#insn-00b34d78) · [`00b34ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md#insn-00b34ce4)

~~~diff
- 00b34cb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b34cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b34cb0 bytes 681e00f9
+ 00b34d78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
+ 00b34d78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b34d78 bytes 681e00f9
- 00b34c1c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b34c1c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b34ce4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b34ce4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b34c1c bytes 28050034
+ 00b34ce4 bytes 28050034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bcfc7004a557e41e5b17831ece237c9"></a>

### [`00b371b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b371b4.md) → [`00b3727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b3727c.md) _ZNK10reflection7EnumVal6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfac0.md) · 呼出先 2件 [`00bdfa80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfa80.md) [`00bdfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaa0.md)
- 新版 呼出元 1件 [`00bdfb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb70.md) · 呼出先 2件 [`00bdfb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb30.md) [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.78% / 新版 90.78%

CFGの説明率　旧版 76.37% / 新版 75.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3743c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3744c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b37458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b374fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b37440"
      ]
    ],
    [
      "unmatched:00b3743c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b37398"
      ]
    ],
    [
      "unmatched:00b3744c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3739c"
      ]
    ]
  ],
  "added": [
    [
      "00b374fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b37508"
      ]
    ],
    [
      "00b37504",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b37398"
      ]
    ],
    [
      "00b37514",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3739c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3743c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b371b4.md#insn-00b3743c) · [`00b3744c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b371b4.md#insn-00b3744c) · [`00b37458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b371b4.md#insn-00b37458)

~~~diff
- 00b3743c ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:4", "const:0:4"]]
- 00b3743c ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b3743c bytes abf4ff35
- 00b3744c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3744c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b3744c bytes 43f4ff54
- 00b37458 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b37458 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b37458 bytes e3f3ff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c38fa8d4820bd2af8d7d8f421add1850"></a>

### [`00b37c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b37c10.md) → [`00b37cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b37/00b37cd8.md) _ZNK10reflection7RPCCall6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfad0.md) · 呼出先 2件 [`00bdfaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaa0.md) [`00bdfaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfaf0.md)
- 新版 呼出元 1件 [`00bdfb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb80.md) · 呼出先 2件 [`00bdfb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb50.md) [`00bdfba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfba0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.38% / 新版 80.38%

CFGの説明率　旧版 47.21% / 新版 47.01%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 24件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b37c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b37c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b37c14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b37c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b37c14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b37c18",
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
      "00b37cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b37cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b37ce0",
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

- 旧版 [`00b37c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b37c10.md#insn-00b37c10) · [`00b37c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b37c10.md#insn-00b37c14) · [`00b37c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b37/00b37c10.md#insn-00b37c18)

~~~diff
- 00b37c10 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b37c10 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b37c10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b37c10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b37c10 bytes f85fbca9
- 00b37c14 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b37c14 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b37c14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b37c14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b37c14 bytes f65701a9
- 00b37c18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b37c18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b37c18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b37c18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b37c18 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fa4e2f0eb149f97113f1b8fdd22a801"></a>

### [`00b39120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39120.md) → [`00b391e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b391e8.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0030.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00be00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00e0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 19.05% / 新版 19.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b39124"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b39124"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b39128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b39124",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b39128",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3912c",
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
      "00b391ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b391f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b391f4",
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

- 旧版 [`00b39124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39120.md#insn-00b39124) · [`00b39128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39120.md#insn-00b39128) · [`00b3912c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39120.md#insn-00b3912c)

~~~diff
- 00b39124 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b39124 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b39124 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b39124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b39124 bytes fc6f01a9
- 00b39128 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b39128 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b39128 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b39128 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b39128 bytes fa6702a9
- 00b3912c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3912c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3912c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b3912c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3912c bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8abf6847e9106ab744aef1a71081159"></a>

### [`00b3a694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a694.md) → [`00b3a75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0060.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0000.md)
- 新版 呼出元 1件 [`00be0110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0110.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 85.12% / 新版 85.12%

CFGの説明率　旧版 7.69% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3a874"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b3a93c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3a874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a694.md#insn-00b3a874) · [`00b3a6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a694.md#insn-00b3a6c8)
- 新版 [`00b3a93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md#insn-00b3a93c) · [`00b3a790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md#insn-00b3a790)

~~~diff
- 00b3a874 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3a874 ["RETURN", null, ["register:0:8"]]
- 00b3a874 bytes c0035fd6
+ 00b3a93c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b3a93c ["RETURN", null, ["register:0:8"]]
+ 00b3a93c bytes c0035fd6
- 00b3a6c8 ["INT_ADD", "register:40f0:8", ["const:b3a6c8:8", "const:4:8"]]
- 00b3a6c8 ["CALL", null, ["callee:00be00b0:8"]]
+ 00b3a790 ["INT_ADD", "register:40f0:8", ["const:b3a790:8", "const:4:8"]]
+ 00b3a790 ["CALL", null, ["callee:00be00b0:8"]]
- 00b3a6c8 bytes 4e960294
+ 00b3a790 bytes 48960294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18878b31d63a6047bded87d2579e93db"></a>

### [`00b3a878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a878.md) → [`00b3a940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a940.md) FUN_00b3a940

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b39d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39d04.md) [`00b3ac8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3ac8c.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0060.md)
- 新版 呼出元 2件 [`00b39dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39dcc.md) [`00b3ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3ad54.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be0110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0110.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.15% / 新版 72.15%

CFGの説明率　旧版 44.44% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3a87c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3a87c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3a880"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3a87c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3a880",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3a884",
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
      "00b3a944",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b3a948",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3a94c",
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

- 旧版 [`00b3a87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a878.md#insn-00b3a87c) · [`00b3a880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a878.md#insn-00b3a880) · [`00b3a884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a878.md#insn-00b3a884)

~~~diff
- 00b3a87c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b3a87c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b3a87c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b3a87c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3a87c bytes fc6f01a9
- 00b3a880 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b3a880 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b3a880 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3a880 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3a880 bytes fa6702a9
- 00b3a884 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3a884 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3a884 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b3a884 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3a884 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3866491c438389b801ef3600379241"></a>

### [`00b3b770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b770.md) → [`00b3b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3b838.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0010.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.95% / 新版 63.95%

CFGの説明率　旧版 27.27% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b870"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3b79c",
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
      "00b3b864",
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

- 旧版 [`00b3b79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b770.md#insn-00b3b79c) · [`00b3b838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b770.md#insn-00b3b838) · [`00b3b840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3b770.md#insn-00b3b840)

~~~diff
- 00b3b79c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b3b79c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b3b79c ["COPY", "tmp:2:8", ["register:8:8"]]
- 00b3b79c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3b79c bytes e10300a9
- 00b3b838 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b3b838 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3b838 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b3b838 ["INT_ZEXT", "register:40a0:8", ["tmp:0:4"]]
- 00b3b838 bytes 5401891a
- 00b3b840 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3b840 ["COPY", "tmp:1:4", ["register:40e0:4"]]
- 00b3b840 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3b840 ["COPY", "tmp:1:4", ["register:4098:4"]]
- 00b3b840 bytes 8233931a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2236f39691ea07074bb2b0507c590265"></a>

### [`00b3be18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3be18.md) → [`00b3bee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc50.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0010.md)
- 新版 呼出元 1件 [`00bdfd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd00.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 37.50% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3bfb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b3c078"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3bfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3be18.md#insn-00b3bfb0) · [`00b3be54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3b/00b3be18.md#insn-00b3be54)
- 新版 [`00b3c078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md#insn-00b3c078) · [`00b3bf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bee0.md#insn-00b3bf1c)

~~~diff
- 00b3bfb0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3bfb0 ["RETURN", null, ["register:0:8"]]
- 00b3bfb0 bytes c0035fd6
+ 00b3c078 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b3c078 ["RETURN", null, ["register:0:8"]]
+ 00b3c078 bytes c0035fd6
- 00b3be54 ["INT_ADD", "register:40f0:8", ["const:b3be54:8", "const:4:8"]]
- 00b3be54 ["CALL", null, ["callee:00be00c0:8"]]
+ 00b3bf1c ["INT_ADD", "register:40f0:8", ["const:b3bf1c:8", "const:4:8"]]
+ 00b3bf1c ["CALL", null, ["callee:00be00c0:8"]]
- 00b3be54 bytes 6f900294
+ 00b3bf1c bytes 69900294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c103a5fea8315d9ef683137681ac2a3f"></a>

### [`00b3c284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3c284.md) → [`00b3c34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c34c.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection6ObjectEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2f0.md) · 呼出先 2件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md) [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md)
- 新版 呼出元 1件 [`00bdf3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3a0.md) · 呼出先 2件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md) [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 61.54% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3c284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3c288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3c288"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3c284",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3c288",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3c28c",
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
      "00b3c34c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b3c350",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b3c354",
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

- 旧版 [`00b3c284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3c284.md#insn-00b3c284) · [`00b3c288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3c284.md#insn-00b3c288) · [`00b3c28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3c284.md#insn-00b3c28c)

~~~diff
- 00b3c284 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b3c284 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b3c284 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b3c284 bytes f50f1df8
- 00b3c288 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b3c288 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b3c288 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b3c288 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3c288 bytes f44f01a9
- 00b3c28c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b3c28c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b3c28c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3c28c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3c28c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a30079725902720f056c55fee7e2470"></a>

### [`00b3cce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md) → [`00b3cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0050.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bdfff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md)
- 新版 呼出元 1件 [`00be0100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0100.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 80.99% / 新版 80.99%

CFGの説明率　旧版 35.71% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3cd18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md#insn-00b3cd18) · [`00b3cd2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md#insn-00b3cd2c) · [`00b3cd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md#insn-00b3cd30)
- 新版 [`00b3cde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md#insn-00b3cde0)

~~~diff
- 00b3cd18 ["INT_ADD", "register:40f0:8", ["const:b3cd18:8", "const:4:8"]]
- 00b3cd18 ["CALL", null, ["callee:00be00a0:8"]]
+ 00b3cde0 ["INT_ADD", "register:40f0:8", ["const:b3cde0:8", "const:4:8"]]
+ 00b3cde0 ["CALL", null, ["callee:00be00a0:8"]]
- 00b3cd18 bytes b68c0294
+ 00b3cde0 bytes b08c0294
- 00b3cd2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:20:8"]]
- 00b3cd2c ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3cd2c ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b3cd2c ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b3cd2c bytes 092142a9
- 00b3cd30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3cd30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b3cd30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b3cd30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b3cd30 bytes 1801098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf6723ec56f923c0e0e0a2fac4c6464a"></a>

### [`00b3d140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d140.md) → [`00b3d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc30.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bdfff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md)
- 新版 呼出元 1件 [`00bdfce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfce0.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.47% / 新版 84.47%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3d17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d140.md#insn-00b3d17c) · [`00b3d1d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d140.md#insn-00b3d1d4) · [`00b3d1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d140.md#insn-00b3d1d8)
- 新版 [`00b3d244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md#insn-00b3d244)

~~~diff
- 00b3d17c ["INT_ADD", "register:40f0:8", ["const:b3d17c:8", "const:4:8"]]
- 00b3d17c ["CALL", null, ["callee:00be00a0:8"]]
+ 00b3d244 ["INT_ADD", "register:40f0:8", ["const:b3d244:8", "const:4:8"]]
+ 00b3d244 ["CALL", null, ["callee:00be00a0:8"]]
- 00b3d17c bytes 9d8b0294
+ 00b3d244 bytes 978b0294
- 00b3d1d4 ["INT_SUB", "register:4040:8", ["register:40b0:8", "register:40d0:8"]]
- 00b3d1d4 bytes c8021acb
- 00b3d1d8 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b3d1d8 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b3d1d8 ["INT_SEXT", "register:4048:8", ["tmp:1:4"]]
- 00b3d1d8 bytes 290380b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27cbedb7fd15b15497d58cdeab157892"></a>

### [`00b3d2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d2dc.md) → [`00b3d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md) _ZNSt6__ndk127__insertion_sort_incompleteIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEbT

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfcc0.md) · 呼出先 4件 [`00b3cec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cec8.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bdfff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md) [`00be0050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0050.md)
- 新版 呼出元 1件 [`00bdfd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd70.md) · 呼出先 4件 [`00b3cf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cf90.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md) [`00be0100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0100.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 74.29% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b3d3ec",
      "DATA",
      [
        "storage",
        "002f8584",
        "switchD_00b3d330::switchdataD_002f8584",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b3d3ec",
      "DATA",
      [
        "storage",
        "002f8584",
        "switchD_00b3d3f8::switchdataD_002f8584",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3d314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d2dc.md#insn-00b3d314) · [`00b3d320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d2dc.md#insn-00b3d320) · [`00b3d328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d2dc.md#insn-00b3d328)
- 新版 [`00b3d3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md#insn-00b3d3dc) · [`00b3d3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md#insn-00b3d3e8)

~~~diff
- 00b3d314 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3d314 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b3d314 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00b3d3dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b3d3dc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b3d3dc ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b3d314 bytes 48050054
+ 00b3d3dc bytes 48050054
- 00b3d320 ["COPY", "register:4050:8", ["const:b3d334:8"]]
+ 00b3d3e8 ["COPY", "register:4050:8", ["const:b3d3fc:8"]]
- 00b3d320 bytes aa000010
+ 00b3d3e8 bytes aa000010
- 00b3d328 ["INT_LEFT", "tmp:0:8", ["register:4058:8", "const:2:4"]]
- 00b3d328 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b3d328 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:1:8"]]
- 00b3d328 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:1:8"]]
- 00b3d328 bytes 4a090b8b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17ffe16880cbc270f38545b6f266936c"></a>

### [`00b3d67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d67c.md) → [`00b3d744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d744.md) _ZNSt6__ndk16__sortIRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEvT0_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd80.md) · 呼出先 7件 [`00b3e1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e1f0.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bdfc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc60.md) [`00bdfcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfcf0.md) [`00bdfd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd80.md)
- 新版 呼出元 1件 [`00bdfe30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe30.md) · 呼出先 7件 [`00b3e2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e2b8.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdfd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd10.md) [`00bdfda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfda0.md) [`00bdfe30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.35% / 新版 79.35%

CFGの説明率　旧版 36.73% / 新版 37.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3d6cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3d794"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3d6d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3d6cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3d6d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3dcf8"
      ]
    ],
    [
      "unmatched:00b3d7d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3db18"
      ]
    ]
  ],
  "added": [
    [
      "00b3d794",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b3d798",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3dcf8"
      ]
    ],
    [
      "00b3d8a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3db18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3d6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d67c.md#insn-00b3d6cc) · [`00b3d6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d67c.md#insn-00b3d6d0) · [`00b3d794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d67c.md#insn-00b3d794)

~~~diff
- 00b3d6cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b3d6cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 00b3d6cc bytes f81300f9
- 00b3d6d0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3d6d0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b3d6d0 ["CBRANCH", null, ["local:b62:8", "tmp:1:1"]]
- 00b3d6d0 bytes 092b0054
- 00b3d794 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b3d794 ["INT_ADD", "register:40d0:8", ["register:40d0:8", "const:4:8"]]
- 00b3d794 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b3d794 ["INT_ZEXT", "register:4098:8", ["tmp:1:4"]]
- 00b3d794 bytes 534740b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ba9f12b8c54021223cef1f7cf4e4c2"></a>

### [`00b3ddc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3ddc0.md) → [`00b3de88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3de88.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0020.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00be00d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00d0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.27% / 新版 80.27%

CFGの説明率　旧版 19.05% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3df64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3e02c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3de88"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3de88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3ddc0.md#insn-00b3de88) · [`00b3de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3ddc0.md#insn-00b3de90) · [`00b3df28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3ddc0.md#insn-00b3df28)

~~~diff
- 00b3de88 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b3de88 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3de88 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b3de88 ["INT_ZEXT", "register:40a0:8", ["tmp:0:4"]]
- 00b3de88 bytes 5401891a
- 00b3de90 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3de90 ["COPY", "tmp:1:4", ["register:40e0:4"]]
- 00b3de90 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3de90 ["COPY", "tmp:1:4", ["register:4098:4"]]
- 00b3de90 bytes 8233931a
- 00b3df28 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3df28 ["COPY", "tmp:1:4", ["register:40b8:4"]]
- 00b3df28 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3df28 ["COPY", "tmp:1:4", ["register:4098:4"]]
- 00b3df28 bytes e232931a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31ab73cbfeee380c23775282e0adc0c8"></a>

### [`00b3e00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e00c.md) → [`00b3e0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e0d4.md) _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0080.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0020.md)
- 新版 呼出元 1件 [`00be0130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0130.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00d0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.16% / 新版 61.16%

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
      "site": "00b3e020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3e020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3e0e8"
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
      "unmatched:00b3e020",
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
      "00b3e0e8",
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

- 旧版 [`00b3e020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e00c.md#insn-00b3e020) · [`00b3e0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e00c.md#insn-00b3e0e8)
- 新版 [`00b3e0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e0d4.md#insn-00b3e0e8)

~~~diff
- 00b3e020 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b3e020 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b3e020 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b3e020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3e020 bytes fd7b05a9
- 00b3e0e8 ["INT_SUB", "register:4058:8", ["register:4048:8", "register:4058:8"]]
- 00b3e0e8 bytes 2b010bcb
+ 00b3e0e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b3e0e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b3e0e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
+ 00b3e0e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b3e0e8 bytes fd7b05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c481965e733f92425f2c61699ea2ec9"></a>

### [`00b3e468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e468.md) → [`00b3e530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e530.md) _ZNSt6__ndk118__insertion_sort_3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS5_EEEEvT0_SB_T

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc60.md) · 呼出先 2件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00be0020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0020.md)
- 新版 呼出元 1件 [`00bdfd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd10.md) · 呼出先 2件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00be00d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.02% / 新版 66.02%

CFGの説明率　旧版 12.50% / 新版 19.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3e46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3e46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3e470"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3e46c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3e470",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3e474",
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
      "00b3e534",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b3e538",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3e53c",
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

- 旧版 [`00b3e46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e468.md#insn-00b3e46c) · [`00b3e470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e468.md#insn-00b3e470) · [`00b3e474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e468.md#insn-00b3e474)

~~~diff
- 00b3e46c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b3e46c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b3e46c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b3e46c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3e46c bytes fc6f01a9
- 00b3e470 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b3e470 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b3e470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3e470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3e470 bytes fa6702a9
- 00b3e474 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3e474 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3e474 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b3e474 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3e474 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f022c635f8021d210df74faab57f6ff"></a>

### [`00b3eca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eca0.md) → [`00b3ed68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__append_forward_unsafeIPKcEERS5_T_SA_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbf0.md) · 呼出先 6件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md)
- 新版 呼出元 1件 [`00bdfca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfca0.md) · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 79.10% / 新版 77.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ee68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ee68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3ef30"
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
      "unmatched:00b3ee68",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3ef08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3eff0"
      ]
    ]
  ],
  "added": [
    [
      "00b3ef30",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b3efd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3eff0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ee68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eca0.md#insn-00b3ee68) · [`00b3ef08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3eca0.md#insn-00b3ef08)
- 新版 [`00b3ef30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3ed68.md#insn-00b3ef30)

~~~diff
- 00b3ee68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b3ee68 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b3ee68 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00b3ee68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3ee68 bytes e86300a9
- 00b3ef08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3ef08 ["CBRANCH", null, ["local:b41:8", "tmp:0:1"]]
- 00b3ef08 bytes 01010054
+ 00b3ef30 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b3ef30 ["COPY", "tmp:1:8", ["register:40c0:8"]]
+ 00b3ef30 ["COPY", "tmp:2:8", ["register:8:8"]]
+ 00b3ef30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b3ef30 bytes e86300a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1af5e7a099ebe20d63398d903df91705"></a>

### [`00b3f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f044.md) → [`00b3f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f10c.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_valu

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbd0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 75.00% / 新版 72.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f078"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f07c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3f140"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f044.md#insn-00b3f078) · [`00b3f07c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f044.md#insn-00b3f07c)
- 新版 [`00b3f140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f10c.md#insn-00b3f140)

~~~diff
- 00b3f078 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f078 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f078 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3f078 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b3f078 bytes 7601899a
- 00b3f07c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3f07c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b3f07c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f07c ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b3f07c bytes 5515819a
+ 00b3f140 ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00b3f140 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b3f140 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b3f140 ["COPY", "register:40b0:8", ["tmp:0:8"]]
+ 00b3f140 bytes 7601899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ef19522971a9e68fc59e68df304c04d"></a>

### [`00b3f158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f158.md) → [`00b3f220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f220.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfee0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdff90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 56.00% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f218"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f220"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3f2e0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f158.md#insn-00b3f218) · [`00b3f220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f158.md#insn-00b3f220) · [`00b3f268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f158.md#insn-00b3f268)

~~~diff
- 00b3f218 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f218 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f218 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3f218 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b3f218 bytes 77018a9a
- 00b3f220 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b3f220 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3f220 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f220 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b3f220 bytes e232969a
- 00b3f268 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3f268 ["RETURN", null, ["register:0:8"]]
- 00b3f268 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-462ad20ce515ee52eeef5f4877913b52"></a>

### [`00b3f26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f26c.md) → [`00b3f334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f334.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfed0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdff80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff80.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 86.67% / 新版 83.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f31c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3f3e4"
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
      "unmatched:00b3f31c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f3f8"
      ]
    ]
  ],
  "added": [
    [
      "00b3f3e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f3f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f26c.md#insn-00b3f31c) · [`00b3f294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f26c.md#insn-00b3f294)
- 新版 [`00b3f3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f334.md#insn-00b3f3e4) · [`00b3f35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f334.md#insn-00b3f35c)

~~~diff
- 00b3f31c ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00b3f31c bytes a2000054
+ 00b3f3e4 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
+ 00b3f3e4 bytes a2000054
- 00b3f294 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b3f294 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b3f35c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00b3f35c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b3f294 bytes 570600b4
+ 00b3f35c bytes 570600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eba07820c199d52d3e950a8e211128f3"></a>

### [`00b3f38c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f38c.md) → [`00b3f454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f454.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_co

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdfb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb90.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc40.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b3f3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f38c.md#insn-00b3f3e0) · [`00b3f424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f38c.md#insn-00b3f424) · [`00b3f46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f38c.md#insn-00b3f46c)
- 新版 [`00b3f4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f454.md#insn-00b3f4ec) · [`00b3f534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f454.md#insn-00b3f534)

~~~diff
- 00b3f3e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b3f3e0 ["INT_ZEXT", "register:4040:8", ["tmp:0:1"]]
- 00b3f3e0 bytes e8a79f1a
- 00b3f424 ["INT_ADD", "register:40f0:8", ["const:b3f424:8", "const:4:8"]]
- 00b3f424 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3f4ec ["INT_ADD", "register:40f0:8", ["const:b3f4ec:8", "const:4:8"]]
+ 00b3f4ec ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3f424 bytes 376f0294
+ 00b3f4ec bytes 316f0294
- 00b3f46c ["INT_ADD", "register:40f0:8", ["const:b3f46c:8", "const:4:8"]]
- 00b3f46c ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b3f534 ["INT_ADD", "register:40f0:8", ["const:b3f534:8", "const:4:8"]]
+ 00b3f534 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b3f46c bytes 256f0294
+ 00b3f534 bytes 1f6f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f8664bb4f920fef6af12887dfcb82dc"></a>

### [`00b3f6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f6c4.md) → [`00b3f78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f78c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfe40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe40.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfef0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.06% / 新版 84.06%

CFGの説明率　旧版 69.23% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f73c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3f748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f7cc"
      ]
    ]
  ],
  "added": [
    [
      "00b3f810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3f7cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f6c4.md#insn-00b3f6f8) · [`00b3f6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f6c4.md#insn-00b3f6fc) · [`00b3f73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f6c4.md#insn-00b3f73c)

~~~diff
- 00b3f6f8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f6f8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f6f8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3f6f8 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b3f6f8 bytes 7601899a
- 00b3f6fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3f6fc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b3f6fc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b3f6fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b3f6fc bytes 5515819a
- 00b3f73c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3f73c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3f73c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3f73c ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b3f73c bytes 78018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbf9a4c52c882bb07b1890d7d88be1a6"></a>

### [`00b40790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40790.md) → [`00b40858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40858.md) _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc20.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdfcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfcd0.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.98% / 新版 95.98%

CFGの説明率　旧版 82.05% / 新版 82.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b407a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b407a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40868"
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
      "unmatched:00b407a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b407b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40a90"
      ]
    ]
  ],
  "added": [
    [
      "00b40868",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40a90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b407a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40790.md#insn-00b407a0) · [`00b407b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40790.md#insn-00b407b8) · [`00b40868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40790.md#insn-00b40868)
- 新版 [`00b40930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40858.md#insn-00b40930)

~~~diff
- 00b407a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b407a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b407a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b407a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b407a0 bytes fd7b04a9
- 00b407b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b407b8 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b407b8 bytes 81100054
- 00b40868 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b40868 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b40868 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b40868 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b40930 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00b40930 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b40930 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b40930 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b40868 bytes 29fd0736
+ 00b40930 bytes 29fd0736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a87bae1266a80f14906e1d3f8512f73a"></a>

### [`00b40ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40ce0.md) → [`00b40da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40da8.md) _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdffa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffa0.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00be0050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0050.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.85% / 新版 76.85%

CFGの説明率　旧版 44.44% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40de0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40de4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40df4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b40d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40e34"
      ]
    ],
    [
      "unmatched:00b40d68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40f4c"
      ]
    ],
    [
      "unmatched:00b40e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40e94"
      ]
    ]
  ],
  "added": [
    [
      "00b40e20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40e34"
      ]
    ],
    [
      "00b40e30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40f4c"
      ]
    ],
    [
      "00b40edc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40e94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40ce0.md#insn-00b40d58) · [`00b40d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40ce0.md#insn-00b40d64) · [`00b40d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40ce0.md#insn-00b40d68)

~~~diff
- 00b40d58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b40d58 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b40d58 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b40d58 bytes a8000054
- 00b40d64 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b40d64 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b40d64 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b40d64 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b40d64 bytes 1531899a
- 00b40d68 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b40d68 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b40d68 bytes f50800b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bda02684a222ffda3fdb31850683691"></a>

### [`00b40e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40e90.md) → [`00b40f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md) FUN_00b40f58

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md) [`00b1cd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 2件 [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 70.00% / 新版 61.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40f7c",
      "DATA",
      [
        "storage",
        "002f8596",
        "switchD_00b40ebc::switchdataD_002f8596",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b40f7c",
      "DATA",
      [
        "storage",
        "002f8596",
        "switchD_00b40f84::switchdataD_002f8596",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40e90.md#insn-00b40ea0) · [`00b40eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40e90.md#insn-00b40eb0) · [`00b40ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40e90.md#insn-00b40ec8)
- 新版 [`00b40f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md#insn-00b40f68) · [`00b40f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md#insn-00b40f78) · [`00b40f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md#insn-00b40f90)

~~~diff
- 00b40ea0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b40ea0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b40ea0 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00b40f68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b40f68 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b40f68 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00b40ea0 bytes 68010054
+ 00b40f68 bytes 68010054
- 00b40eb0 ["COPY", "register:4050:8", ["const:b40ec0:8"]]
+ 00b40f78 ["COPY", "register:4050:8", ["const:b40f88:8"]]
- 00b40eb0 bytes 8a000010
+ 00b40f78 bytes 8a000010
- 00b40ec8 ["BRANCH", null, ["local:b12:8"]]
+ 00b40f90 ["BRANCH", null, ["local:b11:8"]]
- 00b40ec8 bytes 13000014
+ 00b40f90 bytes 13000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cec7e830d7b74020a550efbc387e94c9"></a>

### [`00b41118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41118.md) → [`00b411e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b411e0.md) _ZNSt6__ndk16vectorIN11flatbuffers5ValueENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEvDpOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff60.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00be0010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0010.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.15% / 新版 83.15%

CFGの説明率　旧版 34.38% / 新版 34.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4119c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b41158",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41240"
      ]
    ],
    [
      "unmatched:00b41168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4133c"
      ]
    ]
  ],
  "added": [
    [
      "00b41220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41240"
      ]
    ],
    [
      "00b41230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4133c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b41158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41118.md#insn-00b41158) · [`00b41164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41118.md#insn-00b41164) · [`00b41168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41118.md#insn-00b41168)

~~~diff
- 00b41158 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b41158 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b41158 bytes 03010054
- 00b41164 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b41164 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b41164 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b41164 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b41164 bytes 1631899a
- 00b41168 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b41168 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00b41168 bytes 760800b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5cb1afe142035cf1f5ed100ea7ffec"></a>

### [`00b41604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41604.md) → [`00b416cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b416cc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff10.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdffc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffc0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 61.76% / 新版 61.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41604"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41608"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b41604",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b41608",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4160c",
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
      "00b416cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b416d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b416d4",
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

- 旧版 [`00b41604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41604.md#insn-00b41604) · [`00b41608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41604.md#insn-00b41608) · [`00b4160c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41604.md#insn-00b4160c)

~~~diff
- 00b41604 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b41604 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b41604 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b41604 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b41604 bytes fc6fbaa9
- 00b41608 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b41608 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b41608 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b41608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b41608 bytes fa6701a9
- 00b4160c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4160c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4160c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4160c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4160c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74960cb3ed32befcd3dab2655fce6fd5"></a>

### [`00b42b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42b0c.md) → [`00b42bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42bd4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfea0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 89.86% / 新版 89.86%

CFGの説明率　旧版 59.26% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42b40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42b58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b42c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b42b4c"
      ]
    ],
    [
      "00b42c74",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b42b4c"
      ]
    ]
  ],
  "added": [
    [
      "00b42c58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42c14"
      ]
    ],
    [
      "00b42c74",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42c14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42b0c.md#insn-00b42b40) · [`00b42b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42b0c.md#insn-00b42b44) · [`00b42b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42b0c.md#insn-00b42b58)

~~~diff
- 00b42b40 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b42b40 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b42b40 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b42b40 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b42b40 bytes 7601899a
- 00b42b44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b42b44 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b42b44 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b42b44 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b42b44 bytes 5515819a
- 00b42b58 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b42b58 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b42b58 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00b42b58 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00b42b58 bytes 00219f5a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee9a8a8ae221e288f5f9bdebb29c892"></a>

### [`00b42d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42d80.md) → [`00b42e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42e48.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfe20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe20.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfed0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 27.27% / 新版 32.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42db8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42dcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b42dbc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42eac"
      ]
    ],
    [
      "unmatched:00b42de0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42eec"
      ]
    ],
    [
      "00b42ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b42dc0"
      ]
    ]
  ],
  "added": [
    [
      "00b42e84",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42eac"
      ]
    ],
    [
      "00b42ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42eec"
      ]
    ],
    [
      "00b42ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b42e88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42d80.md#insn-00b42db4) · [`00b42db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42d80.md#insn-00b42db8) · [`00b42dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42d80.md#insn-00b42dcc)

~~~diff
- 00b42db4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b42db4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b42db4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b42db4 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b42db4 bytes 7601899a
- 00b42db8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b42db8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b42db8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b42db8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b42db8 bytes 5515819a
- 00b42dcc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b42dcc ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b42dcc ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00b42dcc ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00b42dcc bytes 00219f5a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-229d30761e2ae2909841dc7a48decae9"></a>

### [`00b42e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42e94.md) → [`00b42f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42f5c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfe10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe10.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfec0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 68.75% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42ed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b42f14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b42f44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43020"
      ]
    ]
  ],
  "added": [
    [
      "00b4300c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43020"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b42ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42e94.md#insn-00b42ed4) · [`00b42f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42e94.md#insn-00b42f0c) · [`00b42f14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42e94.md#insn-00b42f14)

~~~diff
- 00b42ed4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b42ed4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b42ed4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b42ed4 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b42ed4 bytes 7801899a
- 00b42f0c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b42f0c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b42f0c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b42f0c ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 00b42f0c bytes 3901889a
- 00b42f14 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b42f14 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b42f14 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b42f14 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b42f14 bytes 3633989a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4773f96b3b8506f78187a3cda3dabd98"></a>

### [`00b43650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43650.md) → [`00b43718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43718.md) FUN_00b43718

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b42fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42fb4.md) [`00b438b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b438b4.md) · 呼出先 1件 [`00be00b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00b0.md)
- 新版 呼出元 2件 [`00b4307c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4307c.md) [`00b4397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4397c.md) · 呼出先 1件 [`00be0160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0160.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 50.00% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b436f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b436f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b437bc"
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
      "unmatched:00b4369c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b43764",
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

- 旧版 [`00b4369c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43650.md#insn-00b4369c) · [`00b436f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43650.md#insn-00b436f4) · [`00b436f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43650.md#insn-00b436f8)

~~~diff
- 00b4369c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b4369c ["INT_ADD", "register:40f0:8", ["const:b4369c:8", "const:4:8"]]
- 00b4369c ["CALLIND", null, ["register:0:8"]]
- 00b4369c bytes 20013fd6
- 00b436f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b436f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b436f4 bytes 880200f9
- 00b436f8 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b436f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b436f8 bytes e90200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab0a4bcc431067c6914b89566e4c76d"></a>

### [`00b43758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43758.md) → [`00b43820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43820.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfc90.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdfd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd40.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 83.87% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43758"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4375c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4375c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43758",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4375c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43760",
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
      "00b43820",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b43824",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b43828",
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

- 旧版 [`00b43758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43758.md#insn-00b43758) · [`00b4375c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43758.md#insn-00b4375c) · [`00b43760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43758.md#insn-00b43760)

~~~diff
- 00b43758 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b43758 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b43758 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b43758 bytes f90f1bf8
- 00b4375c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4375c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4375c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4375c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4375c bytes f85f01a9
- 00b43760 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b43760 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b43760 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b43760 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b43760 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34394eea8d34cecca4dcbeb7cc14c067"></a>

### [`00b438b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b438b4.md) → [`00b4397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4397c.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd20.md) · 呼出先 2件 [`00b43650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43650.md) [`00be00b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00b0.md)
- 新版 呼出元 1件 [`00bdfdd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfdd0.md) · 呼出先 2件 [`00b43718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43718.md) [`00be0160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0160.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.60% / 新版 93.60%

CFGの説明率　旧版 68.33% / 新版 65.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43aa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b43b68"
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
      "00b439bc",
      "DATA",
      [
        "storage",
        "002f85c2",
        "switchD_00b43900::switchdataD_002f85c2",
        "byte"
      ]
    ],
    [
      "unmatched:00b43adc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43c00"
      ]
    ],
    [
      "unmatched:00b43b60",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43c04"
      ]
    ]
  ],
  "added": [
    [
      "00b439bc",
      "DATA",
      [
        "storage",
        "002f85c2",
        "switchD_00b439c8::switchdataD_002f85c2",
        "byte"
      ]
    ],
    [
      "00b43ba4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43c00"
      ]
    ],
    [
      "00b43c28",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b43c04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b438b4.md#insn-00b43a40) · [`00b43a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b438b4.md#insn-00b43a44) · [`00b43aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b438b4.md#insn-00b43aa0)
- 新版 [`00b43b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4397c.md#insn-00b43b0c)

~~~diff
- 00b43a40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b43a40 ["INT_ADD", "register:40f0:8", ["const:b43a40:8", "const:4:8"]]
- 00b43a40 ["CALLIND", null, ["register:0:8"]]
- 00b43a40 bytes 00013fd6
- 00b43a44 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b43a44 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b43a44 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b43a44 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b43b0c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b43b0c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b43b0c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b43b0c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b43a44 bytes 00030036
+ 00b43b0c bytes 00030036
- 00b43aa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b43aa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b43aa0 bytes 6082803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b81d480b4dac086e58c6a116dfee18e"></a>

### [`00b43b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43b64.md) → [`00b43c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43c2c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfe00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe00.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfeb0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 87.50% / 新版 91.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b43c64"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b43b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43b64.md#insn-00b43b9c) · [`00b43b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43b64.md#insn-00b43b80)
- 新版 [`00b43c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43c2c.md#insn-00b43c64) · [`00b43c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43c2c.md#insn-00b43c48)

~~~diff
- 00b43b9c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b43b9c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b43b9c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43b9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b43b9c bytes 5515819a
+ 00b43c64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b43c64 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b43c64 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b43c64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
+ 00b43c64 bytes 5515819a
- 00b43b80 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b43b80 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00b43c48 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00b43c48 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b43b80 bytes f70600b4
+ 00b43c48 bytes f70600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83bbd71be43849ac7efcc86f5b019659"></a>

### [`00b43c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43c78.md) → [`00b43d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43d40.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfdf0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfea0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 80.65% / 新版 80.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43cbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b43d84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43d94"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b43cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43c78.md#insn-00b43cbc) · [`00b43d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43c78.md#insn-00b43d94)
- 新版 [`00b43d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43d40.md#insn-00b43d84)

~~~diff
- 00b43cbc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b43cbc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b43cbc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43cbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00b43cbc bytes 5515829a
+ 00b43d84 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b43d84 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b43d84 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b43d84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
+ 00b43d84 bytes 5515829a
- 00b43d94 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b43d94 ["RETURN", null, ["register:0:8"]]
- 00b43d94 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e530091f8bbec62c6352da0c4154eca0"></a>

### [`00b43eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43eac.md) → [`00b43f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43f74.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfeb0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdff60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff60.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 86.67% / 新版 83.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b44044"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b43f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43eac.md#insn-00b43f7c) · [`00b43ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43eac.md#insn-00b43ed4)
- 新版 [`00b44044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43f74.md#insn-00b44044) · [`00b43f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b43f74.md#insn-00b43f9c)

~~~diff
- 00b43f7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b43f7c ["COPY", "tmp:1:8", ["register:40e0:8"]]
- 00b43f7c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b43f7c ["INT_ADD", "tmp:1:8", ["register:40d0:8", "const:1:8"]]
- 00b43f7c bytes 80179a9a
+ 00b44044 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b44044 ["COPY", "tmp:1:8", ["register:40e0:8"]]
+ 00b44044 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b44044 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "const:1:8"]]
+ 00b44044 bytes 80179a9a
- 00b43ed4 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00b43ed4 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b43f9c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00b43f9c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b43ed4 bytes 570600b4
+ 00b43f9c bytes 570600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c6376141bb73cc0763a2843d744077a"></a>

### [`00b43fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43fcc.md) → [`00b44094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44094.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdfe80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe80.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff30.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44044"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4404c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44050"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b440d4"
      ]
    ]
  ],
  "added": [
    [
      "00b44118",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b440d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43fcc.md#insn-00b44044) · [`00b4404c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43fcc.md#insn-00b4404c) · [`00b44050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b43fcc.md#insn-00b44050)

~~~diff
- 00b44044 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b44044 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b44044 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b44044 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b44044 bytes 78018a9a
- 00b4404c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b4404c ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b4404c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b4404c ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 00b4404c bytes c232989a
- 00b44050 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00b44050 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b44050 bytes e2fdffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a00f10f8ff2343175e9b461c007a717d"></a>

### [`00b440e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b440e0.md) → [`00b441a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b441a8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfe50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe50.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdff00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff00.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 83.87% / 新版 83.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44120"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44124"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b441e8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b44120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b440e0.md#insn-00b44120) · [`00b44124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b440e0.md#insn-00b44124)
- 新版 [`00b441e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b441a8.md#insn-00b441e8)

~~~diff
- 00b44120 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b44120 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b44120 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b44120 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00b44120 bytes 7801899a
- 00b44124 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b44124 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b44124 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b44124 ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00b44124 bytes 5515829a
+ 00b441e8 ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00b441e8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b441e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b441e8 ["COPY", "register:40c0:8", ["tmp:0:8"]]
+ 00b441e8 bytes 7801899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5512f1579e54a3fc3ad8f288806a9fce"></a>

### [`00b44480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44480.md) → [`00b44548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44548.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_value

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff20.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdffd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdffd0.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44528"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44540"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44640"
      ]
    ]
  ],
  "added": [
    [
      "00b445f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44640"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44480.md#insn-00b44528) · [`00b44540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44480.md#insn-00b44540) · [`00b44548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44480.md#insn-00b44548)

~~~diff
- 00b44528 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b44528 bytes 80020054
- 00b44540 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b44540 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b44540 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b44540 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b44540 bytes 77018a9a
- 00b44548 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b44548 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b44548 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b44548 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b44548 bytes e232969a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d691aa9c838a545c8a41d8989a9b5650"></a>

### [`00b446b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b446b4.md) → [`00b4477c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b4477c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRS6_EEEvDpOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdff80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff80.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md)
- 新版 呼出元 1件 [`00be0030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0030.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 37.04% / 新版 30.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44768"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4476c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44770"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b446ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448c8"
      ]
    ],
    [
      "unmatched:00b44728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448c0"
      ]
    ],
    [
      "unmatched:00b4475c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44858"
      ]
    ]
  ],
  "added": [
    [
      "00b447b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448c8"
      ]
    ],
    [
      "00b447f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448c0"
      ]
    ],
    [
      "00b44824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44858"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b446ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b446b4.md#insn-00b446ec) · [`00b44728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b446b4.md#insn-00b44728) · [`00b4475c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b446b4.md#insn-00b4475c)

~~~diff
- 00b446ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b446ec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b446ec ["CBRANCH", null, ["local:b19:8", "tmp:1:1"]]
- 00b446ec bytes a8080054
- 00b44728 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b44728 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b44728 bytes 960600b4
- 00b4475c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b4475c bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d402cd5c4b89b21b523d7ce89acf6964"></a>

### [`00b44e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44e50.md) → [`00b44f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44f18.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be00c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be0170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0170.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 96.91% / 新版 96.91%

CFGの説明率　旧版 53.85% / 新版 51.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b44f4c"
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
      "unmatched:00b44e84",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b44f48",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44f4c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b45010",
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

- 旧版 [`00b44e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44e50.md#insn-00b44e84) · [`00b44f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44e50.md#insn-00b44f48)
- 新版 [`00b44f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44f18.md#insn-00b44f4c)

~~~diff
- 00b44e84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44e84 ["INT_ADD", "register:40f0:8", ["const:b44e84:8", "const:4:8"]]
- 00b44e84 ["CALLIND", null, ["register:0:8"]]
- 00b44e84 bytes 00013fd6
- 00b44f48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b44f48 ["INT_ADD", "register:40f0:8", ["const:b44f48:8", "const:4:8"]]
- 00b44f48 ["CALLIND", null, ["register:0:8"]]
- 00b44f48 bytes 00013fd6
+ 00b44f4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44f4c ["INT_ADD", "register:40f0:8", ["const:b44f4c:8", "const:4:8"]]
+ 00b44f4c ["CALLIND", null, ["register:0:8"]]
+ 00b44f4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d3ecff2610e0e2e73a22b9d5fae0a0"></a>

### [`00b44fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44fd4.md) → [`00b4509c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b4509c.md) FUN_00b4509c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b44938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44938.md) [`00b45238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b45238.md) · 呼出先 1件 [`00be00c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00c0.md)
- 新版 呼出元 2件 [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md) [`00b45300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45300.md) · 呼出先 1件 [`00be0170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0170.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 53.85% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b450a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45120"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b45058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44fd4.md#insn-00b45058) · [`00b450a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44fd4.md#insn-00b450a0)
- 新版 [`00b45120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b4509c.md#insn-00b45120)

~~~diff
- 00b45058 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b45058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b45058 bytes 090300f9
- 00b450a0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b450a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b450a0 bytes a80200f9
+ 00b45120 ["COPY", "tmp:0:8", ["register:40c0:8"]]
+ 00b45120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00b45120 bytes 090300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31b56b1f55e5490a00ce29d5b24e9222"></a>

### [`00b450dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b450dc.md) → [`00b451a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b451a4.md) _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfca0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdfd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfd50.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 70.00% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45208"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45128"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45128",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00b45208",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b451f0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00b452d0",
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

- 旧版 [`00b45128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b450dc.md#insn-00b45128) · [`00b45140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b450dc.md#insn-00b45140)
- 新版 [`00b451f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b451a4.md#insn-00b451f0)

~~~diff
- 00b45128 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b45128 ["INT_ADD", "register:40f0:8", ["const:b45128:8", "const:4:8"]]
- 00b45128 ["CALLIND", null, ["register:0:8"]]
- 00b45128 bytes 20013fd6
- 00b45140 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b45140 bytes 880200f9
+ 00b451f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b451f0 ["INT_ADD", "register:40f0:8", ["const:b451f0:8", "const:4:8"]]
+ 00b451f0 ["CALLIND", null, ["register:0:8"]]
+ 00b451f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489d4de6ea246bc3df5d3a58920bc7ef"></a>

### [`00b45b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b45b34.md) → [`00b45bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b45/00b45bfc.md) _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be00a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be0150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0150.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.66% / 新版 88.66%

CFGの説明率　旧版 27.27% / 新版 32.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45b38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45b34",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45b38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45b3c",
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
      "00b45bfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b45c00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b45c04",
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

- 旧版 [`00b45b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b45b34.md#insn-00b45b34) · [`00b45b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b45b34.md#insn-00b45b38) · [`00b45b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b45/00b45b34.md#insn-00b45b3c)

~~~diff
- 00b45b34 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b45b34 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b45b34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b45b34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45b34 bytes f85fbca9
- 00b45b38 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b45b38 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b45b38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45b38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45b38 bytes f65701a9
- 00b45b3c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45b3c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45b3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b45b3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45b3c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd6cd27ee46959467eff5e95a7d91e7c"></a>

### [`00b4636c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b4636c.md) → [`00b46434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46434.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbe0.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bdfc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 37.04% / 新版 43.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4636c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4636c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4636c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46370",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b46374",
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
      "00b46434",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b46438",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4643c",
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

- 旧版 [`00b4636c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b4636c.md#insn-00b4636c) · [`00b46370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b4636c.md#insn-00b46370) · [`00b46374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b4636c.md#insn-00b46374)

~~~diff
- 00b4636c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4636c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4636c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b4636c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4636c bytes f85fbca9
- 00b46370 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b46370 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b46370 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b46370 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46370 bytes f65701a9
- 00b46374 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b46374 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b46374 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b46374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b46374 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a952f7448dc26c1a226b71be80d722"></a>

### [`00b46db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46db4.md) → [`00b46e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e7c.md) _ZN11flatbuffers8LoadFileEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf9b0.md) · 呼出先 1件 [`00b46650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46650.md)
- 新版 呼出元 1件 [`00bdfa60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa60.md) · 呼出先 1件 [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46db8",
      "READ",
      [
        "storage",
        "00c246c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b46dc0",
      "COMPUTED_JUMP",
      [
        "mapped_function",
        "00b46718"
      ]
    ]
  ],
  "added": [
    [
      "00b46e80",
      "READ",
      [
        "storage",
        "00c24778",
        null,
        "pointer"
      ]
    ],
    [
      "00b46e88",
      "COMPUTED_JUMP",
      [
        "mapped_function",
        "00b46718"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46db4.md#insn-00b46db4) · [`00b46db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46db4.md#insn-00b46db8) · [`00b46dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46db4.md#insn-00b46dbc)

~~~diff
- 00b46db4 ["COPY", "register:4040:8", ["const:c24000:8"]]
- 00b46db4 bytes e80600d0
- 00b46db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:6c8:8"]]
- 00b46db8 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46db8 bytes 036543f9
- 00b46dbc ["INT_AND", "tmp:0:4", ["register:4008:4", "const:1:4"]]
- 00b46dbc ["INT_ZEXT", "register:4008:8", ["tmp:0:4"]]
- 00b46dbc bytes 21000012
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17c71a7af8dbfb54d2e4fd51bee3fb69"></a>

### [`00b46dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46dd0.md) → [`00b46e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e98.md) _ZN11flatbuffers19SetLoadFileFunctionEPFbPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b46650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46dec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46eb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b46de4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b46dd8",
      "READ",
      [
        "storage",
        "00c246c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b46ddc",
      "READ",
      [
        "storage",
        "00c1b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b46de8",
      "DATA",
      [
        "storage",
        "00b46650",
        "_ZN11flatbuffers11LoadFileRawEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46ea0",
      "READ",
      [
        "storage",
        "00c24778",
        null,
        "pointer"
      ]
    ],
    [
      "00b46ea4",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b46eb0",
      "DATA",
      [
        "storage",
        "00b46718",
        "_ZN11flatbuffers11LoadFileRawEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46dd0.md#insn-00b46de4) · [`00b46dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46dd0.md#insn-00b46dec) · [`00b46df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46dd0.md#insn-00b46df0)

~~~diff
- 00b46de4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b46de4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b46de4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b46de4 ["COPY", "register:4050:8", ["tmp:0:8"]]
- 00b46de4 bytes 4a01809a
- 00b46dec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6c8:8"]]
- 00b46dec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b46dec bytes 2a6503f9
- 00b46df0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b46df0 ["RETURN", null, ["register:0:8"]]
- 00b46df0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb29a00febfec91b941dd807450b6ba1"></a>

### [`00b47088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47088.md) → [`00b47150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47150.md) FUN_00b47150

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md) [`00be01a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

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
      "site": "00b470a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b470ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47170"
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
      "unmatched:00b47098",
      "READ",
      [
        "storage",
        "00c1afd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b470a8",
      "DATA",
      [
        "storage",
        "00c113b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b470ac",
      "DATA",
      [
        "storage",
        "00c113d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b47160",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00b47170",
      "DATA",
      [
        "storage",
        "00c11460",
        null,
        "pointer"
      ]
    ],
    [
      "00b47174",
      "DATA",
      [
        "storage",
        "00c11488",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b470a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47088.md#insn-00b470a8) · [`00b470ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47088.md#insn-00b470ac)
- 新版 [`00b47170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47150.md#insn-00b47170)

~~~diff
- 00b470a8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b470a8 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b470a8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b470a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b470a8 bytes 098400f8
- 00b470ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b470ac ["INT_ADD", "register:4098:8", ["register:4098:8", "const:b0:8"]]
- 00b470ac ["STORE", null, ["const:1b1:8", "register:4098:8", "tmp:0:8"]]
- 00b470ac bytes 680e0bf8
+ 00b47170 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b47170 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b47170 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00b47170 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b47170 bytes 098400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2679bcb06c6f02335d123a0dd7042a25"></a>

### [`00b470c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b470c4.md) → [`00b4718c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4718c.md) _ZN11flatbuffers14StripExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 10.00% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b470dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b470e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b470e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b470e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b471dc"
      ]
    ]
  ],
  "added": [
    [
      "00b471ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b471dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b470dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b470c4.md#insn-00b470dc) · [`00b470e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b470c4.md#insn-00b470e0) · [`00b470e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b470c4.md#insn-00b470e4)

~~~diff
- 00b470dc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b470dc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b470dc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b470dc ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b470dc bytes 6301899a
- 00b470e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b470e0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b470e0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b470e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b470e0 bytes 4815819a
- 00b470e4 ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
- 00b470e4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b470e4 bytes 830100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea333bc87e37a5a0bad4456853486db9"></a>

### [`00b47118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47118.md) → [`00b471e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b471e0.md) _ZN11flatbuffers12GetExtensionERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 29.17% / 新版 29.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47130"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47134"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47138"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47234"
      ]
    ],
    [
      "unmatched:00b4713c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47234"
      ]
    ],
    [
      "unmatched:00b47150",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4713c"
      ]
    ]
  ],
  "added": [
    [
      "00b47200",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47234"
      ]
    ],
    [
      "00b47204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47234"
      ]
    ],
    [
      "00b47218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47204"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47118.md#insn-00b47130) · [`00b47134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47118.md#insn-00b47134) · [`00b47138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47118.md#insn-00b47138)

~~~diff
- 00b47130 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b47130 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b47130 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b47130 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b47130 bytes 6801899a
- 00b47134 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b47134 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b47134 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b47134 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b47134 bytes 4915819a
- 00b47138 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b47138 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b47138 bytes a80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b36c8a46aefa14bdd86425f0c0d6f76"></a>

### [`00b47220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47220.md) → [`00b472e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b472e8.md) _ZN11flatbuffers13StripFileNameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 15.79% / 新版 10.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47334",
      "PARAM",
      [
        "storage",
        "002987ed",
        null,
        null
      ]
    ],
    [
      "unmatched:00b472c0",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b472c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde6f0"
      ]
    ]
  ],
  "added": [
    [
      "00b47334",
      "PARAM",
      [
        "storage",
        "0029887a",
        null,
        null
      ]
    ],
    [
      "00b47388",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47390",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde6f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47220.md#insn-00b47258) · [`00b4725c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47220.md#insn-00b4725c) · [`00b47270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47220.md#insn-00b47270)
- 新版 [`00b47324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b472e8.md#insn-00b47324) · [`00b47338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b472e8.md#insn-00b47338)

~~~diff
- 00b47258 ["COPY", "tmp:0:8", ["const:7ed:8"]]
- 00b47258 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00b47258 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00b47258 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00b47258 bytes d6b61f91
- 00b4725c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b4725c ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00b47324 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b47324 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b4725c bytes 950200b4
+ 00b47324 bytes 950200b4
- 00b47270 ["INT_ADD", "register:40f0:8", ["const:b47270:8", "const:4:8"]]
- 00b47270 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b47338 ["INT_ADD", "register:40f0:8", ["const:b47338:8", "const:4:8"]]
+ 00b47338 ["CALL", null, ["callee:00bdb130:8"]]
- 00b47270 bytes 844f0294
+ 00b47338 bytes 7e4f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-438865f48191064d05a9ab830f79e7b1"></a>

### [`00b47754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47754.md) → [`00b4781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4781c.md) _ZN11flatbuffers18RemoveStringQuotesERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47768"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4776c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47778"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47778",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47874"
      ]
    ]
  ],
  "added": [
    [
      "00b47840",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47874"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47754.md#insn-00b47768) · [`00b4776c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47754.md#insn-00b4776c) · [`00b47778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47754.md#insn-00b47778)

~~~diff
- 00b47768 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b47768 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b47768 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b47768 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b47768 bytes 4915809a
- 00b4776c ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b4776c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b4776c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b4776c ["COPY", "register:4050:8", ["tmp:0:8"]]
- 00b4776c bytes 8a018b9a
- 00b47778 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b47778 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b47778 bytes a3010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cec9d6b5306cc8268247ab20c9faace"></a>

### [`00b477b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b477b0.md) → [`00b47878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md) _ZN11flatbuffers19SetGlobalTestLocaleEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.06% / 新版 89.06%

CFGの説明率　旧版 66.67% / 新版 76.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b477b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b477b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b477b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b477b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b477b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b477bc",
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
      "00b4787c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b47880",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b47884",
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

- 旧版 [`00b477b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b477b0.md#insn-00b477b4) · [`00b477b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b477b0.md#insn-00b477b8) · [`00b477bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b477b0.md#insn-00b477bc)

~~~diff
- 00b477b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b477b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b477b4 bytes f71300f9
- 00b477b8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b477b8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b477b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b477b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b477b8 bytes f65703a9
- 00b477bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b477bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b477bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b477bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b477bc bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07dd0187128558aaaf58c2522fecde33"></a>

### [`00b478b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b478b0.md) → [`00b47978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47978.md) _ZN11flatbuffers23ReadEnvironmentVariableEPKcPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdc950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc950.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca00.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 52.17% / 新版 52.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b478b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b478b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b478b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b478b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b478b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b478bc",
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
      "00b4797c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b47980",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b47984",
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

- 旧版 [`00b478b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b478b0.md#insn-00b478b4) · [`00b478b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b478b0.md#insn-00b478b8) · [`00b478bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b478b0.md#insn-00b478bc)

~~~diff
- 00b478b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b478b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b478b4 bytes f71300f9
- 00b478b8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b478b8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b478b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b478b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b478b8 bytes f65703a9
- 00b478bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b478bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b478bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b478bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b478bc bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cedc38ada183199862f9c67daaf1ac23"></a>

### [`00b47a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47a3c.md) → [`00b47b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b04.md) FUN_00b47b04

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md) [`00be01a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.90% / 新版 61.90%

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
      "site": "00b47a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47b34"
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
      "unmatched:00b47a54",
      "READ",
      [
        "storage",
        "00c1b140",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b47a6c",
      "DATA",
      [
        "storage",
        "00c111a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b47a70",
      "DATA",
      [
        "storage",
        "00c111d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b47b1c",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b47b34",
      "DATA",
      [
        "storage",
        "00c11258",
        null,
        "pointer"
      ]
    ],
    [
      "00b47b38",
      "DATA",
      [
        "storage",
        "00c11280",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47a3c.md#insn-00b47a6c) · [`00b47a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47a3c.md#insn-00b47a70)
- 新版 [`00b47b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b04.md#insn-00b47b34)

~~~diff
- 00b47a6c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b47a6c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b47a6c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00b47a6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b47a6c bytes 0a0401f8
- 00b47a70 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b47a70 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:b8:8"]]
- 00b47a70 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00b47a70 bytes 888e0bf8
+ 00b47b34 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b47b34 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b47b34 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 00b47b34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b47b34 bytes 0a0401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870adc5bd932c8eca6553a03080aa795"></a>

### [`00b47d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47d38.md) → [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekoffExNS_8ios_base7seekdirEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b4856c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b4856c.md) [`00be01c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01c0.md) [`00be01d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md) [`00be0280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0280.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 8.33% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47da0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e8c"
      ]
    ],
    [
      "unmatched:00b47da0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e94"
      ]
    ],
    [
      "unmatched:00b47d64",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47e44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e8c"
      ]
    ],
    [
      "00b47e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47e94"
      ]
    ],
    [
      "00b47e2c",
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

- 旧版 [`00b47d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47d38.md#insn-00b47d64) · [`00b47d7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47d38.md#insn-00b47d7c) · [`00b47da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47d38.md#insn-00b47da0)

~~~diff
- 00b47d64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47d64 ["INT_ADD", "register:40f0:8", ["const:b47d64:8", "const:4:8"]]
- 00b47d64 ["CALLIND", null, ["register:0:8"]]
- 00b47d64 bytes 00013fd6
- 00b47d7c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b47d7c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b47d7c bytes 4b020054
- 00b47da0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b47da0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b47da0 ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
- 00b47da0 bytes 68010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb9d4936875049c4138a92e4d483725e"></a>

### [`00b47df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47df8.md) → [`00b47ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE7seekposENS_4fposI9mbstate_tEEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be01c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01c0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 16.67% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47dfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b47dfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b47df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b47dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b47e00",
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
      "00b47ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b47ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b47ec8",
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

- 旧版 [`00b47df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47df8.md#insn-00b47df8) · [`00b47dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47df8.md#insn-00b47dfc) · [`00b47e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47df8.md#insn-00b47e00)

~~~diff
- 00b47df8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b47df8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b47df8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b47df8 bytes f50f1df8
- 00b47dfc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b47dfc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b47dfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b47dfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b47dfc bytes f44f01a9
- 00b47e00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b47e00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b47e00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b47e00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b47e00 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4313dd74c2a6cdd3bf06325c85965073"></a>

### [`00b482d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b482d4.md) → [`00b4839c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4839c.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE9pbackfailEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 70.00% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b482e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b483b0"
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
      "unmatched:00b482e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b483e4"
      ]
    ]
  ],
  "added": [
    [
      "00b483b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b483e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b482e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b482d4.md#insn-00b482e8) · [`00b482d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b482d4.md#insn-00b482d8)
- 新版 [`00b483b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4839c.md#insn-00b483b0) · [`00b483a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4839c.md#insn-00b483a0)

~~~diff
- 00b482e8 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00b482e8 bytes a2010054
+ 00b483b0 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
+ 00b483b0 bytes a2010054
- 00b482d8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b482d8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b483a0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b483a0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b482d8 bytes 290200b4
+ 00b483a0 bytes 290200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c919a45e7d363c0f6bed43add4a7303f"></a>

### [`00b48334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48334.md) → [`00b483fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE8overflowEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b4856c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b4856c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b48634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48634.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 66.67% / 新版 59.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b484d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b484dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b485a0"
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
      "unmatched:00b484e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48630"
      ]
    ],
    [
      "unmatched:00b48518",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48558"
      ]
    ]
  ],
  "added": [
    [
      "00b485a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48630"
      ]
    ],
    [
      "00b485e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48558"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48334.md#insn-00b48414) · [`00b484d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48334.md#insn-00b484d8) · [`00b484dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48334.md#insn-00b484dc)
- 新版 [`00b484dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b483fc.md#insn-00b484dc)

~~~diff
- 00b48414 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b48414 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 00b484dc ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b484dc ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00b48414 bytes a8010034
+ 00b484dc bytes a8010034
- 00b484d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00b484d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4010:8"]]
- 00b484d8 bytes 621600f9
- 00b484dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b484dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:8"]]
- 00b484dc bytes 631e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b83155c39b5484a7a700425020218220"></a>

### [`00b48638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48638.md) → [`00b48700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48700.md) _ZTv0_n24_NSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00b48638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4863c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4863c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48638",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4863c",
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
      "00b48700",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48704",
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

- 旧版 [`00b48638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48638.md#insn-00b48638) · [`00b4863c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48638.md#insn-00b4863c)
- 新版 [`00b48700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48700.md#insn-00b48700)

~~~diff
- 00b48638 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b48638 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48638 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48638 bytes f30f1ef8
- 00b4863c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4863c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4863c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4863c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4863c bytes fd7b01a9
+ 00b48700 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00b48700 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b48700 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b48700 bytes f30f1ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b619c1aad56c3cf5be91cd0a2db37960"></a>

### [`00b48668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48668.md) → [`00b48730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48730.md) FUN_00b48730

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 37.93% / 新版 37.93%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48668"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4866c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4866c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48668",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4866c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48678",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48730",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48734",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48740",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48668.md#insn-00b48668) · [`00b4866c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48668.md#insn-00b4866c) · [`00b48694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48668.md#insn-00b48694)

~~~diff
- 00b48668 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b48668 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b48668 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48668 bytes f30f1ef8
- 00b4866c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4866c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4866c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4866c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4866c bytes fd7b01a9
- 00b48694 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:70:8"]]
- 00b48694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b48694 bytes 083800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d7e2026647b3eb297cc004e1881ee89"></a>

### [`00b486dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b486dc.md) → [`00b487a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b487a4.md) FUN_00b487a4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.61% / 新版 60.61%

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
      "site": "00b48708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4870c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b486f4",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b48708",
      "DATA",
      [
        "storage",
        "00c112f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b4870c",
      "DATA",
      [
        "storage",
        "00c11320",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b487bc",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00b487d0",
      "DATA",
      [
        "storage",
        "00c113a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b487d4",
      "DATA",
      [
        "storage",
        "00c113d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b486dc.md#insn-00b48708) · [`00b4870c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b486dc.md#insn-00b4870c) · [`00b48720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b486dc.md#insn-00b48720)

~~~diff
- 00b48708 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b48708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b48708 bytes 6a0200f9
- 00b4870c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b4870c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:70:8"]]
- 00b4870c ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00b4870c bytes 880e07f8
- 00b48720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b48720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b48720 bytes 690600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-990701e798ba030453f9a51eab035926"></a>

### [`00b487a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b487a8.md) → [`00b48870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48870.md) FUN_00b48870

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md) [`00be01a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b487cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b487d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48894"
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
      "00b48880",
      "READ",
      [
        "storage",
        "00c1afd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b487cc",
      "DATA",
      [
        "storage",
        "00c113b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b487d0",
      "DATA",
      [
        "storage",
        "00c113d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48880",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00b48894",
      "DATA",
      [
        "storage",
        "00c11460",
        null,
        "pointer"
      ]
    ],
    [
      "00b48898",
      "DATA",
      [
        "storage",
        "00c11488",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b487cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b487a8.md#insn-00b487cc) · [`00b487d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b487a8.md#insn-00b487d0)
- 新版 [`00b48894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48870.md#insn-00b48894)

~~~diff
- 00b487cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b487cc ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b487cc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b487cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b487cc bytes 098400f8
- 00b487d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b487d0 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:b0:8"]]
- 00b487d0 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00b487d0 bytes 880e0bf8
+ 00b48894 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b48894 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b48894 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00b48894 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b48894 bytes 098400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61dcbd655b090d6256835a73bfa7d675"></a>

### [`00b48a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48a88.md) → [`00b48b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b50.md) FUN_00b48b50

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a990.md) · 呼出先 2件 [`00bddb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb80.md) [`00bddd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd00.md)
- 新版 呼出元 1件 [`00b4aa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md) · 呼出先 2件 [`00bddc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc30.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b48b78"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48a88.md#insn-00b48ab0) · [`00b48a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48a88.md#insn-00b48a98)
- 新版 [`00b48b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b50.md#insn-00b48b78) · [`00b48b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b50.md#insn-00b48b60)

~~~diff
- 00b48ab0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b48ab0 ["RETURN", null, ["register:0:8"]]
- 00b48ab0 bytes c0035fd6
+ 00b48b78 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b48b78 ["RETURN", null, ["register:0:8"]]
+ 00b48b78 bytes c0035fd6
- 00b48a98 ["INT_ADD", "register:40f0:8", ["const:b48a98:8", "const:4:8"]]
- 00b48a98 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b48b60 ["INT_ADD", "register:40f0:8", ["const:b48b60:8", "const:4:8"]]
+ 00b48b60 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b48a98 bytes 9a540294
+ 00b48b60 bytes 94540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f846ac2460aaa66ea33bbb5f729bcbc4"></a>

### [`00b48afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48afc.md) → [`00b48bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48bc4.md) _ZN8firebase9messaging8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0350.md) · 呼出先 5件 [`00b49400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49400.md) [`00bddc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc70.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md) [`00bddd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd00.md)
- 新版 呼出元 1件 [`00be0400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0400.md) · 呼出先 5件 [`00b494c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md) [`00bddd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd20.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48b30",
      "PARAM",
      [
        "storage",
        "00b49400",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48b34",
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
      "00b48bf8",
      "PARAM",
      [
        "storage",
        "00b494c8",
        null,
        null
      ]
    ],
    [
      "00b48bfc",
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

- 旧版 [`00b48b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48afc.md#insn-00b48b0c) · [`00b48b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48afc.md#insn-00b48b1c) · [`00b48b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48afc.md#insn-00b48b20)
- 新版 [`00b48bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48bc4.md#insn-00b48bd4) · [`00b48be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48bc4.md#insn-00b48be4) · [`00b48be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48bc4.md#insn-00b48be8)

~~~diff
- 00b48b0c ["INT_ADD", "register:40f0:8", ["const:b48b0c:8", "const:4:8"]]
- 00b48b0c ["CALL", null, ["callee:00bddd20:8"]]
+ 00b48bd4 ["INT_ADD", "register:40f0:8", ["const:b48bd4:8", "const:4:8"]]
+ 00b48bd4 ["CALL", null, ["callee:00bddd20:8"]]
- 00b48b0c bytes 59540294
+ 00b48bd4 bytes 53540294
- 00b48b1c ["INT_ADD", "register:40f0:8", ["const:b48b1c:8", "const:4:8"]]
- 00b48b1c ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b48be4 ["INT_ADD", "register:40f0:8", ["const:b48be4:8", "const:4:8"]]
+ 00b48be4 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b48b1c bytes 79540294
+ 00b48be4 bytes 73540294
- 00b48b20 ["INT_ADD", "register:40f0:8", ["const:b48b20:8", "const:4:8"]]
- 00b48b20 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b48be8 ["INT_ADD", "register:40f0:8", ["const:b48be8:8", "const:4:8"]]
+ 00b48be8 ["CALL", null, ["callee:00bddd40:8"]]
- 00b48b20 bytes 5c540294
+ 00b48be8 bytes 56540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c52a3f098743e326a31bc0f64e1268f"></a>

### [`00b48b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b3c.md) → [`00b48c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md) _ZN8firebase9messaging8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0360.md) · 呼出先 5件 [`00bddc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc70.md) [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md) [`00bddd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd00.md) [`00be0340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0340.md)
- 新版 呼出元 1件 [`00be0410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0410.md) · 呼出先 5件 [`00bddd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd20.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md) [`00bdddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddb0.md) [`00be03f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03f0.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48b68",
      "PARAM",
      [
        "storage",
        "002f8894",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48c30",
      "PARAM",
      [
        "storage",
        "002f8894",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b3c.md#insn-00b48b4c) · [`00b48b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b3c.md#insn-00b48b54) · [`00b48b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b3c.md#insn-00b48b5c)
- 新版 [`00b48c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md#insn-00b48c14) · [`00b48c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md#insn-00b48c1c) · [`00b48c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md#insn-00b48c24)

~~~diff
- 00b48b4c ["INT_ADD", "register:40f0:8", ["const:b48b4c:8", "const:4:8"]]
- 00b48b4c ["CALL", null, ["callee:00bddd20:8"]]
+ 00b48c14 ["INT_ADD", "register:40f0:8", ["const:b48c14:8", "const:4:8"]]
+ 00b48c14 ["CALL", null, ["callee:00bddd20:8"]]
- 00b48b4c bytes 49540294
+ 00b48c14 bytes 43540294
- 00b48b54 ["INT_ADD", "register:40f0:8", ["const:b48b54:8", "const:4:8"]]
- 00b48b54 ["CALL", null, ["callee:00be03f0:8"]]
+ 00b48c1c ["INT_ADD", "register:40f0:8", ["const:b48c1c:8", "const:4:8"]]
+ 00b48c1c ["CALL", null, ["callee:00be03f0:8"]]
- 00b48b54 bytes fb5d0294
+ 00b48c1c bytes f55d0294
- 00b48b5c ["INT_ADD", "register:40f0:8", ["const:b48b5c:8", "const:4:8"]]
- 00b48b5c ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b48c24 ["INT_ADD", "register:40f0:8", ["const:b48c24:8", "const:4:8"]]
+ 00b48c24 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b48b5c bytes 69540294
+ 00b48c24 bytes 63540294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc69e01ec5e960a49015f515e5b0f67"></a>

### [`00b48e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48e68.md) → [`00b48f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48f30.md) _ZN8firebase9messaging16PollableListenerC2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

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
      "site": "00b48e68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48e6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b48e6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b48e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b48e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48f44",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b48f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b48f44",
      "READ",
      [
        "storage",
        "00c1ba90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48e68.md#insn-00b48e68) · [`00b48e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48e68.md#insn-00b48e6c) · [`00b48e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48e68.md#insn-00b48e88)

~~~diff
- 00b48e68 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b48e68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b48e68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b48e68 bytes f50f1df8
- 00b48e6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b48e6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b48e6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b48e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b48e6c bytes f44f01a9
- 00b48e88 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b48e88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b48e88 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3c90dd3385fe2693c1063695c4699a"></a>

### [`00b492a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b492a8.md) → [`00b49370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49370.md) _ZN8firebase9messaging20PollableListenerImpl21PollRegistrationTokenEPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be02c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be02c0.md) · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00be0370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0370.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 68.75% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b492ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b492f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b493b4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b492ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b492a8.md#insn-00b492ec) · [`00b492f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b492a8.md#insn-00b492f0)
- 新版 [`00b493b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49370.md#insn-00b493b4)

~~~diff
- 00b492ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b492ec ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b492ec ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b492ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
- 00b492ec bytes 2115959a
- 00b492f0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b492f0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b492f0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b492f0 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b492f0 bytes 62018a9a
+ 00b493b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b493b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00b493b4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b493b4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1:8"]]
+ 00b493b4 bytes 2115959a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e89bb4b15deb9428616c28d0b6339c"></a>

### [`00b49364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49364.md) → [`00b4942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4942c.md) _ZN8firebase9messaging10FutureData6CreateEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0210.md) · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddce0.md)
- 新版 呼出元 1件 [`00be02c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02c0.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4945c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4939c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49450",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b49394",
      "WRITE",
      [
        "storage",
        "010a0ea0",
        "_ZN8firebase9messaging10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49450",
      "READ",
      [
        "storage",
        "00c1ba88",
        null,
        "pointer"
      ]
    ],
    [
      "00b4945c",
      "WRITE",
      [
        "storage",
        "010a0f60",
        "_ZN8firebase9messaging10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49364.md#insn-00b49394) · [`00b4939c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49364.md#insn-00b4939c)
- 新版 [`00b4945c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4942c.md#insn-00b4945c)

~~~diff
- 00b49394 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b49394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b49394 bytes 130100f9
- 00b4939c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4939c ["RETURN", null, ["register:0:8"]]
- 00b4939c bytes c0035fd6
+ 00b4945c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b4945c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00b4945c bytes 130100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74f3e4c2d3bdb759cac27d0b1ca6a3b"></a>

### [`00b49860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49860.md) → [`00b49928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49928.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0310.md) · 呼出先 1件 [`00be0330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0330.md)
- 新版 呼出元 1件 [`00be03c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03c0.md) · 呼出先 1件 [`00be03e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03e0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b498c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b498c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b498cc"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b498c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49860.md#insn-00b498c8) · [`00b498cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49860.md#insn-00b498cc)
- 新版 [`00b49990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49928.md#insn-00b49990)

~~~diff
- 00b498c8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:10:8"]]
- 00b498c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b498c8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b498c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b498c8 bytes 008300ad
- 00b498cc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b498cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b498cc bytes 0003803d
+ 00b49990 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:10:8"]]
+ 00b49990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00b49990 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00b49990 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
+ 00b49990 bytes 008300ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12c6734879e566770d989dc593a1781d"></a>

### [`00b49c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49c34.md) → [`00b49cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49cfc.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0250.md) · 呼出先 1件 [`00be0270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0270.md)
- 新版 呼出元 1件 [`00be0300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md) · 呼出先 1件 [`00be0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0320.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49c34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49c38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49c34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b49c3c",
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
      "00b49cfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b49d00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b49d04",
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

- 旧版 [`00b49c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49c34.md#insn-00b49c34) · [`00b49c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49c34.md#insn-00b49c38) · [`00b49c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49c34.md#insn-00b49c3c)

~~~diff
- 00b49c34 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b49c34 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b49c34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b49c34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b49c34 bytes f657bda9
- 00b49c38 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b49c38 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b49c38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b49c38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49c38 bytes f44f01a9
- 00b49c3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b49c3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b49c3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b49c3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b49c3c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882b22cd4bc767e633241993dcd1365e"></a>

### [`00b4a350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a350.md) → [`00b4a418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md) FUN_00b4a418

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a13c.md) · 呼出先 4件 [`00ae03b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae03b4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 61.90% / 新版 56.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a398"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a404"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b4a460"
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
      "unmatched:00b4a404",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4a504"
      ]
    ],
    [
      "unmatched:00b4a488",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4a48c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00ae047c"
      ]
    ]
  ],
  "added": [
    [
      "00b4a4cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4a504"
      ]
    ],
    [
      "00b4a550",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ],
    [
      "00b4a554",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00ae047c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a350.md#insn-00b4a398) · [`00b4a404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a350.md#insn-00b4a404)
- 新版 [`00b4a460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md#insn-00b4a460)

~~~diff
- 00b4a398 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b4a398 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b4a398 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b4a398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b4a398 bytes 48b5889a
- 00b4a404 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00b4a404 bytes c0010054
+ 00b4a460 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b4a460 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b4a460 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b4a460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
+ 00b4a460 bytes 48b5889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-924cc81e335962e54cc753ef99e71230"></a>

### [`00b4a490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a490.md) → [`00b4a558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be03b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03b0.md) · 呼出先 4件 [`00ae03b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae03b4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00be0460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0460.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.75% / 新版 73.75%

CFGの説明率　旧版 18.52% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a490"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4a494"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4a490",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4a494",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4a498",
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
      "00b4a558",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b4a55c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b4a560",
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

- 旧版 [`00b4a490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a490.md#insn-00b4a490) · [`00b4a494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a490.md#insn-00b4a494) · [`00b4a498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a490.md#insn-00b4a498)

~~~diff
- 00b4a490 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b4a490 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b4a490 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4a490 bytes f90f1bf8
- 00b4a494 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b4a494 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b4a494 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4a494 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4a494 bytes f85f01a9
- 00b4a498 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b4a498 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b4a498 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b4a498 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4a498 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-757236125666582954351e3d8336c1cb"></a>

### [`00b4aa08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa08.md) → [`00b4aad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aad0.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "site": "00b4aa34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4aafc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aa1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aa18",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4aa1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4aa38"
      ]
    ],
    [
      "unmatched:00b4aa28",
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
      "00b4aae0",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ab00"
      ]
    ],
    [
      "00b4aaf0",
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

- 旧版 [`00b4aa1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa08.md#insn-00b4aa1c) · [`00b4aa2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa08.md#insn-00b4aa2c) · [`00b4aa34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa08.md#insn-00b4aa34)

~~~diff
- 00b4aa1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aa1c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4aa1c bytes e80000b5
- 00b4aa2c ["INT_ADD", "register:40f0:8", ["const:b4aa2c:8", "const:4:8"]]
- 00b4aa2c ["CALL", null, ["callee:00bde040:8"]]
- 00b4aa2c bytes 594d0294
- 00b4aa34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ef8:8"]]
- 00b4aa34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aa34 bytes 607e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4256505faa0aeb1d1ee8d646ece282e"></a>

### [`00b4aa88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa88.md) → [`00b4ab50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab50.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00b4aab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ab80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aa9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aa98",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4aa9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4aabc"
      ]
    ],
    [
      "unmatched:00b4aaa8",
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
      "00b4ab60",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ab84"
      ]
    ],
    [
      "00b4ab70",
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

- 旧版 [`00b4aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa88.md#insn-00b4aa9c) · [`00b4aab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa88.md#insn-00b4aab0) · [`00b4aab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4aa88.md#insn-00b4aab8)

~~~diff
- 00b4aa9c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aa9c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4aa9c bytes 080100b5
- 00b4aab0 ["INT_ADD", "register:40f0:8", ["const:b4aab0:8", "const:4:8"]]
- 00b4aab0 ["CALL", null, ["callee:00bde040:8"]]
- 00b4aab0 bytes 384d0294
- 00b4aab8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ef8:8"]]
- 00b4aab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aab8 bytes 607e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

