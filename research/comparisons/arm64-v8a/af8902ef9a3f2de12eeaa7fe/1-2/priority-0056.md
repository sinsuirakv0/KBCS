# v15.7.4 → v16.0.0 · 最優先の変更候補 (56)

[一覧の目次](README.md)

<a id="compare-438043fd5a8135ef7d92fd6f6ff56976"></a>

### [`00ae40d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae40d8.md) → [`00b43e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e5c.md) _ZN8firebase8LogDebugEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)
- 新版 呼出元 1件 [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 24.39% / 新版 24.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae40dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae40dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae40e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae40dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae40e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae40e8",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b43e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b43e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b43e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae40dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae40d8.md#insn-00ae40dc) · [`00ae40e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae40d8.md#insn-00ae40e0) · [`00ae40e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae40d8.md#insn-00ae40e8)

~~~diff
- 00ae40dc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ae40dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae40dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00ae40dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae40dc bytes fc4f11a9
- 00ae40e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae40e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae40e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00ae40e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae40e0 bytes fd7b12a9
- 00ae40e8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00ae40e8 ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00ae40e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:88:8"]]
- 00ae40e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae40e8 bytes e18b08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc2ac904e706b27a418ddb26a93d408"></a>

### [`00ae42c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae42c4.md) → [`00b44048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44048.md) _ZN8firebase8LogErrorEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)
- 新版 呼出元 1件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.66% / 新版 53.66%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae42dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae42dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae42e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae42dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae42e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae42e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44060",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00b44064",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b44068",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae42dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae42c4.md#insn-00ae42dc) · [`00ae42e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae42c4.md#insn-00ae42e0) · [`00ae42e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae42c4.md#insn-00ae42e4)

~~~diff
- 00ae42dc ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00ae42dc ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00ae42dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a8:8"]]
- 00ae42dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae42dc bytes e59b0aa9
- 00ae42e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b8:8"]]
- 00ae42e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00ae42e0 bytes e75f00f9
- 00ae42e4 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00ae42e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ae42e4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ae42e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00ae42e4 bytes e00700ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8400be869b7cca633a641d92736c8fda"></a>

### [`00ae4368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4368.md) → [`00b440ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b440ec.md) _ZN8firebase9LogAssertEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)
- 新版 呼出元 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.73% / 新版 70.73%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae43c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae43c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae43c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae43c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae43c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae43c8",
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
      "00b44144",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b44148",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b4414c",
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

- 旧版 [`00ae43c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4368.md#insn-00ae43c0) · [`00ae43c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4368.md#insn-00ae43c4) · [`00ae43c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4368.md#insn-00ae43c8)

~~~diff
- 00ae43c0 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00ae43c0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00ae43c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae43c0 bytes ad831ef8
- 00ae43c4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ae43c4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ae43c4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae43c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae43c4 bytes abab3ca9
- 00ae43c8 ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00ae43c8 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00ae43c8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00ae43c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae43c8 bytes aeb33da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61ef0405289c05b2ccfac9250baa7487"></a>

### [`00ae440c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae440c.md) → [`00b44190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44190.md) _ZN8firebase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde240.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md)
- 新版 呼出元 1件 [`00c5acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acc0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 62.16% / 新版 62.16%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4464"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4464"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4460",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4464",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4468",
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
      "00b441e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b441e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b441ec",
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

- 旧版 [`00ae4460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae440c.md#insn-00ae4460) · [`00ae4464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae440c.md#insn-00ae4464) · [`00ae4468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae440c.md#insn-00ae4468)

~~~diff
- 00ae4460 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00ae4460 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00ae4460 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae4460 bytes ac831ef8
- 00ae4464 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00ae4464 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ae4464 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae4464 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4464 bytes aaa73ca9
- 00ae4468 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00ae4468 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00ae4468 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00ae4468 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4468 bytes adaf3da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8818c5a08e585db6496adedfa565d2e0"></a>

### [`00ae44cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md) → [`00b44250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md) _ZN8firebase14LogGetCallbackEPPv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b44278",
      "incomplete_value": true,
      "site": "00b4427c",
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
      "definition_site": "00ae44f4",
      "incomplete_value": true,
      "site": "00ae44f8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b44268",
      "incomplete_value": false,
      "site": "00b4426c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:f3a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae44e4",
      "incomplete_value": false,
      "site": "00ae44e8",
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
            "const:d5d:8"
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
      "definition_site": "00b4428c",
      "incomplete_value": true,
      "site": "00b44294",
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
      "definition_site": "00ae4508",
      "incomplete_value": true,
      "site": "00ae4510",
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
      "00b44268",
      "PARAM",
      [
        "storage",
        "0029bd5d",
        null,
        "string"
      ]
    ],
    [
      "00b44274",
      "READ",
      [
        "storage",
        "00c1b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44278",
      "READ",
      [
        "storage",
        "010a0150",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44268",
      "PARAM",
      [
        "storage",
        "002abf3a",
        null,
        "string"
      ]
    ],
    [
      "00b44274",
      "READ",
      [
        "storage",
        "00c9b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b44278",
      "READ",
      [
        "storage",
        "01125010",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae44e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md#insn-00ae44e8) · [`00ae44e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md#insn-00ae44e0) · [`00ae44e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md#insn-00ae44e4)
- 新版 [`00b4426c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md#insn-00b4426c) · [`00b44264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md#insn-00b44264) · [`00b44268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44250.md#insn-00b44268)

~~~diff
- 00ae44e8 ["INT_ADD", "register:40f0:8", ["const:ae44e8:8", "const:4:8"]]
- 00ae44e8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4426c ["INT_ADD", "register:40f0:8", ["const:b4426c:8", "const:4:8"]]
+ 00b4426c ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae44e8 bytes 26e70394
+ 00b4426c bytes 655a0494
- 00ae44e0 ["COPY", "register:4000:8", ["const:29b000:8"]]
+ 00b44264 ["COPY", "register:4000:8", ["const:2ab000:8"]]
- 00ae44e0 bytes a0bdfff0
+ 00b44264 bytes 20bbfff0
- 00ae44e4 ["COPY", "tmp:0:8", ["const:d5d:8"]]
- 00ae44e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae44e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae44e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b44268 ["COPY", "tmp:0:8", ["const:f3a:8"]]
+ 00b44268 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44268 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44268 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae44e4 bytes 00743591
+ 00b44268 bytes 00e83c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a59908c14508d0f85daf70149c94ebc"></a>

### [`00ae4514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md) → [`00b44298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44298.md) FUN_00b44298

採用 · 移動量 `+0x5fd84` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde260.md)
- 新版 呼出元 1件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ace0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4528"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4524",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4528",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae452c",
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
      "00b442a8",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00b442ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "00b442b0",
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

- 旧版 [`00ae4524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md#insn-00ae4524) · [`00ae4528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md#insn-00ae4528) · [`00ae452c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md#insn-00ae452c)

~~~diff
- 00ae4524 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00ae4524 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00ae4524 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00ae4524 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4524 bytes e20f08a9
- 00ae4528 ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00ae4528 ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00ae4528 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00ae4528 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4528 bytes e41709a9
- 00ae452c ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00ae452c ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00ae452c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00ae452c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae452c bytes e61f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ea7e277dd6992da9972f4db77dbb78"></a>

### [`00ae474c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md) → [`00b444d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b444d0.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae4778"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b444fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b444e4",
      "incomplete_value": true,
      "site": "00b444e4",
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
      "definition_site": "00ae4760",
      "incomplete_value": true,
      "site": "00ae4760",
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
      "00b444e0",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae476c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae4770",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b444e0",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b444f0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "00b444f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md#insn-00ae4760) · [`00ae4770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md#insn-00ae4770) · [`00ae4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md#insn-00ae4778)
- 新版 [`00b444e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b444d0.md#insn-00b444e4)

~~~diff
- 00ae4760 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae4760 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b444e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b444e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae4760 bytes e80000b5
+ 00b444e4 bytes e80000b5
- 00ae4770 ["INT_ADD", "register:40f0:8", ["const:ae4770:8", "const:4:8"]]
- 00ae4770 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae4770 bytes 48e60394
- 00ae4778 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae4778 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4778 bytes 60b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46be9f2b16b05b53e2b76072e52b60f1"></a>

### [`00ae478c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md) → [`00b44510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md) _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassReq

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) · 呼出先 4件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) [`00bde4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4b0.md) [`00bde6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6f0.md)
- 新版 呼出元 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) · 呼出先 4件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5af30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af30.md) [`00c5b170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b170.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 27.78% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae47ac",
      "incomplete_value": false,
      "site": "00ae47c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "definition_site": "00ae47f8",
      "incomplete_value": false,
      "site": "00ae4804",
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
            "const:e94:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b445c0",
      "incomplete_value": false,
      "site": "00b445cc",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae483c",
      "incomplete_value": false,
      "site": "00ae4848",
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
            "const:609:8"
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
      "unmatched:00ae47ac",
      "PARAM",
      [
        "storage",
        "002a6110",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae47f8",
      "PARAM",
      [
        "storage",
        "002a1e94",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae483c",
      "PARAM",
      [
        "storage",
        "00299609",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44530",
      "PARAM",
      [
        "storage",
        "002b6bd4",
        null,
        "string"
      ]
    ],
    [
      "00b4457c",
      "PARAM",
      [
        "storage",
        "002b2555",
        null,
        "string"
      ]
    ],
    [
      "00b445c0",
      "PARAM",
      [
        "storage",
        "002a9468",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae47c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md#insn-00ae47c0) · [`00ae4804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md#insn-00ae4804) · [`00ae4848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md#insn-00ae4848)
- 新版 [`00b44544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md#insn-00b44544) · [`00b44588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md#insn-00b44588) · [`00b445cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44510.md#insn-00b445cc)

~~~diff
- 00ae47c0 ["INT_ADD", "register:40f0:8", ["const:ae47c0:8", "const:4:8"]]
- 00ae47c0 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b44544 ["INT_ADD", "register:40f0:8", ["const:b44544:8", "const:4:8"]]
+ 00b44544 ["CALL", null, ["callee:00c5ad30:8"]]
- 00ae47c0 bytes bce60394
+ 00b44544 bytes fb590494
- 00ae4804 ["INT_ADD", "register:40f0:8", ["const:ae4804:8", "const:4:8"]]
- 00ae4804 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b44588 ["INT_ADD", "register:40f0:8", ["const:b44588:8", "const:4:8"]]
+ 00b44588 ["CALL", null, ["callee:00c5ad30:8"]]
- 00ae4804 bytes abe60394
+ 00b44588 bytes ea590494
- 00ae4848 ["INT_ADD", "register:40f0:8", ["const:ae4848:8", "const:4:8"]]
- 00ae4848 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b445cc ["INT_ADD", "register:40f0:8", ["const:b445cc:8", "const:4:8"]]
+ 00b445cc ["CALL", null, ["callee:00c5ad30:8"]]
- 00ae4848 bytes 9ae60394
+ 00b445cc bytes d9590494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103344af7f7ce60e0f039f871c1fe92d"></a>

### [`00ae48bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md) → [`00b44640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b4466c",
      "incomplete_value": true,
      "site": "00b4466c",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae48e8",
      "incomplete_value": true,
      "site": "00ae48e8",
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
            "const:368:8"
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
      "definition_site": "00b44654",
      "incomplete_value": true,
      "site": "00b44654",
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
      "definition_site": "00ae48d0",
      "incomplete_value": true,
      "site": "00ae48d0",
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
      "definition_site": "00b4465c",
      "incomplete_value": false,
      "site": "00b44664",
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
            "const:9e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae48d8",
      "incomplete_value": false,
      "site": "00ae48e0",
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
            "const:d6a:8"
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
      "00b44650",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4465c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00b4466c",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44650",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4465c",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "00b4466c",
      "WRITE",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md#insn-00ae48e0) · [`00ae48e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md#insn-00ae48e8) · [`00ae48c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md#insn-00ae48c8)
- 新版 [`00b44664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md#insn-00b44664) · [`00b4466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md#insn-00b4466c) · [`00b4464c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44640.md#insn-00b4464c)

~~~diff
- 00ae48e0 ["INT_ADD", "register:40f0:8", ["const:ae48e0:8", "const:4:8"]]
- 00ae48e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b44664 ["INT_ADD", "register:40f0:8", ["const:b44664:8", "const:4:8"]]
+ 00b44664 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae48e0 bytes ece50394
+ 00b44664 bytes 2b590494
- 00ae48e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae48e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4466c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
+ 00b4466c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae48e8 bytes 60b601f9
+ 00b4466c bytes 601601f9
- 00ae48c8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4464c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae48c8 bytes f32d0090
+ 00b4464c bytes 132f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3dd6e9c3421283e260f38e51c74f6ec"></a>

### [`00ae48fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md) → [`00b44680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44680.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00ae492c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b446b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44694",
      "incomplete_value": true,
      "site": "00b44694",
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
      "definition_site": "00ae4910",
      "incomplete_value": true,
      "site": "00ae4910",
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
      "00b44690",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae491c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae4924",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b44690",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b446a0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "00b446a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md#insn-00ae4910) · [`00ae4924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md#insn-00ae4924) · [`00ae492c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md#insn-00ae492c)
- 新版 [`00b44694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44680.md#insn-00b44694)

~~~diff
- 00ae4910 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae4910 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b44694 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44694 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae4910 bytes 080100b5
+ 00b44694 bytes 080100b5
- 00ae4924 ["INT_ADD", "register:40f0:8", ["const:ae4924:8", "const:4:8"]]
- 00ae4924 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae4924 bytes dbe50394
- 00ae492c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae492c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae492c bytes 60b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-957317fe91cc30317c85033181f38f2c"></a>

### [`00ae4940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md) → [`00b446c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b446f4",
      "incomplete_value": true,
      "site": "00b446f4",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4970",
      "incomplete_value": true,
      "site": "00ae4970",
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
            "const:368:8"
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
      "definition_site": "00b446d8",
      "incomplete_value": true,
      "site": "00b446d8",
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
      "definition_site": "00ae4954",
      "incomplete_value": true,
      "site": "00ae4954",
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
      "definition_site": "00b446e0",
      "incomplete_value": false,
      "site": "00b446ec",
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
            "const:9e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae495c",
      "incomplete_value": false,
      "site": "00ae4968",
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
            "const:d6a:8"
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
      "00b446d4",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00b446e0",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00b446f4",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b446d4",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b446e0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "00b446f4",
      "WRITE",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md#insn-00ae4968) · [`00ae4970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md#insn-00ae4970) · [`00ae494c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md#insn-00ae494c)
- 新版 [`00b446ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md#insn-00b446ec) · [`00b446f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md#insn-00b446f4) · [`00b446d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b446c4.md#insn-00b446d0)

~~~diff
- 00ae4968 ["INT_ADD", "register:40f0:8", ["const:ae4968:8", "const:4:8"]]
- 00ae4968 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b446ec ["INT_ADD", "register:40f0:8", ["const:b446ec:8", "const:4:8"]]
+ 00b446ec ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae4968 bytes cae50394
+ 00b446ec bytes 09590494
- 00ae4970 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae4970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b446f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:228:8"]]
+ 00b446f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4970 bytes 60b601f9
+ 00b446f4 bytes 601601f9
- 00ae494c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b446d0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae494c bytes f32d0090
+ 00b446d0 bytes 132f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eadfdb3c0a39aa3496af30bc8c4086f"></a>

### [`00ae4990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md) → [`00b44714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44714.md) _ZN8firebase4util12class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4990"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4994"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4990",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4994",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4998",
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
      "00b44714",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b44718",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4471c",
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

- 旧版 [`00ae4990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md#insn-00ae4990) · [`00ae4994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md#insn-00ae4994) · [`00ae4998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md#insn-00ae4998)

~~~diff
- 00ae4990 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae4990 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae4990 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae4990 bytes f50f1df8
- 00ae4994 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae4994 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae4994 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae4994 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4994 bytes f44f01a9
- 00ae4998 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae4998 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae4998 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae4998 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4998 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9625c65b321c238927e865c6c8d4182"></a>

### [`00ae4a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md) → [`00b4480c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4480c.md) _ZN8firebase4util12class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 77.78% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b44898",
      "incomplete_value": true,
      "site": "00b44898",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4b14",
      "incomplete_value": true,
      "site": "00ae4b14",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44848"
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
      "00b44820",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4482c",
      "READ",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae4ac4",
      "WRITE",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b44820",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4482c",
      "READ",
      [
        "storage",
        "01125230",
        null,
        "undefined1"
      ]
    ],
    [
      "00b44848",
      "WRITE",
      [
        "storage",
        "01125230",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md#insn-00ae4aa0) · [`00ae4ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md#insn-00ae4ac0) · [`00ae4ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md#insn-00ae4ac4)
- 新版 [`00b44824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4480c.md#insn-00b44824)

~~~diff
- 00ae4aa0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae4aa0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b44824 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b44824 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae4aa0 bytes c10300b4
+ 00b44824 bytes c10300b4
- 00ae4ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4ac0 ["INT_ADD", "register:40f0:8", ["const:ae4ac0:8", "const:4:8"]]
- 00ae4ac0 ["CALLIND", null, ["register:0:8"]]
- 00ae4ac0 bytes 00013fd6
- 00ae4ac4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae4ac4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae4ac4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:370:8"]]
- 00ae4ac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae4ac4 bytes bfc20d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-190ec3ca2146f30c287a294d4a769cde"></a>

### [`00ae4b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md) → [`00b448ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b448ac.md) _ZN8firebase4util12class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae4b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b448ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4b44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4b3c",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae4b44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448f0"
      ]
    ],
    [
      "unmatched:00ae4b4c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b448c0",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b448c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448f0"
      ]
    ],
    [
      "00b448d0",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md#insn-00ae4b44) · [`00ae4b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md#insn-00ae4b60) · [`00ae4b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md#insn-00ae4b68)
- 新版 [`00b448e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b448ac.md#insn-00b448e4)

~~~diff
- 00ae4b44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae4b44 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae4b44 bytes 410100b5
- 00ae4b60 ["INT_ADD", "register:40f0:8", ["const:ae4b60:8", "const:4:8"]]
- 00ae4b60 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b448e4 ["INT_ADD", "register:40f0:8", ["const:b448e4:8", "const:4:8"]]
+ 00b448e4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae4b60 bytes 4ce50394
+ 00b448e4 bytes 8b580494
- 00ae4b68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
- 00ae4b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4b68 bytes 80b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73c769650fae5ead3f1af81781ae3e55"></a>

### [`00ae4b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md) → [`00b4491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b4491c.md) _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) · 呼出先 5件 [`00af15f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)
- 新版 呼出元 1件 [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md) · 呼出先 5件 [`00b51378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.55% / 新版 73.55%

CFGの説明率　旧版 41.79% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4bac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4bb0",
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
      "00b4492c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b44930",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b44934",
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

- 旧版 [`00ae4ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md#insn-00ae4ba8) · [`00ae4bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md#insn-00ae4bac) · [`00ae4bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md#insn-00ae4bb0)

~~~diff
- 00ae4ba8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae4ba8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae4ba8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00ae4ba8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4ba8 bytes f65715a9
- 00ae4bac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae4bac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae4bac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00ae4bac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4bac bytes f44f16a9
- 00ae4bb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae4bb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae4bb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00ae4bb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4bb0 bytes fd7b17a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45f00a40729a21beeffd95de2a3d3072"></a>

### [`00ae4e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md) → [`00b44b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md) _ZN8firebase4util12class_loader11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b44ba4",
      "incomplete_value": false,
      "site": "00b44ba8",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4e20",
      "incomplete_value": false,
      "site": "00ae4e24",
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
      "definition_site": "00b44bb4",
      "incomplete_value": true,
      "site": "00b44bc0",
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
      "definition_site": "00ae4e30",
      "incomplete_value": true,
      "site": "00ae4e3c",
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
      "00b44ba4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b44bb4",
      "DATA",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44ba4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b44bb4",
      "DATA",
      [
        "storage",
        "01125238",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md#insn-00ae4e24) · [`00ae4e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md#insn-00ae4e1c) · [`00ae4e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md#insn-00ae4e20)
- 新版 [`00b44ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md#insn-00b44ba8) · [`00b44ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md#insn-00b44ba0) · [`00b44ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44b88.md#insn-00b44ba4)

~~~diff
- 00ae4e24 ["INT_ADD", "register:40f0:8", ["const:ae4e24:8", "const:4:8"]]
- 00ae4e24 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b44ba8 ["INT_ADD", "register:40f0:8", ["const:b44ba8:8", "const:4:8"]]
+ 00b44ba8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae4e24 bytes d7e40394
+ 00b44ba8 bytes 16580494
- 00ae4e1c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b44ba0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae4e1c bytes a0bdff90
+ 00b44ba0 bytes 20bbff90
- 00ae4e20 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae4e20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae4e20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae4e20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b44ba4 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b44ba4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44ba4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b44ba4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae4e20 bytes 001c1591
+ 00b44ba4 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d5445f40745e7bb192249deb8eaa03b"></a>

### [`00ae4e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md) → [`00b44bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md) _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b44c04",
      "incomplete_value": true,
      "site": "00b44c04",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4e80",
      "incomplete_value": true,
      "site": "00ae4e80",
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
            "const:368:8"
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
      "definition_site": "00b44be0",
      "incomplete_value": true,
      "site": "00b44be0",
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
      "definition_site": "00ae4e5c",
      "incomplete_value": true,
      "site": "00ae4e5c",
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
      "definition_site": "00b44be8",
      "incomplete_value": false,
      "site": "00b44bfc",
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
            "const:9e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4e64",
      "incomplete_value": false,
      "site": "00ae4e78",
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
            "const:d6a:8"
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
      "00b44bd8",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44be8",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00b44c04",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44bd8",
      "READ",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44be8",
      "PARAM",
      [
        "storage",
        "002b89e6",
        null,
        "string"
      ]
    ],
    [
      "00b44c04",
      "WRITE",
      [
        "storage",
        "01125228",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md#insn-00ae4e78) · [`00ae4e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md#insn-00ae4e80) · [`00ae4e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md#insn-00ae4e4c)
- 新版 [`00b44bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md#insn-00b44bfc) · [`00b44c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md#insn-00b44c04) · [`00b44bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44bc4.md#insn-00b44bd0)

~~~diff
- 00ae4e78 ["INT_ADD", "register:40f0:8", ["const:ae4e78:8", "const:4:8"]]
- 00ae4e78 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b44bfc ["INT_ADD", "register:40f0:8", ["const:b44bfc:8", "const:4:8"]]
+ 00b44bfc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae4e78 bytes 86e40394
+ 00b44bfc bytes c5570494
- 00ae4e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
- 00ae4e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b44c04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:228:8"]]
+ 00b44c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4e80 bytes 80b601f9
+ 00b44c04 bytes 801601f9
- 00ae4e4c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b44bd0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae4e4c bytes f42d0090
+ 00b44bd0 bytes 142f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4533bf67aee77c114e90bc8d631c3aee"></a>

### [`00ae4eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md) → [`00b44c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md) _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) · 呼出先 5件 [`00af15f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)
- 新版 呼出元 1件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) · 呼出先 5件 [`00b51378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51378.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.71% / 新版 78.71%

CFGの説明率　旧版 56.52% / 新版 47.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4ec8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4ef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4ef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b44c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae50a0"
      ]
    ]
  ],
  "added": [
    [
      "00b44c4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b44c74",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b44c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44e24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md#insn-00ae4ec8) · [`00ae4ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md#insn-00ae4ef0) · [`00ae4f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md#insn-00ae4f10)
- 新版 [`00b44c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44c34.md#insn-00b44c94)

~~~diff
- 00ae4ec8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae4ec8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae4ec8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00ae4ec8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4ec8 bytes fd7b17a9
- 00ae4ef0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ae4ef0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00ae4ef0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae4ef0 bytes a8031af8
- 00ae4f10 ["INT_ADD", "register:40f0:8", ["const:ae4f10:8", "const:4:8"]]
- 00ae4f10 ["CALL", null, ["callee:00c5ad30:8"]]
+ 00b44c94 ["INT_ADD", "register:40f0:8", ["const:b44c94:8", "const:4:8"]]
+ 00b44c94 ["CALL", null, ["callee:00c5ad30:8"]]
- 00ae4f10 bytes e8e40394
+ 00b44c94 bytes 27580494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae3f7d633608eab9a7324b56e7e86f41"></a>

### [`00ae5158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md) → [`00b44edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44edc.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae5184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44f08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44ef0",
      "incomplete_value": true,
      "site": "00b44ef0",
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
      "definition_site": "00ae516c",
      "incomplete_value": true,
      "site": "00ae516c",
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
      "00b44eec",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5188"
      ]
    ],
    [
      "unmatched:00ae5178",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b44eec",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b44f0c"
      ]
    ],
    [
      "00b44efc",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae517c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md#insn-00ae517c) · [`00ae5184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md#insn-00ae5184) · [`00ae5194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md#insn-00ae5194)

~~~diff
- 00ae517c ["INT_ADD", "register:40f0:8", ["const:ae517c:8", "const:4:8"]]
- 00ae517c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae517c bytes c5e30394
- 00ae5184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00ae5184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5184 bytes 60ca01f9
- 00ae5194 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5194 ["RETURN", null, ["register:0:8"]]
- 00ae5194 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94214f50c569aa7ed509cda001e55c96"></a>

### [`00ae5198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md) → [`00b44f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f1c.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00ae51c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44f48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44f30",
      "incomplete_value": true,
      "site": "00b44f30",
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
      "definition_site": "00ae51ac",
      "incomplete_value": true,
      "site": "00ae51ac",
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
      "00b44f2c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae51b4",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae51bc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b44f2c",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44f38",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "00b44f40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae51ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md#insn-00ae51ac) · [`00ae51bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md#insn-00ae51bc) · [`00ae51c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md#insn-00ae51c4)
- 新版 [`00b44f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f1c.md#insn-00b44f30)

~~~diff
- 00ae51ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae51ac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b44f30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44f30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae51ac bytes e80000b5
+ 00b44f30 bytes e80000b5
- 00ae51bc ["INT_ADD", "register:40f0:8", ["const:ae51bc:8", "const:4:8"]]
- 00ae51bc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae51bc bytes b5e30394
- 00ae51c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00ae51c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae51c4 bytes 60ca01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a10abaa2dc2b334ef977532e0e53d67"></a>

### [`00ae51d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md) → [`00b44f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f5c.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae5208"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44f8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44f70",
      "incomplete_value": true,
      "site": "00b44f70",
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
      "definition_site": "00ae51ec",
      "incomplete_value": true,
      "site": "00ae51ec",
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
      "00b44f6c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae51f8",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5200",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b44f6c",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44f7c",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "00b44f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae51ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md#insn-00ae51ec) · [`00ae5200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md#insn-00ae5200) · [`00ae5208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md#insn-00ae5208)
- 新版 [`00b44f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44f5c.md#insn-00b44f70)

~~~diff
- 00ae51ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae51ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b44f70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44f70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae51ec bytes 080100b5
+ 00b44f70 bytes 080100b5
- 00ae5200 ["INT_ADD", "register:40f0:8", ["const:ae5200:8", "const:4:8"]]
- 00ae5200 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5200 bytes a4e30394
- 00ae5208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00ae5208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5208 bytes 60ca01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de5776c78e9f53f9e4a7d62b1d7863ef"></a>

### [`00ae521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md) → [`00b44fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae524c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44fd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b44fb4",
      "incomplete_value": true,
      "site": "00b44fb4",
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
      "definition_site": "00ae5230",
      "incomplete_value": true,
      "site": "00ae5230",
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
      "00b44fb0",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5238",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae524c",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b44fb0",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b44fbc",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "00b44fd0",
      "WRITE",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md#insn-00ae5230) · [`00ae5244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md#insn-00ae5244) · [`00ae524c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md#insn-00ae524c)
- 新版 [`00b44fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md#insn-00b44fb4) · [`00b44fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44fa0.md#insn-00b44fc8)

~~~diff
- 00ae5230 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5230 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b44fb4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b44fb4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5230 bytes 080100b5
+ 00b44fb4 bytes 080100b5
- 00ae5244 ["INT_ADD", "register:40f0:8", ["const:ae5244:8", "const:4:8"]]
- 00ae5244 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b44fc8 ["INT_ADD", "register:40f0:8", ["const:b44fc8:8", "const:4:8"]]
+ 00b44fc8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5244 bytes 93e30394
+ 00b44fc8 bytes d2560494
- 00ae524c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00ae524c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae524c bytes 60ca01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5b66a0631f035bbc2c6a021947cef62"></a>

### [`00ae526c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md) → [`00b44ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ff0.md) _ZN8firebase4util17jniresultcallback15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 28.57% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45078",
      "incomplete_value": true,
      "site": "00b45078",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae52f4",
      "incomplete_value": true,
      "site": "00ae52f4",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae52ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae52c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45004",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45010",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae52f8"
      ]
    ],
    [
      "unmatched:00ae52a0",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45004",
      "READ",
      [
        "storage",
        "01125258",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45010",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4507c"
      ]
    ],
    [
      "00b45024",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md#insn-00ae52ac) · [`00ae52c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md#insn-00ae52c0) · [`00ae52f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md#insn-00ae52f4)
- 新版 [`00b45078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ff0.md#insn-00b45078)

~~~diff
- 00ae52ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae52ac ["INT_ADD", "register:40f0:8", ["const:ae52ac:8", "const:4:8"]]
- 00ae52ac ["CALLIND", null, ["register:0:8"]]
- 00ae52ac bytes 00013fd6
- 00ae52c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae52c0 ["INT_ADD", "register:40f0:8", ["const:ae52c0:8", "const:4:8"]]
- 00ae52c0 ["CALLIND", null, ["register:0:8"]]
- 00ae52c0 bytes 00013fd6
- 00ae52f4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae52f4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:398:8"]]
- 00ae52f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b45078 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b45078 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:258:8"]]
+ 00b45078 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae52f4 bytes a0620e39
+ 00b45078 bytes a0620939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e452bbf4af245a8ea16894453903a47"></a>

### [`00ae5308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md) → [`00b4508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md) _ZN8firebase4util17jniresultcallback12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 55.56% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5344"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45118",
      "incomplete_value": true,
      "site": "00b45118",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5394",
      "incomplete_value": true,
      "site": "00ae5394",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b450c8"
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
      "00b450a0",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b450ac",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae5344",
      "WRITE",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b450a0",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b450ac",
      "READ",
      [
        "storage",
        "01125258",
        null,
        "undefined1"
      ]
    ],
    [
      "00b450c8",
      "WRITE",
      [
        "storage",
        "01125258",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md#insn-00ae5320) · [`00ae5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md#insn-00ae5344) · [`00ae5390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md#insn-00ae5390)
- 新版 [`00b450a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md#insn-00b450a4) · [`00b45114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md#insn-00b45114)

~~~diff
- 00ae5320 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5320 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b450a4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b450a4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae5320 bytes c10300b4
+ 00b450a4 bytes c10300b4
- 00ae5344 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5344 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5344 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:398:8"]]
- 00ae5344 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5344 bytes bf620e39
- 00ae5390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5390 ["INT_ADD", "register:40f0:8", ["const:ae5390:8", "const:4:8"]]
- 00ae5390 ["CALLIND", null, ["register:0:8"]]
+ 00b45114 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45114 ["INT_ADD", "register:40f0:8", ["const:b45114:8", "const:4:8"]]
+ 00b45114 ["CALLIND", null, ["register:0:8"]]
- 00ae5390 bytes 00013fd6
+ 00b45114 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72d563d440a5239ab1e4ce8303f9e06a"></a>

### [`00ae53a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md) → [`00b4512c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md) _ZN8firebase4util17jniresultcallback14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00b4516c",
      "incomplete_value": true,
      "site": "00b4516c",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae53e8",
      "incomplete_value": true,
      "site": "00ae53e8",
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
            "const:390:8"
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
      "definition_site": "00b45148",
      "incomplete_value": true,
      "site": "00b45148",
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
      "definition_site": "00ae53c4",
      "incomplete_value": true,
      "site": "00ae53c4",
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
      "definition_site": "00b45150",
      "incomplete_value": false,
      "site": "00b45164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae53cc",
      "incomplete_value": false,
      "site": "00ae53e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "00b45140",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45150",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00b4516c",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45140",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45150",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "00b4516c",
      "WRITE",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae53e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md#insn-00ae53e0) · [`00ae53e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md#insn-00ae53e8) · [`00ae53b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md#insn-00ae53b4)
- 新版 [`00b45164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md#insn-00b45164) · [`00b4516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md#insn-00b4516c) · [`00b45138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4512c.md#insn-00b45138)

~~~diff
- 00ae53e0 ["INT_ADD", "register:40f0:8", ["const:ae53e0:8", "const:4:8"]]
- 00ae53e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45164 ["INT_ADD", "register:40f0:8", ["const:b45164:8", "const:4:8"]]
+ 00b45164 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae53e0 bytes 2ce30394
+ 00b45164 bytes 6b560494
- 00ae53e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
- 00ae53e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4516c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
+ 00b4516c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae53e8 bytes 80ca01f9
+ 00b4516c bytes 802a01f9
- 00ae53b4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b45138 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae53b4 bytes d42d00f0
+ 00b45138 bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-343ce8e3cdb603c8b62022fc3b76f147"></a>

### [`00ae5454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md) → [`00b451d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md) _ZN8firebase4util17jniresultcallback13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b45218",
      "incomplete_value": true,
      "site": "00b45218",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5494",
      "incomplete_value": true,
      "site": "00ae5494",
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
            "const:390:8"
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
      "definition_site": "00b451f4",
      "incomplete_value": true,
      "site": "00b451f4",
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
      "definition_site": "00ae5470",
      "incomplete_value": true,
      "site": "00ae5470",
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
      "definition_site": "00b451fc",
      "incomplete_value": false,
      "site": "00b45210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5478",
      "incomplete_value": false,
      "site": "00ae548c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "00b451ec",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b451fc",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00b45218",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b451ec",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ],
    [
      "00b451fc",
      "PARAM",
      [
        "storage",
        "002b04bd",
        null,
        "string"
      ]
    ],
    [
      "00b45218",
      "WRITE",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae548c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md#insn-00ae548c) · [`00ae5494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md#insn-00ae5494) · [`00ae5460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md#insn-00ae5460)
- 新版 [`00b45210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md#insn-00b45210) · [`00b45218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md#insn-00b45218) · [`00b451e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b451d8.md#insn-00b451e4)

~~~diff
- 00ae548c ["INT_ADD", "register:40f0:8", ["const:ae548c:8", "const:4:8"]]
- 00ae548c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45210 ["INT_ADD", "register:40f0:8", ["const:b45210:8", "const:4:8"]]
+ 00b45210 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae548c bytes 01e30394
+ 00b45210 bytes 40560494
- 00ae5494 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
- 00ae5494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b45218 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:250:8"]]
+ 00b45218 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5494 bytes 80ca01f9
+ 00b45218 bytes 802a01f9
- 00ae5460 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b451e4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae5460 bytes d42d00f0
+ 00b451e4 bytes 142f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c1eba99c6f277ddb8814a0e56338f4"></a>

### [`00ae54c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md) → [`00b45248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md) _ZN8firebase4util17jniresultcallback10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b45264",
      "incomplete_value": false,
      "site": "00b45268",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae54e0",
      "incomplete_value": false,
      "site": "00ae54e4",
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
      "definition_site": "00b45274",
      "incomplete_value": true,
      "site": "00b45280",
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
      "definition_site": "00ae54f0",
      "incomplete_value": true,
      "site": "00ae54fc",
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
      "00b45264",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b45274",
      "DATA",
      [
        "storage",
        "010a03b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b45264",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b45274",
      "DATA",
      [
        "storage",
        "01125270",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae54e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md#insn-00ae54e4) · [`00ae54dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md#insn-00ae54dc) · [`00ae54e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md#insn-00ae54e0)
- 新版 [`00b45268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md#insn-00b45268) · [`00b45260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md#insn-00b45260) · [`00b45264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md#insn-00b45264)

~~~diff
- 00ae54e4 ["INT_ADD", "register:40f0:8", ["const:ae54e4:8", "const:4:8"]]
- 00ae54e4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b45268 ["INT_ADD", "register:40f0:8", ["const:b45268:8", "const:4:8"]]
+ 00b45268 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae54e4 bytes 27e30394
+ 00b45268 bytes 66560494
- 00ae54dc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b45260 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae54dc bytes a0bdff90
+ 00b45260 bytes 20bbff90
- 00ae54e0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae54e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae54e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae54e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b45264 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b45264 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b45264 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b45264 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae54e0 bytes 00c81791
+ 00b45264 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4084d1804f9e85b788849b09a86a27a"></a>

### [`00ae5500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md) → [`00b45284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45284.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae5500"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5500",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5504",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45294",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45284",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45288",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45294",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md#insn-00ae5500) · [`00ae5504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md#insn-00ae5504) · [`00ae5514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md#insn-00ae5514)
- 新版 [`00b45298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45284.md#insn-00b45298)

~~~diff
- 00ae5500 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae5500 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae5500 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5500 bytes f30f1ef8
- 00ae5504 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5504 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5504 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5504 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5504 bytes fd7b01a9
- 00ae5514 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5514 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b45298 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45298 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5514 bytes e80000b5
+ 00b45298 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae1f5a2ca1b3d59bcc8d7da81ad1c889"></a>

### [`00ae5540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md) → [`00b452c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b452c4.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 50.00% / 新版 40.00%

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
      "site": "00ae556c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b452f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b452d8",
      "incomplete_value": true,
      "site": "00b452d8",
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
      "definition_site": "00ae5554",
      "incomplete_value": true,
      "site": "00ae5554",
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
      "00b452d4",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae555c",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5564",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b452d4",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b452e0",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ],
    [
      "00b452e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md#insn-00ae5554) · [`00ae5564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md#insn-00ae5564) · [`00ae556c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md#insn-00ae556c)
- 新版 [`00b452d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b452c4.md#insn-00b452d8)

~~~diff
- 00ae5554 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5554 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b452d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b452d8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae5554 bytes e80000b5
+ 00b452d8 bytes e80000b5
- 00ae5564 ["INT_ADD", "register:40f0:8", ["const:ae5564:8", "const:4:8"]]
- 00ae5564 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5564 bytes cbe20394
- 00ae556c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
- 00ae556c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae556c bytes 60de01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d448de36081c2dcc206ae2e6eb93022d"></a>

### [`00ae5580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md) → [`00b45304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45304.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae55b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45334"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45318",
      "incomplete_value": true,
      "site": "00b45318",
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
      "definition_site": "00ae5594",
      "incomplete_value": true,
      "site": "00ae5594",
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
      "00b45314",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae55a0",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae55a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b45314",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45324",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ],
    [
      "00b4532c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md#insn-00ae5594) · [`00ae55a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md#insn-00ae55a8) · [`00ae55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md#insn-00ae55b0)
- 新版 [`00b45318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45304.md#insn-00b45318)

~~~diff
- 00ae5594 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5594 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b45318 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45318 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5594 bytes 080100b5
+ 00b45318 bytes 080100b5
- 00ae55a8 ["INT_ADD", "register:40f0:8", ["const:ae55a8:8", "const:4:8"]]
- 00ae55a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae55a8 bytes bae20394
- 00ae55b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
- 00ae55b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae55b0 bytes 60de01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a37c4a596a2ae4d69edc70d04774675"></a>

### [`00ae55c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md) → [`00b45348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45348.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae55f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45378"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae55d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae55d4",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae55d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4537c"
      ]
    ],
    [
      "unmatched:00ae55e0",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45358",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4535c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4537c"
      ]
    ],
    [
      "00b45364",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae55d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md#insn-00ae55d8) · [`00ae55ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md#insn-00ae55ec) · [`00ae55f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md#insn-00ae55f4)
- 新版 [`00b45370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45348.md#insn-00b45370)

~~~diff
- 00ae55d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae55d8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae55d8 bytes 080100b5
- 00ae55ec ["INT_ADD", "register:40f0:8", ["const:ae55ec:8", "const:4:8"]]
- 00ae55ec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45370 ["INT_ADD", "register:40f0:8", ["const:b45370:8", "const:4:8"]]
+ 00b45370 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae55ec bytes a9e20394
+ 00b45370 bytes e8550494
- 00ae55f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
- 00ae55f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae55f4 bytes 60de01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4d332dd1fe1bd1f87aaa860e5b174cc"></a>

### [`00ae5614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md) → [`00b45398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45398.md) _ZN8firebase4util26cppthreaddispatchercontext15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5618"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5614",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5618",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae561c",
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
      "00b45398",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4539c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b453a0",
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

- 旧版 [`00ae5614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md#insn-00ae5614) · [`00ae5618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md#insn-00ae5618) · [`00ae561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md#insn-00ae561c)

~~~diff
- 00ae5614 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae5614 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae5614 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5614 bytes f50f1df8
- 00ae5618 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae5618 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae5618 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5618 bytes f44f01a9
- 00ae561c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae561c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae561c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae561c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae561c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98c512c1da7e24f5541f7af717796c0"></a>

### [`00ae56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md) → [`00b45434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45434.md) _ZN8firebase4util26cppthreaddispatchercontext12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 55.56% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae56ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b454c0",
      "incomplete_value": true,
      "site": "00b454c0",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae573c",
      "incomplete_value": true,
      "site": "00ae573c",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45470"
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
      "00b45448",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45454",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae56ec",
      "WRITE",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45448",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45454",
      "READ",
      [
        "storage",
        "01125280",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45470",
      "WRITE",
      [
        "storage",
        "01125280",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae56c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md#insn-00ae56c8) · [`00ae56ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md#insn-00ae56ec) · [`00ae5724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md#insn-00ae5724)
- 新版 [`00b4544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45434.md#insn-00b4544c)

~~~diff
- 00ae56c8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae56c8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b4544c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4544c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae56c8 bytes c10300b4
+ 00b4544c bytes c10300b4
- 00ae56ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae56ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae56ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3c0:8"]]
- 00ae56ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae56ec bytes bf020f39
- 00ae5724 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5724 ["INT_ADD", "register:40f0:8", ["const:ae5724:8", "const:4:8"]]
- 00ae5724 ["CALLIND", null, ["register:0:8"]]
- 00ae5724 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1e99e55bbf2c152ca290466f91a692d"></a>

### [`00ae5750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md) → [`00b454d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b454d4.md) _ZN8firebase4util26cppthreaddispatchercontext14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae5790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45514"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae576c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5764",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae576c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45518"
      ]
    ],
    [
      "unmatched:00ae5774",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b454e8",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b454f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45518"
      ]
    ],
    [
      "00b454f8",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae576c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md#insn-00ae576c) · [`00ae5788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md#insn-00ae5788) · [`00ae5790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md#insn-00ae5790)
- 新版 [`00b4550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b454d4.md#insn-00b4550c)

~~~diff
- 00ae576c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae576c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae576c bytes 410100b5
- 00ae5788 ["INT_ADD", "register:40f0:8", ["const:ae5788:8", "const:4:8"]]
- 00ae5788 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4550c ["INT_ADD", "register:40f0:8", ["const:b4550c:8", "const:4:8"]]
+ 00b4550c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5788 bytes 42e20394
+ 00b4550c bytes 81550494
- 00ae5790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
- 00ae5790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5790 bytes 80de01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df0c17fce0db7c85a010516534a5cab4"></a>

### [`00ae57fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md) → [`00b45580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45580.md) _ZN8firebase4util26cppthreaddispatchercontext13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae583c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b455c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5818"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5810",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5818",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b455c4"
      ]
    ],
    [
      "unmatched:00ae5820",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45594",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4559c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b455c4"
      ]
    ],
    [
      "00b455a4",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md#insn-00ae5818) · [`00ae5834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md#insn-00ae5834) · [`00ae583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md#insn-00ae583c)
- 新版 [`00b455b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45580.md#insn-00b455b8)

~~~diff
- 00ae5818 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5818 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5818 bytes 410100b5
- 00ae5834 ["INT_ADD", "register:40f0:8", ["const:ae5834:8", "const:4:8"]]
- 00ae5834 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b455b8 ["INT_ADD", "register:40f0:8", ["const:b455b8:8", "const:4:8"]]
+ 00b455b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5834 bytes 17e20394
+ 00b455b8 bytes 56550494
- 00ae583c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
- 00ae583c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae583c bytes 80de01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70787707cff521e7f4763553132a520e"></a>

### [`00ae58a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md) → [`00b4562c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4562c.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae58d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45658"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45640",
      "incomplete_value": true,
      "site": "00b45640",
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
      "definition_site": "00ae58bc",
      "incomplete_value": true,
      "site": "00ae58bc",
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
      "00b4563c",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae58d8"
      ]
    ],
    [
      "unmatched:00ae58c8",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4563c",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4565c"
      ]
    ],
    [
      "00b4564c",
      "PARAM",
      [
        "storage",
        "002bad63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae58bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md#insn-00ae58bc) · [`00ae58cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md#insn-00ae58cc) · [`00ae58d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md#insn-00ae58d4)
- 新版 [`00b45640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4562c.md#insn-00b45640)

~~~diff
- 00ae58bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae58bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b45640 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45640 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae58bc bytes e80000b5
+ 00b45640 bytes e80000b5
- 00ae58cc ["INT_ADD", "register:40f0:8", ["const:ae58cc:8", "const:4:8"]]
- 00ae58cc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae58cc bytes f1e10394
- 00ae58d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
- 00ae58d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae58d4 bytes 60fa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-740193d1a2f1061fbdb8f5a310ec3ab1"></a>

### [`00ae596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md) → [`00b456f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456f0.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae596c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5970"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae596c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5970",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45700",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b456f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b456f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45700",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md#insn-00ae596c) · [`00ae5970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md#insn-00ae5970) · [`00ae5980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md#insn-00ae5980)
- 新版 [`00b45704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b456f0.md#insn-00b45704)

~~~diff
- 00ae596c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae596c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae596c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae596c bytes f30f1ef8
- 00ae5970 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5970 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5970 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5970 bytes fd7b01a9
- 00ae5980 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5980 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b45704 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45704 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae5980 bytes 080100b5
+ 00b45704 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-778adbc95f26af3c518a0911d541544e"></a>

### [`00ae59bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md) → [`00b45740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45740.md) _ZN8firebase4util19cppthreaddispatcher15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 58.97% / 新版 58.97%

CFGの説明率　旧版 42.86% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b457c8",
      "incomplete_value": true,
      "site": "00b457c8",
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
            "const:2b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5a44",
      "incomplete_value": true,
      "site": "00ae5a44",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae59fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5a10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45754",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae59f0",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b457c8",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45754",
      "READ",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45774",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b457c8",
      "WRITE",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae59fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md#insn-00ae59fc) · [`00ae5a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md#insn-00ae5a10) · [`00ae5a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md#insn-00ae5a28)

~~~diff
- 00ae59fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae59fc ["INT_ADD", "register:40f0:8", ["const:ae59fc:8", "const:4:8"]]
- 00ae59fc ["CALLIND", null, ["register:0:8"]]
- 00ae59fc bytes 00013fd6
- 00ae5a10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5a10 ["INT_ADD", "register:40f0:8", ["const:ae5a10:8", "const:4:8"]]
- 00ae5a10 ["CALLIND", null, ["register:0:8"]]
- 00ae5a10 bytes 00013fd6
- 00ae5a28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5a28 ["INT_ADD", "register:40f0:8", ["const:ae5a28:8", "const:4:8"]]
- 00ae5a28 ["CALLIND", null, ["register:0:8"]]
- 00ae5a28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b42737343da9756bab5ace2f13b06cb5"></a>

### [`00ae5a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md) → [`00b457dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b457dc.md) _ZN8firebase4util19cppthreaddispatcher12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 44.44% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5a94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b45868",
      "incomplete_value": true,
      "site": "00b45868",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ae4",
      "incomplete_value": true,
      "site": "00ae5ae4",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45818"
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
      "00b457f0",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b457fc",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae5a94",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b457f0",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b457fc",
      "READ",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45818",
      "WRITE",
      [
        "storage",
        "011252b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md#insn-00ae5a70) · [`00ae5a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md#insn-00ae5a90) · [`00ae5a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md#insn-00ae5a94)
- 新版 [`00b457f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b457dc.md#insn-00b457f4)

~~~diff
- 00ae5a70 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5a70 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b457f4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b457f4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae5a70 bytes c10300b4
+ 00b457f4 bytes c10300b4
- 00ae5a90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5a90 ["INT_ADD", "register:40f0:8", ["const:ae5a90:8", "const:4:8"]]
- 00ae5a90 ["CALLIND", null, ["register:0:8"]]
- 00ae5a90 bytes 00013fd6
- 00ae5a94 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5a94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5a94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3f8:8"]]
- 00ae5a94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5a94 bytes bfe20f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fd609c6bcaef4264fe71a77b441f8ba"></a>

### [`00ae5af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md) → [`00b4587c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4587c.md) _ZN8firebase4util19cppthreaddispatcher14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae5b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b458bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5b14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5b0c",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b458c0"
      ]
    ],
    [
      "unmatched:00ae5b1c",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45890",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45898",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b458c0"
      ]
    ],
    [
      "00b458a0",
      "PARAM",
      [
        "storage",
        "002bad63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md#insn-00ae5b14) · [`00ae5b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md#insn-00ae5b30) · [`00ae5b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md#insn-00ae5b38)
- 新版 [`00b458b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4587c.md#insn-00b458b4)

~~~diff
- 00ae5b14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5b14 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5b14 bytes 410100b5
- 00ae5b30 ["INT_ADD", "register:40f0:8", ["const:ae5b30:8", "const:4:8"]]
- 00ae5b30 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b458b4 ["INT_ADD", "register:40f0:8", ["const:b458b4:8", "const:4:8"]]
+ 00b458b4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5b30 bytes 58e10394
+ 00b458b4 bytes 97540494
- 00ae5b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
- 00ae5b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5b38 bytes 80fa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c34cf7c2b323c09487bed1ed2d7f07b5"></a>

### [`00ae5ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md) → [`00b45928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45928.md) _ZN8firebase4util19cppthreaddispatcher13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae5be4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45968"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5bc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5bb8",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5bc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4596c"
      ]
    ],
    [
      "unmatched:00ae5bc8",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4593c",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45944",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4596c"
      ]
    ],
    [
      "00b4594c",
      "PARAM",
      [
        "storage",
        "002bad63",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md#insn-00ae5bc0) · [`00ae5bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md#insn-00ae5bdc) · [`00ae5be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md#insn-00ae5be4)
- 新版 [`00b45960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45928.md#insn-00b45960)

~~~diff
- 00ae5bc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5bc0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5bc0 bytes 410100b5
- 00ae5bdc ["INT_ADD", "register:40f0:8", ["const:ae5bdc:8", "const:4:8"]]
- 00ae5bdc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45960 ["INT_ADD", "register:40f0:8", ["const:b45960:8", "const:4:8"]]
+ 00b45960 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5bdc bytes 2de10394
+ 00b45960 bytes 6c540494
- 00ae5be4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
- 00ae5be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5be4 bytes 80fa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ce216612f8995545d9d956ffd17753c"></a>

### [`00ae5c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md) → [`00b459d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b459d4.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae5c50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5c54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5c54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5c50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5c54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b459e4",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b459d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b459d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b459e4",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md#insn-00ae5c50) · [`00ae5c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md#insn-00ae5c54) · [`00ae5c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md#insn-00ae5c64)
- 新版 [`00b459e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b459d4.md#insn-00b459e8)

~~~diff
- 00ae5c50 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae5c50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae5c50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5c50 bytes f30f1ef8
- 00ae5c54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5c54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5c54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5c54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5c54 bytes fd7b01a9
- 00ae5c64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5c64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b459e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b459e8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae5c64 bytes e80000b5
+ 00b459e8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f33c11857217136e6a3f52193f6b55a1"></a>

### [`00ae5d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md) → [`00b45a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45ac8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45aac",
      "incomplete_value": true,
      "site": "00b45aac",
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
      "definition_site": "00ae5d28",
      "incomplete_value": true,
      "site": "00ae5d28",
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
      "00b45aa8",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45aac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5d48"
      ]
    ],
    [
      "unmatched:00ae5d30",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45aa8",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45aac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45acc"
      ]
    ],
    [
      "00b45ab4",
      "PARAM",
      [
        "storage",
        "002bbd77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md#insn-00ae5d28) · [`00ae5d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md#insn-00ae5d3c) · [`00ae5d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md#insn-00ae5d44)
- 新版 [`00b45aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md#insn-00b45aac) · [`00b45ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45a98.md#insn-00b45ac0)

~~~diff
- 00ae5d28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5d28 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45aac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45aac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5d28 bytes 080100b5
+ 00b45aac bytes 080100b5
- 00ae5d3c ["INT_ADD", "register:40f0:8", ["const:ae5d3c:8", "const:4:8"]]
- 00ae5d3c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45ac0 ["INT_ADD", "register:40f0:8", ["const:b45ac0:8", "const:4:8"]]
+ 00b45ac0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5d3c bytes d5e00394
+ 00b45ac0 bytes 14540494
- 00ae5d44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00ae5d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5d44 bytes 600e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b256c1accd4d420e4a2f8b6f75812eb5"></a>

### [`00ae5e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md) → [`00b45b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md) _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5e3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5e8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45bc0"
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
      "00b45b98",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45ba4",
      "READ",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5e40"
      ]
    ]
  ],
  "added": [
    [
      "00b45b98",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45ba4",
      "READ",
      [
        "storage",
        "011252e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45bc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md#insn-00ae5e18) · [`00ae5e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md#insn-00ae5e3c) · [`00ae5e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md#insn-00ae5e4c)
- 新版 [`00b45b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45b84.md#insn-00b45b9c)

~~~diff
- 00ae5e18 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5e18 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b45b9c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b45b9c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00ae5e18 bytes c10300b4
+ 00b45b9c bytes c10300b4
- 00ae5e3c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5e3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5e3c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:420:8"]]
- 00ae5e3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5e3c bytes bf821039
- 00ae5e4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5e4c ["INT_ADD", "register:40f0:8", ["const:ae5e4c:8", "const:4:8"]]
- 00ae5e4c ["CALLIND", null, ["register:0:8"]]
- 00ae5e4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93ffa6cd289f2a0a48702ff2640ab25a"></a>

### [`00ae5ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md) → [`00b45c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae5ee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45c64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5ebc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5eb4",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5ebc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45c68"
      ]
    ],
    [
      "unmatched:00ae5ec4",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45c38",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45c68"
      ]
    ],
    [
      "00b45c48",
      "PARAM",
      [
        "storage",
        "002bbd77",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md#insn-00ae5ebc) · [`00ae5ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md#insn-00ae5ed8) · [`00ae5ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md#insn-00ae5ee0)
- 新版 [`00b45c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45c24.md#insn-00b45c5c)

~~~diff
- 00ae5ebc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5ebc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5ebc bytes 410100b5
- 00ae5ed8 ["INT_ADD", "register:40f0:8", ["const:ae5ed8:8", "const:4:8"]]
- 00ae5ed8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45c5c ["INT_ADD", "register:40f0:8", ["const:b45c5c:8", "const:4:8"]]
+ 00b45c5c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae5ed8 bytes 6ee00394
+ 00b45c5c bytes ad530494
- 00ae5ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00ae5ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5ee0 bytes 800e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a1c55c9f92dcfced91ebbc519d3e3e8"></a>

### [`00ae5f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md) → [`00b45cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45cd0.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5f4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5f4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5f50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5f4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5f60",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b45ce4",
      "READ",
      [
        "storage",
        "011252d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md#insn-00ae5f4c) · [`00ae5f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md#insn-00ae5f50) · [`00ae5f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md#insn-00ae5f68)

~~~diff
- 00ae5f4c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae5f4c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae5f4c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae5f4c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5f4c bytes f44fbea9
- 00ae5f50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5f50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5f50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5f50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5f50 bytes fd7b01a9
- 00ae5f68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5f68 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5f68 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a860d07397f3f403e0cdcfdd19cb8198"></a>

### [`00ae5ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md) → [`00b45d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae6024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45da8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45d90",
      "incomplete_value": true,
      "site": "00b45d90",
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
      "definition_site": "00ae600c",
      "incomplete_value": true,
      "site": "00ae600c",
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
      "00b45d8c",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45d90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6028"
      ]
    ],
    [
      "unmatched:00ae6018",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45d8c",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45d90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45dac"
      ]
    ],
    [
      "00b45d9c",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md#insn-00ae600c) · [`00ae601c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md#insn-00ae601c) · [`00ae6024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md#insn-00ae6024)
- 新版 [`00b45d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45d7c.md#insn-00b45d90)

~~~diff
- 00ae600c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae600c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b45d90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45d90 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae600c bytes e80000b5
+ 00b45d90 bytes e80000b5
- 00ae601c ["INT_ADD", "register:40f0:8", ["const:ae601c:8", "const:4:8"]]
- 00ae601c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae601c bytes 1de00394
- 00ae6024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00ae6024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6024 bytes 601e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58405552553d1848ed755720bb15655"></a>

### [`00ae6038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md) → [`00b45dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 25.00% / 新版 16.67%

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
      "site": "00ae6064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45de8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b45dd0",
      "incomplete_value": true,
      "site": "00b45dd0",
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
      "definition_site": "00ae604c",
      "incomplete_value": true,
      "site": "00ae604c",
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
      "00b45dcc",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6068"
      ]
    ],
    [
      "unmatched:00ae6054",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45dcc",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45dd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45dec"
      ]
    ],
    [
      "00b45dd8",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae604c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md#insn-00ae604c) · [`00ae605c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md#insn-00ae605c) · [`00ae6064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md#insn-00ae6064)
- 新版 [`00b45dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45dbc.md#insn-00b45dd0)

~~~diff
- 00ae604c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae604c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b45dd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b45dd0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae604c bytes e80000b5
+ 00b45dd0 bytes e80000b5
- 00ae605c ["INT_ADD", "register:40f0:8", ["const:ae605c:8", "const:4:8"]]
- 00ae605c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae605c bytes 0de00394
- 00ae6064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00ae6064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6064 bytes 601e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c57558bd0f4b67322f530b3a21c15ec6"></a>

### [`00ae60bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md) → [`00b45e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae60ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45e70"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae60d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45e50",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae60d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45e74"
      ]
    ],
    [
      "unmatched:00ae60d8",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45e50",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45e74"
      ]
    ],
    [
      "00b45e5c",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae60d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md#insn-00ae60d0) · [`00ae60e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md#insn-00ae60e4) · [`00ae60ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md#insn-00ae60ec)
- 新版 [`00b45e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e40.md#insn-00b45e68)

~~~diff
- 00ae60d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae60d0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae60d0 bytes 080100b5
- 00ae60e4 ["INT_ADD", "register:40f0:8", ["const:ae60e4:8", "const:4:8"]]
- 00ae60e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b45e68 ["INT_ADD", "register:40f0:8", ["const:b45e68:8", "const:4:8"]]
+ 00b45e68 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae60e4 bytes ebdf0394
+ 00b45e68 bytes 2a530494
- 00ae60ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00ae60ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae60ec bytes 601e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e650323126b654894bb3cee7da3870a"></a>

### [`00ae610c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md) → [`00b45e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45f18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6168"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45ea4",
      "READ",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45eb0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6198"
      ]
    ],
    [
      "unmatched:00ae6140",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b45ea4",
      "READ",
      [
        "storage",
        "01125300",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45eb0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45f1c"
      ]
    ],
    [
      "00b45ec4",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae614c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md#insn-00ae614c) · [`00ae6160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md#insn-00ae6160) · [`00ae6168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md#insn-00ae6168)
- 新版 [`00b45ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45e90.md#insn-00b45ed0)

~~~diff
- 00ae614c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae614c ["INT_ADD", "register:40f0:8", ["const:ae614c:8", "const:4:8"]]
- 00ae614c ["CALLIND", null, ["register:0:8"]]
+ 00b45ed0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b45ed0 ["INT_ADD", "register:40f0:8", ["const:b45ed0:8", "const:4:8"]]
+ 00b45ed0 ["CALLIND", null, ["register:0:8"]]
- 00ae614c bytes 00013fd6
+ 00b45ed0 bytes 00013fd6
- 00ae6160 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6160 ["INT_ADD", "register:40f0:8", ["const:ae6160:8", "const:4:8"]]
- 00ae6160 ["CALLIND", null, ["register:0:8"]]
- 00ae6160 bytes 00013fd6
- 00ae6168 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00ae6168 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8891802a447a13fe1caedf200d9f63e"></a>

### [`00ae61a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md) → [`00b45f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45f2c.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 70.00% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae61a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae61ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae61ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae61a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae61ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae61b0",
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
      "00b45f2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b45f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b45f34",
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

- 旧版 [`00ae61a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md#insn-00ae61a8) · [`00ae61ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md#insn-00ae61ac) · [`00ae61b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md#insn-00ae61b0)

~~~diff
- 00ae61a8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae61a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae61a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae61a8 bytes f50f1df8
- 00ae61ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae61ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae61ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae61ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae61ac bytes f44f01a9
- 00ae61b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae61b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae61b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae61b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae61b0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aa236fc5c67ad5675170a3511ae02d7"></a>

### [`00ae6248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md) → [`00b45fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae6288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4600c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6264"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae625c",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6264",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46010"
      ]
    ],
    [
      "unmatched:00ae626c",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45fe0",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46010"
      ]
    ],
    [
      "00b45ff0",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md#insn-00ae6264) · [`00ae6280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md#insn-00ae6280) · [`00ae6288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md#insn-00ae6288)
- 新版 [`00b46004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45fcc.md#insn-00b46004)

~~~diff
- 00ae6264 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6264 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6264 bytes 410100b5
- 00ae6280 ["INT_ADD", "register:40f0:8", ["const:ae6280:8", "const:4:8"]]
- 00ae6280 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46004 ["INT_ADD", "register:40f0:8", ["const:b46004:8", "const:4:8"]]
+ 00b46004 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6280 bytes 84df0394
+ 00b46004 bytes c3520494
- 00ae6288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
- 00ae6288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6288 bytes 801e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92bc0abe7f356021839d15812e16535"></a>

### [`00ae62f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md) → [`00b46078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b460b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6310"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6308",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6310",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b460bc"
      ]
    ],
    [
      "unmatched:00ae6318",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4608c",
      "READ",
      [
        "storage",
        "011252f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46094",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b460bc"
      ]
    ],
    [
      "00b4609c",
      "PARAM",
      [
        "storage",
        "002af2cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md#insn-00ae6310) · [`00ae632c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md#insn-00ae632c) · [`00ae6334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md#insn-00ae6334)
- 新版 [`00b460b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46078.md#insn-00b460b0)

~~~diff
- 00ae6310 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6310 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6310 bytes 410100b5
- 00ae632c ["INT_ADD", "register:40f0:8", ["const:ae632c:8", "const:4:8"]]
- 00ae632c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b460b0 ["INT_ADD", "register:40f0:8", ["const:b460b0:8", "const:4:8"]]
+ 00b460b0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae632c bytes 59df0394
+ 00b460b0 bytes 98520494
- 00ae6334 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
- 00ae6334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6334 bytes 801e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5257f97b5606212f4be6b9c587ece0eb"></a>

### [`00ae63a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md) → [`00b46124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae63cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46150"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46138",
      "incomplete_value": true,
      "site": "00b46138",
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
      "definition_site": "00ae63b4",
      "incomplete_value": true,
      "site": "00ae63b4",
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
      "00b46134",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae63c0",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae63c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b46134",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46144",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b46148",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae63b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md#insn-00ae63b4) · [`00ae63c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md#insn-00ae63c4) · [`00ae63cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md#insn-00ae63cc)
- 新版 [`00b46138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46124.md#insn-00b46138)

~~~diff
- 00ae63b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae63b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46138 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46138 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae63b4 bytes e80000b5
+ 00b46138 bytes e80000b5
- 00ae63c4 ["INT_ADD", "register:40f0:8", ["const:ae63c4:8", "const:4:8"]]
- 00ae63c4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae63c4 bytes 33df0394
- 00ae63cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
- 00ae63cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae63cc bytes 603602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2282071b65f7448f046d71f9dd397d7"></a>

### [`00ae63e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md) → [`00b46164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b46190",
      "incomplete_value": true,
      "site": "00b46190",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae640c",
      "incomplete_value": true,
      "site": "00ae640c",
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
            "const:468:8"
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
      "definition_site": "00b46178",
      "incomplete_value": true,
      "site": "00b46178",
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
      "definition_site": "00ae63f4",
      "incomplete_value": true,
      "site": "00ae63f4",
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
      "definition_site": "00b46180",
      "incomplete_value": false,
      "site": "00b46188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63fc",
      "incomplete_value": false,
      "site": "00ae6404",
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
            "const:156:8"
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
      "00b46174",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46180",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      "00b46190",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46174",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46180",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b46190",
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md#insn-00ae6404) · [`00ae640c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md#insn-00ae640c) · [`00ae63ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md#insn-00ae63ec)
- 新版 [`00b46188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md#insn-00b46188) · [`00b46190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md#insn-00b46190) · [`00b46170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46164.md#insn-00b46170)

~~~diff
- 00ae6404 ["INT_ADD", "register:40f0:8", ["const:ae6404:8", "const:4:8"]]
- 00ae6404 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46188 ["INT_ADD", "register:40f0:8", ["const:b46188:8", "const:4:8"]]
+ 00b46188 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6404 bytes 23df0394
+ 00b46188 bytes 62520494
- 00ae640c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
- 00ae640c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00b46190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae640c bytes 603602f9
+ 00b46190 bytes 609601f9
- 00ae63ec ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b46170 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae63ec bytes d32d00d0
+ 00b46170 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7155e6bb018bee08d66a4e739c8bfb54"></a>

### [`00ae6420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md) → [`00b461a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae6450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b461d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b461b8",
      "incomplete_value": true,
      "site": "00b461b8",
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
      "definition_site": "00ae6434",
      "incomplete_value": true,
      "site": "00ae6434",
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
      "00b461b4",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6440",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6448",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b461b4",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b461c4",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b461cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md#insn-00ae6434) · [`00ae6448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md#insn-00ae6448) · [`00ae6450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md#insn-00ae6450)
- 新版 [`00b461b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461a4.md#insn-00b461b8)

~~~diff
- 00ae6434 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6434 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b461b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b461b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6434 bytes 080100b5
+ 00b461b8 bytes 080100b5
- 00ae6448 ["INT_ADD", "register:40f0:8", ["const:ae6448:8", "const:4:8"]]
- 00ae6448 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6448 bytes 12df0394
- 00ae6450 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
- 00ae6450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6450 bytes 603602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9230573704d0db47fbfa3239e8593bc"></a>

### [`00ae6464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md) → [`00b461e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae6494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46218"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b461fc",
      "incomplete_value": true,
      "site": "00b461fc",
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
      "definition_site": "00ae6478",
      "incomplete_value": true,
      "site": "00ae6478",
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
      "00b461f8",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6480",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6494",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b461f8",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46204",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ],
    [
      "00b46218",
      "WRITE",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md#insn-00ae6478) · [`00ae648c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md#insn-00ae648c) · [`00ae6494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md#insn-00ae6494)
- 新版 [`00b461fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md#insn-00b461fc) · [`00b46210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b461e8.md#insn-00b46210)

~~~diff
- 00ae6478 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6478 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b461fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b461fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6478 bytes 080100b5
+ 00b461fc bytes 080100b5
- 00ae648c ["INT_ADD", "register:40f0:8", ["const:ae648c:8", "const:4:8"]]
- 00ae648c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46210 ["INT_ADD", "register:40f0:8", ["const:b46210:8", "const:4:8"]]
+ 00b46210 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae648c bytes 01df0394
+ 00b46210 bytes 40520494
- 00ae6494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
- 00ae6494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6494 bytes 603602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-781af0039ac6ec6b7ea9a0255ec4aae9"></a>

### [`00ae64b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md) → [`00b46238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46238.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae64b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae64b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae64b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae64b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae64b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae64bc",
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
      "00b46238",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4623c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46240",
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

- 旧版 [`00ae64b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md#insn-00ae64b4) · [`00ae64b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md#insn-00ae64b8) · [`00ae64bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md#insn-00ae64bc)

~~~diff
- 00ae64b4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae64b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae64b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae64b4 bytes f50f1df8
- 00ae64b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae64b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae64b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae64b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae64b8 bytes f44f01a9
- 00ae64bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae64bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae64bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae64bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae64bc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ef5fe4344d1624ea35f23c0c7da352f"></a>

### [`00ae6550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md) → [`00b462d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae658c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae65dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46310"
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
      "00b462e8",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6568",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46364"
      ]
    ],
    [
      "00b462f4",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b462e8",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b462ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46364"
      ]
    ],
    [
      "00b462f4",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md#insn-00ae6568) · [`00ae658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md#insn-00ae658c) · [`00ae65b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md#insn-00ae65b4)
- 新版 [`00b46338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b462d4.md#insn-00b46338)

~~~diff
- 00ae6568 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6568 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae6568 bytes c10300b4
- 00ae658c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae658c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae658c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:470:8"]]
- 00ae658c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae658c bytes bfc21139
- 00ae65b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae65b4 ["INT_ADD", "register:40f0:8", ["const:ae65b4:8", "const:4:8"]]
- 00ae65b4 ["CALLIND", null, ["register:0:8"]]
+ 00b46338 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46338 ["INT_ADD", "register:40f0:8", ["const:b46338:8", "const:4:8"]]
+ 00b46338 ["CALLIND", null, ["register:0:8"]]
- 00ae65b4 bytes 00013fd6
+ 00b46338 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f1a77ec3de243bf99c826963a73a74"></a>

### [`00ae65f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md) → [`00b46374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae6630"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b463b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae660c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6604",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae660c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b463b8"
      ]
    ],
    [
      "unmatched:00ae6614",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46388",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46390",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b463b8"
      ]
    ],
    [
      "00b46398",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae660c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md#insn-00ae660c) · [`00ae6628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md#insn-00ae6628) · [`00ae6630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md#insn-00ae6630)
- 新版 [`00b463ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46374.md#insn-00b463ac)

~~~diff
- 00ae660c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae660c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae660c bytes 410100b5
- 00ae6628 ["INT_ADD", "register:40f0:8", ["const:ae6628:8", "const:4:8"]]
- 00ae6628 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b463ac ["INT_ADD", "register:40f0:8", ["const:b463ac:8", "const:4:8"]]
+ 00b463ac ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6628 bytes 9ade0394
+ 00b463ac bytes d9510494
- 00ae6630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
- 00ae6630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6630 bytes 803602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79aa48f7059fc8ab8f1631a2362bde3d"></a>

### [`00ae669c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md) → [`00b46420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00ae66dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46460"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae66b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae66b0",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae66b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46464"
      ]
    ],
    [
      "unmatched:00ae66c0",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46434",
      "READ",
      [
        "storage",
        "01125328",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4643c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46464"
      ]
    ],
    [
      "00b46444",
      "PARAM",
      [
        "storage",
        "002bd0e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae66b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md#insn-00ae66b8) · [`00ae66d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md#insn-00ae66d4) · [`00ae66dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md#insn-00ae66dc)
- 新版 [`00b46458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46420.md#insn-00b46458)

~~~diff
- 00ae66b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae66b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae66b8 bytes 410100b5
- 00ae66d4 ["INT_ADD", "register:40f0:8", ["const:ae66d4:8", "const:4:8"]]
- 00ae66d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46458 ["INT_ADD", "register:40f0:8", ["const:b46458:8", "const:4:8"]]
+ 00b46458 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae66d4 bytes 6fde0394
+ 00b46458 bytes ae510494
- 00ae66dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
- 00ae66dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae66dc bytes 803602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6078a0aab86bf62f6e6416e8cba8d55a"></a>

### [`00ae670c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md) → [`00b46490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

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
      "definition_site": "00b464ac",
      "incomplete_value": false,
      "site": "00b464b0",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6728",
      "incomplete_value": false,
      "site": "00ae672c",
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
      "definition_site": "00b464bc",
      "incomplete_value": true,
      "site": "00b464c8",
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
    "old": null,
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
      "00b464ac",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6738",
      "DATA",
      [
        "storage",
        "010a0488",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b464ac",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b464bc",
      "DATA",
      [
        "storage",
        "01125348",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae672c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md#insn-00ae672c) · [`00ae6724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md#insn-00ae6724) · [`00ae6728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md#insn-00ae6728)
- 新版 [`00b464b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md#insn-00b464b0) · [`00b464a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md#insn-00b464a8) · [`00b464ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46490.md#insn-00b464ac)

~~~diff
- 00ae672c ["INT_ADD", "register:40f0:8", ["const:ae672c:8", "const:4:8"]]
- 00ae672c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b464b0 ["INT_ADD", "register:40f0:8", ["const:b464b0:8", "const:4:8"]]
+ 00b464b0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae672c bytes 95de0394
+ 00b464b0 bytes d4510494
- 00ae6724 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b464a8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae6724 bytes 80bdfff0
+ 00b464a8 bytes 00bbfff0
- 00ae6728 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae6728 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6728 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6728 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b464ac ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b464ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b464ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b464ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6728 bytes 00c81791
+ 00b464ac bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b0ef1b01ffe3a32f09efaef82f97c09"></a>

### [`00ae6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md) → [`00b4650c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 25.00% / 新版 20.00%

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
      "site": "00ae67b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46538"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46520",
      "incomplete_value": true,
      "site": "00b46520",
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
      "definition_site": "00ae679c",
      "incomplete_value": true,
      "site": "00ae679c",
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
      "00b4651c",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae67a4",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae67ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b4651c",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46528",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "00b46530",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae679c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md#insn-00ae679c) · [`00ae67ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md#insn-00ae67ac) · [`00ae67b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md#insn-00ae67b4)
- 新版 [`00b46520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4650c.md#insn-00b46520)

~~~diff
- 00ae679c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae679c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b46520 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46520 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae679c bytes e80000b5
+ 00b46520 bytes e80000b5
- 00ae67ac ["INT_ADD", "register:40f0:8", ["const:ae67ac:8", "const:4:8"]]
- 00ae67ac ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae67ac bytes 39de0394
- 00ae67b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
- 00ae67b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae67b4 bytes 604a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652416712c5cce8ceaca67d58aed5941"></a>

### [`00ae67c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md) → [`00b4654c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae67f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4657c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46560",
      "incomplete_value": true,
      "site": "00b46560",
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
      "definition_site": "00ae67dc",
      "incomplete_value": true,
      "site": "00ae67dc",
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
      "00b4655c",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae67e8",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae67f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b4655c",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4656c",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "00b46574",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae67dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md#insn-00ae67dc) · [`00ae67f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md#insn-00ae67f0) · [`00ae67f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md#insn-00ae67f8)
- 新版 [`00b46560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4654c.md#insn-00b46560)

~~~diff
- 00ae67dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae67dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b46560 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b46560 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae67dc bytes 080100b5
+ 00b46560 bytes 080100b5
- 00ae67f0 ["INT_ADD", "register:40f0:8", ["const:ae67f0:8", "const:4:8"]]
- 00ae67f0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae67f0 bytes 28de0394
- 00ae67f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
- 00ae67f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae67f8 bytes 604a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13ea5bb0dc4ce813ce4cbfb9a0936cff"></a>

### [`00ae680c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md) → [`00b46590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00ae683c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b465c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b465a4",
      "incomplete_value": true,
      "site": "00b465a4",
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
      "definition_site": "00ae6820",
      "incomplete_value": true,
      "site": "00ae6820",
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
      "00b465a0",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6828",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae683c",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b465a0",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b465ac",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ],
    [
      "00b465c0",
      "WRITE",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md#insn-00ae6820) · [`00ae6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md#insn-00ae6834) · [`00ae683c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md#insn-00ae683c)
- 新版 [`00b465a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md#insn-00b465a4) · [`00b465b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46590.md#insn-00b465b8)

~~~diff
- 00ae6820 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6820 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b465a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b465a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6820 bytes 080100b5
+ 00b465a4 bytes 080100b5
- 00ae6834 ["INT_ADD", "register:40f0:8", ["const:ae6834:8", "const:4:8"]]
- 00ae6834 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b465b8 ["INT_ADD", "register:40f0:8", ["const:b465b8:8", "const:4:8"]]
+ 00b465b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6834 bytes 17de0394
+ 00b465b8 bytes 56510494
- 00ae683c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
- 00ae683c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae683c bytes 604a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35ce844e3b939b3e1ffe59e68cd357ad"></a>

### [`00ae685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md) → [`00b465e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b465e0.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae685c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6860"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6860"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae685c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6860",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6864",
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
      "00b465e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b465e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b465e8",
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

- 旧版 [`00ae685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md#insn-00ae685c) · [`00ae6860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md#insn-00ae6860) · [`00ae6864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md#insn-00ae6864)

~~~diff
- 00ae685c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae685c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae685c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae685c bytes f50f1df8
- 00ae6860 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae6860 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae6860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6860 bytes f44f01a9
- 00ae6864 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6864 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6864 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae6864 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6864 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ed4858aadf72b5598d8e23ed1444d8"></a>

### [`00ae68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md) → [`00b4667c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md) _ZN8firebase4util18file_output_stream12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 36.36% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b466b8",
      "incomplete_value": true,
      "site": "00b466b8",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6934",
      "incomplete_value": true,
      "site": "00ae6934",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6984"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46708"
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
      "00b46690",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46694",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6988"
      ]
    ],
    [
      "00b4669c",
      "READ",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46690",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46694",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4670c"
      ]
    ],
    [
      "00b4669c",
      "READ",
      [
        "storage",
        "01125358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md#insn-00ae6934) · [`00ae695c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md#insn-00ae695c) · [`00ae6980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md#insn-00ae6980)
- 新版 [`00b466b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4667c.md#insn-00b466b8)

~~~diff
- 00ae6934 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6934 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6934 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:498:8"]]
- 00ae6934 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b466b8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b466b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b466b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
+ 00b466b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6934 bytes bf621239
+ 00b466b8 bytes bf620d39
- 00ae695c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae695c ["INT_ADD", "register:40f0:8", ["const:ae695c:8", "const:4:8"]]
- 00ae695c ["CALLIND", null, ["register:0:8"]]
- 00ae695c bytes 00013fd6
- 00ae6980 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6980 ["INT_ADD", "register:40f0:8", ["const:ae6980:8", "const:4:8"]]
- 00ae6980 ["CALLIND", null, ["register:0:8"]]
- 00ae6980 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66fa5914624ef704f2fdc75184c23236"></a>

### [`00ae6998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md) → [`00b4671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b4671c.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae699c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6998",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae699c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae69ac",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4671c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46720",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46730",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md#insn-00ae6998) · [`00ae699c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md#insn-00ae699c) · [`00ae69b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md#insn-00ae69b4)

~~~diff
- 00ae6998 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae6998 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae6998 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6998 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6998 bytes f44fbea9
- 00ae699c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae699c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae699c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae699c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae699c bytes fd7b01a9
- 00ae69b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae69b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae69b4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d645f56e939c91153665e69a1a5b69bf"></a>

### [`00ae6a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md) → [`00b467c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00ae6a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46808"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6a60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6a58",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6a60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4680c"
      ]
    ],
    [
      "unmatched:00ae6a68",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b467dc",
      "READ",
      [
        "storage",
        "01125350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b467e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4680c"
      ]
    ],
    [
      "00b467ec",
      "PARAM",
      [
        "storage",
        "002b04f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md#insn-00ae6a60) · [`00ae6a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md#insn-00ae6a7c) · [`00ae6a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md#insn-00ae6a84)
- 新版 [`00b46800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b467c8.md#insn-00b46800)

~~~diff
- 00ae6a60 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6a60 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae6a60 bytes 410100b5
- 00ae6a7c ["INT_ADD", "register:40f0:8", ["const:ae6a7c:8", "const:4:8"]]
- 00ae6a7c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46800 ["INT_ADD", "register:40f0:8", ["const:b46800:8", "const:4:8"]]
+ 00b46800 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6a7c bytes 85dd0394
+ 00b46800 bytes c4500494
- 00ae6a84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
- 00ae6a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6a84 bytes 804a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfad9a057324f06a20acc4f98bf5c8ff"></a>

### [`00ae6b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md) → [`00b468b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00ae6b5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b468e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b468c8",
      "incomplete_value": true,
      "site": "00b468c8",
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
      "definition_site": "00ae6b44",
      "incomplete_value": true,
      "site": "00ae6b44",
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
      "00b468c4",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6b4c",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6b54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b468c4",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b468d0",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ],
    [
      "00b468d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md#insn-00ae6b44) · [`00ae6b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md#insn-00ae6b54) · [`00ae6b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md#insn-00ae6b5c)
- 新版 [`00b468c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468b4.md#insn-00b468c8)

~~~diff
- 00ae6b44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6b44 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b468c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b468c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6b44 bytes e80000b5
+ 00b468c8 bytes e80000b5
- 00ae6b54 ["INT_ADD", "register:40f0:8", ["const:ae6b54:8", "const:4:8"]]
- 00ae6b54 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6b54 bytes 4fdd0394
- 00ae6b5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00ae6b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6b5c bytes 606202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f15de5b4df057f69b8391eb265d3d353"></a>

### [`00ae6b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md) → [`00b468f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b468f4.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6ba0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46924"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6b84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b46904",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46928"
      ]
    ],
    [
      "unmatched:00ae6b90",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46904",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46928"
      ]
    ],
    [
      "00b46914",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md#insn-00ae6b84) · [`00ae6b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md#insn-00ae6b98) · [`00ae6ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md#insn-00ae6ba0)

~~~diff
- 00ae6b84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6b84 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6b84 bytes 080100b5
- 00ae6b98 ["INT_ADD", "register:40f0:8", ["const:ae6b98:8", "const:4:8"]]
- 00ae6b98 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6b98 bytes 3edd0394
- 00ae6ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00ae6ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6ba0 bytes 606202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e5cba551378e39dc5b3f6385df9bfa0"></a>

### [`00ae6bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md) → [`00b46938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6bb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6bb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46948",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46938",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4693c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46948",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md#insn-00ae6bb4) · [`00ae6bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md#insn-00ae6bb8) · [`00ae6bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md#insn-00ae6bc8)
- 新版 [`00b4694c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46938.md#insn-00b4694c)

~~~diff
- 00ae6bb4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae6bb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6bb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6bb4 bytes f30f1ef8
- 00ae6bb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6bb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6bb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6bb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6bb8 bytes fd7b01a9
- 00ae6bc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6bc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4694c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4694c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6bc8 bytes 080100b5
+ 00b4694c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c6a54a90c7a716825bb872388b09981"></a>

### [`00ae6ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md) → [`00b46a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b46a60",
      "incomplete_value": true,
      "site": "00b46a60",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6cdc",
      "incomplete_value": true,
      "site": "00ae6cdc",
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
            "const:4c8:8"
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
      "definition_site": "00b46ab0",
      "incomplete_value": true,
      "site": "00b46ab0",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6d2c",
      "incomplete_value": true,
      "site": "00ae6d2c",
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
            "const:4c0:8"
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
      "definition_site": "00b46a3c",
      "incomplete_value": true,
      "site": "00b46a3c",
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
      "definition_site": "00ae6cb8",
      "incomplete_value": true,
      "site": "00ae6cb8",
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
      "00b46a38",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46a44",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46a60",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46a38",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46a44",
      "READ",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46a60",
      "WRITE",
      [
        "storage",
        "01125388",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md#insn-00ae6cdc) · [`00ae6d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md#insn-00ae6d28) · [`00ae6d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md#insn-00ae6d2c)
- 新版 [`00b46a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md#insn-00b46a60) · [`00b46aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md#insn-00b46aac) · [`00b46ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46a24.md#insn-00b46ab0)

~~~diff
- 00ae6cdc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6cdc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6cdc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4c8:8"]]
- 00ae6cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46a60 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46a60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46a60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:388:8"]]
+ 00b46a60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6cdc bytes bf221339
+ 00b46a60 bytes bf220e39
- 00ae6d28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6d28 ["INT_ADD", "register:40f0:8", ["const:ae6d28:8", "const:4:8"]]
- 00ae6d28 ["CALLIND", null, ["register:0:8"]]
+ 00b46aac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46aac ["INT_ADD", "register:40f0:8", ["const:b46aac:8", "const:4:8"]]
+ 00b46aac ["CALLIND", null, ["register:0:8"]]
- 00ae6d28 bytes 00013fd6
+ 00b46aac bytes 00013fd6
- 00ae6d2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00ae6d2c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae6d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b46ab0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
+ 00b46ab0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b46ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae6d2c bytes 9f6202f9
+ 00b46ab0 bytes 9fc201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9edf3ae18dd7d6916e02f38b811dee"></a>

### [`00ae6d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md) → [`00b46ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae6d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46b04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6d5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6d54",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6d5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46b08"
      ]
    ],
    [
      "unmatched:00ae6d64",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46ad8",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46ae0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46b08"
      ]
    ],
    [
      "00b46ae8",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md#insn-00ae6d5c) · [`00ae6d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md#insn-00ae6d78) · [`00ae6d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md#insn-00ae6d80)
- 新版 [`00b46afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ac4.md#insn-00b46afc)

~~~diff
- 00ae6d5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6d5c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6d5c bytes 410100b5
- 00ae6d78 ["INT_ADD", "register:40f0:8", ["const:ae6d78:8", "const:4:8"]]
- 00ae6d78 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46afc ["INT_ADD", "register:40f0:8", ["const:b46afc:8", "const:4:8"]]
+ 00b46afc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6d78 bytes c6dc0394
+ 00b46afc bytes 05500494
- 00ae6d80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00ae6d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6d80 bytes 806202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ded2a75c368468548d4a4990463763f"></a>

### [`00ae6dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md) → [`00b46b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46bb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6e08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6e00",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6e08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46bb4"
      ]
    ],
    [
      "unmatched:00ae6e10",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b46b84",
      "READ",
      [
        "storage",
        "01125380",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46b8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46bb4"
      ]
    ],
    [
      "00b46b94",
      "PARAM",
      [
        "storage",
        "002b8a16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md#insn-00ae6e08) · [`00ae6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md#insn-00ae6e24) · [`00ae6e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md#insn-00ae6e2c)
- 新版 [`00b46ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46b70.md#insn-00b46ba8)

~~~diff
- 00ae6e08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6e08 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6e08 bytes 410100b5
- 00ae6e24 ["INT_ADD", "register:40f0:8", ["const:ae6e24:8", "const:4:8"]]
- 00ae6e24 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46ba8 ["INT_ADD", "register:40f0:8", ["const:b46ba8:8", "const:4:8"]]
+ 00b46ba8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6e24 bytes 9bdc0394
+ 00b46ba8 bytes da4f0494
- 00ae6e2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00ae6e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6e2c bytes 806202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10173fad9f911ee42aea3a3136424272"></a>

### [`00ae6e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md) → [`00b46be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md) _ZN8firebase4util16dex_class_loader10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b46bfc",
      "incomplete_value": false,
      "site": "00b46c00",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e78",
      "incomplete_value": false,
      "site": "00ae6e7c",
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
      "definition_site": "00b46c0c",
      "incomplete_value": true,
      "site": "00b46c18",
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
      "definition_site": "00ae6e88",
      "incomplete_value": true,
      "site": "00ae6e94",
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
      "00b46bfc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b46c0c",
      "DATA",
      [
        "storage",
        "010a04e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46bfc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b46c0c",
      "DATA",
      [
        "storage",
        "011253a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md#insn-00ae6e7c) · [`00ae6e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md#insn-00ae6e74) · [`00ae6e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md#insn-00ae6e78)
- 新版 [`00b46c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md#insn-00b46c00) · [`00b46bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md#insn-00b46bf8) · [`00b46bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46be0.md#insn-00b46bfc)

~~~diff
- 00ae6e7c ["INT_ADD", "register:40f0:8", ["const:ae6e7c:8", "const:4:8"]]
- 00ae6e7c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b46c00 ["INT_ADD", "register:40f0:8", ["const:b46c00:8", "const:4:8"]]
+ 00b46c00 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae6e7c bytes c1dc0394
+ 00b46c00 bytes 00500494
- 00ae6e74 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b46bf8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae6e74 bytes 80bdfff0
+ 00b46bf8 bytes 00bbfff0
- 00ae6e78 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae6e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46bfc ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b46bfc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46bfc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46bfc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6e78 bytes 00c81791
+ 00b46bfc bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b34ffa020d2319234d6cfd3e749e2171"></a>

### [`00ae6e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md) → [`00b46c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b46c48",
      "incomplete_value": true,
      "site": "00b46c48",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ec4",
      "incomplete_value": true,
      "site": "00ae6ec4",
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
            "const:4e8:8"
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
      "definition_site": "00b46c30",
      "incomplete_value": true,
      "site": "00b46c30",
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
      "definition_site": "00ae6eac",
      "incomplete_value": true,
      "site": "00ae6eac",
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
      "definition_site": "00b46c3c",
      "incomplete_value": false,
      "site": "00b46c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6eb8",
      "incomplete_value": false,
      "site": "00ae6ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:edc:8"
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
      "00b46c2c",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c3c",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00b46c48",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46c2c",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c3c",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "00b46c48",
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md#insn-00ae6ebc) · [`00ae6ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md#insn-00ae6ec4) · [`00ae6ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md#insn-00ae6ea4)
- 新版 [`00b46c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md#insn-00b46c40) · [`00b46c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md#insn-00b46c48) · [`00b46c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c1c.md#insn-00b46c28)

~~~diff
- 00ae6ebc ["INT_ADD", "register:40f0:8", ["const:ae6ebc:8", "const:4:8"]]
- 00ae6ebc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46c40 ["INT_ADD", "register:40f0:8", ["const:b46c40:8", "const:4:8"]]
+ 00b46c40 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6ebc bytes 75dc0394
+ 00b46c40 bytes b44f0494
- 00ae6ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae6ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46c48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00b46c48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6ec4 bytes 607602f9
+ 00b46c48 bytes 60d601f9
- 00ae6ea4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b46c28 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae6ea4 bytes d32d00d0
+ 00b46c28 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e89f1a2c6689b4cef1a40c43b059824d"></a>

### [`00ae6ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md) → [`00b46c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b46c88",
      "incomplete_value": true,
      "site": "00b46c88",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f04",
      "incomplete_value": true,
      "site": "00ae6f04",
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
            "const:4e8:8"
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
      "definition_site": "00b46c70",
      "incomplete_value": true,
      "site": "00b46c70",
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
      "definition_site": "00ae6eec",
      "incomplete_value": true,
      "site": "00ae6eec",
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
      "definition_site": "00b46c78",
      "incomplete_value": false,
      "site": "00b46c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ef4",
      "incomplete_value": false,
      "site": "00ae6efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:edc:8"
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
      "00b46c6c",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c78",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00b46c88",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46c6c",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46c78",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "00b46c88",
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md#insn-00ae6efc) · [`00ae6f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md#insn-00ae6f04) · [`00ae6ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md#insn-00ae6ee4)
- 新版 [`00b46c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md#insn-00b46c80) · [`00b46c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md#insn-00b46c88) · [`00b46c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c5c.md#insn-00b46c68)

~~~diff
- 00ae6efc ["INT_ADD", "register:40f0:8", ["const:ae6efc:8", "const:4:8"]]
- 00ae6efc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46c80 ["INT_ADD", "register:40f0:8", ["const:b46c80:8", "const:4:8"]]
+ 00b46c80 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6efc bytes 65dc0394
+ 00b46c80 bytes a44f0494
- 00ae6f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae6f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00b46c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6f04 bytes 607602f9
+ 00b46c88 bytes 60d601f9
- 00ae6ee4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b46c68 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae6ee4 bytes d32d00d0
+ 00b46c68 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a151d60ad23f76e624f1d3f46c4af305"></a>

### [`00ae6f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md) → [`00b46c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46c9c.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

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
      "site": "00ae6f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46ccc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b46cb0",
      "incomplete_value": true,
      "site": "00b46cb0",
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
      "definition_site": "00ae6f2c",
      "incomplete_value": true,
      "site": "00ae6f2c",
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
      "00b46cac",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6f4c"
      ]
    ],
    [
      "unmatched:00ae6f38",
      "PARAM",
      [
        "storage",
        "002a4edc",
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
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46cd0"
      ]
    ],
    [
      "00b46cbc",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md#insn-00ae6f40) · [`00ae6f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md#insn-00ae6f48) · [`00ae6f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md#insn-00ae6f58)

~~~diff
- 00ae6f40 ["INT_ADD", "register:40f0:8", ["const:ae6f40:8", "const:4:8"]]
- 00ae6f40 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6f40 bytes 54dc0394
- 00ae6f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae6f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6f48 bytes 607602f9
- 00ae6f58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6f58 ["RETURN", null, ["register:0:8"]]
- 00ae6f58 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31dd490b387982bebf5008641c13077c"></a>

### [`00ae6f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md) → [`00b46ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b46d10",
      "incomplete_value": true,
      "site": "00b46d10",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f8c",
      "incomplete_value": true,
      "site": "00ae6f8c",
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
            "const:4e8:8"
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
      "definition_site": "00b46cf4",
      "incomplete_value": true,
      "site": "00b46cf4",
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
      "definition_site": "00ae6f70",
      "incomplete_value": true,
      "site": "00ae6f70",
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
      "definition_site": "00b46cfc",
      "incomplete_value": false,
      "site": "00b46d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f78",
      "incomplete_value": false,
      "site": "00ae6f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a4000:8"
          ],
          [
            "leaf",
            "const:edc:8"
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
      "00b46cf0",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cfc",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00b46d10",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46cf0",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46cfc",
      "PARAM",
      [
        "storage",
        "002b587d",
        null,
        "string"
      ]
    ],
    [
      "00b46d10",
      "WRITE",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md#insn-00ae6f84) · [`00ae6f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md#insn-00ae6f8c) · [`00ae6f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md#insn-00ae6f68)
- 新版 [`00b46d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md#insn-00b46d08) · [`00b46d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md#insn-00b46d10) · [`00b46cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46ce0.md#insn-00b46cec)

~~~diff
- 00ae6f84 ["INT_ADD", "register:40f0:8", ["const:ae6f84:8", "const:4:8"]]
- 00ae6f84 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46d08 ["INT_ADD", "register:40f0:8", ["const:b46d08:8", "const:4:8"]]
+ 00b46d08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae6f84 bytes 43dc0394
+ 00b46d08 bytes 824f0494
- 00ae6f8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae6f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
+ 00b46d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6f8c bytes 607602f9
+ 00b46d10 bytes 60d601f9
- 00ae6f68 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b46cec ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae6f68 bytes d32d00d0
+ 00b46cec bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfd8b0f0ca3cd870f5919588504ab357"></a>

### [`00ae6fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md) → [`00b46d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7034"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46db8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46d64",
      "incomplete_value": true,
      "site": "00b46d70",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6fe0",
      "incomplete_value": true,
      "site": "00ae6fec",
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
                "const:4e8:8"
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
      "00b46d44",
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46d50",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7038"
      ]
    ],
    [
      "00b46d64",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46d44",
      "READ",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46d50",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b46dbc"
      ]
    ],
    [
      "00b46d64",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md#insn-00ae6fec) · [`00ae7028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md#insn-00ae7028) · [`00ae7034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md#insn-00ae7034)
- 新版 [`00b46d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46d30.md#insn-00b46d70)

~~~diff
- 00ae6fec ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6fec ["INT_ADD", "register:40f0:8", ["const:ae6fec:8", "const:4:8"]]
- 00ae6fec ["CALLIND", null, ["register:0:8"]]
+ 00b46d70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b46d70 ["INT_ADD", "register:40f0:8", ["const:b46d70:8", "const:4:8"]]
+ 00b46d70 ["CALLIND", null, ["register:0:8"]]
- 00ae6fec bytes 00013fd6
+ 00b46d70 bytes 00013fd6
- 00ae7028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7028 ["INT_ADD", "register:40f0:8", ["const:ae7028:8", "const:4:8"]]
- 00ae7028 ["CALLIND", null, ["register:0:8"]]
- 00ae7028 bytes 00013fd6
- 00ae7034 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7034 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4f0:8"]]
- 00ae7034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7034 bytes a0c21339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa30523daa4cf204621830a29bab6265"></a>

### [`00ae7048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md) → [`00b46dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 60.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46e08",
      "incomplete_value": true,
      "site": "00b46e08",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7084",
      "incomplete_value": true,
      "site": "00ae7084",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae70d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b46e58"
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
      "00b46de0",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46dec",
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46e08",
      "WRITE",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b46de0",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46dec",
      "READ",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b46e08",
      "WRITE",
      [
        "storage",
        "011253b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md#insn-00ae7060) · [`00ae7084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md#insn-00ae7084) · [`00ae70d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md#insn-00ae70d0)
- 新版 [`00b46de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md#insn-00b46de4) · [`00b46e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46dcc.md#insn-00b46e08)

~~~diff
- 00ae7060 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7060 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b46de4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b46de4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae7060 bytes c10300b4
+ 00b46de4 bytes c10300b4
- 00ae7084 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7084 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7084 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4f0:8"]]
- 00ae7084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b46e08 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b46e08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b46e08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3b0:8"]]
+ 00b46e08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7084 bytes bfc21339
+ 00b46e08 bytes bfc20e39
- 00ae70d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae70d0 ["INT_ADD", "register:40f0:8", ["const:ae70d0:8", "const:4:8"]]
- 00ae70d0 ["CALLIND", null, ["register:0:8"]]
- 00ae70d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66e1be626fedd789e43033c7df1d94cd"></a>

### [`00ae70e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md) → [`00b46e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46e6c.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae70e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae70e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae70ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae70e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae70ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae70fc",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46e70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46e80",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae70e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md#insn-00ae70e8) · [`00ae70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md#insn-00ae70ec) · [`00ae7104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md#insn-00ae7104)

~~~diff
- 00ae70e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae70e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae70e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae70e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae70e8 bytes f44fbea9
- 00ae70ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae70ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae70ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae70ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae70ec bytes fd7b01a9
- 00ae7104 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7104 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae7104 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9e0e23cdb8b7947367356ac2994fa1"></a>

### [`00ae7158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md) → [`00b46edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b46ef8",
      "incomplete_value": false,
      "site": "00b46efc",
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
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7174",
      "incomplete_value": false,
      "site": "00ae7178",
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
      "definition_site": "00b46f08",
      "incomplete_value": true,
      "site": "00b46f14",
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
      "definition_site": "00ae7184",
      "incomplete_value": true,
      "site": "00ae7190",
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
      "00b46ef8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b46f08",
      "DATA",
      [
        "storage",
        "010a04f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46ef8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b46f08",
      "DATA",
      [
        "storage",
        "011253b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md#insn-00ae7178) · [`00ae7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md#insn-00ae7170) · [`00ae7174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md#insn-00ae7174)
- 新版 [`00b46efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md#insn-00b46efc) · [`00b46ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md#insn-00b46ef4) · [`00b46ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46edc.md#insn-00b46ef8)

~~~diff
- 00ae7178 ["INT_ADD", "register:40f0:8", ["const:ae7178:8", "const:4:8"]]
- 00ae7178 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b46efc ["INT_ADD", "register:40f0:8", ["const:b46efc:8", "const:4:8"]]
+ 00b46efc ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae7178 bytes 02dc0394
+ 00b46efc bytes 414f0494
- 00ae7170 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b46ef4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae7170 bytes 80bdffb0
+ 00b46ef4 bytes 00bbffd0
- 00ae7174 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae7174 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7174 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7174 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46ef8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b46ef8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46ef8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46ef8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7174 bytes 001c1591
+ 00b46ef8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33a5bbe326aeb196c4ef844647fd48b"></a>

### [`00ae7194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md) → [`00b46f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f18.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7198"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7194",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7198",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae71a8",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46f18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b46f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b46f2c",
      "READ",
      [
        "storage",
        "011253a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md#insn-00ae7194) · [`00ae7198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md#insn-00ae7198) · [`00ae71b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md#insn-00ae71b0)

~~~diff
- 00ae7194 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae7194 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae7194 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae7194 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7194 bytes f44fbea9
- 00ae7198 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7198 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae7198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7198 bytes fd7b01a9
- 00ae71b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae71b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae71b0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970f7b28d9c81a903cbeec2ad1f7bbf6"></a>

### [`00ae7204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md) → [`00b46f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b46fa4",
      "incomplete_value": false,
      "site": "00b46fa8",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7220",
      "incomplete_value": false,
      "site": "00ae7224",
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
      "definition_site": "00b46fb4",
      "incomplete_value": true,
      "site": "00b46fc0",
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
      "definition_site": "00ae7230",
      "incomplete_value": true,
      "site": "00ae723c",
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
      "00b46fa4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b46fb4",
      "DATA",
      [
        "storage",
        "010a0500",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46fa4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b46fb4",
      "DATA",
      [
        "storage",
        "011253c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md#insn-00ae7224) · [`00ae721c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md#insn-00ae721c) · [`00ae7220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md#insn-00ae7220)
- 新版 [`00b46fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md#insn-00b46fa8) · [`00b46fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md#insn-00b46fa0) · [`00b46fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46f88.md#insn-00b46fa4)

~~~diff
- 00ae7224 ["INT_ADD", "register:40f0:8", ["const:ae7224:8", "const:4:8"]]
- 00ae7224 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b46fa8 ["INT_ADD", "register:40f0:8", ["const:b46fa8:8", "const:4:8"]]
+ 00b46fa8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae7224 bytes d7db0394
+ 00b46fa8 bytes 164f0494
- 00ae721c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b46fa0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae721c bytes 80bdffd0
+ 00b46fa0 bytes 00bbfff0
- 00ae7220 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b46fa4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b46fa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46fa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b46fa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7220 bytes 00c81791
+ 00b46fa4 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df384d6f56fe7b0f596ad04c3b3d35de"></a>

### [`00ae7240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md) → [`00b46fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b46ff0",
      "incomplete_value": true,
      "site": "00b46ff0",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae726c",
      "incomplete_value": true,
      "site": "00ae726c",
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
            "const:508:8"
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
      "definition_site": "00b46fd8",
      "incomplete_value": true,
      "site": "00b46fd8",
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
      "definition_site": "00ae7254",
      "incomplete_value": true,
      "site": "00ae7254",
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
      "definition_site": "00b46fe4",
      "incomplete_value": false,
      "site": "00b46fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7260",
      "incomplete_value": false,
      "site": "00ae7264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:339:8"
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
      "00b46fd4",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46fe4",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      "00b46ff0",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b46fd4",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b46fe4",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b46ff0",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md#insn-00ae7264) · [`00ae726c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md#insn-00ae726c) · [`00ae724c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md#insn-00ae724c)
- 新版 [`00b46fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md#insn-00b46fe8) · [`00b46ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md#insn-00b46ff0) · [`00b46fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b46/00b46fc4.md#insn-00b46fd0)

~~~diff
- 00ae7264 ["INT_ADD", "register:40f0:8", ["const:ae7264:8", "const:4:8"]]
- 00ae7264 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b46fe8 ["INT_ADD", "register:40f0:8", ["const:b46fe8:8", "const:4:8"]]
+ 00b46fe8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7264 bytes 8bdb0394
+ 00b46fe8 bytes ca4e0494
- 00ae726c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae726c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b46ff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
+ 00b46ff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae726c bytes 608602f9
+ 00b46ff0 bytes 60e601f9
- 00ae724c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b46fd0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae724c bytes d32d00b0
+ 00b46fd0 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d4976d413c4d7c6824e478b273b11aa"></a>

### [`00ae72c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md) → [`00b47044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b47074",
      "incomplete_value": true,
      "site": "00b47074",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72f0",
      "incomplete_value": true,
      "site": "00ae72f0",
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
            "const:508:8"
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
      "definition_site": "00b47058",
      "incomplete_value": true,
      "site": "00b47058",
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
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72d4",
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
      "definition_site": "00b47064",
      "incomplete_value": false,
      "site": "00b4706c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72e0",
      "incomplete_value": false,
      "site": "00ae72e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:339:8"
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
      "00b47054",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47064",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      "00b47074",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47054",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47064",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b47074",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae72e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md#insn-00ae72e8) · [`00ae72f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md#insn-00ae72f0) · [`00ae72cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md#insn-00ae72cc)
- 新版 [`00b4706c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md#insn-00b4706c) · [`00b47074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md#insn-00b47074) · [`00b47050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47044.md#insn-00b47050)

~~~diff
- 00ae72e8 ["INT_ADD", "register:40f0:8", ["const:ae72e8:8", "const:4:8"]]
- 00ae72e8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4706c ["INT_ADD", "register:40f0:8", ["const:b4706c:8", "const:4:8"]]
+ 00b4706c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae72e8 bytes 6adb0394
+ 00b4706c bytes a94e0494
- 00ae72f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae72f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
+ 00b47074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae72f0 bytes 608602f9
+ 00b47074 bytes 60e601f9
- 00ae72cc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b47050 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae72cc bytes d32d00b0
+ 00b47050 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c99f400c59aaf488034f44c3d2424f2e"></a>

### [`00ae7304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md) → [`00b47088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b470b8",
      "incomplete_value": true,
      "site": "00b470b8",
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
            "const:3c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7334",
      "incomplete_value": true,
      "site": "00ae7334",
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
            "const:508:8"
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
      "definition_site": "00b4709c",
      "incomplete_value": true,
      "site": "00b4709c",
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
      "definition_site": "00ae7318",
      "incomplete_value": true,
      "site": "00ae7318",
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
      "definition_site": "00b470a4",
      "incomplete_value": false,
      "site": "00b470b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:591:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7320",
      "incomplete_value": false,
      "site": "00ae732c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:339:8"
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
      "00b47098",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b470a4",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      "00b470b8",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47098",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b470a4",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ],
    [
      "00b470b8",
      "WRITE",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae732c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md#insn-00ae732c) · [`00ae7334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md#insn-00ae7334) · [`00ae7310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md#insn-00ae7310)
- 新版 [`00b470b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md#insn-00b470b0) · [`00b470b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md#insn-00b470b8) · [`00b47094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47088.md#insn-00b47094)

~~~diff
- 00ae732c ["INT_ADD", "register:40f0:8", ["const:ae732c:8", "const:4:8"]]
- 00ae732c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b470b0 ["INT_ADD", "register:40f0:8", ["const:b470b0:8", "const:4:8"]]
+ 00b470b0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae732c bytes 59db0394
+ 00b470b0 bytes 984e0494
- 00ae7334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
- 00ae7334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b470b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c8:8"]]
+ 00b470b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7334 bytes 608602f9
+ 00b470b8 bytes 60e601f9
- 00ae7310 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b47094 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae7310 bytes d32d00b0
+ 00b47094 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4695e6b64d8e6b54d9290225875ccc0e"></a>

### [`00ae7354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md) → [`00b470d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47160",
      "incomplete_value": true,
      "site": "00b47160",
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
            "const:3d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae73dc",
      "incomplete_value": true,
      "site": "00ae73dc",
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
            "const:510:8"
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
      "definition_site": "00b4710c",
      "incomplete_value": true,
      "site": "00b47118",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:3c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7388",
      "incomplete_value": true,
      "site": "00ae7394",
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
                "const:508:8"
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
      "00b470ec",
      "READ",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4710c",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47160",
      "WRITE",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b470ec",
      "READ",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4710c",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47160",
      "WRITE",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md#insn-00ae7394) · [`00ae73dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md#insn-00ae73dc) · [`00ae7364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md#insn-00ae7364)
- 新版 [`00b47118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md#insn-00b47118) · [`00b47160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md#insn-00b47160) · [`00b470e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b470d8.md#insn-00b470e8)

~~~diff
- 00ae7394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7394 ["INT_ADD", "register:40f0:8", ["const:ae7394:8", "const:4:8"]]
- 00ae7394 ["CALLIND", null, ["register:0:8"]]
+ 00b47118 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47118 ["INT_ADD", "register:40f0:8", ["const:b47118:8", "const:4:8"]]
+ 00b47118 ["CALLIND", null, ["register:0:8"]]
- 00ae7394 bytes 00013fd6
+ 00b47118 bytes 00013fd6
- 00ae73dc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae73dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:510:8"]]
- 00ae73dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47160 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47160 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3d0:8"]]
+ 00b47160 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae73dc bytes a0421439
+ 00b47160 bytes a0420f39
- 00ae7364 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b470e8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00ae7364 bytes d52d00b0
+ 00b470e8 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bc5b33b76c891c3be36f1f1a5059535"></a>

### [`00ae73f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md) → [`00b47174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00ae742c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae747c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b471b0"
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
      "00b47188",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47194",
      "READ",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae742c",
      "WRITE",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47188",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47194",
      "READ",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b471b0",
      "WRITE",
      [
        "storage",
        "011253d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md#insn-00ae7408) · [`00ae742c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md#insn-00ae742c) · [`00ae7464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md#insn-00ae7464)
- 新版 [`00b4718c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47174.md#insn-00b4718c)

~~~diff
- 00ae7408 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7408 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b4718c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4718c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae7408 bytes c10300b4
+ 00b4718c bytes c10300b4
- 00ae742c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae742c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae742c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:510:8"]]
- 00ae742c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae742c bytes bf421439
- 00ae7464 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7464 ["INT_ADD", "register:40f0:8", ["const:ae7464:8", "const:4:8"]]
- 00ae7464 ["CALLIND", null, ["register:0:8"]]
- 00ae7464 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a87a2a87293ca598b3598c0d3da8c54"></a>

### [`00ae7490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md) → [`00b47214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae74d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47254"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae74ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae74a4",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae74ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47258"
      ]
    ],
    [
      "unmatched:00ae74b4",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47228",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47258"
      ]
    ],
    [
      "00b47238",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae74ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md#insn-00ae74ac) · [`00ae74c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md#insn-00ae74c8) · [`00ae74d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md#insn-00ae74d0)
- 新版 [`00b4724c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47214.md#insn-00b4724c)

~~~diff
- 00ae74ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae74ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae74ac bytes 410100b5
- 00ae74c8 ["INT_ADD", "register:40f0:8", ["const:ae74c8:8", "const:4:8"]]
- 00ae74c8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4724c ["INT_ADD", "register:40f0:8", ["const:b4724c:8", "const:4:8"]]
+ 00b4724c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae74c8 bytes f2da0394
+ 00b4724c bytes 314e0494
- 00ae74d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae74d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae74d0 bytes 808602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3fd9ef09a55d5de56afd009821d9d08"></a>

### [`00ae753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md) → [`00b472c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00ae757c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47300"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7558"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7550",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47304"
      ]
    ],
    [
      "unmatched:00ae7560",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b472d4",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b472dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47304"
      ]
    ],
    [
      "00b472e4",
      "PARAM",
      [
        "storage",
        "002be591",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md#insn-00ae7558) · [`00ae7574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md#insn-00ae7574) · [`00ae757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md#insn-00ae757c)
- 新版 [`00b472f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b472c0.md#insn-00b472f8)

~~~diff
- 00ae7558 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7558 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7558 bytes 410100b5
- 00ae7574 ["INT_ADD", "register:40f0:8", ["const:ae7574:8", "const:4:8"]]
- 00ae7574 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b472f8 ["INT_ADD", "register:40f0:8", ["const:b472f8:8", "const:4:8"]]
+ 00b472f8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7574 bytes c7da0394
+ 00b472f8 bytes 064e0494
- 00ae757c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
- 00ae757c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae757c bytes 808602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e651fe0786eb8d2ec75f9f917d5c16d"></a>

### [`00ae75ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md) → [`00b47330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4734c",
      "incomplete_value": false,
      "site": "00b47350",
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
            "const:451:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75c8",
      "incomplete_value": false,
      "site": "00ae75cc",
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
      "definition_site": "00b4735c",
      "incomplete_value": true,
      "site": "00b47368",
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
      "definition_site": "00ae75d8",
      "incomplete_value": true,
      "site": "00ae75e4",
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
      "00b4734c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4735c",
      "DATA",
      [
        "storage",
        "010a0568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4734c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4735c",
      "DATA",
      [
        "storage",
        "01125428",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae75cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md#insn-00ae75cc) · [`00ae75c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md#insn-00ae75c4) · [`00ae75c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md#insn-00ae75c8)
- 新版 [`00b47350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md#insn-00b47350) · [`00b47348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md#insn-00b47348) · [`00b4734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47330.md#insn-00b4734c)

~~~diff
- 00ae75cc ["INT_ADD", "register:40f0:8", ["const:ae75cc:8", "const:4:8"]]
- 00ae75cc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b47350 ["INT_ADD", "register:40f0:8", ["const:b47350:8", "const:4:8"]]
+ 00b47350 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae75cc bytes edda0394
+ 00b47350 bytes 2c4e0494
- 00ae75c4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b47348 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae75c4 bytes 80bdffd0
+ 00b47348 bytes 00bbffd0
- 00ae75c8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae75c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae75c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae75c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4734c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4734c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4734c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4734c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae75c8 bytes 00c81791
+ 00b4734c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a8481be4915631da892cc4c3b8bbd7"></a>

### [`00ae75e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md) → [`00b4736c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae7614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47398"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47380",
      "incomplete_value": true,
      "site": "00b47380",
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
      "definition_site": "00ae75fc",
      "incomplete_value": true,
      "site": "00ae75fc",
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
      "00b4737c",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7608",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae760c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b4737c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4738c",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47390",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae75fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md#insn-00ae75fc) · [`00ae760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md#insn-00ae760c) · [`00ae7614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md#insn-00ae7614)
- 新版 [`00b47380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4736c.md#insn-00b47380)

~~~diff
- 00ae75fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae75fc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47380 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47380 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae75fc bytes e80000b5
+ 00b47380 bytes e80000b5
- 00ae760c ["INT_ADD", "register:40f0:8", ["const:ae760c:8", "const:4:8"]]
- 00ae760c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae760c bytes a1da0394
- 00ae7614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae7614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7614 bytes 60ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2de70ff924c6025355fb0c75c7e36740"></a>

### [`00ae7668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md) → [`00b473ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00ae7698"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4741c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47400",
      "incomplete_value": true,
      "site": "00b47400",
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
      "definition_site": "00ae767c",
      "incomplete_value": true,
      "site": "00ae767c",
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
      "00b473fc",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7688",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7690",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b473fc",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4740c",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47414",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae767c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md#insn-00ae767c) · [`00ae7690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md#insn-00ae7690) · [`00ae7698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md#insn-00ae7698)
- 新版 [`00b47400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b473ec.md#insn-00b47400)

~~~diff
- 00ae767c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae767c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47400 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47400 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae767c bytes 080100b5
+ 00b47400 bytes 080100b5
- 00ae7690 ["INT_ADD", "register:40f0:8", ["const:ae7690:8", "const:4:8"]]
- 00ae7690 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7690 bytes 80da0394
- 00ae7698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae7698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7698 bytes 60ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b46c4fe1d10db2017c8f105e4fa8a7"></a>

### [`00ae76ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md) → [`00b47430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b47460",
      "incomplete_value": true,
      "site": "00b47460",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae76dc",
      "incomplete_value": true,
      "site": "00ae76dc",
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
            "const:570:8"
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
      "definition_site": "00b47444",
      "incomplete_value": true,
      "site": "00b47444",
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
      "definition_site": "00ae76c0",
      "incomplete_value": true,
      "site": "00ae76c0",
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
      "definition_site": "00b4744c",
      "incomplete_value": false,
      "site": "00b47458",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae76c8",
      "incomplete_value": false,
      "site": "00ae76d4",
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
            "const:497:8"
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
      "00b47440",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4744c",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00b47460",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47440",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4744c",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ],
    [
      "00b47460",
      "WRITE",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae76d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md#insn-00ae76d4) · [`00ae76dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md#insn-00ae76dc) · [`00ae76b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md#insn-00ae76b8)
- 新版 [`00b47458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md#insn-00b47458) · [`00b47460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md#insn-00b47460) · [`00b4743c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47430.md#insn-00b4743c)

~~~diff
- 00ae76d4 ["INT_ADD", "register:40f0:8", ["const:ae76d4:8", "const:4:8"]]
- 00ae76d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47458 ["INT_ADD", "register:40f0:8", ["const:b47458:8", "const:4:8"]]
+ 00b47458 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae76d4 bytes 6fda0394
+ 00b47458 bytes ae4d0494
- 00ae76dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00ae76dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:430:8"]]
+ 00b47460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae76dc bytes 60ba02f9
+ 00b47460 bytes 601a02f9
- 00ae76b8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4743c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae76b8 bytes d32d00b0
+ 00b4743c bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e334b2db22cfd983189a527af5df09d"></a>

### [`00ae76fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md) → [`00b47480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47508",
      "incomplete_value": true,
      "site": "00b47508",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7784",
      "incomplete_value": true,
      "site": "00ae7784",
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
            "const:578:8"
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
      "definition_site": "00b474b4",
      "incomplete_value": true,
      "site": "00b474c0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7730",
      "incomplete_value": true,
      "site": "00ae773c",
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
                "const:570:8"
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
      "00b47494",
      "READ",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ],
    [
      "00b474b4",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47508",
      "WRITE",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47494",
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      "00b474b4",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47508",
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md#insn-00ae773c) · [`00ae7784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md#insn-00ae7784) · [`00ae770c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md#insn-00ae770c)
- 新版 [`00b474c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md#insn-00b474c0) · [`00b47508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md#insn-00b47508) · [`00b47490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47480.md#insn-00b47490)

~~~diff
- 00ae773c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae773c ["INT_ADD", "register:40f0:8", ["const:ae773c:8", "const:4:8"]]
- 00ae773c ["CALLIND", null, ["register:0:8"]]
+ 00b474c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b474c0 ["INT_ADD", "register:40f0:8", ["const:b474c0:8", "const:4:8"]]
+ 00b474c0 ["CALLIND", null, ["register:0:8"]]
- 00ae773c bytes 00013fd6
+ 00b474c0 bytes 00013fd6
- 00ae7784 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7784 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:578:8"]]
- 00ae7784 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47508 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47508 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:438:8"]]
+ 00b47508 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7784 bytes a0e21539
+ 00b47508 bytes a0e21039
- 00ae770c ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b47490 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00ae770c bytes d52d00b0
+ 00b47490 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c9a0b49d0c49a1a609d67ebc6ecb730"></a>

### [`00ae7798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md) → [`00b4751c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47558",
      "incomplete_value": true,
      "site": "00b47558",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae77d4",
      "incomplete_value": true,
      "site": "00ae77d4",
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
            "const:578:8"
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
      "definition_site": "00b475a8",
      "incomplete_value": true,
      "site": "00b475a8",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7824",
      "incomplete_value": true,
      "site": "00ae7824",
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
            "const:570:8"
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
      "definition_site": "00b47534",
      "incomplete_value": true,
      "site": "00b47534",
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
      "definition_site": "00ae77b0",
      "incomplete_value": true,
      "site": "00ae77b0",
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
      "00b47530",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4753c",
      "READ",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47558",
      "WRITE",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47530",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4753c",
      "READ",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47558",
      "WRITE",
      [
        "storage",
        "01125438",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae77b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md#insn-00ae77b0) · [`00ae77d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md#insn-00ae77d4) · [`00ae77fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md#insn-00ae77fc)
- 新版 [`00b47534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md#insn-00b47534) · [`00b47558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4751c.md#insn-00b47558)

~~~diff
- 00ae77b0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae77b0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b47534 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b47534 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae77b0 bytes c10300b4
+ 00b47534 bytes c10300b4
- 00ae77d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae77d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae77d4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:578:8"]]
- 00ae77d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47558 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47558 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47558 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:438:8"]]
+ 00b47558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae77d4 bytes bfe21539
+ 00b47558 bytes bfe21039
- 00ae77fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae77fc ["INT_ADD", "register:40f0:8", ["const:ae77fc:8", "const:4:8"]]
- 00ae77fc ["CALLIND", null, ["register:0:8"]]
- 00ae77fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a22164d0dc848f0acf9da6325de51b5"></a>

### [`00ae7838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md) → [`00b475bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae7878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b475fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7854"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae784c",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47600"
      ]
    ],
    [
      "unmatched:00ae785c",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b475d0",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b475d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47600"
      ]
    ],
    [
      "00b475e0",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md#insn-00ae7854) · [`00ae7870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md#insn-00ae7870) · [`00ae7878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md#insn-00ae7878)
- 新版 [`00b475f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b475bc.md#insn-00b475f4)

~~~diff
- 00ae7854 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7854 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7854 bytes 410100b5
- 00ae7870 ["INT_ADD", "register:40f0:8", ["const:ae7870:8", "const:4:8"]]
- 00ae7870 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b475f4 ["INT_ADD", "register:40f0:8", ["const:b475f4:8", "const:4:8"]]
+ 00b475f4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7870 bytes 08da0394
+ 00b475f4 bytes 474d0494
- 00ae7878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00ae7878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7878 bytes 80ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

