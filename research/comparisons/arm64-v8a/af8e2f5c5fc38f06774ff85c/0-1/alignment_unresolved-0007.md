# v15.7.2 → v15.7.3 · 命令位置の検査未完了 (7)

[一覧の目次](README.md)

<a id="compare-c258ca659d46e82a40e7f81b7ae11ca6"></a>

### [`00bde890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde890.md) → [`00bde940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00af90fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af90fc.md) [`00af9488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md) [`00afa7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa7c4.md) · 呼出先 1件 [`00afabc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afabc4.md)
- 新版 呼出元 3件 [`00af91c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md) [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) [`00afa88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md) · 呼出先 1件 [`00afac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde894",
      "READ",
      [
        "storage",
        "00c1dc80",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde89c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afac8c"
      ]
    ]
  ],
  "added": [
    [
      "00bde944",
      "READ",
      [
        "storage",
        "00c1dd30",
        null,
        "pointer"
      ]
    ],
    [
      "00bde94c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afac8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde890.md#insn-00bde894) · [`00bde898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde890.md#insn-00bde898) · [`00bde89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde890.md#insn-00bde89c)

~~~diff
- 00bde894 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c80:8"]]
- 00bde894 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde894 bytes 114246f9
- 00bde898 ["COPY", "tmp:0:8", ["const:c80:8"]]
- 00bde898 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde898 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde898 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde898 bytes 10023291
- 00bde89c ["COPY", "register:0:8", ["register:4088:8"]]
- 00bde89c ["BRANCHIND", null, ["register:0:8"]]
- 00bde89c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccc1def901160fe2468b034aa2a7c2e5"></a>

### [`00bde8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8a0.md) → [`00bde950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af9488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md) · 呼出先 1件 [`00afadc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afadc0.md)
- 新版 呼出元 1件 [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) · 呼出先 1件 [`00afae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde8a4",
      "READ",
      [
        "storage",
        "00c1dc88",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde8ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afae88"
      ]
    ]
  ],
  "added": [
    [
      "00bde954",
      "READ",
      [
        "storage",
        "00c1dd38",
        null,
        "pointer"
      ]
    ],
    [
      "00bde95c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afae88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8a0.md#insn-00bde8a0) · [`00bde8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8a0.md#insn-00bde8a4) · [`00bde8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8a0.md#insn-00bde8a8)

~~~diff
- 00bde8a0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde8a0 bytes f00100f0
- 00bde8a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c88:8"]]
- 00bde8a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde8a4 bytes 114646f9
- 00bde8a8 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00bde8a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde8a8 bytes 10223291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f10df52bd120b02416b1fc4a6ab663"></a>

### [`00bde8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8b0.md) → [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00af9488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md) [`00afae90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afae90.md) · 呼出先 1件 [`00afae90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afae90.md)
- 新版 呼出元 2件 [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) [`00afaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md) · 呼出先 1件 [`00afaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde8b4",
      "READ",
      [
        "storage",
        "00c1dc90",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde8bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afaf58"
      ]
    ]
  ],
  "added": [
    [
      "00bde964",
      "READ",
      [
        "storage",
        "00c1dd40",
        null,
        "pointer"
      ]
    ],
    [
      "00bde96c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afaf58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8b0.md#insn-00bde8b0) · [`00bde8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8b0.md#insn-00bde8b4) · [`00bde8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8b0.md#insn-00bde8b8)

~~~diff
- 00bde8b0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde8b0 bytes f00100f0
- 00bde8b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c90:8"]]
- 00bde8b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde8b4 bytes 114a46f9
- 00bde8b8 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00bde8b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde8b8 bytes 10423291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a92d52ca05d667ef218310673f25b36"></a>

### [`00bde8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8c0.md) → [`00bde970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde970.md) _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00af92d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af92d0.md) · 呼出先 1件 [`00afacd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afacd8.md)
- 新版 呼出元 1件 [`00af9398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9398.md) · 呼出先 1件 [`00afada0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afada0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bde8c4",
      "READ",
      [
        "storage",
        "00c1dc98",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bde8cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afada0"
      ]
    ]
  ],
  "added": [
    [
      "00bde974",
      "READ",
      [
        "storage",
        "00c1dd48",
        null,
        "pointer"
      ]
    ],
    [
      "00bde97c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afada0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bde8c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8c0.md#insn-00bde8c0) · [`00bde8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8c0.md#insn-00bde8c4) · [`00bde8c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8c0.md#insn-00bde8c8)

~~~diff
- 00bde8c0 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bde8c0 bytes f00100f0
- 00bde8c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:c98:8"]]
- 00bde8c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bde8c4 bytes 114e46f9
- 00bde8c8 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00bde8c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bde8c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bde8c8 bytes 10623291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db55601392b6b4e51ee7fdb83ef7f1b"></a>

### [`00bdec60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec60.md) → [`00bded10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded10.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertIPKcEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__li

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00afdf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdf50.md) [`00afe3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe3a4.md) · 呼出先 1件 [`00afe3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe3a4.md)
- 新版 呼出元 2件 [`00afe018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe018.md) [`00afe46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md) · 呼出先 1件 [`00afe46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe46c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdec64",
      "READ",
      [
        "storage",
        "00c1de68",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdec6c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afe46c"
      ]
    ]
  ],
  "added": [
    [
      "00bded14",
      "READ",
      [
        "storage",
        "00c1df18",
        null,
        "pointer"
      ]
    ],
    [
      "00bded1c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afe46c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdec60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec60.md#insn-00bdec60) · [`00bdec64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec60.md#insn-00bdec64) · [`00bdec68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec60.md#insn-00bdec68)

~~~diff
- 00bdec60 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdec60 bytes f00100f0
- 00bdec64 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:e68:8"]]
- 00bdec64 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdec64 bytes 113647f9
- 00bdec68 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00bdec68 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdec68 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdec68 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdec68 bytes 10a23991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7da670e3de1066d4ae3b4a7ed9b2c72c"></a>

### [`00bdec70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec70.md) → [`00bded20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded20.md) &lt;EXTERNAL&gt;::__strchr_chk

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00afce0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afce0c.md) [`00afd77c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd77c.md) · 呼出先 1件 [`010a55f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a55f0.md)
- 新版 呼出元 2件 [`00afced4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afced4.md) [`00afd844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd844.md) · 呼出先 1件 [`010a55f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a55f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdec74",
      "READ",
      [
        "storage",
        "00c1de70",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdec7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55f0"
      ]
    ]
  ],
  "added": [
    [
      "00bded24",
      "READ",
      [
        "storage",
        "00c1df20",
        null,
        "pointer"
      ]
    ],
    [
      "00bded2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a55f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdec70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec70.md#insn-00bdec70) · [`00bdec74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec70.md#insn-00bdec74) · [`00bdec78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec70.md#insn-00bdec78)

~~~diff
- 00bdec70 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdec70 bytes f00100f0
- 00bdec74 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:e70:8"]]
- 00bdec74 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdec74 bytes 113a47f9
- 00bdec78 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00bdec78 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdec78 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdec78 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdec78 bytes 10c23991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3316ab83ee2c1450da5f27ca091e79c4"></a>

### [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md) → [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 23件 [`00aff154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff154.md) [`00b01608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md) [`00b0278c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md) [`00b0dcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md) [`00b0de68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md) · 呼出先 1件 [`00b00e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e74.md)
- 新版 呼出元 23件 [`00aff21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff21c.md) [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) [`00b0ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md) [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) · 呼出先 1件 [`00b00f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bded04",
      "READ",
      [
        "storage",
        "00c1deb8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bded0c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b00f3c"
      ]
    ]
  ],
  "added": [
    [
      "00bdedb4",
      "READ",
      [
        "storage",
        "00c1df68",
        null,
        "pointer"
      ]
    ],
    [
      "00bdedbc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b00f3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md#insn-00bded00) · [`00bded04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md#insn-00bded04) · [`00bded08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md#insn-00bded08)

~~~diff
- 00bded00 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bded00 bytes f00100f0
- 00bded04 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:eb8:8"]]
- 00bded04 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bded04 bytes 115e47f9
- 00bded08 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00bded08 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bded08 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bded08 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bded08 bytes 10e23a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-568e0146a18f0aae32a3a5259eef4e8d"></a>

### [`00bded20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded20.md) → [`00bdedd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md) _ZN8firebase26ReferenceCountedFutureImplD1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00afec10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec10.md) · 呼出先 1件 [`00afea18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md)
- 新版 呼出元 1件 [`00afecd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecd8.md) · 呼出先 1件 [`00afeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bded24",
      "READ",
      [
        "storage",
        "00c1dec8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bded2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afeae0"
      ]
    ]
  ],
  "added": [
    [
      "00bdedd4",
      "READ",
      [
        "storage",
        "00c1df78",
        null,
        "pointer"
      ]
    ],
    [
      "00bdeddc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00afeae0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bded20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded20.md#insn-00bded20) · [`00bded24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded20.md#insn-00bded24) · [`00bded28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded20.md#insn-00bded28)

~~~diff
- 00bded20 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bded20 bytes f00100f0
- 00bded24 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ec8:8"]]
- 00bded24 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bded24 bytes 116647f9
- 00bded28 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 00bded28 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bded28 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bded28 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bded28 bytes 10223b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64761e59d1487eefce260b6a89665a73"></a>

### [`00bded90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded90.md) → [`00bdee40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee40.md) _ZN8firebase16StaticFutureData26CleanupFutureDataForModuleEPKv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b5c790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5c/00b5c790.md) · 呼出先 1件 [`00b02154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02154.md)
- 新版 呼出元 1件 [`00b5c858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c858.md) · 呼出先 1件 [`00b0221c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b0221c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bded94",
      "READ",
      [
        "storage",
        "00c1df00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bded9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0221c"
      ]
    ]
  ],
  "added": [
    [
      "00bdee44",
      "READ",
      [
        "storage",
        "00c1dfb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdee4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0221c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bded90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded90.md#insn-00bded90) · [`00bded94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded90.md#insn-00bded94) · [`00bded98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded90.md#insn-00bded98)

~~~diff
- 00bded90 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bded90 bytes f00100f0
- 00bded94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f00:8"]]
- 00bded94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bded94 bytes 118247f9
- 00bded98 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 00bded98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bded98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bded98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bded98 bytes 10023c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce2d4dd0120bb11f3f94ed8a62c1d755"></a>

### [`00bdee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md) → [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) _ZdaPv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`00b030f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b030f8.md) [`00b0ce34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0ce34.md) [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) [`00b2e528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e528.md) [`00b47a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47a90.md) · 呼出先 1件 [`00bd4e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4e1c.md)
- 新版 呼出元 16件 [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) [`00b0cefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cefc.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b2e5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e5f0.md) [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md) · 呼出先 1件 [`00bd4ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4ee4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdee94",
      "READ",
      [
        "storage",
        "00c1df80",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdee9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4ee4"
      ]
    ]
  ],
  "added": [
    [
      "00bdef44",
      "READ",
      [
        "storage",
        "00c1e030",
        null,
        "pointer"
      ]
    ],
    [
      "00bdef4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00bd4ee4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md#insn-00bdee90) · [`00bdee94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md#insn-00bdee94) · [`00bdee98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md#insn-00bdee98)

~~~diff
- 00bdee90 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdee90 bytes f00100f0
- 00bdee94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:f80:8"]]
- 00bdee94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdee94 bytes 11c247f9
- 00bdee98 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 00bdee98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdee98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdee98 bytes 10023e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa5047f44cfa779b26dbc037cb43892d"></a>

### [`00bdef70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef70.md) → [`00bdf020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf020.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4c3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md) · 呼出先 1件 [`00b0dba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dba8.md)
- 新版 呼出元 1件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) · 呼出先 1件 [`00b0dc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdef74",
      "READ",
      [
        "storage",
        "00c1dff0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdef7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0dc70"
      ]
    ]
  ],
  "added": [
    [
      "00bdf024",
      "READ",
      [
        "storage",
        "00c1e0a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf02c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0dc70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdef70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef70.md#insn-00bdef70) · [`00bdef74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef70.md#insn-00bdef74) · [`00bdef78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef70.md#insn-00bdef78)

~~~diff
- 00bdef70 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdef70 bytes f00100f0
- 00bdef74 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ff0:8"]]
- 00bdef74 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdef74 bytes 11fa47f9
- 00bdef78 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00bdef78 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef78 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef78 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdef78 bytes 10c23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279a51695bf8222693527cde39aa81eb"></a>

### [`00bdef80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef80.md) → [`00bdf030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf030.md) _ZN20google_play_services23MakeAvailableLastResultEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b0de68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md) · 呼出先 1件 [`00b0e08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e08c.md)
- 新版 呼出元 1件 [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) · 呼出先 1件 [`00b0e154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e154.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdef84",
      "READ",
      [
        "storage",
        "00c1dff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdef8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0e154"
      ]
    ]
  ],
  "added": [
    [
      "00bdf034",
      "READ",
      [
        "storage",
        "00c1e0a8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf03c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b0e154"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdef80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef80.md#insn-00bdef80) · [`00bdef84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef80.md#insn-00bdef84) · [`00bdef88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef80.md#insn-00bdef88)

~~~diff
- 00bdef80 ["COPY", "register:4080:8", ["const:c1d000:8"]]
- 00bdef80 bytes f00100f0
- 00bdef84 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ff8:8"]]
- 00bdef84 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdef84 bytes 11fe47f9
- 00bdef88 ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00bdef88 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef88 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdef88 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdef88 bytes 10e23f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c016c55cbb2e9404559ba12d3d8740fd"></a>

### [`00bdf000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf000.md) → [`00bdf0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0b0.md) _ZN10reflection12FieldBuilder12add_requiredEb

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md) · 呼出先 1件 [`00b34b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34b3c.md)
- 新版 呼出元 1件 [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) · 呼出先 1件 [`00b34c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34c04.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf004",
      "READ",
      [
        "storage",
        "00c1e038",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf00c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34c04"
      ]
    ]
  ],
  "added": [
    [
      "00bdf0b4",
      "READ",
      [
        "storage",
        "00c1e0e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf0bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34c04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf000.md#insn-00bdf000) · [`00bdf004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf000.md#insn-00bdf004) · [`00bdf008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf000.md#insn-00bdf008)

~~~diff
- 00bdf000 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf000 bytes f00100f0
- 00bdf004 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:38:8"]]
- 00bdf004 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf004 bytes 111e40f9
- 00bdf008 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00bdf008 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf008 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf008 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf008 bytes 10e20091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37924e698a06e7413099856e5981f804"></a>

### [`00bdf010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf010.md) → [`00bdf0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf0c0.md) _ZN10reflection12FieldBuilder14add_deprecatedEb

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md) · 呼出先 1件 [`00b34c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34c04.md)
- 新版 呼出元 1件 [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) · 呼出先 1件 [`00b34ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ccc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf014",
      "READ",
      [
        "storage",
        "00c1e040",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf01c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34ccc"
      ]
    ]
  ],
  "added": [
    [
      "00bdf0c4",
      "READ",
      [
        "storage",
        "00c1e0f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf0cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34ccc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf010.md#insn-00bdf010) · [`00bdf014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf010.md#insn-00bdf014) · [`00bdf018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf010.md#insn-00bdf018)

~~~diff
- 00bdf010 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf010 bytes f00100f0
- 00bdf014 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:40:8"]]
- 00bdf014 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf014 bytes 112240f9
- 00bdf018 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00bdf018 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf018 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf018 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf018 bytes 10020191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cb18bacc8eec334e8dc74789cffe869"></a>

### [`00bdf140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf140.md) → [`00bdf1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1f0.md) _ZN11flatbuffers11SymbolTableINS_7EnumValEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b254d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b25/00b254d8.md) [`00b2bde4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2bde4.md) · 呼出先 1件 [`00b2c2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c2e4.md)
- 新版 呼出元 2件 [`00b255a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b255a0.md) [`00b2beac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2beac.md) · 呼出先 1件 [`00b2c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf144",
      "READ",
      [
        "storage",
        "00c1e0d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf14c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2c3ac"
      ]
    ]
  ],
  "added": [
    [
      "00bdf1f4",
      "READ",
      [
        "storage",
        "00c1e188",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf1fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2c3ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf140.md#insn-00bdf140) · [`00bdf144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf140.md#insn-00bdf144) · [`00bdf148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf140.md#insn-00bdf148)

~~~diff
- 00bdf140 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf140 bytes f00100f0
- 00bdf144 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:d8:8"]]
- 00bdf144 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf144 bytes 116e40f9
- 00bdf148 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00bdf148 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf148 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf148 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf148 bytes 10620391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3098156c3bf82e5d19b01a696f2090fe"></a>

### [`00bdf1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf1e0.md) → [`00bdf290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf290.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE2EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2eea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2eea8.md) · 呼出先 1件 [`00b2f278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2f278.md)
- 新版 呼出元 1件 [`00b2ef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md) · 呼出先 1件 [`00b2f340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf1e4",
      "READ",
      [
        "storage",
        "00c1e128",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf1ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f340"
      ]
    ]
  ],
  "added": [
    [
      "00bdf294",
      "READ",
      [
        "storage",
        "00c1e1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf29c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f340"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf1e0.md#insn-00bdf1e0) · [`00bdf1e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf1e0.md#insn-00bdf1e4) · [`00bdf1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf1e0.md#insn-00bdf1e8)

~~~diff
- 00bdf1e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf1e0 bytes f00100f0
- 00bdf1e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:128:8"]]
- 00bdf1e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf1e4 bytes 119640f9
- 00bdf1e8 ["COPY", "tmp:0:8", ["const:128:8"]]
- 00bdf1e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf1e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf1e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf1e8 bytes 10a20491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c473d14cb54143948e7a520006b853b6"></a>

### [`00bdf200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf200.md) → [`00bdf2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2b0.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE4EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2eea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2eea8.md) · 呼出先 1件 [`00b2f6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2f6e4.md)
- 新版 呼出元 1件 [`00b2ef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md) · 呼出先 1件 [`00b2f7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf204",
      "READ",
      [
        "storage",
        "00c1e138",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf20c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f7ac"
      ]
    ]
  ],
  "added": [
    [
      "00bdf2b4",
      "READ",
      [
        "storage",
        "00c1e1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf2bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2f7ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf200.md#insn-00bdf200) · [`00bdf204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf200.md#insn-00bdf204) · [`00bdf208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf200.md#insn-00bdf208)

~~~diff
- 00bdf200 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf200 bytes f00100f0
- 00bdf204 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:138:8"]]
- 00bdf204 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf204 bytes 119e40f9
- 00bdf208 ["COPY", "tmp:0:8", ["const:138:8"]]
- 00bdf208 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf208 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf208 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf208 bytes 10e20491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c382efc98ed7ebcca41812861a38fd07"></a>

### [`00bdf2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2c0.md) → [`00bdf370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf370.md) _ZN11flatbuffers17FlatBufferBuilder10AddElementItEEvtT_S2_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b17054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md) [`00b2afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md) [`00b2c5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c5c0.md) · 呼出先 1件 [`00b1b028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b028.md)
- 新版 呼出元 3件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) [`00b2c688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c688.md) · 呼出先 1件 [`00b1b0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b0f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf2c4",
      "READ",
      [
        "storage",
        "00c1e198",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf2cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1b0f0"
      ]
    ]
  ],
  "added": [
    [
      "00bdf374",
      "READ",
      [
        "storage",
        "00c1e248",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf37c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1b0f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2c0.md#insn-00bdf2c0) · [`00bdf2c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2c0.md#insn-00bdf2c4) · [`00bdf2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf2c0.md#insn-00bdf2c8)

~~~diff
- 00bdf2c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf2c0 bytes f00100f0
- 00bdf2c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:198:8"]]
- 00bdf2c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf2c4 bytes 11ce40f9
- 00bdf2c8 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00bdf2c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf2c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf2c8 bytes 10620691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03e3fde28f7d9a7bb03d342731d6446"></a>

### [`00bdf320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf320.md) → [`00bdf3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3d0.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection7ServiceEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2883c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b28/00b2883c.md) · 呼出先 1件 [`00b3e8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3e/00b3e8d4.md)
- 新版 呼出元 1件 [`00b28904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md) · 呼出先 1件 [`00b3e99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3e/00b3e99c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf324",
      "READ",
      [
        "storage",
        "00c1e1c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf32c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3e99c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf3d4",
      "READ",
      [
        "storage",
        "00c1e278",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf3dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3e99c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf320.md#insn-00bdf320) · [`00bdf324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf320.md#insn-00bdf324) · [`00bdf328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf320.md#insn-00bdf328)

~~~diff
- 00bdf320 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf320 bytes f00100f0
- 00bdf324 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1c8:8"]]
- 00bdf324 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf324 bytes 11e640f9
- 00bdf328 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00bdf328 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf328 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf328 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf328 bytes 10220791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40f37482c252cbd3f9437a2b30fcee23"></a>

### [`00bdf330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf330.md) → [`00bdf3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf3e0.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIN10reflection8KeyValueEEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b29b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b29/00b29b48.md) · 呼出先 1件 [`00b39c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39c34.md)
- 新版 呼出元 1件 [`00b29c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29c10.md) · 呼出先 1件 [`00b39cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39cfc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf334",
      "READ",
      [
        "storage",
        "00c1e1d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf33c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b39cfc"
      ]
    ]
  ],
  "added": [
    [
      "00bdf3e4",
      "READ",
      [
        "storage",
        "00c1e280",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf3ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b39cfc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf330.md#insn-00bdf330) · [`00bdf334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf330.md#insn-00bdf334) · [`00bdf338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf330.md#insn-00bdf338)

~~~diff
- 00bdf330 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf330 bytes f00100f0
- 00bdf334 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1d0:8"]]
- 00bdf334 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf334 bytes 11ea40f9
- 00bdf338 ["COPY", "tmp:0:8", ["const:1d0:8"]]
- 00bdf338 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf338 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf338 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf338 bytes 10420791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee759b35327c98c25c23669b4c957138"></a>

### [`00bdf360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf360.md) → [`00bdf410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf410.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIfEEjT_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b17054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md) [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) · 呼出先 1件 [`00b1c364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c364.md)
- 新版 呼出元 3件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1c42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c42c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf364",
      "READ",
      [
        "storage",
        "00c1e1e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf36c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c42c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf414",
      "READ",
      [
        "storage",
        "00c1e298",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf41c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c42c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf360.md#insn-00bdf360) · [`00bdf364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf360.md#insn-00bdf364) · [`00bdf368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf360.md#insn-00bdf368)

~~~diff
- 00bdf360 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf360 bytes f00100f0
- 00bdf364 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1e8:8"]]
- 00bdf364 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf364 bytes 11f640f9
- 00bdf368 ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00bdf368 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf368 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf368 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf368 bytes 10a20791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2eba183f19d19f72bceeb83b975ae4f"></a>

### [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md) → [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIjEEjT_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 34件 [`00b17054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md) [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) [`00b1c720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c720.md) [`00b1cb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cb78.md) · 呼出先 1件 [`00b1b6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b6a8.md)
- 新版 呼出元 34件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b1c7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c7e8.md) [`00b1cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cc40.md) · 呼出先 1件 [`00b1b770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b770.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf384",
      "READ",
      [
        "storage",
        "00c1e1f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf38c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1b770"
      ]
    ]
  ],
  "added": [
    [
      "00bdf434",
      "READ",
      [
        "storage",
        "00c1e2a8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf43c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1b770"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md#insn-00bdf380) · [`00bdf384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md#insn-00bdf384) · [`00bdf388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md#insn-00bdf388)

~~~diff
- 00bdf380 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf380 bytes f00100f0
- 00bdf384 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:1f8:8"]]
- 00bdf384 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf384 bytes 11fe40f9
- 00bdf388 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 00bdf388 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf388 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf388 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf388 bytes 10e20791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b72600675c1f22aad4f8f9ce0cc35206"></a>

### [`00bdf390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf390.md) → [`00bdf440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf440.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIlEEjT_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b17054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md) [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) [`00b2afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md) [`00b2c49c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c49c.md) · 呼出先 1件 [`00b1bb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bb74.md)
- 新版 呼出元 5件 [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) [`00b2c564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c564.md) · 呼出先 1件 [`00b1bc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bc3c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf394",
      "READ",
      [
        "storage",
        "00c1e200",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf39c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1bc3c"
      ]
    ]
  ],
  "added": [
    [
      "00bdf444",
      "READ",
      [
        "storage",
        "00c1e2b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf44c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1bc3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf390.md#insn-00bdf390) · [`00bdf394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf390.md#insn-00bdf394) · [`00bdf398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf390.md#insn-00bdf398)

~~~diff
- 00bdf390 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf390 bytes f00100f0
- 00bdf394 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:200:8"]]
- 00bdf394 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf394 bytes 110241f9
- 00bdf398 ["COPY", "tmp:0:8", ["const:200:8"]]
- 00bdf398 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf398 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf398 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf398 bytes 10020891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cafdecf2b499f12c42c743e8f55f3570"></a>

### [`00bdf3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3b0.md) → [`00bdf460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf460.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIvEEjNS_6OffsetIT_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) · 呼出先 1件 [`00b1cb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cb78.md)
- 新版 呼出元 2件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1cc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cc40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf3b4",
      "READ",
      [
        "storage",
        "00c1e210",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf3bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1cc40"
      ]
    ]
  ],
  "added": [
    [
      "00bdf464",
      "READ",
      [
        "storage",
        "00c1e2c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf46c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1cc40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3b0.md#insn-00bdf3b0) · [`00bdf3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3b0.md#insn-00bdf3b4) · [`00bdf3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3b0.md#insn-00bdf3b8)

~~~diff
- 00bdf3b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf3b0 bytes f00100f0
- 00bdf3b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:210:8"]]
- 00bdf3b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf3b4 bytes 110a41f9
- 00bdf3b8 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00bdf3b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf3b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf3b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf3b8 bytes 10420891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2d9b1dd96b9c53f0b6af9563dd39048"></a>

### [`00bdf3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3e0.md) → [`00bdf490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf490.md) _ZN11flatbuffers17FlatBufferBuilder12CreateVectorIhEENS_6OffsetINS_6VectorIT_EEEERKNSt6__ndk16vectorIS4_NS7_9allocatorIS4_EEEE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b3fbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3fbc0.md) · 呼出先 1件 [`00b40260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40260.md)
- 新版 呼出元 1件 [`00b3fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fc88.md) · 呼出先 1件 [`00b40328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40328.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf3e4",
      "READ",
      [
        "storage",
        "00c1e228",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf3ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b40328"
      ]
    ]
  ],
  "added": [
    [
      "00bdf494",
      "READ",
      [
        "storage",
        "00c1e2d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf49c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b40328"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3e0.md#insn-00bdf3e0) · [`00bdf3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3e0.md#insn-00bdf3e4) · [`00bdf3e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf3e0.md#insn-00bdf3e8)

~~~diff
- 00bdf3e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf3e0 bytes f00100f0
- 00bdf3e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:228:8"]]
- 00bdf3e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf3e4 bytes 111641f9
- 00bdf3e8 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00bdf3e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf3e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf3e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf3e8 bytes 10a20891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d7db60b48c7ef016f36b0464c2413a4"></a>

### [`00bdf490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf490.md) → [`00bdf540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf540.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7RPCCallEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b296a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b29/00b296a4.md) · 呼出先 1件 [`00b34e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b34e10.md)
- 新版 呼出元 1件 [`00b2976c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b2976c.md) · 呼出先 1件 [`00b34ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b34ed8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf494",
      "READ",
      [
        "storage",
        "00c1e280",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf49c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34ed8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf544",
      "READ",
      [
        "storage",
        "00c1e330",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf54c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b34ed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf490.md#insn-00bdf490) · [`00bdf494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf490.md#insn-00bdf494) · [`00bdf498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf490.md#insn-00bdf498)

~~~diff
- 00bdf490 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf490 bytes f00100f0
- 00bdf494 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:280:8"]]
- 00bdf494 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf494 bytes 114241f9
- 00bdf498 ["COPY", "tmp:0:8", ["const:280:8"]]
- 00bdf498 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf498 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf498 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf498 bytes 10020a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aa681bbc7b3ca87f313ff77f6381e14"></a>

### [`00bdf4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4a0.md) → [`00bdf550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf550.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection7ServiceEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2883c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b28/00b2883c.md) · 呼出先 1件 [`00b33ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33ebc.md)
- 新版 呼出元 1件 [`00b28904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md) · 呼出先 1件 [`00b33f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33f84.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf4a4",
      "READ",
      [
        "storage",
        "00c1e288",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf4ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b33f84"
      ]
    ]
  ],
  "added": [
    [
      "00bdf554",
      "READ",
      [
        "storage",
        "00c1e338",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf55c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b33f84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4a0.md#insn-00bdf4a0) · [`00bdf4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4a0.md#insn-00bdf4a4) · [`00bdf4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4a0.md#insn-00bdf4a8)

~~~diff
- 00bdf4a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf4a0 bytes f00100f0
- 00bdf4a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:288:8"]]
- 00bdf4a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf4a4 bytes 114641f9
- 00bdf4a8 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00bdf4a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf4a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf4a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf4a8 bytes 10220a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d574dddbb21a0d8b345b92cbea20e6ff"></a>

### [`00bdf4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4b0.md) → [`00bdf560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf560.md) _ZN11flatbuffers17FlatBufferBuilder9AddOffsetINS_6VectorINS_6OffsetIN10reflection8KeyValueEEEEEEEvtNS3_IT_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b29390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b29/00b29390.md) [`00b296a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b29/00b296a4.md) [`00b29f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b29/00b29f9c.md) [`00b2afe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2afe0.md) [`00b2b59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2b59c.md) · 呼出先 1件 [`00b347ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b34/00b347ec.md)
- 新版 呼出元 5件 [`00b29458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29458.md) [`00b2976c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b2976c.md) [`00b2a064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a064.md) [`00b2b0a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b0a8.md) [`00b2b664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b664.md) · 呼出先 1件 [`00b348b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b34/00b348b4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf4b4",
      "READ",
      [
        "storage",
        "00c1e290",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf4bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b348b4"
      ]
    ]
  ],
  "added": [
    [
      "00bdf564",
      "READ",
      [
        "storage",
        "00c1e340",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf56c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b348b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4b0.md#insn-00bdf4b0) · [`00bdf4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4b0.md#insn-00bdf4b4) · [`00bdf4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4b0.md#insn-00bdf4b8)

~~~diff
- 00bdf4b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf4b0 bytes f00100f0
- 00bdf4b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:290:8"]]
- 00bdf4b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf4b4 bytes 114a41f9
- 00bdf4b8 ["COPY", "tmp:0:8", ["const:290:8"]]
- 00bdf4b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf4b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf4b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf4b8 bytes 10420a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea08b4a79c08a9434cee0090325915c1"></a>

### [`00bdf4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4e0.md) → [`00bdf590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf590.md) _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b14dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14dc8.md) [`00b1b794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b794.md) [`00b20aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20aec.md) · 呼出先 1件 [`00b2ed90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2ed90.md)
- 新版 呼出元 3件 [`00b14e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md) [`00b1b85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md) [`00b20bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md) · 呼出先 1件 [`00b2ee58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ee58.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf4e4",
      "READ",
      [
        "storage",
        "00c1e2a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf4ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2ee58"
      ]
    ]
  ],
  "added": [
    [
      "00bdf594",
      "READ",
      [
        "storage",
        "00c1e358",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf59c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2ee58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4e0.md#insn-00bdf4e0) · [`00bdf4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4e0.md#insn-00bdf4e4) · [`00bdf4e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4e0.md#insn-00bdf4e8)

~~~diff
- 00bdf4e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf4e0 bytes f00100f0
- 00bdf4e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2a8:8"]]
- 00bdf4e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf4e4 bytes 115641f9
- 00bdf4e8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00bdf4e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf4e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf4e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf4e8 bytes 10a20a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbaab01240eaa01f451c441a69372e86"></a>

### [`00bdf500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf500.md) → [`00bdf5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5b0.md) _ZN11flatbuffers20TypeToIntervalStringIaEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1a230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a230.md) [`00b2f4ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2f4ac.md) · 呼出先 1件 [`00b307f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b30/00b307f0.md)
- 新版 呼出元 2件 [`00b1a2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md) [`00b2f574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md) · 呼出先 1件 [`00b308b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b308b8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf504",
      "READ",
      [
        "storage",
        "00c1e2b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf50c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b308b8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf5b4",
      "READ",
      [
        "storage",
        "00c1e368",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf5bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b308b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf500.md#insn-00bdf500) · [`00bdf504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf500.md#insn-00bdf504) · [`00bdf508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf500.md#insn-00bdf508)

~~~diff
- 00bdf500 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf500 bytes f00100f0
- 00bdf504 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2b8:8"]]
- 00bdf504 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf504 bytes 115e41f9
- 00bdf508 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00bdf508 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf508 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf508 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf508 bytes 10e20a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4dd1bbd0cdcbba6ef07453140741b7b"></a>

### [`00bdf510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf510.md) → [`00bdf5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5c0.md) _ZN11flatbuffers20TypeToIntervalStringIhEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b16bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16bc0.md) [`00b2f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2f044.md) [`00b2f278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2f278.md) [`00b2f6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2f6e4.md) · 呼出先 1件 [`00b30650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b30/00b30650.md)
- 新版 呼出元 4件 [`00b16c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md) [`00b2f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f10c.md) [`00b2f340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md) [`00b2f7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md) · 呼出先 1件 [`00b30718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30718.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf514",
      "READ",
      [
        "storage",
        "00c1e2c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf51c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30718"
      ]
    ]
  ],
  "added": [
    [
      "00bdf5c4",
      "READ",
      [
        "storage",
        "00c1e370",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf5cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30718"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf510.md#insn-00bdf510) · [`00bdf514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf510.md#insn-00bdf514) · [`00bdf518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf510.md#insn-00bdf518)

~~~diff
- 00bdf510 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf510 bytes f00100f0
- 00bdf514 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2c0:8"]]
- 00bdf514 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf514 bytes 116241f9
- 00bdf518 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00bdf518 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf518 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf518 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf518 bytes 10020b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e70c54f58c0175b255aa1a32a5bb58"></a>

### [`00bdf530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf530.md) → [`00bdf5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5e0.md) _ZN11flatbuffers20TypeToIntervalStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b16328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16328.md) [`00b2ffc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2ffc0.md) · 呼出先 1件 [`00b30e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b30/00b30e70.md)
- 新版 呼出元 2件 [`00b163f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md) [`00b30088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30088.md) · 呼出先 1件 [`00b30f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30f38.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bdf5e4",
      "READ",
      [
        "storage",
        "00c1e2d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf53c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30f38"
      ]
    ]
  ],
  "added": [
    [
      "00bdf5e4",
      "READ",
      [
        "storage",
        "00c1e380",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf5ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf530.md#insn-00bdf534) · [`00bdf538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf530.md#insn-00bdf538) · [`00bdf53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf530.md#insn-00bdf53c)
- 新版 `00bdf5e4`（命令位置の公開資料なし）

~~~diff
- 00bdf534 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2d0:8"]]
- 00bdf534 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bdf5e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:380:8"]]
+ 00bdf5e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf534 bytes 116a41f9
+ 00bdf5e4 bytes 11c241f9
- 00bdf538 ["COPY", "tmp:0:8", ["const:2d0:8"]]
- 00bdf538 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf538 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf538 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf538 bytes 10420b91
- 00bdf53c ["COPY", "register:0:8", ["register:4088:8"]]
- 00bdf53c ["BRANCHIND", null, ["register:0:8"]]
- 00bdf53c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d70be317c81ccbe6c6541c09b0b75e5d"></a>

### [`00bdf550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf550.md) → [`00bdf600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf600.md) _ZN11flatbuffers20TypeToIntervalStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1bc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bc60.md) [`00b30424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b30/00b30424.md) · 呼出先 1件 [`00b311b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b31/00b311b0.md)
- 新版 呼出元 2件 [`00b1bd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md) [`00b304ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b304ec.md) · 呼出先 1件 [`00b31278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31278.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf554",
      "READ",
      [
        "storage",
        "00c1e2e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf55c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b31278"
      ]
    ]
  ],
  "added": [
    [
      "00bdf604",
      "READ",
      [
        "storage",
        "00c1e390",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf60c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b31278"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf550.md#insn-00bdf550) · [`00bdf554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf550.md#insn-00bdf554) · [`00bdf558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf550.md#insn-00bdf558)

~~~diff
- 00bdf550 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf550 bytes f00100f0
- 00bdf554 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2e0:8"]]
- 00bdf554 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf554 bytes 117241f9
- 00bdf558 ["COPY", "tmp:0:8", ["const:2e0:8"]]
- 00bdf558 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf558 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf558 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf558 bytes 10820b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49aac941c1d6d0ec7f6d2a624fb0a7d0"></a>

### [`00bdf570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf570.md) → [`00bdf620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf620.md) _ZN11flatbuffers20TypeToIntervalStringItEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1abd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1abd4.md) [`00b2fb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2f/00b2fb50.md) · 呼出先 1件 [`00b30b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b30/00b30b30.md)
- 新版 呼出元 2件 [`00b1ac9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md) [`00b2fc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fc18.md) · 呼出先 1件 [`00b30bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30bf8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf574",
      "READ",
      [
        "storage",
        "00c1e2f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf57c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30bf8"
      ]
    ]
  ],
  "added": [
    [
      "00bdf624",
      "READ",
      [
        "storage",
        "00c1e3a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf62c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b30bf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf570.md#insn-00bdf570) · [`00bdf574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf570.md#insn-00bdf574) · [`00bdf578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf570.md#insn-00bdf578)

~~~diff
- 00bdf570 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf570 bytes f00100f0
- 00bdf574 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:2f0:8"]]
- 00bdf574 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf574 bytes 117a41f9
- 00bdf578 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00bdf578 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf578 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf578 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf578 bytes 10c20b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dec08ec2378ddefeae32a39cd747245"></a>

### [`00bdf5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5b0.md) → [`00bdf660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md) _ZN11flatbuffers4atotIfEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b13d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b13/00b13d30.md) [`00b17054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md) [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) · 呼出先 1件 [`00b1c17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c17c.md)
- 新版 呼出元 4件 [`00b13df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md) [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) · 呼出先 1件 [`00b1c244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdf5b4",
      "READ",
      [
        "storage",
        "00c1e310",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdf5bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c244"
      ]
    ]
  ],
  "added": [
    [
      "00bdf664",
      "READ",
      [
        "storage",
        "00c1e3c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdf66c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b1c244"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdf5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5b0.md#insn-00bdf5b0) · [`00bdf5b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5b0.md#insn-00bdf5b4) · [`00bdf5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5b0.md#insn-00bdf5b8)

~~~diff
- 00bdf5b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdf5b0 bytes f00100f0
- 00bdf5b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:310:8"]]
- 00bdf5b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdf5b4 bytes 118a41f9
- 00bdf5b8 ["COPY", "tmp:0:8", ["const:310:8"]]
- 00bdf5b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdf5b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdf5b8 bytes 10420c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d4e462835acbeaf77d303696c95fab4"></a>

### [`00bdfbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbd0.md) → [`00bdfc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc80.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_valu

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00b11350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11350.md) [`00b115bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b115bc.md) [`00b22f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b22/00b22f20.md) [`00b2aa3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2a/00b2aa3c.md) [`00b2b6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2b/00b2b6b0.md) · 呼出先 1件 [`00b3f044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3f044.md)
- 新版 呼出元 7件 [`00b11418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11418.md) [`00b11684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md) [`00b22fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22fe8.md) [`00b2ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2ab04.md) [`00b2b778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b778.md) · 呼出先 1件 [`00b3f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3f10c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfbd4",
      "READ",
      [
        "storage",
        "00c1e620",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfbdc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3f10c"
      ]
    ]
  ],
  "added": [
    [
      "00bdfc84",
      "READ",
      [
        "storage",
        "00c1e6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfc8c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3f10c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbd0.md#insn-00bdfbd0) · [`00bdfbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbd0.md#insn-00bdfbd4) · [`00bdfbd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbd0.md#insn-00bdfbd8)

~~~diff
- 00bdfbd0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfbd0 bytes f00100f0
- 00bdfbd4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:620:8"]]
- 00bdfbd4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfbd4 bytes 111243f9
- 00bdfbd8 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00bdfbd8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfbd8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfbd8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfbd8 bytes 10821891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-182c976ae52cfc7fa3f220fcfedbcd94"></a>

### [`00bdfbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbe0.md) → [`00bdfc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfc90.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b29b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b29/00b29b48.md) · 呼出先 1件 [`00b4636c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b4636c.md)
- 新版 呼出元 1件 [`00b29c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b29/00b29c10.md) · 呼出先 1件 [`00b46434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46434.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfbe4",
      "READ",
      [
        "storage",
        "00c1e628",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfbec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46434"
      ]
    ]
  ],
  "added": [
    [
      "00bdfc94",
      "READ",
      [
        "storage",
        "00c1e6d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfc9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46434"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfbe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbe0.md#insn-00bdfbe0) · [`00bdfbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbe0.md#insn-00bdfbe4) · [`00bdfbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfbe0.md#insn-00bdfbe8)

~~~diff
- 00bdfbe0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfbe0 bytes f00100f0
- 00bdfbe4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:628:8"]]
- 00bdfbe4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfbe4 bytes 111643f9
- 00bdfbe8 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00bdfbe8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfbe8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfbe8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfbe8 bytes 10a21891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f9fe4537d13d9ef7c945db05fd6ad9b"></a>

### [`00bdfd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd20.md) → [`00bdfdd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfdd0.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b42fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42fb4.md) · 呼出先 1件 [`00b438b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b43/00b438b4.md)
- 新版 呼出元 1件 [`00b4307c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4307c.md) · 呼出先 1件 [`00b4397c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b43/00b4397c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfd24",
      "READ",
      [
        "storage",
        "00c1e6c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfd2c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4397c"
      ]
    ]
  ],
  "added": [
    [
      "00bdfdd4",
      "READ",
      [
        "storage",
        "00c1e778",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfddc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4397c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd20.md#insn-00bdfd20) · [`00bdfd24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd20.md#insn-00bdfd24) · [`00bdfd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfd20.md#insn-00bdfd28)

~~~diff
- 00bdfd20 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfd20 bytes f00100f0
- 00bdfd24 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:6c8:8"]]
- 00bdfd24 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfd24 bytes 116643f9
- 00bdfd28 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00bdfd28 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfd28 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfd28 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfd28 bytes 10221b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb3ed97c11d8ba2a188dd8bcaccb16a"></a>

### [`00bdfdc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfdc0.md) → [`00bdfe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe70.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b28e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b28/00b28e9c.md) [`00b44938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44938.md) · 呼出先 1件 [`00b44938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44938.md)
- 新版 呼出元 2件 [`00b28f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md) [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md) · 呼出先 1件 [`00b44a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b44a00.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfdc4",
      "READ",
      [
        "storage",
        "00c1e718",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfdcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b44a00"
      ]
    ]
  ],
  "added": [
    [
      "00bdfe74",
      "READ",
      [
        "storage",
        "00c1e7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdfe7c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b44a00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfdc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfdc0.md#insn-00bdfdc0) · [`00bdfdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfdc0.md#insn-00bdfdc4) · [`00bdfdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfdc0.md#insn-00bdfdc8)

~~~diff
- 00bdfdc0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfdc0 bytes f00100f0
- 00bdfdc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:718:8"]]
- 00bdfdc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfdc4 bytes 118e43f9
- 00bdfdc8 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00bdfdc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfdc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfdc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfdc8 bytes 10621c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16bb747a1f3da91a1b156749061af5b"></a>

### [`00bdfe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe90.md) → [`00bdff40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff40.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2c2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c2e4.md) · 呼出先 1件 [`00b42c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42c20.md)
- 新版 呼出元 1件 [`00b2c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md) · 呼出先 1件 [`00b42ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42ce8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfe94",
      "READ",
      [
        "storage",
        "00c1e780",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfe9c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b42ce8"
      ]
    ]
  ],
  "added": [
    [
      "00bdff44",
      "READ",
      [
        "storage",
        "00c1e830",
        null,
        "pointer"
      ]
    ],
    [
      "00bdff4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b42ce8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe90.md#insn-00bdfe90) · [`00bdfe94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe90.md#insn-00bdfe94) · [`00bdfe98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfe90.md#insn-00bdfe98)

~~~diff
- 00bdfe90 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfe90 bytes f00100f0
- 00bdfe94 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:780:8"]]
- 00bdfe94 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfe94 bytes 11c243f9
- 00bdfe98 ["COPY", "tmp:0:8", ["const:780:8"]]
- 00bdfe98 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe98 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfe98 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfe98 bytes 10021e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dcc069d46e7f8ee9113e360e8ad133d"></a>

### [`00bdfea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfea0.md) → [`00bdff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdff50.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_c

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2c2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2c/00b2c2e4.md) · 呼出先 1件 [`00b42b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42b0c.md)
- 新版 呼出元 1件 [`00b2c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c3ac.md) · 呼出先 1件 [`00b42bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b42bd4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfea4",
      "READ",
      [
        "storage",
        "00c1e788",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfeac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b42bd4"
      ]
    ]
  ],
  "added": [
    [
      "00bdff54",
      "READ",
      [
        "storage",
        "00c1e838",
        null,
        "pointer"
      ]
    ],
    [
      "00bdff5c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b42bd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfea0.md#insn-00bdfea0) · [`00bdfea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfea0.md#insn-00bdfea4) · [`00bdfea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfea0.md#insn-00bdfea8)

~~~diff
- 00bdfea0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfea0 bytes f00100f0
- 00bdfea4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:788:8"]]
- 00bdfea4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfea4 bytes 11c643f9
- 00bdfea8 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00bdfea8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfea8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfea8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfea8 bytes 10221e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac356f991a0548739f57dcf84bdf344"></a>

### [`00bdffc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffc0.md) → [`00be0070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0070.md) _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_co

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1cedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cedc.md) · 呼出先 1件 [`00b2eb24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2eb24.md)
- 新版 呼出元 1件 [`00b1cfa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md) · 呼出先 1件 [`00b2ebec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ebec.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdffc4",
      "READ",
      [
        "storage",
        "00c1e818",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdffcc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2ebec"
      ]
    ]
  ],
  "added": [
    [
      "00be0074",
      "READ",
      [
        "storage",
        "00c1e8c8",
        null,
        "pointer"
      ]
    ],
    [
      "00be007c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b2ebec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdffc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffc0.md#insn-00bdffc0) · [`00bdffc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffc0.md#insn-00bdffc4) · [`00bdffc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffc0.md#insn-00bdffc8)

~~~diff
- 00bdffc0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdffc0 bytes f00100f0
- 00bdffc4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:818:8"]]
- 00bdffc4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdffc4 bytes 110e44f9
- 00bdffc8 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00bdffc8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdffc8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdffc8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdffc8 bytes 10622091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b3a8e54a774a670ff3055c246b5734"></a>

### [`00bdffe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md) → [`00be0090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0090.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b261c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b26/00b261c4.md) [`00b3203c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b32/00b3203c.md) [`00b331b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b331b0.md) [`00b33b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33b54.md) [`00b44200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b44/00b44200.md) · 呼出先 1件 [`00b33600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b33/00b33600.md)
- 新版 呼出元 5件 [`00b2628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2628c.md) [`00b32104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b32/00b32104.md) [`00b33278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33278.md) [`00b33c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b33c1c.md) [`00b442c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b442c8.md) · 呼出先 1件 [`00b336c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b33/00b336c8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdffe4",
      "READ",
      [
        "storage",
        "00c1e828",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdffec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b336c8"
      ]
    ]
  ],
  "added": [
    [
      "00be0094",
      "READ",
      [
        "storage",
        "00c1e8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00be009c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b336c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdffe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md#insn-00bdffe4) · [`00bdffe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md#insn-00bdffe8) · [`00bdffec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdffe0.md#insn-00bdffec)

~~~diff
- 00bdffe4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:828:8"]]
- 00bdffe4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdffe4 bytes 111644f9
- 00bdffe8 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00bdffe8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdffe8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdffe8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdffe8 bytes 10a22091
- 00bdffec ["COPY", "register:0:8", ["register:4088:8"]]
- 00bdffec ["BRANCHIND", null, ["register:0:8"]]
- 00bdffec bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0984ed4747cb55ff345cbb3faa999c66"></a>

### [`00bdfff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md) → [`00be00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00a0.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b3c354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3c354.md) [`00b3cce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md) [`00b3d140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d140.md) [`00b3d2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3d/00b3d2dc.md) · 呼出先 1件 [`00b3ca98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3ca98.md)
- 新版 呼出元 4件 [`00b3c41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3c41c.md) [`00b3cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cdac.md) [`00b3d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d208.md) [`00b3d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3d/00b3d3a4.md) · 呼出先 1件 [`00b3cb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3c/00b3cb60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdfff4",
      "READ",
      [
        "storage",
        "00c1e830",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdfffc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3cb60"
      ]
    ]
  ],
  "added": [
    [
      "00be00a4",
      "READ",
      [
        "storage",
        "00c1e8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00be00ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3cb60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdfff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md#insn-00bdfff0) · [`00bdfff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md#insn-00bdfff4) · [`00bdfff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfff0.md#insn-00bdfff8)

~~~diff
- 00bdfff0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00bdfff0 bytes f00100f0
- 00bdfff4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:830:8"]]
- 00bdfff4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00bdfff4 bytes 111a44f9
- 00bdfff8 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00bdfff8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfff8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00bdfff8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00bdfff8 bytes 10c22091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59e299b18d16e7530491027b6efd83f2"></a>

### [`00be0000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0000.md) → [`00be00b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be00b0.md) _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b39d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b39/00b39d04.md) [`00b3a694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a694.md) [`00b3aaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3aaf0.md) [`00b3ac8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3ac8c.md) · 呼出先 1件 [`00b3a448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3a/00b3a448.md)
- 新版 呼出元 4件 [`00b39dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b39/00b39dcc.md) [`00b3a75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a75c.md) [`00b3abb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3abb8.md) [`00b3ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3ad54.md) · 呼出先 1件 [`00b3a510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3a/00b3a510.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0004",
      "READ",
      [
        "storage",
        "00c1e838",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be000c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3a510"
      ]
    ]
  ],
  "added": [
    [
      "00be00b4",
      "READ",
      [
        "storage",
        "00c1e8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00be00bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b3a510"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0000.md#insn-00be0004) · [`00be0008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0000.md#insn-00be0008) · [`00be000c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0000.md#insn-00be000c)

~~~diff
- 00be0004 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:838:8"]]
- 00be0004 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0004 bytes 111e44f9
- 00be0008 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00be0008 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0008 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0008 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0008 bytes 10e22091
- 00be000c ["COPY", "register:0:8", ["register:4088:8"]]
- 00be000c ["BRANCHIND", null, ["register:0:8"]]
- 00be000c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a13044dbd63ec7d14a0683bcc492cdba"></a>

### [`00be0110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0110.md) → [`00be01c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01c0.md) &lt;EXTERNAL&gt;::asin

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1e2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e2cc.md) · 呼出先 1件 [`010a5638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5638.md)
- 新版 呼出元 1件 [`00b1e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md) · 呼出先 1件 [`010a5638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5638.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0114",
      "READ",
      [
        "storage",
        "00c1e8c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be011c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5638"
      ]
    ]
  ],
  "added": [
    [
      "00be01c4",
      "READ",
      [
        "storage",
        "00c1e970",
        null,
        "pointer"
      ]
    ],
    [
      "00be01cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5638"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0110.md#insn-00be0110) · [`00be0114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0110.md#insn-00be0114) · [`00be0118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0110.md#insn-00be0118)

~~~diff
- 00be0110 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0110 bytes f00100d0
- 00be0114 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8c0:8"]]
- 00be0114 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0114 bytes 116244f9
- 00be0118 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00be0118 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0118 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0118 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0118 bytes 10022391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08bad0f8b686082f0fd614adc1eda9a4"></a>

### [`00be0140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0140.md) → [`00be01f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01f0.md) &lt;EXTERNAL&gt;::strpbrk

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b23eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b23/00b23eb0.md) · 呼出先 1件 [`010a5650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5650.md)
- 新版 呼出元 1件 [`00b23f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md) · 呼出先 1件 [`010a5650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5650.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0144",
      "READ",
      [
        "storage",
        "00c1e8d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be014c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5650"
      ]
    ]
  ],
  "added": [
    [
      "00be01f4",
      "READ",
      [
        "storage",
        "00c1e988",
        null,
        "pointer"
      ]
    ],
    [
      "00be01fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5650"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0140.md#insn-00be0140) · [`00be0144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0140.md#insn-00be0144) · [`00be0148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0140.md#insn-00be0148)

~~~diff
- 00be0140 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0140 bytes f00100d0
- 00be0144 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8d8:8"]]
- 00be0144 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0144 bytes 116e44f9
- 00be0148 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00be0148 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0148 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0148 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0148 bytes 10622391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb93d1a3fdb2254d85afc3e82e2728e9"></a>

### [`00be0150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0150.md) → [`00be0200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0200.md) &lt;EXTERNAL&gt;::strtoull

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b0f350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f350.md) [`00b2e174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2e174.md) [`00b78170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b78/00b78170.md) · 呼出先 1件 [`010a5658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5658.md)
- 新版 呼出元 3件 [`00b0f418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md) [`00b2e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2e23c.md) [`00b78238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b78/00b78238.md) · 呼出先 1件 [`010a5658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5658.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0154",
      "READ",
      [
        "storage",
        "00c1e8e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be015c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5658"
      ]
    ]
  ],
  "added": [
    [
      "00be0204",
      "READ",
      [
        "storage",
        "00c1e990",
        null,
        "pointer"
      ]
    ],
    [
      "00be020c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5658"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0150.md#insn-00be0150) · [`00be0154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0150.md#insn-00be0154) · [`00be0158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0150.md#insn-00be0158)

~~~diff
- 00be0150 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0150 bytes f00100d0
- 00be0154 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e0:8"]]
- 00be0154 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0154 bytes 117244f9
- 00be0158 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00be0158 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0158 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0158 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0158 bytes 10822391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-336e1c1425a8ea79dfcd83e2e412282b"></a>

### [`00be0160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0160.md) → [`00be0210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0210.md) &lt;EXTERNAL&gt;::toupper

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b0e204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e204.md) [`00b0e470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e470.md) · 呼出先 1件 [`010a5660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5660.md)
- 新版 呼出元 2件 [`00b0e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e2cc.md) [`00b0e538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e538.md) · 呼出先 1件 [`010a5660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5660.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0164",
      "READ",
      [
        "storage",
        "00c1e8e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be016c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5660"
      ]
    ]
  ],
  "added": [
    [
      "00be0214",
      "READ",
      [
        "storage",
        "00c1e998",
        null,
        "pointer"
      ]
    ],
    [
      "00be021c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5660"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0160.md#insn-00be0160) · [`00be0164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0160.md#insn-00be0164) · [`00be0168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0160.md#insn-00be0168)

~~~diff
- 00be0160 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0160 bytes f00100d0
- 00be0164 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e8:8"]]
- 00be0164 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0164 bytes 117644f9
- 00be0168 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00be0168 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0168 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0168 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0168 bytes 10a22391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb6f99f1bf373fc10f55af872b945ec"></a>

### [`00be0170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0170.md) → [`00be0220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0220.md) _ZNKSt6__ndk16locale9has_facetERNS0_2idE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48844.md) [`00b88710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b88710.md) · 呼出先 1件 [`00ba8634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba8634.md)
- 新版 呼出元 2件 [`00b4890c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4890c.md) [`00b887d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b887d8.md) · 呼出先 1件 [`00ba86fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba86fc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0174",
      "READ",
      [
        "storage",
        "00c1e8f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be017c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00ba86fc"
      ]
    ]
  ],
  "added": [
    [
      "00be0224",
      "READ",
      [
        "storage",
        "00c1e9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00be022c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00ba86fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0170.md#insn-00be0170) · [`00be0174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0170.md#insn-00be0174) · [`00be0178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0170.md#insn-00be0178)

~~~diff
- 00be0170 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0170 bytes f00100d0
- 00be0174 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8f0:8"]]
- 00be0174 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0174 bytes 117a44f9
- 00be0178 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00be0178 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0178 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0178 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0178 bytes 10c22391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf916957edbcc23ef782af2e32e715fe"></a>

### [`00be0180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0180.md) → [`00be0230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b47a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47a90.md) [`00b889c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b88/00b889c8.md) · 呼出先 1件 [`00b47e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47e68.md)
- 新版 呼出元 2件 [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md) [`00b88a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md) · 呼出先 1件 [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0184",
      "READ",
      [
        "storage",
        "00c1e8f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be018c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47f30"
      ]
    ]
  ],
  "added": [
    [
      "00be0234",
      "READ",
      [
        "storage",
        "00c1e9a8",
        null,
        "pointer"
      ]
    ],
    [
      "00be023c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47f30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0180.md#insn-00be0180) · [`00be0184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0180.md#insn-00be0184) · [`00be0188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0180.md#insn-00be0188)

~~~diff
- 00be0180 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0180 bytes f00100d0
- 00be0184 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8f8:8"]]
- 00be0184 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0184 bytes 117e44f9
- 00be0188 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00be0188 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0188 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0188 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0188 bytes 10e22391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e4e70575e56d19bec040237928bc1e"></a>

### [`00be01a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md) → [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`00b464d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b464d0.md) [`00b46614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46614.md) [`00b46650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46650.md) [`00b46e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46e18.md) [`00b47088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47088.md) · 呼出先 1件 [`00b47a90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47a90.md)
- 新版 呼出元 12件 [`00b46598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md) [`00b466dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b466dc.md) [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md) [`00b46ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ee0.md) [`00b47150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47150.md) · 呼出先 1件 [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01a4",
      "READ",
      [
        "storage",
        "00c1e908",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47b58"
      ]
    ]
  ],
  "added": [
    [
      "00be0254",
      "READ",
      [
        "storage",
        "00c1e9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00be025c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47b58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md#insn-00be01a4) · [`00be01a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md#insn-00be01a8) · [`00be01ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01a0.md#insn-00be01ac)

~~~diff
- 00be01a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:908:8"]]
- 00be01a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01a4 bytes 118644f9
- 00be01a8 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00be01a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01a8 bytes 10222491
- 00be01ac ["COPY", "register:0:8", ["register:4088:8"]]
- 00be01ac ["BRANCHIND", null, ["register:0:8"]]
- 00be01ac bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23bd3dffa9aa881a8edee1ee00dfb6c3"></a>

### [`00be01b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01b0.md) → [`00be0260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0260.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b46650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46650.md) · 呼出先 1件 [`00b46c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b46/00b46c00.md)
- 新版 呼出元 1件 [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md) · 呼出先 1件 [`00b46cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46cc8.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01b4",
      "READ",
      [
        "storage",
        "00c1e910",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46cc8"
      ]
    ]
  ],
  "added": [
    [
      "00be0264",
      "READ",
      [
        "storage",
        "00c1e9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00be026c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46cc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01b0.md#insn-00be01b4) · [`00be01b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01b0.md#insn-00be01b8) · [`00be01bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01b0.md#insn-00be01bc)

~~~diff
- 00be01b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:910:8"]]
- 00be01b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01b4 bytes 118a44f9
- 00be01b8 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00be01b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01b8 bytes 10422491
- 00be01bc ["COPY", "register:0:8", ["register:4088:8"]]
- 00be01bc ["BRANCHIND", null, ["register:0:8"]]
- 00be01bc bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6469c953453b664d9be6c8b5b7a5c029"></a>

### [`00be01c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01c0.md) → [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md) &lt;EXTERNAL&gt;::fseeko

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b47d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47d38.md) [`00b47df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47df8.md) [`00b47e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b47e68.md) · 呼出先 1件 [`010a5668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5668.md)
- 新版 呼出元 3件 [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) [`00b47ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md) [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md) · 呼出先 1件 [`010a5668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5668.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01c4",
      "READ",
      [
        "storage",
        "00c1e918",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5668"
      ]
    ]
  ],
  "added": [
    [
      "00be0274",
      "READ",
      [
        "storage",
        "00c1e9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00be027c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5668"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01c0.md#insn-00be01c0) · [`00be01c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01c0.md#insn-00be01c4) · [`00be01c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01c0.md#insn-00be01c8)

~~~diff
- 00be01c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be01c0 bytes f00100d0
- 00be01c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:918:8"]]
- 00be01c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01c4 bytes 118e44f9
- 00be01c8 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00be01c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01c8 bytes 10622491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118c57a302a7df1b610fb02b4c83ab95"></a>

### [`00be01e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01e0.md) → [`00be0290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0290.md) &lt;EXTERNAL&gt;::realpath

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b476c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b476c4.md) · 呼出先 1件 [`010a5678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5678.md)
- 新版 呼出元 1件 [`00b4778c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4778c.md) · 呼出先 1件 [`010a5678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5678.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01e4",
      "READ",
      [
        "storage",
        "00c1e928",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5678"
      ]
    ]
  ],
  "added": [
    [
      "00be0294",
      "READ",
      [
        "storage",
        "00c1e9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00be029c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5678"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01e0.md#insn-00be01e4) · [`00be01e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01e0.md#insn-00be01e8) · [`00be01ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01e0.md#insn-00be01ec)

~~~diff
- 00be01e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:928:8"]]
- 00be01e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01e4 bytes 119644f9
- 00be01e8 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00be01e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01e8 bytes 10a22491
- 00be01ec ["COPY", "register:0:8", ["register:4088:8"]]
- 00be01ec ["BRANCHIND", null, ["register:0:8"]]
- 00be01ec bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffe30c6314ef1bff0f0bb3885bf1a2ca"></a>

### [`00be01f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01f0.md) → [`00be02a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02a0.md) &lt;EXTERNAL&gt;::setlocale

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b477b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b47/00b477b0.md) [`00ba842c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba842c.md) · 呼出先 1件 [`010a5680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a5680.md)
- 新版 呼出元 2件 [`00b47878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md) [`00ba84f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md) · 呼出先 1件 [`010a5680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5680.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be01f4",
      "READ",
      [
        "storage",
        "00c1e930",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be01fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5680"
      ]
    ]
  ],
  "added": [
    [
      "00be02a4",
      "READ",
      [
        "storage",
        "00c1e9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00be02ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5680"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be01f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01f0.md#insn-00be01f0) · [`00be01f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01f0.md#insn-00be01f4) · [`00be01f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be01f0.md#insn-00be01f8)

~~~diff
- 00be01f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be01f0 bytes f00100d0
- 00be01f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:930:8"]]
- 00be01f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be01f4 bytes 119a44f9
- 00be01f8 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00be01f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be01f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be01f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be01f8 bytes 10c22491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b05d531ed92b2ea368bc543e78d0042"></a>

### [`00be0210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0210.md) → [`00be02c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02c0.md) _ZN8firebase9messaging10FutureData6CreateEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4c3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4c3b8.md) · 呼出先 1件 [`00b49364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49364.md)
- 新版 呼出元 1件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) · 呼出先 1件 [`00b4942c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4942c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0214",
      "READ",
      [
        "storage",
        "00c1e940",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be021c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4942c"
      ]
    ]
  ],
  "added": [
    [
      "00be02c4",
      "READ",
      [
        "storage",
        "00c1e9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00be02cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4942c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0210.md#insn-00be0210) · [`00be0214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0210.md#insn-00be0214) · [`00be0218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0210.md#insn-00be0218)

~~~diff
- 00be0210 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0210 bytes f00100d0
- 00be0214 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:940:8"]]
- 00be0214 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0214 bytes 11a244f9
- 00be0218 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00be0218 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0218 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0218 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0218 bytes 10022591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15450671786218433b69bd76b53dab20"></a>

### [`00be0220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0220.md) → [`00be02d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02d0.md) _ZN8firebase9messaging10FutureData7DestroyEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md) · 呼出先 1件 [`00b493b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b493b4.md)
- 新版 呼出元 1件 [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00b4947c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4947c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0224",
      "READ",
      [
        "storage",
        "00c1e948",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be022c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4947c"
      ]
    ]
  ],
  "added": [
    [
      "00be02d4",
      "READ",
      [
        "storage",
        "00c1e9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00be02dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4947c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0220.md#insn-00be0220) · [`00be0224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0220.md#insn-00be0224) · [`00be0228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0220.md#insn-00be0228)

~~~diff
- 00be0220 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0220 bytes f00100d0
- 00be0224 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:948:8"]]
- 00be0224 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0224 bytes 11a644f9
- 00be0228 ["COPY", "tmp:0:8", ["const:948:8"]]
- 00be0228 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0228 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0228 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0228 bytes 10222591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-317a0a92bd829f759bec63543a0c3c8c"></a>

### [`00be0230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0230.md) → [`00be02e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02e0.md) _ZN8firebase9messaging11HasListenerEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4b7bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b7bc.md) · 呼出先 1件 [`00b48c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48c80.md)
- 新版 呼出元 1件 [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) · 呼出先 1件 [`00b48d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d48.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0234",
      "READ",
      [
        "storage",
        "00c1e950",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be023c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48d48"
      ]
    ]
  ],
  "added": [
    [
      "00be02e4",
      "READ",
      [
        "storage",
        "00c1ea00",
        null,
        "pointer"
      ]
    ],
    [
      "00be02ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48d48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0230.md#insn-00be0230) · [`00be0234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0230.md#insn-00be0234) · [`00be0238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0230.md#insn-00be0238)

~~~diff
- 00be0230 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0230 bytes f00100d0
- 00be0234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:950:8"]]
- 00be0234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0234 bytes 11aa44f9
- 00be0238 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00be0238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0238 bytes 10422591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a2d8bb40bc2cbfc6efcea04fb4ab517"></a>

### [`00be0240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0240.md) → [`00be02f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02f0.md) _ZN8firebase9messaging11SetListenerEPNS0_8ListenerE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b48cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48cc4.md) [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md) · 呼出先 1件 [`00b48b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b7c.md)
- 新版 呼出元 2件 [`00b48d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d8c.md) [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00b48c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md)

変更の種類 comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00be02f4",
      "READ",
      [
        "storage",
        "00c1e958",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00be02f4",
      "READ",
      [
        "storage",
        "00c1ea08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0240.md#insn-00be0244) · [`00be0248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0240.md#insn-00be0248)
- 新版 `00be02f4`（命令位置の公開資料なし） · `00be02f8`（命令位置の公開資料なし）

~~~diff
- 00be0244 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:958:8"]]
- 00be0244 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
+ 00be02f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a08:8"]]
+ 00be02f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0244 bytes 11ae44f9
+ 00be02f4 bytes 110645f9
- 00be0248 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00be0248 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0248 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0248 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0248 bytes 10622591
+ 00be02f8 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00be02f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
+ 00be02f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
+ 00be02f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
+ 00be02f8 bytes 10222891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05a1367b51a8f1888b761b5c77f06bfe"></a>

### [`00be0270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0270.md) → [`00be0320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0320.md) _ZN8firebase9messaging12NotificationaSERKS1_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49c34.md) · 呼出先 1件 [`00b49f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49f54.md)
- 新版 呼出元 1件 [`00b49cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49cfc.md) · 呼出先 1件 [`00b4a01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a01c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0274",
      "READ",
      [
        "storage",
        "00c1e970",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be027c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a01c"
      ]
    ]
  ],
  "added": [
    [
      "00be0324",
      "READ",
      [
        "storage",
        "00c1ea20",
        null,
        "pointer"
      ]
    ],
    [
      "00be032c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a01c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0270.md#insn-00be0270) · [`00be0274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0270.md#insn-00be0274) · [`00be0278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0270.md#insn-00be0278)

~~~diff
- 00be0270 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0270 bytes f00100d0
- 00be0274 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:970:8"]]
- 00be0274 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0274 bytes 11ba44f9
- 00be0278 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00be0278 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0278 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0278 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0278 bytes 10c22591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efb4cd18deafbff8294997e7c69400cf"></a>

### [`00be0280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0280.md) → [`00be0330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md) _ZN8firebase9messaging16PollableListenerD1Ev

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48fac.md) · 呼出先 1件 [`00b48ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48ef0.md)
- 新版 呼出元 1件 [`00b49074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49074.md) · 呼出先 1件 [`00b48fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0284",
      "READ",
      [
        "storage",
        "00c1e978",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be028c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48fb8"
      ]
    ]
  ],
  "added": [
    [
      "00be0334",
      "READ",
      [
        "storage",
        "00c1ea28",
        null,
        "pointer"
      ]
    ],
    [
      "00be033c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48fb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0280.md#insn-00be0280) · [`00be0284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0280.md#insn-00be0284) · [`00be0288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0280.md#insn-00be0288)

~~~diff
- 00be0280 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0280 bytes f00100d0
- 00be0284 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:978:8"]]
- 00be0284 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0284 bytes 11be44f9
- 00be0288 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00be0288 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0288 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0288 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0288 bytes 10e22591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba984c0da69b376494869444826a2ba3"></a>

### [`00be0290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0290.md) → [`00be0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b7c.md) · 呼出先 1件 [`00b4b4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4b/00b4b4d4.md)
- 新版 呼出元 1件 [`00b48c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md) · 呼出先 1件 [`00b4b59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0294",
      "READ",
      [
        "storage",
        "00c1e980",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be029c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4b59c"
      ]
    ]
  ],
  "added": [
    [
      "00be0344",
      "READ",
      [
        "storage",
        "00c1ea30",
        null,
        "pointer"
      ]
    ],
    [
      "00be034c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4b59c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0290.md#insn-00be0294) · [`00be0298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0290.md#insn-00be0298) · [`00be029c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0290.md#insn-00be029c)

~~~diff
- 00be0294 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:980:8"]]
- 00be0294 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0294 bytes 11c244f9
- 00be0298 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00be0298 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0298 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0298 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0298 bytes 10022691
- 00be029c ["COPY", "register:0:8", ["register:4088:8"]]
- 00be029c ["BRANCHIND", null, ["register:0:8"]]
- 00be029c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-916fec857bb051709645b616dfb1e619"></a>

### [`00be02a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be02a0.md) → [`00be0350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0350.md) _ZN8firebase9messaging20PollableListenerImpl11PollMessageEPNS0_7MessageE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49158.md) · 呼出先 1件 [`00b49160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49160.md)
- 新版 呼出元 1件 [`00b49220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49220.md) · 呼出先 1件 [`00b49228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be02a4",
      "READ",
      [
        "storage",
        "00c1e988",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be02ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49228"
      ]
    ]
  ],
  "added": [
    [
      "00be0354",
      "READ",
      [
        "storage",
        "00c1ea38",
        null,
        "pointer"
      ]
    ],
    [
      "00be035c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49228"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be02a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be02a0.md#insn-00be02a0) · [`00be02a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be02a0.md#insn-00be02a4) · [`00be02a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be02a0.md#insn-00be02a8)

~~~diff
- 00be02a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be02a0 bytes f00100d0
- 00be02a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:988:8"]]
- 00be02a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be02a4 bytes 11c644f9
- 00be02a8 ["COPY", "tmp:0:8", ["const:988:8"]]
- 00be02a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be02a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be02a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be02a8 bytes 10222691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37980b5a8566589544d0ef4d0b91e2c9"></a>

### [`00be0310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0310.md) → [`00be03c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03c0.md) _ZN8firebase9messaging7MessageC2ERKS1_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48fd8.md) · 呼出先 1件 [`00b49860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49860.md)
- 新版 呼出元 1件 [`00b490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md) · 呼出先 1件 [`00b49928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49928.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0314",
      "READ",
      [
        "storage",
        "00c1e9c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be031c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49928"
      ]
    ]
  ],
  "added": [
    [
      "00be03c4",
      "READ",
      [
        "storage",
        "00c1ea70",
        null,
        "pointer"
      ]
    ],
    [
      "00be03cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49928"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0310.md#insn-00be0310) · [`00be0314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0310.md#insn-00be0314) · [`00be0318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0310.md#insn-00be0318)

~~~diff
- 00be0310 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0310 bytes f00100d0
- 00be0314 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9c0:8"]]
- 00be0314 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0314 bytes 11e244f9
- 00be0318 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00be0318 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0318 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0318 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0318 bytes 10022791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed26a81c424449025b27f7ab3c284c3"></a>

### [`00be0360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0360.md) → [`00be0410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0410.md) _ZN8firebase9messaging8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md) · 呼出先 1件 [`00b48b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48b3c.md)
- 新版 呼出元 1件 [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00b48c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c04.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0364",
      "READ",
      [
        "storage",
        "00c1e9e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be036c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48c04"
      ]
    ]
  ],
  "added": [
    [
      "00be0414",
      "READ",
      [
        "storage",
        "00c1ea98",
        null,
        "pointer"
      ]
    ],
    [
      "00be041c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48c04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0360.md#insn-00be0360) · [`00be0364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0360.md#insn-00be0364) · [`00be0368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0360.md#insn-00be0368)

~~~diff
- 00be0360 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0360 bytes f00100d0
- 00be0364 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9e8:8"]]
- 00be0364 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0364 bytes 11f644f9
- 00be0368 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 00be0368 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0368 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0368 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0368 bytes 10a22791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-545a1f1e01fc38152379a186c9429bd9"></a>

### [`00be0370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0370.md) → [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48ac8.md) [`00b49400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b49400.md) · 呼出先 1件 [`00b4cdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4c/00b4cdc8.md)
- 新版 呼出元 2件 [`00b48b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b90.md) [`00b494c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md) · 呼出先 1件 [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0374",
      "READ",
      [
        "storage",
        "00c1e9f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be037c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4ce90"
      ]
    ]
  ],
  "added": [
    [
      "00be0424",
      "READ",
      [
        "storage",
        "00c1eaa0",
        null,
        "pointer"
      ]
    ],
    [
      "00be042c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4ce90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0370.md#insn-00be0370) · [`00be0374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0370.md#insn-00be0374) · [`00be0378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0370.md#insn-00be0378)

~~~diff
- 00be0370 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0370 bytes f00100d0
- 00be0374 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9f0:8"]]
- 00be0374 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0374 bytes 11fa44f9
- 00be0378 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 00be0378 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0378 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0378 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0378 bytes 10c22791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7f9469efbeb9d833babe8402c1d8c48"></a>

### [`00be0380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0380.md) → [`00be0430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0430.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48d48.md) [`00b647c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b647c4.md) · 呼出先 1件 [`00b77c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b77/00b77c0c.md)
- 新版 呼出元 2件 [`00b48e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48e10.md) [`00b6488c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b6488c.md) · 呼出先 1件 [`00b77cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b77/00b77cd4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0384",
      "READ",
      [
        "storage",
        "00c1e9f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be038c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b77cd4"
      ]
    ]
  ],
  "added": [
    [
      "00be0434",
      "READ",
      [
        "storage",
        "00c1eaa8",
        null,
        "pointer"
      ]
    ],
    [
      "00be043c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b77cd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0380.md#insn-00be0380) · [`00be0384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0380.md#insn-00be0384) · [`00be0388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0380.md#insn-00be0388)

~~~diff
- 00be0380 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0380 bytes f00100d0
- 00be0384 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9f8:8"]]
- 00be0384 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0384 bytes 11fe44f9
- 00be0388 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00be0388 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0388 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0388 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0388 bytes 10e22791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2285485fb8677c2724c2a3eb1b343d77"></a>

### [`00be0390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0390.md) → [`00be0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md) _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b48ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48ef0.md) · 呼出先 1件 [`00b4942c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b49/00b4942c.md)
- 新版 呼出元 1件 [`00b48fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md) · 呼出先 1件 [`00b494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494f4.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0394",
      "READ",
      [
        "storage",
        "00c1ea00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be039c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b494f4"
      ]
    ]
  ],
  "added": [
    [
      "00be0444",
      "READ",
      [
        "storage",
        "00c1eab0",
        null,
        "pointer"
      ]
    ],
    [
      "00be044c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b494f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0390.md#insn-00be0394) · [`00be0398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0390.md#insn-00be0398) · [`00be039c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0390.md#insn-00be039c)

~~~diff
- 00be0394 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a00:8"]]
- 00be0394 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0394 bytes 110245f9
- 00be0398 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 00be0398 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0398 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0398 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0398 bytes 10022891
- 00be039c ["COPY", "register:0:8", ["register:4088:8"]]
- 00be039c ["BRANCHIND", null, ["register:0:8"]]
- 00be039c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a6d027350e8eb7ad73026bdfb5dd00f"></a>

### [`00be03c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03c0.md) → [`00be0470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0470.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE10push_frontERKS4_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a13c.md) · 呼出先 1件 [`00b4a850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a850.md)
- 新版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 1件 [`00b4a918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a918.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03c4",
      "READ",
      [
        "storage",
        "00c1ea18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a918"
      ]
    ]
  ],
  "added": [
    [
      "00be0474",
      "READ",
      [
        "storage",
        "00c1eac8",
        null,
        "pointer"
      ]
    ],
    [
      "00be047c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a918"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03c0.md#insn-00be03c0) · [`00be03c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03c0.md#insn-00be03c4) · [`00be03c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03c0.md#insn-00be03c8)

~~~diff
- 00be03c0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03c0 bytes f00100d0
- 00be03c4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a18:8"]]
- 00be03c4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03c4 bytes 110e45f9
- 00be03c8 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 00be03c8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03c8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03c8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03c8 bytes 10622891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-672aa3dfca8c56d06373de1d5cad7ed3"></a>

### [`00be03d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03d0.md) → [`00be0480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0480.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a13c.md) · 呼出先 1件 [`00b4a710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a710.md)
- 新版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 1件 [`00b4a7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a7d8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03d4",
      "READ",
      [
        "storage",
        "00c1ea20",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a7d8"
      ]
    ]
  ],
  "added": [
    [
      "00be0484",
      "READ",
      [
        "storage",
        "00c1ead0",
        null,
        "pointer"
      ]
    ],
    [
      "00be048c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a7d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03d0.md#insn-00be03d0) · [`00be03d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03d0.md#insn-00be03d4) · [`00be03d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03d0.md#insn-00be03d8)

~~~diff
- 00be03d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03d0 bytes f00100d0
- 00be03d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a20:8"]]
- 00be03d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03d4 bytes 111245f9
- 00be03d8 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00be03d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03d8 bytes 10822891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bb362e061a17a0b47ed67117dd523b6"></a>

### [`00be03e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03e0.md) → [`00be0490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0490.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b48/00b48fd8.md) · 呼出先 1件 [`00b4a13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4a/00b4a13c.md)
- 新版 呼出元 1件 [`00b490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md) · 呼出先 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03e4",
      "READ",
      [
        "storage",
        "00c1ea28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a204"
      ]
    ]
  ],
  "added": [
    [
      "00be0494",
      "READ",
      [
        "storage",
        "00c1ead8",
        null,
        "pointer"
      ]
    ],
    [
      "00be049c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a204"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03e0.md#insn-00be03e0) · [`00be03e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03e0.md#insn-00be03e4) · [`00be03e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be03e0.md#insn-00be03e8)

~~~diff
- 00be03e0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03e0 bytes f00100d0
- 00be03e4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a28:8"]]
- 00be03e4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03e4 bytes 111645f9
- 00be03e8 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00be03e8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03e8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03e8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03e8 bytes 10a22891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c86236139eea882f3eddeba2bc191265"></a>

### [`00be0400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0400.md) → [`00be04b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md) _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xb0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4edc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b4e/00b4edc0.md) · 呼出先 1件 [`00b50144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b50/00b50144.md)
- 新版 呼出元 1件 [`00b4ee88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee88.md) · 呼出先 1件 [`00b5020c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b5020c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0404",
      "READ",
      [
        "storage",
        "00c1ea38",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be040c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5020c"
      ]
    ]
  ],
  "added": [
    [
      "00be04b4",
      "READ",
      [
        "storage",
        "00c1eae8",
        null,
        "pointer"
      ]
    ],
    [
      "00be04bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b5020c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0400.md#insn-00be0400) · [`00be0404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0400.md#insn-00be0404) · [`00be0408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0400.md#insn-00be0408)

~~~diff
- 00be0400 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0400 bytes f00100d0
- 00be0404 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a38:8"]]
- 00be0404 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0404 bytes 111e45f9
- 00be0408 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00be0408 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0408 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0408 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0408 bytes 10e22891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

