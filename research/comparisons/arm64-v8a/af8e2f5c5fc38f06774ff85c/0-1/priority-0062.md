# v15.7.2 → v15.7.3 · 最優先の変更候補 (62)

[一覧の目次](README.md)

<a id="compare-53cfdb67abf52c3b1a38bc24cbb358ad"></a>

### [`00af1780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1780.md) → [`00af1848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1848.md) _ZN8firebase4util19VariantMapToJavaMapEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4b0.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bde4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4c0.md)
- 新版 呼出元 1件 [`00bde560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde560.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde570.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 59.14% / 新版 59.14%

CFGの説明率　旧版 4.65% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af17c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af17d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af182c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af17a4",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af17a8",
      "READ",
      [
        "storage",
        "010a0760",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1880",
      "READ",
      [
        "storage",
        "010a0888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af186c",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1870",
      "READ",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1880",
      "READ",
      [
        "storage",
        "010a0948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af17b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1780.md#insn-00af17b0) · [`00af17c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1780.md#insn-00af17c8) · [`00af17d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1780.md#insn-00af17d8)
- 新版 `00af1878`（命令位置の公開資料なし）

~~~diff
- 00af17b0 ["INT_ADD", "register:40f0:8", ["const:af17b0:8", "const:4:8"]]
- 00af17b0 ["CALL", null, ["callee:0056681c:8"]]
+ 00af1878 ["INT_ADD", "register:40f0:8", ["const:af1878:8", "const:4:8"]]
+ 00af1878 ["CALL", null, ["callee:0056681c:8"]]
- 00af17b0 bytes 1bd4e997
+ 00af1878 bytes e9d3e997
- 00af17c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af17c8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00af17c8 bytes a1000054
- 00af17d8 ["CBRANCH", null, ["local:b32:8", "register:101:1"]]
- 00af17d8 bytes 00080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2880d9f18c8100dde4db9d7e6cca51"></a>

### [`00af18f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af18f4.md) → [`00af19bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af19bc.md) _ZN8firebase4util19VariantToJavaObjectEP7_JNIEnvRKNS_7VariantE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4c0.md) · 呼出先 7件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbb0.md) [`00bddbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbd0.md) [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00bde4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4b0.md)
- 新版 呼出元 1件 [`00bde570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde570.md) · 呼出先 7件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bddc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) [`00bddc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde560.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.14% / 新版 79.14%

CFGの説明率　旧版 9.43% / 新版 10.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af18f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af18f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af18f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af18f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af18f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af18fc",
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
      "00af19bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af19c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af19c4",
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

- 旧版 [`00af18f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af18f4.md#insn-00af18f4) · [`00af18f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af18f4.md#insn-00af18f8) · [`00af18fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af18f4.md#insn-00af18fc)

~~~diff
- 00af18f4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af18f4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af18f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af18f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af18f4 bytes f657bda9
- 00af18f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af18f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af18f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af18f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af18f8 bytes f44f01a9
- 00af18fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af18fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af18fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af18fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af18fc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76bf08b55b4c20ade65b7f24cf754cd6"></a>

### [`00af1c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1c8c.md) → [`00af1d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1d54.md) _ZN8firebase4util15StdMapToJavaMapEP7_JNIEnvPP8_jobjectRKNSt6__ndk13mapINS6_12basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESD_NS6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3a0.md) · 呼出先 1件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md)
- 新版 呼出元 1件 [`00bde450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde450.md) · 呼出先 1件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 57.58% / 新版 59.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1df8",
      "incomplete_value": true,
      "site": "00af1e08",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1df0",
      "incomplete_value": true,
      "site": "00af1e08",
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
            "register:40a0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1dfc",
      "incomplete_value": true,
      "site": "00af1e08",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af1d74",
      "READ",
      [
        "storage",
        "010a0888",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1e48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1e74"
      ]
    ]
  ],
  "added": [
    [
      "00af1d74",
      "READ",
      [
        "storage",
        "010a0948",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1e48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1e60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1c8c.md#insn-00af1d40) · [`00af1d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1c8c.md#insn-00af1d94) · [`00af1da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1c8c.md#insn-00af1da8)
- 新版 `00af1e08`（命令位置の公開資料なし） · `00af1e70`（命令位置の公開資料なし） · `00af1e5c`（命令位置の公開資料なし）

~~~diff
- 00af1d40 ["INT_ADD", "register:40f0:8", ["const:af1d40:8", "const:4:8"]]
- 00af1d40 ["CALL", null, ["callee:0047495c:8"]]
+ 00af1e08 ["INT_ADD", "register:40f0:8", ["const:af1e08:8", "const:4:8"]]
+ 00af1e08 ["CALL", null, ["callee:0047495c:8"]]
- 00af1d40 bytes 070be697
+ 00af1e08 bytes d50ae697
- 00af1d94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af1d94 ["INT_ADD", "register:40f0:8", ["const:af1d94:8", "const:4:8"]]
- 00af1d94 ["CALLIND", null, ["register:0:8"]]
+ 00af1e70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af1e70 ["INT_ADD", "register:40f0:8", ["const:af1e70:8", "const:4:8"]]
+ 00af1e70 ["CALLIND", null, ["register:0:8"]]
- 00af1d94 bytes 00013fd6
+ 00af1e70 bytes 00013fd6
- 00af1da8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af1da8 ["INT_ADD", "register:40f0:8", ["const:af1da8:8", "const:4:8"]]
- 00af1da8 ["CALLIND", null, ["register:0:8"]]
+ 00af1e5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af1e5c ["INT_ADD", "register:40f0:8", ["const:af1e5c:8", "const:4:8"]]
+ 00af1e5c ["CALLIND", null, ["register:0:8"]]
- 00af1da8 bytes 00013fd6
+ 00af1e5c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5cd277695c0a9eb11686e36d3367565"></a>

### [`00af1e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1e20.md) → [`00af1ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1ee8.md) _ZN8firebase4util15JavaMapToStdMapEP7_JNIEnvPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESA_NS3_4lessISA_EEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.45% / 新版 88.45%

CFGの説明率　旧版 86.30% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1fb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af1f4c"
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
      "00af1f28",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af1e84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1f70"
      ]
    ],
    [
      "00af1f74",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af1f28",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1f70"
      ]
    ],
    [
      "00af1f74",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af1e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1e20.md#insn-00af1e68) · [`00af1e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1e20.md#insn-00af1e7c) · [`00af1e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1e20.md#insn-00af1e84)
- 新版 `00af1f30`（命令位置の公開資料なし）

~~~diff
- 00af1e68 ["INT_ADD", "register:40f0:8", ["const:af1e68:8", "const:4:8"]]
- 00af1e68 ["CALL", null, ["callee:0047495c:8"]]
+ 00af1f30 ["INT_ADD", "register:40f0:8", ["const:af1f30:8", "const:4:8"]]
+ 00af1f30 ["CALL", null, ["callee:0047495c:8"]]
- 00af1e68 bytes bd0ae697
+ 00af1f30 bytes 8b0ae697
- 00af1e7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af1e7c ["INT_ADD", "register:40f0:8", ["const:af1e7c:8", "const:4:8"]]
- 00af1e7c ["CALLIND", null, ["register:0:8"]]
- 00af1e7c bytes 00013fd6
- 00af1e84 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00af1e84 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67d102db99639c234050307115d6e958"></a>

### [`00af23f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af23f8.md) → [`00af24c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24c0.md) FUN_00af24c0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00af23f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af23f4.md) [`00af26fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af26fc.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9a0.md)
- 新版 呼出元 2件 [`00af24bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af24bc.md) [`00af27c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2500",
      "incomplete_value": true,
      "site": "00af2508",
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2438",
      "incomplete_value": true,
      "site": "00af2440",
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
                "const:898:8"
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
      "definition_site": "00af254c",
      "incomplete_value": true,
      "site": "00af2558",
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
                "const:998:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2484",
      "incomplete_value": true,
      "site": "00af2490",
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
                "const:8d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af259c",
      "incomplete_value": true,
      "site": "00af25ac",
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
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af24d4",
      "incomplete_value": true,
      "site": "00af24e4",
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af2500",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00af254c",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af259c",
      "READ",
      [
        "storage",
        "010a0808",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af2500",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined8"
      ]
    ],
    [
      "00af254c",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af259c",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af2440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af23f8.md#insn-00af2440) · [`00af2490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af23f8.md#insn-00af2490) · [`00af24e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af23f8.md#insn-00af24e4)
- 新版 `00af2508`（命令位置の公開資料なし） · `00af2558`（命令位置の公開資料なし） · `00af25ac`（命令位置の公開資料なし）

~~~diff
- 00af2440 ["INT_ADD", "register:40f0:8", ["const:af2440:8", "const:4:8"]]
- 00af2440 ["CALL", null, ["callee:0047495c:8"]]
+ 00af2508 ["INT_ADD", "register:40f0:8", ["const:af2508:8", "const:4:8"]]
+ 00af2508 ["CALL", null, ["callee:0047495c:8"]]
- 00af2440 bytes 4709e697
+ 00af2508 bytes 1509e697
- 00af2490 ["INT_ADD", "register:40f0:8", ["const:af2490:8", "const:4:8"]]
- 00af2490 ["CALL", null, ["callee:0047495c:8"]]
+ 00af2558 ["INT_ADD", "register:40f0:8", ["const:af2558:8", "const:4:8"]]
+ 00af2558 ["CALL", null, ["callee:0047495c:8"]]
- 00af2490 bytes 3309e697
+ 00af2558 bytes 0109e697
- 00af24e4 ["INT_ADD", "register:40f0:8", ["const:af24e4:8", "const:4:8"]]
- 00af24e4 ["CALL", null, ["callee:00474b70:8"]]
+ 00af25ac ["INT_ADD", "register:40f0:8", ["const:af25ac:8", "const:4:8"]]
+ 00af25ac ["CALL", null, ["callee:00474b70:8"]]
- 00af24e4 bytes a309e697
+ 00af25ac bytes 7109e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45966f1b602cca9e22cfdfbc63f5c698"></a>

### [`00af26fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af26fc.md) → [`00af27c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af27c4.md) _ZN8firebase4util19JavaObjectToVariantEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde490.md) · 呼出先 19件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00558/00558f34.md) [`0056c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c6c4.md)
- 新版 呼出元 1件 [`00bde540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde540.md) · 呼出先 19件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00558f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00558/00558f34.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 77.65% / 新版 77.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af2c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af2ca0"
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
      "00af27fc",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2858",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2878",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af27fc",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2858",
      "READ",
      [
        "storage",
        "010a0710",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2878",
      "READ",
      [
        "storage",
        "010a0730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af2744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af26fc.md#insn-00af2744) · [`00af2780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af26fc.md#insn-00af2780) · [`00af27a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af26fc.md#insn-00af27a0)
- 新版 `00af280c`（命令位置の公開資料なし） · `00af2848`（命令位置の公開資料なし） · `00af2868`（命令位置の公開資料なし）

~~~diff
- 00af2744 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af2744 ["INT_ADD", "register:40f0:8", ["const:af2744:8", "const:4:8"]]
- 00af2744 ["CALLIND", null, ["register:0:8"]]
+ 00af280c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af280c ["INT_ADD", "register:40f0:8", ["const:af280c:8", "const:4:8"]]
+ 00af280c ["CALLIND", null, ["register:0:8"]]
- 00af2744 bytes 00013fd6
+ 00af280c bytes 00013fd6
- 00af2780 ["INT_ADD", "register:40f0:8", ["const:af2780:8", "const:4:8"]]
- 00af2780 ["CALL", null, ["callee:00bdb010:8"]]
+ 00af2848 ["INT_ADD", "register:40f0:8", ["const:af2848:8", "const:4:8"]]
+ 00af2848 ["CALL", null, ["callee:00bdb010:8"]]
- 00af2780 bytes f8a10394
+ 00af2848 bytes f2a10394
- 00af27a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af27a0 ["INT_ADD", "register:40f0:8", ["const:af27a0:8", "const:4:8"]]
- 00af27a0 ["CALLIND", null, ["register:0:8"]]
+ 00af2868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af2868 ["INT_ADD", "register:40f0:8", ["const:af2868:8", "const:4:8"]]
+ 00af2868 ["CALLIND", null, ["register:0:8"]]
- 00af27a0 bytes 00013fd6
+ 00af2868 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841ec28342abe16a771ae4fa2e360b87"></a>

### [`00af2e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af2e14.md) → [`00af2edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af2/00af2edc.md) _ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde550.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bde600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde600.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2f1c",
      "incomplete_value": true,
      "site": "00af2f24",
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
                "const:998:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2e54",
      "incomplete_value": true,
      "site": "00af2e5c",
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
                "const:8d8:8"
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
      "definition_site": "00af2f68",
      "incomplete_value": true,
      "site": "00af2f74",
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
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2ea0",
      "incomplete_value": true,
      "site": "00af2eac",
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af2f8c",
      "incomplete_value": true,
      "site": "00af2f98",
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af2ec4",
      "incomplete_value": true,
      "site": "00af2ed0",
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af2f1c",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2f68",
      "READ",
      [
        "storage",
        "010a0808",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2f8c",
      "READ",
      [
        "storage",
        "010a0808",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af2f1c",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2f68",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af2f8c",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af2e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af2e14.md#insn-00af2e5c) · [`00af2eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af2e14.md#insn-00af2eac) · [`00af2ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af2e14.md#insn-00af2ed0)
- 新版 `00af2f24`（命令位置の公開資料なし） · `00af2f74`（命令位置の公開資料なし） · `00af2f98`（命令位置の公開資料なし）

~~~diff
- 00af2e5c ["INT_ADD", "register:40f0:8", ["const:af2e5c:8", "const:4:8"]]
- 00af2e5c ["CALL", null, ["callee:0047495c:8"]]
+ 00af2f24 ["INT_ADD", "register:40f0:8", ["const:af2f24:8", "const:4:8"]]
+ 00af2f24 ["CALL", null, ["callee:0047495c:8"]]
- 00af2e5c bytes c006e697
+ 00af2f24 bytes 8e06e697
- 00af2eac ["INT_ADD", "register:40f0:8", ["const:af2eac:8", "const:4:8"]]
- 00af2eac ["CALL", null, ["callee:00474b70:8"]]
+ 00af2f74 ["INT_ADD", "register:40f0:8", ["const:af2f74:8", "const:4:8"]]
+ 00af2f74 ["CALL", null, ["callee:00474b70:8"]]
- 00af2eac bytes 3107e697
+ 00af2f74 bytes ff06e697
- 00af2ed0 ["INT_ADD", "register:40f0:8", ["const:af2ed0:8", "const:4:8"]]
- 00af2ed0 ["CALL", null, ["callee:00474b70:8"]]
+ 00af2f98 ["INT_ADD", "register:40f0:8", ["const:af2f98:8", "const:4:8"]]
+ 00af2f98 ["CALL", null, ["callee:00474b70:8"]]
- 00af2ed0 bytes 2807e697
+ 00af2f98 bytes f606e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9558999051fbc602acfba9e60fcfe4d7"></a>

### [`00af30c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af30c8.md) → [`00af3190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3190.md) _ZN8firebase4util23VariantVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde540.md) · 呼出先 3件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bde4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4c0.md)
- 新版 呼出元 1件 [`00bde5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5f0.md) · 呼出先 3件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af31b4",
      "incomplete_value": true,
      "site": "00af31c0",
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
                "const:530:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af30ec",
      "incomplete_value": true,
      "site": "00af30f8",
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af31b8",
      "incomplete_value": true,
      "site": "00af31c0",
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af30f0",
      "incomplete_value": true,
      "site": "00af30f8",
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
                "const:480:8"
              ]
            ]
          ]
        ]
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
      "00af31b4",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "00af31b8",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00af31d4",
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
      "00af31b4",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00af31b8",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af31d4",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af30f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af30c8.md#insn-00af30f8) · [`00af30e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af30c8.md#insn-00af30e4) · [`00af30ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af30c8.md#insn-00af30ec)
- 新版 `00af31c0`（命令位置の公開資料なし） · `00af31ac`（命令位置の公開資料なし） · `00af31b4`（命令位置の公開資料なし）

~~~diff
- 00af30f8 ["INT_ADD", "register:40f0:8", ["const:af30f8:8", "const:4:8"]]
- 00af30f8 ["CALL", null, ["callee:0056681c:8"]]
+ 00af31c0 ["INT_ADD", "register:40f0:8", ["const:af31c0:8", "const:4:8"]]
+ 00af31c0 ["CALL", null, ["callee:0056681c:8"]]
- 00af30f8 bytes c9cde997
+ 00af31c0 bytes 97cde997
- 00af30e4 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00af30e4 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00af30e4 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00af30e4 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00af31ac ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00af31ac ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00af31ac ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00af31ac ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00af30e4 bytes f7021291
+ 00af31ac bytes f7021591
- 00af30ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00af30ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af31b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 00af31b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af30ec bytes 013942f9
+ 00af31b4 bytes 019942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-205b2955d877ce9c7e066ee3b83e5d19"></a>

### [`00af31b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af31b0.md) → [`00af3278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3278.md) _ZN8firebase4util25JavaListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_IS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.15% / 新版 99.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af32b0",
      "incomplete_value": true,
      "site": "00af32b8",
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af31e8",
      "incomplete_value": true,
      "site": "00af31f0",
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
                "const:840:8"
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
      "definition_site": "00af3380",
      "incomplete_value": true,
      "site": "00af3390",
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af32b8",
      "incomplete_value": true,
      "site": "00af32c8",
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af32b0",
      "READ",
      [
        "storage",
        "010a0840",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3380",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af32b0",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3380",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af31f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af31b0.md#insn-00af31f0) · [`00af32b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af31b0.md#insn-00af32b8) · [`00af32c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af31b0.md#insn-00af32c8)
- 新版 `00af32b8`（命令位置の公開資料なし） · `00af3380`（命令位置の公開資料なし） · `00af3390`（命令位置の公開資料なし）

~~~diff
- 00af31f0 ["INT_ADD", "register:40f0:8", ["const:af31f0:8", "const:4:8"]]
- 00af31f0 ["CALL", null, ["callee:005533e0:8"]]
+ 00af32b8 ["INT_ADD", "register:40f0:8", ["const:af32b8:8", "const:4:8"]]
+ 00af32b8 ["CALL", null, ["callee:005533e0:8"]]
- 00af31f0 bytes 7c80e997
+ 00af32b8 bytes 4a80e997
- 00af32b8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:830:8"]]
- 00af32b8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af3380 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:8f0:8"]]
+ 00af3380 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af32b8 bytes 421b44f9
+ 00af3380 bytes 427b44f9
- 00af32c8 ["INT_ADD", "register:40f0:8", ["const:af32c8:8", "const:4:8"]]
- 00af32c8 ["CALL", null, ["callee:0047495c:8"]]
+ 00af3390 ["INT_ADD", "register:40f0:8", ["const:af3390:8", "const:4:8"]]
+ 00af3390 ["CALL", null, ["callee:0047495c:8"]]
- 00af32c8 bytes a505e697
+ 00af3390 bytes 7305e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88cedb248e0d6e4ad102fbd47090eaf7"></a>

### [`00af3498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3498.md) → [`00af3560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3560.md) _ZN8firebase4util31JavaObjectListToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc50.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af359c",
      "incomplete_value": true,
      "site": "00af35a4",
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af34d4",
      "incomplete_value": true,
      "site": "00af34dc",
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
                "const:840:8"
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
      "definition_site": "00af3684",
      "incomplete_value": true,
      "site": "00af3694",
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af35bc",
      "incomplete_value": true,
      "site": "00af35cc",
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af36d8",
      "incomplete_value": true,
      "site": "00af36e4",
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
                "register:40e0:8"
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
      "definition_site": "00af3610",
      "incomplete_value": true,
      "site": "00af361c",
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
                "register:40e0:8"
              ],
              [
                "leaf",
                "const:998:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af359c",
      "READ",
      [
        "storage",
        "010a0840",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3684",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00af36d8",
      "READ",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af359c",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3684",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af36d8",
      "READ",
      [
        "storage",
        "010a0a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af34dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3498.md#insn-00af34dc) · [`00af35cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3498.md#insn-00af35cc) · [`00af361c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af3498.md#insn-00af361c)
- 新版 `00af35a4`（命令位置の公開資料なし） · `00af3694`（命令位置の公開資料なし） · `00af36e4`（命令位置の公開資料なし）

~~~diff
- 00af34dc ["INT_ADD", "register:40f0:8", ["const:af34dc:8", "const:4:8"]]
- 00af34dc ["CALL", null, ["callee:005533e0:8"]]
+ 00af35a4 ["INT_ADD", "register:40f0:8", ["const:af35a4:8", "const:4:8"]]
+ 00af35a4 ["CALL", null, ["callee:005533e0:8"]]
- 00af34dc bytes c17fe997
+ 00af35a4 bytes 8f7fe997
- 00af35cc ["INT_ADD", "register:40f0:8", ["const:af35cc:8", "const:4:8"]]
- 00af35cc ["CALL", null, ["callee:0047495c:8"]]
+ 00af3694 ["INT_ADD", "register:40f0:8", ["const:af3694:8", "const:4:8"]]
+ 00af3694 ["CALL", null, ["callee:0047495c:8"]]
- 00af35cc bytes e404e697
+ 00af3694 bytes b204e697
- 00af361c ["INT_ADD", "register:40f0:8", ["const:af361c:8", "const:4:8"]]
- 00af361c ["CALL", null, ["callee:0047495c:8"]]
+ 00af36e4 ["INT_ADD", "register:40f0:8", ["const:af36e4:8", "const:4:8"]]
+ 00af36e4 ["CALL", null, ["callee:0047495c:8"]]
- 00af361c bytes d004e697
+ 00af36e4 bytes 9e04e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74549382a0a614b6f70dc44057103234"></a>

### [`00af379c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af379c.md) → [`00af3864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3864.md) _ZN8firebase4util21JavaListToVariantListEP7_JNIEnvPNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEEP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde520.md) · 呼出先 8件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md)
- 新版 呼出元 1件 [`00bde5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5d0.md) · 呼出先 8件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af38a0",
      "incomplete_value": true,
      "site": "00af38a8",
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
                "const:900:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af37d8",
      "incomplete_value": true,
      "site": "00af37e0",
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
                "const:840:8"
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
      "definition_site": "00af3968",
      "incomplete_value": true,
      "site": "00af3978",
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af38a0",
      "incomplete_value": true,
      "site": "00af38b0",
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af38a0",
      "READ",
      [
        "storage",
        "010a0840",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3968",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af38a0",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined8"
      ]
    ],
    [
      "00af3968",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af37e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af379c.md#insn-00af37e0) · [`00af38b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af379c.md#insn-00af38b0) · [`00af37d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af3/00af379c.md#insn-00af37d8)
- 新版 `00af38a8`（命令位置の公開資料なし） · `00af3978`（命令位置の公開資料なし） · `00af38a0`（命令位置の公開資料なし）

~~~diff
- 00af37e0 ["INT_ADD", "register:40f0:8", ["const:af37e0:8", "const:4:8"]]
- 00af37e0 ["CALL", null, ["callee:005533e0:8"]]
+ 00af38a8 ["INT_ADD", "register:40f0:8", ["const:af38a8:8", "const:4:8"]]
+ 00af38a8 ["CALL", null, ["callee:005533e0:8"]]
- 00af37e0 bytes 007fe997
+ 00af38a8 bytes ce7ee997
- 00af38b0 ["INT_ADD", "register:40f0:8", ["const:af38b0:8", "const:4:8"]]
- 00af38b0 ["CALL", null, ["callee:0047495c:8"]]
+ 00af3978 ["INT_ADD", "register:40f0:8", ["const:af3978:8", "const:4:8"]]
+ 00af3978 ["CALL", null, ["callee:0047495c:8"]]
- 00af38b0 bytes 2b04e697
+ 00af3978 bytes f903e697
- 00af37d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:840:8"]]
- 00af37d8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af38a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:900:8"]]
+ 00af38a0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af37d8 bytes 022144f9
+ 00af38a0 bytes 028144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1202ee3646c9f61907df039a0eb6dff"></a>

### [`00af4108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4108.md) → [`00af41d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af41d0.md) _ZN8firebase4util15JDoubleToDoubleEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde360.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af411c",
      "incomplete_value": true,
      "site": "00af4124",
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
                "const:698:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af4138"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00af4200"
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
      "00af41e4",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af4138",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00af41e4",
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined8"
      ]
    ],
    [
      "00af4200",
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

- 旧版 [`00af4124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4108.md#insn-00af4124) · [`00af4138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4108.md#insn-00af4138)
- 新版 `00af41ec`（命令位置の公開資料なし） · `00af4200`（命令位置の公開資料なし）

~~~diff
- 00af4124 ["INT_ADD", "register:40f0:8", ["const:af4124:8", "const:4:8"]]
- 00af4124 ["CALL", null, ["callee:00bde360:8"]]
+ 00af41ec ["INT_ADD", "register:40f0:8", ["const:af41ec:8", "const:4:8"]]
+ 00af41ec ["CALL", null, ["callee:00bde360:8"]]
- 00af4124 bytes 63a80394
+ 00af41ec bytes 5da80394
- 00af4138 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4138 ["INT_ADD", "register:40f0:8", ["const:af4138:8", "const:4:8"]]
- 00af4138 ["CALLIND", null, ["register:0:8"]]
- 00af4138 bytes 00013fd6
+ 00af4200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4200 ["INT_ADD", "register:40f0:8", ["const:af4200:8", "const:4:8"]]
+ 00af4200 ["CALLIND", null, ["register:0:8"]]
+ 00af4200 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21447d1a625511f1979e6f7ff5db38bd"></a>

### [`00af4214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4214.md) → [`00af42dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af42dc.md) _ZN8firebase4util15IsJBooleanArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af42f8",
      "incomplete_value": false,
      "site": "00af4304",
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
            "const:d73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4230",
      "incomplete_value": false,
      "site": "00af423c",
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
            "const:ce6:8"
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
      "00af42f8",
      "PARAM",
      [
        "storage",
        "0029bce6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af42f8",
      "PARAM",
      [
        "storage",
        "0029bd73",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af423c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4214.md#insn-00af423c) · [`00af4230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4214.md#insn-00af4230) · [`00af4258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4214.md#insn-00af4258)
- 新版 `00af4304`（命令位置の公開資料なし） · `00af42f8`（命令位置の公開資料なし） · `00af4320`（命令位置の公開資料なし）

~~~diff
- 00af423c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af423c ["INT_ADD", "register:40f0:8", ["const:af423c:8", "const:4:8"]]
- 00af423c ["CALLIND", null, ["register:0:8"]]
+ 00af4304 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4304 ["INT_ADD", "register:40f0:8", ["const:af4304:8", "const:4:8"]]
+ 00af4304 ["CALLIND", null, ["register:0:8"]]
- 00af423c bytes 00013fd6
+ 00af4304 bytes 00013fd6
- 00af4230 ["COPY", "tmp:0:8", ["const:ce6:8"]]
- 00af4230 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4230 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4230 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af42f8 ["COPY", "tmp:0:8", ["const:d73:8"]]
+ 00af42f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af42f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af42f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4230 bytes 21983391
+ 00af42f8 bytes 21cc3591
- 00af4258 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4258 ["INT_ADD", "register:40f0:8", ["const:af4258:8", "const:4:8"]]
- 00af4258 ["CALLIND", null, ["register:0:8"]]
+ 00af4320 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4320 ["INT_ADD", "register:40f0:8", ["const:af4320:8", "const:4:8"]]
+ 00af4320 ["CALLIND", null, ["register:0:8"]]
- 00af4258 bytes 00013fd6
+ 00af4320 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fce8d1b5359246fb531ab49f21bd373"></a>

### [`00af428c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af428c.md) → [`00af4354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4354.md) _ZN8firebase4util12IsJByteArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af4370",
      "incomplete_value": false,
      "site": "00af437c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:fab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af42a8",
      "incomplete_value": false,
      "site": "00af42b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:fa5:8"
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
      "00af4370",
      "PARAM",
      [
        "storage",
        "002aafa5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af4370",
      "PARAM",
      [
        "storage",
        "002aafab",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af42b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af428c.md#insn-00af42b4) · [`00af42a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af428c.md#insn-00af42a8) · [`00af42d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af428c.md#insn-00af42d0)
- 新版 `00af437c`（命令位置の公開資料なし） · `00af4370`（命令位置の公開資料なし） · `00af4398`（命令位置の公開資料なし）

~~~diff
- 00af42b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af42b4 ["INT_ADD", "register:40f0:8", ["const:af42b4:8", "const:4:8"]]
- 00af42b4 ["CALLIND", null, ["register:0:8"]]
+ 00af437c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af437c ["INT_ADD", "register:40f0:8", ["const:af437c:8", "const:4:8"]]
+ 00af437c ["CALLIND", null, ["register:0:8"]]
- 00af42b4 bytes 00013fd6
+ 00af437c bytes 00013fd6
- 00af42a8 ["COPY", "tmp:0:8", ["const:fa5:8"]]
- 00af42a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af42a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af42a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af4370 ["COPY", "tmp:0:8", ["const:fab:8"]]
+ 00af4370 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4370 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4370 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af42a8 bytes 21943e91
+ 00af4370 bytes 21ac3e91
- 00af42d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af42d0 ["INT_ADD", "register:40f0:8", ["const:af42d0:8", "const:4:8"]]
- 00af42d0 ["CALLIND", null, ["register:0:8"]]
+ 00af4398 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4398 ["INT_ADD", "register:40f0:8", ["const:af4398:8", "const:4:8"]]
+ 00af4398 ["CALLIND", null, ["register:0:8"]]
- 00af42d0 bytes 00013fd6
+ 00af4398 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c27ebec36a93edb1f75146df6512852"></a>

### [`00af4304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4304.md) → [`00af43cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af43cc.md) _ZN8firebase4util12IsJCharArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af43e8",
      "incomplete_value": false,
      "site": "00af43f4",
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
            "const:73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4320",
      "incomplete_value": false,
      "site": "00af432c",
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
            "const:7a:8"
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
      "00af43e8",
      "PARAM",
      [
        "storage",
        "002a607a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af43e8",
      "PARAM",
      [
        "storage",
        "002a6073",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af432c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4304.md#insn-00af432c) · [`00af4320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4304.md#insn-00af4320) · [`00af4348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4304.md#insn-00af4348)
- 新版 `00af43f4`（命令位置の公開資料なし） · `00af43e8`（命令位置の公開資料なし） · `00af4410`（命令位置の公開資料なし）

~~~diff
- 00af432c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af432c ["INT_ADD", "register:40f0:8", ["const:af432c:8", "const:4:8"]]
- 00af432c ["CALLIND", null, ["register:0:8"]]
+ 00af43f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af43f4 ["INT_ADD", "register:40f0:8", ["const:af43f4:8", "const:4:8"]]
+ 00af43f4 ["CALLIND", null, ["register:0:8"]]
- 00af432c bytes 00013fd6
+ 00af43f4 bytes 00013fd6
- 00af4320 ["COPY", "tmp:0:8", ["const:7a:8"]]
- 00af4320 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4320 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4320 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af43e8 ["COPY", "tmp:0:8", ["const:73:8"]]
+ 00af43e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af43e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af43e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4320 bytes 21e80191
+ 00af43e8 bytes 21cc0191
- 00af4348 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4348 ["INT_ADD", "register:40f0:8", ["const:af4348:8", "const:4:8"]]
- 00af4348 ["CALLIND", null, ["register:0:8"]]
+ 00af4410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4410 ["INT_ADD", "register:40f0:8", ["const:af4410:8", "const:4:8"]]
+ 00af4410 ["CALLIND", null, ["register:0:8"]]
- 00af4348 bytes 00013fd6
+ 00af4410 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b75dfa8a7fbe80c16c7b04a1db259ebf"></a>

### [`00af437c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af437c.md) → [`00af4444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4444.md) _ZN8firebase4util13IsJShortArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af4460",
      "incomplete_value": false,
      "site": "00af446c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:ce9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4398",
      "incomplete_value": false,
      "site": "00af43a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a3000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
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
      "00af4460",
      "PARAM",
      [
        "storage",
        "002a3cf0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af4460",
      "PARAM",
      [
        "storage",
        "002a3ce9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af43a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af437c.md#insn-00af43a4) · [`00af4398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af437c.md#insn-00af4398) · [`00af43c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af437c.md#insn-00af43c0)
- 新版 `00af446c`（命令位置の公開資料なし） · `00af4460`（命令位置の公開資料なし） · `00af4488`（命令位置の公開資料なし）

~~~diff
- 00af43a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af43a4 ["INT_ADD", "register:40f0:8", ["const:af43a4:8", "const:4:8"]]
- 00af43a4 ["CALLIND", null, ["register:0:8"]]
+ 00af446c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af446c ["INT_ADD", "register:40f0:8", ["const:af446c:8", "const:4:8"]]
+ 00af446c ["CALLIND", null, ["register:0:8"]]
- 00af43a4 bytes 00013fd6
+ 00af446c bytes 00013fd6
- 00af4398 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 00af4398 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4398 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4398 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af4460 ["COPY", "tmp:0:8", ["const:ce9:8"]]
+ 00af4460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4398 bytes 21c03391
+ 00af4460 bytes 21a43391
- 00af43c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af43c0 ["INT_ADD", "register:40f0:8", ["const:af43c0:8", "const:4:8"]]
- 00af43c0 ["CALLIND", null, ["register:0:8"]]
+ 00af4488 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4488 ["INT_ADD", "register:40f0:8", ["const:af4488:8", "const:4:8"]]
+ 00af4488 ["CALLIND", null, ["register:0:8"]]
- 00af43c0 bytes 00013fd6
+ 00af4488 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84886e51b908d3902b558095f49f471"></a>

### [`00af43f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af43f4.md) → [`00af44bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af44bc.md) _ZN8firebase4util11IsJIntArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af44d8",
      "incomplete_value": false,
      "site": "00af44e4",
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
            "const:fbd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4410",
      "incomplete_value": false,
      "site": "00af441c",
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
            "const:fb7:8"
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
      "00af44d8",
      "PARAM",
      [
        "storage",
        "002a9fb7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af44d8",
      "PARAM",
      [
        "storage",
        "002a9fbd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af441c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af43f4.md#insn-00af441c) · [`00af4410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af43f4.md#insn-00af4410) · [`00af4438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af43f4.md#insn-00af4438)
- 新版 `00af44e4`（命令位置の公開資料なし） · `00af44d8`（命令位置の公開資料なし） · `00af4500`（命令位置の公開資料なし）

~~~diff
- 00af441c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af441c ["INT_ADD", "register:40f0:8", ["const:af441c:8", "const:4:8"]]
- 00af441c ["CALLIND", null, ["register:0:8"]]
+ 00af44e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af44e4 ["INT_ADD", "register:40f0:8", ["const:af44e4:8", "const:4:8"]]
+ 00af44e4 ["CALLIND", null, ["register:0:8"]]
- 00af441c bytes 00013fd6
+ 00af44e4 bytes 00013fd6
- 00af4410 ["COPY", "tmp:0:8", ["const:fb7:8"]]
- 00af4410 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4410 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4410 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af44d8 ["COPY", "tmp:0:8", ["const:fbd:8"]]
+ 00af44d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af44d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af44d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4410 bytes 21dc3e91
+ 00af44d8 bytes 21f43e91
- 00af4438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4438 ["INT_ADD", "register:40f0:8", ["const:af4438:8", "const:4:8"]]
- 00af4438 ["CALLIND", null, ["register:0:8"]]
+ 00af4500 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4500 ["INT_ADD", "register:40f0:8", ["const:af4500:8", "const:4:8"]]
+ 00af4500 ["CALLIND", null, ["register:0:8"]]
- 00af4438 bytes 00013fd6
+ 00af4500 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e66fc39210f89f2f312c9b6454460ab8"></a>

### [`00af446c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af446c.md) → [`00af4534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4534.md) _ZN8firebase4util12IsJLongArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af4550",
      "incomplete_value": false,
      "site": "00af455c",
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
            "const:611:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4488",
      "incomplete_value": false,
      "site": "00af4494",
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
            "const:584:8"
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
      "00af4550",
      "PARAM",
      [
        "storage",
        "00298584",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af4550",
      "PARAM",
      [
        "storage",
        "00298611",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af4494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af446c.md#insn-00af4494) · [`00af4488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af446c.md#insn-00af4488) · [`00af44b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af446c.md#insn-00af44b0)
- 新版 `00af455c`（命令位置の公開資料なし） · `00af4550`（命令位置の公開資料なし） · `00af4578`（命令位置の公開資料なし）

~~~diff
- 00af4494 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4494 ["INT_ADD", "register:40f0:8", ["const:af4494:8", "const:4:8"]]
- 00af4494 ["CALLIND", null, ["register:0:8"]]
+ 00af455c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af455c ["INT_ADD", "register:40f0:8", ["const:af455c:8", "const:4:8"]]
+ 00af455c ["CALLIND", null, ["register:0:8"]]
- 00af4494 bytes 00013fd6
+ 00af455c bytes 00013fd6
- 00af4488 ["COPY", "tmp:0:8", ["const:584:8"]]
- 00af4488 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4488 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4488 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af4550 ["COPY", "tmp:0:8", ["const:611:8"]]
+ 00af4550 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4550 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4550 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4488 bytes 21101691
+ 00af4550 bytes 21441891
- 00af44b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af44b0 ["INT_ADD", "register:40f0:8", ["const:af44b0:8", "const:4:8"]]
- 00af44b0 ["CALLIND", null, ["register:0:8"]]
+ 00af4578 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4578 ["INT_ADD", "register:40f0:8", ["const:af4578:8", "const:4:8"]]
+ 00af4578 ["CALLIND", null, ["register:0:8"]]
- 00af44b0 bytes 00013fd6
+ 00af4578 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6200eeb5b721ac949e0acc33aee7668"></a>

### [`00af44e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af44e4.md) → [`00af45ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af45ac.md) _ZN8firebase4util13IsJFloatArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af45c8",
      "incomplete_value": false,
      "site": "00af45d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:74c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4500",
      "incomplete_value": false,
      "site": "00af450c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:6bf:8"
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
      "00af45c8",
      "PARAM",
      [
        "storage",
        "0029a6bf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af45c8",
      "PARAM",
      [
        "storage",
        "0029a74c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af450c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af44e4.md#insn-00af450c) · [`00af4500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af44e4.md#insn-00af4500) · [`00af4528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af44e4.md#insn-00af4528)
- 新版 `00af45d4`（命令位置の公開資料なし） · `00af45c8`（命令位置の公開資料なし） · `00af45f0`（命令位置の公開資料なし）

~~~diff
- 00af450c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af450c ["INT_ADD", "register:40f0:8", ["const:af450c:8", "const:4:8"]]
- 00af450c ["CALLIND", null, ["register:0:8"]]
+ 00af45d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af45d4 ["INT_ADD", "register:40f0:8", ["const:af45d4:8", "const:4:8"]]
+ 00af45d4 ["CALLIND", null, ["register:0:8"]]
- 00af450c bytes 00013fd6
+ 00af45d4 bytes 00013fd6
- 00af4500 ["COPY", "tmp:0:8", ["const:6bf:8"]]
- 00af4500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af45c8 ["COPY", "tmp:0:8", ["const:74c:8"]]
+ 00af45c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af45c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af45c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4500 bytes 21fc1a91
+ 00af45c8 bytes 21301d91
- 00af4528 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4528 ["INT_ADD", "register:40f0:8", ["const:af4528:8", "const:4:8"]]
- 00af4528 ["CALLIND", null, ["register:0:8"]]
+ 00af45f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af45f0 ["INT_ADD", "register:40f0:8", ["const:af45f0:8", "const:4:8"]]
+ 00af45f0 ["CALLIND", null, ["register:0:8"]]
- 00af4528 bytes 00013fd6
+ 00af45f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d51e3b635d744b80c1b393a59e464c87"></a>

### [`00af455c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af455c.md) → [`00af4624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4624.md) _ZN8firebase4util14IsJDoubleArrayEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af4640",
      "incomplete_value": false,
      "site": "00af464c",
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
            "const:693:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af4578",
      "incomplete_value": false,
      "site": "00af4584",
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
            "const:606:8"
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
      "00af4640",
      "PARAM",
      [
        "storage",
        "00299606",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af4640",
      "PARAM",
      [
        "storage",
        "00299693",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af4584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af455c.md#insn-00af4584) · [`00af4578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af455c.md#insn-00af4578) · [`00af45a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af455c.md#insn-00af45a0)
- 新版 `00af464c`（命令位置の公開資料なし） · `00af4640`（命令位置の公開資料なし） · `00af4668`（命令位置の公開資料なし）

~~~diff
- 00af4584 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4584 ["INT_ADD", "register:40f0:8", ["const:af4584:8", "const:4:8"]]
- 00af4584 ["CALLIND", null, ["register:0:8"]]
+ 00af464c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af464c ["INT_ADD", "register:40f0:8", ["const:af464c:8", "const:4:8"]]
+ 00af464c ["CALLIND", null, ["register:0:8"]]
- 00af4584 bytes 00013fd6
+ 00af464c bytes 00013fd6
- 00af4578 ["COPY", "tmp:0:8", ["const:606:8"]]
- 00af4578 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00af4578 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00af4578 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00af4640 ["COPY", "tmp:0:8", ["const:693:8"]]
+ 00af4640 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4640 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00af4640 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00af4578 bytes 21181891
+ 00af4640 bytes 214c1a91
- 00af45a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af45a0 ["INT_ADD", "register:40f0:8", ["const:af45a0:8", "const:4:8"]]
- 00af45a0 ["CALLIND", null, ["register:0:8"]]
+ 00af4668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4668 ["INT_ADD", "register:40f0:8", ["const:af4668:8", "const:4:8"]]
+ 00af4668 ["CALLIND", null, ["register:0:8"]]
- 00af45a0 bytes 00013fd6
+ 00af4668 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c0d5bbda10ee2bfc158f95f1b7f9ea"></a>

### [`00af48d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af48d4.md) → [`00af499c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af499c.md) _ZN8firebase4util19JCharArrayToVariantEP7_JNIEnvP11_jcharArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bde460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde460.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde510.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 78.57% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af49a0",
      "incomplete_value": true,
      "site": "00af49ac",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af49a4",
      "incomplete_value": false,
      "site": "00af49ac",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af49ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af48d4.md#insn-00af49ac) · [`00af4914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af48d4.md#insn-00af4914) · [`00af4930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af48d4.md#insn-00af4930)
- 新版 `00af4a74`（命令位置の公開資料なし） · `00af49dc`（命令位置の公開資料なし） · `00af49f8`（命令位置の公開資料なし）

~~~diff
- 00af49ac ["INT_ADD", "register:40f0:8", ["const:af49ac:8", "const:4:8"]]
- 00af49ac ["CALL", null, ["callee:00bdd990:8"]]
+ 00af4a74 ["INT_ADD", "register:40f0:8", ["const:af4a74:8", "const:4:8"]]
+ 00af4a74 ["CALL", null, ["callee:00bdd990:8"]]
- 00af49ac bytes cda30394
+ 00af4a74 bytes c7a30394
- 00af4914 ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4914 ["INT_ADD", "register:40f0:8", ["const:af4914:8", "const:4:8"]]
- 00af4914 ["CALLIND", null, ["register:0:8"]]
+ 00af49dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af49dc ["INT_ADD", "register:40f0:8", ["const:af49dc:8", "const:4:8"]]
+ 00af49dc ["CALLIND", null, ["register:0:8"]]
- 00af4914 bytes 20013fd6
+ 00af49dc bytes 20013fd6
- 00af4930 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4930 ["INT_ADD", "register:40f0:8", ["const:af4930:8", "const:4:8"]]
- 00af4930 ["CALLIND", null, ["register:0:8"]]
+ 00af49f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af49f8 ["INT_ADD", "register:40f0:8", ["const:af49f8:8", "const:4:8"]]
+ 00af49f8 ["CALLIND", null, ["register:0:8"]]
- 00af4930 bytes 00013fd6
+ 00af49f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4373d62c1cda474b68fe5d8ac35c3eb"></a>

### [`00af4d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4d4c.md) → [`00af4e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4e14.md) _ZN8firebase4util19JLongArrayToVariantEP7_JNIEnvP11_jlongArray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bde470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde470.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde520.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af4e14",
      "incomplete_value": true,
      "site": "00af4e20",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af4e18",
      "incomplete_value": false,
      "site": "00af4e20",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "ordinal": 4,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af4e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4d4c.md#insn-00af4e20) · [`00af4d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4d4c.md#insn-00af4d8c) · [`00af4da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af4/00af4d4c.md#insn-00af4da8)
- 新版 `00af4ee8`（命令位置の公開資料なし） · `00af4e54`（命令位置の公開資料なし） · `00af4e70`（命令位置の公開資料なし）

~~~diff
- 00af4e20 ["INT_ADD", "register:40f0:8", ["const:af4e20:8", "const:4:8"]]
- 00af4e20 ["CALL", null, ["callee:00bdd990:8"]]
+ 00af4ee8 ["INT_ADD", "register:40f0:8", ["const:af4ee8:8", "const:4:8"]]
+ 00af4ee8 ["CALL", null, ["callee:00bdd990:8"]]
- 00af4e20 bytes b0a20394
+ 00af4ee8 bytes aaa20394
- 00af4d8c ["COPY", "register:0:8", ["register:4048:8"]]
- 00af4d8c ["INT_ADD", "register:40f0:8", ["const:af4d8c:8", "const:4:8"]]
- 00af4d8c ["CALLIND", null, ["register:0:8"]]
+ 00af4e54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00af4e54 ["INT_ADD", "register:40f0:8", ["const:af4e54:8", "const:4:8"]]
+ 00af4e54 ["CALLIND", null, ["register:0:8"]]
- 00af4d8c bytes 20013fd6
+ 00af4e54 bytes 20013fd6
- 00af4da8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af4da8 ["INT_ADD", "register:40f0:8", ["const:af4da8:8", "const:4:8"]]
- 00af4da8 ["CALLIND", null, ["register:0:8"]]
+ 00af4e70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af4e70 ["INT_ADD", "register:40f0:8", ["const:af4e70:8", "const:4:8"]]
+ 00af4e70 ["CALLIND", null, ["register:0:8"]]
- 00af4da8 bytes 00013fd6
+ 00af4e70 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1afd0f2de72c787e308472b03634c917"></a>

### [`00af531c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af531c.md) → [`00af53e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af53e4.md) _ZN8firebase4util15JArrayToVariantEP7_JNIEnvP7_jarray

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde380.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde430.md) [`00bde450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde450.md) [`00bde460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde460.md)
- 新版 呼出元 1件 [`00bde430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde430.md) · 呼出先 11件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4e0.md) [`00bde500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde500.md) [`00bde510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde510.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 59.78% / 新版 59.78%

CFGの説明率　旧版 30.00% / 新版 25.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 16件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af54f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5560"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af55d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af5414",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af547c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00af53c4"
      ]
    ],
    [
      "00af5484",
      "PARAM",
      [
        "storage",
        "0029531a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af5414",
      "READ",
      [
        "storage",
        "010a0668",
        null,
        "undefined8"
      ]
    ],
    [
      "00af547c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af548c"
      ]
    ],
    [
      "00af5484",
      "PARAM",
      [
        "storage",
        "002953a7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af535c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af531c.md#insn-00af535c) · [`00af53c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af531c.md#insn-00af53c0) · [`00af53d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af531c.md#insn-00af53d8)
- 新版 `00af5424`（命令位置の公開資料なし） · `00af5488`（命令位置の公開資料なし） · `00af54a0`（命令位置の公開資料なし）

~~~diff
- 00af535c ["INT_ADD", "register:40f0:8", ["const:af535c:8", "const:4:8"]]
- 00af535c ["CALL", null, ["callee:00474b70:8"]]
+ 00af5424 ["INT_ADD", "register:40f0:8", ["const:af5424:8", "const:4:8"]]
+ 00af5424 ["CALL", null, ["callee:00474b70:8"]]
- 00af535c bytes 05fee597
+ 00af5424 bytes d3fde597
- 00af53c0 ["INT_ADD", "register:40f0:8", ["const:af53c0:8", "const:4:8"]]
- 00af53c0 ["CALL", null, ["callee:00bde130:8"]]
+ 00af5488 ["INT_ADD", "register:40f0:8", ["const:af5488:8", "const:4:8"]]
+ 00af5488 ["CALL", null, ["callee:00bde130:8"]]
- 00af53c0 bytes 30a30394
+ 00af5488 bytes 2aa30394
- 00af53d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af53d8 ["INT_ADD", "register:40f0:8", ["const:af53d8:8", "const:4:8"]]
- 00af53d8 ["CALLIND", null, ["register:0:8"]]
+ 00af54a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af54a0 ["INT_ADD", "register:40f0:8", ["const:af54a0:8", "const:4:8"]]
+ 00af54a0 ["CALLIND", null, ["register:0:8"]]
- 00af53d8 bytes 00013fd6
+ 00af54a0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66660c7a6965c8f0f68c0ff6d317abfc"></a>

### [`00af57bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af57bc.md) → [`00af5884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5884.md) _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde370.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 1件 [`00bde420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde420.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 37.50% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af57d8",
      "incomplete_value": true,
      "site": "00af57e4",
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
                "const:970:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af57f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5834"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af58a0",
      "READ",
      [
        "storage",
        "010a0970",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af5878",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00af5880",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde6f0"
      ]
    ]
  ],
  "added": [
    [
      "00af58a0",
      "READ",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00af5940",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00af5948",
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

- 旧版 [`00af57e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af57bc.md#insn-00af57e4) · [`00af57f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af57bc.md#insn-00af57f8) · [`00af5834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af57bc.md#insn-00af5834)
- 新版 `00af58ac`（命令位置の公開資料なし）

~~~diff
- 00af57e4 ["INT_ADD", "register:40f0:8", ["const:af57e4:8", "const:4:8"]]
- 00af57e4 ["CALL", null, ["callee:0047495c:8"]]
+ 00af58ac ["INT_ADD", "register:40f0:8", ["const:af58ac:8", "const:4:8"]]
+ 00af58ac ["CALL", null, ["callee:0047495c:8"]]
- 00af57e4 bytes 5efce597
+ 00af58ac bytes 2cfce597
- 00af57f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af57f8 ["INT_ADD", "register:40f0:8", ["const:af57f8:8", "const:4:8"]]
- 00af57f8 ["CALLIND", null, ["register:0:8"]]
- 00af57f8 bytes 00013fd6
- 00af5834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5834 ["INT_ADD", "register:40f0:8", ["const:af5834:8", "const:4:8"]]
- 00af5834 ["CALLIND", null, ["register:0:8"]]
- 00af5834 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8459e2ff7ff2a79fe8efaa23c2d9446b"></a>

### [`00af5884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5884.md) → [`00af594c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af594c.md) _ZN8firebase4util13CharsToJniUriEP7_JNIEnvPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde330.md) · 呼出先 2件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md)
- 新版 呼出元 1件 [`00bde3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3e0.md) · 呼出先 2件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 4.17% / 新版 4.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5884",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5888",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af588c",
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
      "00af594c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00af5950",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af5954",
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

- 旧版 [`00af5884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5884.md#insn-00af5884) · [`00af5888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5884.md#insn-00af5888) · [`00af588c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5884.md#insn-00af588c)

~~~diff
- 00af5884 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00af5884 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00af5884 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5884 bytes f70f1cf8
- 00af5888 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af5888 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af5888 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5888 bytes f65701a9
- 00af588c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af588c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af588c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af588c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af588c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ede11f2b5385b3a346a77e27a225b61"></a>

### [`00af5a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5a3c.md) → [`00af5b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5b04.md) _ZN8firebase4util10CharsToURLEP7_JNIEnvPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.10% / 新版 56.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5a3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5a40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5a40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5a3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5a40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5a44",
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
      "00af5b04",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af5b08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af5b0c",
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

- 旧版 [`00af5a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5a3c.md#insn-00af5a3c) · [`00af5a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5a3c.md#insn-00af5a40) · [`00af5a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5a3c.md#insn-00af5a44)

~~~diff
- 00af5a3c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af5a3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af5a3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5a3c bytes f50f1df8
- 00af5a40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5a40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5a40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5a40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5a40 bytes f44f01a9
- 00af5a44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5a44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5a44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5a44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5a44 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99197230974e91cb34d43cfa0db37c7c"></a>

### [`00af5ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5ae0.md) → [`00af5ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ba8.md) _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4f0.md) · 呼出先 1件 [`00bde6e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6e0.md)
- 新版 呼出元 1件 [`00bde5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde5a0.md) · 呼出先 1件 [`00bde790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde790.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5ae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5ae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5ae4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5ae0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5b0c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af5bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af5bd4",
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

- 旧版 [`00af5ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5ae0.md#insn-00af5ae0) · [`00af5ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5ae0.md#insn-00af5ae4) · [`00af5b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5ae0.md#insn-00af5b0c)

~~~diff
- 00af5ae0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af5ae0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af5ae0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af5ae0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5ae0 bytes f657bda9
- 00af5ae4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af5ae4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af5ae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5ae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5ae4 bytes f44f01a9
- 00af5b0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af5b0c ["INT_ADD", "register:40f0:8", ["const:af5b0c:8", "const:4:8"]]
- 00af5b0c ["CALLIND", null, ["register:0:8"]]
- 00af5b0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea3d5bf863f49fa5e2d6629b983ce52c"></a>

### [`00af5bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bc0.md) → [`00af5c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5c88.md) _ZN8firebase4util15ContinueBuilderEP7_JNIEnvP8_jobjectS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5bc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5bc4",
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
      "00af5c88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af5c8c",
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

- 旧版 [`00af5bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bc0.md#insn-00af5bc0) · [`00af5bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bc0.md#insn-00af5bc4)
- 新版 `00af5c88`（命令位置の公開資料なし）

~~~diff
- 00af5bc0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00af5bc0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af5bc0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5bc0 bytes f30f1ef8
- 00af5bc4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5bc4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5bc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5bc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5bc4 bytes fd7b01a9
+ 00af5c88 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00af5c88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00af5c88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00af5c88 bytes f30f1ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-293dbdef66039b6c1c8c6b6fdfa34841"></a>

### [`00af5bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bec.md) → [`00af5cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5cb4.md) _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfc0.md) · 呼出先 6件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md)
- 新版 呼出元 1件 [`00bde070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde070.md) · 呼出先 6件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.15% / 新版 76.15%

CFGの説明率　旧版 12.00% / 新版 16.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5bf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5bf4",
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
      "00af5cb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00af5cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00af5cbc",
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

- 旧版 [`00af5bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bec.md#insn-00af5bec) · [`00af5bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bec.md#insn-00af5bf0) · [`00af5bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5bec.md#insn-00af5bf4)

~~~diff
- 00af5bec ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00af5bec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00af5bec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5bec bytes fb0f1af8
- 00af5bf0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af5bf0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af5bf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5bf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5bf0 bytes fa6701a9
- 00af5bf4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af5bf4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af5bf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af5bf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5bf4 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-894c9f2c0599fad4c3b4a1ee32757ed2"></a>

### [`00af5df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md) → [`00af5ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ebc.md) _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af5f08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af5eec",
      "incomplete_value": false,
      "site": "00af5f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af5e24",
      "incomplete_value": false,
      "site": "00af5e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:9c8:8"
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
      "unmatched:00af5e24",
      "PARAM",
      [
        "storage",
        "010a09c8",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af5f58",
      "PARAM",
      [
        "storage",
        "010a09c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af5eec",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ],
    [
      "00af5f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af5f58",
      "PARAM",
      [
        "storage",
        "010a0a88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md#insn-00af5e40) · [`00af5e44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md#insn-00af5e44) · [`00af5e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md#insn-00af5e94)
- 新版 `00af5f0c`（命令位置の公開資料なし） · `00af5f5c`（命令位置の公開資料なし）

~~~diff
- 00af5e40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00af5e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af5e40 bytes e80f00f9
- 00af5e44 ["INT_ADD", "register:40f0:8", ["const:af5e44:8", "const:4:8"]]
- 00af5e44 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00af5f0c ["INT_ADD", "register:40f0:8", ["const:af5f0c:8", "const:4:8"]]
+ 00af5f0c ["CALL", null, ["callee:00bde7d0:8"]]
- 00af5e44 bytes 37a20394
+ 00af5f0c bytes 31a20394
- 00af5e94 ["INT_ADD", "register:40f0:8", ["const:af5e94:8", "const:4:8"]]
- 00af5e94 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00af5f5c ["INT_ADD", "register:40f0:8", ["const:af5f5c:8", "const:4:8"]]
+ 00af5f5c ["CALL", null, ["callee:00bde7e0:8"]]
- 00af5e94 bytes 27a20394
+ 00af5f5c bytes 21a20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8225eef77d577dc206c26375814867c"></a>

### [`00af5f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f24.md) → [`00af5fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5fec.md) _ZN8firebase4util41CppThreadDispatcherContext_nativeFunctionEP7_JNIEnvP8_jobjectll

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-30b0ad2259c2decd2673cf43e26404d5"></a>

### [`00af5f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f34.md) → [`00af5ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ffc.md) _ZN8firebase4util17JavaThreadContext6CancelEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bde260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde310.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.33% / 新版 63.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5f38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af601c",
      "READ",
      [
        "storage",
        "010a02d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af5ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6000",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af601c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f34.md#insn-00af5f34) · [`00af5f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f34.md#insn-00af5f38) · [`00af5f5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5f34.md#insn-00af5f5c)
- 新版 `00af6024`（命令位置の公開資料なし）

~~~diff
- 00af5f34 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00af5f34 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af5f34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5f34 bytes f30f1ef8
- 00af5f38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5f38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5f38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5f38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5f38 bytes fd7b01a9
- 00af5f5c ["INT_ADD", "register:40f0:8", ["const:af5f5c:8", "const:4:8"]]
- 00af5f5c ["CALL", null, ["callee:00551e14:8"]]
+ 00af6024 ["INT_ADD", "register:40f0:8", ["const:af6024:8", "const:4:8"]]
+ 00af6024 ["CALL", null, ["callee:00551e14:8"]]
- 00af5f5c bytes ae6fe997
+ 00af6024 bytes 7c6fe997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34e34724fa6ee2107e48e8d7b1e5f377"></a>

### [`00af5fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5fac.md) → [`00af6074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6074.md) _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bde260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde310.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5fb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af5fb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af5fac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5fb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af5fcc",
      "READ",
      [
        "storage",
        "010a02d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af6074",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6078",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af6094",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af5fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5fac.md#insn-00af5fac) · [`00af5fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5fac.md#insn-00af5fb0) · [`00af5fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5fac.md#insn-00af5fd4)
- 新版 `00af609c`（命令位置の公開資料なし）

~~~diff
- 00af5fac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00af5fac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af5fac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af5fac bytes f30f1ef8
- 00af5fb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af5fb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af5fb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af5fb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af5fb0 bytes fd7b01a9
- 00af5fd4 ["INT_ADD", "register:40f0:8", ["const:af5fd4:8", "const:4:8"]]
- 00af5fd4 ["CALL", null, ["callee:00551e14:8"]]
+ 00af609c ["INT_ADD", "register:40f0:8", ["const:af609c:8", "const:4:8"]]
+ 00af609c ["CALL", null, ["callee:00551e14:8"]]
- 00af5fd4 bytes 906fe997
+ 00af609c bytes 5e6fe997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b1d691c3050ac80246d8c67d34e3524"></a>

### [`00af6024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6024.md) → [`00af60ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af60ec.md) _ZN8firebase4util17JavaThreadContext24AcquireExecuteCancelLockEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bde260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde260.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde310.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af610c",
      "incomplete_value": true,
      "site": "00af6114",
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6064"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af607c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af610c",
      "READ",
      [
        "storage",
        "010a02e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6064",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00af607c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00af610c",
      "READ",
      [
        "storage",
        "010a03a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af612c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "00af6144",
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

- 旧版 [`00af604c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6024.md#insn-00af604c) · [`00af6064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6024.md#insn-00af6064) · [`00af607c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6024.md#insn-00af607c)
- 新版 `00af6114`（命令位置の公開資料なし）

~~~diff
- 00af604c ["INT_ADD", "register:40f0:8", ["const:af604c:8", "const:4:8"]]
- 00af604c ["CALL", null, ["callee:00474b70:8"]]
+ 00af6114 ["INT_ADD", "register:40f0:8", ["const:af6114:8", "const:4:8"]]
+ 00af6114 ["CALL", null, ["callee:00474b70:8"]]
- 00af604c bytes c9fae597
+ 00af6114 bytes 97fae597
- 00af6064 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af6064 ["INT_ADD", "register:40f0:8", ["const:af6064:8", "const:4:8"]]
- 00af6064 ["CALLIND", null, ["register:0:8"]]
- 00af6064 bytes 00013fd6
- 00af607c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af607c ["INT_ADD", "register:40f0:8", ["const:af607c:8", "const:4:8"]]
- 00af607c ["CALLIND", null, ["register:0:8"]]
- 00af607c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b7e3230959253b8299900c93a8441e"></a>

### [`00af60a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af60a8.md) → [`00af6170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6170.md) _ZN8firebase4util17JavaThreadContext9TerminateEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde400.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bde4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4b0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 7.04% / 新版 7.04%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af60ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af60a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af60ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af60b0",
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
      "00af6170",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af6174",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af6178",
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

- 旧版 [`00af60a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af60a8.md#insn-00af60a8) · [`00af60ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af60a8.md#insn-00af60ac) · [`00af60b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af60a8.md#insn-00af60b0)

~~~diff
- 00af60a8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00af60a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af60a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af60a8 bytes f50f1df8
- 00af60ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af60ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af60ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af60ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af60ac bytes f44f01a9
- 00af60b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af60b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af60b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af60b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af60b0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02713ba22aff18f6e6a3a45fe03fe3dd"></a>

### [`00af61c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af61c4.md) → [`00af628c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af628c.md) _ZN8firebase4util17JavaThreadContext13SetupInstanceEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bde200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af62b4",
      "incomplete_value": true,
      "site": "00af62c0",
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af61ec",
      "incomplete_value": true,
      "site": "00af61f8",
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
                "const:2b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af62b8",
      "incomplete_value": true,
      "site": "00af62c0",
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
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af61f0",
      "incomplete_value": true,
      "site": "00af61f8",
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
                "const:2c8:8"
              ]
            ]
          ]
        ]
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
      "unmatched:00af61ec",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af61f0",
      "READ",
      [
        "storage",
        "010a02c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af62b4",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af62b8",
      "READ",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af61f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af61c4.md#insn-00af61f8) · [`00af61ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af61c4.md#insn-00af61ec) · [`00af61f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af61c4.md#insn-00af61f0)
- 新版 `00af62c0`（命令位置の公開資料なし）

~~~diff
- 00af61f8 ["INT_ADD", "register:40f0:8", ["const:af61f8:8", "const:4:8"]]
- 00af61f8 ["CALL", null, ["callee:0056681c:8"]]
+ 00af62c0 ["INT_ADD", "register:40f0:8", ["const:af62c0:8", "const:4:8"]]
+ 00af62c0 ["CALL", null, ["callee:0056681c:8"]]
- 00af61f8 bytes 89c1e997
+ 00af62c0 bytes 57c1e997
- 00af61ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b8:8"]]
- 00af61ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af61ec bytes 015d41f9
- 00af61f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2c8:8"]]
- 00af61f0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00af61f0 bytes 226541f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ec8e5f2504e5aefc123823e63dad7b7"></a>

### [`00af625c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af625c.md) → [`00af6324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6324.md) _ZN8firebase4util17JavaThreadContext15RunOnMainThreadEP7_JNIEnvP8_jobjectPFvPvES6_S8_PS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3e0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bde200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde200.md) [`00bde2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00bde490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde490.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md) [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 71.88% / 新版 71.88%

CFGの説明率　旧版 25.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af62b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af6378"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af6288",
      "incomplete_value": true,
      "site": "00af6294",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:2b8:8"
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
      "unmatched:00af6288",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af628c",
      "READ",
      [
        "storage",
        "010a02c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af62b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af639c"
      ]
    ]
  ],
  "added": [
    [
      "00af6350",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6354",
      "READ",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6378",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af639c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af625c.md#insn-00af6294) · [`00af62a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af625c.md#insn-00af62a8) · [`00af62b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af625c.md#insn-00af62b0)
- 新版 `00af635c`（命令位置の公開資料なし）

~~~diff
- 00af6294 ["INT_ADD", "register:40f0:8", ["const:af6294:8", "const:4:8"]]
- 00af6294 ["CALL", null, ["callee:0056681c:8"]]
+ 00af635c ["INT_ADD", "register:40f0:8", ["const:af635c:8", "const:4:8"]]
+ 00af635c ["CALL", null, ["callee:0056681c:8"]]
- 00af6294 bytes 62c1e997
+ 00af635c bytes 30c1e997
- 00af62a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af62a8 ["INT_ADD", "register:40f0:8", ["const:af62a8:8", "const:4:8"]]
- 00af62a8 ["CALLIND", null, ["register:0:8"]]
- 00af62a8 bytes 00013fd6
- 00af62b0 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00af62b0 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22eb606deda534a68a5b30530db60a69"></a>

### [`00af635c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af635c.md) → [`00af6424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6424.md) _ZN8firebase4util17JavaThreadContext21RunOnBackgroundThreadEP7_JNIEnvPFvPvES4_S6_PS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde3f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3f0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bde200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde200.md) [`00bde2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00bde4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4a0.md) · 呼出先 3件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2b0.md) [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.35% / 新版 69.35%

CFGの説明率　旧版 8.33% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af63ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6410"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af6474"
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
      "unmatched:00af6384",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6388",
      "READ",
      [
        "storage",
        "010a02c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af63ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af6498"
      ]
    ]
  ],
  "added": [
    [
      "00af644c",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6450",
      "READ",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6474",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af6498"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af635c.md#insn-00af6390) · [`00af63ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af635c.md#insn-00af63ac) · [`00af63bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af635c.md#insn-00af63bc)
- 新版 `00af6458`（命令位置の公開資料なし）

~~~diff
- 00af6390 ["INT_ADD", "register:40f0:8", ["const:af6390:8", "const:4:8"]]
- 00af6390 ["CALL", null, ["callee:0056681c:8"]]
+ 00af6458 ["INT_ADD", "register:40f0:8", ["const:af6458:8", "const:4:8"]]
+ 00af6458 ["CALL", null, ["callee:0056681c:8"]]
- 00af6390 bytes 23c1e997
+ 00af6458 bytes f1c0e997
- 00af63ac ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00af63ac bytes 20010054
- 00af63bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00af63bc ["INT_ADD", "register:40f0:8", ["const:af63bc:8", "const:4:8"]]
- 00af63bc ["CALLIND", null, ["register:0:8"]]
- 00af63bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a60144e59b6b8853c816259910087749"></a>

### [`00af65e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af65e0.md) → [`00af66a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af66a8.md) _ZN8firebase4util16FindClassInFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3b0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bde460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde460.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.55% / 新版 74.55%

CFGの説明率　旧版 30.43% / 新版 29.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 16件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af65f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af65f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af65f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6608",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af66bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af66c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af66d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af65f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af65e0.md#insn-00af65f4) · [`00af65f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af65e0.md#insn-00af65f8) · [`00af6608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af65e0.md#insn-00af6608)

~~~diff
- 00af65f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af65f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af65f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00af65f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af65f4 bytes f44f0ea9
- 00af65f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af65f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af65f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00af65f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af65f8 bytes fd7b0fa9
- 00af6608 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af6608 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa8:8"]]
- 00af6608 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af6608 bytes a8831af8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-093ceee741580591bd22c74c8180ca35"></a>

### [`00af6ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6ce0.md) → [`00af6da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6da8.md) _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6f0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7a0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.53% / 新版 85.53%

CFGの説明率　旧版 34.48% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6ce0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6ce0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6ce4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6ce0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6ce4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6ce8",
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
      "00af6da8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00af6dac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af6db0",
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

- 旧版 [`00af6ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6ce0.md#insn-00af6ce0) · [`00af6ce4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6ce0.md#insn-00af6ce4) · [`00af6ce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6ce0.md#insn-00af6ce8)

~~~diff
- 00af6ce0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af6ce0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af6ce0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00af6ce0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6ce0 bytes f85fbca9
- 00af6ce4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af6ce4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af6ce4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af6ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6ce4 bytes f65701a9
- 00af6ce8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6ce8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6ce8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6ce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6ce8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-165da5d2d4d40df130dba6acc7368fa4"></a>

### [`00af6e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6e10.md) → [`00af6ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af6/00af6ed8.md) _ZN8firebase4util25GetResourceIdFromActivityEP7_JNIEnvP8_jobjectPKcNS0_12ResourceTypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 55.45% / 新版 55.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 10件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af6f20"
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
      "unmatched:00af6e2c",
      "READ",
      [
        "storage",
        "010a0440",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af6e58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af6f44"
      ]
    ],
    [
      "00af6f48",
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
      "00af6ef4",
      "READ",
      [
        "storage",
        "010a0500",
        null,
        "undefined8"
      ]
    ],
    [
      "00af6f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af6f44"
      ]
    ],
    [
      "00af6f48",
      "READ",
      [
        "storage",
        "010a04f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af6e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6e10.md#insn-00af6e3c) · [`00af6e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6e10.md#insn-00af6e50) · [`00af6e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6e10.md#insn-00af6e58)
- 新版 `00af6f04`（命令位置の公開資料なし）

~~~diff
- 00af6e3c ["INT_ADD", "register:40f0:8", ["const:af6e3c:8", "const:4:8"]]
- 00af6e3c ["CALL", null, ["callee:0047495c:8"]]
+ 00af6f04 ["INT_ADD", "register:40f0:8", ["const:af6f04:8", "const:4:8"]]
+ 00af6f04 ["CALL", null, ["callee:0047495c:8"]]
- 00af6e3c bytes c8f6e597
+ 00af6f04 bytes 96f6e597
- 00af6e50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af6e50 ["INT_ADD", "register:40f0:8", ["const:af6e50:8", "const:4:8"]]
- 00af6e50 ["CALLIND", null, ["register:0:8"]]
- 00af6e50 bytes 00013fd6
- 00af6e58 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00af6e58 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60bac0efab9e5392c80c778a630921d3"></a>

### [`00af6fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6fc8.md) → [`00af7090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7090.md) _ZN8firebase4util29GetResourceStringFromActivityEP7_JNIEnvP8_jobjecti

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 42.86% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af6fcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af6fc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6fcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af6fd0",
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
      "00af7090",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00af7094",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af7098",
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

- 旧版 [`00af6fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6fc8.md#insn-00af6fc8) · [`00af6fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6fc8.md#insn-00af6fcc) · [`00af6fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af6/00af6fc8.md#insn-00af6fd0)

~~~diff
- 00af6fc8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af6fc8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af6fc8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00af6fc8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af6fc8 bytes f657bda9
- 00af6fcc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af6fcc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af6fcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af6fcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6fcc bytes f44f01a9
- 00af6fd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af6fd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af6fd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af6fd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af6fd0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a6d55730d4868d65114d59527651d9b"></a>

### [`00af7190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7190.md) → [`00af7258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7258.md) _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfd0.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 1件 [`00bde080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde080.md) · 呼出先 3件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 85.00% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af7274",
      "incomplete_value": true,
      "site": "00af7280",
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
                "const:a00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af71ac",
      "incomplete_value": true,
      "site": "00af71b8",
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
                "const:940:8"
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
      "definition_site": "00af72c8",
      "incomplete_value": true,
      "site": "00af72d4",
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
                "const:a08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af7200",
      "incomplete_value": true,
      "site": "00af720c",
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
                "const:948:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7278"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af7274",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined8"
      ]
    ],
    [
      "00af72c8",
      "READ",
      [
        "storage",
        "010a0948",
        null,
        "undefined8"
      ]
    ],
    [
      "00af7348",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af7274",
      "READ",
      [
        "storage",
        "010a0a00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af72c8",
      "READ",
      [
        "storage",
        "010a0a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00af7348",
      "READ",
      [
        "storage",
        "010a0a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af71b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7190.md#insn-00af71b8) · [`00af720c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7190.md#insn-00af720c) · [`00af7278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7190.md#insn-00af7278)
- 新版 `00af7280`（命令位置の公開資料なし） · `00af72d4`（命令位置の公開資料なし）

~~~diff
- 00af71b8 ["INT_ADD", "register:40f0:8", ["const:af71b8:8", "const:4:8"]]
- 00af71b8 ["CALL", null, ["callee:0047495c:8"]]
+ 00af7280 ["INT_ADD", "register:40f0:8", ["const:af7280:8", "const:4:8"]]
+ 00af7280 ["CALL", null, ["callee:0047495c:8"]]
- 00af71b8 bytes e9f5e597
+ 00af7280 bytes b7f5e597
- 00af720c ["INT_ADD", "register:40f0:8", ["const:af720c:8", "const:4:8"]]
- 00af720c ["CALL", null, ["callee:0047495c:8"]]
+ 00af72d4 ["INT_ADD", "register:40f0:8", ["const:af72d4:8", "const:4:8"]]
+ 00af72d4 ["CALL", null, ["callee:0047495c:8"]]
- 00af720c bytes d4f5e597
+ 00af72d4 bytes a2f5e597
- 00af7278 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af7278 ["INT_ADD", "register:40f0:8", ["const:af7278:8", "const:4:8"]]
- 00af7278 ["CALLIND", null, ["register:0:8"]]
- 00af7278 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cacc7964ad434fc8c2dcfa046a16a75"></a>

### [`00af7334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7334.md) → [`00af73fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af73fc.md) _ZN8firebase4util12LogExceptionEP7_JNIEnvNS_8LogLevelEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf60.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md) [`00bde140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde140.md)
- 新版 呼出元 1件 [`00bde010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde010.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.58% / 新版 63.58%

CFGの説明率　旧版 36.36% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 26件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7338"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7338"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af733c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7338",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af733c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af7340",
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
      "00af7400",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00af7404",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00af7408",
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

- 旧版 [`00af7338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7334.md#insn-00af7338) · [`00af733c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7334.md#insn-00af733c) · [`00af7340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7334.md#insn-00af7340)

~~~diff
- 00af7338 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00af7338 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af7338 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00af7338 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7338 bytes fc6711a9
- 00af733c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af733c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af733c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00af733c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af733c bytes f85f12a9
- 00af7340 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00af7340 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00af7340 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00af7340 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af7340 bytes f65713a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b74706397fb23d0fe2376ced2a67cca"></a>

### [`00af7674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7674.md) → [`00af773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af773c.md) _ZN8firebase4util19GetThreadsafeJNIEnvEP7_JavaVM

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde440.md) · 呼出先 4件 [`00af7660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7660.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1f0.md) [`00bde740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde740.md)
- 新版 呼出元 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md) · 呼出先 4件 [`00af7728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7728.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2a0.md) [`00bde7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af7764",
      "incomplete_value": true,
      "site": "00af776c",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:8e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af769c",
      "incomplete_value": true,
      "site": "00af76a4",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:838:8"
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
      "definition_site": "00af7768",
      "incomplete_value": true,
      "site": "00af776c",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:8c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af76a0",
      "incomplete_value": true,
      "site": "00af76a4",
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
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af777c",
      "incomplete_value": true,
      "site": "00af7780",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af76b4",
      "incomplete_value": true,
      "site": "00af76b8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "LOAD"
            ]
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
      "00af7764",
      "READ",
      [
        "storage",
        "00c1b838",
        null,
        "pointer"
      ]
    ],
    [
      "00af7764",
      "PARAM",
      [
        "storage",
        "010a0bf8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ],
    [
      "00af7768",
      "READ",
      [
        "storage",
        "00c1b810",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00af7764",
      "READ",
      [
        "storage",
        "00c1b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00af7764",
      "PARAM",
      [
        "storage",
        "010a0cb8",
        "_ZN8firebase4util23pthread_key_initializedE",
        "undefined4"
      ]
    ],
    [
      "00af7768",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af76a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7674.md#insn-00af76a4) · [`00af76b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7674.md#insn-00af76b8) · [`00af769c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7674.md#insn-00af769c)
- 新版 `00af776c`（命令位置の公開資料なし） · `00af7780`（命令位置の公開資料なし） · `00af7764`（命令位置の公開資料なし）

~~~diff
- 00af76a4 ["INT_ADD", "register:40f0:8", ["const:af76a4:8", "const:4:8"]]
- 00af76a4 ["CALL", null, ["callee:00bde7f0:8"]]
+ 00af776c ["INT_ADD", "register:40f0:8", ["const:af776c:8", "const:4:8"]]
+ 00af776c ["CALL", null, ["callee:00bde7f0:8"]]
- 00af76a4 bytes 279c0394
+ 00af776c bytes 219c0394
- 00af76b8 ["INT_ADD", "register:40f0:8", ["const:af76b8:8", "const:4:8"]]
- 00af76b8 ["CALL", null, ["callee:00bdb2a0:8"]]
+ 00af7780 ["INT_ADD", "register:40f0:8", ["const:af7780:8", "const:4:8"]]
+ 00af7780 ["CALL", null, ["callee:00bdb2a0:8"]]
- 00af76b8 bytes ce8e0394
+ 00af7780 bytes c88e0394
- 00af769c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:838:8"]]
- 00af769c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af7764 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8e8:8"]]
+ 00af7764 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00af769c bytes 001c44f9
+ 00af7764 bytes 007444f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a85cd9a60e1959ec5f5d33643bd6548"></a>

### [`00af7aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7aa8.md) → [`00af7b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7b70.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emp

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde670.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) [`00bde620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde620.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md)
- 新版 呼出元 1件 [`00bde720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde720.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 42.31% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7b40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af7c08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7b50",
      "incomplete_value": true,
      "site": "00af7b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af7b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7bf8"
      ]
    ]
  ],
  "added": [
    [
      "00af7c08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7bf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7aa8.md#insn-00af7b40) · [`00af7b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7aa8.md#insn-00af7b58)
- 新版 `00af7c20`（命令位置の公開資料なし） · `00af7c08`（命令位置の公開資料なし）

~~~diff
- 00af7b40 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00af7b40 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00af7b40 bytes 95ffffb5
- 00af7b58 ["INT_ADD", "register:40f0:8", ["const:af7b58:8", "const:4:8"]]
- 00af7b58 ["CALL", null, ["callee:00bdd9a0:8"]]
+ 00af7c20 ["INT_ADD", "register:40f0:8", ["const:af7c20:8", "const:4:8"]]
+ 00af7c20 ["CALL", null, ["callee:00bdd9a0:8"]]
- 00af7b58 bytes 66970394
+ 00af7c20 bytes 60970394
+ 00af7c08 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00af7c08 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00af7c08 bytes 95ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa55105b329d460d4a3bba3c00d208ca"></a>

### [`00af7bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7bc4.md) → [`00af7c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7c8c.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6c0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md)
- 新版 呼出元 1件 [`00bde770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde770.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 69.23% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7c28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af7cf0"
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
      "unmatched:00af7c28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7d04"
      ]
    ],
    [
      "unmatched:00af7c6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7d68"
      ]
    ]
  ],
  "added": [
    [
      "00af7cf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7d04"
      ]
    ],
    [
      "00af7d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7d68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7c28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7bc4.md#insn-00af7c28) · [`00af7c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7bc4.md#insn-00af7c5c) · [`00af7c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7bc4.md#insn-00af7c6c)
- 新版 `00af7d24`（命令位置の公開資料なし）

~~~diff
- 00af7c28 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af7c28 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00af7c28 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00af7c28 bytes a8000054
- 00af7c5c ["INT_ADD", "register:40f0:8", ["const:af7c5c:8", "const:4:8"]]
- 00af7c5c ["CALL", null, ["callee:00bde6e0:8"]]
+ 00af7d24 ["INT_ADD", "register:40f0:8", ["const:af7d24:8", "const:4:8"]]
+ 00af7d24 ["CALL", null, ["callee:00bde6e0:8"]]
- 00af7c5c bytes 759a0394
+ 00af7d24 bytes 6f9a0394
- 00af7c6c ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00af7c6c bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f79d57820c779a046ba41c0cd8d3bca"></a>

### [`00af7d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7d14.md) → [`00af7ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af7/00af7ddc.md) _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6d0.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af7e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af7ed8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af7d90",
      "incomplete_value": true,
      "site": "00af7d94",
      "value": [
        "INT_LEFT",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              "INT_LEFT"
            ]
          ],
          [
            "leaf",
            "const:3:8"
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
      "unmatched:00af7e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7f08"
      ]
    ]
  ],
  "added": [
    [
      "00af7ed8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af7f08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af7d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7d14.md#insn-00af7d94) · [`00af7e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af7/00af7d14.md#insn-00af7e10)
- 新版 `00af7e5c`（命令位置の公開資料なし） · `00af7ed8`（命令位置の公開資料なし）

~~~diff
- 00af7d94 ["INT_ADD", "register:40f0:8", ["const:af7d94:8", "const:4:8"]]
- 00af7d94 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00af7e5c ["INT_ADD", "register:40f0:8", ["const:af7e5c:8", "const:4:8"]]
+ 00af7e5c ["CALL", null, ["callee:00bdaff0:8"]]
- 00af7d94 bytes 6b8c0394
+ 00af7e5c bytes 658c0394
- 00af7e10 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00af7e10 bytes 80010054
+ 00af7ed8 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
+ 00af7ed8 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-345701b4e280684283c25ef43dbdd7d8"></a>

### [`00af81c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af81c8.md) → [`00af8290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8290.md) _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde650.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.76% / 新版 70.76%

CFGの説明率　旧版 40.34% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 12件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af824c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8260"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af81d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af82b0"
      ]
    ],
    [
      "unmatched:00af81ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af82c4"
      ]
    ],
    [
      "unmatched:00af82bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af83c0"
      ]
    ]
  ],
  "added": [
    [
      "00af8298",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af82b0"
      ]
    ],
    [
      "00af82b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af82c4"
      ]
    ],
    [
      "00af8384",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af83c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af81c8.md#insn-00af8204) · [`00af824c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af81c8.md#insn-00af824c) · [`00af8260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af81c8.md#insn-00af8260)

~~~diff
- 00af8204 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 00af8204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af8204 bytes 280900f9
- 00af824c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:10:8"]]
- 00af824c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4068:8"]]
- 00af824c bytes 4d0900f9
- 00af8260 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00af8260 ["INT_ZEXT", "tmp:1:8", ["register:4070:4"]]
- 00af8260 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af8260 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:3:8"]]
- 00af8260 bytes aa592ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e8b76478bf8c87310bdd3e1595e357"></a>

### [`00af8578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8578.md) → [`00af8640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8640.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) · 呼出先 2件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md)
- 新版 呼出元 1件 [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) · 呼出先 2件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 35.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af85c8",
      "incomplete_value": true,
      "site": "00af85dc",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00af85c4",
      "incomplete_value": true,
      "site": "00af85dc",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              [
                "live",
                "register:40a8:8"
              ],
              [
                "live",
                "register:40a0:8"
              ]
            ]
          ],
          [
            "live",
            "register:4008:8"
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
    "new": null,
    "old": {
      "definition_site": "00af85cc",
      "incomplete_value": true,
      "site": "00af85dc",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00af85dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8578.md#insn-00af85dc) · [`00af8604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8578.md#insn-00af8604) · [`00af8638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8578.md#insn-00af8638)
- 新版 `00af86a4`（命令位置の公開資料なし） · `00af86cc`（命令位置の公開資料なし）

~~~diff
- 00af85dc ["INT_ADD", "register:40f0:8", ["const:af85dc:8", "const:4:8"]]
- 00af85dc ["CALL", null, ["callee:00bde1d0:8"]]
+ 00af86a4 ["INT_ADD", "register:40f0:8", ["const:af86a4:8", "const:4:8"]]
+ 00af86a4 ["CALL", null, ["callee:00bde1d0:8"]]
- 00af85dc bytes d1960394
+ 00af86a4 bytes cb960394
- 00af8604 ["INT_ADD", "register:40f0:8", ["const:af8604:8", "const:4:8"]]
- 00af8604 ["CALL", null, ["callee:00bdb160:8"]]
+ 00af86cc ["INT_ADD", "register:40f0:8", ["const:af86cc:8", "const:4:8"]]
+ 00af86cc ["CALL", null, ["callee:00bdb160:8"]]
- 00af8604 bytes ab8a0394
+ 00af86cc bytes a58a0394
- 00af8638 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00af8638 ["RETURN", null, ["register:0:8"]]
- 00af8638 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d4373f11d308234268537755f5c2b7"></a>

### [`00af863c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af863c.md) → [`00af8704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8704.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd990.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdda40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda40.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 25.93% / 新版 24.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af86b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af86b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af8778"
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
      "unmatched:00af86b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8794"
      ]
    ]
  ],
  "added": [
    [
      "00af8780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8794"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af86b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af863c.md#insn-00af86b0) · [`00af86b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af863c.md#insn-00af86b8) · [`00af86f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af863c.md#insn-00af86f0)
- 新版 `00af87b8`（命令位置の公開資料なし）

~~~diff
- 00af86b0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00af86b0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00af86b0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00af86b0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00af86b0 bytes 2831889a
- 00af86b8 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00af86b8 bytes a2000054
- 00af86f0 ["INT_ADD", "register:40f0:8", ["const:af86f0:8", "const:4:8"]]
- 00af86f0 ["CALL", null, ["callee:00bdb160:8"]]
+ 00af87b8 ["INT_ADD", "register:40f0:8", ["const:af87b8:8", "const:4:8"]]
+ 00af87b8 ["CALL", null, ["callee:00bdb160:8"]]
- 00af86f0 bytes 708a0394
+ 00af87b8 bytes 6a8a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e4a3fcf3b398e3e5d55f062a7ca6da"></a>

### [`00af8750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8750.md) → [`00af8818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8818.md) Java_com_google_firebase_app_internal_cpp_Log_nativeLog

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfa0.md) [`00bde140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) [`00bde1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.21% / 新版 73.21%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af877c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af8844"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af87cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af877c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af87b8",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af87bc",
      "DATA",
      [
        "storage",
        "002cfde0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af8844",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00af8880",
      "READ",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af8884",
      "DATA",
      [
        "storage",
        "002cfde0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af877c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8750.md#insn-00af877c) · [`00af87cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8750.md#insn-00af87cc) · [`00af87d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8750.md#insn-00af87d8)

~~~diff
- 00af877c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00af877c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af877c bytes e81f00f9
- 00af87cc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00af87cc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00af87cc ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00af87cc ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00af87cc bytes 62018a9a
- 00af87d8 ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00af87d8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00af87d8 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00af87d8 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00af87d8 bytes c3018d9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2fcf585d5366388d83a91822d0a9116"></a>

### [`00af89c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af89c4.md) → [`00af8a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8a8c.md) _ZN8firebase8internal16JObjectReferenceC2ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde220.md) · 呼出先 1件 [`00bde440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde440.md)
- 新版 呼出元 1件 [`00bde2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde2d0.md) · 呼出先 1件 [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af89e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af89fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af8aa8"
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
      "unmatched:00af89e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8ab8"
      ]
    ],
    [
      "unmatched:00af89fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8ad8"
      ]
    ]
  ],
  "added": [
    [
      "00af8aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8ab8"
      ]
    ],
    [
      "00af8ac4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8ad8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af89e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af89c4.md#insn-00af89e0) · [`00af89fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af89c4.md#insn-00af89fc)
- 新版 `00af8aa8`（命令位置の公開資料なし）

~~~diff
- 00af89e0 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00af89e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00af89e0 bytes 950000b4
- 00af89fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00af89fc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00af89fc bytes a10000b4
+ 00af8aa8 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00af8aa8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00af8aa8 bytes 950000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b55856d40f22c79f3696b483d8101db"></a>

### [`00af8a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8a40.md) → [`00af8b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8b08.md) _ZN8firebase8internal16JObjectReferenceaSEOS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-6479d462dec19c22d98382a171932a5b"></a>

### [`00af8bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8bec.md) → [`00af8cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8cb4.md) _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 18.18% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af8d48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00af8c44",
      "incomplete_value": true,
      "site": "00af8c4c",
      "value": [
        "live",
        "register:40a8:8"
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
      "unmatched:00af8c80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8d60"
      ]
    ]
  ],
  "added": [
    [
      "00af8d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af8d60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8bec.md#insn-00af8c4c) · [`00af8c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8bec.md#insn-00af8c80)
- 新版 `00af8d14`（命令位置の公開資料なし） · `00af8d48`（命令位置の公開資料なし）

~~~diff
- 00af8c4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00af8c4c ["INT_ADD", "register:40f0:8", ["const:af8c4c:8", "const:4:8"]]
- 00af8c4c ["CALLIND", null, ["register:0:8"]]
+ 00af8d14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00af8d14 ["INT_ADD", "register:40f0:8", ["const:af8d14:8", "const:4:8"]]
+ 00af8d14 ["CALLIND", null, ["register:0:8"]]
- 00af8c4c bytes 00013fd6
+ 00af8d14 bytes 00013fd6
- 00af8c80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00af8c80 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00af8c80 bytes c1000054
+ 00af8d48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00af8d48 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00af8d48 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688f23b7bac39ec3f62bdac4d804b0a5"></a>

### [`00af8d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8d88.md) → [`00af8e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af8/00af8e50.md) _ZN8firebase10app_common6AddAppEPNS_3AppEPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS_10InitResultENS3_4l

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7d0.md) · 呼出先 20件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bde880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde880.md) · 呼出先 20件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.59% / 新版 89.59%

CFGの説明率　旧版 40.70% / 新版 42.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 4件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8dbc"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af8ef4",
      "incomplete_value": false,
      "site": "00af8ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af8e2c",
      "incomplete_value": false,
      "site": "00af8e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af8e64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af8dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af8dd8",
      "PARAM",
      [
        "storage",
        "0029cd51",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af8df8",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af8e84",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af8ea0",
      "PARAM",
      [
        "storage",
        "0029cdde",
        null,
        "string"
      ]
    ],
    [
      "00af8ec0",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af8dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8d88.md#insn-00af8dbc) · [`00af8ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8d88.md#insn-00af8ddc) · [`00af8de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af8/00af8d88.md#insn-00af8de4)
- 新版 `00af8ea4`（命令位置の公開資料なし） · `00af8eac`（命令位置の公開資料なし）

~~~diff
- 00af8dbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00af8dbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af8dbc bytes e81f00f9
- 00af8ddc ["INT_ADD", "register:40f0:8", ["const:af8ddc:8", "const:4:8"]]
- 00af8ddc ["CALL", null, ["callee:00bde130:8"]]
+ 00af8ea4 ["INT_ADD", "register:40f0:8", ["const:af8ea4:8", "const:4:8"]]
+ 00af8ea4 ["CALL", null, ["callee:00bde130:8"]]
- 00af8ddc bytes a9940394
+ 00af8ea4 bytes a3940394
- 00af8de4 ["BRANCH", null, ["local:b62:8"]]
+ 00af8eac ["BRANCH", null, ["local:b58:8"]]
- 00af8de4 bytes b7000014
+ 00af8eac bytes b7000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7242973456e2bf5965368c29ae58548"></a>

### [`00af90fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af90fc.md) → [`00af91c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af91c4.md) _ZN8firebase10app_common13FindAppByNameEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde770.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bde820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde820.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 55.00% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af9260"
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
      "00af91f4",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9204",
      "READ",
      [
        "storage",
        "010a0c18",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af9198",
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
      "00af91f4",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9204",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9260",
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

- 旧版 [`00af9134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af90fc.md#insn-00af9134) · [`00af9140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af90fc.md#insn-00af9140) · [`00af9198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af90fc.md#insn-00af9198)
- 新版 `00af91fc`（命令位置の公開資料なし） · `00af9208`（命令位置の公開資料なし）

~~~diff
- 00af9134 ["INT_ADD", "register:40f0:8", ["const:af9134:8", "const:4:8"]]
- 00af9134 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00af91fc ["INT_ADD", "register:40f0:8", ["const:af91fc:8", "const:4:8"]]
+ 00af91fc ["CALL", null, ["callee:00bddbd0:8"]]
- 00af9134 bytes 7b920394
+ 00af91fc bytes 75920394
- 00af9140 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00af9140 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00af9208 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00af9208 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00af9140 bytes b40500b4
+ 00af9208 bytes b40500b4
- 00af9198 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af9198 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 00af9198 ["COPY", "tmp:2:8", ["register:8:8"]]
- 00af9198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9198 bytes e85b00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d877b8cc0f1735f4c55d4183cc5093f"></a>

### [`00af9234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9234.md) → [`00af92fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7b0.md) · 呼出先 1件 [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 1件 [`00bde860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md) · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af930c",
      "incomplete_value": false,
      "site": "00af9310",
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
            "const:ec6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af9244",
      "incomplete_value": false,
      "site": "00af9248",
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
            "const:ecd:8"
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
    "new": null,
    "old": {
      "definition_site": "00af9250",
      "incomplete_value": true,
      "site": "00af9258",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:4"
              ]
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
      "unmatched:00af9244",
      "PARAM",
      [
        "storage",
        "002a4ecd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af930c",
      "PARAM",
      [
        "storage",
        "002a4ec6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9234.md#insn-00af9248) · [`00af9244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9234.md#insn-00af9244)
- 新版 `00af9310`（命令位置の公開資料なし） · `00af930c`（命令位置の公開資料なし）

~~~diff
- 00af9248 ["INT_ADD", "register:40f0:8", ["const:af9248:8", "const:4:8"]]
- 00af9248 ["CALL", null, ["callee:00bde980:8"]]
+ 00af9310 ["INT_ADD", "register:40f0:8", ["const:af9310:8", "const:4:8"]]
+ 00af9310 ["CALL", null, ["callee:00bde980:8"]]
- 00af9248 bytes a2950394
+ 00af9310 bytes 9c950394
- 00af9244 ["COPY", "tmp:0:8", ["const:ecd:8"]]
- 00af9244 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00af9244 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00af9244 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00af9244 bytes 00343b91
+ 00af930c ["COPY", "tmp:0:8", ["const:ec6:8"]]
+ 00af930c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00af930c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00af930c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00af930c bytes 00183b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a7eb14b0c48555e270db35bf2ad18f8"></a>

### [`00af9268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9268.md) → [`00af9330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9330.md) _ZN8firebase10app_common9GetAnyAppEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9268"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af926c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9268",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af926c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af9340",
      "READ",
      [
        "storage",
        "010a0c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af9330",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af9334",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af9340",
      "READ",
      [
        "storage",
        "010a0cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9268.md#insn-00af9268) · [`00af926c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9268.md#insn-00af926c) · [`00af928c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9268.md#insn-00af928c)
- 新版 `00af9354`（命令位置の公開資料なし）

~~~diff
- 00af9268 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af9268 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af9268 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00af9268 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af9268 bytes f44fbea9
- 00af926c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af926c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af926c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af926c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af926c bytes fd7b01a9
- 00af928c ["INT_ADD", "register:40f0:8", ["const:af928c:8", "const:4:8"]]
- 00af928c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00af9354 ["INT_ADD", "register:40f0:8", ["const:af9354:8", "const:4:8"]]
+ 00af9354 ["CALL", null, ["callee:00bddbd0:8"]]
- 00af928c bytes 25920394
+ 00af9354 bytes 1f920394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca473a6e2336bab440e63cb45f25cc17"></a>

### [`00af92d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af92d0.md) → [`00af9398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9398.md) _ZN8firebase10app_common10GetAllAppsEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde750.md) · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bde800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde800.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 39.62% / 新版 40.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af92d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af92d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af92d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af92d8",
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
      "00af9398",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00af939c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00af93a0",
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

- 旧版 [`00af92d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af92d0.md#insn-00af92d0) · [`00af92d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af92d0.md#insn-00af92d4) · [`00af92d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af92d0.md#insn-00af92d8)

~~~diff
- 00af92d0 ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00af92d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00af92d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00af92d0 bytes fb0f1af8
- 00af92d4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00af92d4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00af92d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00af92d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af92d4 bytes fa6701a9
- 00af92d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00af92d8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00af92d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00af92d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af92d8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c6835343e93cbb13fa0414b931d517b"></a>

### [`00af9488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md) → [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) _ZN8firebase10app_common9RemoveAppEPNS_3AppE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7e0.md) · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bde890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde890.md) · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.79% / 新版 78.79%

CFGの説明率　旧版 29.17% / 新版 28.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 4件, `store_destination` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af94b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af95e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af9714",
      "incomplete_value": true,
      "site": "00af9714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af964c",
      "incomplete_value": true,
      "site": "00af964c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af94b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af9584",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9594",
      "READ",
      [
        "storage",
        "010a0c18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af957c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af9584",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9594",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af94b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md#insn-00af94b4) · [`00af94c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md#insn-00af94c4) · [`00af94d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9488.md#insn-00af94d0)
- 新版 `00af958c`（命令位置の公開資料なし） · `00af9598`（命令位置の公開資料なし）

~~~diff
- 00af94b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00af94b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af94b4 bytes e80f00f9
- 00af94c4 ["INT_ADD", "register:40f0:8", ["const:af94c4:8", "const:4:8"]]
- 00af94c4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00af958c ["INT_ADD", "register:40f0:8", ["const:af958c:8", "const:4:8"]]
+ 00af958c ["CALL", null, ["callee:00bddbd0:8"]]
- 00af94c4 bytes 97910394
+ 00af958c bytes 91910394
- 00af94d0 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00af94d0 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 00af9598 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00af9598 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00af94d0 bytes 550900b4
+ 00af9598 bytes 550900b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8318374399e06112ac04280e5bf94bbd"></a>

### [`00af9698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9698.md) → [`00af9760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9760.md) _ZN8firebase10app_common14DestroyAllAppsEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 26.67% / 新版 26.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af96a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af96a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af96ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af96a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af96ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af9780",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af9770",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af9774",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af9780",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af96a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9698.md#insn-00af96a8) · [`00af96ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9698.md#insn-00af96ac) · [`00af96d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9698.md#insn-00af96d4)

~~~diff
- 00af96a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af96a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af96a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00af96a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af96a8 bytes f44f04a9
- 00af96ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af96ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af96ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00af96ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af96ac bytes fd7b05a9
- 00af96d4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00af96d4 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 00af96d4 bytes 880900b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb743bb987bfa3e932df07b2d896ae3c"></a>

### [`00af9954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9954.md) → [`00af9a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9a1c.md) _ZN8firebase10app_common15RegisterLibraryEPKcS2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7a0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde780.md) [`00bde790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde790.md)
- 新版 呼出元 1件 [`00bde850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde850.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde830.md) [`00bde840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde840.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 11.11% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 7件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af99b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00af9a78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af998c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af9a34",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9a4c",
      "READ",
      [
        "storage",
        "00c1b850",
        null,
        "pointer"
      ]
    ],
    [
      "00af9a50",
      "READ",
      [
        "storage",
        "010a0c08",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af9a34",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9a4c",
      "READ",
      [
        "storage",
        "00c1b900",
        null,
        "pointer"
      ]
    ],
    [
      "00af9a50",
      "READ",
      [
        "storage",
        "010a0cc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af997c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9954.md#insn-00af997c) · [`00af998c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9954.md#insn-00af998c) · [`00af99b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9954.md#insn-00af99b0)
- 新版 `00af9a44`（命令位置の公開資料なし）

~~~diff
- 00af997c ["INT_ADD", "register:40f0:8", ["const:af997c:8", "const:4:8"]]
- 00af997c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00af9a44 ["INT_ADD", "register:40f0:8", ["const:af9a44:8", "const:4:8"]]
+ 00af9a44 ["CALL", null, ["callee:00bddbd0:8"]]
- 00af997c bytes 69900394
+ 00af9a44 bytes 63900394
- 00af998c ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00af998c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00af998c bytes 760100b5
- 00af99b0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00af99b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af99b0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb8b9def5e572bcfc78f9b56a72628a"></a>

### [`00af99ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af99ec.md) → [`00af9ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ab4.md) _ZN8firebase10app_common15LibraryRegistry15RegisterLibraryEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde780.md) · 呼出先 12件 [`0044a6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a6d0.md) [`00470ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470ef0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bde830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde830.md) · 呼出先 12件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`00470ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ef0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.59% / 新版 89.59%

CFGの説明率　旧版 21.10% / 新版 21.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 11件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9a24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9a28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9a24",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9a28",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9a2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af9aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00af9af0",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "00af9af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af99ec.md#insn-00af9a24) · [`00af9a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af99ec.md#insn-00af9a28) · [`00af9a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af99ec.md#insn-00af9a2c)

~~~diff
- 00af9a24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00af9a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00af9a24 bytes e82f00f9
- 00af9a28 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00af9a28 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00af9a28 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00af9a28 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00af9a28 bytes ff7f04a9
- 00af9a2c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00af9a2c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00af9a2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00af9a2c bytes ff1f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df4acca87d29bde3bcc044b0e5050eea"></a>

### [`00af9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9e20.md) → [`00af9ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md) _ZN8firebase10app_common15LibraryRegistry15UpdateUserAgentEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde790.md) · 呼出先 5件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 1件 [`00bde840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde840.md) · 呼出先 5件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.24% / 新版 82.24%

CFGの説明率　旧版 18.84% / 新版 19.40%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9e30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9e30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af9e34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af9e30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9e34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af9e4c",
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
      "00af9ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00af9efc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00af9f14",
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

- 旧版 [`00af9e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9e20.md#insn-00af9e30) · [`00af9e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9e20.md#insn-00af9e34) · [`00af9e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9e20.md#insn-00af9e4c)

~~~diff
- 00af9e30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00af9e30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00af9e30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00af9e30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9e30 bytes f44f09a9
- 00af9e34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00af9e34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00af9e34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00af9e34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af9e34 bytes fd7b0aa9
- 00af9e4c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af9e4c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00af9e4c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00af9e4c bytes a8831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ddc9a95a153bae4ce2764ce0575e339"></a>

### [`00afa080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa080.md) → [`00afa148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa148.md) _ZN8firebase10app_common30RegisterLibrariesFromUserAgentEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 74.42% / 新版 74.42%

CFGの説明率　旧版 43.75% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa088"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa084",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa088",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa08c",
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
      "00afa14c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00afa150",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00afa154",
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

- 旧版 [`00afa084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa080.md#insn-00afa084) · [`00afa088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa080.md#insn-00afa088) · [`00afa08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa080.md#insn-00afa08c)

~~~diff
- 00afa084 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00afa084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00afa084 bytes f91300f9
- 00afa088 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afa088 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afa088 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afa088 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa088 bytes f85f03a9
- 00afa08c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afa08c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afa08c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00afa08c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa08c bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c098c8ea92c3ec10137ed86e78529307"></a>

### [`00afa1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa1d8.md) → [`00afa2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa2a0.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7c0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde830.md)
- 新版 呼出元 1件 [`00bde870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde870.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8e0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 51.47% / 新版 51.47%

CFGの説明率　旧版 7.14% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa22c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa22c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afa2b4",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa2c8",
      "READ",
      [
        "storage",
        "00c1b850",
        null,
        "pointer"
      ]
    ],
    [
      "00afa2cc",
      "READ",
      [
        "storage",
        "010a0c08",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afa2b4",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa2c8",
      "READ",
      [
        "storage",
        "00c1b900",
        null,
        "pointer"
      ]
    ],
    [
      "00afa2cc",
      "READ",
      [
        "storage",
        "010a0cc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa1d8.md#insn-00afa1f8) · [`00afa208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa1d8.md#insn-00afa208) · [`00afa21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa1d8.md#insn-00afa21c)
- 新版 `00afa2c0`（命令位置の公開資料なし） · `00afa2d0`（命令位置の公開資料なし） · `00afa2e4`（命令位置の公開資料なし）

~~~diff
- 00afa1f8 ["INT_ADD", "register:40f0:8", ["const:afa1f8:8", "const:4:8"]]
- 00afa1f8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afa2c0 ["INT_ADD", "register:40f0:8", ["const:afa2c0:8", "const:4:8"]]
+ 00afa2c0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afa1f8 bytes 4a8e0394
+ 00afa2c0 bytes 448e0394
- 00afa208 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00afa208 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00afa2d0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00afa2d0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00afa208 bytes 880000b4
+ 00afa2d0 bytes 880000b4
- 00afa21c ["INT_ADD", "register:40f0:8", ["const:afa21c:8", "const:4:8"]]
- 00afa21c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afa2e4 ["INT_ADD", "register:40f0:8", ["const:afa2e4:8", "const:4:8"]]
+ 00afa2e4 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afa21c bytes 49830394
+ 00afa2e4 bytes 43830394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36205594fd3747abb7b2b7d83de2b5bd"></a>

### [`00afa2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa2e8.md) → [`00afa3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa3b0.md) _ZN8firebase10app_common12GetUserAgentEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde760.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bde810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde810.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 22.22% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 7件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afa3f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa310"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afa3c0",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00afa308",
      "READ",
      [
        "storage",
        "00c1b850",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afa30c",
      "READ",
      [
        "storage",
        "010a0c08",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afa3c0",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa3d0",
      "READ",
      [
        "storage",
        "00c1b900",
        null,
        "pointer"
      ]
    ],
    [
      "00afa3d4",
      "READ",
      [
        "storage",
        "010a0cc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa2e8.md#insn-00afa300) · [`00afa310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa2e8.md#insn-00afa310) · [`00afa330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa2e8.md#insn-00afa330)
- 新版 `00afa3c8`（命令位置の公開資料なし）

~~~diff
- 00afa300 ["INT_ADD", "register:40f0:8", ["const:afa300:8", "const:4:8"]]
- 00afa300 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afa3c8 ["INT_ADD", "register:40f0:8", ["const:afa3c8:8", "const:4:8"]]
+ 00afa3c8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afa300 bytes 088e0394
+ 00afa3c8 bytes 028e0394
- 00afa310 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00afa310 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00afa310 bytes 400100b5
- 00afa330 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afa330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afa330 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acacc5b2a7d8d64c72923163fc207dfe"></a>

### [`00afa368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa368.md) → [`00afa430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa430.md) _ZN8firebase10app_common17GetLibraryVersionEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00470ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470ef0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00470ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ef0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_store_alignment

命令の説明率　旧版 93.41% / 新版 93.41%

CFGの説明率　旧版 11.11% / 新版 10.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa3cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa3d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa394",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00afa464",
      "READ",
      [
        "storage",
        "010a0c00",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa474",
      "READ",
      [
        "storage",
        "00c1b850",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afa45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00afa464",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa474",
      "READ",
      [
        "storage",
        "00c1b900",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa368.md#insn-00afa394) · [`00afa3a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa368.md#insn-00afa3a4) · [`00afa3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa368.md#insn-00afa3bc)
- 新版 `00afa46c`（命令位置の公開資料なし） · `00afa484`（命令位置の公開資料なし）

~~~diff
- 00afa394 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00afa394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00afa394 bytes e90f00f9
- 00afa3a4 ["INT_ADD", "register:40f0:8", ["const:afa3a4:8", "const:4:8"]]
- 00afa3a4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afa46c ["INT_ADD", "register:40f0:8", ["const:afa46c:8", "const:4:8"]]
+ 00afa46c ["CALL", null, ["callee:00bddbd0:8"]]
- 00afa3a4 bytes df8d0394
+ 00afa46c bytes d98d0394
- 00afa3bc ["INT_ADD", "register:40f0:8", ["const:afa3bc:8", "const:4:8"]]
- 00afa3bc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afa484 ["INT_ADD", "register:40f0:8", ["const:afa484:8", "const:4:8"]]
+ 00afa484 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afa3bc bytes e1820394
+ 00afa484 bytes db820394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebdc2d4346820e6f5e900d5b769fddf2"></a>

### [`00afa4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa4d4.md) → [`00afa59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa59c.md) _ZN8firebase10app_common25GetOuterMostSdkAndVersionEPNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00470ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470ef0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00470ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470ef0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.53% / 新版 75.53%

CFGの説明率　旧版 14.29% / 新版 14.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 11件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 24件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa4d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa4d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa4dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa4d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa4dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa4e0",
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
      "00afa5a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00afa5a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00afa5a8",
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

- 旧版 [`00afa4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa4d4.md#insn-00afa4d8) · [`00afa4dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa4d4.md#insn-00afa4dc) · [`00afa4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa4d4.md#insn-00afa4e0)

~~~diff
- 00afa4d8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afa4d8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00afa4d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afa4d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa4d8 bytes fc6f06a9
- 00afa4dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00afa4dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00afa4dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00afa4dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa4dc bytes fa6707a9
- 00afa4e0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afa4e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afa4e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00afa4e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa4e0 bytes f85f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20bbe84fa6a6c331fe92c41422db206b"></a>

### [`00afa7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa7c4.md) → [`00afa88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md) _ZN8firebase10app_common19FindAppLoggerByNameEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 19.23% / 新版 20.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa7d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa7d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa7d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa7ec",
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
      "00afa89c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afa8a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afa8b4",
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

- 旧版 [`00afa7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa7c4.md#insn-00afa7d4) · [`00afa7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa7c4.md#insn-00afa7d8) · [`00afa7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa7c4.md#insn-00afa7ec)

~~~diff
- 00afa7d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa7d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa7d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00afa7d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa7d4 bytes f44f05a9
- 00afa7d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afa7d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afa7d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afa7d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa7d8 bytes fd7b06a9
- 00afa7ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00afa7ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afa7ec bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a323658ab60d06166cfb01567c9659cf"></a>

### [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) → [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) FUN_00afa9c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 8件 [`00af9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af9/00af9e20.md) [`00afd380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd380.md) [`00afd444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd444.md) [`00b115bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b115bc.md) [`00b12714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12714.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 8件 [`00af9ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9ee8.md) [`00afd448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md) [`00afd50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md) [`00b11684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md) [`00b127dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 62.50% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afaa70",
      "incomplete_value": true,
      "site": "00afaa7c",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afa9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md#insn-00afa9b4) · [`00afa938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md#insn-00afa938) · [`00afa950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md#insn-00afa950)
- 新版 `00afaa7c`（命令位置の公開資料なし） · `00afaa00`（命令位置の公開資料なし） · `00afaa18`（命令位置の公開資料なし）

~~~diff
- 00afa9b4 ["INT_ADD", "register:40f0:8", ["const:afa9b4:8", "const:4:8"]]
- 00afa9b4 ["CALL", null, ["callee:00bdb160:8"]]
+ 00afaa7c ["INT_ADD", "register:40f0:8", ["const:afaa7c:8", "const:4:8"]]
+ 00afaa7c ["CALL", null, ["callee:00bdb160:8"]]
- 00afa9b4 bytes bf810394
+ 00afaa7c bytes b9810394
- 00afa938 ["INT_ADD", "register:40f0:8", ["const:afa938:8", "const:4:8"]]
- 00afa938 ["CALL", null, ["callee:00bdb140:8"]]
+ 00afaa00 ["INT_ADD", "register:40f0:8", ["const:afaa00:8", "const:4:8"]]
+ 00afaa00 ["CALL", null, ["callee:00bdb140:8"]]
- 00afa938 bytes d6810394
+ 00afaa00 bytes d0810394
- 00afa950 ["INT_ADD", "register:40f0:8", ["const:afa950:8", "const:4:8"]]
- 00afa950 ["CALL", null, ["callee:00bdb140:8"]]
+ 00afaa18 ["INT_ADD", "register:40f0:8", ["const:afaa18:8", "const:4:8"]]
+ 00afaa18 ["CALL", null, ["callee:00bdb140:8"]]
- 00afa950 bytes d0810394
+ 00afaa18 bytes ca810394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dc5d9bed373140c166145adc5d668bf"></a>

### [`00afa9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa9e4.md) → [`00afaaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md) · 呼出先 3件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md) · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 13.33% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afa9e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afa9e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa9e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afa9ec",
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
      "00afaaac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00afaab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afaab4",
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

- 旧版 [`00afa9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa9e4.md#insn-00afa9e4) · [`00afa9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa9e4.md#insn-00afa9e8) · [`00afa9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa9e4.md#insn-00afa9ec)

~~~diff
- 00afa9e4 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00afa9e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00afa9e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afa9e4 bytes f70f1cf8
- 00afa9e8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afa9e8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afa9e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afa9e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa9e8 bytes f65701a9
- 00afa9ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afa9ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afa9ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afa9ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afa9ec bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed4661111446de13cd8d70b9772f090d"></a>

### [`00afabc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afabc4.md) → [`00afac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afac8c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde890.md) · 呼出先 1件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00bde940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde940.md) · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 76.81% / 新版 76.81%

CFGの説明率　旧版 14.81% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afabfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afac10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afac1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afac48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afaccc"
      ]
    ],
    [
      "00afad28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00afac14"
      ]
    ],
    [
      "unmatched:00afac6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afad84"
      ]
    ]
  ],
  "added": [
    [
      "00afad10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afaccc"
      ]
    ],
    [
      "00afad28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afacdc"
      ]
    ],
    [
      "00afad34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afad84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afabfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afabc4.md#insn-00afabfc) · [`00afac10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afabc4.md#insn-00afac10) · [`00afac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afabc4.md#insn-00afac1c)

~~~diff
- 00afabfc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afabfc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00afabfc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afabfc ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00afabfc bytes 5515819a
- 00afac10 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00afac10 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00afac10 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00afac10 ["INT_NEGATE", "tmp:1:4", ["tmp:0:4"]]
- 00afac10 bytes 00219f5a
- 00afac1c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00afac1c ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00afac1c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afac1c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afac1c bytes 94b2979a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58f0566eebbd6d0b9ecf4d0803bc9f1c"></a>

### [`00afadc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afadc0.md) → [`00afae88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afae88.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8a0.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcd0.md) [`00bde1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1e0.md) [`00bde650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde650.md)
- 新版 呼出元 1件 [`00bde950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde950.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) [`00bde290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde290.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 36.84% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afadc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afadc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afadc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afadc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afadc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afadc8",
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
      "00afae88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afae8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afae90",
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

- 旧版 [`00afadc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afadc0.md#insn-00afadc0) · [`00afadc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afadc0.md#insn-00afadc4) · [`00afadc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afadc0.md#insn-00afadc8)

~~~diff
- 00afadc0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afadc0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afadc0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afadc0 bytes f50f1df8
- 00afadc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afadc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afadc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afadc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afadc4 bytes f44f01a9
- 00afadc8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afadc8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afadc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afadc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afadc8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48cd95eaba883d3f2347be6083e108a7"></a>

### [`00afae90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afae90.md) → [`00afaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaf58.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8b0.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcd0.md) [`00bde1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1e0.md) [`00bde8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8b0.md)
- 新版 呼出元 1件 [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) [`00bde290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde290.md) [`00bde960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde960.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00afaf8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00afaeb4",
      "incomplete_value": true,
      "site": "00afaeb8",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00afaec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afafa8"
      ]
    ]
  ],
  "added": [
    [
      "00afaf8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afafa8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afaeb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afae90.md#insn-00afaeb8) · [`00afaec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afae90.md#insn-00afaec4)
- 新版 `00afaf80`（命令位置の公開資料なし） · `00afaf8c`（命令位置の公開資料なし）

~~~diff
- 00afaeb8 ["INT_ADD", "register:40f0:8", ["const:afaeb8:8", "const:4:8"]]
- 00afaeb8 ["CALL", null, ["callee:00bde960:8"]]
+ 00afaf80 ["INT_ADD", "register:40f0:8", ["const:afaf80:8", "const:4:8"]]
+ 00afaf80 ["CALL", null, ["callee:00bde960:8"]]
- 00afaeb8 bytes 7e8e0394
+ 00afaf80 bytes 788e0394
- 00afaec4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00afaec4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00afaec4 bytes f40000b4
+ 00afaf8c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00afaf8c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00afaf8c bytes f40000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3b6d22a22b5cb9f38a61085797cce2"></a>

### [`00afaf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf04.md) → [`00afafcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afafcc.md) _INIT_271

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00afaf54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf54.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00afb01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb01c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaf04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaf08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaf08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afaf04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaf08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaf18",
      "READ",
      [
        "storage",
        "00c1b7f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afafcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afafd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afafe0",
      "READ",
      [
        "storage",
        "00c1b8a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afaf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf04.md#insn-00afaf04) · [`00afaf08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf04.md#insn-00afaf08) · [`00afaf28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf04.md#insn-00afaf28)
- 新版 `00afaff0`（命令位置の公開資料なし）

~~~diff
- 00afaf04 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00afaf04 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afaf04 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afaf04 bytes f30f1ef8
- 00afaf08 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afaf08 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afaf08 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afaf08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaf08 bytes fd7b01a9
- 00afaf28 ["INT_ADD", "register:40f0:8", ["const:afaf28:8", "const:4:8"]]
- 00afaf28 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00afaff0 ["INT_ADD", "register:40f0:8", ["const:afaff0:8", "const:4:8"]]
+ 00afaff0 ["CALL", null, ["callee:00bdaf90:8"]]
- 00afaf28 bytes ee7f0394
+ 00afaff0 bytes e87f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7030b443e349da7ea8364f1d09b0b47"></a>

### [`00afaf5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf5c.md) → [`00afb024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb024.md) _ZNK8firebase10LoggerBase8LogDebugEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 11.11% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaf60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaf60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afaf64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afaf60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaf64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afaf68",
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
      "00afb028",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afb02c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afb030",
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

- 旧版 [`00afaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf5c.md#insn-00afaf60) · [`00afaf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf5c.md#insn-00afaf64) · [`00afaf68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afaf5c.md#insn-00afaf68)

~~~diff
- 00afaf60 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afaf60 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afaf60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00afaf60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaf60 bytes fc5712a9
- 00afaf64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afaf64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afaf64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00afaf64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaf64 bytes f44f13a9
- 00afaf68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afaf68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afaf68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00afaf68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afaf68 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ee1e4b600d35d1f397680af1e58de50"></a>

### [`00afb0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb0c4.md) → [`00afb18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb18c.md) _ZNK8firebase10LoggerBase7LogInfoEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 12.50% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb0d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb0d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb0dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb0d8",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb0dc",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb0e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00afb1a0",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "00afb1a4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00afb1a8",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb0c4.md#insn-00afb0d8) · [`00afb0dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb0c4.md#insn-00afb0dc) · [`00afb0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb0c4.md#insn-00afb0e0)

~~~diff
- 00afb0d8 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00afb0d8 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00afb0d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00afb0d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb0d8 bytes e20f08a9
- 00afb0dc ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00afb0dc ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00afb0dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00afb0dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb0dc bytes e41709a9
- 00afb0e0 ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00afb0e0 ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00afb0e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00afb0e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb0e0 bytes e61f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a6db91b0a9f6ba83b4f782c59529876"></a>

### [`00afb194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb194.md) → [`00afb25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb25c.md) _ZNK8firebase10LoggerBase10LogWarningEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb19c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb198",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb19c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb1a0",
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
      "00afb260",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afb264",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afb268",
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

- 旧版 [`00afb198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb194.md#insn-00afb198) · [`00afb19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb194.md#insn-00afb19c) · [`00afb1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb194.md#insn-00afb1a0)

~~~diff
- 00afb198 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00afb198 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afb198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00afb198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb198 bytes fc5712a9
- 00afb19c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afb19c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afb19c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00afb19c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb19c bytes f44f13a9
- 00afb1a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afb1a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afb1a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00afb1a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb1a0 bytes fd7b14a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a40ea7df2499cb9bfb2de83aaa1163d"></a>

### [`00afb264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb264.md) → [`00afb32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb32c.md) _ZNK8firebase10LoggerBase8LogErrorEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.69% / 新版 82.69%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb278"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb2b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb278",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb2bc",
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
      "00afb340",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "00afb380",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00afb384",
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

- 旧版 [`00afb278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb264.md#insn-00afb278) · [`00afb2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb264.md#insn-00afb2b8) · [`00afb2bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb264.md#insn-00afb2bc)

~~~diff
- 00afb278 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00afb278 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00afb278 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00afb278 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb278 bytes e20f08a9
- 00afb2b8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00afb2b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00afb2b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00afb2b8 bytes ab831df8
- 00afb2bc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afb2bc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00afb2bc ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff90:8"]]
- 00afb2bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb2bc bytes a92339a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55d2e4e48378d40fb397223313113bfb"></a>

### [`00afb334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb334.md) → [`00afb3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb3fc.md) _ZNK8firebase10LoggerBase9LogAssertEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 67.31% / 新版 67.31%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb34c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb348",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb34c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb350",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00afb410",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ],
    [
      "00afb414",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00afb418",
      "WRITE",
      [
        "storage",
        "Stack[-0xb0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb334.md#insn-00afb348) · [`00afb34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb334.md#insn-00afb34c) · [`00afb350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb334.md#insn-00afb350)

~~~diff
- 00afb348 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00afb348 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00afb348 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00afb348 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb348 bytes e20f08a9
- 00afb34c ["COPY", "tmp:0:8", ["register:4020:8"]]
- 00afb34c ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00afb34c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00afb34c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb34c bytes e41709a9
- 00afb350 ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00afb350 ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00afb350 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00afb350 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb350 bytes e61f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c343be07b3c513d5631dd98fb971c298"></a>

### [`00afb584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb584.md) → [`00afb64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb64c.md) _ZNK8firebase12SystemLogger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00afb5a0",
      "incomplete_value": true,
      "site": "00afb5b8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4008:4"
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
      "definition_site": "00afb5b0",
      "incomplete_value": true,
      "site": "00afb5b8",
      "value": [
        "live",
        "register:4010:8"
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
      "definition_site": "00afb5a4",
      "incomplete_value": true,
      "site": "00afb5b8",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afb5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb584.md#insn-00afb5b8) · [`00afb5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb584.md#insn-00afb5d8)
- 新版 `00afb680`（命令位置の公開資料なし） · `00afb6a0`（命令位置の公開資料なし）

~~~diff
- 00afb5b8 ["INT_ADD", "register:40f0:8", ["const:afb5b8:8", "const:4:8"]]
- 00afb5b8 ["CALL", null, ["callee:00bde250:8"]]
+ 00afb680 ["INT_ADD", "register:40f0:8", ["const:afb680:8", "const:4:8"]]
+ 00afb680 ["CALL", null, ["callee:00bde250:8"]]
- 00afb5b8 bytes fa8a0394
+ 00afb680 bytes f48a0394
- 00afb5d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afb5d8 ["RETURN", null, ["register:0:8"]]
- 00afb5d8 bytes c0035fd6
+ 00afb6a0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afb6a0 ["RETURN", null, ["register:0:8"]]
+ 00afb6a0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d754d6878c0cf6c295d0737f04ffa11"></a>

### [`00afb68c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb68c.md) → [`00afb754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb754.md) _ZN8firebase8callback10InitializeEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde850.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 1件 [`00bde900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde900.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb6ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb690",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afb768",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb778",
      "READ",
      [
        "storage",
        "010a0c28",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00afb758",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afb768",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb778",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb68c.md#insn-00afb690) · [`00afb6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb68c.md#insn-00afb6a8) · [`00afb6ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb68c.md#insn-00afb6ec)
- 新版 `00afb770`（命令位置の公開資料なし）

~~~diff
- 00afb690 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afb690 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afb690 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afb690 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb690 bytes f44f01a9
- 00afb6a8 ["INT_ADD", "register:40f0:8", ["const:afb6a8:8", "const:4:8"]]
- 00afb6a8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afb770 ["INT_ADD", "register:40f0:8", ["const:afb770:8", "const:4:8"]]
+ 00afb770 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afb6a8 bytes 1e890394
+ 00afb770 bytes 18890394
- 00afb6ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c30:8"]]
- 00afb6ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00afb6ec bytes 341906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee2a257354864b1c5bd97ee384c0b133"></a>

### [`00afb720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb720.md) → [`00afb7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb7e8.md) _ZN8firebase8callback9TerminateEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde860.md) · 呼出先 4件 [`00afb87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bdeb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb60.md)
- 新版 呼出元 1件 [`00bde910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde910.md) · 呼出先 4件 [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdec10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afb814",
      "incomplete_value": true,
      "site": "00afb814",
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
      "definition_site": "00afb74c",
      "incomplete_value": true,
      "site": "00afb74c",
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
      "definition_site": "00afb800",
      "incomplete_value": true,
      "site": "00afb804",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "00afb738",
      "incomplete_value": true,
      "site": "00afb73c",
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
                "const:c20:8"
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
      "definition_site": "00afb81c",
      "incomplete_value": true,
      "site": "00afb820",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": null,
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
      "00afb7f8",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb80c",
      "READ",
      [
        "storage",
        "010a0c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afb7f8",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb80c",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb720.md#insn-00afb73c) · [`00afb74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb720.md#insn-00afb74c) · [`00afb758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb720.md#insn-00afb758)
- 新版 `00afb804`（命令位置の公開資料なし） · `00afb814`（命令位置の公開資料なし） · `00afb820`（命令位置の公開資料なし）

~~~diff
- 00afb73c ["INT_ADD", "register:40f0:8", ["const:afb73c:8", "const:4:8"]]
- 00afb73c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afb804 ["INT_ADD", "register:40f0:8", ["const:afb804:8", "const:4:8"]]
+ 00afb804 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afb73c bytes f9880394
+ 00afb804 bytes f3880394
- 00afb74c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00afb74c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00afb814 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00afb814 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00afb74c bytes a80000b4
+ 00afb814 bytes a80000b4
- 00afb758 ["INT_ADD", "register:40f0:8", ["const:afb758:8", "const:4:8"]]
- 00afb758 ["CALL", null, ["callee:00bdec10:8"]]
+ 00afb820 ["INT_ADD", "register:40f0:8", ["const:afb820:8", "const:4:8"]]
+ 00afb820 ["CALL", null, ["callee:00bdec10:8"]]
- 00afb758 bytes 028d0394
+ 00afb820 bytes fc8c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6437e11829d240aa62ccd7e37161a3e9"></a>

### [`00afb774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb774.md) → [`00afb83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb83c.md) _ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb60.md) · 呼出先 4件 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bdec10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec10.md) · 呼出先 4件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.76% / 新版 75.76%

CFGの説明率　旧版 17.86% / 新版 17.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb774"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb778"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb778"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb774",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb778",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afb77c",
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
      "00afb83c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00afb840",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afb844",
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

- 旧版 [`00afb774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb774.md#insn-00afb774) · [`00afb778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb774.md#insn-00afb778) · [`00afb77c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb774.md#insn-00afb77c)

~~~diff
- 00afb774 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00afb774 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00afb774 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afb774 bytes f70f1cf8
- 00afb778 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afb778 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afb778 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afb778 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb778 bytes f65701a9
- 00afb77c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afb77c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afb77c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afb77c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afb77c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639282c6c7bea94cb681576d1f01efd4"></a>

### [`00afb87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md) → [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) FUN_00afb944

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00afb720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb720.md) [`00afbc54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbc54.md) [`00afbd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbd80.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md)
- 新版 呼出元 3件 [`00afb7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb7e8.md) [`00afbd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md) [`00afbe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb8b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb8d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb8e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afb890",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb96c",
      "READ",
      [
        "storage",
        "010a0c28",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00afb8b0",
      "WRITE",
      [
        "storage",
        "010a0c28",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00afb958",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb96c",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afb978",
      "WRITE",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb89c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md#insn-00afb89c) · [`00afb8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md#insn-00afb8b0) · [`00afb8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md#insn-00afb8b4)
- 新版 `00afb964`（命令位置の公開資料なし）

~~~diff
- 00afb89c ["INT_ADD", "register:40f0:8", ["const:afb89c:8", "const:4:8"]]
- 00afb89c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afb964 ["INT_ADD", "register:40f0:8", ["const:afb964:8", "const:4:8"]]
+ 00afb964 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afb89c bytes a1880394
+ 00afb964 bytes 9b880394
- 00afb8b0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c28:8"]]
- 00afb8b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00afb8b0 bytes a12a0cb9
- 00afb8b4 ["BOOL_NEGATE", "tmp:0:1", ["register:100:1"]]
- 00afb8b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00afb8b4 bytes a5000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0de894420d55fb06ffabd838121a6c72"></a>

### [`00afb93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb93c.md) → [`00afba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afba04.md) _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb30.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md) [`00bdeb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb50.md)
- 新版 呼出元 1件 [`00bdebe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebe0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md) [`00bdec00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb9b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afb9bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afba78"
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
      "00afba1c",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00afb964",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba3c",
      "READ",
      [
        "storage",
        "010a0c28",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00afba1c",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba2c",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba3c",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb93c.md#insn-00afb960) · [`00afb96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb93c.md#insn-00afb96c) · [`00afb9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb93c.md#insn-00afb9b0)
- 新版 `00afba28`（命令位置の公開資料なし） · `00afba34`（命令位置の公開資料なし）

~~~diff
- 00afb960 ["INT_ADD", "register:40f0:8", ["const:afb960:8", "const:4:8"]]
- 00afb960 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afba28 ["INT_ADD", "register:40f0:8", ["const:afba28:8", "const:4:8"]]
+ 00afba28 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afb960 bytes 70880394
+ 00afba28 bytes 6a880394
- 00afb96c ["INT_ADD", "register:40f0:8", ["const:afb96c:8", "const:4:8"]]
- 00afb96c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afba34 ["INT_ADD", "register:40f0:8", ["const:afba34:8", "const:4:8"]]
+ 00afba34 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afb96c bytes 6d880394
+ 00afba34 bytes 67880394
- 00afb9b0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c30:8"]]
- 00afb9b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00afb9b0 bytes f61a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f522d4619b420b1b60ad858483f8dea8"></a>

### [`00afb9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb9f4.md) → [`00afbabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbabc.md) _ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb50.md) · 呼出先 5件 [`00afc23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc23c.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bdec00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec00.md) · 呼出先 5件 [`00afc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc304.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 7.14% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afba30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afba38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afba3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afbaec",
      "READ",
      [
        "storage",
        "00c1b888",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afba38",
      "DATA",
      [
        "storage",
        "00c106f8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00afbb7c",
      "READ",
      [
        "storage",
        "00c10708",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00afbaec",
      "READ",
      [
        "storage",
        "00c1b938",
        null,
        "pointer"
      ]
    ],
    [
      "00afbb00",
      "DATA",
      [
        "storage",
        "00c107a8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00afbb7c",
      "READ",
      [
        "storage",
        "00c107b8",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afba18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb9f4.md#insn-00afba18) · [`00afba30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb9f4.md#insn-00afba30) · [`00afba38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb9f4.md#insn-00afba38)
- 新版 `00afbae0`（命令位置の公開資料なし）

~~~diff
- 00afba18 ["INT_ADD", "register:40f0:8", ["const:afba18:8", "const:4:8"]]
- 00afba18 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afbae0 ["INT_ADD", "register:40f0:8", ["const:afbae0:8", "const:4:8"]]
+ 00afbae0 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afba18 bytes 4a7d0394
+ 00afbae0 bytes 447d0394
- 00afba30 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00afba30 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00afba30 ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:8:8"]]
- 00afba30 ["STORE", null, ["const:1b1:8", "register:40b8:8", "tmp:1:8"]]
- 00afba30 bytes ff8e00f8
- 00afba38 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afba38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afba38 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f29036221751e5c89086e4e0968702ab"></a>

### [`00afbadc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbadc.md) → [`00afbba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbba4.md) _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6d0.md) [`00bdeb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb30.md) [`00bdeb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bdebe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebe0.md) [`00bdec40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec40.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00afbb30",
      "incomplete_value": true,
      "site": "00afbb38",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afbbb4",
      "READ",
      [
        "storage",
        "010a0c38",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00afbb04",
      "READ",
      [
        "storage",
        "010a0c40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afbbb4",
      "READ",
      [
        "storage",
        "010a0cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00afbbcc",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbb38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbadc.md#insn-00afbb38) · [`00afbaec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbadc.md#insn-00afbaec) · [`00afbafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbadc.md#insn-00afbafc)
- 新版 `00afbc00`（命令位置の公開資料なし） · `00afbbb4`（命令位置の公開資料なし） · `00afbbc4`（命令位置の公開資料なし）

~~~diff
- 00afbb38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afbb38 ["INT_ADD", "register:40f0:8", ["const:afbb38:8", "const:4:8"]]
- 00afbb38 ["CALLIND", null, ["register:0:8"]]
+ 00afbc00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afbc00 ["INT_ADD", "register:40f0:8", ["const:afbc00:8", "const:4:8"]]
+ 00afbc00 ["CALLIND", null, ["register:0:8"]]
- 00afbb38 bytes 00013fd6
+ 00afbc00 bytes 00013fd6
- 00afbaec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c38:8"]]
- 00afbaec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00afbaec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00afbbb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf8:8"]]
+ 00afbbb4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00afbbb4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00afbaec bytes 08e17039
+ 00afbbb4 bytes 08e17339
- 00afbafc ["INT_ADD", "register:40f0:8", ["const:afbafc:8", "const:4:8"]]
- 00afbafc ["CALL", null, ["callee:00bdb780:8"]]
+ 00afbbc4 ["INT_ADD", "register:40f0:8", ["const:afbbc4:8", "const:4:8"]]
+ 00afbbc4 ["CALL", null, ["callee:00bdb780:8"]]
- 00afbafc bytes f57e0394
+ 00afbbc4 bytes ef7e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab42784601654a61d75309923b3e9b9"></a>

### [`00afbb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbb64.md) → [`00afbc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbc2c.md) _ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6d0.md) [`00bdeb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb30.md) [`00bdeb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bdebe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebe0.md) [`00bdec40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 81.67% / 新版 81.67%

CFGの説明率　旧版 33.33% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbb68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbb6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbb6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afbb68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afbb6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afbb70",
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
      "00afbc30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afbc34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afbc38",
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

- 旧版 [`00afbb68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbb64.md#insn-00afbb68) · [`00afbb6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbb64.md#insn-00afbb6c) · [`00afbb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbb64.md#insn-00afbb70)

~~~diff
- 00afbb68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00afbb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afbb68 bytes f51300f9
- 00afbb6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afbb6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afbb6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afbb6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afbb6c bytes f44f03a9
- 00afbb70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afbb70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afbb70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00afbb70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afbb70 bytes fd7b04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-428965d557de72a99251c688c84bbd14"></a>

### [`00afbc54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbc54.md) → [`00afbd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md) _ZN8firebase8callback14RemoveCallbackEPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afb87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.33% / 新版 69.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbcd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afbda0"
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
      "00afbd38",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbd4c",
      "READ",
      [
        "storage",
        "010a0c28",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00afbc90",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afbd38",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbd4c",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afbd58",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbc7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbc54.md#insn-00afbc7c) · [`00afbc84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbc54.md#insn-00afbc84) · [`00afbc98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbc54.md#insn-00afbc98)
- 新版 `00afbd44`（命令位置の公開資料なし） · `00afbd4c`（命令位置の公開資料なし）

~~~diff
- 00afbc7c ["INT_ADD", "register:40f0:8", ["const:afbc7c:8", "const:4:8"]]
- 00afbc7c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afbd44 ["INT_ADD", "register:40f0:8", ["const:afbd44:8", "const:4:8"]]
+ 00afbd44 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afbc7c bytes a9870394
+ 00afbd44 bytes a3870394
- 00afbc84 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c28:8"]]
- 00afbc84 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00afbc84 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00afbd4c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ce8:8"]]
+ 00afbd4c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00afbd4c ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00afbc84 bytes 082b4cb9
+ 00afbd4c bytes 08eb4cb9
- 00afbc98 ["INT_ADD", "register:40f0:8", ["const:afbc98:8", "const:4:8"]]
- 00afbc98 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afbc98 bytes a2870394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd89c47c1c65bfb547784e4a1925f625"></a>

### [`00afbd80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbd80.md) → [`00afbe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md) _ZN8firebase8callback13PollCallbacksEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00afb87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb87c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdb6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6d0.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.88% / 新版 72.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbdfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbe08"
    }
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afbeec",
      "incomplete_value": false,
      "site": "00afbeec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbe24",
      "incomplete_value": false,
      "site": "00afbe24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "00afbe60",
      "READ",
      [
        "storage",
        "010a0c20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00afbda8",
      "READ",
      [
        "storage",
        "010a0c28",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00afbdb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afbf1c"
      ]
    ]
  ],
  "added": [
    [
      "00afbe60",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbe70",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afbe78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afbf1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbd80.md#insn-00afbda0) · [`00afbdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbd80.md#insn-00afbdb0) · [`00afbdbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbd80.md#insn-00afbdbc)
- 新版 `00afbe68`（命令位置の公開資料なし）

~~~diff
- 00afbda0 ["INT_ADD", "register:40f0:8", ["const:afbda0:8", "const:4:8"]]
- 00afbda0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afbe68 ["INT_ADD", "register:40f0:8", ["const:afbe68:8", "const:4:8"]]
+ 00afbe68 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afbda0 bytes 60870394
+ 00afbe68 bytes 5a870394
- 00afbdb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00afbdb0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00afbdb0 bytes 2b050054
- 00afbdbc ["INT_ADD", "register:40f0:8", ["const:afbdbc:8", "const:4:8"]]
- 00afbdbc ["CALL", null, ["callee:00bddbd0:8"]]
- 00afbdbc bytes 59870394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52d220b784e85591ed909fac4e4f7566"></a>

### [`00afbe6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbe6c.md) → [`00afbf34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbf34.md) _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb70.md) · 呼出先 5件 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bdeb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb40.md)
- 新版 呼出元 1件 [`00bdec20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec20.md) · 呼出先 5件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdebf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebf0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 17.65% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afbf8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afbe98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afbe90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bddbd0"
      ]
    ],
    [
      "unmatched:00afbe98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc044"
      ]
    ],
    [
      "unmatched:00afbeb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afbf98"
      ]
    ]
  ],
  "added": [
    [
      "00afbf58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bddbd0"
      ]
    ],
    [
      "00afbf60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc044"
      ]
    ],
    [
      "00afbf7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afbf98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbe90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbe6c.md#insn-00afbe90) · [`00afbe98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbe6c.md#insn-00afbe98) · [`00afbeb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbe6c.md#insn-00afbeb4)

~~~diff
- 00afbe90 ["INT_ADD", "register:40f0:8", ["const:afbe90:8", "const:4:8"]]
- 00afbe90 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afbe90 bytes 24870394
- 00afbe98 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00afbe98 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00afbe98 bytes 280700b4
- 00afbeb4 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00afbeb4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00afbeb4 bytes f60000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e9859e6dd9b5829d7c5ea0d16355117"></a>

### [`00afbfa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbfa4.md) → [`00afc06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc06c.md) _ZN8firebase8callback18CallbackDispatcherD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb80.md) · 呼出先 6件 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md)
- 新版 呼出元 1件 [`00bdec30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec30.md) · 呼出先 6件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.51% / 新版 74.51%

CFGの説明率　旧版 20.00% / 新版 17.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc0c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc0cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afc098",
      "PARAM",
      [
        "storage",
        "0029dcf0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00afbff0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc158"
      ]
    ],
    [
      "unmatched:00afc014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc0d0"
      ]
    ]
  ],
  "added": [
    [
      "00afc098",
      "PARAM",
      [
        "storage",
        "0029dd7d",
        null,
        "string"
      ]
    ],
    [
      "00afc0b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc158"
      ]
    ],
    [
      "00afc0dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc0d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbfd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbfa4.md#insn-00afbfd4) · [`00afbfe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbfa4.md#insn-00afbfe8) · [`00afbff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbfa4.md#insn-00afbff0)
- 新版 `00afc09c`（命令位置の公開資料なし） · `00afc0b0`（命令位置の公開資料なし）

~~~diff
- 00afbfd4 ["INT_ADD", "register:40f0:8", ["const:afbfd4:8", "const:4:8"]]
- 00afbfd4 ["CALL", null, ["callee:00bddf10:8"]]
+ 00afc09c ["INT_ADD", "register:40f0:8", ["const:afc09c:8", "const:4:8"]]
+ 00afc09c ["CALL", null, ["callee:00bddf10:8"]]
- 00afbfd4 bytes a3870394
+ 00afc09c bytes 9d870394
- 00afbfe8 ["INT_ADD", "register:40f0:8", ["const:afbfe8:8", "const:4:8"]]
- 00afbfe8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00afc0b0 ["INT_ADD", "register:40f0:8", ["const:afc0b0:8", "const:4:8"]]
+ 00afc0b0 ["CALL", null, ["callee:00bdb010:8"]]
- 00afbfe8 bytes de7b0394
+ 00afc0b0 bytes d87b0394
- 00afbff0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00afbff0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00afbff0 bytes 080500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dce55615871e17653f0d230efd53133"></a>

### [`00afc13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc13c.md) → [`00afc204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc204.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 10.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc13c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc140"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc13c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc140",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc144",
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
      "00afc204",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afc208",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afc20c",
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

- 旧版 [`00afc13c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc13c.md#insn-00afc13c) · [`00afc140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc13c.md#insn-00afc140) · [`00afc144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc13c.md#insn-00afc144)

~~~diff
- 00afc13c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afc13c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afc13c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc13c bytes f50f1df8
- 00afc140 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc140 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc140 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc140 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc140 bytes f44f01a9
- 00afc144 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc144 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc144 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afc144 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc144 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f3df13da31ea2ed3f44f5d52702ba3"></a>

### [`00afc1b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc1b8.md) → [`00afc280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc280.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 11.11% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afc2a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afc2a8",
      "incomplete_value": true,
      "site": "00afc2ac",
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
                "const:20:8"
              ]
            ]
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
      "unmatched:00afc1d0",
      "READ",
      [
        "storage",
        "00c1b888",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afc1dc",
      "DATA",
      [
        "storage",
        "00c106f8",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00afc298",
      "READ",
      [
        "storage",
        "00c1b938",
        null,
        "pointer"
      ]
    ],
    [
      "00afc2a4",
      "DATA",
      [
        "storage",
        "00c107a8",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc1b8.md#insn-00afc1dc) · [`00afc1e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc1b8.md#insn-00afc1e4)
- 新版 `00afc2ac`（命令位置の公開資料なし） · `00afc2a4`（命令位置の公開資料なし）

~~~diff
- 00afc1dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afc1dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afc1dc bytes 080000f9
- 00afc1e4 ["INT_ADD", "register:40f0:8", ["const:afc1e4:8", "const:4:8"]]
- 00afc1e4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afc2ac ["INT_ADD", "register:40f0:8", ["const:afc2ac:8", "const:4:8"]]
+ 00afc2ac ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc1e4 bytes 4f860394
+ 00afc2ac bytes 49860394
+ 00afc2a4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00afc2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00afc2a4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7973028a3787a507ad6ed3ee6d9171"></a>

### [`00afc2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc2ac.md) → [`00afc374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc374.md) _ZN8firebase8callback16BlockingCallbackD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdebc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdebc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00afc390",
      "incomplete_value": true,
      "site": "00afc394",
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
      "definition_site": "00afc2c8",
      "incomplete_value": true,
      "site": "00afc2cc",
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
      "00afc388",
      "READ",
      [
        "storage",
        "00c1b880",
        null,
        "pointer"
      ]
    ],
    [
      "00afc394",
      "DATA",
      [
        "storage",
        "00c10748",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00afc388",
      "READ",
      [
        "storage",
        "00c1b930",
        null,
        "pointer"
      ]
    ],
    [
      "00afc394",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc2ac.md#insn-00afc2c0) · [`00afc2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc2ac.md#insn-00afc2d4)
- 新版 `00afc388`（命令位置の公開資料なし） · `00afc39c`（命令位置の公開資料なし）

~~~diff
- 00afc2c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:880:8"]]
- 00afc2c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afc388 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:930:8"]]
+ 00afc388 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc2c0 bytes 294144f9
+ 00afc388 bytes 299944f9
- 00afc2d4 ["INT_ADD", "register:40f0:8", ["const:afc2d4:8", "const:4:8"]]
- 00afc2d4 ["CALL", null, ["callee:00bdec70:8"]]
+ 00afc39c ["INT_ADD", "register:40f0:8", ["const:afc39c:8", "const:4:8"]]
+ 00afc39c ["CALL", null, ["callee:00bdec70:8"]]
- 00afc2d4 bytes 3b8a0394
+ 00afc39c bytes 358a0394
~~~


<a id="compare-8d9468dcd011b55c921da9010749d16e"></a>

### [`00afc300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc300.md) → [`00afc3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc3c8.md) _ZN8firebase8callback16BlockingCallbackD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdebc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdebc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec70.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afc3e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afc3ec",
      "incomplete_value": true,
      "site": "00afc3f0",
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
            "register:4040:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afc324",
      "incomplete_value": true,
      "site": "00afc328",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc314",
      "READ",
      [
        "storage",
        "00c1b880",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00afc320",
      "DATA",
      [
        "storage",
        "00c10748",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "unmatched:00afc33c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00afc3dc",
      "READ",
      [
        "storage",
        "00c1b930",
        null,
        "pointer"
      ]
    ],
    [
      "00afc3e8",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00afc404",
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

- 旧版 [`00afc320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc300.md#insn-00afc320) · [`00afc328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc300.md#insn-00afc328) · [`00afc33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc300.md#insn-00afc33c)
- 新版 `00afc3f0`（命令位置の公開資料なし）

~~~diff
- 00afc320 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00afc320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00afc320 bytes 090000f9
- 00afc328 ["INT_ADD", "register:40f0:8", ["const:afc328:8", "const:4:8"]]
- 00afc328 ["CALL", null, ["callee:00bdec70:8"]]
+ 00afc3f0 ["INT_ADD", "register:40f0:8", ["const:afc3f0:8", "const:4:8"]]
+ 00afc3f0 ["CALL", null, ["callee:00bdec70:8"]]
- 00afc328 bytes 268a0394
+ 00afc3f0 bytes 208a0394
- 00afc33c ["COPY", "register:0:8", ["register:4040:8"]]
- 00afc33c ["INT_ADD", "register:40f0:8", ["const:afc33c:8", "const:4:8"]]
- 00afc33c ["CALLIND", null, ["register:0:8"]]
- 00afc33c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-427a57317708065353f90f472cc309bf"></a>

### [`00afc360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc360.md) → [`00afc428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc428.md) _ZN8firebase8callback13CallbackEntry7ExecuteEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeb40.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bdebf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebf0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 15.38% / 新版 15.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00afc378",
      "incomplete_value": true,
      "site": "00afc37c",
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
      "definition_site": "00afc3d4",
      "incomplete_value": true,
      "site": "00afc3d8",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afc4c0",
      "incomplete_value": true,
      "site": "00afc4c8",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 8,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afc37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc360.md#insn-00afc37c) · [`00afc3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc360.md#insn-00afc3d8) · [`00afc400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc360.md#insn-00afc400)
- 新版 `00afc444`（命令位置の公開資料なし） · `00afc4a0`（命令位置の公開資料なし） · `00afc4c8`（命令位置の公開資料なし）

~~~diff
- 00afc37c ["INT_ADD", "register:40f0:8", ["const:afc37c:8", "const:4:8"]]
- 00afc37c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afc444 ["INT_ADD", "register:40f0:8", ["const:afc444:8", "const:4:8"]]
+ 00afc444 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc37c bytes e9850394
+ 00afc444 bytes e3850394
- 00afc3d8 ["INT_ADD", "register:40f0:8", ["const:afc3d8:8", "const:4:8"]]
- 00afc3d8 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00afc4a0 ["INT_ADD", "register:40f0:8", ["const:afc4a0:8", "const:4:8"]]
+ 00afc4a0 ["CALL", null, ["callee:00bddbe0:8"]]
- 00afc3d8 bytes d6850394
+ 00afc4a0 bytes d0850394
- 00afc400 ["INT_ADD", "register:40f0:8", ["const:afc400:8", "const:4:8"]]
- 00afc400 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00afc4c8 ["INT_ADD", "register:40f0:8", ["const:afc4c8:8", "const:4:8"]]
+ 00afc4c8 ["CALL", null, ["callee:00bddbe0:8"]]
- 00afc400 bytes cc850394
+ 00afc4c8 bytes c6850394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

