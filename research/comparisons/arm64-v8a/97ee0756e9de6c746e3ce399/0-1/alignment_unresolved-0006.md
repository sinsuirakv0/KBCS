# v15.7.2 → v15.7.3 · 命令位置の検査未完了 (6)

[一覧の目次](README.md)

<a id="compare-171d0c01db86bfc10e9d80a4f8446089"></a>

### [`00bdafd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafd0.md) → [`00bdb080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb080.md) __cxa_free_exception

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005054cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00505/005054cc.md) [`005060a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/005060a8.md) · 呼出先 1件 [`00bd4fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4fe8.md)
- 新版 呼出元 2件 [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) [`005060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md) · 呼出先 1件 [`00bd50b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd50b0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdafd4",
      "READ",
      [
        "storage",
        "00c1c020",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdafdc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd50b0"
      ]
    ]
  ],
  "added": [
    [
      "00bdb084",
      "READ",
      [
        "storage",
        "00c1c0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb08c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd50b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdafd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafd0.md#insn-00bdafd0) · [`00bdafd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafd0.md#insn-00bdafd4) · [`00bdafd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafd0.md#insn-00bdafd8)

~~~diff
- 00bdafd0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdafd0 bytes 100200d0
- 00bdafd4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:20:8"]]
- 00bdafd4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdafd4 bytes 111240f9
- 00bdafd8 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00bdafd8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdafd8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdafd8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdafd8 bytes 10820091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f39402182c8917dac7cd2f996764678"></a>

### [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) → [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) &lt;EXTERNAL&gt;::memmove

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 467件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md) [`0041f280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f280.md) · 呼出先 1件 [`010a5028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5028.md)
- 新版 呼出元 467件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`0041f280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f280.md) · 呼出先 1件 [`010a5028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5028.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaff4",
      "READ",
      [
        "storage",
        "00c1c030",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdaffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5028"
      ]
    ]
  ],
  "added": [
    [
      "00bdb0a4",
      "READ",
      [
        "storage",
        "00c1c0e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb0ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5028"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md#insn-00bdaff0) · [`00bdaff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md#insn-00bdaff4) · [`00bdaff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md#insn-00bdaff8)

~~~diff
- 00bdaff0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdaff0 bytes 100200d0
- 00bdaff4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:30:8"]]
- 00bdaff4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdaff4 bytes 111a40f9
- 00bdaff8 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00bdaff8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaff8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdaff8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdaff8 bytes 10c20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a35e9bc7f8543b59949c36ff5c83c04"></a>

### [`00bdb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md) → [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) _ZNSt6__ndk115__thread_structC1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00423fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423fe8.md) [`00450398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450398.md) [`0045c944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045c/0045c944.md) [`00474f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474f1c.md) [`004a832c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a8/004a832c.md) · 呼出先 1件 [`00b7dc38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7dc38.md)
- 新版 呼出元 10件 [`00423fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423fe8.md) [`00450398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450398.md) [`0045c944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c944.md) [`00474f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474f1c.md) [`004a832c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a832c.md) · 呼出先 1件 [`00b7dd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dd00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb1b4",
      "READ",
      [
        "storage",
        "00c1c110",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb1bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7dd00"
      ]
    ]
  ],
  "added": [
    [
      "00bdb264",
      "READ",
      [
        "storage",
        "00c1c1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb26c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7dd00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md#insn-00bdb1b0) · [`00bdb1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md#insn-00bdb1b4) · [`00bdb1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md#insn-00bdb1b8)

~~~diff
- 00bdb1b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb1b0 bytes 100200b0
- 00bdb1b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:110:8"]]
- 00bdb1b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb1b4 bytes 118a40f9
- 00bdb1b8 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00bdb1b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb1b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb1b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb1b8 bytes 10420491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d4c0497129b1f918e591bc2b4f19537"></a>

### [`00bdb220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb220.md) → [`00bdb2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2d0.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00428128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428128.md) [`00450150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450150.md) [`00474da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474da4.md) [`00474f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474f1c.md) [`004a7ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a7/004a7ed0.md) · 呼出先 1件 [`00b7d788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d788.md)
- 新版 呼出元 8件 [`00428128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428128.md) [`00450150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450150.md) [`00474da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474da4.md) [`00474f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474f1c.md) [`004a7ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7ed0.md) · 呼出先 1件 [`00b7d850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d850.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb224",
      "READ",
      [
        "storage",
        "00c1c148",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb22c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d850"
      ]
    ]
  ],
  "added": [
    [
      "00bdb2d4",
      "READ",
      [
        "storage",
        "00c1c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb2dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d850"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb220.md#insn-00bdb220) · [`00bdb224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb220.md#insn-00bdb224) · [`00bdb228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb220.md#insn-00bdb228)

~~~diff
- 00bdb220 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb220 bytes 100200b0
- 00bdb224 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:148:8"]]
- 00bdb224 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb224 bytes 11a640f9
- 00bdb228 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00bdb228 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb228 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb228 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb228 bytes 10220591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-687e34f192bc4954db32a12eafb413ed"></a>

### [`00bdb230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb230.md) → [`00bdb2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2e0.md) _ZNSt6__ndk16threadD2Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`00428128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428128.md) [`00450150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450150.md) [`00450398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450398.md) [`0045c7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045c/0045c7fc.md) [`00474da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474da4.md) · 呼出先 1件 [`00b7d768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d768.md)
- 新版 呼出元 14件 [`00428128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428128.md) [`00450150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450150.md) [`00450398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450398.md) [`0045c7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c7fc.md) [`00474da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474da4.md) · 呼出先 1件 [`00b7d830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d830.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb234",
      "READ",
      [
        "storage",
        "00c1c150",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb23c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d830"
      ]
    ]
  ],
  "added": [
    [
      "00bdb2e4",
      "READ",
      [
        "storage",
        "00c1c200",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb2ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d830"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb230.md#insn-00bdb230) · [`00bdb234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb230.md#insn-00bdb234) · [`00bdb238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb230.md#insn-00bdb238)

~~~diff
- 00bdb230 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb230 bytes 100200b0
- 00bdb234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:150:8"]]
- 00bdb234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb234 bytes 11aa40f9
- 00bdb238 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00bdb238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb238 bytes 10420591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87920dc7277dd7a269e83cbbfb01aabe"></a>

### [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md) → [`00bdb2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2f0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKc

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 82件 [`0042c4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c4b8.md) [`0042c564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042c/0042c564.md) [`0044b8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b9cc.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) · 呼出先 1件 [`00b75014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75014.md)
- 新版 呼出元 82件 [`0042c4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c4b8.md) [`0042c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042c564.md) [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) · 呼出先 1件 [`00b750dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750dc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb244",
      "READ",
      [
        "storage",
        "00c1c158",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb24c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b750dc"
      ]
    ]
  ],
  "added": [
    [
      "00bdb2f4",
      "READ",
      [
        "storage",
        "00c1c208",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb2fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b750dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md#insn-00bdb240) · [`00bdb244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md#insn-00bdb244) · [`00bdb248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb240.md#insn-00bdb248)

~~~diff
- 00bdb240 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb240 bytes 100200b0
- 00bdb244 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:158:8"]]
- 00bdb244 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb244 bytes 11ae40f9
- 00bdb248 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00bdb248 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb248 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb248 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb248 bytes 10620591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f33281a306c16fd9e8a9dbd47fcc8c77"></a>

### [`00bdb2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md) → [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`00489628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00489/00489628.md) [`004e6520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6520.md) [`00501b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00501/00501b08.md) [`0053c990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c990.md) · 呼出先 1件 [`00b38828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b38/00b38828.md)
- 新版 呼出元 6件 [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00489628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md) [`004e6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6520.md) [`00501b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md) [`0053c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md) · 呼出先 1件 [`00b388f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b38/00b388f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb2b4",
      "READ",
      [
        "storage",
        "00c1c190",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb2bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b388f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdb364",
      "READ",
      [
        "storage",
        "00c1c240",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb36c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b388f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md#insn-00bdb2b0) · [`00bdb2b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md#insn-00bdb2b4) · [`00bdb2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md#insn-00bdb2b8)

~~~diff
- 00bdb2b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb2b0 bytes 100200b0
- 00bdb2b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:190:8"]]
- 00bdb2b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb2b4 bytes 11ca40f9
- 00bdb2b8 ["COPY", "tmp:0:8", ["const:190:8"]]
- 00bdb2b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb2b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb2b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb2b8 bytes 10420691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c8cd2b218419af5e6d8fc9bd7074ee7"></a>

### [`00bdb4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4c0.md) → [`00bdb570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb570.md) &lt;EXTERNAL&gt;::atan2f

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0044ab0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ab0c.md) [`00532f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/00532f34.md) · 呼出先 1件 [`010a50a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a50a0.md)
- 新版 呼出元 2件 [`0044ab0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab0c.md) [`00532f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532f34.md) · 呼出先 1件 [`010a50a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a50a0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb4c4",
      "READ",
      [
        "storage",
        "00c1c298",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb4cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a50a0"
      ]
    ]
  ],
  "added": [
    [
      "00bdb574",
      "READ",
      [
        "storage",
        "00c1c348",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb57c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a50a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4c0.md#insn-00bdb4c0) · [`00bdb4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4c0.md#insn-00bdb4c4) · [`00bdb4c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4c0.md#insn-00bdb4c8)

~~~diff
- 00bdb4c0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb4c0 bytes 100200b0
- 00bdb4c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:298:8"]]
- 00bdb4c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb4c4 bytes 114e41f9
- 00bdb4c8 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00bdb4c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb4c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb4c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb4c8 bytes 10620a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253fe0571b01238d700548e731131344"></a>

### [`00bdb4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4d0.md) → [`00bdb580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb580.md) &lt;EXTERNAL&gt;::powf

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0044ab6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ab6c.md) [`00549128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549128.md) · 呼出先 1件 [`010a50a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a50a8.md)
- 新版 呼出元 2件 [`0044ab6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ab6c.md) [`00549128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549128.md) · 呼出先 1件 [`010a50a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a50a8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb4d4",
      "READ",
      [
        "storage",
        "00c1c2a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb4dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a50a8"
      ]
    ]
  ],
  "added": [
    [
      "00bdb584",
      "READ",
      [
        "storage",
        "00c1c350",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb58c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a50a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4d0.md#insn-00bdb4d0) · [`00bdb4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4d0.md#insn-00bdb4d4) · [`00bdb4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb4d0.md#insn-00bdb4d8)

~~~diff
- 00bdb4d0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb4d0 bytes 100200b0
- 00bdb4d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2a0:8"]]
- 00bdb4d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb4d4 bytes 115241f9
- 00bdb4d8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00bdb4d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb4d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb4d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb4d8 bytes 10820a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25fed77d3ebca7a761f3a12c08e8ce1d"></a>

### [`00bdb550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb550.md) → [`00bdb600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb600.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00455270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00455/00455270.md) [`005161d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00516/005161d4.md) [`00564c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564c60.md) · 呼出先 1件 [`00b7ca94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7ca94.md)
- 新版 呼出元 3件 [`00455270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00455/00455270.md) [`005161d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005161d4.md) [`00564c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564c60.md) · 呼出先 1件 [`00b7cb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cb5c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb554",
      "READ",
      [
        "storage",
        "00c1c2e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb55c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7cb5c"
      ]
    ]
  ],
  "added": [
    [
      "00bdb604",
      "READ",
      [
        "storage",
        "00c1c390",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb60c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7cb5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb550.md#insn-00bdb550) · [`00bdb554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb550.md#insn-00bdb554) · [`00bdb558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb550.md#insn-00bdb558)

~~~diff
- 00bdb550 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb550 bytes 100200b0
- 00bdb554 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2e0:8"]]
- 00bdb554 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb554 bytes 117241f9
- 00bdb558 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 00bdb558 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb558 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb558 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb558 bytes 10820b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-998ac6b3e03f72a4e7b9ce0e44e910e1"></a>

### [`00bdb560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md) → [`00bdb610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb610.md) _ZNSt13exception_ptrC1ERKS_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00455270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00455/00455270.md) [`005161d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00516/005161d4.md) [`00564c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00564/00564c60.md) [`00b72a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b72a7c.md) [`00b7c9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c9ac.md) · 呼出先 1件 [`00b7295c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b72/00b7295c.md)
- 新版 呼出元 7件 [`00455270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00455/00455270.md) [`005161d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00516/005161d4.md) [`00564c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00564/00564c60.md) [`00b72b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72b44.md) [`00b7ca74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7ca74.md) · 呼出先 1件 [`00b72a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b72/00b72a24.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb564",
      "READ",
      [
        "storage",
        "00c1c2e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb56c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b72a24"
      ]
    ]
  ],
  "added": [
    [
      "00bdb614",
      "READ",
      [
        "storage",
        "00c1c398",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb61c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b72a24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md#insn-00bdb560) · [`00bdb564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md#insn-00bdb564) · [`00bdb568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb560.md#insn-00bdb568)

~~~diff
- 00bdb560 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb560 bytes 100200b0
- 00bdb564 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2e8:8"]]
- 00bdb564 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb564 bytes 117641f9
- 00bdb568 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00bdb568 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb568 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb568 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb568 bytes 10a20b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fd85d8df68f27d86e0cbd8d056b1baa"></a>

### [`00bdb5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5d0.md) → [`00bdb680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb680.md) _ZNSt6__ndk16futureIvEC2EPNS_17__assoc_sub_stateE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0045c7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045c/0045c7fc.md) [`005962e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/005962e8.md) [`00b7cf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cf10.md) · 呼出先 1件 [`00b7cbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cbdc.md)
- 新版 呼出元 3件 [`0045c7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045c7fc.md) [`005962e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/005962e8.md) [`00b7cfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cfd8.md) · 呼出先 1件 [`00b7cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cca4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb5d4",
      "READ",
      [
        "storage",
        "00c1c320",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb5dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7cca4"
      ]
    ]
  ],
  "added": [
    [
      "00bdb684",
      "READ",
      [
        "storage",
        "00c1c3d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb68c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7cca4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5d0.md#insn-00bdb5d0) · [`00bdb5d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5d0.md#insn-00bdb5d4) · [`00bdb5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5d0.md#insn-00bdb5d8)

~~~diff
- 00bdb5d0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb5d0 bytes 100200b0
- 00bdb5d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:320:8"]]
- 00bdb5d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb5d4 bytes 119241f9
- 00bdb5d8 ["COPY", "tmp:0:8", ["const:320:8"]]
- 00bdb5d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb5d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb5d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb5d8 bytes 10820c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44a478f53264b7b7908c018cb20f82c4"></a>

### [`00bdb5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5e0.md) → [`00bdb690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb690.md) _ZNSt6__ndk117__assoc_sub_state4waitEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0045caa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045c/0045caa4.md) [`00515b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00515/00515b48.md) [`0059675c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00596/0059675c.md) · 呼出先 1件 [`00b7cb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7cb24.md)
- 新版 呼出元 3件 [`0045caa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045c/0045caa4.md) [`00515b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00515/00515b48.md) [`0059675c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00596/0059675c.md) · 呼出先 1件 [`00b7cbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7cbec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb5e4",
      "READ",
      [
        "storage",
        "00c1c328",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb5ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7cbec"
      ]
    ]
  ],
  "added": [
    [
      "00bdb694",
      "READ",
      [
        "storage",
        "00c1c3d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb69c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7cbec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5e0.md#insn-00bdb5e0) · [`00bdb5e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5e0.md#insn-00bdb5e4) · [`00bdb5e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb5e0.md#insn-00bdb5e8)

~~~diff
- 00bdb5e0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb5e0 bytes 100200b0
- 00bdb5e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:328:8"]]
- 00bdb5e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb5e4 bytes 119641f9
- 00bdb5e8 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00bdb5e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb5e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb5e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb5e8 bytes 10a20c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a27bedffab6a4714c45dd063a4a5ca7"></a>

### [`00bdb7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7a0.md) → [`00bdb850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb850.md) _ZN5Botan11DER_Encoder12DER_Sequence12get_contentsEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004826c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004826c4.md) · 呼出先 1件 [`0048f014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048f/0048f014.md)
- 新版 呼出元 1件 [`004826c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md) · 呼出先 1件 [`0048f014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f014.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb7a4",
      "READ",
      [
        "storage",
        "00c1c408",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb7ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048f014"
      ]
    ]
  ],
  "added": [
    [
      "00bdb854",
      "READ",
      [
        "storage",
        "00c1c4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb85c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048f014"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7a0.md#insn-00bdb7a0) · [`00bdb7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7a0.md#insn-00bdb7a4) · [`00bdb7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7a0.md#insn-00bdb7a8)

~~~diff
- 00bdb7a0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb7a0 bytes 100200b0
- 00bdb7a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:408:8"]]
- 00bdb7a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb7a4 bytes 110642f9
- 00bdb7a8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 00bdb7a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb7a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb7a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb7a8 bytes 10221091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6bf6694986b325c6f0ea6fa24c2cd60"></a>

### [`00bdb7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md) → [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md) _ZN5Botan11BER_Decoder8end_consEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 28件 [`004828a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/004828a4.md) [`004830c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/004830c8.md) [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md) [`004c56b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c56b0.md) [`004c5ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c5ac8.md) · 呼出先 1件 [`00482c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00482/00482c08.md)
- 新版 呼出元 28件 [`004828a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004828a4.md) [`004830c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004830c8.md) [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) [`004c56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md) [`004c5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5ac8.md) · 呼出先 1件 [`00482c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482c08.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb7c4",
      "READ",
      [
        "storage",
        "00c1c418",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb7cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00482c08"
      ]
    ]
  ],
  "added": [
    [
      "00bdb874",
      "READ",
      [
        "storage",
        "00c1c4c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb87c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00482c08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md#insn-00bdb7c0) · [`00bdb7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md#insn-00bdb7c4) · [`00bdb7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb7c0.md#insn-00bdb7c8)

~~~diff
- 00bdb7c0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb7c0 bytes 100200b0
- 00bdb7c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:418:8"]]
- 00bdb7c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb7c4 bytes 110e42f9
- 00bdb7c8 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00bdb7c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb7c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb7c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb7c8 bytes 10621091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d1be1533cbb137bb75c86fa9212f4ab"></a>

### [`00bdb810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb810.md) → [`00bdb8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8c0.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00489628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00489/00489628.md) · 呼出先 1件 [`0048322c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/0048322c.md)
- 新版 呼出元 1件 [`00489628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md) · 呼出先 1件 [`0048322c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/0048322c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb814",
      "READ",
      [
        "storage",
        "00c1c440",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb81c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048322c"
      ]
    ]
  ],
  "added": [
    [
      "00bdb8c4",
      "READ",
      [
        "storage",
        "00c1c4f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb8cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048322c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb810.md#insn-00bdb810) · [`00bdb814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb810.md#insn-00bdb814) · [`00bdb818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb810.md#insn-00bdb818)

~~~diff
- 00bdb810 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb810 bytes 100200b0
- 00bdb814 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:440:8"]]
- 00bdb814 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb814 bytes 112242f9
- 00bdb818 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00bdb818 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb818 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb818 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb818 bytes 10021191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad812437eb722bbf8fd658f80f1294ff"></a>

### [`00bdb820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb820.md) → [`00bdb8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8d0.md) _ZN5Botan18BER_Decoding_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00483728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483728.md) [`004839c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/004839c4.md) · 呼出先 1件 [`00483554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483554.md)
- 新版 呼出元 2件 [`00483728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483728.md) [`004839c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004839c4.md) · 呼出先 1件 [`00483554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483554.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb824",
      "READ",
      [
        "storage",
        "00c1c448",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb82c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00483554"
      ]
    ]
  ],
  "added": [
    [
      "00bdb8d4",
      "READ",
      [
        "storage",
        "00c1c4f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb8dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00483554"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb820.md#insn-00bdb820) · [`00bdb824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb820.md#insn-00bdb824) · [`00bdb828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb820.md#insn-00bdb828)

~~~diff
- 00bdb820 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb820 bytes 100200b0
- 00bdb824 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:448:8"]]
- 00bdb824 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb824 bytes 112642f9
- 00bdb828 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00bdb828 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb828 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb828 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb828 bytes 10221191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b87718bd01603a9db04d74651e61e4a8"></a>

### [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md) → [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md) _ZN5Botan9ExceptionC2EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`00483554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483554.md) [`00483664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483664.md) [`0048ae8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048ae8c.md) [`004a6834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a6/004a6834.md) [`004d7760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7760.md) · 呼出先 1件 [`004d7584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d7584.md)
- 新版 呼出元 14件 [`00483554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483554.md) [`00483664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483664.md) [`0048ae8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae8c.md) [`004a6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a6/004a6834.md) [`004d7760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7760.md) · 呼出先 1件 [`004d7584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d7584.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb834",
      "READ",
      [
        "storage",
        "00c1c450",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb83c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d7584"
      ]
    ]
  ],
  "added": [
    [
      "00bdb8e4",
      "READ",
      [
        "storage",
        "00c1c500",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb8ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d7584"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md#insn-00bdb830) · [`00bdb834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md#insn-00bdb834) · [`00bdb838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb830.md#insn-00bdb838)

~~~diff
- 00bdb830 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb830 bytes 100200b0
- 00bdb834 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:450:8"]]
- 00bdb834 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb834 bytes 112a42f9
- 00bdb838 ["COPY", "tmp:0:8", ["const:450:8"]]
- 00bdb838 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb838 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb838 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb838 bytes 10421191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94fe5de7c263bbbea976fbb4d0b2dc5"></a>

### [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md) → [`00bdb8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8f0.md) _ZNSt6__ndk19to_stringEj

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 15件 [`00483728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483728.md) [`004839c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/004839c4.md) [`00484b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484b8c.md) [`00489628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00489/00489628.md) [`0048a0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048a0a0.md) · 呼出先 1件 [`00b7974c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b79/00b7974c.md)
- 新版 呼出元 15件 [`00483728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483728.md) [`004839c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004839c4.md) [`00484b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484b8c.md) [`00489628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md) [`0048a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a0a0.md) · 呼出先 1件 [`00b79814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b79/00b79814.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb844",
      "READ",
      [
        "storage",
        "00c1c458",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb84c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b79814"
      ]
    ]
  ],
  "added": [
    [
      "00bdb8f4",
      "READ",
      [
        "storage",
        "00c1c508",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb8fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b79814"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md#insn-00bdb840) · [`00bdb844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md#insn-00bdb844) · [`00bdb848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb840.md#insn-00bdb848)

~~~diff
- 00bdb840 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb840 bytes 100200b0
- 00bdb844 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:458:8"]]
- 00bdb844 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb844 bytes 112e42f9
- 00bdb848 ["COPY", "tmp:0:8", ["const:458:8"]]
- 00bdb848 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb848 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb848 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb848 bytes 10621191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a043dd3841eebc2b63e5e82f63f1228e"></a>

### [`00bdb850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb850.md) → [`00bdb900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb900.md) _ZN5Botan11DER_Encoder12get_contentsEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00483ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00483/00483ed8.md) [`00490d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00490/00490d78.md) [`004c73c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c7/004c73c4.md) [`004cf634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cf634.md) [`004ee7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004ee7d8.md) · 呼出先 1件 [`0048fa0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048f/0048fa0c.md)
- 新版 呼出元 7件 [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00490d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490d78.md) [`004c73c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c7/004c73c4.md) [`004cf634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cf634.md) [`004ee7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004ee7d8.md) · 呼出先 1件 [`0048fa0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fa0c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb854",
      "READ",
      [
        "storage",
        "00c1c460",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb85c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048fa0c"
      ]
    ]
  ],
  "added": [
    [
      "00bdb904",
      "READ",
      [
        "storage",
        "00c1c510",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb90c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048fa0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb850.md#insn-00bdb850) · [`00bdb854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb850.md#insn-00bdb854) · [`00bdb858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb850.md#insn-00bdb858)

~~~diff
- 00bdb850 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb850 bytes 100200b0
- 00bdb854 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:460:8"]]
- 00bdb854 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb854 bytes 113242f9
- 00bdb858 ["COPY", "tmp:0:8", ["const:460:8"]]
- 00bdb858 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb858 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb858 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb858 bytes 10821191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-335ab20126205600dca75e730009c5b9"></a>

### [`00bdb860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb860.md) → [`00bdb910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb910.md) _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`004840c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/004840c4.md) [`00495378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00495/00495378.md) [`00495668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00495/00495668.md) [`004a32dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a3/004a32dc.md) [`004a34dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a3/004a34dc.md) · 呼出先 1件 [`004d8e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8e54.md)
- 新版 呼出元 10件 [`004840c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md) [`00495378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495378.md) [`00495668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495668.md) [`004a32dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a32dc.md) [`004a34dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a34dc.md) · 呼出先 1件 [`004d8e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8e54.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb864",
      "READ",
      [
        "storage",
        "00c1c468",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb86c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d8e54"
      ]
    ]
  ],
  "added": [
    [
      "00bdb914",
      "READ",
      [
        "storage",
        "00c1c518",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb91c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d8e54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb860.md#insn-00bdb860) · [`00bdb864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb860.md#insn-00bdb864) · [`00bdb868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb860.md#insn-00bdb868)

~~~diff
- 00bdb860 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb860 bytes 100200b0
- 00bdb864 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:468:8"]]
- 00bdb864 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb864 bytes 113642f9
- 00bdb868 ["COPY", "tmp:0:8", ["const:468:8"]]
- 00bdb868 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb868 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb868 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb868 bytes 10a21191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-807b5a47e680bab7bdaae81c1b74b534"></a>

### [`00bdb870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb870.md) → [`00bdb920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb920.md) _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 38件 [`00484260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484260.md) [`00495378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00495/00495378.md) [`0049a0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049a/0049a0a0.md) [`0049c784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049c/0049c784.md) [`004a29fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a2/004a29fc.md) · 呼出先 1件 [`004d751c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d7/004d751c.md)
- 新版 呼出元 38件 [`00484260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484260.md) [`00495378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495378.md) [`0049a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049a/0049a0a0.md) [`0049c784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049c/0049c784.md) [`004a29fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a2/004a29fc.md) · 呼出先 1件 [`004d751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d7/004d751c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb874",
      "READ",
      [
        "storage",
        "00c1c470",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb87c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d751c"
      ]
    ]
  ],
  "added": [
    [
      "00bdb924",
      "READ",
      [
        "storage",
        "00c1c520",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb92c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d751c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb870.md#insn-00bdb870) · [`00bdb874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb870.md#insn-00bdb874) · [`00bdb878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb870.md#insn-00bdb878)

~~~diff
- 00bdb870 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb870 bytes 100200b0
- 00bdb874 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:470:8"]]
- 00bdb874 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb874 bytes 113a42f9
- 00bdb878 ["COPY", "tmp:0:8", ["const:470:8"]]
- 00bdb878 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb878 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb878 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb878 bytes 10c21191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08c5b9fc5e4b3886a1427934d596a44c"></a>

### [`00bdb880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb880.md) → [`00bdb930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb930.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00484570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484570.md) · 呼出先 1件 [`00484754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484754.md)
- 新版 呼出元 1件 [`00484570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484570.md) · 呼出先 1件 [`00484754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb884",
      "READ",
      [
        "storage",
        "00c1c478",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb88c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00484754"
      ]
    ]
  ],
  "added": [
    [
      "00bdb934",
      "READ",
      [
        "storage",
        "00c1c528",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb93c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00484754"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb880.md#insn-00bdb880) · [`00bdb884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb880.md#insn-00bdb884) · [`00bdb888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb880.md#insn-00bdb888)

~~~diff
- 00bdb880 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb880 bytes 100200b0
- 00bdb884 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:478:8"]]
- 00bdb884 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb884 bytes 113e42f9
- 00bdb888 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00bdb888 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb888 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb888 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb888 bytes 10e21191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b957fd9e5c99bdf5cc719aaf868b2904"></a>

### [`00bdb890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb890.md) → [`00bdb940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb940.md) _ZN5Botan11Invalid_OIDC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00484570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484570.md) [`00484754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484754.md) · 呼出先 1件 [`004d8d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d8d44.md)
- 新版 呼出元 2件 [`00484570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484570.md) [`00484754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md) · 呼出先 1件 [`004d8d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d8d44.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb894",
      "READ",
      [
        "storage",
        "00c1c480",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb89c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d8d44"
      ]
    ]
  ],
  "added": [
    [
      "00bdb944",
      "READ",
      [
        "storage",
        "00c1c530",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb94c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d8d44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb890.md#insn-00bdb890) · [`00bdb894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb890.md#insn-00bdb894) · [`00bdb898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb890.md#insn-00bdb898)

~~~diff
- 00bdb890 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb890 bytes 100200b0
- 00bdb894 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:480:8"]]
- 00bdb894 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb894 bytes 114242f9
- 00bdb898 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00bdb898 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb898 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb898 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb898 bytes 10021291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a166ab9782fbc9247e3aeee38057759"></a>

### [`00bdb8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8a0.md) → [`00bdb950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb950.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00484754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484754.md) [`0048ae8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048ae8c.md) [`00491ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00491/00491ef0.md) [`004c3c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c3c00.md) [`004c5e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c5e50.md) · 呼出先 1件 [`0048bf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048bf84.md)
- 新版 呼出元 9件 [`00484754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md) [`0048ae8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae8c.md) [`00491ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/00491ef0.md) [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`004c5e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5e50.md) · 呼出先 1件 [`0048bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bf84.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb8a4",
      "READ",
      [
        "storage",
        "00c1c488",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb8ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048bf84"
      ]
    ]
  ],
  "added": [
    [
      "00bdb954",
      "READ",
      [
        "storage",
        "00c1c538",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb95c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048bf84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8a0.md#insn-00bdb8a0) · [`00bdb8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8a0.md#insn-00bdb8a4) · [`00bdb8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8a0.md#insn-00bdb8a8)

~~~diff
- 00bdb8a0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb8a0 bytes 100200b0
- 00bdb8a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:488:8"]]
- 00bdb8a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb8a4 bytes 114642f9
- 00bdb8a8 ["COPY", "tmp:0:8", ["const:488:8"]]
- 00bdb8a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb8a8 bytes 10221291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4171e962de944008247f03d0abd89931"></a>

### [`00bdb8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8b0.md) → [`00bdb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb960.md) _ZNK5Botan3OID9as_stringEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00485f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00485/00485f54.md) [`004873a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00487/004873a4.md) [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md) [`004c52e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c52e0.md) [`004c585c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c585c.md) · 呼出先 1件 [`00484b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484b8c.md)
- 新版 呼出元 12件 [`00485f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md) [`004873a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00487/004873a4.md) [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) [`004c52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md) [`004c585c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md) · 呼出先 1件 [`00484b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484b8c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb8b4",
      "READ",
      [
        "storage",
        "00c1c490",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb8bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00484b8c"
      ]
    ]
  ],
  "added": [
    [
      "00bdb964",
      "READ",
      [
        "storage",
        "00c1c540",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb96c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00484b8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8b0.md#insn-00bdb8b0) · [`00bdb8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8b0.md#insn-00bdb8b4) · [`00bdb8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8b0.md#insn-00bdb8b8)

~~~diff
- 00bdb8b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb8b0 bytes 100200b0
- 00bdb8b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:490:8"]]
- 00bdb8b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb8b4 bytes 114a42f9
- 00bdb8b8 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00bdb8b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb8b8 bytes 10421291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2929745bfcd72c55b79924a0771567fe"></a>

### [`00bdb8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8c0.md) → [`00bdb970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb970.md) _ZN5Botan3OIDpLEj

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00484e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484e1c.md) · 呼出先 1件 [`00484d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484d30.md)
- 新版 呼出元 1件 [`00484e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484e1c.md) · 呼出先 1件 [`00484d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484d30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb8c4",
      "READ",
      [
        "storage",
        "00c1c498",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb8cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00484d30"
      ]
    ]
  ],
  "added": [
    [
      "00bdb974",
      "READ",
      [
        "storage",
        "00c1c548",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb97c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00484d30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8c0.md#insn-00bdb8c0) · [`00bdb8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8c0.md#insn-00bdb8c4) · [`00bdb8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8c0.md#insn-00bdb8c8)

~~~diff
- 00bdb8c0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb8c0 bytes 100200b0
- 00bdb8c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:498:8"]]
- 00bdb8c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb8c4 bytes 114e42f9
- 00bdb8c8 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00bdb8c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb8c8 bytes 10621291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95d6e4d6e9890ada64f8eefadc22e0dd"></a>

### [`00bdb8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8d0.md) → [`00bdb980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb980.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 23件 [`00484f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484f50.md) [`00485f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00485/00485f54.md) [`0048a574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048a574.md) [`0048a5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048a5bc.md) [`0048b6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048b6ac.md) · 呼出先 1件 [`0048a5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048a5d8.md)
- 新版 呼出元 23件 [`00484f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484f50.md) [`00485f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md) [`0048a574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a574.md) [`0048a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5bc.md) [`0048b6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b6ac.md) · 呼出先 1件 [`0048a5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5d8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb8d4",
      "READ",
      [
        "storage",
        "00c1c4a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb8dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048a5d8"
      ]
    ]
  ],
  "added": [
    [
      "00bdb984",
      "READ",
      [
        "storage",
        "00c1c550",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb98c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048a5d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8d0.md#insn-00bdb8d0) · [`00bdb8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8d0.md#insn-00bdb8d4) · [`00bdb8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8d0.md#insn-00bdb8d8)

~~~diff
- 00bdb8d0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb8d0 bytes 100200b0
- 00bdb8d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:4a0:8"]]
- 00bdb8d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb8d4 bytes 115242f9
- 00bdb8d8 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00bdb8d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb8d8 bytes 10821291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64e9443581b4c1880dfd91382bf692f2"></a>

### [`00bdb8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8e0.md) → [`00bdb990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb990.md) _ZN5Botan14Encoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 15件 [`00484f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00484/00484f50.md) [`0048b804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048b/0048b804.md) [`0048f37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048f/0048f37c.md) [`00494634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00494/00494634.md) [`004984bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00498/004984bc.md) · 呼出先 1件 [`004d89f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d8/004d89f4.md)
- 新版 呼出元 15件 [`00484f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484f50.md) [`0048b804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b804.md) [`0048f37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md) [`00494634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494634.md) [`004984bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004984bc.md) · 呼出先 1件 [`004d89f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d8/004d89f4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb8e4",
      "READ",
      [
        "storage",
        "00c1c4a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb8ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d89f4"
      ]
    ]
  ],
  "added": [
    [
      "00bdb994",
      "READ",
      [
        "storage",
        "00c1c558",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb99c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d89f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8e0.md#insn-00bdb8e0) · [`00bdb8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8e0.md#insn-00bdb8e4) · [`00bdb8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb8e0.md#insn-00bdb8e8)

~~~diff
- 00bdb8e0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb8e0 bytes 100200b0
- 00bdb8e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:4a8:8"]]
- 00bdb8e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb8e4 bytes 115642f9
- 00bdb8e8 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00bdb8e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb8e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb8e8 bytes 10a21291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb3b9542d0010fa75eab422f93ef4a40"></a>

### [`00bdb920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb920.md) → [`00bdb9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9d0.md) _ZNK5Botan14ASN1_Formatter6decodeERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERNS_11BER_DecoderEm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00485e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00485/00485e70.md) [`00485f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00485/00485f54.md) · 呼出先 1件 [`00485f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00485/00485f54.md)
- 新版 呼出元 2件 [`00485e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485e70.md) [`00485f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md) · 呼出先 1件 [`00485f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdb924",
      "READ",
      [
        "storage",
        "00c1c4c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdb92c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00485f54"
      ]
    ]
  ],
  "added": [
    [
      "00bdb9d4",
      "READ",
      [
        "storage",
        "00c1c578",
        null,
        "pointer"
      ]
    ],
    [
      "00bdb9dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00485f54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdb920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb920.md#insn-00bdb920) · [`00bdb924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb920.md#insn-00bdb924) · [`00bdb928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb920.md#insn-00bdb928)

~~~diff
- 00bdb920 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdb920 bytes 100200b0
- 00bdb924 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:4c8:8"]]
- 00bdb924 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdb924 bytes 116642f9
- 00bdb928 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00bdb928 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb928 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdb928 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdb928 bytes 10221391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f5033073de8574e5babc3ea4614591"></a>

### [`00bdbb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb10.md) → [`00bdbbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbc0.md) _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`004c13f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c1/004c13f0.md) [`004c15a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c1/004c15a4.md) [`004e6d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md) [`004e7c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7c0c.md) [`004e7de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e7/004e7de0.md) · 呼出先 1件 [`0048d518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048d/0048d518.md)
- 新版 呼出元 10件 [`004c13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c13f0.md) [`004c15a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c15a4.md) [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) [`004e7c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7c0c.md) [`004e7de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e7/004e7de0.md) · 呼出先 1件 [`0048d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d518.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbb14",
      "READ",
      [
        "storage",
        "00c1c5c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbb1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048d518"
      ]
    ]
  ],
  "added": [
    [
      "00bdbbc4",
      "READ",
      [
        "storage",
        "00c1c670",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbbcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048d518"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb10.md#insn-00bdbb10) · [`00bdbb14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb10.md#insn-00bdbb14) · [`00bdbb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb10.md#insn-00bdbb18)

~~~diff
- 00bdbb10 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbb10 bytes 100200b0
- 00bdbb14 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:5c0:8"]]
- 00bdbb14 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbb14 bytes 11e242f9
- 00bdbb18 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 00bdbb18 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbb18 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbb18 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbb18 bytes 10021791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66034a554436ea6bd50f5be6e72b49f8"></a>

### [`00bdbb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb30.md) → [`00bdbbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbe0.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0048ddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048d/0048ddf0.md) [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md) [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`00513c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00513/00513c60.md) · 呼出先 1件 [`0048e994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048e/0048e994.md)
- 新版 呼出元 4件 [`0048ddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048ddf0.md) [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`00513c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513c60.md) · 呼出先 1件 [`0048e994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e994.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbb34",
      "READ",
      [
        "storage",
        "00c1c5d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbb3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048e994"
      ]
    ]
  ],
  "added": [
    [
      "00bdbbe4",
      "READ",
      [
        "storage",
        "00c1c680",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbbec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048e994"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb30.md#insn-00bdbb30) · [`00bdbb34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb30.md#insn-00bdbb34) · [`00bdbb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb30.md#insn-00bdbb38)

~~~diff
- 00bdbb30 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbb30 bytes 100200b0
- 00bdbb34 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:5d0:8"]]
- 00bdbb34 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbb34 bytes 11ea42f9
- 00bdbb38 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00bdbb38 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbb38 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbb38 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbb38 bytes 10421791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bce745fd78162bc9a7f2372561675b0"></a>

### [`00bdbc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc80.md) → [`00bdbd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd30.md) _ZN5Botan13base64_encodeEPKhm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004c2990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c2990.md) [`004e6ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6ca0.md) [`0055dbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055dbb0.md) · 呼出先 1件 [`00492b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00492/00492b90.md)
- 新版 呼出元 3件 [`004c2990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2990.md) [`004e6ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6ca0.md) [`0055dbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055dbb0.md) · 呼出先 1件 [`00492b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492b90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbc84",
      "READ",
      [
        "storage",
        "00c1c678",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbc8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00492b90"
      ]
    ]
  ],
  "added": [
    [
      "00bdbd34",
      "READ",
      [
        "storage",
        "00c1c728",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbd3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00492b90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc80.md#insn-00bdbc80) · [`00bdbc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc80.md#insn-00bdbc84) · [`00bdbc88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc80.md#insn-00bdbc88)

~~~diff
- 00bdbc80 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbc80 bytes 100200b0
- 00bdbc84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:678:8"]]
- 00bdbc84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbc84 bytes 113e43f9
- 00bdbc88 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00bdbc88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbc88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbc88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbc88 bytes 10e21991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f22cf87cb8d3451b97785c449ceaa2cc"></a>

### [`00bdbcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbcf0.md) → [`00bdbda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbda0.md) _ZN5Botan6BigIntmIERKS0_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00493850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00493/00493850.md) [`004989ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00498/004989ec.md) [`004b77d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b7/004b77d0.md) [`004b8aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b8/004b8aa0.md) [`004b8bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b8/004b8bd8.md) · 呼出先 1件 [`00495e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00495/00495e3c.md)
- 新版 呼出元 9件 [`00493850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md) [`004989ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004989ec.md) [`004b77d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b77d0.md) [`004b8aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8aa0.md) [`004b8bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8bd8.md) · 呼出先 1件 [`00495e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495e3c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbcf4",
      "READ",
      [
        "storage",
        "00c1c6b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbcfc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00495e3c"
      ]
    ]
  ],
  "added": [
    [
      "00bdbda4",
      "READ",
      [
        "storage",
        "00c1c760",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbdac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00495e3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbcf0.md#insn-00bdbcf0) · [`00bdbcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbcf0.md#insn-00bdbcf4) · [`00bdbcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbcf0.md#insn-00bdbcf8)

~~~diff
- 00bdbcf0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbcf0 bytes 100200b0
- 00bdbcf4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:6b0:8"]]
- 00bdbcf4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbcf4 bytes 115a43f9
- 00bdbcf8 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00bdbcf8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbcf8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbcf8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbcf8 bytes 10c21a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0baf68642dc98733b0e66443cb4b2fc"></a>

### [`00bdbe80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe80.md) → [`00bdbf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf30.md) _ZN5Botan16get_sig_paddingsENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0049d8dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049d/0049d8dc.md) · 呼出先 1件 [`004c476c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c4/004c476c.md)
- 新版 呼出元 1件 [`0049d8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049d8dc.md) · 呼出先 1件 [`004c476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c476c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbe84",
      "READ",
      [
        "storage",
        "00c1c778",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbe8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c476c"
      ]
    ]
  ],
  "added": [
    [
      "00bdbf34",
      "READ",
      [
        "storage",
        "00c1c828",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbf3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c476c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbe80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe80.md#insn-00bdbe80) · [`00bdbe84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe80.md#insn-00bdbe84) · [`00bdbe88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe80.md#insn-00bdbe88)

~~~diff
- 00bdbe80 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbe80 bytes 100200b0
- 00bdbe84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:778:8"]]
- 00bdbe84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbe84 bytes 11be43f9
- 00bdbe88 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00bdbe88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbe88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbe88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbe88 bytes 10e21d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9711c9c25c49e55c245657477a028475"></a>

### [`00bdbe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe90.md) → [`00bdbf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf40.md) _ZN5Botan12pkcs_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0049dbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049d/0049dbe4.md) [`0049e24c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049e/0049e24c.md) · 呼出先 1件 [`0049dd0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049d/0049dd0c.md)
- 新版 呼出元 2件 [`0049dbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dbe4.md) [`0049e24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049e/0049e24c.md) · 呼出先 1件 [`0049dd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dd0c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdbe94",
      "READ",
      [
        "storage",
        "00c1c780",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdbe9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049dd0c"
      ]
    ]
  ],
  "added": [
    [
      "00bdbf44",
      "READ",
      [
        "storage",
        "00c1c830",
        null,
        "pointer"
      ]
    ],
    [
      "00bdbf4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049dd0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdbe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe90.md#insn-00bdbe90) · [`00bdbe94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe90.md#insn-00bdbe94) · [`00bdbe98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe90.md#insn-00bdbe98)

~~~diff
- 00bdbe90 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdbe90 bytes 100200b0
- 00bdbe94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:780:8"]]
- 00bdbe94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdbe94 bytes 11c243f9
- 00bdbe98 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00bdbe98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbe98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdbe98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdbe98 bytes 10021e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4115a428a8138b447e7f1f97390f5c04"></a>

### [`00bdc070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc070.md) → [`00bdc120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc120.md) _ZN5Botan20parse_algorithm_nameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004a3d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a3/004a3d70.md) [`004fc6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md) · 呼出先 1件 [`004ae0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ae/004ae0e8.md)
- 新版 呼出元 2件 [`004a3d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a3/004a3d70.md) [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md) · 呼出先 1件 [`004ae0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ae/004ae0e8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc074",
      "READ",
      [
        "storage",
        "00c1c870",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc07c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ae0e8"
      ]
    ]
  ],
  "added": [
    [
      "00bdc124",
      "READ",
      [
        "storage",
        "00c1c920",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc12c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ae0e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc070.md#insn-00bdc070) · [`00bdc074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc070.md#insn-00bdc074) · [`00bdc078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc070.md#insn-00bdc078)

~~~diff
- 00bdc070 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc070 bytes 10020090
- 00bdc074 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:870:8"]]
- 00bdc074 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc074 bytes 113a44f9
- 00bdc078 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00bdc078 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc078 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc078 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc078 bytes 10c22191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33a87041a898083f4e97f8ffe715afb3"></a>

### [`00bdc1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1b0.md) → [`00bdc260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc260.md) _ZN5Botan13Threaded_Fork8set_nextEPPNS_6FilterEm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004a791c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a7/004a791c.md) [`004a7da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a7/004a7da8.md) · 呼出先 1件 [`004a7a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a7/004a7a98.md)
- 新版 呼出元 2件 [`004a791c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a791c.md) [`004a7da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7da8.md) · 呼出先 1件 [`004a7a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7a98.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc1b4",
      "READ",
      [
        "storage",
        "00c1c910",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc1bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a7a98"
      ]
    ]
  ],
  "added": [
    [
      "00bdc264",
      "READ",
      [
        "storage",
        "00c1c9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc26c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004a7a98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1b0.md#insn-00bdc1b0) · [`00bdc1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1b0.md#insn-00bdc1b4) · [`00bdc1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1b0.md#insn-00bdc1b8)

~~~diff
- 00bdc1b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc1b0 bytes 10020090
- 00bdc1b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:910:8"]]
- 00bdc1b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc1b4 bytes 118a44f9
- 00bdc1b8 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00bdc1b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc1b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc1b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc1b8 bytes 10422491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dceccd7cb82804576bb88e28d47927c9"></a>

### [`00bdc1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md) → [`00bdc270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc270.md) _ZNSt6__ndk118condition_variable10notify_oneEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004a7ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a7/004a7ed0.md) [`004a86e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004a8/004a86e8.md) [`00b7d4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d4c0.md) [`00b7d6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d6ec.md) · 呼出先 1件 [`00b7c288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7c/00b7c288.md)
- 新版 呼出元 4件 [`004a7ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a7/004a7ed0.md) [`004a86e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004a8/004a86e8.md) [`00b7d588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d588.md) [`00b7d7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d7b4.md) · 呼出先 1件 [`00b7c350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7c/00b7c350.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc1c4",
      "READ",
      [
        "storage",
        "00c1c918",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc1cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7c350"
      ]
    ]
  ],
  "added": [
    [
      "00bdc274",
      "READ",
      [
        "storage",
        "00c1c9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc27c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7c350"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md#insn-00bdc1c0) · [`00bdc1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md#insn-00bdc1c4) · [`00bdc1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc1c0.md#insn-00bdc1c8)

~~~diff
- 00bdc1c0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc1c0 bytes 10020090
- 00bdc1c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:918:8"]]
- 00bdc1c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc1c4 bytes 118e44f9
- 00bdc1c8 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00bdc1c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc1c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc1c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc1c8 bytes 10622491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1192de6879f37fa35a9bd6876049e02b"></a>

### [`00bdc230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc230.md) → [`00bdc2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc2e0.md) _ZN5Botan4HMAC5clearEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004aa2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004aa/004aa2e4.md) · 呼出先 1件 [`004aa268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004aa/004aa268.md)
- 新版 呼出元 1件 [`004aa2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa2e4.md) · 呼出先 1件 [`004aa268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa268.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc234",
      "READ",
      [
        "storage",
        "00c1c950",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc23c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004aa268"
      ]
    ]
  ],
  "added": [
    [
      "00bdc2e4",
      "READ",
      [
        "storage",
        "00c1ca00",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc2ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004aa268"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc230.md#insn-00bdc230) · [`00bdc234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc230.md#insn-00bdc234) · [`00bdc238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc230.md#insn-00bdc238)

~~~diff
- 00bdc230 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc230 bytes 10020090
- 00bdc234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:950:8"]]
- 00bdc234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc234 bytes 11aa44f9
- 00bdc238 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00bdc238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc238 bytes 10422591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6aa7349a5c372826ff13d9c32123c38"></a>

### [`00bdc250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc250.md) → [`00bdc300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc300.md) _ZN5Botan4HMACC1EPNS_12HashFunctionE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004aa404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004aa/004aa404.md) [`004ab3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ab/004ab3f4.md) · 呼出先 1件 [`004aa464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004aa/004aa464.md)
- 新版 呼出元 2件 [`004aa404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa404.md) [`004ab3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ab3f4.md) · 呼出先 1件 [`004aa464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004aa/004aa464.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc254",
      "READ",
      [
        "storage",
        "00c1c960",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc25c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004aa464"
      ]
    ]
  ],
  "added": [
    [
      "00bdc304",
      "READ",
      [
        "storage",
        "00c1ca10",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc30c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004aa464"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc250.md#insn-00bdc250) · [`00bdc254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc250.md#insn-00bdc254) · [`00bdc258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc250.md#insn-00bdc258)

~~~diff
- 00bdc250 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc250 bytes 10020090
- 00bdc254 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:960:8"]]
- 00bdc254 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc254 bytes 11b244f9
- 00bdc258 ["COPY", "tmp:0:8", ["const:960:8"]]
- 00bdc258 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc258 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc258 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc258 bytes 10822591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5934b855772e8e1d2de08eefafc4377"></a>

### [`00bdc330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc330.md) → [`00bdc3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc3e0.md) _ZN5Botan9PK_SignerD1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`004ab19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ab/004ab19c.md) [`004ecb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edb24.md) [`004edd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004edd80.md) [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) · 呼出先 1件 [`004ccf1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cc/004ccf1c.md)
- 新版 呼出元 7件 [`004ab19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ab/004ab19c.md) [`004ecb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ecb70.md) [`004edb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edb24.md) [`004edd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004edd80.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) · 呼出先 1件 [`004ccf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cc/004ccf1c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc334",
      "READ",
      [
        "storage",
        "00c1c9d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc33c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ccf1c"
      ]
    ]
  ],
  "added": [
    [
      "00bdc3e4",
      "READ",
      [
        "storage",
        "00c1ca80",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc3ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ccf1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc330.md#insn-00bdc330) · [`00bdc334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc330.md#insn-00bdc334) · [`00bdc338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc330.md#insn-00bdc338)

~~~diff
- 00bdc330 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc330 bytes 10020090
- 00bdc334 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
- 00bdc334 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc334 bytes 11ea44f9
- 00bdc338 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00bdc338 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc338 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc338 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc338 bytes 10422791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5783d06c9cab5c25a9ba3d6119b4674f"></a>

### [`00bdc410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc410.md) → [`00bdc4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4c0.md) _ZN5Botan3gcdERKNS_6BigIntES2_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004b6d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b6/004b6d50.md) [`004b8d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b8/004b8d44.md) · 呼出先 1件 [`004b77d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b7/004b77d0.md)
- 新版 呼出元 2件 [`004b6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b6/004b6d50.md) [`004b8d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8d44.md) · 呼出先 1件 [`004b77d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b7/004b77d0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc414",
      "READ",
      [
        "storage",
        "00c1ca40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc41c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b77d0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc4c4",
      "READ",
      [
        "storage",
        "00c1caf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc4cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b77d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc410.md#insn-00bdc410) · [`00bdc414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc410.md#insn-00bdc414) · [`00bdc418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc410.md#insn-00bdc418)

~~~diff
- 00bdc410 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc410 bytes 10020090
- 00bdc414 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a40:8"]]
- 00bdc414 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc414 bytes 112245f9
- 00bdc418 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 00bdc418 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc418 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc418 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc418 bytes 10022991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee01f8f974e890c0b01b26a2bb837372"></a>

### [`00bdc440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc440.md) → [`00bdc4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc4f0.md) _ZN5Botan3lcmERKNS_6BigIntES2_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004c5f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c5f28.md) [`004cfcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cf/004cfcb0.md) [`004d04c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d04c0.md) [`004d0c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d0/004d0c9c.md) [`004d1904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d1/004d1904.md) · 呼出先 1件 [`004b8d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b8/004b8d44.md)
- 新版 呼出元 5件 [`004c5f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c5f28.md) [`004cfcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cf/004cfcb0.md) [`004d04c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d04c0.md) [`004d0c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d0/004d0c9c.md) [`004d1904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d1/004d1904.md) · 呼出先 1件 [`004b8d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8d44.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc444",
      "READ",
      [
        "storage",
        "00c1ca58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc44c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b8d44"
      ]
    ]
  ],
  "added": [
    [
      "00bdc4f4",
      "READ",
      [
        "storage",
        "00c1cb08",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc4fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b8d44"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc440.md#insn-00bdc440) · [`00bdc444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc440.md#insn-00bdc444) · [`00bdc448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc440.md#insn-00bdc448)

~~~diff
- 00bdc440 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc440 bytes 10020090
- 00bdc444 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a58:8"]]
- 00bdc444 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc444 bytes 112e45f9
- 00bdc448 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00bdc448 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc448 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc448 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc448 bytes 10622991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8771412b8254a438e96ba544404042c8"></a>

### [`00bdc450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc450.md) → [`00bdc500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc500.md) _ZN5Botan25almost_montgomery_inverseERNS_6BigIntERKS0_S3_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004b97b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b9/004b97b0.md) · 呼出先 1件 [`004b8e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004b8/004b8e58.md)
- 新版 呼出元 1件 [`004b97b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b9/004b97b0.md) · 呼出先 1件 [`004b8e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b8e58.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc454",
      "READ",
      [
        "storage",
        "00c1ca60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc45c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b8e58"
      ]
    ]
  ],
  "added": [
    [
      "00bdc504",
      "READ",
      [
        "storage",
        "00c1cb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc50c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004b8e58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc450.md#insn-00bdc450) · [`00bdc454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc450.md#insn-00bdc454) · [`00bdc458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc450.md#insn-00bdc458)

~~~diff
- 00bdc450 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc450 bytes 10020090
- 00bdc454 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a60:8"]]
- 00bdc454 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc454 bytes 113245f9
- 00bdc458 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00bdc458 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc458 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc458 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc458 bytes 10822991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5510c25cfd74de91c1586ae4a20be75d"></a>

### [`00bdc490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc490.md) → [`00bdc540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc540.md) _ZN5Botan9power_modERKNS_6BigIntES2_S2_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004be0f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004be/004be0f4.md) · 呼出先 1件 [`004bb1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bb/004bb1c0.md)
- 新版 呼出元 1件 [`004be0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004be/004be0f4.md) · 呼出先 1件 [`004bb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb1c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc494",
      "READ",
      [
        "storage",
        "00c1ca80",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc49c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004bb1c0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc544",
      "READ",
      [
        "storage",
        "00c1cb30",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc54c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004bb1c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc490.md#insn-00bdc490) · [`00bdc494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc490.md#insn-00bdc494) · [`00bdc498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc490.md#insn-00bdc498)

~~~diff
- 00bdc490 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc490 bytes 10020090
- 00bdc494 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a80:8"]]
- 00bdc494 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc494 bytes 114245f9
- 00bdc498 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00bdc498 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc498 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc498 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc498 bytes 10022a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0841aaac422a2ca9e328e886cedb6b3f"></a>

### [`00bdc4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4b0.md) → [`00bdc560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc560.md) _ZNK5Botan9Power_Mod12set_exponentERKNS_6BigIntE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004bb1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bb/004bb1c0.md) [`004bbc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bb/004bbc30.md) · 呼出先 1件 [`004bb59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bb/004bb59c.md)
- 新版 呼出元 2件 [`004bb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb1c0.md) [`004bbc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bbc30.md) · 呼出先 1件 [`004bb59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb59c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc4b4",
      "READ",
      [
        "storage",
        "00c1ca90",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc4bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004bb59c"
      ]
    ]
  ],
  "added": [
    [
      "00bdc564",
      "READ",
      [
        "storage",
        "00c1cb40",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc56c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004bb59c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4b0.md#insn-00bdc4b0) · [`00bdc4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4b0.md#insn-00bdc4b4) · [`00bdc4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4b0.md#insn-00bdc4b8)

~~~diff
- 00bdc4b0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc4b0 bytes 10020090
- 00bdc4b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a90:8"]]
- 00bdc4b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc4b4 bytes 114a45f9
- 00bdc4b8 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 00bdc4b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc4b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc4b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc4b8 bytes 10422a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9c75a45e91511a8e354e9b00cecd3c7"></a>

### [`00bdc4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4e0.md) → [`00bdc590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc590.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004bf57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004bf/004bf57c.md) [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md) [`004c177c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c1/004c177c.md) · 呼出先 1件 [`004c1fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c1/004c1fec.md)
- 新版 呼出元 3件 [`004bf57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bf/004bf57c.md) [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) [`004c177c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c177c.md) · 呼出先 1件 [`004c1fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c1fec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc4e4",
      "READ",
      [
        "storage",
        "00c1caa8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc4ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c1fec"
      ]
    ]
  ],
  "added": [
    [
      "00bdc594",
      "READ",
      [
        "storage",
        "00c1cb58",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc59c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c1fec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4e0.md#insn-00bdc4e0) · [`00bdc4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4e0.md#insn-00bdc4e4) · [`00bdc4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc4e0.md#insn-00bdc4e8)

~~~diff
- 00bdc4e0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc4e0 bytes 10020090
- 00bdc4e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:aa8:8"]]
- 00bdc4e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc4e4 bytes 115645f9
- 00bdc4e8 ["COPY", "tmp:0:8", ["const:aa8:8"]]
- 00bdc4e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc4e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc4e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc4e8 bytes 10a22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9734e99746d5fc3a8166aff6967cfc74"></a>

### [`00bdc500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc500.md) → [`00bdc5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5b0.md) _ZN5Botan13pbes2_decryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) · 呼出先 1件 [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md)
- 新版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) · 呼出先 1件 [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc504",
      "READ",
      [
        "storage",
        "00c1cab8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc50c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c05ec"
      ]
    ]
  ],
  "added": [
    [
      "00bdc5b4",
      "READ",
      [
        "storage",
        "00c1cb68",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc5bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c05ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc500.md#insn-00bdc500) · [`00bdc504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc500.md#insn-00bdc504) · [`00bdc508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc500.md#insn-00bdc508)

~~~diff
- 00bdc500 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc500 bytes 10020090
- 00bdc504 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ab8:8"]]
- 00bdc504 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc504 bytes 115e45f9
- 00bdc508 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00bdc508 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc508 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc508 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc508 bytes 10e22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-177c5f82ff0dbe39667b52c15be50801"></a>

### [`00bdc510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc510.md) → [`00bdc5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5c0.md) _ZN5Botan11BER_Decoder15decode_optionalImEERS0_RT_NS_8ASN1_TagES5_RKS3_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md) [`004e637c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e637c.md) [`004e6d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e6/004e6d3c.md) [`004f03d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md) [`004f52c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f5/004f52c8.md) · 呼出先 1件 [`004c13f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c1/004c13f0.md)
- 新版 呼出元 7件 [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) [`004e637c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e637c.md) [`004e6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e6/004e6d3c.md) [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) [`004f52c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f5/004f52c8.md) · 呼出先 1件 [`004c13f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c13f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc514",
      "READ",
      [
        "storage",
        "00c1cac0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc51c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c13f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc5c4",
      "READ",
      [
        "storage",
        "00c1cb70",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc5cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c13f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc510.md#insn-00bdc510) · [`00bdc514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc510.md#insn-00bdc514) · [`00bdc518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc510.md#insn-00bdc518)

~~~diff
- 00bdc510 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc510 bytes 10020090
- 00bdc514 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ac0:8"]]
- 00bdc514 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc514 bytes 116245f9
- 00bdc518 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 00bdc518 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc518 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc518 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc518 bytes 10022b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fd738988d661da79551c606a3745269"></a>

### [`00bdc520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc520.md) → [`00bdc5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5d0.md) _ZN5Botan11BER_Decoder15decode_optionalINS_19AlgorithmIdentifierEEERS0_RT_NS_8ASN1_TagES6_RKS4_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c05ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c0/004c05ec.md) [`004fcb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fcb38.md) · 呼出先 1件 [`004c15a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c1/004c15a4.md)
- 新版 呼出元 2件 [`004c05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c0/004c05ec.md) [`004fcb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fcb38.md) · 呼出先 1件 [`004c15a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c1/004c15a4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc524",
      "READ",
      [
        "storage",
        "00c1cac8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc52c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c15a4"
      ]
    ]
  ],
  "added": [
    [
      "00bdc5d4",
      "READ",
      [
        "storage",
        "00c1cb78",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc5dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c15a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc520.md#insn-00bdc520) · [`00bdc524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc520.md#insn-00bdc524) · [`00bdc528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc520.md#insn-00bdc528)

~~~diff
- 00bdc520 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc520 bytes 10020090
- 00bdc524 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ac8:8"]]
- 00bdc524 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc524 bytes 116645f9
- 00bdc528 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00bdc528 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc528 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc528 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc528 bytes 10222b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279839f8d62312c23b856db87f98caed"></a>

### [`00bdc540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc540.md) → [`00bdc5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5f0.md) _ZN5Botan8PEM_Code6encodeEPKhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`004c8c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c8/004c8c88.md) [`004c93c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c93c4.md) [`004c9804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9804.md) [`004c9c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9c28.md) [`004cdf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cdf20.md) · 呼出先 1件 [`004c2990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c2990.md)
- 新版 呼出元 6件 [`004c8c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c8/004c8c88.md) [`004c93c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c93c4.md) [`004c9804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9804.md) [`004c9c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9c28.md) [`004cdf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cdf20.md) · 呼出先 1件 [`004c2990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2990.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc544",
      "READ",
      [
        "storage",
        "00c1cad8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc54c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c2990"
      ]
    ]
  ],
  "added": [
    [
      "00bdc5f4",
      "READ",
      [
        "storage",
        "00c1cb88",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc5fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c2990"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc540.md#insn-00bdc540) · [`00bdc544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc540.md#insn-00bdc544) · [`00bdc548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc540.md#insn-00bdc548)

~~~diff
- 00bdc540 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc540 bytes 10020090
- 00bdc544 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ad8:8"]]
- 00bdc544 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc544 bytes 116e45f9
- 00bdc548 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00bdc548 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc548 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc548 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc548 bytes 10622b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d39c1feef1d7d8b9183d499cbe6a9ad9"></a>

### [`00bdc550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc550.md) → [`00bdc600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc600.md) _ZN5Botan8PEM_Code18decode_check_labelERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c36b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c36b4.md) [`004ce004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce004.md) · 呼出先 1件 [`004c2d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c2d3c.md)
- 新版 呼出元 2件 [`004c36b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c36b4.md) [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md) · 呼出先 1件 [`004c2d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2d3c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc554",
      "READ",
      [
        "storage",
        "00c1cae0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc55c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c2d3c"
      ]
    ]
  ],
  "added": [
    [
      "00bdc604",
      "READ",
      [
        "storage",
        "00c1cb90",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc60c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c2d3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc550.md#insn-00bdc550) · [`00bdc554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc550.md#insn-00bdc554) · [`00bdc558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc550.md#insn-00bdc558)

~~~diff
- 00bdc550 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc550 bytes 10020090
- 00bdc554 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ae0:8"]]
- 00bdc554 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc554 bytes 117245f9
- 00bdc558 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00bdc558 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc558 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc558 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc558 bytes 10822b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a740b41d55cb998399e0bfdb09496760"></a>

### [`00bdc560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc560.md) → [`00bdc610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc610.md) _ZN5Botan8PEM_Code6decodeERNS_10DataSourceERNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004c2d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c2d3c.md) [`004c37cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c37cc.md) [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) [`004ea660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ea/004ea660.md) · 呼出先 1件 [`004c2f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c2f88.md)
- 新版 呼出元 4件 [`004c2d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2d3c.md) [`004c37cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c37cc.md) [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`004ea660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md) · 呼出先 1件 [`004c2f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc564",
      "READ",
      [
        "storage",
        "00c1cae8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc56c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c2f88"
      ]
    ]
  ],
  "added": [
    [
      "00bdc614",
      "READ",
      [
        "storage",
        "00c1cb98",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc61c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c2f88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc560.md#insn-00bdc560) · [`00bdc564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc560.md#insn-00bdc564) · [`00bdc568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc560.md#insn-00bdc568)

~~~diff
- 00bdc560 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc560 bytes 10020090
- 00bdc564 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ae8:8"]]
- 00bdc564 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc564 bytes 117645f9
- 00bdc568 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00bdc568 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc568 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc568 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc568 bytes 10a22b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbe8372893fc0c106f1ff6aeb6e6ba05"></a>

### [`00bdc570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc570.md) → [`00bdc620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc620.md) _ZN5Botan17DataSource_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004c36b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c36b4.md) [`004c37cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c37cc.md) [`004cafdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ca/004cafdc.md) [`004ce7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce7d8.md) · 呼出先 1件 [`004d6c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004d6/004d6c30.md)
- 新版 呼出元 4件 [`004c36b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c36b4.md) [`004c37cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c37cc.md) [`004cafdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ca/004cafdc.md) [`004ce7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce7d8.md) · 呼出先 1件 [`004d6c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6c30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc574",
      "READ",
      [
        "storage",
        "00c1caf0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc57c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d6c30"
      ]
    ]
  ],
  "added": [
    [
      "00bdc624",
      "READ",
      [
        "storage",
        "00c1cba0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc62c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004d6c30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc570.md#insn-00bdc570) · [`00bdc574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc570.md#insn-00bdc574) · [`00bdc578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc570.md#insn-00bdc578)

~~~diff
- 00bdc570 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc570 bytes 10020090
- 00bdc574 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:af0:8"]]
- 00bdc574 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc574 bytes 117a45f9
- 00bdc578 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00bdc578 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc578 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc578 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc578 bytes 10c22b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36befb700f0ec5b4cf4c467031fdcf76"></a>

### [`00bdc5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5c0.md) → [`00bdc670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md) _ZN5Botan13EMSA_PKCS1v15C1EPNS_12HashFunctionE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c3c00.md) [`0051038c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00510/0051038c.md) · 呼出先 1件 [`0049dbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049d/0049dbe4.md)
- 新版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`0051038c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/0051038c.md) · 呼出先 1件 [`0049dbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049d/0049dbe4.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdc674",
      "READ",
      [
        "storage",
        "00c1cb18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bdc674",
      "READ",
      [
        "storage",
        "00c1cbc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc5c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5c0.md#insn-00bdc5c4) · [`00bdc5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5c0.md#insn-00bdc5c8)
- 新版 [`00bdc674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md#insn-00bdc674) · [`00bdc678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc670.md#insn-00bdc678)

~~~diff
- 00bdc5c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b18:8"]]
- 00bdc5c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdc674 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bc8:8"]]
+ 00bdc674 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc5c4 bytes 118e45f9
+ 00bdc674 bytes 11e645f9
- 00bdc5c8 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00bdc5c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc5c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc5c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc5c8 bytes 10622c91
+ 00bdc678 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00bdc678 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
+ 00bdc678 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
+ 00bdc678 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
+ 00bdc678 bytes 10222f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f13f30f80e85d69a8df141165e1ae540"></a>

### [`00bdc5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5e0.md) → [`00bdc690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc690.md) _ZN5Botan8PSSR_RawC2EPNS_12HashFunctionEm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c3/004c3c00.md) [`00510820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00510/00510820.md) · 呼出先 1件 [`0049fe48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049f/0049fe48.md)
- 新版 呼出元 2件 [`004c3c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c3/004c3c00.md) [`00510820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00510/00510820.md) · 呼出先 1件 [`0049fe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049f/0049fe48.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc5e4",
      "READ",
      [
        "storage",
        "00c1cb28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc5ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049fe48"
      ]
    ]
  ],
  "added": [
    [
      "00bdc694",
      "READ",
      [
        "storage",
        "00c1cbd8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc69c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0049fe48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5e0.md#insn-00bdc5e0) · [`00bdc5e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5e0.md#insn-00bdc5e4) · [`00bdc5e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc5e0.md#insn-00bdc5e8)

~~~diff
- 00bdc5e0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc5e0 bytes 10020090
- 00bdc5e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b28:8"]]
- 00bdc5e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc5e4 bytes 119645f9
- 00bdc5e8 ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00bdc5e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc5e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc5e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc5e8 bytes 10a22c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ada4d5e534dd90bd88496b98deb0f31"></a>

### [`00bdc630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc630.md) → [`00bdc6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6e0.md) _ZN5Botan13RSA_PublicKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004c52e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c52e0.md) · 呼出先 1件 [`004c56b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c56b0.md)
- 新版 呼出元 1件 [`004c52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c52e0.md) · 呼出先 1件 [`004c56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c56b0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc634",
      "READ",
      [
        "storage",
        "00c1cb50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc63c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c56b0"
      ]
    ]
  ],
  "added": [
    [
      "00bdc6e4",
      "READ",
      [
        "storage",
        "00c1cc00",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc6ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c56b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc630.md#insn-00bdc630) · [`00bdc634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc630.md#insn-00bdc634) · [`00bdc638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc630.md#insn-00bdc638)

~~~diff
- 00bdc630 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc630 bytes 10020090
- 00bdc634 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b50:8"]]
- 00bdc634 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc634 bytes 11aa45f9
- 00bdc638 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 00bdc638 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc638 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc638 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc638 bytes 10422d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f36881fef9f7ddfd71b1422dcff14e8"></a>

### [`00bdc640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc640.md) → [`00bdc6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc6f0.md) _ZN5Botan16load_private_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c9/004c9e38.md) · 呼出先 1件 [`004c585c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c5/004c585c.md)
- 新版 呼出元 1件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) · 呼出先 1件 [`004c585c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c5/004c585c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc644",
      "READ",
      [
        "storage",
        "00c1cb58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc64c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c585c"
      ]
    ]
  ],
  "added": [
    [
      "00bdc6f4",
      "READ",
      [
        "storage",
        "00c1cc08",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc6fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004c585c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc640.md#insn-00bdc640) · [`00bdc644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc640.md#insn-00bdc644) · [`00bdc648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc640.md#insn-00bdc648)

~~~diff
- 00bdc640 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc640 bytes 10020090
- 00bdc644 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b58:8"]]
- 00bdc644 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc644 bytes 11ae45f9
- 00bdc648 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 00bdc648 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc648 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc648 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc648 bytes 10622d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba4254fa99682213906b7b8673bb009"></a>

### [`00bdc770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc770.md) → [`00bdc820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc820.md) _ZN5Botan4X50910PEM_encodeERKNS_10Public_KeyE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004ce7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce7d8.md) [`00501b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00501/00501b08.md) · 呼出先 1件 [`004cdf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004cd/004cdf20.md)
- 新版 呼出元 2件 [`004ce7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce7d8.md) [`00501b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00501/00501b08.md) · 呼出先 1件 [`004cdf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004cd/004cdf20.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc774",
      "READ",
      [
        "storage",
        "00c1cbf0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc77c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004cdf20"
      ]
    ]
  ],
  "added": [
    [
      "00bdc824",
      "READ",
      [
        "storage",
        "00c1cca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc82c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004cdf20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc770.md#insn-00bdc770) · [`00bdc774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc770.md#insn-00bdc774) · [`00bdc778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc770.md#insn-00bdc778)

~~~diff
- 00bdc770 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc770 bytes 10020090
- 00bdc774 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bf0:8"]]
- 00bdc774 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc774 bytes 11fa45f9
- 00bdc778 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 00bdc778 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc778 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc778 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc778 bytes 10c22f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c25985c911b1c5437d5e9b9afee421d6"></a>

### [`00bdc780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md) → [`00bdc830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc830.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004ce670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce670.md) [`004ce6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce6fc.md) [`004ce7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce7d8.md) [`004ec0b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec0b4.md) [`0055ddc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055ddc8.md) · 呼出先 1件 [`004ce004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce004.md)
- 新版 呼出元 5件 [`004ce670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce670.md) [`004ce6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md) [`004ce7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce7d8.md) [`004ec0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec0b4.md) [`0055ddc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055ddc8.md) · 呼出先 1件 [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc784",
      "READ",
      [
        "storage",
        "00c1cbf8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc78c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce004"
      ]
    ]
  ],
  "added": [
    [
      "00bdc834",
      "READ",
      [
        "storage",
        "00c1cca8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc83c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce004"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md#insn-00bdc780) · [`00bdc784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md#insn-00bdc784) · [`00bdc788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc780.md#insn-00bdc788)

~~~diff
- 00bdc780 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc780 bytes 10020090
- 00bdc784 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bf8:8"]]
- 00bdc784 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc784 bytes 11fe45f9
- 00bdc788 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00bdc788 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc788 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc788 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc788 bytes 10e22f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17b772261bd84721a5bbdd053f1aff6"></a>

### [`00bdc7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7a0.md) → [`00bdc850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc850.md) _ZN5Botan4X5098load_keyERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004fdfd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fd/004fdfd8.md) [`00500f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00500/00500f10.md) · 呼出先 1件 [`004ce6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ce/004ce6fc.md)
- 新版 呼出元 2件 [`004fdfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fd/004fdfd8.md) [`00500f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00500/00500f10.md) · 呼出先 1件 [`004ce6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce6fc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdc7a4",
      "READ",
      [
        "storage",
        "00c1cc08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdc7ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce6fc"
      ]
    ]
  ],
  "added": [
    [
      "00bdc854",
      "READ",
      [
        "storage",
        "00c1ccb8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdc85c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ce6fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdc7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7a0.md#insn-00bdc7a0) · [`00bdc7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7a0.md#insn-00bdc7a4) · [`00bdc7a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc7a0.md#insn-00bdc7a8)

~~~diff
- 00bdc7a0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdc7a0 bytes 10020090
- 00bdc7a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c08:8"]]
- 00bdc7a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdc7a4 bytes 110646f9
- 00bdc7a8 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00bdc7a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc7a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdc7a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdc7a8 bytes 10223091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e3b824d072def65b20d9e9608cc3db6"></a>

### [`00bdcbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbc0.md) → [`00bdcc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc70.md) _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`004e21a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e2/004e21a8.md) [`004f27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f2/004f27ec.md) [`004fb978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb978.md) [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) [`0050af44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050af44.md) · 呼出先 1件 [`004dbf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004db/004dbf98.md)
- 新版 呼出元 9件 [`004e21a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e2/004e21a8.md) [`004f27ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f27ec.md) [`004fb978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050af44.md) · 呼出先 1件 [`004dbf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004db/004dbf98.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcbc4",
      "READ",
      [
        "storage",
        "00c1ce18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcbcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004dbf98"
      ]
    ]
  ],
  "added": [
    [
      "00bdcc74",
      "READ",
      [
        "storage",
        "00c1cec8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcc7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004dbf98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbc0.md#insn-00bdcbc0) · [`00bdcbc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbc0.md#insn-00bdcbc4) · [`00bdcbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbc0.md#insn-00bdcbc8)

~~~diff
- 00bdcbc0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcbc0 bytes 10020090
- 00bdcbc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:e18:8"]]
- 00bdcbc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcbc4 bytes 110e47f9
- 00bdcbc8 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00bdcbc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcbc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcbc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcbc8 bytes 10623891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf5785c934712bc04a288867e0298f68"></a>

### [`00bdcbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbe0.md) → [`00bdcc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004ede80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050b/0050b45c.md) · 呼出先 1件 [`004e3024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e3/004e3024.md)
- 新版 呼出元 3件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050b/0050b45c.md) · 呼出先 1件 [`004e3024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e3/004e3024.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcbe4",
      "READ",
      [
        "storage",
        "00c1ce28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcbec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e3024"
      ]
    ]
  ],
  "added": [
    [
      "00bdcc94",
      "READ",
      [
        "storage",
        "00c1ced8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcc9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e3024"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbe0.md#insn-00bdcbe0) · [`00bdcbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbe0.md#insn-00bdcbe4) · [`00bdcbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbe0.md#insn-00bdcbe8)

~~~diff
- 00bdcbe0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcbe0 bytes 10020090
- 00bdcbe4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:e28:8"]]
- 00bdcbe4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcbe4 bytes 111647f9
- 00bdcbe8 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00bdcbe8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcbe8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcbe8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcbe8 bytes 10a23891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f6e955f0e8cb888a2eb4a80daa63a1"></a>

### [`00bdccb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccb0.md) → [`00bdcd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd60.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004e8a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8a14.md) · 呼出先 1件 [`004e85ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e85ec.md)
- 新版 呼出元 1件 [`004e8a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md) · 呼出先 1件 [`004e85ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e85ec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdccb4",
      "READ",
      [
        "storage",
        "00c1ce90",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdccbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e85ec"
      ]
    ]
  ],
  "added": [
    [
      "00bdcd64",
      "READ",
      [
        "storage",
        "00c1cf40",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcd6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e85ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdccb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccb0.md#insn-00bdccb0) · [`00bdccb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccb0.md#insn-00bdccb4) · [`00bdccb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccb0.md#insn-00bdccb8)

~~~diff
- 00bdccb0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdccb0 bytes 10020090
- 00bdccb4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:e90:8"]]
- 00bdccb4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdccb4 bytes 114a47f9
- 00bdccb8 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00bdccb8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdccb8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdccb8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdccb8 bytes 10423a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3d1544e9336ea7f9ff59a6abf4f55dd"></a>

### [`00bdccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccd0.md) → [`00bdcd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd80.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00504f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00504/00504f50.md) · 呼出先 1件 [`004e8a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004e8/004e8a14.md)
- 新版 呼出元 1件 [`00504f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00504/00504f50.md) · 呼出先 1件 [`004e8a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004e8/004e8a14.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdccd4",
      "READ",
      [
        "storage",
        "00c1cea0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdccdc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8a14"
      ]
    ]
  ],
  "added": [
    [
      "00bdcd84",
      "READ",
      [
        "storage",
        "00c1cf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcd8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004e8a14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccd0.md#insn-00bdccd0) · [`00bdccd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccd0.md#insn-00bdccd4) · [`00bdccd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdccd0.md#insn-00bdccd8)

~~~diff
- 00bdccd0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdccd0 bytes 10020090
- 00bdccd4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ea0:8"]]
- 00bdccd4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdccd4 bytes 115247f9
- 00bdccd8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00bdccd8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdccd8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdccd8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdccd8 bytes 10823a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-305eca42998944cc2d8db46dd4c18a13"></a>

### [`00bdcdc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdc0.md) → [`00bdce70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce70.md) _ZNK5Botan14PKCS10_Request10path_limitEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ede80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md) · 呼出先 1件 [`004ec8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ec/004ec8c8.md)
- 新版 呼出元 1件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) · 呼出先 1件 [`004ec8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ec/004ec8c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcdc4",
      "READ",
      [
        "storage",
        "00c1cf18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcdcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ec8c8"
      ]
    ]
  ],
  "added": [
    [
      "00bdce74",
      "READ",
      [
        "storage",
        "00c1cfc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdce7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004ec8c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcdc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdc0.md#insn-00bdcdc0) · [`00bdcdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdc0.md#insn-00bdcdc4) · [`00bdcdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdc0.md#insn-00bdcdc8)

~~~diff
- 00bdcdc0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcdc0 bytes 10020090
- 00bdcdc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f18:8"]]
- 00bdcdc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcdc4 bytes 118e47f9
- 00bdcdc8 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00bdcdc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcdc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcdc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcdc8 bytes 10623c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d3389a0651f7f8f05d2edc8d2b1b8e2"></a>

### [`00bdcdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdf0.md) → [`00bdcea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcea0.md) _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004ede80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a638.md) · 呼出先 1件 [`004f61e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f6/004f61e8.md)
- 新版 呼出元 2件 [`004ede80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ed/004ede80.md) [`0050a638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a638.md) · 呼出先 1件 [`004f61e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f6/004f61e8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcdf4",
      "READ",
      [
        "storage",
        "00c1cf30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcdfc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f61e8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcea4",
      "READ",
      [
        "storage",
        "00c1cfe0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdceac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f61e8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdf0.md#insn-00bdcdf0) · [`00bdcdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdf0.md#insn-00bdcdf4) · [`00bdcdf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdf0.md#insn-00bdcdf8)

~~~diff
- 00bdcdf0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcdf0 bytes 10020090
- 00bdcdf4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f30:8"]]
- 00bdcdf4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcdf4 bytes 119a47f9
- 00bdcdf8 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00bdcdf8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcdf8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcdf8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcdf8 bytes 10c23c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0b2c96753fec8c172c9e3d5460bb311"></a>

### [`00bdce30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce30.md) → [`00bdcee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcee0.md) _ZNK5Botan7X509_CA10update_crlERKNS_8X509_CRLERKNSt6__ndk16vectorINS_9CRL_EntryENS4_9allocatorIS6_EEEERNS_21RandomNumberGeneratorENS4_6chron

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004eef24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004eef24.md) · 呼出先 1件 [`004eef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004eef84.md)
- 新版 呼出元 1件 [`004eef24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004eef24.md) · 呼出先 1件 [`004eef84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ee/004eef84.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdce34",
      "READ",
      [
        "storage",
        "00c1cf50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdce3c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004eef84"
      ]
    ]
  ],
  "added": [
    [
      "00bdcee4",
      "READ",
      [
        "storage",
        "00c1d000",
        null,
        "pointer"
      ]
    ],
    [
      "00bdceec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004eef84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce30.md#insn-00bdce30) · [`00bdce34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce30.md#insn-00bdce34) · [`00bdce38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce30.md#insn-00bdce38)

~~~diff
- 00bdce30 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdce30 bytes 10020090
- 00bdce34 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f50:8"]]
- 00bdce34 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce34 bytes 11aa47f9
- 00bdce38 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00bdce38 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce38 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce38 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdce38 bytes 10423d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-206daa278e55ba8cb4d3d5e3c9a5dc79"></a>

### [`00bdce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce40.md) → [`00bdcef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcef0.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004ef204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004ef204.md) · 呼出先 1件 [`004efb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ef/004efb8c.md)
- 新版 呼出元 1件 [`004ef204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004ef204.md) · 呼出先 1件 [`004efb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ef/004efb8c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdce44",
      "READ",
      [
        "storage",
        "00c1cf58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdce4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004efb8c"
      ]
    ]
  ],
  "added": [
    [
      "00bdcef4",
      "READ",
      [
        "storage",
        "00c1d008",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcefc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004efb8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce40.md#insn-00bdce40) · [`00bdce44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce40.md#insn-00bdce44) · [`00bdce48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce40.md#insn-00bdce48)

~~~diff
- 00bdce40 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdce40 bytes 10020090
- 00bdce44 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f58:8"]]
- 00bdce44 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce44 bytes 11ae47f9
- 00bdce48 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00bdce48 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce48 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce48 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdce48 bytes 10623d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-444441f44fbff6a77ba73a172583e653"></a>

### [`00bdce50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce50.md) → [`00bdcf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf00.md) _ZNK5Botan8X509_CRL10is_revokedERKNS_16X509_CertificateE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005054cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00505/005054cc.md) · 呼出先 1件 [`004f00b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f00b0.md)
- 新版 呼出元 1件 [`005054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00505/005054cc.md) · 呼出先 1件 [`004f00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f00b0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdce54",
      "READ",
      [
        "storage",
        "00c1cf60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdce5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f00b0"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf04",
      "READ",
      [
        "storage",
        "00c1d010",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcf0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f00b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce50.md#insn-00bdce50) · [`00bdce54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce50.md#insn-00bdce54) · [`00bdce58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce50.md#insn-00bdce58)
- 新版 [`00bdcf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf00.md#insn-00bdcf00)

~~~diff
- 00bdce50 ["COPY", "register:4080:8", ["const:c1c000:8"]]
+ 00bdcf00 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdce50 bytes 10020090
+ 00bdcf00 bytes 100200b0
- 00bdce54 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f60:8"]]
- 00bdce54 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce54 bytes 11b247f9
- 00bdce58 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 00bdce58 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce58 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce58 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdce58 bytes 10823d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1bc567154cd6275b74da5224711c8d8"></a>

### [`00bdce60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce60.md) → [`00bdcf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf10.md) _ZNK5Botan14Cert_Extension10CRL_Number14get_crl_numberEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f03d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f0/004f03d8.md) · 呼出先 1件 [`004fa788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fa/004fa788.md)
- 新版 呼出元 1件 [`004f03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f0/004f03d8.md) · 呼出先 1件 [`004fa788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fa/004fa788.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdce64",
      "READ",
      [
        "storage",
        "00c1cf68",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdce6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fa788"
      ]
    ]
  ],
  "added": [
    [
      "00bdcf14",
      "READ",
      [
        "storage",
        "00c1d018",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcf1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fa788"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdce60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce60.md#insn-00bdce60) · [`00bdce64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce60.md#insn-00bdce64) · [`00bdce68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce60.md#insn-00bdce68)

~~~diff
- 00bdce60 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdce60 bytes 10020090
- 00bdce64 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f68:8"]]
- 00bdce64 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdce64 bytes 11b647f9
- 00bdce68 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00bdce68 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce68 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdce68 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdce68 bytes 10a23d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-856e793b7d3eb71a8031a0f9d664928c"></a>

### [`00bdcef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcef0.md) → [`00bdcfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfa0.md) _ZN5Botan11BER_Decoder11decode_listINS_14GeneralSubtreeEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f73a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f73a8.md) · 呼出先 1件 [`004f78a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f7/004f78a4.md)
- 新版 呼出元 1件 [`004f73a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f73a8.md) · 呼出先 1件 [`004f78a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f7/004f78a4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcef4",
      "READ",
      [
        "storage",
        "00c1cfb0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcefc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f78a4"
      ]
    ]
  ],
  "added": [
    [
      "00bdcfa4",
      "READ",
      [
        "storage",
        "00c1d060",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcfac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f78a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcef0.md#insn-00bdcef0) · [`00bdcef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcef0.md#insn-00bdcef4) · [`00bdcef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcef0.md#insn-00bdcef8)

~~~diff
- 00bdcef0 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcef0 bytes 10020090
- 00bdcef4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fb0:8"]]
- 00bdcef4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcef4 bytes 11da47f9
- 00bdcef8 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00bdcef8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcef8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcef8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcef8 bytes 10c23e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577fe9115956bb1c76b90dfe4e59f77f"></a>

### [`00bdcf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf00.md) → [`00bdcfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfb0.md) _ZNK5Botan16X509_Certificate11is_criticalERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f8244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8244.md) · 呼出先 1件 [`004f8990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004f8/004f8990.md)
- 新版 呼出元 1件 [`004f8244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8244.md) · 呼出先 1件 [`004f8990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f8/004f8990.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf04",
      "READ",
      [
        "storage",
        "00c1cfb8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f8990"
      ]
    ]
  ],
  "added": [
    [
      "00bdcfb4",
      "READ",
      [
        "storage",
        "00c1d068",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcfbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004f8990"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf00.md#insn-00bdcf00) · [`00bdcf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf00.md#insn-00bdcf04) · [`00bdcf08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf00.md#insn-00bdcf08)

~~~diff
- 00bdcf00 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcf00 bytes 10020090
- 00bdcf04 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fb8:8"]]
- 00bdcf04 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf04 bytes 11de47f9
- 00bdcf08 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 00bdcf08 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf08 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf08 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf08 bytes 10e23e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1297a7b78efd2f86d87af23a88e12e"></a>

### [`00bdcf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf10.md) → [`00bdcfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfc0.md) _ZN5Botan11BER_Decoder11decode_listINS_14Cert_Extension23CRL_Distribution_Points18Distribution_PointEEERS0_RNSt6__ndk16vectorIT_NS6_9allocat

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004fb0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb0d8.md) · 呼出先 1件 [`004fb4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb4c0.md)
- 新版 呼出元 1件 [`004fb0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb0d8.md) · 呼出先 1件 [`004fb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb4c0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf14",
      "READ",
      [
        "storage",
        "00c1cfc0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fb4c0"
      ]
    ]
  ],
  "added": [
    [
      "00bdcfc4",
      "READ",
      [
        "storage",
        "00c1d070",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcfcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fb4c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf10.md#insn-00bdcf10) · [`00bdcf14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf10.md#insn-00bdcf14) · [`00bdcf18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf10.md#insn-00bdcf18)

~~~diff
- 00bdcf10 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcf10 bytes 10020090
- 00bdcf14 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fc0:8"]]
- 00bdcf14 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf14 bytes 11e247f9
- 00bdcf18 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 00bdcf18 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf18 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf18 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf18 bytes 10023f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4446c1fd1b98460560f04a81badf0aa5"></a>

### [`00bdcf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf20.md) → [`00bdcfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcfd0.md) _ZN5Botan11BER_Decoder24decode_optional_implicitINS_15AlternativeNameEEERS0_RT_NS_8ASN1_TagES6_S6_S6_RKS4_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004fb978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fb978.md) · 呼出先 1件 [`004fbbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fb/004fbbe8.md)
- 新版 呼出元 1件 [`004fb978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fb978.md) · 呼出先 1件 [`004fbbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fb/004fbbe8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf24",
      "READ",
      [
        "storage",
        "00c1cfc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fbbe8"
      ]
    ]
  ],
  "added": [
    [
      "00bdcfd4",
      "READ",
      [
        "storage",
        "00c1d078",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcfdc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fbbe8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf20.md#insn-00bdcf20) · [`00bdcf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf20.md#insn-00bdcf24) · [`00bdcf28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf20.md#insn-00bdcf28)

~~~diff
- 00bdcf20 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcf20 bytes 10020090
- 00bdcf24 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fc8:8"]]
- 00bdcf24 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf24 bytes 11e647f9
- 00bdcf28 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00bdcf28 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf28 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf28 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf28 bytes 10223f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-881d97ed628d9693101b14d511a3bd1b"></a>

### [`00bdcf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf40.md) → [`00bdcff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcff0.md) _ZNK5Botan11X509_Object23hash_used_for_signatureEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00503af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503af8.md) [`0050a3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0050a/0050a3ac.md) · 呼出先 1件 [`004fc6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004fc/004fc6ac.md)
- 新版 呼出元 2件 [`00503af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503af8.md) [`0050a3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050a3ac.md) · 呼出先 1件 [`004fc6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004fc/004fc6ac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf44",
      "READ",
      [
        "storage",
        "00c1cfd8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fc6ac"
      ]
    ]
  ],
  "added": [
    [
      "00bdcff4",
      "READ",
      [
        "storage",
        "00c1d088",
        null,
        "pointer"
      ]
    ],
    [
      "00bdcffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "004fc6ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf40.md#insn-00bdcf40) · [`00bdcf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf40.md#insn-00bdcf44) · [`00bdcf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf40.md#insn-00bdcf48)

~~~diff
- 00bdcf40 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcf40 bytes 10020090
- 00bdcf44 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:fd8:8"]]
- 00bdcf44 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf44 bytes 11ee47f9
- 00bdcf48 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00bdcf48 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf48 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf48 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf48 bytes 10623f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9de20bdfef7be6d5e7fa148bfb9e119"></a>

### [`00bdcf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf80.md) → [`00bdd030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd030.md) _ZN5Botan9X509_TimeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00503338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/00503338.md) [`0050339c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00503/0050339c.md) · 呼出先 1件 [`0048ae6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0048a/0048ae6c.md)
- 新版 呼出元 2件 [`00503338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/00503338.md) [`0050339c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00503/0050339c.md) · 呼出先 1件 [`0048ae6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae6c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcf84",
      "READ",
      [
        "storage",
        "00c1cff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcf8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048ae6c"
      ]
    ]
  ],
  "added": [
    [
      "00bdd034",
      "READ",
      [
        "storage",
        "00c1d0a8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd03c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0048ae6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf80.md#insn-00bdcf80) · [`00bdcf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf80.md#insn-00bdcf84) · [`00bdcf88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcf80.md#insn-00bdcf88)

~~~diff
- 00bdcf80 ["COPY", "register:4080:8", ["const:c1c000:8"]]
- 00bdcf80 bytes 10020090
- 00bdcf84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ff8:8"]]
- 00bdcf84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcf84 bytes 11fe47f9
- 00bdcf88 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00bdcf88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcf88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcf88 bytes 10e23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57cd4a4b310240f16530a8d00c9321b1"></a>

### [`00bdcfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfc0.md) → [`00bdd070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd070.md) _ZN5Botan4PKIX9check_crlERKNSt6__ndk16vectorINS1_10shared_ptrIKNS_16X509_CertificateEEENS1_9allocatorIS6_EEEERKNS2_IPNS_17Certificate_StoreE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00508860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00508/00508860.md) · 呼出先 1件 [`005060a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00506/005060a8.md)
- 新版 呼出元 1件 [`00508860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00508/00508860.md) · 呼出先 1件 [`005060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00506/005060a8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdcfc4",
      "READ",
      [
        "storage",
        "00c1d018",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdcfcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005060a8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd074",
      "READ",
      [
        "storage",
        "00c1d0c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd07c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "005060a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdcfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfc0.md#insn-00bdcfc0) · [`00bdcfc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfc0.md#insn-00bdcfc4) · [`00bdcfc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcfc0.md#insn-00bdcfc8)

~~~diff
- 00bdcfc0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdcfc0 bytes 100200b0
- 00bdcfc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:18:8"]]
- 00bdcfc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdcfc4 bytes 110e40f9
- 00bdcfc8 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00bdcfc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcfc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdcfc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdcfc8 bytes 10620091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5a0bd7828cef1182d87c12c6a4fd8b"></a>

### [`00bdd170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd170.md) → [`00bdd220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd220.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0054841c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/0054841c.md) · 呼出先 1件 [`00b7d228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d228.md)
- 新版 呼出元 1件 [`0054841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/0054841c.md) · 呼出先 1件 [`00b7d2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d2f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd174",
      "READ",
      [
        "storage",
        "00c1d0f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd17c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d2f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdd224",
      "READ",
      [
        "storage",
        "00c1d1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd22c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b7d2f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd170.md#insn-00bdd170) · [`00bdd174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd170.md#insn-00bdd174) · [`00bdd178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd170.md#insn-00bdd178)

~~~diff
- 00bdd170 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd170 bytes 10020090
- 00bdd174 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f0:8"]]
- 00bdd174 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd174 bytes 117a40f9
- 00bdd178 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00bdd178 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd178 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd178 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd178 bytes 10c20391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5f2db7cf2bdcaf23962116c9d3c665"></a>

### [`00bdd180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd180.md) → [`00bdd230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd230.md) _ZNSt6__ndk115recursive_mutexD1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005488c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00548/005488c4.md) · 呼出先 1件 [`00b7d2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d2cc.md)
- 新版 呼出元 1件 [`005488c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00548/005488c4.md) · 呼出先 1件 [`00b7d394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d394.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd184",
      "READ",
      [
        "storage",
        "00c1d0f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bdd234",
      "READ",
      [
        "storage",
        "00c1d1a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd180.md#insn-00bdd180) · [`00bdd184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd180.md#insn-00bdd184) · [`00bdd188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd180.md#insn-00bdd188)

~~~diff
- 00bdd180 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd180 bytes 10020090
- 00bdd184 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f8:8"]]
- 00bdd184 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd184 bytes 117e40f9
- 00bdd188 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00bdd188 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd188 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd188 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd188 bytes 10e20391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9457d8e4f10d1eb48d7921a571587d4"></a>

### [`00bdd1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1b0.md) → [`00bdd260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd260.md) &lt;EXTERNAL&gt;::log10f

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00549504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00549/00549504.md) · 呼出先 1件 [`010a5238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5238.md)
- 新版 呼出元 1件 [`00549504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00549/00549504.md) · 呼出先 1件 [`010a5238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5238.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd1b4",
      "READ",
      [
        "storage",
        "00c1d110",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd1bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5238"
      ]
    ]
  ],
  "added": [
    [
      "00bdd264",
      "READ",
      [
        "storage",
        "00c1d1c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd26c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5238"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1b0.md#insn-00bdd1b0) · [`00bdd1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1b0.md#insn-00bdd1b4) · [`00bdd1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1b0.md#insn-00bdd1b8)

~~~diff
- 00bdd1b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd1b0 bytes 10020090
- 00bdd1b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:110:8"]]
- 00bdd1b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd1b4 bytes 118a40f9
- 00bdd1b8 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00bdd1b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd1b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd1b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd1b8 bytes 10420491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b42ee8d5c10c5af6444aff6cab118b85"></a>

### [`00bdd1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1c0.md) → [`00bdd270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd270.md) &lt;EXTERNAL&gt;::expf

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0054cdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054c/0054cdf0.md) · 呼出先 1件 [`010a5240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5240.md)
- 新版 呼出元 1件 [`0054cdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054c/0054cdf0.md) · 呼出先 1件 [`010a5240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5240.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd1c4",
      "READ",
      [
        "storage",
        "00c1d118",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd1cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5240"
      ]
    ]
  ],
  "added": [
    [
      "00bdd274",
      "READ",
      [
        "storage",
        "00c1d1c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd27c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5240"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1c0.md#insn-00bdd1c0) · [`00bdd1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1c0.md#insn-00bdd1c4) · [`00bdd1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1c0.md#insn-00bdd1c8)

~~~diff
- 00bdd1c0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd1c0 bytes 10020090
- 00bdd1c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:118:8"]]
- 00bdd1c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd1c4 bytes 118e40f9
- 00bdd1c8 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00bdd1c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd1c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd1c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd1c8 bytes 10620491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45b8b0a4afa28b4cae1b6e9beefb88c5"></a>

### [`00bdd1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1e0.md) → [`00bdd290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd290.md) &lt;EXTERNAL&gt;::__fread_chk

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0054da70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0054d/0054da70.md) · 呼出先 1件 [`010a5250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5250.md)
- 新版 呼出元 1件 [`0054da70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0054d/0054da70.md) · 呼出先 1件 [`010a5250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5250.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd1e4",
      "READ",
      [
        "storage",
        "00c1d128",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd1ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5250"
      ]
    ]
  ],
  "added": [
    [
      "00bdd294",
      "READ",
      [
        "storage",
        "00c1d1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd29c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5250"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1e0.md#insn-00bdd1e0) · [`00bdd1e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1e0.md#insn-00bdd1e4) · [`00bdd1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd1e0.md#insn-00bdd1e8)

~~~diff
- 00bdd1e0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd1e0 bytes 10020090
- 00bdd1e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:128:8"]]
- 00bdd1e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd1e4 bytes 119640f9
- 00bdd1e8 ["COPY", "tmp:0:8", ["const:128:8"]]
- 00bdd1e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd1e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd1e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd1e8 bytes 10a20491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90bc65ca31b8c788818db54b52f8879"></a>

### [`00bdd210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd210.md) → [`00bdd2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2c0.md) &lt;EXTERNAL&gt;::AAssetManager_open

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00559ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559ef4.md) [`0055aad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055aad0.md) [`0055af38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055af38.md) · 呼出先 1件 [`010a5268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5268.md)
- 新版 呼出元 3件 [`00559ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559ef4.md) [`0055aad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055aad0.md) [`0055af38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af38.md) · 呼出先 1件 [`010a5268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5268.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd214",
      "READ",
      [
        "storage",
        "00c1d140",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd21c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5268"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2c4",
      "READ",
      [
        "storage",
        "00c1d1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd2cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5268"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd210.md#insn-00bdd210) · [`00bdd214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd210.md#insn-00bdd214) · [`00bdd218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd210.md#insn-00bdd218)

~~~diff
- 00bdd210 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd210 bytes 10020090
- 00bdd214 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:140:8"]]
- 00bdd214 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd214 bytes 11a240f9
- 00bdd218 ["COPY", "tmp:0:8", ["const:140:8"]]
- 00bdd218 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd218 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd218 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd218 bytes 10020591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b5ed0291f2b36227a2d9e16ee388ca"></a>

### [`00bdd230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd230.md) → [`00bdd2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd2e0.md) &lt;EXTERNAL&gt;::AAsset_read

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00559fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00559/00559fe0.md) [`0055af38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055a/0055af38.md) · 呼出先 1件 [`010a5278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5278.md)
- 新版 呼出元 2件 [`00559fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00559/00559fe0.md) [`0055af38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055a/0055af38.md) · 呼出先 1件 [`010a5278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5278.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd234",
      "READ",
      [
        "storage",
        "00c1d150",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd23c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5278"
      ]
    ]
  ],
  "added": [
    [
      "00bdd2e4",
      "READ",
      [
        "storage",
        "00c1d200",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd2ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5278"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd230.md#insn-00bdd230) · [`00bdd234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd230.md#insn-00bdd234) · [`00bdd238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd230.md#insn-00bdd238)

~~~diff
- 00bdd230 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd230 bytes 10020090
- 00bdd234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:150:8"]]
- 00bdd234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd234 bytes 11aa40f9
- 00bdd238 ["COPY", "tmp:0:8", ["const:150:8"]]
- 00bdd238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd238 bytes 10420591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d51786c93b826de8f93b7a35886a210"></a>

### [`00bdd380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd380.md) → [`00bdd430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd430.md) &lt;EXTERNAL&gt;::AndroidBitmap_unlockPixels

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0055c994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5318.md)
- 新版 呼出元 2件 [`0055c994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055c/0055c994.md) [`0055d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055d/0055d5cc.md) · 呼出先 1件 [`010a5318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5318.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd384",
      "READ",
      [
        "storage",
        "00c1d1f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd38c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5318"
      ]
    ]
  ],
  "added": [
    [
      "00bdd434",
      "READ",
      [
        "storage",
        "00c1d2a8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd43c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5318"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd380.md#insn-00bdd380) · [`00bdd384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd380.md#insn-00bdd384) · [`00bdd388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd380.md#insn-00bdd388)

~~~diff
- 00bdd380 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd380 bytes 10020090
- 00bdd384 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1f8:8"]]
- 00bdd384 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd384 bytes 11fe40f9
- 00bdd388 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00bdd388 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd388 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd388 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd388 bytes 10e20791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6f8db0f526905b0018674e82b662d8c"></a>

### [`00bdd3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3f0.md) → [`00bdd4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd4a0.md) &lt;EXTERNAL&gt;::timegm

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00574f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574f30.md) · 呼出先 1件 [`010a5348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5348.md)
- 新版 呼出元 1件 [`00574f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574f30.md) · 呼出先 1件 [`010a5348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5348.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd3f4",
      "READ",
      [
        "storage",
        "00c1d230",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd3fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5348"
      ]
    ]
  ],
  "added": [
    [
      "00bdd4a4",
      "READ",
      [
        "storage",
        "00c1d2e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd4ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5348"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3f0.md#insn-00bdd3f0) · [`00bdd3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3f0.md#insn-00bdd3f4) · [`00bdd3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3f0.md#insn-00bdd3f8)

~~~diff
- 00bdd3f0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd3f0 bytes 10020090
- 00bdd3f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:230:8"]]
- 00bdd3f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd3f4 bytes 111a41f9
- 00bdd3f8 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00bdd3f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd3f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd3f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd3f8 bytes 10c20891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc20c7448f7b4bca6bdb099dfd73a6db"></a>

### [`00bdd4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4d0.md) → [`00bdd580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd580.md) &lt;EXTERNAL&gt;::glDisable

採用 · 移動量 `+0xb0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0056e920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e920.md) [`0056e934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056e934.md) [`0056ead8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056ead8.md) [`0056ec28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056e/0056ec28.md) [`0056f438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f438.md) · 呼出先 1件 [`010a53b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a53b8.md)
- 新版 呼出元 5件 [`0056e920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e920.md) [`0056e934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056e934.md) [`0056ead8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056ead8.md) [`0056ec28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056e/0056ec28.md) [`0056f438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f438.md) · 呼出先 1件 [`010a53b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a53b8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdd4d4",
      "READ",
      [
        "storage",
        "00c1d2a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdd4dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a53b8"
      ]
    ]
  ],
  "added": [
    [
      "00bdd584",
      "READ",
      [
        "storage",
        "00c1d350",
        null,
        "pointer"
      ]
    ],
    [
      "00bdd58c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a53b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdd4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4d0.md#insn-00bdd4d0) · [`00bdd4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4d0.md#insn-00bdd4d4) · [`00bdd4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd4d0.md#insn-00bdd4d8)

~~~diff
- 00bdd4d0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdd4d0 bytes 10020090
- 00bdd4d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2a0:8"]]
- 00bdd4d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdd4d4 bytes 115241f9
- 00bdd4d8 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00bdd4d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd4d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdd4d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdd4d8 bytes 10820a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c137b1a173328def9b6ae8b09d789fca"></a>

### [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md) → [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 32件 [`00af22dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af22dc.md) [`00af36ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af36ec.md) [`00af57bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af57bc.md) [`00af7190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7190.md) [`00b033b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b033b4.md) · 呼出先 1件 [`00af3a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3a74.md)
- 新版 呼出元 32件 [`00af23a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af23a4.md) [`00af37b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af37b4.md) [`00af5884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5884.md) [`00af7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7258.md) [`00b0347c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0347c.md) · 呼出先 1件 [`00af3b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3b3c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde644",
      "READ",
      [
        "storage",
        "00c1db58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde64c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3b3c"
      ]
    ]
  ],
  "added": [
    [
      "00bde6f4",
      "READ",
      [
        "storage",
        "00c1dc08",
        null,
        "pointer"
      ]
    ],
    [
      "00bde6fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3b3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md#insn-00bde640) · [`00bde644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md#insn-00bde644) · [`00bde648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md#insn-00bde648)

~~~diff
- 00bde640 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde640 bytes f00100f0
- 00bde644 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b58:8"]]
- 00bde644 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde644 bytes 11ae45f9
- 00bde648 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 00bde648 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde648 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde648 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde648 bytes 10622d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b5dbe261f7216c70845c6d9502cc443"></a>

### [`00bde690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde690.md) → [`00bde740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde740.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af0b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) [`00af77d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af77d4.md) · 呼出先 1件 [`00af77d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af77d4.md)
- 新版 呼出元 2件 [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00af789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af789c.md) · 呼出先 1件 [`00af789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af789c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde694",
      "READ",
      [
        "storage",
        "00c1db80",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde69c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af789c"
      ]
    ]
  ],
  "added": [
    [
      "00bde744",
      "READ",
      [
        "storage",
        "00c1dc30",
        null,
        "pointer"
      ]
    ],
    [
      "00bde74c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af789c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde690.md#insn-00bde690) · [`00bde694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde690.md#insn-00bde694) · [`00bde698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde690.md#insn-00bde698)

~~~diff
- 00bde690 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde690 bytes f00100f0
- 00bde694 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b80:8"]]
- 00bde694 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde694 bytes 11c245f9
- 00bde698 ["COPY", "tmp:0:8", ["const:b80:8"]]
- 00bde698 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde698 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde698 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde698 bytes 10022e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49af76420a5916311d0ff35f0829f74f"></a>

### [`00bde6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6b0.md) → [`00bde760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde760.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE7reserveEm

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af379c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af379c.md) [`00af51cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af51cc.md) · 呼出先 1件 [`00af3958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3958.md)
- 新版 呼出元 2件 [`00af3864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md) [`00af5294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5294.md) · 呼出先 1件 [`00af3a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3a20.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde6b4",
      "READ",
      [
        "storage",
        "00c1db90",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde6bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3a20"
      ]
    ]
  ],
  "added": [
    [
      "00bde764",
      "READ",
      [
        "storage",
        "00c1dc40",
        null,
        "pointer"
      ]
    ],
    [
      "00bde76c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af3a20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6b0.md#insn-00bde6b0) · [`00bde6b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6b0.md#insn-00bde6b4) · [`00bde6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6b0.md#insn-00bde6b8)

~~~diff
- 00bde6b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde6b0 bytes f00100f0
- 00bde6b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b90:8"]]
- 00bde6b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde6b4 bytes 11ca45f9
- 00bde6b8 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00bde6b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde6b8 bytes 10422e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed3ec3167d6bb602f3ba403669a03cd"></a>

### [`00bde6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6c0.md) → [`00bde770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde770.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00af2e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af2e14.md) [`00b23250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23250.md) [`00b23430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23430.md) [`00b58cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b58/00b58cb8.md) · 呼出先 1件 [`00af7bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7bc4.md)
- 新版 呼出元 4件 [`00af2edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af2edc.md) [`00b23318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23318.md) [`00b234f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b234f8.md) [`00b58d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58d80.md) · 呼出先 1件 [`00af7c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde6c4",
      "READ",
      [
        "storage",
        "00c1db98",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde6cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7c8c"
      ]
    ]
  ],
  "added": [
    [
      "00bde774",
      "READ",
      [
        "storage",
        "00c1dc48",
        null,
        "pointer"
      ]
    ],
    [
      "00bde77c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af7c8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6c0.md#insn-00bde6c0) · [`00bde6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6c0.md#insn-00bde6c4) · [`00bde6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6c0.md#insn-00bde6c8)

~~~diff
- 00bde6c0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde6c0 bytes f00100f0
- 00bde6c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:b98:8"]]
- 00bde6c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde6c4 bytes 11ce45f9
- 00bde6c8 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00bde6c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde6c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde6c8 bytes 10622e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edf4d3a42242ab74254d785bf298caf4"></a>

### [`00bde700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde700.md) → [`00bde7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7b0.md) &lt;EXTERNAL&gt;::__strncat_chk

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af7334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7334.md) · 呼出先 1件 [`010a5590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5590.md)
- 新版 呼出元 1件 [`00af73fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af73fc.md) · 呼出先 1件 [`010a5590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5590.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde704",
      "READ",
      [
        "storage",
        "00c1dbb8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde70c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5590"
      ]
    ]
  ],
  "added": [
    [
      "00bde7b4",
      "READ",
      [
        "storage",
        "00c1dc68",
        null,
        "pointer"
      ]
    ],
    [
      "00bde7bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5590"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde700.md#insn-00bde700) · [`00bde704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde700.md#insn-00bde704) · [`00bde708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde700.md#insn-00bde708)

~~~diff
- 00bde700 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde700 bytes f00100f0
- 00bde704 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bb8:8"]]
- 00bde704 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde704 bytes 11de45f9
- 00bde708 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 00bde708 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde708 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde708 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde708 bytes 10e22e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59814f8dedf5ed777d2dde43f975223"></a>

### [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) → [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) &lt;EXTERNAL&gt;::pthread_mutex_lock

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 22件 [`00af0b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) [`00af1258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1258.md) [`00af5bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bec.md) [`00af5df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md) [`00b053ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b053ac.md) · 呼出先 1件 [`010a55a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a55a0.md)
- 新版 呼出元 22件 [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00af1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md) [`00af5cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md) [`00af5ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md) [`00b05474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05474.md) · 呼出先 1件 [`010a55a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a55a0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde724",
      "READ",
      [
        "storage",
        "00c1dbc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde72c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55a0"
      ]
    ]
  ],
  "added": [
    [
      "00bde7d4",
      "READ",
      [
        "storage",
        "00c1dc78",
        null,
        "pointer"
      ]
    ],
    [
      "00bde7dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md#insn-00bde720) · [`00bde724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md#insn-00bde724) · [`00bde728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md#insn-00bde728)

~~~diff
- 00bde720 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde720 bytes f00100f0
- 00bde724 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bc8:8"]]
- 00bde724 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde724 bytes 11e645f9
- 00bde728 ["COPY", "tmp:0:8", ["const:bc8:8"]]
- 00bde728 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde728 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde728 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde728 bytes 10222f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94ba0c31079f4a344efb4825ef6a899"></a>

### [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) → [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) &lt;EXTERNAL&gt;::pthread_mutex_unlock

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 25件 [`00af0b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) [`00af1258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1258.md) [`00af5bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bec.md) [`00af5df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md) [`00b053dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b053dc.md) · 呼出先 1件 [`010a55a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a55a8.md)
- 新版 呼出元 25件 [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00af1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md) [`00af5cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md) [`00af5ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md) [`00b054a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054a4.md) · 呼出先 1件 [`010a55a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a55a8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde734",
      "READ",
      [
        "storage",
        "00c1dbd0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde73c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55a8"
      ]
    ]
  ],
  "added": [
    [
      "00bde7e4",
      "READ",
      [
        "storage",
        "00c1dc80",
        null,
        "pointer"
      ]
    ],
    [
      "00bde7ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md#insn-00bde730) · [`00bde734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md#insn-00bde734) · [`00bde738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md#insn-00bde738)

~~~diff
- 00bde730 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde730 bytes f00100f0
- 00bde734 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:bd0:8"]]
- 00bde734 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde734 bytes 11ea45f9
- 00bde738 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 00bde738 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde738 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde738 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde738 bytes 10422f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed67831f1dad643204d817eb61f9d269"></a>

### [`00bde7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7b0.md) → [`00bde860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) · 呼出先 1件 [`00af9234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9234.md)
- 新版 呼出元 1件 [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 1件 [`00af92fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde7b4",
      "READ",
      [
        "storage",
        "00c1dc10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde7bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af92fc"
      ]
    ]
  ],
  "added": [
    [
      "00bde864",
      "READ",
      [
        "storage",
        "00c1dcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00bde86c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af92fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7b0.md#insn-00bde7b0) · [`00bde7b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7b0.md#insn-00bde7b4) · [`00bde7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7b0.md#insn-00bde7b8)

~~~diff
- 00bde7b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde7b0 bytes f00100f0
- 00bde7b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c10:8"]]
- 00bde7b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde7b4 bytes 110a46f9
- 00bde7b8 ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00bde7b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde7b8 bytes 10423091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c918e7e20dc05cd7046a1e6cb2db52"></a>

### [`00bde7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7c0.md) → [`00bde870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde870.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) · 呼出先 1件 [`00afa1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa1d8.md)
- 新版 呼出元 1件 [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 1件 [`00afa2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa2a0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde7c4",
      "READ",
      [
        "storage",
        "00c1dc18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde7cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afa2a0"
      ]
    ]
  ],
  "added": [
    [
      "00bde874",
      "READ",
      [
        "storage",
        "00c1dcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bde87c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afa2a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7c0.md#insn-00bde7c0) · [`00bde7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7c0.md#insn-00bde7c4) · [`00bde7c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7c0.md#insn-00bde7c8)

~~~diff
- 00bde7c0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde7c0 bytes f00100f0
- 00bde7c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c18:8"]]
- 00bde7c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde7c4 bytes 110e46f9
- 00bde7c8 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00bde7c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde7c8 bytes 10623091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf646529219534eaf6d2dba6eb9b677e"></a>

### [`00bde7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7d0.md) → [`00bde880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md) _ZN8firebase10app_common6AddAppEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10InitResultENS3_4l

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) · 呼出先 1件 [`00af8d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8d88.md)
- 新版 呼出元 1件 [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 1件 [`00af8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde7d4",
      "READ",
      [
        "storage",
        "00c1dc20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde7dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af8e50"
      ]
    ]
  ],
  "added": [
    [
      "00bde884",
      "READ",
      [
        "storage",
        "00c1dcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00bde88c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00af8e50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7d0.md#insn-00bde7d0) · [`00bde7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7d0.md#insn-00bde7d4) · [`00bde7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7d0.md#insn-00bde7d8)

~~~diff
- 00bde7d0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde7d0 bytes f00100f0
- 00bde7d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c20:8"]]
- 00bde7d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde7d4 bytes 111246f9
- 00bde7d8 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00bde7d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde7d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde7d8 bytes 10823091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0cbd3a7ff0c3453c968b8e013535755"></a>

### [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md) → [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 13件 [`00af9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9e20.md) [`00afd508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd508.md) [`00b02438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02438.md) [`00b1d748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d748.md) [`00b210f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b21/00b210f8.md) · 呼出先 1件 [`00afa9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa9e4.md)
- 新版 呼出元 13件 [`00af9ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md) [`00afd5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd5d0.md) [`00b02500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md) [`00b1d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md) [`00b211c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b211c0.md) · 呼出先 1件 [`00afaaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde874",
      "READ",
      [
        "storage",
        "00c1dc70",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde87c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afaaac"
      ]
    ]
  ],
  "added": [
    [
      "00bde924",
      "READ",
      [
        "storage",
        "00c1dd20",
        null,
        "pointer"
      ]
    ],
    [
      "00bde92c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afaaac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md#insn-00bde870) · [`00bde874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md#insn-00bde874) · [`00bde878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md#insn-00bde878)

~~~diff
- 00bde870 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde870 bytes f00100f0
- 00bde874 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c70:8"]]
- 00bde874 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde874 bytes 113a46f9
- 00bde878 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00bde878 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde878 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde878 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde878 bytes 10c23191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

