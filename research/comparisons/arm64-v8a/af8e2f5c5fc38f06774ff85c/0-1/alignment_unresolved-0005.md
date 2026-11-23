# v15.7.2 → v15.7.3 · 命令位置の検査未完了 (5)

[一覧の目次](README.md)

<a id="compare-4fba9c76c8cbe5c91e2750bdce248384"></a>

### [`00b728cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b728cc.md) → [`00b72994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72994.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdaf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf70.md) · 呼出先 3件 [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bdc7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7b0.md)
- 新版 呼出元 1件 [`00bdb020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb020.md) · 呼出先 3件 [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bdc860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc860.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b7290c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7291c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b729d4"
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
      "00b729b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7290c"
      ]
    ],
    [
      "unmatched:00b7290c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb220"
      ]
    ],
    [
      "unmatched:00b72918",
      "PARAM",
      [
        "storage",
        "0029568a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b729b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b729d4"
      ]
    ],
    [
      "00b729d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb220"
      ]
    ],
    [
      "00b729e0",
      "PARAM",
      [
        "storage",
        "00295717",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b728cc.md#insn-00b72908) · [`00b7290c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b728cc.md#insn-00b7290c) · [`00b7291c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b728cc.md#insn-00b7291c)

~~~diff
- 00b72908 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b72908 ["RETURN", null, ["register:0:8"]]
- 00b72908 bytes c0035fd6
- 00b7290c ["INT_ADD", "register:40f0:8", ["const:b7290c:8", "const:4:8"]]
- 00b7290c ["CALL", null, ["callee:00bdb220:8"]]
- 00b7290c bytes 19a20194
- 00b7291c ["INT_ADD", "register:40f0:8", ["const:b7291c:8", "const:4:8"]]
- 00b7291c ["CALL", null, ["callee:00bdb280:8"]]
- 00b7291c bytes 2da20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ebac8987401837d6cd37d7d484b477d"></a>

### [`00b72924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72924.md) → [`00b729ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b729ec.md) _ZSt18uncaught_exceptionv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be00f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00f0.md) · 呼出先 1件 [`00be0e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e00.md)
- 新版 呼出元 1件 [`00be01a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01a0.md) · 呼出先 1件 [`00be0eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0eb0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "00b72944"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b72a0c"
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
      "unmatched:00b7293c",
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
      "00b72a04",
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

- 旧版 [`00b72944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72924.md#insn-00b72944) · [`00b72930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72924.md#insn-00b72930)
- 新版 `00b72a0c`（命令位置の公開資料なし） · `00b729f8`（命令位置の公開資料なし）

~~~diff
- 00b72944 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b72944 ["RETURN", null, ["register:0:8"]]
- 00b72944 bytes c0035fd6
+ 00b72a0c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b72a0c ["RETURN", null, ["register:0:8"]]
+ 00b72a0c bytes c0035fd6
- 00b72930 ["INT_ADD", "register:40f0:8", ["const:b72930:8", "const:4:8"]]
- 00b72930 ["CALL", null, ["callee:00be0eb0:8"]]
+ 00b729f8 ["INT_ADD", "register:40f0:8", ["const:b729f8:8", "const:4:8"]]
+ 00b729f8 ["CALL", null, ["callee:00be0eb0:8"]]
- 00b72930 bytes 34b90194
+ 00b729f8 bytes 2eb90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaf521d1f05d59d705da769dfbc14d80"></a>

### [`00b729d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b729d0.md) → [`00b72a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a98.md) _ZNSt16nested_exceptionC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ef0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b729f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72ab8"
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
      "unmatched:00b729e8",
      "READ",
      [
        "storage",
        "00c1bb40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b729f0",
      "DATA",
      [
        "storage",
        "00c12b30",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b72ab0",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b72ab8",
      "DATA",
      [
        "storage",
        "00c12be0",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b729f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b729d0.md#insn-00b729f0) · [`00b729e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b729d0.md#insn-00b729e8)
- 新版 `00b72ab8`（命令位置の公開資料なし）

~~~diff
- 00b729f0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b729f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b729f0 bytes 080000f9
+ 00b72ab8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b72ab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b72ab8 bytes 080000f9
- 00b729e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b40:8"]]
- 00b729e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b729e8 bytes 08a145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0063c3cb00601823910221c3fac9a4f6"></a>

### [`00b72a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a38.md) → [`00b72b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b00.md) _ZNSt16nested_exceptionD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e50.md) · 呼出先 1件 [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md)
- 新版 呼出元 1件 [`00be0f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f00.md) · 呼出先 1件 [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b72a48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72b10"
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
      "unmatched:00b72a40",
      "READ",
      [
        "storage",
        "00c1bb40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b72a48",
      "DATA",
      [
        "storage",
        "00c12b30",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "unmatched:00b72a4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb450"
      ]
    ]
  ],
  "added": [
    [
      "00b72b08",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b72b10",
      "DATA",
      [
        "storage",
        "00c12be0",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00b72b14",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb450"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a38.md#insn-00b72a48) · [`00b72a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a38.md#insn-00b72a3c)
- 新版 `00b72b10`（命令位置の公開資料なし）

~~~diff
- 00b72a48 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b72a48 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b72a48 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b72a48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b72a48 bytes 088400f8
+ 00b72b10 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b72b10 ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00b72b10 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00b72b10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b72b10 bytes 088400f8
- 00b72a3c ["COPY", "register:4040:8", ["const:c1b000:8"]]
- 00b72a3c bytes 480500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f26a6c2c5e11135f1324fb2a847422"></a>

### [`00b72aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72aec.md) → [`00b72bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72bb4.md) _ZNSt6__ndk112__next_primeEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8d0.md) · 呼出先 1件 [`00b7320c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7320c.md)
- 新版 呼出元 1件 [`00bdd980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd980.md) · 呼出先 1件 [`00b732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 86.40% / 新版 86.40%

CFGの説明率　旧版 44.16% / 新版 46.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 26件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72cd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b72cd8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b72c44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b732b0"
      ]
    ],
    [
      "unmatched:00b72cd8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72bfc"
      ]
    ],
    [
      "unmatched:00b72d64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b732b0"
      ]
    ]
  ],
  "added": [
    [
      "00b72d0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b732b0"
      ]
    ],
    [
      "00b72da0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72bfc"
      ]
    ],
    [
      "00b72e2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b732b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b72c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72aec.md#insn-00b72c44) · [`00b72cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72aec.md#insn-00b72cd0) · [`00b72cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72aec.md#insn-00b72cd8)

~~~diff
- 00b72c44 ["CBRANCH", null, ["local:b128:8", "register:101:1"]]
- 00b72c44 bytes 202d0054
- 00b72cd0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b72cd0 ["INT_EQUAL", "tmp:1:1", ["register:4078:8", "const:0:8"]]
- 00b72cd0 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b72cd0 ["INT_DIV", "tmp:0:8", ["register:4000:8", "register:4078:8"]]
- 00b72cd0 bytes 1008cf9a
- 00b72cd8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b72cd8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b72cd8 bytes e3f2ff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a41a80a1bb7296abd3ddb259aba6cd"></a>

### [`00b7342c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7342c.md) → [`00b734f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b734f4.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73448"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b73510"
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
      "unmatched:00b73448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b73530"
      ]
    ]
  ],
  "added": [
    [
      "00b73510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b73530"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7342c.md#insn-00b73448) · [`00b73450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7342c.md#insn-00b73450)
- 新版 `00b73510`（命令位置の公開資料なし） · `00b73518`（命令位置の公開資料なし）

~~~diff
- 00b73448 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b73448 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b73448 bytes 080100b4
+ 00b73510 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b73510 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b73510 bytes 080100b4
- 00b73450 ["INT_ADD", "register:40f0:8", ["const:b73450:8", "const:4:8"]]
- 00b73450 ["CALL", null, ["callee:00bd6e50:8"]]
+ 00b73518 ["INT_ADD", "register:40f0:8", ["const:b73518:8", "const:4:8"]]
+ 00b73518 ["CALL", null, ["callee:00bd6e50:8"]]
- 00b73450 bytes 508e0194
+ 00b73518 bytes 4e8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-163a5937cc59de0fa46fea6f0624fc1f"></a>

### [`00b736a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b736a8.md) → [`00b73770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73770.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdafe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafe0.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdb090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb090.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

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
      "site": "00b736d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b73798"
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
      "unmatched:00b736c8",
      "READ",
      [
        "storage",
        "00c1bb60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b736d0",
      "DATA",
      [
        "storage",
        "00c16830",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b73790",
      "READ",
      [
        "storage",
        "00c1bc10",
        null,
        "pointer"
      ]
    ],
    [
      "00b73798",
      "DATA",
      [
        "storage",
        "00c168e0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b736d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b736a8.md#insn-00b736d0) · [`00b736c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b736a8.md#insn-00b736c8)
- 新版 `00b73798`（命令位置の公開資料なし）

~~~diff
- 00b736d0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b736d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b736d0 bytes 080000f9
+ 00b73798 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b73798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b73798 bytes 080000f9
- 00b736c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 00b736c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b736c8 bytes 08b145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8ac4dedf3f6f47a2f1a8f35fa25e43e"></a>

### [`00b73da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73da4.md) → [`00b73e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73e6c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16find_last_not_ofEPKcmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.88% / 新版 96.88%

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
      "site": "00b73e20"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b73ee8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b73e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73da4.md#insn-00b73e20) · [`00b73e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73da4.md#insn-00b73e00)
- 新版 `00b73ee8`（命令位置の公開資料なし） · `00b73ec8`（命令位置の公開資料なし）

~~~diff
- 00b73e20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b73e20 ["RETURN", null, ["register:0:8"]]
- 00b73e20 bytes c0035fd6
+ 00b73ee8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b73ee8 ["RETURN", null, ["register:0:8"]]
+ 00b73ee8 bytes c0035fd6
- 00b73e00 ["INT_ADD", "register:40f0:8", ["const:b73e00:8", "const:4:8"]]
- 00b73e00 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b73ec8 ["INT_ADD", "register:40f0:8", ["const:b73ec8:8", "const:4:8"]]
+ 00b73ec8 ["CALL", null, ["callee:00bdb130:8"]]
- 00b73e00 bytes a09c0194
+ 00b73ec8 bytes 9a9c0194
~~~


<a id="compare-b30ddf43f1d9f8aa9303bb379bddc634"></a>

### [`00b73e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73e3c.md) → [`00b73f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73f04.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofEPKcmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 54.55% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b73f68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b73ec4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b73ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b73f4c"
      ]
    ]
  ],
  "added": [
    [
      "00b73f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b73f4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b73ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73e3c.md#insn-00b73ea0) · [`00b73ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73e3c.md#insn-00b73ec4)
- 新版 `00b73f68`（命令位置の公開資料なし）

~~~diff
- 00b73ea0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b73ea0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b73ea0 bytes 21ffff54
- 00b73ec4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b73ec4 ["RETURN", null, ["register:0:8"]]
- 00b73ec4 bytes c0035fd6
+ 00b73f68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b73f68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b73f68 bytes 21ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3e70feaa4679a82f497e9ffb3905bf"></a>

### [`00b74088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74088.md) → [`00b74150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74150.md) FUN_00b74150

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b74350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74350.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00b74418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74418.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 88.89% / 新版 84.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b741b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b74278"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b741b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74088.md#insn-00b741b0) · [`00b740b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74088.md#insn-00b740b8)
- 新版 `00b74278`（命令位置の公開資料なし） · `00b74180`（命令位置の公開資料なし）

~~~diff
- 00b741b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b741b0 ["RETURN", null, ["register:0:8"]]
- 00b741b0 bytes c0035fd6
+ 00b74278 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b74278 ["RETURN", null, ["register:0:8"]]
+ 00b74278 bytes c0035fd6
- 00b740b8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b740b8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00b74180 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b74180 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b740b8 bytes e3070054
+ 00b74180 bytes e3070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbfcf28b8909854117ec5b6f4fe4c147"></a>

### [`00b74620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74620.md) → [`00b746e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b746e8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4copyEPcmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74668"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b74730"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b74668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74620.md#insn-00b74668) · [`00b74648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74620.md#insn-00b74648)
- 新版 `00b74730`（命令位置の公開資料なし） · `00b74710`（命令位置の公開資料なし）

~~~diff
- 00b74668 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b74668 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b74668 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b74668 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b74668 bytes 4915809a
+ 00b74730 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b74730 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b74730 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b74730 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
+ 00b74730 bytes 4915809a
- 00b74648 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b74648 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b74710 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b74710 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b74648 bytes 23020054
+ 00b74710 bytes 23020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cbf2904bfce953a26331bbf0aa8dd8e"></a>

### [`00b74690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74690.md) → [`00b74758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74758.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 81.82% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b746bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b746c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b74784"
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
      "unmatched:00b746c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74824"
      ]
    ]
  ],
  "added": [
    [
      "00b7478c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74824"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b746bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74690.md#insn-00b746bc) · [`00b746c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74690.md#insn-00b746c4)
- 新版 `00b74784`（命令位置の公開資料なし）

~~~diff
- 00b746bc ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b746bc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b746bc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b746bc ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b746bc bytes 4901899a
- 00b746c4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b746c4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b746c4 bytes c3040054
+ 00b74784 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b74784 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b74784 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b74784 ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 00b74784 bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f44d039c648997246a6e9f37ee3b063"></a>

### [`00b7476c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b7476c.md) → [`00b74834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74834.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb680.md) · 呼出先 1件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md)
- 新版 呼出元 1件 [`00bdb730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb730.md) · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74780"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74788"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b74848"
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
      "unmatched:00b74788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7489c"
      ]
    ]
  ],
  "added": [
    [
      "00b74850",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7489c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b74780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b7476c.md#insn-00b74780) · [`00b74788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b7476c.md#insn-00b74788)
- 新版 `00b74848`（命令位置の公開資料なし）

~~~diff
- 00b74780 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b74780 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b74780 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b74780 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b74780 bytes 4801889a
- 00b74788 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b74788 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b74788 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00b74788 bytes 69020054
+ 00b74848 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b74848 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b74848 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b74848 ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00b74848 bytes 4801889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f0094cb23e47832a7e697d52ce226cc"></a>

### [`00b74c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c18.md) → [`00b74ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ce0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdc9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc9e0.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00b74c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c90.md)
- 新版 呼出元 1件 [`00bdca90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca90.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00b74d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74d58.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 80.00% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74c40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b74d00"
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
      "unmatched:00b74c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74d54"
      ]
    ]
  ],
  "added": [
    [
      "00b74d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b74d54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b74c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c18.md#insn-00b74c38) · [`00b74c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74c18.md#insn-00b74c40)
- 新版 `00b74d00`（命令位置の公開資料なし）

~~~diff
- 00b74c38 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b74c38 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b74c38 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b74c38 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b74c38 bytes 4901899a
- 00b74c40 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b74c40 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b74c40 bytes 63020054
+ 00b74d00 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b74d00 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b74d00 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b74d00 ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 00b74d00 bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e9f20226da7b3f70687d84b86dde8c"></a>

### [`00b74f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74f2c.md) → [`00b74ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b74/00b74ff4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 75.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b74f88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b75050"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b74f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74f2c.md#insn-00b74f88) · [`00b74f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b74/00b74f2c.md#insn-00b74f54)
- 新版 `00b75050`（命令位置の公開資料なし） · `00b7501c`（命令位置の公開資料なし）

~~~diff
- 00b74f88 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b74f88 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b74f88 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b74f88 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00b74f88 bytes 2931969a
+ 00b75050 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b75050 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00b75050 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b75050 ["COPY", "tmp:1:8", ["register:40b0:8"]]
+ 00b75050 bytes 2931969a
- 00b74f54 ["INT_ADD", "register:40f0:8", ["const:b74f54:8", "const:4:8"]]
- 00b74f54 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b7501c ["INT_ADD", "register:40f0:8", ["const:b7501c:8", "const:4:8"]]
+ 00b7501c ["CALL", null, ["callee:00bdb140:8"]]
- 00b74f54 bytes 4f980194
+ 00b7501c bytes 49980194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c7ef35a5f7a0a7142856da6e9a66b7f"></a>

### [`00b75058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75058.md) → [`00b75120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75120.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 71.43% / 新版 78.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75080"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75084"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b75148"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b75080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75058.md#insn-00b75080) · [`00b75084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75058.md#insn-00b75084)
- 新版 `00b75148`（命令位置の公開資料なし）

~~~diff
- 00b75080 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b75080 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00b75080 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b75080 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b75080 bytes 7715809a
- 00b75084 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b75084 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b75084 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b75084 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b75084 bytes 4801899a
+ 00b75148 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b75148 ["COPY", "tmp:1:8", ["register:4058:8"]]
+ 00b75148 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b75148 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
+ 00b75148 bytes 7715809a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3945db732d5d3c68804d60be274042e2"></a>

### [`00b75128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75128.md) → [`00b751f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b751f0.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmRKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75168"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7518c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b75230"
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
      "unmatched:00b75168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75294"
      ]
    ],
    [
      "unmatched:00b751d0",
      "PARAM",
      [
        "storage",
        "0029f1a9",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b751d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00b75230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75294"
      ]
    ],
    [
      "00b75298",
      "PARAM",
      [
        "storage",
        "0029f236",
        null,
        "string"
      ]
    ],
    [
      "00b7529c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0041fdf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75128.md#insn-00b75168) · [`00b7518c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75128.md#insn-00b7518c) · [`00b751d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75128.md#insn-00b751d4)

~~~diff
- 00b75168 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b75168 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b75168 bytes 23030054
- 00b7518c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7518c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b7518c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b7518c ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00b7518c bytes 5431859a
- 00b751d4 ["INT_ADD", "register:40f0:8", ["const:b751d4:8", "const:4:8"]]
- 00b751d4 ["CALL", null, ["callee:0041fdf0:8"]]
- 00b751d4 bytes 07abe297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8db86f4044b2c38bae85fbfc06a61ef"></a>

### [`00b75734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75734.md) → [`00b757fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b757fc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmRKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00bdc080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75734.md#insn-00b75750) · [`00b75768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75734.md#insn-00b75768) · [`00b75780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75734.md#insn-00b75780)
- 新版 `00b75818`（命令位置の公開資料なし） · `00b75848`（命令位置の公開資料なし）

~~~diff
- 00b75750 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b75750 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b75818 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b75818 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b75750 bytes 23010054
+ 00b75818 bytes 23010054
- 00b75768 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00b75768 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00b75768 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00b75768 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00b75768 bytes 4201038b
- 00b75780 ["INT_ADD", "register:40f0:8", ["const:b75780:8", "const:4:8"]]
- 00b75780 ["CALL", null, ["callee:0041fddc:8"]]
+ 00b75848 ["INT_ADD", "register:40f0:8", ["const:b75848:8", "const:4:8"]]
+ 00b75848 ["CALL", null, ["callee:0041fddc:8"]]
- 00b75780 bytes 97a9e297
+ 00b75848 bytes 65a9e297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6665635f87b880379509448def73cfa"></a>

### [`00b75974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75974.md) → [`00b75a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a3c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 35.71% / 新版 37.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75ac0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b75b88"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b759f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b75a38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75bb8"
      ]
    ]
  ],
  "added": [
    [
      "00b75b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75bb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b759f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75974.md#insn-00b759f8) · [`00b75a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75974.md#insn-00b75a38) · [`00b75ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75974.md#insn-00b75ac0)

~~~diff
- 00b759f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b759f8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b759f8 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b759f8 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b759f8 bytes 2881889a
- 00b75a38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b75a38 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00b75a38 bytes c80500b5
- 00b75ac0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b75ac0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b75ac0 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b75ac0 ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 00b75ac0 bytes 7f7b29b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17392351b37b72239352c25ade837352"></a>

### [`00b75c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75c9c.md) → [`00b75d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75d64.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ef0.md) [`00be0f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be0fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fa0.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b75cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75c9c.md#insn-00b75cac) · [`00b75cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75c9c.md#insn-00b75cc4)
- 新版 `00b75d8c`（命令位置の公開資料なし） · `00b75d74`（命令位置の公開資料なし）

~~~diff
- 00b75cac ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b75cac bytes fd030091
- 00b75cc4 ["INT_ADD", "register:40f0:8", ["const:b75cc4:8", "const:4:8"]]
- 00b75cc4 ["CALL", null, ["callee:00be0fc0:8"]]
+ 00b75d8c ["INT_ADD", "register:40f0:8", ["const:b75d8c:8", "const:4:8"]]
+ 00b75d8c ["CALL", null, ["callee:00be0fc0:8"]]
- 00b75cc4 bytes 93ac0194
+ 00b75d8c bytes 8dac0194
+ 00b75d74 ["COPY", "register:40e8:8", ["register:8:8"]]
+ 00b75d74 bytes fd030091
~~~


<a id="compare-1cff145f308e3f417968d5936d0646b6"></a>

### [`00b75e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75e60.md) → [`00b75f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75f28.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f20.md) · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 1件 [`00be0fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fd0.md) · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.74% / 新版 76.74%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7603c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b75e88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b75e90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7607c"
      ]
    ],
    [
      "unmatched:00b75ec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75fc0"
      ]
    ],
    [
      "unmatched:00b75f3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b75f70"
      ]
    ]
  ],
  "added": [
    [
      "00b75f58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7607c"
      ]
    ],
    [
      "00b75f8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b75fc0"
      ]
    ],
    [
      "00b76004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76038"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b75e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75e60.md#insn-00b75e88) · [`00b75e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75e60.md#insn-00b75e90) · [`00b75eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75e60.md#insn-00b75eb8)

~~~diff
- 00b75e88 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b75e88 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b75e88 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b75e88 ["COPY", "register:40a0:8", ["tmp:0:8"]]
- 00b75e88 bytes 5401899a
- 00b75e90 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b75e90 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00b75e90 bytes 23090054
- 00b75eb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b75eb8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b75eb8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b75eb8 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b75eb8 bytes 01018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c8738a6a7decc2334a1a4a7147507d0"></a>

### [`00b75fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75fec.md) → [`00b760b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b760b4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 37.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7600c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7603c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76048"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7600c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7615c"
      ]
    ],
    [
      "unmatched:00b76048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76164"
      ]
    ]
  ],
  "added": [
    [
      "00b760d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7615c"
      ]
    ],
    [
      "00b76110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76164"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7600c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75fec.md#insn-00b7600c) · [`00b7603c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75fec.md#insn-00b7603c) · [`00b76048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75fec.md#insn-00b76048)

~~~diff
- 00b7600c ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00b7600c bytes 42040054
- 00b7603c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7603c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7603c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b7603c ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b7603c bytes 0801899a
- 00b76048 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b76048 bytes a2020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64768581870affec957f086953af5aba"></a>

### [`00b76294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76294.md) → [`00b7635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b7635c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 85.19% / 新版 88.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b762d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b762f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76304"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76408"
      ]
    ]
  ],
  "added": [
    [
      "00b763cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76408"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b762d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76294.md#insn-00b762d8) · [`00b762f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76294.md#insn-00b762f4) · [`00b76304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76294.md#insn-00b76304)

~~~diff
- 00b762d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b762d8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b762d8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b762d8 ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00b762d8 bytes 1631829a
- 00b762f4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b762f4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b762f4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b762f4 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b762f4 bytes 21018b9a
- 00b76304 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00b76304 bytes e2010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e4622aee9f2a6679defcdd3ba8f9ba"></a>

### [`00b76960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76960.md) → [`00b76a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a28.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7699c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b76a64"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7699c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76960.md#insn-00b7699c) · [`00b7697c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76960.md#insn-00b7697c)
- 新版 `00b76a64`（命令位置の公開資料なし） · `00b76a44`（命令位置の公開資料なし）

~~~diff
- 00b7699c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b7699c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7699c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b7699c ["COPY", "register:4098:8", ["tmp:0:8"]]
- 00b7699c bytes 73018a9a
+ 00b76a64 ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00b76a64 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b76a64 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b76a64 ["COPY", "register:4098:8", ["tmp:0:8"]]
+ 00b76a64 bytes 73018a9a
- 00b7697c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7697c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b7697c ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
+ 00b76a44 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b76a44 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00b76a44 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00b7697c bytes 89020054
+ 00b76a44 bytes 89020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f07bdd1fc935b9bac2beebd6fc3d0dd1"></a>

### [`00b769d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b769d4.md) → [`00b76a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76a9c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEmw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 50.00% / 新版 52.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b769d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b769d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b769dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b769d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b769dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b769e0",
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
      "00b76aa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b76aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b76aa8",
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

- 旧版 [`00b769d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b769d4.md#insn-00b769d8) · [`00b769dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b769d4.md#insn-00b769dc) · [`00b769e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b769d4.md#insn-00b769e0)

~~~diff
- 00b769d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b769d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b769d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b769d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b769d8 bytes fd7bbda9
- 00b769dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b769dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b769dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b769dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b769dc bytes f65701a9
- 00b769e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b769e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b769e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b769e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b769e0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc504bb73fe60d8ffabf38989377a06"></a>

### [`00b76b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76b10.md) → [`00b76bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76bd8.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE12find_last_ofEPKwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 44.44% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b76b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76b10.md#insn-00b76b28) · [`00b76b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76b10.md#insn-00b76b3c) · [`00b76b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76b10.md#insn-00b76b68)
- 新版 `00b76bf0`（命令位置の公開資料なし） · `00b76c30`（命令位置の公開資料なし）

~~~diff
- 00b76b28 ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
- 00b76b28 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b76bf0 ["INT_EQUAL", "tmp:0:1", ["register:4018:8", "const:0:8"]]
+ 00b76bf0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b76b28 bytes 230300b4
+ 00b76bf0 bytes 230300b4
- 00b76b3c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b76b3c bytes fd030091
- 00b76b68 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b76b68 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b76c30 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b76c30 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b76b68 bytes 750100b4
+ 00b76c30 bytes 750100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0bfb4025ab8bf127baff8586e0008b2"></a>

### [`00b76ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76ebc.md) → [`00b76f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b76/00b76f84.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5rfindEwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 50.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76ed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76edc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b76edc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76fd4"
      ]
    ]
  ],
  "added": [
    [
      "00b76fa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76fd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b76ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76ebc.md#insn-00b76ed4) · [`00b76ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76ebc.md#insn-00b76ed8) · [`00b76edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b76/00b76ebc.md#insn-00b76edc)

~~~diff
- 00b76ed4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b76ed4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76ed4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b76ed4 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b76ed4 bytes 4801899a
- 00b76ed8 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b76ed8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b76ed8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b76ed8 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b76ed8 bytes 89018b9a
- 00b76edc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b76edc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b76edc bytes 880100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-311f96a15aa8fc77d76eb83a1ab968eb"></a>

### [`00b7702c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7702c.md) → [`00b770f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b770f4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5eraseEmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00b770a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b770a4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00b7716c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7716c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7704c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77054"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7705c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b77054",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77168"
      ]
    ],
    [
      "unmatched:00b7705c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77138"
      ]
    ]
  ],
  "added": [
    [
      "00b7711c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77168"
      ]
    ],
    [
      "00b77124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77138"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7704c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7702c.md#insn-00b7704c) · [`00b77054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7702c.md#insn-00b77054) · [`00b7705c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7702c.md#insn-00b7705c)

~~~diff
- 00b7704c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b7704c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7704c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b7704c ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b7704c bytes 4901899a
- 00b77054 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b77054 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b77054 bytes 63020054
- 00b7705c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00b7705c bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79866c7d63c7429be93e8e00c6be6a12"></a>

### [`00b77140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77140.md) → [`00b77208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77208.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendERKS5_mm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 73.13% / 新版 73.13%

CFGの説明率　旧版 26.67% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77188"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77194"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b771ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b771c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b772ac"
      ]
    ]
  ],
  "added": [
    [
      "00b77288",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b772ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b77188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77140.md#insn-00b77188) · [`00b77194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77140.md#insn-00b77194) · [`00b771ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77140.md#insn-00b771ac)

~~~diff
- 00b77188 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b77188 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b77188 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b77188 ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00b77188 bytes 8b018b9a
- 00b77194 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b77194 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b77194 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b77194 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00b77194 bytes 2631839a
- 00b771ac ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b771ac ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b771ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b771ac ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b771ac bytes 4101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7601f6894f0a10acb4e0704ed8b64443"></a>

### [`00b772e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b772e4.md) → [`00b773ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b773ac.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00be0f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7730c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b773d4"
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
      "unmatched:00b7730c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77434"
      ]
    ]
  ],
  "added": [
    [
      "00b773d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b77434"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7730c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b772e4.md#insn-00b7730c) · [`00b77348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b772e4.md#insn-00b77348)
- 新版 `00b773d4`（命令位置の公開資料なし） · `00b77410`（命令位置の公開資料なし）

~~~diff
- 00b7730c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b7730c bytes 00030054
+ 00b773d4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00b773d4 bytes 00030054
- 00b77348 ["INT_ADD", "register:40f0:8", ["const:b77348:8", "const:4:8"]]
- 00b77348 ["CALL", null, ["callee:00be1000:8"]]
+ 00b77410 ["INT_ADD", "register:40f0:8", ["const:b77410:8", "const:4:8"]]
+ 00b77410 ["CALL", null, ["callee:00be1000:8"]]
- 00b77348 bytes 02a70194
+ 00b77410 bytes fca60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b938c0a81f5e63438e259e73a2fc8c"></a>

### [`00b77370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77370.md) → [`00b77438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77438.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7595c.md) [`00be0f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f10.md) [`00be0f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b75a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75a24.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 36.36% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b773b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b77478"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b773b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77370.md#insn-00b773b0) · [`00b7739c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77370.md#insn-00b7739c)
- 新版 `00b77478`（命令位置の公開資料なし） · `00b77464`（命令位置の公開資料なし）

~~~diff
- 00b773b0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b773b0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b773b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b773b0 ["COPY", "register:4048:8", ["tmp:0:8"]]
- 00b773b0 bytes 4901899a
+ 00b77478 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00b77478 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b77478 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b77478 ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 00b77478 bytes 4901899a
- 00b7739c ["INT_ADD", "register:40f0:8", ["const:b7739c:8", "const:4:8"]]
- 00b7739c ["CALL", null, ["callee:00be0fc0:8"]]
+ 00b77464 ["INT_ADD", "register:40f0:8", ["const:b77464:8", "const:4:8"]]
+ 00b77464 ["CALL", null, ["callee:00be0fc0:8"]]
- 00b7739c bytes dda60194
+ 00b77464 bytes d7a60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76b607cc89aeb90e06f86e1dd67bf4b0"></a>

### [`00b774b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b774b4.md) → [`00b7757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7757c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEPKwmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md) [`00be0f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md) [`00be1000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 50.00% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b774e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b774e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b774ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b774ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b775c0"
      ]
    ],
    [
      "unmatched:00b77510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7760c"
      ]
    ]
  ],
  "added": [
    [
      "00b775b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b775c0"
      ]
    ],
    [
      "00b775d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7760c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b774e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b774b4.md#insn-00b774e0) · [`00b774e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b774b4.md#insn-00b774e4) · [`00b774ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b774b4.md#insn-00b774ec)

~~~diff
- 00b774e0 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b774e0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b774e0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b774e0 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b774e0 bytes 97018b9a
- 00b774e4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b774e4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b774e4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b774e4 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b774e4 bytes 4801899a
- 00b774ec ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b774ec bytes 62000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3fdf7e7957a47f9b8da4c5d727cf57a"></a>

### [`00b7764c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7764c.md) → [`00b77714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77714.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEaSERKS5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b776a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b776a4.md) [`00b77778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77778.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7776c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b7776c.md) [`00b77840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77840.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 44.44% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7768c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b77690"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b77754"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7768c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7764c.md#insn-00b7768c) · [`00b77690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b7764c.md#insn-00b77690)
- 新版 `00b77754`（命令位置の公開資料なし）

~~~diff
- 00b7768c ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b7768c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b7768c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b7768c ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b7768c bytes 8101899a
- 00b77690 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b77690 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b77690 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b77690 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b77690 bytes 62018a9a
+ 00b77754 ["COPY", "tmp:0:8", ["register:4060:8"]]
+ 00b77754 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b77754 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b77754 ["COPY", "register:4008:8", ["tmp:0:8"]]
+ 00b77754 bytes 8101899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9368b039d2b11d5d652a048728568926"></a>

### [`00b77808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77808.md) → [`00b778d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b778d0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00be0f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f00.md) [`00be0f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0f10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00be0fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fb0.md) [`00be0fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0fc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7781c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77808.md#insn-00b7781c) · [`00b7782c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77808.md#insn-00b7782c) · [`00b77864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77808.md#insn-00b77864)
- 新版 `00b778f4`（命令位置の公開資料なし） · `00b7792c`（命令位置の公開資料なし）

~~~diff
- 00b7781c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b7781c bytes fd030091
- 00b7782c ["INT_ADD", "register:40f0:8", ["const:b7782c:8", "const:4:8"]]
- 00b7782c ["CALL", null, ["callee:00be0fc0:8"]]
+ 00b778f4 ["INT_ADD", "register:40f0:8", ["const:b778f4:8", "const:4:8"]]
+ 00b778f4 ["CALL", null, ["callee:00be0fc0:8"]]
- 00b7782c bytes b9a50194
+ 00b778f4 bytes b3a50194
- 00b77864 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 00b7792c ["CBRANCH", null, ["local:b2:8", "register:102:1"]]
- 00b77864 bytes 62010054
+ 00b7792c bytes 62010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6571bba77ff655a23d045b277c765468"></a>

### [`00b79314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79314.md) → [`00b793dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b793dc.md) _ZNSt6__ndk19to_stringEl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb280.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdb330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb330.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.04% / 新版 97.04%

CFGの説明率　旧版 75.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b794cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b79594"
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
      "unmatched:00b79490",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b79558",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b794cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79314.md#insn-00b794cc) · [`00b79398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79314.md#insn-00b79398)
- 新版 `00b79594`（命令位置の公開資料なし） · `00b79460`（命令位置の公開資料なし）

~~~diff
- 00b794cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b794cc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b794cc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b794cc ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b794cc bytes 0801899a
+ 00b79594 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b79594 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b79594 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b79594 ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00b79594 bytes 0801899a
- 00b79398 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b79398 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b79460 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b79460 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b79398 bytes 0b080054
+ 00b79460 bytes 0b080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52220b3f3ff523db77c1dd2095f518e7"></a>

### [`00b79530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79530.md) → [`00b795f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b795f8.md) _ZNSt6__ndk19to_stringEx

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbf0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bddca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddca0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 57.69% / 新版 57.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79678"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b79740"
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
      "unmatched:00b795e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b796d4"
      ]
    ],
    [
      "unmatched:00b79670",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79680",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b796a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b796d4"
      ]
    ],
    [
      "00b79738",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00b79748",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b795e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79530.md#insn-00b795e0) · [`00b79678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79530.md#insn-00b79678) · [`00b79688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79530.md#insn-00b79688)

~~~diff
- 00b795e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b795e0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b795e0 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00b795e0 bytes 69010054
- 00b79678 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b79678 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b79678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79678 bytes 08000079
- 00b79688 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:2:8"]]
- 00b79688 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 00b79688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b79688 bytes 0a040079
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c82ac0d23f746a7d512a0739e324453"></a>

### [`00b79d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79d78.md) → [`00b79e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79e40.md) _ZNSt6__ndk110to_wstringEl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.98% / 新版 75.98%

CFGの説明率　旧版 56.10% / 新版 56.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79d80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b79d84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b79d80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b79d88",
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
      "00b79e48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b79e4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b79e50",
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

- 旧版 [`00b79d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79d78.md#insn-00b79d80) · [`00b79d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79d78.md#insn-00b79d84) · [`00b79d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79d78.md#insn-00b79d88)

~~~diff
- 00b79d80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b79d80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b79d80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b79d80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b79d80 bytes fd7b02a9
- 00b79d84 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b79d84 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b79d84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b79d84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b79d84 bytes f65703a9
- 00b79d88 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b79d88 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b79d88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b79d88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b79d88 bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11693462039385bfd4add2bdc17fd952"></a>

### [`00b7a310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a310.md) → [`00b7a3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a3d8.md) _ZNSt6__ndk110to_wstringEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 54.17% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7a380",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a548"
      ]
    ],
    [
      "unmatched:00b7a3d4",
      "READ",
      [
        "storage",
        "002b11c0",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7a3d8",
      "READ",
      [
        "storage",
        "002b1a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7a448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a548"
      ]
    ],
    [
      "00b7a49c",
      "READ",
      [
        "storage",
        "002b11c0",
        null,
        null
      ]
    ],
    [
      "00b7a4a0",
      "READ",
      [
        "storage",
        "002b1a40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a310.md#insn-00b7a380) · [`00b7a424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a310.md#insn-00b7a424) · [`00b7a434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a310.md#insn-00b7a434)

~~~diff
- 00b7a380 ["CBRANCH", null, ["local:b17:8", "register:102:1"]]
- 00b7a380 bytes 02080054
- 00b7a424 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:ffffffffffffffe0:8"]]
- 00b7a424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50e0:16"]]
- 00b7a424 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7a424 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50c0:16"]]
- 00b7a424 bytes 87193fad
- 00b7a434 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:ffffffffffffffc0:8"]]
- 00b7a434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b7a434 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7a434 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
- 00b7a434 bytes 84413ead
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56191726a43b7a8dab1c46e0a83a4730"></a>

### [`00b7a484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a484.md) → [`00b7a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a54c.md) _ZNSt6__ndk110to_wstringEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.44% / 新版 85.44%

CFGの説明率　旧版 41.18% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a494"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a69c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7a494",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7a4a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a588"
      ]
    ],
    [
      "unmatched:00b7a62c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a708"
      ]
    ]
  ],
  "added": [
    [
      "00b7a55c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b7a570",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a588"
      ]
    ],
    [
      "00b7a6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a708"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a484.md#insn-00b7a494) · [`00b7a4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a484.md#insn-00b7a4a8)
- 新版 `00b7a55c`（命令位置の公開資料なし）

~~~diff
- 00b7a494 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7a494 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7a494 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b7a494 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7a494 bytes f44f04a9
- 00b7a4a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b7a4a8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b7a4a8 bytes c90000b5
+ 00b7a55c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b7a55c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b7a55c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 00b7a55c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b7a55c bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99d40382df015cc286f49dba76a11920"></a>

### [`00b7a6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a6fc.md) → [`00b7a7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7a/00b7a7c4.md) _ZNSt6__ndk110to_wstringEy

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8a4.md) [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`006ad8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8a4.md) [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.85% / 新版 77.85%

CFGの説明率　旧版 36.11% / 新版 36.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a914"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a914"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7a924"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7a720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a800"
      ]
    ],
    [
      "unmatched:00b7a748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a844"
      ]
    ],
    [
      "unmatched:00b7a7e8",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7a7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a800"
      ]
    ],
    [
      "00b7a810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7a844"
      ]
    ],
    [
      "00b7a8b0",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7a720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a6fc.md#insn-00b7a720) · [`00b7a748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a6fc.md#insn-00b7a748) · [`00b7a7e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7a/00b7a6fc.md#insn-00b7a7e8)

~~~diff
- 00b7a720 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b7a720 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b7a720 bytes c90000b5
- 00b7a748 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7a748 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00b7a748 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00b7a748 bytes a9010054
- 00b7a7e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7a7e8 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b7a7e8 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:1:8"]]
- 00b7a7e8 ["INT_ADD", "tmp:2:8", ["register:4060:8", "tmp:1:8"]]
- 00b7a7e8 bytes 88796878
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5ded128540a0db882dbee651ccb0761"></a>

### [`00b7b2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md) → [`00b7b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b3a4.md) FUN_00b7b3a4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00b791ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b791ec.md) [`00b79314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79314.md) [`00b79530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79530.md) [`00b7974c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b7974c.md) [`00b79810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b79810.md) · 呼出先 0件 
- 新版 呼出元 12件 [`00b792b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b792b4.md) [`00b793dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b793dc.md) [`00b795f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b795f8.md) [`00b79814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md) [`00b798d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b798d8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.32% / 新版 98.32%

CFGの説明率　旧版 52.38% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7b3a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7b468"
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
      "unmatched:00b7b39c",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7b3a8",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b7b464",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ],
    [
      "00b7b470",
      "DATA",
      [
        "storage",
        "002fa9a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7b3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md#insn-00b7b3a0) · [`00b7b2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b2dc.md#insn-00b7b2f8)
- 新版 `00b7b468`（命令位置の公開資料なし） · `00b7b3c0`（命令位置の公開資料なし）

~~~diff
- 00b7b3a0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b7b3a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:3:8"]]
- 00b7b3a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b7b3a0 bytes 0a300078
+ 00b7b468 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00b7b468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:3:8"]]
+ 00b7b468 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
+ 00b7b468 bytes 0a300078
- 00b7b2f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7b2f8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b7b2f8 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
+ 00b7b3c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b7b3c0 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b7b3c0 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00b7b2f8 bytes 28060054
+ 00b7b3c0 bytes 28060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6fe0c807066e892e17a2ccc6a0c095e"></a>

### [`00b7cf5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf5c.md) → [`00b7d024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d024.md) _ZNSt6__ndk17promiseIvE13set_exceptionESt13exception_ptr

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) [`00bdb3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3a0.md) [`00bdb410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb410.md) [`00bdb560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4c0.md) [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

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
      "site": "00b7cf60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cf60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cf64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7cf60",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7cf64",
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
      "00b7d028",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b7d02c",
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

- 旧版 [`00b7cf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf5c.md#insn-00b7cf60) · [`00b7cf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf5c.md#insn-00b7cf64)
- 新版 `00b7d028`（命令位置の公開資料なし）

~~~diff
- 00b7cf60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7cf60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7cf60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b7cf60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7cf60 bytes fd7bbea9
- 00b7cf64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b7cf64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7cf64 bytes f30b00f9
+ 00b7d028 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b7d028 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b7d028 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b7d028 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b7d028 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9acb36b8b96cfcf43c1d47da8563fb7b"></a>

### [`00b7d1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d1b4.md) → [`00b7d27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d27c.md) _ZNSt6__ndk15mutex4lockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb190.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1d0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md)
- 新版 呼出元 1件 [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md) · 呼出先 2件 [`00bdb280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb280.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

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
      "site": "00b7d1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b7d2a4"
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
      "unmatched:00b7d1d8",
      "PARAM",
      [
        "storage",
        "002a0ffa",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7d1dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb280"
      ]
    ]
  ],
  "added": [
    [
      "00b7d2a0",
      "PARAM",
      [
        "storage",
        "002a1087",
        null,
        "string"
      ]
    ],
    [
      "00b7d2a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb280"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d1b4.md#insn-00b7d1dc) · [`00b7d1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d1b4.md#insn-00b7d1c0)
- 新版 `00b7d2a4`（命令位置の公開資料なし） · `00b7d288`（命令位置の公開資料なし）

~~~diff
- 00b7d1dc ["INT_ADD", "register:40f0:8", ["const:b7d1dc:8", "const:4:8"]]
- 00b7d1dc ["CALL", null, ["callee:00bdb280:8"]]
- 00b7d1dc bytes fd770194
+ 00b7d2a4 ["INT_ADD", "register:40f0:8", ["const:b7d2a4:8", "const:4:8"]]
+ 00b7d2a4 ["CALL", null, ["callee:00bdb280:8"]]
+ 00b7d2a4 bytes f7770194
- 00b7d1c0 ["INT_ADD", "register:40f0:8", ["const:b7d1c0:8", "const:4:8"]]
- 00b7d1c0 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00b7d288 ["INT_ADD", "register:40f0:8", ["const:b7d288:8", "const:4:8"]]
+ 00b7d288 ["CALL", null, ["callee:00bde7d0:8"]]
- 00b7d1c0 bytes 58850194
+ 00b7d288 bytes 52850194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e98669c552d5204a33b0270574f1687"></a>

### [`00b7d318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d318.md) → [`00b7d3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d3e0.md) _ZNSt6__ndk115recursive_mutex6unlockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1a0.md) · 呼出先 1件 [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 1件 [`00bdd250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd250.md) · 呼出先 1件 [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "00b7d330"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b7d3f8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d318.md#insn-00b7d330) · [`00b7d324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d318.md#insn-00b7d324)
- 新版 `00b7d3f8`（命令位置の公開資料なし） · `00b7d3ec`（命令位置の公開資料なし）

~~~diff
- 00b7d330 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7d330 ["RETURN", null, ["register:0:8"]]
- 00b7d330 bytes c0035fd6
+ 00b7d3f8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b7d3f8 ["RETURN", null, ["register:0:8"]]
+ 00b7d3f8 bytes c0035fd6
- 00b7d324 ["INT_ADD", "register:40f0:8", ["const:b7d324:8", "const:4:8"]]
- 00b7d324 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00b7d3ec ["INT_ADD", "register:40f0:8", ["const:b7d3ec:8", "const:4:8"]]
+ 00b7d3ec ["CALL", null, ["callee:00bde7e0:8"]]
- 00b7d324 bytes 03850194
+ 00b7d3ec bytes fd840194
~~~


<a id="compare-3a8bd11ab2162e7c8ad1371f30501b68"></a>

### [`00b7d980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d980.md) → [`00b7da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md) FUN_00b7da48

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7dc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc74.md) · 呼出先 5件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1a0.md) [`00bdb430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb430.md) [`00be1150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1150.md)
- 新版 呼出元 1件 [`00b7dd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd3c.md) · 呼出先 5件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb250.md) [`00bdb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb4e0.md) [`00be1200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1200.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 87.50% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d984"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d984"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d988"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7d984",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d988",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d98c",
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
      "00b7da4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b7da50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b7da54",
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

- 旧版 [`00b7d984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d980.md#insn-00b7d984) · [`00b7d988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d980.md#insn-00b7d988) · [`00b7d98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d980.md#insn-00b7d98c)

~~~diff
- 00b7d984 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7d984 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7d984 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b7d984 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7d984 bytes fd7bbda9
- 00b7d988 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7d988 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7d988 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b7d988 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7d988 bytes f65701a9
- 00b7d98c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7d98c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7d98c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7d98c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7d98c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb510e9350fa2c7c359bcbb0e2b72f33"></a>

### [`00b7dc38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc38.md) → [`00b7dd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd00.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "site": "00b7dc70"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b7dd38"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc38.md#insn-00b7dc70) · [`00b7dc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc38.md#insn-00b7dc50)
- 新版 `00b7dd38`（命令位置の公開資料なし） · `00b7dd18`（命令位置の公開資料なし）

~~~diff
- 00b7dc70 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7dc70 ["RETURN", null, ["register:0:8"]]
- 00b7dc70 bytes c0035fd6
+ 00b7dd38 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b7dd38 ["RETURN", null, ["register:0:8"]]
+ 00b7dd38 bytes c0035fd6
- 00b7dc50 ["INT_ADD", "register:40f0:8", ["const:b7dc50:8", "const:4:8"]]
- 00b7dc50 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b7dd18 ["INT_ADD", "register:40f0:8", ["const:b7dd18:8", "const:4:8"]]
+ 00b7dd18 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b7dc50 bytes bc740194
+ 00b7dd18 bytes b6740194
~~~


<a id="compare-50f0924b5b100ab85ca316d657e576dc"></a>

### [`00b7dc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc74.md) → [`00b7dd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd3c.md) _ZNSt6__ndk115__thread_structD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb200.md) · 呼出先 2件 [`00b7d980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d980.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bdb2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2b0.md) · 呼出先 2件 [`00b7da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7da48.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00b7dc78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dc78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dc7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7dc78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7dc7c",
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
      "00b7dd40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b7dd44",
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

- 旧版 [`00b7dc78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc74.md#insn-00b7dc78) · [`00b7dc7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc74.md#insn-00b7dc7c)
- 新版 `00b7dd40`（命令位置の公開資料なし）

~~~diff
- 00b7dc78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7dc78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7dc78 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b7dc78 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7dc78 bytes fd7bbea9
- 00b7dc7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b7dc7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7dc7c bytes f30b00f9
+ 00b7dd40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b7dd40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b7dd40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b7dd40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b7dd40 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d5b5a76e7c2ddbb6e9a2eda69d6eff0"></a>

### [`00b7dcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcd0.md) → [`00b7dd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd98.md) FUN_00b7dd98

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7da4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7da4c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00b7db14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7db14.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b7ddac"
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
      "unmatched:00b7dce0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7dce4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00b7dda8",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ],
    [
      "00b7ddac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcd0.md#insn-00b7dce4) · [`00b7dce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dcd0.md#insn-00b7dce0)
- 新版 `00b7ddac`（命令位置の公開資料なし）

~~~diff
- 00b7dce4 ["INT_ADD", "register:40f0:8", ["const:b7dce4:8", "const:4:8"]]
- 00b7dce4 ["CALL", null, ["callee:00418c38:8"]]
- 00b7dce4 bytes d56be297
+ 00b7ddac ["INT_ADD", "register:40f0:8", ["const:b7ddac:8", "const:4:8"]]
+ 00b7ddac ["CALL", null, ["callee:00418c38:8"]]
+ 00b7ddac bytes a36be297
- 00b7dce0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00b7dce0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7dce0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7dce0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7dce0 bytes 00280c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497928f756b3cdda459be4c1b5d2cfe5"></a>

### [`00b7dce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dce8.md) → [`00b7ddb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7ddb0.md) FUN_00b7ddb0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7db48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7db48.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00b7dc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dc10.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dcec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7dcec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7ddb4"
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
      "unmatched:00b7dcec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7dcf8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7dcfc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00b7ddb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b7ddc0",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ],
    [
      "00b7ddc4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00418c38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7dcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dce8.md#insn-00b7dcec) · [`00b7dcfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dce8.md#insn-00b7dcfc)
- 新版 `00b7ddb4`（命令位置の公開資料なし）

~~~diff
- 00b7dcec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7dcec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7dcec ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00b7dcec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7dcec bytes fd7bbfa9
- 00b7dcfc ["INT_ADD", "register:40f0:8", ["const:b7dcfc:8", "const:4:8"]]
- 00b7dcfc ["CALL", null, ["callee:00418c38:8"]]
- 00b7dcfc bytes cf6be297
+ 00b7ddb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b7ddb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b7ddb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00b7ddb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b7ddb4 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa819c1f0ddf73585eda352eabfe9452"></a>

### [`00b7de94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de94.md) → [`00b7df5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7df5c.md) _ZNKSt6__ndk113random_device7entropyEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be11b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1260.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 20.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ded0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b7df98"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de94.md#insn-00b7ded0) · [`00b7deb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7de94.md#insn-00b7deb4)
- 新版 `00b7df98`（命令位置の公開資料なし） · `00b7df7c`（命令位置の公開資料なし）

~~~diff
- 00b7ded0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b7ded0 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b7ded0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b7ded0 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 00b7ded0 bytes 0831891a
+ 00b7df98 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b7df98 ["COPY", "tmp:1:4", ["register:4040:4"]]
+ 00b7df98 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b7df98 ["COPY", "tmp:1:4", ["register:4048:4"]]
+ 00b7df98 bytes 0831891a
- 00b7deb4 ["INT_ADD", "register:40f0:8", ["const:b7deb4:8", "const:4:8"]]
- 00b7deb4 ["CALL", null, ["callee:00be1260:8"]]
+ 00b7df7c ["INT_ADD", "register:40f0:8", ["const:b7df7c:8", "const:4:8"]]
+ 00b7df7c ["CALL", null, ["callee:00be1260:8"]]
- 00b7deb4 bytes bf8c0194
+ 00b7df7c bytes b98c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fb07033faf010495188d328b98c02f"></a>

### [`00b7defc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7defc.md) → [`00b7dfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dfc4.md) FUN_00b7dfc4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7b694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7b/00b7b694.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b7b75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7b/00b7b75c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7df50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7df54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7df58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7df48",
      "READ",
      [
        "storage",
        "002ad6de",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b7df48",
      "READ",
      [
        "storage",
        "002ad6ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b7e010",
      "READ",
      [
        "storage",
        "002ad6d5",
        null,
        "string"
      ]
    ],
    [
      "00b7e010",
      "READ",
      [
        "storage",
        "002ad6e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7df50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7defc.md#insn-00b7df50) · [`00b7df54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7defc.md#insn-00b7df54) · [`00b7df58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7defc.md#insn-00b7df58)

~~~diff
- 00b7df50 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b7df50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1f:8"]]
- 00b7df50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b7df50 bytes 09f001b8
- 00b7df54 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b7df54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b7df54 bytes 6002803d
- 00b7df58 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b7df58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b7df58 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b7df58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00b7df58 bytes 010800ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c8101f0cae88b37d7b960aea738839a"></a>

### [`00b7e0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e0d8.md) → [`00b7e1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e1a0.md) _ZNSt6__ndk18ios_base5imbueERKNS_6localeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd880.md) [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e0dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e0dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e0e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7e0dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7e0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7e0e4",
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
      "00b7e1a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b7e1a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b7e1ac",
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

- 旧版 [`00b7e0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e0d8.md#insn-00b7e0dc) · [`00b7e0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e0d8.md#insn-00b7e0e0) · [`00b7e0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e0d8.md#insn-00b7e0e4)

~~~diff
- 00b7e0dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7e0dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7e0dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b7e0dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7e0dc bytes fd7bbda9
- 00b7e0e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b7e0e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b7e0e0 bytes f50b00f9
- 00b7e0e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7e0e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7e0e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7e0e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7e0e4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6346929b691b7e3efb3a2415ae5a751f"></a>

### [`00b7e1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e1a0.md) → [`00b7e268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e268.md) _ZNSt6__ndk18ios_base5iwordEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7e5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.41% / 新版 88.41%

CFGの説明率　旧版 53.33% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e1b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e1b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e2a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7e1b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b7e35c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7e2a8"
      ]
    ],
    [
      "unmatched:00b7e29c",
      "DATA",
      [
        "storage",
        "010a1f98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7e278",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b7e35c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e370"
      ]
    ],
    [
      "00b7e364",
      "DATA",
      [
        "storage",
        "010a2058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e1a0.md#insn-00b7e1b0) · [`00b7e2a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e1a0.md#insn-00b7e2a0)
- 新版 `00b7e278`（命令位置の公開資料なし）

~~~diff
- 00b7e1b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7e1b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7e1b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b7e1b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7e1b0 bytes f44f03a9
+ 00b7e278 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b7e278 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b7e278 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
+ 00b7e278 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b7e278 bytes f44f03a9
- 00b7e2a0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b7e2a0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b7e2a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b7e2a0 bytes 1f0000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7328609383ca89032ddaa864d514235e"></a>

### [`00b7e2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e2b4.md) → [`00b7e37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e37c.md) _ZNSt6__ndk18ios_base5pwordEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7e5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e5c8.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b7e690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e690.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.36% / 新版 75.36%

CFGの説明率　旧版 11.11% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e2bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7e2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7e2bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7e2c0",
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
      "00b7e380",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b7e384",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b7e388",
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

- 旧版 [`00b7e2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e2b4.md#insn-00b7e2b8) · [`00b7e2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e2b4.md#insn-00b7e2bc) · [`00b7e2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e2b4.md#insn-00b7e2c0)

~~~diff
- 00b7e2b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7e2b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7e2b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b7e2b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7e2b8 bytes fd7bbca9
- 00b7e2bc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b7e2bc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b7e2bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b7e2bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7e2bc bytes f85f01a9
- 00b7e2c0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7e2c0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7e2c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7e2c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7e2c0 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2107a8ac6b3130dd86f4fab76d763452"></a>

### [`00b81920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81920.md) → [`00b819e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b819e8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8194c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81950"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8193c",
      "READ",
      [
        "storage",
        "00c1bbe8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b8194c",
      "DATA",
      [
        "storage",
        "00c12ff0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b81950",
      "DATA",
      [
        "storage",
        "00c12fc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b81a04",
      "READ",
      [
        "storage",
        "00c1bc98",
        null,
        "pointer"
      ]
    ],
    [
      "00b81a14",
      "DATA",
      [
        "storage",
        "00c130a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b81a18",
      "DATA",
      [
        "storage",
        "00c13078",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81920.md#insn-00b81940) · [`00b8194c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81920.md#insn-00b8194c) · [`00b81950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81920.md#insn-00b81950)

~~~diff
- 00b81940 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00b81940 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b81940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b81940 bytes 1f1c00f9
- 00b8194c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b8194c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 00b8194c ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00b8194c bytes 898e00f8
- 00b81950 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b81950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b81950 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee16368834c96d82e675aa8b77b202e1"></a>

### [`00b81994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81994.md) → [`00b81a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b81/00b81a5c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.00% / 新版 76.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8199c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8199c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b81a64"
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
      "unmatched:00b8199c",
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
      "00b81a64",
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

- 旧版 [`00b8199c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81994.md#insn-00b8199c) · [`00b819c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b81/00b81994.md#insn-00b819c4)
- 新版 `00b81a8c`（命令位置の公開資料なし） · `00b81a64`（命令位置の公開資料なし）

~~~diff
- 00b8199c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8199c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8199c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b8199c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8199c bytes f44f01a9
- 00b819c4 ["INT_ADD", "register:40f0:8", ["const:b819c4:8", "const:4:8"]]
- 00b819c4 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b81a8c ["INT_ADD", "register:40f0:8", ["const:b81a8c:8", "const:4:8"]]
+ 00b81a8c ["CALL", null, ["callee:00be12d0:8"]]
- 00b819c4 bytes 177e0194
+ 00b81a8c bytes 117e0194
+ 00b81a64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b81a64 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b81a64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00b81a64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b81a64 bytes f44f01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d4dc62501b3f7f81770dc6955f8e0e3"></a>

### [`00b824e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b824e8.md) → [`00b825b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b825b0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE3putEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb310.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdb360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb360.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3c0.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdb410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb410.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 18.18% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82528"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b825f0"
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
      "unmatched:00b82528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82630"
      ]
    ]
  ],
  "added": [
    [
      "00b825f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82630"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b824e8.md#insn-00b82528) · [`00b8250c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b824e8.md#insn-00b8250c)
- 新版 `00b825f0`（命令位置の公開資料なし） · `00b825d4`（命令位置の公開資料なし）

~~~diff
- 00b82528 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b82528 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b82528 bytes 000200b4
+ 00b825f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b825f0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b825f0 bytes 000200b4
- 00b8250c ["INT_ADD", "register:40f0:8", ["const:b8250c:8", "const:4:8"]]
- 00b8250c ["CALL", null, ["callee:00bdb3c0:8"]]
+ 00b825d4 ["INT_ADD", "register:40f0:8", ["const:b825d4:8", "const:4:8"]]
+ 00b825d4 ["CALL", null, ["callee:00bdb3c0:8"]]
- 00b8250c bytes 81630194
+ 00b825d4 bytes 7b630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9602f26d072568381e6e1500e2856b30"></a>

### [`00b825e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b825e0.md) → [`00b826a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b826a8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5tellpEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

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
      "site": "00b82630"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b826f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8263c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82634",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b82630",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b826fc",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b826f8",
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

- 旧版 [`00b82630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b825e0.md#insn-00b82630) · [`00b8263c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b825e0.md#insn-00b8263c)
- 新版 `00b826f8`（命令位置の公開資料なし）

~~~diff
- 00b82630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82630 ["INT_ADD", "register:40f0:8", ["const:b82630:8", "const:4:8"]]
- 00b82630 ["CALLIND", null, ["register:0:8"]]
- 00b82630 bytes 00013fd6
- 00b8263c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b8263c ["RETURN", null, ["register:0:8"]]
- 00b8263c bytes c0035fd6
+ 00b826f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b826f8 ["INT_ADD", "register:40f0:8", ["const:b826f8:8", "const:4:8"]]
+ 00b826f8 ["CALLIND", null, ["register:0:8"]]
+ 00b826f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184b7ac256e322e057a5330cfe147eba"></a>

### [`00b82988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82988.md) → [`00b82a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82a50.md) _ZTv0_n24_NSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b8298c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8298c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82990"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8298c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b82990",
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
      "00b82a54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b82a58",
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

- 旧版 [`00b8298c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82988.md#insn-00b8298c) · [`00b82990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82988.md#insn-00b82990)
- 新版 `00b82a54`（命令位置の公開資料なし）

~~~diff
- 00b8298c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b8298c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b8298c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b8298c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b8298c bytes fd7bbea9
- 00b82990 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b82990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b82990 bytes f30b00f9
+ 00b82a54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b82a54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b82a54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b82a54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b82a54 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e235ce81cc8414eaf6fa63610ee1dba1"></a>

### [`00b82a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82a60.md) → [`00b82b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b82/00b82b28.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEE7copyfmtERKS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be11d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11d0.md) [`00be1210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be1280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1280.md) [`00be12c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b82b70"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b82aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82a60.md#insn-00b82aa8) · [`00b82a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b82/00b82a60.md#insn-00b82a78)
- 新版 `00b82b70`（命令位置の公開資料なし） · `00b82b40`（命令位置の公開資料なし）

~~~diff
- 00b82aa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:88:8"]]
- 00b82aa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b82aa8 bytes 684600f9
+ 00b82b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:88:8"]]
+ 00b82b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b82b70 bytes 684600f9
- 00b82a78 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b82b40 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b82a78 bytes 80020054
+ 00b82b40 bytes 80020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62fb3a27b5d62df16a478a8befdb6ac4"></a>

### [`00b85350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85350.md) → [`00b85418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85418.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE4peekEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 62.50% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8539c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b85464"
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
      "unmatched:00b8539c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85478"
      ]
    ]
  ],
  "added": [
    [
      "00b85464",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85478"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8539c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85350.md#insn-00b8539c) · [`00b85378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85350.md#insn-00b85378)
- 新版 `00b85464`（命令位置の公開資料なし） · `00b85440`（命令位置の公開資料なし）

~~~diff
- 00b8539c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b8539c bytes a0000054
+ 00b85464 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00b85464 bytes a0000054
- 00b85378 ["INT_ADD", "register:40f0:8", ["const:b85378:8", "const:4:8"]]
- 00b85378 ["CALL", null, ["callee:00be13d0:8"]]
+ 00b85440 ["INT_ADD", "register:40f0:8", ["const:b85440:8", "const:4:8"]]
+ 00b85440 ["CALL", null, ["callee:00be13d0:8"]]
- 00b85378 bytes ea6f0194
+ 00b85440 bytes e46f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afa35e22617189c1fe001980e71a99bf"></a>

### [`00b85afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85afc.md) → [`00b85bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85bc4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00be1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00be13d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be13d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b85c40"
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
      "unmatched:00b85b78",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b85c40",
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

- 旧版 [`00b85b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85afc.md#insn-00b85b78) · [`00b85b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85afc.md#insn-00b85b38)
- 新版 `00b85c40`（命令位置の公開資料なし） · `00b85c00`（命令位置の公開資料なし）

~~~diff
- 00b85b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b85b78 ["INT_ADD", "register:40f0:8", ["const:b85b78:8", "const:4:8"]]
- 00b85b78 ["CALLIND", null, ["register:0:8"]]
- 00b85b78 bytes 00013fd6
+ 00b85c40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b85c40 ["INT_ADD", "register:40f0:8", ["const:b85c40:8", "const:4:8"]]
+ 00b85c40 ["CALLIND", null, ["register:0:8"]]
+ 00b85c40 bytes 00013fd6
- 00b85b38 ["INT_ADD", "register:40f0:8", ["const:b85b38:8", "const:4:8"]]
- 00b85b38 ["CALL", null, ["callee:00bdb400:8"]]
+ 00b85c00 ["INT_ADD", "register:40f0:8", ["const:b85c00:8", "const:4:8"]]
+ 00b85c00 ["CALL", null, ["callee:00bdb400:8"]]
- 00b85b38 bytes 06560194
+ 00b85c00 bytes 00560194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5548c53e510175f627edb971b8365558"></a>

### [`00b85e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e0c.md) → [`00b85ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85ed4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be00e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be00e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

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
      "site": "00b85e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b85e10",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b85e14",
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
      "00b85ed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b85edc",
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

- 旧版 [`00b85e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e0c.md#insn-00b85e10) · [`00b85e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e0c.md#insn-00b85e14)
- 新版 `00b85ed8`（命令位置の公開資料なし）

~~~diff
- 00b85e10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b85e10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b85e10 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b85e10 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b85e10 bytes fd7bbea9
- 00b85e14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b85e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b85e14 bytes f30b00f9
+ 00b85ed8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b85ed8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b85ed8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b85ed8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b85ed8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-259d0a67104c66ffb091cdc031cd5c1a"></a>

### [`00b85e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e74.md) → [`00b85f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b85/00b85f3c.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

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
      "site": "00b85eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b85ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b85f7c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b85eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e74.md#insn-00b85eb4) · [`00b85ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b85/00b85e74.md#insn-00b85ebc)
- 新版 `00b85f7c`（命令位置の公開資料なし）

~~~diff
- 00b85eb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:88:8"]]
- 00b85eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b85eb4 bytes 684600f9
- 00b85ebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:88:8"]]
- 00b85ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b85ebc bytes 894600f9
+ 00b85f7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:88:8"]]
+ 00b85f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b85f7c bytes 684600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882a7288580ba1bf737412f84dfe056d"></a>

### [`00b88290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88290.md) → [`00b88358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88358.md) _ZNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEOS5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be1220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1220.md) [`00be1370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1370.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be12d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be12d0.md) [`00be1420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1420.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "site": "00b88318"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b883e0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b88318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88290.md#insn-00b88318) · [`00b882d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88290.md#insn-00b882d4)
- 新版 `00b883e0`（命令位置の公開資料なし） · `00b8839c`（命令位置の公開資料なし）

~~~diff
- 00b88318 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b88318 ["RETURN", null, ["register:0:8"]]
- 00b88318 bytes c0035fd6
+ 00b883e0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b883e0 ["RETURN", null, ["register:0:8"]]
+ 00b883e0 bytes c0035fd6
- 00b882d4 ["INT_ADD", "register:40f0:8", ["const:b882d4:8", "const:4:8"]]
- 00b882d4 ["CALL", null, ["callee:00be12d0:8"]]
+ 00b8839c ["INT_ADD", "register:40f0:8", ["const:b8839c:8", "const:4:8"]]
+ 00b8839c ["CALL", null, ["callee:00be12d0:8"]]
- 00b882d4 bytes d3630194
+ 00b8839c bytes cd630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d44fd974b29a2a41a00878b985c6fdb"></a>

### [`00b884e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b884e8.md) → [`00b885b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b885b0.md) _ZNSt6__ndk114basic_ifstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b88e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88e50.md) [`00bdb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb350.md) [`00bdd0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0b0.md) [`00bdd110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd110.md) [`00bdd140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd140.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b88f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88f18.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1c0.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 57.14% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88510"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b885d8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b88510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b884e8.md#insn-00b88510) · [`00b88514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b884e8.md#insn-00b88514)
- 新版 `00b885d8`（命令位置の公開資料なし） · `00b885dc`（命令位置の公開資料なし）

~~~diff
- 00b88510 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b88510 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b88510 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b88510 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b88510 bytes 3615819a
+ 00b885d8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b885d8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00b885d8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b885d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
+ 00b885d8 bytes 3615819a
- 00b88514 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b88514 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b885dc ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b885dc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b88514 bytes 6a0100b4
+ 00b885dc bytes 6a0100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfe3aaf3aedae31f01ff7110fe7eb912"></a>

### [`00b88b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88b28.md) → [`00b88bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88bf0.md) FUN_00b88bf0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdbfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbfd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdc080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc080.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

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
      "site": "00b88b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b88b30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b88b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b88b30",
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
      "00b88bf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b88bf8",
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

- 旧版 [`00b88b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88b28.md#insn-00b88b2c) · [`00b88b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88b28.md#insn-00b88b30)
- 新版 `00b88bf4`（命令位置の公開資料なし）

~~~diff
- 00b88b2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b88b2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b88b2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b88b2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b88b2c bytes fd7bbea9
- 00b88b30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b88b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b88b30 bytes f30b00f9
+ 00b88bf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00b88bf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00b88bf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b88bf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b88bf4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b76d31b6dc02c189e3ead77182d9ba03"></a>

### [`00b89fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89fec.md) → [`00b8a0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0b4.md) FUN_00b8a0b4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be13a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13a0.md) [`00be13c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be1450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1450.md) [`00be1470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1470.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 85.71% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a08c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b8a154"
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
      "unmatched:00b8a08c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b8a154",
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

- 旧版 [`00b8a08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89fec.md#insn-00b8a08c) · [`00b8a02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89fec.md#insn-00b8a02c)
- 新版 `00b8a154`（命令位置の公開資料なし） · `00b8a0f4`（命令位置の公開資料なし）

~~~diff
- 00b8a08c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8a08c ["INT_ADD", "register:40f0:8", ["const:b8a08c:8", "const:4:8"]]
- 00b8a08c ["CALLIND", null, ["register:0:8"]]
- 00b8a08c bytes 00013fd6
+ 00b8a154 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b8a154 ["INT_ADD", "register:40f0:8", ["const:b8a154:8", "const:4:8"]]
+ 00b8a154 ["CALLIND", null, ["register:0:8"]]
+ 00b8a154 bytes 00013fd6
- 00b8a02c ["INT_ADD", "register:40f0:8", ["const:b8a02c:8", "const:4:8"]]
- 00b8a02c ["CALL", null, ["callee:00be1470:8"]]
+ 00b8a0f4 ["INT_ADD", "register:40f0:8", ["const:b8a0f4:8", "const:4:8"]]
+ 00b8a0f4 ["CALL", null, ["callee:00be1470:8"]]
- 00b8a02c bytes e55c0194
+ 00b8a0f4 bytes df5c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23229da1605ac0d3a71c9b3da69e9e83"></a>

### [`00b8a114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a114.md) → [`00b8a1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a1dc.md) FUN_00b8a1dc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b89fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89fd4.md) [`00b89fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b89/00b89fe0.md) · 呼出先 4件 [`00be13a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13a0.md) [`00be13b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13b0.md) [`00be13c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13c0.md) [`00be13d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be13d0.md)
- 新版 呼出元 2件 [`00b8a09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a09c.md) [`00b8a0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a0a8.md) · 呼出先 4件 [`00be1450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1450.md) [`00be1460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1460.md) [`00be1470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1470.md) [`00be1480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1480.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 86.67% / 新版 84.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a1f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8a128",
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
      "00b8a1f0",
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

- 旧版 [`00b8a128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a114.md#insn-00b8a128) · [`00b8a1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a114.md#insn-00b8a1f4)
- 新版 `00b8a1f0`（命令位置の公開資料なし）

~~~diff
- 00b8a128 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8a128 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8a128 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b8a128 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8a128 bytes f44f05a9
+ 00b8a1f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b8a1f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b8a1f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
+ 00b8a1f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b8a1f0 bytes f44f05a9
- 00b8a1f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b8a1f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 00b8a1f4 bytes 180100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a25f32eb9325e9f12387fc98bb56dfd0"></a>

### [`00b8a7ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a7ac.md) → [`00b8a874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a874.md) _ZNKSt6__ndk17collateIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 50.00% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8a7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b8a89c"
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
      "unmatched:00b8a7d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8a8c4"
      ]
    ]
  ],
  "added": [
    [
      "00b8a89c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8a8c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8a7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a7ac.md#insn-00b8a7d4) · [`00b8a7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a7ac.md#insn-00b8a7b4)
- 新版 `00b8a89c`（命令位置の公開資料なし） · `00b8a87c`（命令位置の公開資料なし）

~~~diff
- 00b8a7d4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b8a7d4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b8a7d4 bytes 43010054
+ 00b8a89c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b8a89c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b8a89c bytes 43010054
- 00b8a7b4 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00b8a87c ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b8a7b4 bytes a0010054
+ 00b8a87c bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02d7051b361a7218ffef3a5f6ebfff33"></a>

### [`00b8ab9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md) → [`00b8ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8ac64.md) FUN_00b8ac64

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00b8a910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a910.md) [`00b964fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b964fc.md) [`00b96654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96654.md) [`00b96710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96710.md) [`00b96860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b96/00b96860.md) · 呼出先 3件 [`00bdb710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb710.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md) [`00be0e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e80.md)
- 新版 呼出元 7件 [`00b8a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md) [`00b965c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b965c4.md) [`00b9671c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b9671c.md) [`00b967d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b967d8.md) [`00b96928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b96/00b96928.md) · 呼出先 3件 [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md) [`00be0f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.49% / 新版 94.49%

CFGの説明率　旧版 85.61% / 新版 93.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8abb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8abb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8abb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8abb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8abb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8abb8",
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
      "00b8ac78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b8ac7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b8ac80",
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

- 旧版 [`00b8abb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md#insn-00b8abb0) · [`00b8abb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md#insn-00b8abb4) · [`00b8abb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8ab9c.md#insn-00b8abb8)

~~~diff
- 00b8abb0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b8abb0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b8abb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b8abb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8abb0 bytes f85f0da9
- 00b8abb4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b8abb4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8abb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b8abb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8abb4 bytes f6570ea9
- 00b8abb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8abb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8abb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b8abb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8abb8 bytes f44f0fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc64e54d69b2a9ff81d5ab4ae0d4ca83"></a>

### [`00b8b44c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b44c.md) → [`00b8b514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md) FUN_00b8b514

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8b444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b444.md) · 呼出先 6件 [`00bb9318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9318.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1420.md) [`00be1430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1430.md)
- 新版 呼出元 1件 [`00b8b50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b50c.md) · 呼出先 6件 [`00bb93e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.64% / 新版 89.64%

CFGの説明率　旧版 62.11% / 新版 61.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b53c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b544"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8b550"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8b5f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8b54c"
      ]
    ],
    [
      "unmatched:00b8b53c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b630"
      ]
    ],
    [
      "unmatched:00b8b544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b61c"
      ]
    ]
  ],
  "added": [
    [
      "00b8b5f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b614"
      ]
    ],
    [
      "00b8b604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b630"
      ]
    ],
    [
      "00b8b60c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b61c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8b53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b44c.md#insn-00b8b53c) · [`00b8b544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b44c.md#insn-00b8b544) · [`00b8b550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b44c.md#insn-00b8b550)

~~~diff
- 00b8b53c ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00b8b53c bytes 60010054
- 00b8b544 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8b544 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b8b544 bytes 950000b5
- 00b8b550 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8b550 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b8b550 bytes d50100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f909f5f9074efc263162b743e19e3254"></a>

### [`00b8c53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c53c.md) → [`00b8c604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md) FUN_00b8c604

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8c534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c534.md) · 呼出先 6件 [`00bb9834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9834.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1420.md) [`00be1430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1430.md)
- 新版 呼出元 1件 [`00b8c5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c5fc.md) · 呼出先 6件 [`00bb98fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14d0.md) [`00be14e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.06% / 新版 86.06%

CFGの説明率　旧版 57.73% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8c580"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8c558",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8c580",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00b8c6e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8c63c"
      ]
    ]
  ],
  "added": [
    [
      "00b8c620",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b8c648",
      "WRITE",
      [
        "storage",
        "Stack[-0x180]",
        null,
        null
      ]
    ],
    [
      "00b8c6e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8c704"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8c558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c53c.md#insn-00b8c558) · [`00b8c580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c53c.md#insn-00b8c580) · [`00b8c59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c53c.md#insn-00b8c59c)
- 新版 `00b8c664`（命令位置の公開資料なし）

~~~diff
- 00b8c558 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8c558 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b8c558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b8c558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8c558 bytes f44f18a9
- 00b8c580 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b8c580 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4028:8"]]
- 00b8c580 bytes e50b00f9
- 00b8c59c ["BRANCH", null, ["local:b7:8"]]
+ 00b8c664 ["BRANCH", null, ["local:b9:8"]]
- 00b8c59c bytes 06000014
+ 00b8c664 bytes 06000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b2ea2fdbeb7a316d90e5b15da03f883"></a>

### [`00b8cd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8cd90.md) → [`00b8ce58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md) FUN_00b8ce58

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8cd88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8cd88.md) · 呼出先 6件 [`00bb9a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9a94.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeec0.md) [`00be1440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1440.md) [`00be1450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1450.md)
- 新版 呼出元 1件 [`00b8ce50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce50.md) · 呼出先 6件 [`00bb9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef70.md) [`00be14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be14f0.md) [`00be1500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1500.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 91.74% / 新版 91.74%

CFGの説明率　旧版 66.28% / 新版 65.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ce50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ce58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8ce64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b8cf0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b8ce60"
      ]
    ],
    [
      "unmatched:00b8ce50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8cf44"
      ]
    ],
    [
      "unmatched:00b8ce58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8cf30"
      ]
    ]
  ],
  "added": [
    [
      "00b8cf0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8cf28"
      ]
    ],
    [
      "00b8cf18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8cf44"
      ]
    ],
    [
      "00b8cf20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8cf30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8ce50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8cd90.md#insn-00b8ce50) · [`00b8ce58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8cd90.md#insn-00b8ce58) · [`00b8ce64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8cd90.md#insn-00b8ce64)

~~~diff
- 00b8ce50 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b8ce50 bytes 60010054
- 00b8ce58 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8ce58 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b8ce58 bytes 950000b5
- 00b8ce64 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b8ce64 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b8ce64 bytes d50100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-768193fd5ffb78a795c9c2eee3754881"></a>

### [`00b90f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90f54.md) → [`00b9101c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b9101c.md) _ZNSt6__ndk19__num_getIwE17__stage2_int_loopEwiPcRS2_RjwRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_Pw

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be14b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be14b0.md) · 呼出先 1件 [`00bdb500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb500.md)
- 新版 呼出元 1件 [`00be1560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1560.md) · 呼出先 1件 [`00bdb5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb5b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.88% / 新版 82.88%

CFGの説明率　旧版 42.22% / 新版 45.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9109c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b910a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b910f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b91028",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b91044"
      ]
    ],
    [
      "unmatched:00b9108c",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b91094",
      "DATA",
      [
        "storage",
        "002fb026",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b910f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b91044"
      ]
    ],
    [
      "00b91154",
      "READ",
      [
        "storage",
        "00c1bd40",
        null,
        "pointer"
      ]
    ],
    [
      "00b9115c",
      "DATA",
      [
        "storage",
        "002fb026",
        "_ZNSt6__ndk114__num_get_base5__srcE",
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b90fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90f54.md#insn-00b90fd8) · [`00b91004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90f54.md#insn-00b91004) · [`00b91028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90f54.md#insn-00b91028)
- 新版 `00b910a0`（命令位置の公開資料なし）

~~~diff
- 00b90fd8 ["BRANCH", null, ["local:b12:8"]]
+ 00b910a0 ["BRANCH", null, ["local:b13:8"]]
- 00b90fd8 bytes 16000014
+ 00b910a0 bytes 16000014
- 00b91004 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b91004 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b91004 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b91004 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b91004 bytes 0803809a
- 00b91028 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b91028 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00b91028 bytes a1faff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8001095994c24f05e818191d35abbba9"></a>

### [`00b912a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b91/00b912a8.md) → [`00b91370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b91370.md) _ZNSt6__ndk19__num_getIcE19__stage2_float_loopEcRbRcPcRS4_ccRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1460.md) · 呼出先 1件 [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md)
- 新版 呼出元 1件 [`00be1510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1510.md) · 呼出先 1件 [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.82% / 新版 91.82%

CFGの説明率　旧版 93.33% / 新版 95.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b912ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b912ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b912b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b912ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b912b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b912b4",
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
      "00b91374",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b91378",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b9137c",
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

- 旧版 [`00b912ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b91/00b912a8.md#insn-00b912ac) · [`00b912b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b91/00b912a8.md#insn-00b912b0) · [`00b912b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b91/00b912a8.md#insn-00b912b4)

~~~diff
- 00b912ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b912ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b912ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b912ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b912ac bytes fd7bbaa9
- 00b912b0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b912b0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b912b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b912b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b912b0 bytes fc6f01a9
- 00b912b4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b912b4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b912b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b912b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b912b4 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1a7d3355d9c24e3152d3ce5bf54894"></a>

### [`00ba7e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e98.md) → [`00ba7f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7f60.md) _ZNSt6__ndk16localeD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md) · 呼出先 1件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) · 呼出先 1件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba7f80"
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
      "unmatched:00ba7eb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7f94"
      ]
    ]
  ],
  "added": [
    [
      "00ba7f80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7f94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e98.md#insn-00ba7eb8) · [`00ba7eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7e98.md#insn-00ba7eb0)
- 新版 `00ba7f80`（命令位置の公開資料なし）

~~~diff
- 00ba7eb8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba7eb8 bytes a0000054
+ 00ba7f80 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00ba7f80 bytes a0000054
- 00ba7eb0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00ba7eb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba7eb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba7eb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba7eb0 bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3174df0b3cebca6924759b0d6348a63"></a>

### [`00ba7ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7ef8.md) → [`00ba7fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7fc0.md) _ZNSt6__ndk16localeaSERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be11e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be11e0.md) · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md) · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 10.00% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba7fec"
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
      "unmatched:00ba7f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7ffc"
      ]
    ],
    [
      "unmatched:00ba7f3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8028"
      ]
    ]
  ],
  "added": [
    [
      "00ba7fec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7ffc"
      ]
    ],
    [
      "00ba8004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8028"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7ef8.md#insn-00ba7f24) · [`00ba7f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7ef8.md#insn-00ba7f3c) · [`00ba7f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7ef8.md#insn-00ba7f7c)

~~~diff
- 00ba7f24 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba7f24 bytes 80000054
- 00ba7f3c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00ba7f3c bytes 20010054
- 00ba7f7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba7f7c ["RETURN", null, ["register:0:8"]]
- 00ba7f7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfd61a41033dd20d5407bcafa23e1eed"></a>

### [`00ba8364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8364.md) → [`00ba842c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba842c.md) _ZNKSt6__ndk16locale4nameEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8a0.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00bdd950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd950.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba8448"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8364.md#insn-00ba8380) · [`00ba8370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8364.md#insn-00ba8370)
- 新版 `00ba8448`（命令位置の公開資料なし） · `00ba8438`（命令位置の公開資料なし）

~~~diff
- 00ba8380 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba8380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ba8380 bytes 0001803d
+ 00ba8448 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00ba8448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00ba8448 bytes 0001803d
- 00ba8370 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00ba8370 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba8370 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba8370 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00ba8438 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00ba8438 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ba8438 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ba8438 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ba8370 bytes ca000037
+ 00ba8438 bytes ca000037
~~~


<a id="compare-1987a75102b87ac69d6aa774cb9ed1cd"></a>

### [`00ba86c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba86c4.md) → [`00ba878c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba878c.md) _ZNSt6__ndk16locale2id5__getEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)

変更の種類 call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba86e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba87b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba87c0",
      "incomplete_value": false,
      "site": "00ba87d4",
      "value": [
        "leaf",
        "const:bb9104:8"
      ]
    },
    "old": {
      "definition_site": "00ba86f8",
      "incomplete_value": false,
      "site": "00ba870c",
      "value": [
        "leaf",
        "const:bb903c:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba86e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba87d8"
      ]
    ],
    [
      "00ba87c0",
      "PARAM",
      [
        "storage",
        "00bb903c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba87b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba87d8"
      ]
    ],
    [
      "00ba87c0",
      "PARAM",
      [
        "storage",
        "00bb9104",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba86e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba86c4.md#insn-00ba86e8) · [`00ba870c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba86c4.md#insn-00ba870c)
- 新版 `00ba87d4`（命令位置の公開資料なし） · `00ba87b0`（命令位置の公開資料なし）

~~~diff
- 00ba86e8 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba86e8 bytes 40010054
- 00ba870c ["INT_ADD", "register:40f0:8", ["const:ba870c:8", "const:4:8"]]
- 00ba870c ["CALL", null, ["callee:00be0e90:8"]]
+ 00ba87d4 ["INT_ADD", "register:40f0:8", ["const:ba87d4:8", "const:4:8"]]
+ 00ba87d4 ["CALL", null, ["callee:00be0e90:8"]]
- 00ba870c bytes b5e10094
+ 00ba87d4 bytes afe10094
+ 00ba87b0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00ba87b0 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cea5d0906d6d1a46ea219550c5eec99b"></a>

### [`00ba8d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8d28.md) → [`00ba8df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8df0.md) _ZNKSt6__ndk114collate_bynameIcE12do_transformEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 37.14% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8d34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba8d30",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8d38",
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
      "00ba8df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ba8dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba8e00",
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

- 旧版 [`00ba8d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8d28.md#insn-00ba8d30) · [`00ba8d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8d28.md#insn-00ba8d34) · [`00ba8d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8d28.md#insn-00ba8d38)

~~~diff
- 00ba8d30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba8d30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba8d30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba8d30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8d30 bytes fd7b02a9
- 00ba8d34 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba8d34 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba8d34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ba8d34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8d34 bytes f85f03a9
- 00ba8d38 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba8d38 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba8d38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ba8d38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8d38 bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80e08c4e124317d9bba1012b22c3ab65"></a>

### [`00ba957c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba957c.md) → [`00ba9644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9644.md) _ZNSt6__ndk15ctypeIwED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be18a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1950.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

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
      "site": "00ba9580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9584"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba9580",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba9584",
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
      "00ba9648",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ba964c",
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

- 旧版 [`00ba9580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba957c.md#insn-00ba9580) · [`00ba9584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba957c.md#insn-00ba9584)
- 新版 `00ba9648`（命令位置の公開資料なし）

~~~diff
- 00ba9580 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba9580 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba9580 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ba9580 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba9580 bytes fd7bbea9
- 00ba9584 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ba9584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ba9584 bytes f30b00f9
+ 00ba9648 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00ba9648 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00ba9648 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00ba9648 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00ba9648 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3231ed4f163841f0e0d11afa74824e42"></a>

### [`00ba9630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9630.md) → [`00ba96f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba96f8.md) _ZNKSt6__ndk15ctypeIwE10do_scan_isEmPKwS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 50.00% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9654"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba971c"
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
      "unmatched:00ba9654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba973c"
      ]
    ]
  ],
  "added": [
    [
      "00ba971c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba973c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9630.md#insn-00ba9654) · [`00ba963c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba9/00ba9630.md#insn-00ba963c)
- 新版 `00ba971c`（命令位置の公開資料なし） · `00ba9704`（命令位置の公開資料なし）

~~~diff
- 00ba9654 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00ba9654 bytes 00010054
+ 00ba971c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00ba971c bytes 00010054
- 00ba963c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
+ 00ba9704 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00ba963c bytes a0010054
+ 00ba9704 bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb6df1b56e6738f2910a2e365ede6a17"></a>

### [`00bb3af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3af4.md) → [`00bb3bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3bbc.md) _ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be1c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c10.md) · 呼出先 4件 [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be1570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1570.md) [`00be1bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1bf0.md)
- 新版 呼出元 1件 [`00be1cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1cc0.md) · 呼出先 4件 [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be1620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1620.md) [`00be1ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ca0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.57% / 新版 95.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb3c18",
      "PARAM",
      [
        "storage",
        "002a1fe8",
        null,
        null
      ]
    ],
    [
      "00bb3c40",
      "PARAM",
      [
        "storage",
        "0029c22c",
        null,
        null
      ]
    ],
    [
      "00bb3c8c",
      "PARAM",
      [
        "storage",
        "0029f1dc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb3c18",
      "PARAM",
      [
        "storage",
        "002a2075",
        null,
        null
      ]
    ],
    [
      "00bb3c40",
      "PARAM",
      [
        "storage",
        "0029c2b9",
        null,
        null
      ]
    ],
    [
      "00bb3c8c",
      "PARAM",
      [
        "storage",
        "0029f269",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb3b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3af4.md#insn-00bb3b20) · [`00bb3b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3af4.md#insn-00bb3b24) · [`00bb3b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3af4.md#insn-00bb3b2c)
- 新版 `00bb3be8`（命令位置の公開資料なし） · `00bb3bec`（命令位置の公開資料なし）

~~~diff
- 00bb3b20 ["COPY", "register:40a8:8", ["const:2a1000:8"]]
+ 00bb3be8 ["COPY", "register:40a8:8", ["const:2a2000:8"]]
- 00bb3b20 bytes 75b7ffd0
+ 00bb3be8 bytes 75b7fff0
- 00bb3b24 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00bb3b24 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00bb3b24 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00bb3b24 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00bb3bec ["COPY", "tmp:0:8", ["const:75:8"]]
+ 00bb3bec ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bb3bec ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bb3bec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00bb3b24 bytes b5a23f91
+ 00bb3bec bytes b5d60191
- 00bb3b2c ["COPY", "register:40b8:8", ["const:29c000:8"]]
- 00bb3b2c bytes 57b7ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a24e37f3c9c00e242d857477698ecc5"></a>

### [`00bd48c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd48c0.md) → [`00bd4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4988.md) FUN_00bd4988

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd4bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4bf8.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd150.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd4cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4cc0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd200.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd4b54",
      "PARAM",
      [
        "storage",
        "00299a3c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd4b54",
      "PARAM",
      [
        "storage",
        "00299ac9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd48ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd48c0.md#insn-00bd48ec) · [`00bd490c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd48c0.md#insn-00bd490c) · [`00bd4934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd48c0.md#insn-00bd4934)
- 新版 `00bd49b4`（命令位置の公開資料なし） · `00bd49d4`（命令位置の公開資料なし） · `00bd49fc`（命令位置の公開資料なし）

~~~diff
- 00bd48ec ["INT_ADD", "register:40f0:8", ["const:bd48ec:8", "const:4:8"]]
- 00bd48ec ["CALL", null, ["callee:00bd4cc0:8"]]
+ 00bd49b4 ["INT_ADD", "register:40f0:8", ["const:bd49b4:8", "const:4:8"]]
+ 00bd49b4 ["CALL", null, ["callee:00bd4cc0:8"]]
- 00bd48ec bytes c3000094
+ 00bd49b4 bytes c3000094
- 00bd490c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd490c ["INT_ADD", "register:40f0:8", ["const:bd490c:8", "const:4:8"]]
- 00bd490c ["CALLIND", null, ["register:0:8"]]
+ 00bd49d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd49d4 ["INT_ADD", "register:40f0:8", ["const:bd49d4:8", "const:4:8"]]
+ 00bd49d4 ["CALLIND", null, ["register:0:8"]]
- 00bd490c bytes 00013fd6
+ 00bd49d4 bytes 00013fd6
- 00bd4934 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4934 ["INT_ADD", "register:40f0:8", ["const:bd4934:8", "const:4:8"]]
- 00bd4934 ["CALLIND", null, ["register:0:8"]]
+ 00bd49fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd49fc ["INT_ADD", "register:40f0:8", ["const:bd49fc:8", "const:4:8"]]
+ 00bd49fc ["CALLIND", null, ["register:0:8"]]
- 00bd4934 bytes 00013fd6
+ 00bd49fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63ff853212027e70c80d37fff2815454"></a>

### [`00bd6d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md) → [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) FUN_00bd6df0

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00b73730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73730.md) [`00b73768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73768.md) [`00b738e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b738e0.md) [`00b73918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73918.md) [`00b7e178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7e/00b7e178.md) · 呼出先 0件 
- 新版 呼出元 8件 [`00b737f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b737f8.md) [`00b73830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73830.md) [`00b739a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739a8.md) [`00b739e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b739e0.md) [`00b7e240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7e240.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6d38",
      "READ",
      [
        "storage",
        "010a38d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6df8",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md#insn-00bd6d34) · [`00bd6d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md#insn-00bd6d38) · [`00bd6d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md#insn-00bd6d3c)
- 新版 `00bd6dfc`（命令位置の公開資料なし）

~~~diff
- 00bd6d34 ["COPY", "register:4080:8", ["const:10a3000:8"]]
- 00bd6d34 bytes 702600b0
- 00bd6d38 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8d0:8"]]
- 00bd6d38 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6d38 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6d38 bytes 10426339
- 00bd6d3c ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
- 00bd6d3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd6dfc ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
+ 00bd6dfc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd6d3c bytes 70000034
+ 00bd6dfc bytes 70000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-505e49fd0053c83668a1612caef2c62f"></a>

### [`00bd7070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md) → [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) FUN_00bd7130

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) · 呼出先 4件 [`00bd7230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md) [`00bd7454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7454.md) [`00bd7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md) [`00bd74a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74a8.md)
- 新版 呼出元 1件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) · 呼出先 4件 [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) [`00bd7514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7514.md) [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md) [`00bd7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md)

変更の種類 call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd714c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd720c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd70bc",
      "incomplete_value": false,
      "site": "00bd70cc",
      "value": [
        "leaf",
        "const:1a:8"
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
      "unmatched:00bd714c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd71a8"
      ]
    ]
  ],
  "added": [
    [
      "00bd720c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd71a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd70cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md#insn-00bd70cc) · [`00bd7144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md#insn-00bd7144) · [`00bd714c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md#insn-00bd714c)
- 新版 `00bd718c`（命令位置の公開資料なし） · `00bd7204`（命令位置の公開資料なし）

~~~diff
- 00bd70cc ["COPY", "register:0:8", ["register:4098:8"]]
- 00bd70cc ["INT_ADD", "register:40f0:8", ["const:bd70cc:8", "const:4:8"]]
- 00bd70cc ["CALLIND", null, ["register:0:8"]]
+ 00bd718c ["COPY", "register:0:8", ["register:4098:8"]]
+ 00bd718c ["INT_ADD", "register:40f0:8", ["const:bd718c:8", "const:4:8"]]
+ 00bd718c ["CALLIND", null, ["register:0:8"]]
- 00bd70cc bytes 60023fd6
+ 00bd718c bytes 60023fd6
- 00bd7144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7144 ["INT_ADD", "register:40f0:8", ["const:bd7144:8", "const:4:8"]]
- 00bd7144 ["CALLIND", null, ["register:0:8"]]
+ 00bd7204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7204 ["INT_ADD", "register:40f0:8", ["const:bd7204:8", "const:4:8"]]
+ 00bd7204 ["CALLIND", null, ["register:0:8"]]
- 00bd7144 bytes 00013fd6
+ 00bd7204 bytes 00013fd6
- 00bd714c ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bd714c bytes e0fcff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d6f721230ef78e04612a26118330de"></a>

### [`00bd7b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b80.md) → [`00bd7c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7c40.md) FUN_00bd7c40

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd7f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7f40.md) [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd8000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8000.md) [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 36.36% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bd7d04"
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
      "unmatched:00bd7c44",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd7d04",
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

- 旧版 [`00bd7c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b80.md#insn-00bd7c44) · [`00bd7b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b80.md#insn-00bd7b88)
- 新版 `00bd7d04`（命令位置の公開資料なし） · `00bd7c48`（命令位置の公開資料なし）

~~~diff
- 00bd7c44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7c44 ["INT_ADD", "register:40f0:8", ["const:bd7c44:8", "const:4:8"]]
- 00bd7c44 ["CALLIND", null, ["register:0:8"]]
- 00bd7c44 bytes 00013fd6
+ 00bd7d04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd7d04 ["INT_ADD", "register:40f0:8", ["const:bd7d04:8", "const:4:8"]]
+ 00bd7d04 ["CALLIND", null, ["register:0:8"]]
+ 00bd7d04 bytes 00013fd6
- 00bd7b88 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bd7b88 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bd7b88 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bd7b88 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00bd7c48 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00bd7c48 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00bd7c48 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00bd7c48 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bd7b88 bytes 68000036
+ 00bd7c48 bytes 68000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef586139a8791f33c3c340fcd70292ba"></a>

### [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md) → [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) FUN_00bd97fc

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) [`00bd7660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md) [`00bd84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md) [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bd9904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md) · 呼出先 4件 [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 6件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 38.00% / 新版 39.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd98c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd98f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd98fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd98a8",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd98b0",
      "PARAM",
      [
        "storage",
        "002967c8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd98b8",
      "PARAM",
      [
        "storage",
        "00298b6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9968",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd9970",
      "PARAM",
      [
        "storage",
        "00296855",
        null,
        "string"
      ]
    ],
    [
      "00bd9978",
      "PARAM",
      [
        "storage",
        "00298bfa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd98c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md#insn-00bd98c0) · [`00bd98f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md#insn-00bd98f4) · [`00bd98fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md#insn-00bd98fc)

~~~diff
- 00bd98c0 ["INT_ADD", "register:40f0:8", ["const:bd98c0:8", "const:4:8"]]
- 00bd98c0 ["CALL", null, ["callee:00be1f30:8"]]
- 00bd98c0 bytes 70210094
- 00bd98f4 ["INT_ADD", "register:40f0:8", ["const:bd98f4:8", "const:4:8"]]
- 00bd98f4 ["CALL", null, ["callee:00be1f30:8"]]
- 00bd98f4 bytes 63210094
- 00bd98fc ["INT_ADD", "register:40f0:8", ["const:bd98fc:8", "const:4:8"]]
- 00bd98fc ["CALL", null, ["callee:00bdd310:8"]]
- 00bd98fc bytes 590e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea573bb0ecb21d46a597654f2d5ee44"></a>

### [`00bdad9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad9c.md) → [`00bdae54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae54.md) _Znwm

採用 · 移動量 `+0xb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) · 呼出先 6件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdbaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbaf0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdae04"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bdaebc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaddc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdadfc",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdadfc",
      "PARAM",
      [
        "storage",
        "00c167f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00bdae00",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bdaeb4",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaeb4",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bdaeb8",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad9c.md#insn-00bdaddc) · [`00bdae04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad9c.md#insn-00bdae04)
- 新版 `00bdae94`（命令位置の公開資料なし）

~~~diff
- 00bdaddc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdaddc ["RETURN", null, ["register:0:8"]]
- 00bdaddc bytes c0035fd6
- 00bdae04 ["INT_ADD", "register:40f0:8", ["const:bdae04:8", "const:4:8"]]
- 00bdae04 ["CALL", null, ["callee:00bdb070:8"]]
- 00bdae04 bytes 6f000094
+ 00bdae94 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bdae94 ["RETURN", null, ["register:0:8"]]
+ 00bdae94 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a15d39e1a5dd43dcdba34c697d239979"></a>

### [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) → [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) &lt;EXTERNAL&gt;::__cxa_atexit

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 546件 [`00418304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418304.md) [`00418338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md) [`004185a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md) [`00419294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419294.md) [`00419640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419640.md) · 呼出先 1件 [`010a5008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5008.md)
- 新版 呼出元 546件 [`00418304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418304.md) [`00418338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md) [`004185a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) [`00419294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419294.md) [`00419640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md) · 呼出先 1件 [`010a5008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5008.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaee4",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaeec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5008"
      ]
    ]
  ],
  "added": [
    [
      "00bdaf94",
      "READ",
      [
        "storage",
        "00c1c058",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaf9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5008"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md#insn-00bdaee0) · [`00bdaee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md#insn-00bdaee4) · [`00bdaee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md#insn-00bdaee8)

~~~diff
- 00bdaee0 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaee0 bytes 100200b0
- 00bdaee4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fa8:8"]]
- 00bdaee4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaee4 bytes 11d647f9
- 00bdaee8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 00bdaee8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaee8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaee8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaee8 bytes 10a23e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2d2c73610f8b60908895391e753f3ef"></a>

### [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) → [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) __cxa_guard_acquire

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 356件 [`00418338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md) [`004184bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md) [`004185a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md) [`00419640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419640.md) [`004196bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/004196bc.md) · 呼出先 1件 [`00bba5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md)
- 新版 呼出元 356件 [`00418338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md) [`004184bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) [`004185a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) [`00419640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md) [`004196bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004196bc.md) · 呼出先 1件 [`00bba6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf04",
      "READ",
      [
        "storage",
        "00c1bfb8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bba6bc"
      ]
    ]
  ],
  "added": [
    [
      "00bdafb4",
      "READ",
      [
        "storage",
        "00c1c068",
        null,
        "pointer"
      ]
    ],
    [
      "00bdafbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bba6bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md#insn-00bdaf00) · [`00bdaf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md#insn-00bdaf04) · [`00bdaf08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md#insn-00bdaf08)

~~~diff
- 00bdaf00 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf00 bytes 100200b0
- 00bdaf04 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fb8:8"]]
- 00bdaf04 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf04 bytes 11de47f9
- 00bdaf08 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 00bdaf08 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf08 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf08 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf08 bytes 10e23e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-675516032491514cbe8db625abb28280"></a>

### [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md) → [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 31件 [`00428128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428128.md) [`0043bf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bf90.md) [`0043bfdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043b/0043bfdc.md) [`0044e018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044e/0044e018.md) [`00451c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00451/00451c20.md) · 呼出先 1件 [`00b7d194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d194.md)
- 新版 呼出元 31件 [`00428128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428128.md) [`0043bf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf90.md) [`0043bfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bfdc.md) [`0044e018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044e/0044e018.md) [`00451c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/00451c20.md) · 呼出先 1件 [`00b7d25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf14",
      "READ",
      [
        "storage",
        "00c1bfc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d25c"
      ]
    ]
  ],
  "added": [
    [
      "00bdafc4",
      "READ",
      [
        "storage",
        "00c1c070",
        null,
        "pointer"
      ]
    ],
    [
      "00bdafcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d25c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md#insn-00bdaf10) · [`00bdaf14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md#insn-00bdaf14) · [`00bdaf18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf10.md#insn-00bdaf18)

~~~diff
- 00bdaf10 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf10 bytes 100200b0
- 00bdaf14 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fc0:8"]]
- 00bdaf14 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf14 bytes 11e247f9
- 00bdaf18 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 00bdaf18 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf18 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf18 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf18 bytes 10023f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794009e97d144b42f3161c7e2319d85a"></a>

### [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) → [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1437件 [`00418394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b18.md) · 呼出先 1件 [`00b7342c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7342c.md)
- 新版 呼出元 1437件 [`00418394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 1件 [`00b734f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b734f4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf34",
      "READ",
      [
        "storage",
        "00c1bfd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b734f4"
      ]
    ]
  ],
  "added": [
    [
      "00bdafe4",
      "READ",
      [
        "storage",
        "00c1c080",
        null,
        "pointer"
      ]
    ],
    [
      "00bdafec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b734f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md#insn-00bdaf30) · [`00bdaf34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md#insn-00bdaf34) · [`00bdaf38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md#insn-00bdaf38)

~~~diff
- 00bdaf30 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf30 bytes 100200b0
- 00bdaf34 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fd0:8"]]
- 00bdaf34 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf34 bytes 11ea47f9
- 00bdaf38 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00bdaf38 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf38 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf38 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf38 bytes 10423f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-335ad38c4290a9691ef4f04c78c7cec4"></a>

### [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) → [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) _Znwm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3513件 [`004183ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0041ac3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md) · 呼出先 1件 [`00bdad9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad9c.md)
- 新版 呼出元 3513件 [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) · 呼出先 1件 [`00bdae54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae54.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf44",
      "READ",
      [
        "storage",
        "00c1bfd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bdae54"
      ]
    ]
  ],
  "added": [
    [
      "00bdaff4",
      "READ",
      [
        "storage",
        "00c1c088",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bdae54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md#insn-00bdaf40) · [`00bdaf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md#insn-00bdaf44) · [`00bdaf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md#insn-00bdaf48)

~~~diff
- 00bdaf40 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf40 bytes 100200b0
- 00bdaf44 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fd8:8"]]
- 00bdaf44 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf44 bytes 11ee47f9
- 00bdaf48 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00bdaf48 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf48 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf48 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf48 bytes 10623f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0aa8597e360f508bbc99528ef985d37"></a>

### [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) → [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) _ZdlPv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7045件 [`004188e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004188e8.md) [`00418a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418a7c.md) [`00418b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b94.md) [`00418f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418f90.md) [`004191f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/004191f8.md) · 呼出先 1件 [`00bd4e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e04.md)
- 新版 呼出元 7041件 [`004188e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004188e8.md) [`00418a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418a7c.md) [`00418b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b94.md) [`00418f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418f90.md) [`004191f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004191f8.md) · 呼出先 1件 [`00bd4ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4ecc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf64",
      "READ",
      [
        "storage",
        "00c1bfe8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4ecc"
      ]
    ]
  ],
  "added": [
    [
      "00bdb014",
      "READ",
      [
        "storage",
        "00c1c098",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb01c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4ecc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md#insn-00bdaf60) · [`00bdaf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md#insn-00bdaf64) · [`00bdaf68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md#insn-00bdaf68)

~~~diff
- 00bdaf60 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf60 bytes 100200b0
- 00bdaf64 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fe8:8"]]
- 00bdaf64 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf64 bytes 11f647f9
- 00bdaf68 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00bdaf68 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf68 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf68 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf68 bytes 10a23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dd0c2240cd1a7de5683b0e858279281"></a>

### [`00bdaf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf70.md) → [`00bdb020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb020.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004184bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md) [`004c222c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c222c.md) [`004ce9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce9e4.md) [`00acb930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb930.md) · 呼出先 1件 [`00b728cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b728cc.md)
- 新版 呼出元 4件 [`004184bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) [`004c222c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c222c.md) [`004ce9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce9e4.md) [`00acb9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md) · 呼出先 1件 [`00b72994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72994.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf74",
      "READ",
      [
        "storage",
        "00c1bff0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b72994"
      ]
    ]
  ],
  "added": [
    [
      "00bdb024",
      "READ",
      [
        "storage",
        "00c1c0a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb02c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b72994"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf70.md#insn-00bdaf70) · [`00bdaf74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf70.md#insn-00bdaf74) · [`00bdaf78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf70.md#insn-00bdaf78)

~~~diff
- 00bdaf70 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf70 bytes 100200b0
- 00bdaf74 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ff0:8"]]
- 00bdaf74 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf74 bytes 11fa47f9
- 00bdaf78 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00bdaf78 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf78 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf78 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf78 bytes 10c23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df7fc314b05b9190d42126a133310a4a"></a>

### [`00bdaf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf80.md) → [`00bdb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb030.md) &lt;EXTERNAL&gt;::glGetIntegerv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`004184bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md) [`0056ea48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056ea48.md) [`0056f0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f0a0.md) [`0056f270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f270.md) [`0056f7f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f7f8.md) · 呼出先 1件 [`010a5018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5018.md)
- 新版 呼出元 9件 [`004184bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) [`0056ea48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056ea48.md) [`0056f0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f0a0.md) [`0056f270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f270.md) [`0056f7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f7f8.md) · 呼出先 1件 [`010a5018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5018.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaf84",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaf8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5018"
      ]
    ]
  ],
  "added": [
    [
      "00bdb034",
      "READ",
      [
        "storage",
        "00c1c0a8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb03c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5018"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf80.md#insn-00bdaf80) · [`00bdaf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf80.md#insn-00bdaf84) · [`00bdaf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf80.md#insn-00bdaf88)

~~~diff
- 00bdaf80 ["COPY", "register:4080:8", ["const:c1b000:8"]]
- 00bdaf80 bytes 100200b0
- 00bdaf84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ff8:8"]]
- 00bdaf84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaf84 bytes 11fe47f9
- 00bdaf88 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00bdaf88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaf88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaf88 bytes 10e23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34bdf636c80abf3bd355215c4772e8c0"></a>

### [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) → [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) __cxa_allocate_exception

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 364件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`004376c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004376c8.md) · 呼出先 1件 [`00bd4efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4efc.md)
- 新版 呼出元 364件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004376c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004376c8.md) · 呼出先 1件 [`00bd4fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fc4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdafa4",
      "READ",
      [
        "storage",
        "00c1c008",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdafac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4fc4"
      ]
    ]
  ],
  "added": [
    [
      "00bdb054",
      "READ",
      [
        "storage",
        "00c1c0b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb05c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4fc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md#insn-00bdafa0) · [`00bdafa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md#insn-00bdafa4) · [`00bdafa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md#insn-00bdafa8)

~~~diff
- 00bdafa0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdafa0 bytes 100200d0
- 00bdafa4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8:8"]]
- 00bdafa4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdafa4 bytes 110640f9
- 00bdafa8 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00bdafa8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdafa8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdafa8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdafa8 bytes 10220091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f654e792d829342bf453abfc128ff8e5"></a>

### [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) → [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) __cxa_throw

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 359件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`004377fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00437/004377fc.md) · 呼出先 1件 [`00bd5128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md)
- 新版 呼出元 359件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377fc.md) · 呼出先 1件 [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdafc4",
      "READ",
      [
        "storage",
        "00c1c018",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdafcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd51f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdb074",
      "READ",
      [
        "storage",
        "00c1c0c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb07c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd51f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md#insn-00bdafc0) · [`00bdafc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md#insn-00bdafc4) · [`00bdafc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md#insn-00bdafc8)

~~~diff
- 00bdafc0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdafc0 bytes 100200d0
- 00bdafc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:18:8"]]
- 00bdafc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdafc4 bytes 110e40f9
- 00bdafc8 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00bdafc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdafc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdafc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdafc8 bytes 10620091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

