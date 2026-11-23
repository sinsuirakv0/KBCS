# v15.7.2 → v15.7.3 · 最優先の変更候補 (64)

[一覧の目次](README.md)

<a id="compare-4b5de50c8ddc08c1a8adce56c470792f"></a>

### [`00b05b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b58.md) → [`00b05c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c20.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b05b58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05b58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05b5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05c30",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05c20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05c30",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05b58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b58.md#insn-00b05b58) · [`00b05b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b58.md#insn-00b05b5c) · [`00b05b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b58.md#insn-00b05b6c)
- 新版 [`00b05c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c20.md#insn-00b05c34)

~~~diff
- 00b05b58 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b05b58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b05b58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05b58 bytes f30f1ef8
- 00b05b5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05b5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05b5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05b5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05b5c bytes fd7b01a9
- 00b05b6c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05b6c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b05c34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b05c34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b05b6c bytes 080100b5
+ 00b05c34 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adc2900d35a114110795df8a766bfc74"></a>

### [`00b05ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ba8.md) → [`00b05c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md) _ZN8firebase7options15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b05cc8",
      "incomplete_value": true,
      "site": "00b05cc8",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c00",
      "incomplete_value": true,
      "site": "00b05c00",
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
            "const:d50:8"
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
      "definition_site": "00b05ca4",
      "incomplete_value": true,
      "site": "00b05cb0",
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bdc",
      "incomplete_value": true,
      "site": "00b05be8",
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
                "const:d48:8"
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
      "00b05c84",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05ca4",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05cc8",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b05c84",
      "READ",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05ca4",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05cc8",
      "WRITE",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ba8.md#insn-00b05be8) · [`00b05c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ba8.md#insn-00b05c00) · [`00b05bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ba8.md#insn-00b05bbc)
- 新版 [`00b05cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md#insn-00b05cb0) · [`00b05cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md#insn-00b05cc8) · [`00b05c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md#insn-00b05c84)

~~~diff
- 00b05be8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05be8 ["INT_ADD", "register:40f0:8", ["const:b05be8:8", "const:4:8"]]
- 00b05be8 ["CALLIND", null, ["register:0:8"]]
+ 00b05cb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05cb0 ["INT_ADD", "register:40f0:8", ["const:b05cb0:8", "const:4:8"]]
+ 00b05cb0 ["CALLIND", null, ["register:0:8"]]
- 00b05be8 bytes 00013fd6
+ 00b05cb0 bytes 00013fd6
- 00b05c00 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05c00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d50:8"]]
- 00b05c00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b05cc8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b05cc8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e10:8"]]
+ 00b05cc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05c00 bytes a0423539
+ 00b05cc8 bytes a0423839
- 00b05bbc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d50:8"]]
- 00b05bbc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b05bbc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b05c84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e10:8"]]
+ 00b05c84 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b05c84 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b05bbc bytes a8427539
+ 00b05c84 bytes a8427839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c13ae7da787e4b5eabe2e9bc2fc4ceb"></a>

### [`00b05c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c14.md) → [`00b05cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05cdc.md) _ZN8firebase7options12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b05c50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b05d18"
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
      "00b05cf0",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05cfc",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05d04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b05c54"
      ]
    ]
  ],
  "added": [
    [
      "00b05cf0",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05cfc",
      "READ",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05d04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05d1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c14.md#insn-00b05c2c) · [`00b05c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c14.md#insn-00b05c50) · [`00b05c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c14.md#insn-00b05c58)
- 新版 [`00b05cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05cdc.md#insn-00b05cf4)

~~~diff
- 00b05c2c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05c2c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b05cf4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b05cf4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b05c2c bytes 410200b4
+ 00b05cf4 bytes 410200b4
- 00b05c50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05c50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05c50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d50:8"]]
- 00b05c50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05c50 bytes bf423539
- 00b05c58 ["INT_ADD", "register:40f0:8", ["const:b05c58:8", "const:4:8"]]
- 00b05c58 ["CALL", null, ["callee:00bde090:8"]]
- 00b05c58 bytes e2600394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe2f800bc8078030b4c694912a682c4b"></a>

### [`00b05c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c84.md) → [`00b05d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md) _ZN8firebase7options14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b05d8c",
      "incomplete_value": true,
      "site": "00b05d8c",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05cc4",
      "incomplete_value": true,
      "site": "00b05cc4",
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
            "const:d48:8"
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
      "definition_site": "00b05d68",
      "incomplete_value": true,
      "site": "00b05d68",
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
      "definition_site": "00b05ca0",
      "incomplete_value": true,
      "site": "00b05ca0",
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
      "definition_site": "00b05d70",
      "incomplete_value": false,
      "site": "00b05d84",
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
            "const:eff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ca8",
      "incomplete_value": false,
      "site": "00b05cbc",
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
            "const:f06:8"
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
      "00b05d60",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05d70",
      "PARAM",
      [
        "storage",
        "002a4f06",
        null,
        "string"
      ]
    ],
    [
      "00b05d8c",
      "WRITE",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05d60",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05d70",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05d8c",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c84.md#insn-00b05cbc) · [`00b05cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c84.md#insn-00b05cc4) · [`00b05c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05c84.md#insn-00b05c98)
- 新版 [`00b05d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md#insn-00b05d84) · [`00b05d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md#insn-00b05d8c) · [`00b05d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md#insn-00b05d60)

~~~diff
- 00b05cbc ["INT_ADD", "register:40f0:8", ["const:b05cbc:8", "const:4:8"]]
- 00b05cbc ["CALL", null, ["callee:00bde040:8"]]
+ 00b05d84 ["INT_ADD", "register:40f0:8", ["const:b05d84:8", "const:4:8"]]
+ 00b05d84 ["CALL", null, ["callee:00bde040:8"]]
- 00b05cbc bytes b5600394
+ 00b05d84 bytes af600394
- 00b05cc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00b05cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05d8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
+ 00b05d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05cc4 bytes 80a606f9
+ 00b05d8c bytes 800607f9
- 00b05c98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00b05c98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05d60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
+ 00b05d60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05c98 bytes 81a646f9
+ 00b05d60 bytes 810647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6e15f2e21735e6f2f8c2ff76e5aeffe"></a>

### [`00b05cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05cf4.md) → [`00b05dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md) _ZN8firebase7options11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b05dd8",
      "incomplete_value": false,
      "site": "00b05ddc",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05d10",
      "incomplete_value": false,
      "site": "00b05d14",
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
      "definition_site": "00b05de8",
      "incomplete_value": true,
      "site": "00b05df4",
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
      "definition_site": "00b05d20",
      "incomplete_value": true,
      "site": "00b05d2c",
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
      "00b05dd8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b05de8",
      "DATA",
      [
        "storage",
        "010a0d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05dd8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b05de8",
      "DATA",
      [
        "storage",
        "010a0e18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05cf4.md#insn-00b05d14) · [`00b05d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05cf4.md#insn-00b05d10) · [`00b05d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05cf4.md#insn-00b05d1c)
- 新版 [`00b05ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md#insn-00b05ddc) · [`00b05dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md#insn-00b05dd8) · [`00b05de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md#insn-00b05de4)

~~~diff
- 00b05d14 ["INT_ADD", "register:40f0:8", ["const:b05d14:8", "const:4:8"]]
- 00b05d14 ["CALL", null, ["callee:00bde130:8"]]
+ 00b05ddc ["INT_ADD", "register:40f0:8", ["const:b05ddc:8", "const:4:8"]]
+ 00b05ddc ["CALL", null, ["callee:00bde130:8"]]
- 00b05d14 bytes db600394
+ 00b05ddc bytes d5600394
- 00b05d10 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b05d10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05d10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05d10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05dd8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b05dd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05dd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05dd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05d10 bytes 001c1591
+ 00b05dd8 bytes 00501791
- 00b05d1c ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00b05d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05de4 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00b05de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05d1c bytes 08613591
+ 00b05de4 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aae111d4e8e4827e5cc843f2207cad5"></a>

### [`00b05d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05d30.md) → [`00b05df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05df8.md) _ZN8firebase7options13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

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
      "site": "00b05d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05d30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05d34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05d30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05d44",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05e0c",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05d30.md#insn-00b05d30) · [`00b05d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05d30.md#insn-00b05d34) · [`00b05d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05d30.md#insn-00b05d4c)

~~~diff
- 00b05d30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05d30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05d30 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b05d30 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05d30 bytes f44fbea9
- 00b05d34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05d34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05d34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05d34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05d34 bytes fd7b01a9
- 00b05d4c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05d4c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b05d4c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18c41d6c0c842d3960f6cdb9dd8f5d38"></a>

### [`00b05da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05da0.md) → [`00b05e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md) _ZN8firebase7options10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b05e84",
      "incomplete_value": false,
      "site": "00b05e88",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05dbc",
      "incomplete_value": false,
      "site": "00b05dc0",
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
      "definition_site": "00b05e94",
      "incomplete_value": true,
      "site": "00b05ea0",
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
      "definition_site": "00b05dcc",
      "incomplete_value": true,
      "site": "00b05dd8",
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
      "00b05e84",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b05e94",
      "DATA",
      [
        "storage",
        "010a0d90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b05e84",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b05e94",
      "DATA",
      [
        "storage",
        "010a0e50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05da0.md#insn-00b05dc0) · [`00b05dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05da0.md#insn-00b05dbc) · [`00b05dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05da0.md#insn-00b05dc8)
- 新版 [`00b05e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md#insn-00b05e88) · [`00b05e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md#insn-00b05e84) · [`00b05e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md#insn-00b05e90)

~~~diff
- 00b05dc0 ["INT_ADD", "register:40f0:8", ["const:b05dc0:8", "const:4:8"]]
- 00b05dc0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b05e88 ["INT_ADD", "register:40f0:8", ["const:b05e88:8", "const:4:8"]]
+ 00b05e88 ["CALL", null, ["callee:00bde130:8"]]
- 00b05dc0 bytes b0600394
+ 00b05e88 bytes aa600394
- 00b05dbc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b05dbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05dbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05dbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05e84 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b05e84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05e84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05e84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05dbc bytes 00c81791
+ 00b05e84 bytes 00fc1991
- 00b05dc8 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00b05dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05e90 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00b05e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05dc8 bytes 08413691
+ 00b05e90 bytes 08413991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c8cdcf1407b973385da87661e2e03b1"></a>

### [`00b05ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ddc.md) → [`00b05ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05ed0",
      "incomplete_value": true,
      "site": "00b05ed0",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e08",
      "incomplete_value": true,
      "site": "00b05e08",
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
            "const:d98:8"
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
      "definition_site": "00b05eb8",
      "incomplete_value": true,
      "site": "00b05eb8",
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
      "definition_site": "00b05df0",
      "incomplete_value": true,
      "site": "00b05df0",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b05df0"
      ],
      [
        "FALL_THROUGH",
        "00b05eb8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b05eb8",
      "incomplete_value": true,
      "site": "00b05ed0",
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
      "definition_site": "00b05df0",
      "incomplete_value": true,
      "site": "00b05e08",
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
      "00b05eb4",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05ed0",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05eb4",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05ed0",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ddc.md#insn-00b05e08) · [`00b05dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ddc.md#insn-00b05dec) · [`00b05e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ddc.md#insn-00b05e00)
- 新版 [`00b05ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md#insn-00b05ed0) · [`00b05eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md#insn-00b05eb4) · [`00b05ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md#insn-00b05ec8)

~~~diff
- 00b05e08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05e08 bytes 60ce06f9
+ 00b05ed0 bytes 602e07f9
- 00b05dec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05dec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05eb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05eb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05dec bytes 68ce46f9
+ 00b05eb4 bytes 682e47f9
- 00b05e00 ["INT_ADD", "register:40f0:8", ["const:b05e00:8", "const:4:8"]]
- 00b05e00 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05ec8 ["INT_ADD", "register:40f0:8", ["const:b05ec8:8", "const:4:8"]]
+ 00b05ec8 ["CALL", null, ["callee:00bde040:8"]]
- 00b05e00 bytes 64600394
+ 00b05ec8 bytes 5e600394
~~~


<a id="compare-630ef50e1077d4948e94a4732fafd393"></a>

### [`00b05e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e1c.md) → [`00b05ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05f10",
      "incomplete_value": true,
      "site": "00b05f10",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e48",
      "incomplete_value": true,
      "site": "00b05e48",
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
            "const:d98:8"
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
      "definition_site": "00b05ef8",
      "incomplete_value": true,
      "site": "00b05ef8",
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
      "definition_site": "00b05e30",
      "incomplete_value": true,
      "site": "00b05e30",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b05e30"
      ],
      [
        "FALL_THROUGH",
        "00b05ef8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b05ef8",
      "incomplete_value": true,
      "site": "00b05f10",
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
      "definition_site": "00b05e30",
      "incomplete_value": true,
      "site": "00b05e48",
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
      "00b05ef4",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f10",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05ef4",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f10",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e1c.md#insn-00b05e48) · [`00b05e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e1c.md#insn-00b05e2c) · [`00b05e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e1c.md#insn-00b05e40)
- 新版 [`00b05f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md#insn-00b05f10) · [`00b05ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md#insn-00b05ef4) · [`00b05f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md#insn-00b05f08)

~~~diff
- 00b05e48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05e48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05f10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05f10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05e48 bytes 60ce06f9
+ 00b05f10 bytes 602e07f9
- 00b05e2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05e2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05ef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05e2c bytes 68ce46f9
+ 00b05ef4 bytes 682e47f9
- 00b05e40 ["INT_ADD", "register:40f0:8", ["const:b05e40:8", "const:4:8"]]
- 00b05e40 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05f08 ["INT_ADD", "register:40f0:8", ["const:b05f08:8", "const:4:8"]]
+ 00b05f08 ["CALL", null, ["callee:00bde040:8"]]
- 00b05e40 bytes 54600394
+ 00b05f08 bytes 4e600394
~~~


<a id="compare-748d7c63a751caeff85fd9e154c5b6cc"></a>

### [`00b05e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e5c.md) → [`00b05f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05f54",
      "incomplete_value": true,
      "site": "00b05f54",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e8c",
      "incomplete_value": true,
      "site": "00b05e8c",
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
            "const:d98:8"
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
      "definition_site": "00b05f38",
      "incomplete_value": true,
      "site": "00b05f38",
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
      "definition_site": "00b05e70",
      "incomplete_value": true,
      "site": "00b05e70",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b05e70"
      ],
      [
        "FALL_THROUGH",
        "00b05f38"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b05f38",
      "incomplete_value": true,
      "site": "00b05f54",
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
      "definition_site": "00b05e70",
      "incomplete_value": true,
      "site": "00b05e8c",
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
      "00b05f34",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f54",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05f34",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f54",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e5c.md#insn-00b05e8c) · [`00b05e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e5c.md#insn-00b05e6c) · [`00b05e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05e5c.md#insn-00b05e84)
- 新版 [`00b05f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md#insn-00b05f54) · [`00b05f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md#insn-00b05f34) · [`00b05f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md#insn-00b05f4c)

~~~diff
- 00b05e8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05f54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05f54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05e8c bytes 60ce06f9
+ 00b05f54 bytes 602e07f9
- 00b05e6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05e6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05f34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05e6c bytes 68ce46f9
+ 00b05f34 bytes 682e47f9
- 00b05e84 ["INT_ADD", "register:40f0:8", ["const:b05e84:8", "const:4:8"]]
- 00b05e84 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05f4c ["INT_ADD", "register:40f0:8", ["const:b05f4c:8", "const:4:8"]]
+ 00b05f4c ["CALL", null, ["callee:00bde040:8"]]
- 00b05e84 bytes 43600394
+ 00b05f4c bytes 3d600394
~~~


<a id="compare-707e2fd8b468398e3ce3820bb9e7e8ef"></a>

### [`00b05ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ea0.md) → [`00b05f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05f98",
      "incomplete_value": true,
      "site": "00b05f98",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ed0",
      "incomplete_value": true,
      "site": "00b05ed0",
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
            "const:d98:8"
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
      "definition_site": "00b05f7c",
      "incomplete_value": true,
      "site": "00b05f7c",
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
      "definition_site": "00b05eb4",
      "incomplete_value": true,
      "site": "00b05eb4",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b05eb4"
      ],
      [
        "FALL_THROUGH",
        "00b05f7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b05f7c",
      "incomplete_value": true,
      "site": "00b05f98",
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
      "definition_site": "00b05eb4",
      "incomplete_value": true,
      "site": "00b05ed0",
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
      "00b05f78",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f98",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05f78",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f98",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ea0.md#insn-00b05ed0) · [`00b05eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ea0.md#insn-00b05eb0) · [`00b05ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ea0.md#insn-00b05ec8)
- 新版 [`00b05f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md#insn-00b05f98) · [`00b05f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md#insn-00b05f78) · [`00b05f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md#insn-00b05f90)

~~~diff
- 00b05ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05f98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05ed0 bytes 60ce06f9
+ 00b05f98 bytes 602e07f9
- 00b05eb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d98:8"]]
- 00b05eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
+ 00b05f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05eb0 bytes 68ce46f9
+ 00b05f78 bytes 682e47f9
- 00b05ec8 ["INT_ADD", "register:40f0:8", ["const:b05ec8:8", "const:4:8"]]
- 00b05ec8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05f90 ["INT_ADD", "register:40f0:8", ["const:b05f90:8", "const:4:8"]]
+ 00b05f90 ["CALL", null, ["callee:00bde040:8"]]
- 00b05ec8 bytes 32600394
+ 00b05f90 bytes 2c600394
~~~


<a id="compare-a662ad8d7c81271eca0a31f8a1e665bd"></a>

### [`00b05ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ef0.md) → [`00b05fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md) _ZN8firebase17version_registrar15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b06010",
      "incomplete_value": true,
      "site": "00b06010",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f48",
      "incomplete_value": true,
      "site": "00b05f48",
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
            "const:da0:8"
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
      "definition_site": "00b05fec",
      "incomplete_value": true,
      "site": "00b05ff8",
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f24",
      "incomplete_value": true,
      "site": "00b05f30",
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
                "const:d98:8"
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
      "00b05fcc",
      "READ",
      [
        "storage",
        "010a0da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05fec",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06010",
      "WRITE",
      [
        "storage",
        "010a0da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b05fcc",
      "READ",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05fec",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06010",
      "WRITE",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ef0.md#insn-00b05f30) · [`00b05f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ef0.md#insn-00b05f48) · [`00b05f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ef0.md#insn-00b05f04)
- 新版 [`00b05ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md#insn-00b05ff8) · [`00b06010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md#insn-00b06010) · [`00b05fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md#insn-00b05fcc)

~~~diff
- 00b05f30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05f30 ["INT_ADD", "register:40f0:8", ["const:b05f30:8", "const:4:8"]]
- 00b05f30 ["CALLIND", null, ["register:0:8"]]
+ 00b05ff8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05ff8 ["INT_ADD", "register:40f0:8", ["const:b05ff8:8", "const:4:8"]]
+ 00b05ff8 ["CALLIND", null, ["register:0:8"]]
- 00b05f30 bytes 00013fd6
+ 00b05ff8 bytes 00013fd6
- 00b05f48 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05f48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:da0:8"]]
- 00b05f48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b06010 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b06010 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e60:8"]]
+ 00b06010 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05f48 bytes a0823639
+ 00b06010 bytes a0823939
- 00b05f04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:da0:8"]]
- 00b05f04 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b05f04 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b05fcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e60:8"]]
+ 00b05fcc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b05fcc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b05f04 bytes a8827639
+ 00b05fcc bytes a8827939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec2f4a89712fed419d9e042c450cce9f"></a>

### [`00b05f5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05f5c.md) → [`00b06024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md) _ZN8firebase17version_registrar12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b06060",
      "incomplete_value": true,
      "site": "00b06060",
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
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f98",
      "incomplete_value": true,
      "site": "00b05f98",
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
            "const:da0:8"
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
      "definition_site": "00b06080",
      "incomplete_value": true,
      "site": "00b06080",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05fb8",
      "incomplete_value": true,
      "site": "00b05fb8",
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
            "const:d98:8"
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
      "definition_site": "00b0603c",
      "incomplete_value": true,
      "site": "00b0603c",
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
      "definition_site": "00b05f74",
      "incomplete_value": true,
      "site": "00b05f74",
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
      "00b06038",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06044",
      "READ",
      [
        "storage",
        "010a0da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b06060",
      "WRITE",
      [
        "storage",
        "010a0da0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b06038",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06044",
      "READ",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b06060",
      "WRITE",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05f5c.md#insn-00b05f98) · [`00b05fb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05f5c.md#insn-00b05fb4) · [`00b05fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05f5c.md#insn-00b05fb8)
- 新版 [`00b06060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md#insn-00b06060) · [`00b0607c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md#insn-00b0607c) · [`00b06080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md#insn-00b06080)

~~~diff
- 00b05f98 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05f98 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05f98 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:da0:8"]]
- 00b05f98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b06060 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b06060 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b06060 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e60:8"]]
+ 00b06060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05f98 bytes bf823639
+ 00b06060 bytes bf823939
- 00b05fb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05fb4 ["INT_ADD", "register:40f0:8", ["const:b05fb4:8", "const:4:8"]]
- 00b05fb4 ["CALLIND", null, ["register:0:8"]]
+ 00b0607c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0607c ["INT_ADD", "register:40f0:8", ["const:b0607c:8", "const:4:8"]]
+ 00b0607c ["CALLIND", null, ["register:0:8"]]
- 00b05fb4 bytes 00013fd6
+ 00b0607c bytes 00013fd6
- 00b05fb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00b05fb8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b05fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b06080 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
+ 00b06080 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b06080 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b05fb8 bytes 9fce06f9
+ 00b06080 bytes 9f2e07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a0a2029cb99e4627f321926c192ad2f"></a>

### [`00b05fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05fcc.md) → [`00b06094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md) _ZN8firebase17version_registrar14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b060d4",
      "incomplete_value": true,
      "site": "00b060d4",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0600c",
      "incomplete_value": true,
      "site": "00b0600c",
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
            "const:d98:8"
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
      "definition_site": "00b060b0",
      "incomplete_value": true,
      "site": "00b060b0",
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
      "definition_site": "00b05fe8",
      "incomplete_value": true,
      "site": "00b05fe8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b05fe8"
      ],
      [
        "FALL_THROUGH",
        "00b060b0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b060b0",
      "incomplete_value": true,
      "site": "00b060d4",
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
      "definition_site": "00b05fe8",
      "incomplete_value": true,
      "site": "00b0600c",
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
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b060a8",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b060d4",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b060e8",
      "PARAM",
      [
        "storage",
        "00c10b78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b060a8",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b060d4",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b060e8",
      "PARAM",
      [
        "storage",
        "00c10c28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0600c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05fcc.md#insn-00b0600c) · [`00b05fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05fcc.md#insn-00b05fe0) · [`00b06004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05fcc.md#insn-00b06004)
- 新版 [`00b060d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md#insn-00b060d4) · [`00b060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md#insn-00b060a8) · [`00b060cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md#insn-00b060cc)

~~~diff
- 00b0600c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00b0600c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b060d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
+ 00b060d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b0600c bytes 80ce06f9
+ 00b060d4 bytes 802e07f9
- 00b05fe0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00b05fe0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b060a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
+ 00b060a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05fe0 bytes 81ce46f9
+ 00b060a8 bytes 812e47f9
- 00b06004 ["INT_ADD", "register:40f0:8", ["const:b06004:8", "const:4:8"]]
- 00b06004 ["CALL", null, ["callee:00bde040:8"]]
+ 00b060cc ["INT_ADD", "register:40f0:8", ["const:b060cc:8", "const:4:8"]]
+ 00b060cc ["CALL", null, ["callee:00bde040:8"]]
- 00b06004 bytes e35f0394
+ 00b060cc bytes dd5f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-811a34262b300a820c9a8c3d821df41f"></a>

### [`00b0603c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b0603c.md) → [`00b06104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md) _ZN8firebase17version_registrar11GetMethodIdENS0_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b06120",
      "incomplete_value": false,
      "site": "00b06124",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06058",
      "incomplete_value": false,
      "site": "00b0605c",
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
      "definition_site": "00b06130",
      "incomplete_value": true,
      "site": "00b0613c",
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
      "definition_site": "00b06068",
      "incomplete_value": true,
      "site": "00b06074",
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
      "00b06120",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b06130",
      "DATA",
      [
        "storage",
        "010a0da8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b06120",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b06130",
      "DATA",
      [
        "storage",
        "010a0e68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0605c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b0603c.md#insn-00b0605c) · [`00b06058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b0603c.md#insn-00b06058) · [`00b06064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b0603c.md#insn-00b06064)
- 新版 [`00b06124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md#insn-00b06124) · [`00b06120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md#insn-00b06120) · [`00b0612c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md#insn-00b0612c)

~~~diff
- 00b0605c ["INT_ADD", "register:40f0:8", ["const:b0605c:8", "const:4:8"]]
- 00b0605c ["CALL", null, ["callee:00bde130:8"]]
+ 00b06124 ["INT_ADD", "register:40f0:8", ["const:b06124:8", "const:4:8"]]
+ 00b06124 ["CALL", null, ["callee:00bde130:8"]]
- 00b0605c bytes 09600394
+ 00b06124 bytes 03600394
- 00b06058 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b06058 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b06058 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b06058 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b06120 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b06120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b06120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b06120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b06058 bytes 001c1591
+ 00b06120 bytes 00501791
- 00b06064 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00b06064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b06064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b06064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0612c ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00b0612c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0612c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0612c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b06064 bytes 08a13691
+ 00b0612c bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4ce39c9c01895cc282278ad21f5dda5"></a>

### [`00b060e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b060e8.md) → [`00b061b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md) _ZN8firebase17version_registrar10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b061cc",
      "incomplete_value": false,
      "site": "00b061d0",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06104",
      "incomplete_value": false,
      "site": "00b06108",
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
      "definition_site": "00b061dc",
      "incomplete_value": true,
      "site": "00b061e8",
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
      "definition_site": "00b06114",
      "incomplete_value": true,
      "site": "00b06120",
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
      "00b061cc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b061dc",
      "DATA",
      [
        "storage",
        "010a0dc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b061cc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b061dc",
      "DATA",
      [
        "storage",
        "010a0e80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b060e8.md#insn-00b06108) · [`00b06104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b060e8.md#insn-00b06104) · [`00b06110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b060e8.md#insn-00b06110)
- 新版 [`00b061d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md#insn-00b061d0) · [`00b061cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md#insn-00b061cc) · [`00b061d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md#insn-00b061d8)

~~~diff
- 00b06108 ["INT_ADD", "register:40f0:8", ["const:b06108:8", "const:4:8"]]
- 00b06108 ["CALL", null, ["callee:00bde130:8"]]
+ 00b061d0 ["INT_ADD", "register:40f0:8", ["const:b061d0:8", "const:4:8"]]
+ 00b061d0 ["CALL", null, ["callee:00bde130:8"]]
- 00b06108 bytes de5f0394
+ 00b061d0 bytes d85f0394
- 00b06104 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b06104 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b06104 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b06104 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b061cc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b061cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b061cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b061cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b06104 bytes 00c81791
+ 00b061cc bytes 00fc1991
- 00b06110 ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00b06110 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b06110 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b06110 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b061d8 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00b061d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b061d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b061d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b06110 bytes 08013791
+ 00b061d8 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-965b0310854fe5006e172eb36720575a"></a>

### [`00b06124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md) → [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef10.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b062c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md) [`00b064b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b064b0.md) [`00b068bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bdefc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefc0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06578.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 80.95% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06234",
      "incomplete_value": true,
      "site": "00b06244",
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0616c",
      "incomplete_value": true,
      "site": "00b0617c",
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06238",
      "incomplete_value": true,
      "site": "00b06244",
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06170",
      "incomplete_value": true,
      "site": "00b0617c",
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
                "const:d58:8"
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
      "definition_site": "00b06270",
      "incomplete_value": true,
      "site": "00b0627c",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b06234",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06238",
      "READ",
      [
        "storage",
        "010a0d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b06234",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06238",
      "READ",
      [
        "storage",
        "010a0e18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0617c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md#insn-00b0617c) · [`00b061b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md#insn-00b061b4) · [`00b0615c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md#insn-00b0615c)
- 新版 [`00b06244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md#insn-00b06244) · [`00b0627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md#insn-00b0627c) · [`00b06224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md#insn-00b06224)

~~~diff
- 00b0617c ["INT_ADD", "register:40f0:8", ["const:b0617c:8", "const:4:8"]]
- 00b0617c ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b06244 ["INT_ADD", "register:40f0:8", ["const:b06244:8", "const:4:8"]]
+ 00b06244 ["CALL", null, ["callee:00bddcf0:8"]]
- 00b0617c bytes b15e0394
+ 00b06244 bytes ab5e0394
- 00b061b4 ["INT_ADD", "register:40f0:8", ["const:b061b4:8", "const:4:8"]]
- 00b061b4 ["CALL", null, ["callee:0047495c:8"]]
+ 00b0627c ["INT_ADD", "register:40f0:8", ["const:b0627c:8", "const:4:8"]]
+ 00b0627c ["CALL", null, ["callee:0047495c:8"]]
- 00b061b4 bytes eab9e597
+ 00b0627c bytes b8b9e597
- 00b0615c ["INT_ADD", "register:40f0:8", ["const:b0615c:8", "const:4:8"]]
- 00b0615c ["CALL", null, ["callee:00b06390:8"]]
+ 00b06224 ["INT_ADD", "register:40f0:8", ["const:b06224:8", "const:4:8"]]
+ 00b06224 ["CALL", null, ["callee:00b06390:8"]]
- 00b0615c bytes 5b000094
+ 00b06224 bytes 5b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908860d9df8f0179c8badfdb41ceffe5"></a>

### [`00b062c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md) → [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) FUN_00b06390

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b06124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md) [`00b06b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06b20.md) [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) [`00b080b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b080b4.md) · 呼出先 5件 [`00b068bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md) [`00bddf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf20.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md) [`00bded50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded50.md)
- 新版 呼出元 4件 [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) [`00b06be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md) [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) [`00b0817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md) · 呼出先 5件 [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) [`00bdee00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 83.61% / 新版 83.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b063ac",
      "incomplete_value": false,
      "site": "00b063ac",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b062e4",
      "incomplete_value": false,
      "site": "00b062e4",
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
            "const:dc8:8"
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
      "definition_site": "00b063f8",
      "incomplete_value": true,
      "site": "00b063f8",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06330",
      "incomplete_value": true,
      "site": "00b06330",
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
            "const:c90:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b06450",
      "incomplete_value": true,
      "site": "00b06450",
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
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06388",
      "incomplete_value": true,
      "site": "00b06388",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b063a4",
      "READ",
      [
        "storage",
        "010a0dc8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b063ac",
      "WRITE",
      [
        "storage",
        "010a0dc8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b063d0",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b063a4",
      "READ",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b063ac",
      "WRITE",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b063d0",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b062e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md#insn-00b062e4) · [`00b06328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md#insn-00b06328) · [`00b06330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md#insn-00b06330)
- 新版 [`00b063ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md#insn-00b063ac) · [`00b063f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md#insn-00b063f0) · [`00b063f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md#insn-00b063f8)

~~~diff
- 00b062e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
- 00b062e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b063ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e88:8"]]
+ 00b063ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b062e4 bytes a9ca0db9
+ 00b063ac bytes a98a0eb9
- 00b06328 ["INT_ADD", "register:40f0:8", ["const:b06328:8", "const:4:8"]]
- 00b06328 ["CALL", null, ["callee:00bde040:8"]]
+ 00b063f0 ["INT_ADD", "register:40f0:8", ["const:b063f0:8", "const:4:8"]]
+ 00b063f0 ["CALL", null, ["callee:00bde040:8"]]
- 00b06328 bytes 1a5f0394
+ 00b063f0 bytes 145f0394
- 00b06330 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c90:8"]]
- 00b06330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b063f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d50:8"]]
+ 00b063f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b06330 bytes a04a06f9
+ 00b063f8 bytes a0aa06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61da1eef713afa4487d0b6f515610d6d"></a>

### [`00b064b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b064b0.md) → [`00b06578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06578.md) FUN_00b06578

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b06124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md) [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 2件 [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 81.33% / 新版 79.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0668c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b066ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b067c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b065d8",
      "READ",
      [
        "storage",
        "010a0d60",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06674",
      "READ",
      [
        "storage",
        "010a0d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06710",
      "READ",
      [
        "storage",
        "010a0d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b065d8",
      "READ",
      [
        "storage",
        "010a0e20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06674",
      "READ",
      [
        "storage",
        "010a0e28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06710",
      "READ",
      [
        "storage",
        "010a0e30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0651c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b064b0.md#insn-00b0651c) · [`00b065b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b064b0.md#insn-00b065b8) · [`00b065c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b064b0.md#insn-00b065c4)
- 新版 [`00b065e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06578.md#insn-00b065e4) · [`00b06680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06578.md#insn-00b06680) · [`00b0668c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06578.md#insn-00b0668c)

~~~diff
- 00b0651c ["INT_ADD", "register:40f0:8", ["const:b0651c:8", "const:4:8"]]
- 00b0651c ["CALL", null, ["callee:0047495c:8"]]
+ 00b065e4 ["INT_ADD", "register:40f0:8", ["const:b065e4:8", "const:4:8"]]
+ 00b065e4 ["CALL", null, ["callee:0047495c:8"]]
- 00b0651c bytes 10b9e597
+ 00b065e4 bytes deb8e597
- 00b065b8 ["INT_ADD", "register:40f0:8", ["const:b065b8:8", "const:4:8"]]
- 00b065b8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b06680 ["INT_ADD", "register:40f0:8", ["const:b06680:8", "const:4:8"]]
+ 00b06680 ["CALL", null, ["callee:0047495c:8"]]
- 00b065b8 bytes e9b8e597
+ 00b06680 bytes b7b8e597
- 00b065c4 ["INT_ADD", "register:40f0:8", ["const:b065c4:8", "const:4:8"]]
- 00b065c4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b0668c ["INT_ADD", "register:40f0:8", ["const:b0668c:8", "const:4:8"]]
+ 00b0668c ["CALL", null, ["callee:00bde090:8"]]
- 00b065c4 bytes 875e0394
+ 00b0668c bytes 815e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6994f7459928d99a6708eccf50fb974"></a>

### [`00b068bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md) → [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) FUN_00b06984

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00b06124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06124.md) [`00b062c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md) [`00b06a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06a6c.md) [`00b06b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06b20.md) [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) · 呼出先 4件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde050.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bded70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded70.md)
- 新版 呼出元 6件 [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md) [`00b06be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md) [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 4件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdee20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee20.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.04% / 新版 28.04%

CFGの説明率　旧版 23.53% / 新版 24.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b069b8",
      "incomplete_value": true,
      "site": "00b069b8",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b068f0",
      "incomplete_value": true,
      "site": "00b068f0",
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
            "const:dc8:8"
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
      "site": "00b06930"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06950"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b06998",
      "READ",
      [
        "storage",
        "010a0dc8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b069a8",
      "PARAM",
      [
        "storage",
        "002ab043",
        null,
        "string"
      ]
    ],
    [
      "00b069b0",
      "READ",
      [
        "storage",
        "010a0dc8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b06998",
      "READ",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b069a8",
      "PARAM",
      [
        "storage",
        "002ab049",
        null,
        "string"
      ]
    ],
    [
      "00b069b0",
      "READ",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b068e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md#insn-00b068e0) · [`00b068f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md#insn-00b068f0) · [`00b0691c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md#insn-00b0691c)
- 新版 [`00b069a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md#insn-00b069a8) · [`00b069b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md#insn-00b069b8)

~~~diff
- 00b068e0 ["COPY", "tmp:0:8", ["const:43:8"]]
- 00b068e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b068e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b068e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b069a8 ["COPY", "tmp:0:8", ["const:49:8"]]
+ 00b069a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b069a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b069a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b068e0 bytes 000c0191
+ 00b069a8 bytes 00240191
- 00b068f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc8:8"]]
- 00b068f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b069b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e88:8"]]
+ 00b069b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b068f0 bytes 88ca0db9
+ 00b069b8 bytes 888a0eb9
- 00b0691c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b0691c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b0691c bytes c8000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad5a28c38098f9c7f0716be4571aded8"></a>

### [`00b06b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06b20.md) → [`00b06be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md) _ZN8firebase3App6CreateEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdda00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda00.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00847/0084795c.md) [`00b062c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md) [`00b068bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b068bc.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md)
- 新版 呼出元 1件 [`00bddab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddab0.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

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
      "definition_site": "00b06c64",
      "incomplete_value": true,
      "site": "00b06c68",
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
      "definition_site": "00b06b9c",
      "incomplete_value": true,
      "site": "00b06ba0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06c80",
      "incomplete_value": false,
      "site": "00b06c84",
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
            "const:6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06bb8",
      "incomplete_value": false,
      "site": "00b06bbc",
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
            "const:74:8"
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
      "00b06c54",
      "READ",
      [
        "storage",
        "00c1b878",
        null,
        "pointer"
      ]
    ],
    [
      "00b06c64",
      "READ",
      [
        "storage",
        "00c105e0",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b06c64",
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
      "00b06c54",
      "READ",
      [
        "storage",
        "00c1b928",
        null,
        "pointer"
      ]
    ],
    [
      "00b06c64",
      "READ",
      [
        "storage",
        "00c10690",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b06c64",
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

- 旧版 [`00b06ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06b20.md#insn-00b06ba0) · [`00b06bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06b20.md#insn-00b06bbc) · [`00b06b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06b20.md#insn-00b06b48)
- 新版 [`00b06c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md#insn-00b06c68) · [`00b06c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md#insn-00b06c84) · [`00b06c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md#insn-00b06c10)

~~~diff
- 00b06ba0 ["INT_ADD", "register:40f0:8", ["const:b06ba0:8", "const:4:8"]]
- 00b06ba0 ["CALL", null, ["callee:00bdefd0:8"]]
+ 00b06c68 ["INT_ADD", "register:40f0:8", ["const:b06c68:8", "const:4:8"]]
+ 00b06c68 ["CALL", null, ["callee:00bdefd0:8"]]
- 00b06ba0 bytes e0600394
+ 00b06c68 bytes da600394
- 00b06bbc ["INT_ADD", "register:40f0:8", ["const:b06bbc:8", "const:4:8"]]
- 00b06bbc ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b06c84 ["INT_ADD", "register:40f0:8", ["const:b06c84:8", "const:4:8"]]
+ 00b06c84 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b06bbc bytes 615c0394
+ 00b06c84 bytes 5b5c0394
- 00b06b48 ["INT_ADD", "register:40f0:8", ["const:b06b48:8", "const:4:8"]]
- 00b06b48 ["CALL", null, ["callee:00b06390:8"]]
+ 00b06c10 ["INT_ADD", "register:40f0:8", ["const:b06c10:8", "const:4:8"]]
+ 00b06c10 ["CALL", null, ["callee:00b06390:8"]]
- 00b06b48 bytes e0fdff97
+ 00b06c10 bytes e0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f644a737561cd74191cc7d5294c798a"></a>

### [`00b06c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md) → [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef20.md) · 呼出先 28件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`0084795c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00847/0084795c.md) [`00b062c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b062c8.md)
- 新版 呼出元 1件 [`00bdefd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefd0.md) · 呼出先 28件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.16% / 新版 84.16%

CFGの説明率　旧版 51.47% / 新版 50.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 32件, `store_condition` 5件, `store_destination` 3件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 25件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 17件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06f28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b06d44",
      "READ",
      [
        "storage",
        "00c1b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b06d4c",
      "PARAM",
      [
        "storage",
        "002ac1fc",
        null,
        "string"
      ]
    ],
    [
      "00b06d54",
      "READ",
      [
        "storage",
        "00c246a8",
        "_ZN8firebase22kFirebaseVersionStringE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b06d44",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ],
    [
      "00b06d4c",
      "PARAM",
      [
        "storage",
        "002ac1f3",
        null,
        "string"
      ]
    ],
    [
      "00b06d54",
      "READ",
      [
        "storage",
        "00c24758",
        "_ZN8firebase22kFirebaseVersionStringE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md#insn-00b06f24) · [`00b06f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md#insn-00b06f28) · [`00b06fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b06/00b06c18.md#insn-00b06fd0)
- 新版 [`00b076ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md#insn-00b076ac)

~~~diff
- 00b06f24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00b06f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b06f24 bytes 0a0900f9
- 00b06f28 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b06f28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b06f28 bytes 0001803d
- 00b06fd0 ["COPY", "tmp:0:8", ["const:17:8"]]
- 00b06fd0 ["INT_LESSEQUAL", "register:105:1", ["tmp:0:8", "register:40c0:8"]]
- 00b06fd0 ["INT_SBORROW", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00b06fd0 ["INT_SUB", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00b076ac ["COPY", "tmp:0:8", ["const:17:8"]]
+ 00b076ac ["INT_LESSEQUAL", "register:105:1", ["tmp:0:8", "register:40b8:8"]]
+ 00b076ac ["INT_SBORROW", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00b076ac ["INT_SUB", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00b06fd0 bytes 1f5f00f1
+ 00b076ac bytes ff5e00f1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8b2be0969f615f86b74e21dcd57916a"></a>

### [`00b07eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07eb0.md) → [`00b07f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b07/00b07f78.md) _ZNK8firebase3App7java_vmEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00bdef50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef50.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdf000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf000.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-e7f6065872130401763f5d9d4dccfe64"></a>

### [`00b07ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07ebc.md) → [`00b07f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b07/00b07f84.md) _ZN8firebase3App15RegisterLibraryEPKcS2_Pv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde830.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde7a0.md)
- 新版 呼出元 1件 [`00bde8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8e0.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde850.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07ec0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b07ebc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b07ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b07ec4",
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
      "00b07f84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b07f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b07f8c",
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

- 旧版 [`00b07ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07ebc.md#insn-00b07ebc) · [`00b07ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07ebc.md#insn-00b07ec0) · [`00b07ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07ebc.md#insn-00b07ec4)

~~~diff
- 00b07ebc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b07ebc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b07ebc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b07ebc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b07ebc bytes f85fbca9
- 00b07ec0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b07ec0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b07ec0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b07ec0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b07ec0 bytes f65701a9
- 00b07ec4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b07ec4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b07ec4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b07ec4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b07ec4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba428e3e85a12f814ab1063095378555"></a>

### [`00b07fd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07fd0.md) → [`00b08098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md) _ZN8firebase3App31SetDataCollectionDefaultEnabledEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde440.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b080b0",
      "incomplete_value": true,
      "site": "00b080b0",
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
      "definition_site": "00b07fe8",
      "incomplete_value": true,
      "site": "00b07fe8",
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
      "definition_site": "00b080cc",
      "incomplete_value": true,
      "site": "00b080dc",
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08004",
      "incomplete_value": true,
      "site": "00b08014",
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
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b080ac",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b080cc",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b08100",
      "PARAM",
      [
        "storage",
        "002ac21c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b080ac",
      "READ",
      [
        "storage",
        "010a0da0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b080cc",
      "READ",
      [
        "storage",
        "010a0da0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b08100",
      "PARAM",
      [
        "storage",
        "002ac213",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07fd0.md#insn-00b08014) · [`00b07fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07fd0.md#insn-00b07fe4) · [`00b07ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b07/00b07fd0.md#insn-00b07ffc)
- 新版 [`00b080dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md#insn-00b080dc) · [`00b080ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md#insn-00b080ac) · [`00b080c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md#insn-00b080c4)

~~~diff
- 00b08014 ["INT_ADD", "register:40f0:8", ["const:b08014:8", "const:4:8"]]
- 00b08014 ["CALL", null, ["callee:00551e14:8"]]
+ 00b080dc ["INT_ADD", "register:40f0:8", ["const:b080dc:8", "const:4:8"]]
+ 00b080dc ["CALL", null, ["callee:00551e14:8"]]
- 00b08014 bytes 8027e997
+ 00b080dc bytes 4e27e997
- 00b07fe4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ce0:8"]]
- 00b07fe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b080ac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:da0:8"]]
+ 00b080ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b07fe4 bytes c87246f9
+ 00b080ac bytes c8d246f9
- 00b07ffc ["INT_ADD", "register:40f0:8", ["const:b07ffc:8", "const:4:8"]]
- 00b07ffc ["CALL", null, ["callee:00bde4f0:8"]]
+ 00b080c4 ["INT_ADD", "register:40f0:8", ["const:b080c4:8", "const:4:8"]]
+ 00b080c4 ["CALL", null, ["callee:00bde4f0:8"]]
- 00b07ffc bytes 11590394
+ 00b080c4 bytes 0b590394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e225b491907f35eaa9a12cc822c8d1d"></a>

### [`00b08044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08044.md) → [`00b0810c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md) _ZNK8firebase3App30IsDataCollectionDefaultEnabledEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde440.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b08120",
      "incomplete_value": true,
      "site": "00b08120",
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
      "definition_site": "00b08058",
      "incomplete_value": true,
      "site": "00b08058",
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
      "definition_site": "00b08138",
      "incomplete_value": true,
      "site": "00b08144",
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08070",
      "incomplete_value": true,
      "site": "00b0807c",
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0811c",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b08138",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0811c",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b08138",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0807c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08044.md#insn-00b0807c) · [`00b08054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08044.md#insn-00b08054) · [`00b08068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08044.md#insn-00b08068)
- 新版 [`00b08144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md#insn-00b08144) · [`00b0811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md#insn-00b0811c) · [`00b08130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md#insn-00b08130)

~~~diff
- 00b0807c ["INT_ADD", "register:40f0:8", ["const:b0807c:8", "const:4:8"]]
- 00b0807c ["CALL", null, ["callee:00474b70:8"]]
+ 00b08144 ["INT_ADD", "register:40f0:8", ["const:b08144:8", "const:4:8"]]
+ 00b08144 ["CALL", null, ["callee:00474b70:8"]]
- 00b0807c bytes bdb2e597
+ 00b08144 bytes 8bb2e597
- 00b08054 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
- 00b08054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0811c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
+ 00b0811c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b08054 bytes 886e46f9
+ 00b0811c bytes 88ce46f9
- 00b08068 ["INT_ADD", "register:40f0:8", ["const:b08068:8", "const:4:8"]]
- 00b08068 ["CALL", null, ["callee:00bde4f0:8"]]
+ 00b08130 ["INT_ADD", "register:40f0:8", ["const:b08130:8", "const:4:8"]]
+ 00b08130 ["CALL", null, ["callee:00bde4f0:8"]]
- 00b08068 bytes f6580394
+ 00b08130 bytes f0580394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ca4774a664adce03d29ec3205030182"></a>

### [`00b08654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08654.md) → [`00b0871c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md) _ZN8firebase10AppOptions18LoadFromJsonConfigEPKcPS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0084795c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00847/0084795c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b08798",
      "incomplete_value": true,
      "site": "00b08798",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:7b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b086d0",
      "incomplete_value": true,
      "site": "00b086d0",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b08768",
      "incomplete_value": true,
      "site": "00b087a0",
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
              [
                "leaf",
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b086a0",
      "incomplete_value": true,
      "site": "00b086d8",
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
              [
                "leaf",
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b08830",
      "incomplete_value": true,
      "site": "00b08850",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08768",
      "incomplete_value": true,
      "site": "00b08788",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:2f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b08764",
      "READ",
      [
        "storage",
        "00298725",
        null,
        "string"
      ]
    ],
    [
      "00b08768",
      "READ",
      [
        "storage",
        "0029872c",
        null,
        "string"
      ]
    ],
    [
      "00b08830",
      "READ",
      [
        "storage",
        "002ac2f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b08764",
      "READ",
      [
        "storage",
        "002987b2",
        null,
        "string"
      ]
    ],
    [
      "00b08768",
      "READ",
      [
        "storage",
        "002987b9",
        null,
        "string"
      ]
    ],
    [
      "00b08830",
      "READ",
      [
        "storage",
        "002ac2e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b087b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08654.md#insn-00b087b8) · [`00b087c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08654.md#insn-00b087c8) · [`00b08860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08654.md#insn-00b08860)
- 新版 [`00b08880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md#insn-00b08880) · [`00b08890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md#insn-00b08890) · [`00b08928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md#insn-00b08928)

~~~diff
- 00b087b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:840:8"]]
- 00b087b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b08880 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8f0:8"]]
+ 00b08880 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b087b8 bytes 212044f9
+ 00b08880 bytes 217844f9
- 00b087c8 ["INT_ADD", "register:40f0:8", ["const:b087c8:8", "const:4:8"]]
- 00b087c8 ["CALL", null, ["callee:00bdf010:8"]]
+ 00b08890 ["INT_ADD", "register:40f0:8", ["const:b08890:8", "const:4:8"]]
+ 00b08890 ["CALL", null, ["callee:00bdf010:8"]]
- 00b087c8 bytes e6590394
+ 00b08890 bytes e0590394
- 00b08860 ["INT_ADD", "register:40f0:8", ["const:b08860:8", "const:4:8"]]
- 00b08860 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b08928 ["INT_ADD", "register:40f0:8", ["const:b08928:8", "const:4:8"]]
+ 00b08928 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b08860 bytes 38550394
+ 00b08928 bytes 32550394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbbcc0d366370251ee4a6818f1d54a24"></a>

### [`00b08f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08f40.md) → [`00b09008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b09/00b09008.md) _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde970.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00613/00613984.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdea20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea20.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/00613984.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.06% / 新版 28.06%

CFGの説明率　旧版 3.56% / 新版 3.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_branch_alignment` 52件, `unresolved_call_alignment` 74件, `unresolved_store_alignment` 380件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b09208",
      "incomplete_value": true,
      "site": "00b09208",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b09140",
      "incomplete_value": true,
      "site": "00b09140",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:ecb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 89,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b09168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b09168"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b091dc",
      "READ",
      [
        "storage",
        "0029eecb",
        null,
        "string"
      ]
    ],
    [
      "00b09218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b091c0"
      ]
    ],
    [
      "unmatched:00b0915c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdaff0"
      ]
    ]
  ],
  "added": [
    [
      "00b091dc",
      "READ",
      [
        "storage",
        "0029ef58",
        null,
        "string"
      ]
    ],
    [
      "00b09218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b09288"
      ]
    ],
    [
      "00b09224",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdaff0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b090d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08f40.md#insn-00b090d4) · [`00b09168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08f40.md#insn-00b09168) · [`00b0916c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b08/00b08f40.md#insn-00b0916c)
- 新版 [`00b0919c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b09/00b09008.md#insn-00b0919c)

~~~diff
- 00b090d4 ["INT_ADD", "register:40f0:8", ["const:b090d4:8", "const:4:8"]]
- 00b090d4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b0919c ["INT_ADD", "register:40f0:8", ["const:b0919c:8", "const:4:8"]]
+ 00b0919c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b090d4 bytes 9b470394
+ 00b0919c bytes 95470394
- 00b09168 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b09168 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b09168 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b09168 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b09168 bytes ff7f01a9
- 00b0916c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b0916c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b0916c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b0916c bytes ff0700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13df6ac8c9624458685f5c6a3b9b7f0f"></a>

### [`00b0a3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a3b0.md) → [`00b0a478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a478.md) _ZN11flatbuffers6ParserD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde980.md) · 呼出先 14件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`007101c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00710/007101c4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8f0.md) [`00bde910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde910.md)
- 新版 呼出元 1件 [`00bdea30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea30.md) · 呼出先 14件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`007101c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/007101c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bde9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.68% / 新版 96.68%

CFGの説明率　旧版 68.97% / 新版 68.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a470"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a4ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a684"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0a470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0a554"
      ]
    ],
    [
      "00b0a544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0a468"
      ]
    ],
    [
      "00b0a550",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0a468"
      ]
    ]
  ],
  "added": [
    [
      "00b0a538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0a554"
      ]
    ],
    [
      "00b0a544",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0a530"
      ]
    ],
    [
      "00b0a550",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0a530"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0a470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a3b0.md#insn-00b0a470) · [`00b0a4ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a3b0.md#insn-00b0a4ec) · [`00b0a534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a3b0.md#insn-00b0a534)
- 新版 [`00b0a5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a478.md#insn-00b0a5fc)

~~~diff
- 00b0a470 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00b0a470 bytes e0000054
- 00b0a4ec ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b0a4ec ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0a4ec ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0a4ec ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b0a4ec bytes 89ff0736
- 00b0a534 ["INT_ADD", "register:40f0:8", ["const:b0a534:8", "const:4:8"]]
- 00b0a534 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0a5fc ["INT_ADD", "register:40f0:8", ["const:b0a5fc:8", "const:4:8"]]
+ 00b0a5fc ["CALL", null, ["callee:00bdb010:8"]]
- 00b0a534 bytes 8b420394
+ 00b0a5fc bytes 85420394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e624e6bb47890873e75ae6c50afb935a"></a>

### [`00b0a6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a6fc.md) → [`00b0a7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md) _ZN11flatbuffers10IDLOptionsD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bde910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde910.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bde9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9c0.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 84.13% / 新版 85.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0a8f4",
      "incomplete_value": true,
      "site": "00b0a8f8",
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
                "register:4098:8"
              ],
              [
                "leaf",
                "const:d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 7,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0a830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a6fc.md#insn-00b0a830) · [`00b0a714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a6fc.md#insn-00b0a714) · [`00b0a71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a6fc.md#insn-00b0a71c)
- 新版 [`00b0a8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md#insn-00b0a8f8) · [`00b0a7dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md#insn-00b0a7dc) · [`00b0a7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a7c4.md#insn-00b0a7e4)

~~~diff
- 00b0a830 ["INT_ADD", "register:40f0:8", ["const:b0a830:8", "const:4:8"]]
- 00b0a830 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0a8f8 ["INT_ADD", "register:40f0:8", ["const:b0a8f8:8", "const:4:8"]]
+ 00b0a8f8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0a830 bytes cc410394
+ 00b0a8f8 bytes c6410394
- 00b0a714 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0a714 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0a714 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0a714 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b0a7dc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b0a7dc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b0a7dc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b0a7dc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0a714 bytes a8030037
+ 00b0a7dc bytes a8030037
- 00b0a71c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b0a71c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0a71c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0a71c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b0a7e4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b0a7e4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b0a7e4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b0a7e4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0a71c bytes e8030037
+ 00b0a7e4 bytes e8030037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f759b3521cec0deca4bcd2f15d2d4d8"></a>

### [`00b0a8a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a8a0.md) → [`00b0a968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a968.md) _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde990.md) · 呼出先 5件 [`0084795c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00847/0084795c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bdef10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef10.md)
- 新版 呼出元 1件 [`00bdea40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea40.md) · 呼出先 5件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bdefc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.21% / 新版 90.21%

CFGの説明率　旧版 17.86% / 新版 17.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a8c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b0a98c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0a900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0a8c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0a900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0ab6c"
      ]
    ],
    [
      "unmatched:00b0a938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0a9b0"
      ]
    ]
  ],
  "added": [
    [
      "00b0a98c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b0a9c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0ab6c"
      ]
    ],
    [
      "00b0aa00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0a9b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0a8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a8a0.md#insn-00b0a8c4) · [`00b0a8e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a8a0.md#insn-00b0a8e4) · [`00b0a900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0a/00b0a8a0.md#insn-00b0a900)
- 新版 [`00b0a9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a968.md#insn-00b0a9ac)

~~~diff
- 00b0a8c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b0a8c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b0a8c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b0a8c4 bytes a8831df8
- 00b0a8e4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b0a8e4 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
+ 00b0a9ac ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b0a9ac ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b0a8e4 bytes 890300b4
+ 00b0a9ac bytes 890300b4
- 00b0a900 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b0a900 ["CBRANCH", null, ["local:b49:8", "tmp:0:1"]]
- 00b0a900 bytes 280d00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08cae415485941539c9d0dc096b6130c"></a>

### [`00b0bc38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0b/00b0bc38.md) → [`00b0bd00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0bd00.md) _ZNK8firebase3fbs17AndroidClientInfo6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea20.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdead0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdead0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 44.93% / 新版 44.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0bd1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0bd44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0bd7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0bd1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0bdf4"
      ]
    ],
    [
      "unmatched:00b0bd44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0bd90"
      ]
    ],
    [
      "unmatched:00b0bd7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0be54"
      ]
    ]
  ],
  "added": [
    [
      "00b0bde4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0bdf4"
      ]
    ],
    [
      "00b0be0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0bd90"
      ]
    ],
    [
      "00b0be44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0be54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0bcb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0b/00b0bc38.md#insn-00b0bcb4) · [`00b0bd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0b/00b0bc38.md#insn-00b0bd1c) · [`00b0bd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0b/00b0bc38.md#insn-00b0bd44)
- 新版 [`00b0bd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0b/00b0bd00.md#insn-00b0bd7c)

~~~diff
- 00b0bcb4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b0bcb4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00b0bd7c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b0bd7c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b0bcb4 bytes a3000054
+ 00b0bd7c bytes a3000054
- 00b0bd1c ["CBRANCH", null, ["local:b23:8", "register:102:1"]]
- 00b0bd1c bytes 82000054
- 00b0bd44 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b0bd44 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b0bd44 bytes 23fcff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb11c6909e4b218d06285edf2540f122"></a>

### [`00b0c2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c2c8.md) → [`00b0c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c390.md) _ZNK8firebase3fbs6ApiKey6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea30.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeae0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 82.08% / 新版 82.08%

CFGの説明率　旧版 36.49% / 新版 36.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0c2d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0c2ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0c384"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0c2d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0c3a8"
      ]
    ],
    [
      "unmatched:00b0c2ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0c530"
      ]
    ],
    [
      "00b0c4e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0c530"
      ]
    ]
  ],
  "added": [
    [
      "00b0c39c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0c3a8"
      ]
    ],
    [
      "00b0c3b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0c530"
      ]
    ],
    [
      "00b0c3c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0c530"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0c2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c2c8.md#insn-00b0c2d4) · [`00b0c2ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c2c8.md#insn-00b0c2ec) · [`00b0c344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c2c8.md#insn-00b0c344)
- 新版 [`00b0c40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0c390.md#insn-00b0c40c)

~~~diff
- 00b0c2d4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b0c2d4 bytes 60000054
- 00b0c2ec ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b0c2ec ["CBRANCH", null, ["local:b43:8", "tmp:0:1"]]
- 00b0c2ec bytes e30b0054
- 00b0c344 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b0c344 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00b0c40c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b0c40c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b0c344 bytes a3000054
+ 00b0c40c bytes a3000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45d425d8e2e7b96af0f18390a234bb41"></a>

### [`00b0c94c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c94c.md) → [`00b0ca14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0ca14.md) _ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea10.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bdeac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeac0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 67.65% / 新版 68.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0c97c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ca30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ca90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0c97c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cbb4"
      ]
    ],
    [
      "unmatched:00b0ca30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cb08"
      ]
    ],
    [
      "unmatched:00b0ca90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cb68"
      ]
    ]
  ],
  "added": [
    [
      "00b0ca44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cbb4"
      ]
    ],
    [
      "00b0caf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cb08"
      ]
    ],
    [
      "00b0cb58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cb68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0c97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c94c.md#insn-00b0c97c) · [`00b0c9c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c94c.md#insn-00b0c9c8) · [`00b0ca30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0c94c.md#insn-00b0ca30)
- 新版 [`00b0ca90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0ca14.md#insn-00b0ca90)

~~~diff
- 00b0c97c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b0c97c ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00b0c97c bytes 830b0054
- 00b0c9c8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b0c9c8 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b0ca90 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b0ca90 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b0c9c8 bytes a3000054
+ 00b0ca90 bytes a3000054
- 00b0ca30 ["CBRANCH", null, ["local:b22:8", "register:102:1"]]
- 00b0ca30 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c84b996e31f6db5c896c181e2811a959"></a>

### [`00b0caf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0caf4.md) → [`00b0cbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cbbc.md) _ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde9a0.md) · 呼出先 1件 [`00bdea00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea00.md)
- 新版 呼出元 1件 [`00bdea50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea50.md) · 呼出先 1件 [`00bdeab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 52.40% / 新版 52.40%

CFGの説明率　旧版 17.69% / 新版 17.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 32件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0caf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0caf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0caf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0caf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0caf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0cb34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cc60"
      ]
    ]
  ],
  "added": [
    [
      "00b0cbbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b0cbc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b0cbfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0cc60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0caf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0caf4.md#insn-00b0caf4) · [`00b0caf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0caf4.md#insn-00b0caf8) · [`00b0cb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0caf4.md#insn-00b0cb18)
- 新版 [`00b0cbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cbbc.md#insn-00b0cbe0)

~~~diff
- 00b0caf4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b0caf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b0caf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0caf4 bytes f30f1ef8
- 00b0caf8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0caf8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0caf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0caf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0caf8 bytes fd7b01a9
- 00b0cb18 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b0cb18 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b0cbe0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b0cbe0 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b0cb18 bytes e8030035
+ 00b0cbe0 bytes e8030035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd42b9a0fd8e42aec2fe813735e13ae9"></a>

### [`00b0cec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0cec0.md) → [`00b0cf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md) _ZN11flatbuffers11SymbolTableINS_10ServiceDefEED2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde920.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8f0.md) [`00bdea80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea80.md) [`00bdead0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdead0.md)
- 新版 呼出元 1件 [`00bde9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9d0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bdeb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb30.md) [`00bdeb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 53.57% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0cee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b0cfa8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0cee8",
      "incomplete_value": true,
      "site": "00b0cef0",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00b0cee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0d004"
      ]
    ]
  ],
  "added": [
    [
      "00b0cfa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0d004"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0cec0.md#insn-00b0cee0) · [`00b0cef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0cec0.md#insn-00b0cef0)
- 新版 [`00b0cfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md#insn-00b0cfb8) · [`00b0cfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0c/00b0cf88.md#insn-00b0cfa8)

~~~diff
- 00b0cee0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b0cee0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b0cee0 bytes e1020054
- 00b0cef0 ["INT_ADD", "register:40f0:8", ["const:b0cef0:8", "const:4:8"]]
- 00b0cef0 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0cfb8 ["INT_ADD", "register:40f0:8", ["const:b0cfb8:8", "const:4:8"]]
+ 00b0cfb8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0cef0 bytes 1c380394
+ 00b0cfb8 bytes 16380394
+ 00b0cfa8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b0cfa8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b0cfa8 bytes e1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5049bcc9f6c9e8e224404dd421ff2c"></a>

### [`00b0d2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d2d4.md) → [`00b0d39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeaa0.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdeaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeaa0.md)
- 新版 呼出元 1件 [`00bdeb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb50.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d2d4.md#insn-00b0d2d4) · [`00b0d2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d2d4.md#insn-00b0d2f0) · [`00b0d2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d2d4.md#insn-00b0d2fc)
- 新版 [`00b0d39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md#insn-00b0d39c) · [`00b0d3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md#insn-00b0d3b8) · [`00b0d3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d39c.md#insn-00b0d3c4)

~~~diff
- 00b0d2d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0d2d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b0d39c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b0d39c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b0d2d4 bytes 610200b4
+ 00b0d39c bytes 610200b4
- 00b0d2f0 ["INT_ADD", "register:40f0:8", ["const:b0d2f0:8", "const:4:8"]]
- 00b0d2f0 ["CALL", null, ["callee:00bdeb50:8"]]
+ 00b0d3b8 ["INT_ADD", "register:40f0:8", ["const:b0d3b8:8", "const:4:8"]]
+ 00b0d3b8 ["CALL", null, ["callee:00bdeb50:8"]]
- 00b0d2f0 bytes ec450394
+ 00b0d3b8 bytes e6450394
- 00b0d2fc ["INT_ADD", "register:40f0:8", ["const:b0d2fc:8", "const:4:8"]]
- 00b0d2fc ["CALL", null, ["callee:00bdeb50:8"]]
+ 00b0d3c4 ["INT_ADD", "register:40f0:8", ["const:b0d3c4:8", "const:4:8"]]
+ 00b0d3c4 ["CALL", null, ["callee:00bdeb50:8"]]
- 00b0d2fc bytes e9450394
+ 00b0d3c4 bytes e3450394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-291758c92c93a218e96784b8fb508376"></a>

### [`00b0d4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4f8.md) → [`00b0d5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bde940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde940.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8f0.md) [`00bdeae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeae0.md)
- 新版 呼出元 1件 [`00bde9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9f0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde9a0.md) [`00bdeb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.50% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0d570",
      "incomplete_value": true,
      "site": "00b0d574",
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4f8.md#insn-00b0d574) · [`00b0d524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4f8.md#insn-00b0d524) · [`00b0d544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d4f8.md#insn-00b0d544)
- 新版 [`00b0d63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md#insn-00b0d63c) · [`00b0d5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md#insn-00b0d5ec) · [`00b0d60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d5c0.md#insn-00b0d60c)

~~~diff
- 00b0d574 ["INT_ADD", "register:40f0:8", ["const:b0d574:8", "const:4:8"]]
- 00b0d574 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d63c ["INT_ADD", "register:40f0:8", ["const:b0d63c:8", "const:4:8"]]
+ 00b0d63c ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d574 bytes 7b360394
+ 00b0d63c bytes 75360394
- 00b0d524 ["INT_ADD", "register:40f0:8", ["const:b0d524:8", "const:4:8"]]
- 00b0d524 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0d5ec ["INT_ADD", "register:40f0:8", ["const:b0d5ec:8", "const:4:8"]]
+ 00b0d5ec ["CALL", null, ["callee:00bdb010:8"]]
- 00b0d524 bytes 8f360394
+ 00b0d5ec bytes 89360394
- 00b0d544 ["INT_ADD", "register:40f0:8", ["const:b0d544:8", "const:4:8"]]
- 00b0d544 ["CALL", null, ["callee:00bde9a0:8"]]
+ 00b0d60c ["INT_ADD", "register:40f0:8", ["const:b0d60c:8", "const:4:8"]]
+ 00b0d60c ["CALL", null, ["callee:00bde9a0:8"]]
- 00b0d544 bytes eb440394
+ 00b0d60c bytes e5440394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d44891a896c0bc7a17cc6b070809d2d"></a>

### [`00b0d628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d628.md) → [`00b0d6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdea90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea90.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdea90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdea90.md)
- 新版 呼出元 1件 [`00bdeb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb40.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdeb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeb40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0d628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d628.md#insn-00b0d628) · [`00b0d644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d628.md#insn-00b0d644) · [`00b0d650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d628.md#insn-00b0d650)
- 新版 [`00b0d6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md#insn-00b0d6f0) · [`00b0d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md#insn-00b0d70c) · [`00b0d718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d6f0.md#insn-00b0d718)

~~~diff
- 00b0d628 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b0d628 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b0d6f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b0d6f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b0d628 bytes 610200b4
+ 00b0d6f0 bytes 610200b4
- 00b0d644 ["INT_ADD", "register:40f0:8", ["const:b0d644:8", "const:4:8"]]
- 00b0d644 ["CALL", null, ["callee:00bdeb40:8"]]
+ 00b0d70c ["INT_ADD", "register:40f0:8", ["const:b0d70c:8", "const:4:8"]]
+ 00b0d70c ["CALL", null, ["callee:00bdeb40:8"]]
- 00b0d644 bytes 13450394
+ 00b0d70c bytes 0d450394
- 00b0d650 ["INT_ADD", "register:40f0:8", ["const:b0d650:8", "const:4:8"]]
- 00b0d650 ["CALL", null, ["callee:00bdeb40:8"]]
+ 00b0d718 ["INT_ADD", "register:40f0:8", ["const:b0d718:8", "const:4:8"]]
+ 00b0d718 ["CALL", null, ["callee:00bdeb40:8"]]
- 00b0d650 bytes 10450394
+ 00b0d718 bytes 0a450394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd93f3ef551a858d2dbf112083da656e"></a>

### [`00b0d678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d678.md) → [`00b0d740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md) _ZN20google_play_services10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded50.md) · 呼出先 17件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 1件 [`00bdee00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee00.md) · 呼出先 17件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.13% / 新版 74.13%

CFGの説明率　旧版 37.88% / 新版 36.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 14件, `store_condition` 3件, `store_destination` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0d780",
      "incomplete_value": false,
      "site": "00b0d780",
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
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d6b8",
      "incomplete_value": false,
      "site": "00b0d6b8",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0d7d0",
      "incomplete_value": true,
      "site": "00b0d7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d708",
      "incomplete_value": true,
      "site": "00b0d708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:dd8:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0d850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0d774",
      "READ",
      [
        "storage",
        "010a0dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0d778",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0d780",
      "WRITE",
      [
        "storage",
        "010a0dd0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d774",
      "READ",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0d778",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0d780",
      "WRITE",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d678.md#insn-00b0d6b8) · [`00b0d708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d678.md#insn-00b0d708) · [`00b0d788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0d678.md#insn-00b0d788)
- 新版 [`00b0d780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md#insn-00b0d780) · [`00b0d7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md#insn-00b0d7d0) · [`00b0d850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md#insn-00b0d850)

~~~diff
- 00b0d6b8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:dd0:8"]]
- 00b0d6b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b0d780 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e90:8"]]
+ 00b0d780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b0d6b8 bytes 08d30db9
+ 00b0d780 bytes 08930eb9
- 00b0d708 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:dd8:8"]]
- 00b0d708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00b0d7d0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e98:8"]]
+ 00b0d7d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b0d708 bytes 35ef06f9
+ 00b0d7d0 bytes 354f07f9
- 00b0d788 ["INT_ADD", "register:40f0:8", ["const:b0d788:8", "const:4:8"]]
- 00b0d788 ["CALL", null, ["callee:00bde4d0:8"]]
+ 00b0d850 ["INT_ADD", "register:40f0:8", ["const:b0d850:8", "const:4:8"]]
+ 00b0d850 ["CALL", null, ["callee:00bde4d0:8"]]
- 00b0d788 bytes 26430394
+ 00b0d850 bytes 20430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c39a831376b08e4171498220fd4be13"></a>

### [`00b0da84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0da84.md) → [`00b0db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md) _ZN20google_play_services9TerminateEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded70.md) · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md) [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00bdee20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee20.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.75% / 新版 65.75%

CFGの説明率　旧版 39.13% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0db6c",
      "incomplete_value": true,
      "site": "00b0db6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:e90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0daa4",
      "incomplete_value": true,
      "site": "00b0daa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "leaf",
            "const:dd0:8"
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
    "new": null,
    "old": {
      "site": "00b0db08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0db30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0db60",
      "READ",
      [
        "storage",
        "010a0dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0db6c",
      "WRITE",
      [
        "storage",
        "010a0dd0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0db78",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0db60",
      "READ",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0db6c",
      "WRITE",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0db78",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0da98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0da84.md#insn-00b0da98) · [`00b0daa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0da84.md#insn-00b0daa4) · [`00b0dab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0da84.md#insn-00b0dab4)
- 新版 [`00b0db60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md#insn-00b0db60) · [`00b0db6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md#insn-00b0db6c) · [`00b0db7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md#insn-00b0db7c)

~~~diff
- 00b0da98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00b0da98 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b0da98 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00b0db60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 00b0db60 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b0db60 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00b0da98 bytes 09d14db9
+ 00b0db60 bytes 09914eb9
- 00b0daa4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 00b0daa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b0db6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 00b0db6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b0daa4 bytes 09d10db9
+ 00b0db6c bytes 09910eb9
- 00b0dab4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b0dab4 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b0db7c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b0db7c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b0dab4 bytes 740600b4
+ 00b0db7c bytes 740600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-297f52fd1766b1046b3200bbc4fd1fbd"></a>

### [`00b0dba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dba8.md) → [`00b0dc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef70.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bded50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded50.md)
- 新版 呼出元 1件 [`00bdf020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf020.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bdee00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment

命令の説明率　旧版 87.95% / 新版 87.95%

CFGの説明率　旧版 72.73% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0dda4",
      "incomplete_value": true,
      "site": "00b0dda4",
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
            "const:141:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dcdc",
      "incomplete_value": true,
      "site": "00b0dcdc",
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
            "const:141:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0dda8",
      "incomplete_value": true,
      "site": "00b0dda8",
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
            "const:144:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dce0",
      "incomplete_value": true,
      "site": "00b0dce0",
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
            "const:144:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b0dc90",
      "incomplete_value": true,
      "site": "00b0dc90",
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
      "definition_site": "00b0dbc8",
      "incomplete_value": true,
      "site": "00b0dbc8",
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
      "00b0dc84",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dc98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0dbf8"
      ]
    ],
    [
      "unmatched:00b0dbec",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0dc84",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dc98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0dcc0"
      ]
    ],
    [
      "00b0dcb4",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dba8.md#insn-00b0dbc8) · [`00b0dbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dba8.md#insn-00b0dbf4) · [`00b0dc0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dba8.md#insn-00b0dc0c)
- 新版 [`00b0dc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md#insn-00b0dc90) · [`00b0dcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md#insn-00b0dcd4)

~~~diff
- 00b0dbc8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b0dbc8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b0dc90 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b0dc90 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b0dbc8 bytes a80000b4
+ 00b0dc90 bytes a80000b4
- 00b0dbf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b0dbf4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b0dbf4 bytes 09ffff35
- 00b0dc0c ["INT_ADD", "register:40f0:8", ["const:b0dc0c:8", "const:4:8"]]
- 00b0dc0c ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b0dcd4 ["INT_ADD", "register:40f0:8", ["const:b0dcd4:8", "const:4:8"]]
+ 00b0dcd4 ["CALL", null, ["callee:00bddcf0:8"]]
- 00b0dc0c bytes 0d400394
+ 00b0dcd4 bytes 07400394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-949310eb6db5c9afbcf0359bd31e11dd"></a>

### [`00b0dcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md) → [`00b0ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md) _ZN20google_play_services17CallMakeAvailableEPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b0de68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0ddf4",
      "incomplete_value": true,
      "site": "00b0de04",
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dd2c",
      "incomplete_value": true,
      "site": "00b0dd3c",
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0ddf8",
      "incomplete_value": true,
      "site": "00b0de04",
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dd30",
      "incomplete_value": true,
      "site": "00b0dd3c",
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
                "const:e08:8"
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
      "definition_site": "00b0de38",
      "incomplete_value": true,
      "site": "00b0de3c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dd70",
      "incomplete_value": true,
      "site": "00b0dd74",
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
            "const:130:8"
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
      "unmatched:00b0dd2c",
      "READ",
      [
        "storage",
        "010a0df8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0dd30",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0de30",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0ddf4",
      "READ",
      [
        "storage",
        "010a0eb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0ddf8",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0de30",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md#insn-00b0dd3c) · [`00b0dd74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md#insn-00b0dd74) · [`00b0dd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md#insn-00b0dd90)
- 新版 [`00b0de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md#insn-00b0de04) · [`00b0de3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md#insn-00b0de3c) · [`00b0de58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md#insn-00b0de58)

~~~diff
- 00b0dd3c ["INT_ADD", "register:40f0:8", ["const:b0dd3c:8", "const:4:8"]]
- 00b0dd3c ["CALL", null, ["callee:00bdf040:8"]]
+ 00b0de04 ["INT_ADD", "register:40f0:8", ["const:b0de04:8", "const:4:8"]]
+ 00b0de04 ["CALL", null, ["callee:00bdf040:8"]]
- 00b0dd3c bytes 95440394
+ 00b0de04 bytes 8f440394
- 00b0dd74 ["INT_ADD", "register:40f0:8", ["const:b0dd74:8", "const:4:8"]]
- 00b0dd74 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b0de3c ["INT_ADD", "register:40f0:8", ["const:b0de3c:8", "const:4:8"]]
+ 00b0de3c ["CALL", null, ["callee:00bddf30:8"]]
- 00b0dd74 bytes 43400394
+ 00b0de3c bytes 3d400394
- 00b0dd90 ["INT_ADD", "register:40f0:8", ["const:b0dd90:8", "const:4:8"]]
- 00b0dd90 ["CALL", null, ["callee:00bdedb0:8"]]
+ 00b0de58 ["INT_ADD", "register:40f0:8", ["const:b0de58:8", "const:4:8"]]
+ 00b0de58 ["CALL", null, ["callee:00bdedb0:8"]]
- 00b0dd90 bytes dc430394
+ 00b0de58 bytes d6430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5fb9b3be9cf2119659b31df80cf5302"></a>

### [`00b0de68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md) → [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) _ZN20google_play_services13MakeAvailableEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded60.md) · 呼出先 14件 [`00b0dcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md)
- 新版 呼出元 1件 [`00bdee10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee10.md) · 呼出先 14件 [`00b0ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.75% / 新版 81.75%

CFGの説明率　旧版 17.95% / 新版 17.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0de6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0de70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0de70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0de6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0de70",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0de74",
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
      "00b0df34",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b0df38",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b0df3c",
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

- 旧版 [`00b0de6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md#insn-00b0de6c) · [`00b0de70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md#insn-00b0de70) · [`00b0de74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0de68.md#insn-00b0de74)

~~~diff
- 00b0de6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b0de6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b0de6c bytes f93300f9
- 00b0de70 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b0de70 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b0de70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b0de70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0de70 bytes f85f07a9
- 00b0de74 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b0de74 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0de74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b0de74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0de74 bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a099609797366b640dde4f4418649180"></a>

### [`00b0e08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e08c.md) → [`00b0e154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e154.md) _ZN20google_play_services23MakeAvailableLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdef80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef80.md) · 呼出先 6件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md)
- 新版 呼出元 1件 [`00bdf030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf030.md) · 呼出先 6件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e0a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b0e170"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0e0d0",
      "incomplete_value": true,
      "site": "00b0e0d8",
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
            "const:30:8"
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
      "00b0e168",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b0e0a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0e1bc"
      ]
    ]
  ],
  "added": [
    [
      "00b0e168",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0e170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0e1bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e08c.md#insn-00b0e0a8) · [`00b0e0d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e08c.md#insn-00b0e0d8)
- 新版 [`00b0e1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e154.md#insn-00b0e1a0) · [`00b0e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e154.md#insn-00b0e170)

~~~diff
- 00b0e0a8 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b0e0a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b0e0a8 bytes 750200b4
- 00b0e0d8 ["INT_ADD", "register:40f0:8", ["const:b0e0d8:8", "const:4:8"]]
- 00b0e0d8 ["CALL", null, ["callee:00bddf40:8"]]
+ 00b0e1a0 ["INT_ADD", "register:40f0:8", ["const:b0e1a0:8", "const:4:8"]]
+ 00b0e1a0 ["CALL", null, ["callee:00bddf40:8"]]
- 00b0e0d8 bytes 6e3f0394
+ 00b0e1a0 bytes 683f0394
+ 00b0e170 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b0e170 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b0e170 bytes 750200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c53d7409fa3f798846a1e39ab0bd87ad"></a>

### [`00b0e120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e120.md) → [`00b0e1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e1e8.md) FUN_00b0e1e8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 33.33% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b0e208"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b0e214",
      "incomplete_value": true,
      "site": "00b0e214",
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
      "definition_site": "00b0e14c",
      "incomplete_value": true,
      "site": "00b0e14c",
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
      "unmatched:00b0e140",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b0e210",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0e208",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b0e210",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e120.md#insn-00b0e140) · [`00b0e14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e120.md#insn-00b0e14c) · [`00b0e174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e120.md#insn-00b0e174)
- 新版 [`00b0e214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e1e8.md#insn-00b0e214) · [`00b0e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e1e8.md#insn-00b0e23c)

~~~diff
- 00b0e140 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b0e140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0e140 bytes e81f00f9
- 00b0e14c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00b0e14c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00b0e214 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00b0e214 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b0e14c bytes 140400b4
+ 00b0e214 bytes 140400b4
- 00b0e174 ["INT_ADD", "register:40f0:8", ["const:b0e174:8", "const:4:8"]]
- 00b0e174 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b0e23c ["INT_ADD", "register:40f0:8", ["const:b0e23c:8", "const:4:8"]]
+ 00b0e23c ["CALL", null, ["callee:00bddf30:8"]]
- 00b0e174 bytes 433f0394
+ 00b0e23c bytes 3d3f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3346fbd2ec24bba15d588e541e8cf909"></a>

### [`00b0e630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e630.md) → [`00b0e6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md) _ZN11flatbuffers14DeserializeDocERNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEPKNS_6VectorINS

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf1b0.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6d0.md)
- 新版 呼出元 1件 [`00bdf260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf260.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 78.26% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0e804",
      "incomplete_value": true,
      "site": "00b0e808",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e630.md#insn-00b0e740) · [`00b0e678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e630.md#insn-00b0e678) · [`00b0e680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e630.md#insn-00b0e680)
- 新版 [`00b0e808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md#insn-00b0e808) · [`00b0e748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e6f8.md#insn-00b0e748)

~~~diff
- 00b0e740 ["INT_ADD", "register:40f0:8", ["const:b0e740:8", "const:4:8"]]
- 00b0e740 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b0e808 ["INT_ADD", "register:40f0:8", ["const:b0e808:8", "const:4:8"]]
+ 00b0e808 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0e740 bytes 08320394
+ 00b0e808 bytes 02320394
- 00b0e678 ["INT_OR", "register:40d0:8", ["register:4040:8", "const:1:8"]]
- 00b0e678 bytes 1a0140b2
- 00b0e680 ["BRANCH", null, ["local:b5:8"]]
+ 00b0e748 ["BRANCH", null, ["local:b6:8"]]
- 00b0e680 bytes 0e000014
+ 00b0e748 bytes 0e000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a0e09c6abc7eb848e434a713ae00774"></a>

### [`00b0e77c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e77c.md) → [`00b0e844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md) _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8d0.md) · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdf0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0a0.md)
- 新版 呼出元 1件 [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.48% / 新版 94.48%

CFGの説明率　旧版 79.59% / 新版 79.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b0e9cc"
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
      "00b0e894",
      "PARAM",
      [
        "storage",
        "002a42af",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0e874",
      "PARAM",
      [
        "storage",
        "002a02b5",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0e894",
      "PARAM",
      [
        "storage",
        "002ac6bf",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b0e894",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ],
    [
      "00b0e93c",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ],
    [
      "00b0e95c",
      "PARAM",
      [
        "storage",
        "002ac6b6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e77c.md#insn-00b0e7d8) · [`00b0e840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e77c.md#insn-00b0e840) · [`00b0e880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0e77c.md#insn-00b0e880)
- 新版 [`00b0e8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md#insn-00b0e8a0) · [`00b0e908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md#insn-00b0e908) · [`00b0e948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md#insn-00b0e948)

~~~diff
- 00b0e7d8 ["INT_ADD", "register:40f0:8", ["const:b0e7d8:8", "const:4:8"]]
- 00b0e7d8 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b0e8a0 ["INT_ADD", "register:40f0:8", ["const:b0e8a0:8", "const:4:8"]]
+ 00b0e8a0 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b0e7d8 bytes 16320394
+ 00b0e8a0 bytes 10320394
- 00b0e840 ["INT_ADD", "register:40f0:8", ["const:b0e840:8", "const:4:8"]]
- 00b0e840 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b0e908 ["INT_ADD", "register:40f0:8", ["const:b0e908:8", "const:4:8"]]
+ 00b0e908 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b0e840 bytes fc310394
+ 00b0e908 bytes f6310394
- 00b0e880 ["INT_ADD", "register:40f0:8", ["const:b0e880:8", "const:4:8"]]
- 00b0e880 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b0e948 ["INT_ADD", "register:40f0:8", ["const:b0e948:8", "const:4:8"]]
+ 00b0e948 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b0e880 bytes ec310394
+ 00b0e948 bytes e6310394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6c7b8ac4bbbf909cc56a35e43ebaafb"></a>

### [`00b0ea08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ea08.md) → [`00b0ead0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ead0.md) _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0a0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 80.22% / 新版 80.22%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ea78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ea7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0eab0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0ea3c",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b0ea40",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b0ea78",
      "DATA",
      [
        "storage",
        "00c11040",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b0eb04",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb08",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb40",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ea78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ea08.md#insn-00b0ea78) · [`00b0ea7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ea08.md#insn-00b0ea7c) · [`00b0eab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0ea08.md#insn-00b0eab0)

~~~diff
- 00b0ea78 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b0ea78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0ea78 bytes e84b00f9
- 00b0ea7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b0ea7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b0ea7c bytes fb1300f9
- 00b0eab0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:120:8"]]
- 00b0eab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b0eab0 bytes e82301b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5d2952b8caf4a1382fc4103a541cd41"></a>

### [`00b0eb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eb74.md) → [`00b0ec3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ec3c.md) _ZN11flatbuffers11NumToStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0c0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2d0.md)
- 新版 呼出元 1件 [`00bdf170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf170.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb380.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 28.57% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ebdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ebe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0ebe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0eba4",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b0eba8",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b0ebdc",
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
      "00b0ec6c",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b0ec70",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eca4",
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

- 旧版 [`00b0ebdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eb74.md#insn-00b0ebdc) · [`00b0ebe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eb74.md#insn-00b0ebe0) · [`00b0ebe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eb74.md#insn-00b0ebe4)

~~~diff
- 00b0ebdc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b0ebdc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b0ebdc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b0ebdc bytes a9031af8
- 00b0ebe0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b0ebe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0ebe0 bytes e84b00f9
- 00b0ebe4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b0ebe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b0ebe4 bytes fb1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9557f830f52b132e819e3d847416acc"></a>

### [`00b0eeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eeb0.md) → [`00b0ef78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md) _ZN11flatbuffers6Parser12RecurseErrorEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf6f0.md) · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdc080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc080.md)
- 新版 呼出元 1件 [`00bdf7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7a0.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 57.89% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0efb4",
      "incomplete_value": true,
      "site": "00b0efc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0efbc",
      "incomplete_value": false,
      "site": "00b0efc0",
      "value": [
        "leaf",
        "const:0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0efb0",
      "incomplete_value": false,
      "site": "00b0efc0",
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
            "const:dc1:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0eee8",
      "PARAM",
      [
        "storage",
        "002a3dc8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0ef08",
      "PARAM",
      [
        "storage",
        "0029874a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0ef48",
      "PARAM",
      [
        "storage",
        "00291545",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0efb0",
      "PARAM",
      [
        "storage",
        "002a3dc1",
        null,
        "string"
      ]
    ],
    [
      "00b0efd0",
      "PARAM",
      [
        "storage",
        "002987d7",
        null,
        "string"
      ]
    ],
    [
      "00b0f010",
      "PARAM",
      [
        "storage",
        "00291545",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0eef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eeb0.md#insn-00b0eef8) · [`00b0ef24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eeb0.md#insn-00b0ef24) · [`00b0ef50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0e/00b0eeb0.md#insn-00b0ef50)
- 新版 [`00b0efc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md#insn-00b0efc0) · [`00b0efec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md#insn-00b0efec) · [`00b0f018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md#insn-00b0f018)

~~~diff
- 00b0eef8 ["INT_ADD", "register:40f0:8", ["const:b0eef8:8", "const:4:8"]]
- 00b0eef8 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b0efc0 ["INT_ADD", "register:40f0:8", ["const:b0efc0:8", "const:4:8"]]
+ 00b0efc0 ["CALL", null, ["callee:00bdc130:8"]]
- 00b0eef8 bytes 62340394
+ 00b0efc0 bytes 5c340394
- 00b0ef24 ["INT_ADD", "register:40f0:8", ["const:b0ef24:8", "const:4:8"]]
- 00b0ef24 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b0efec ["INT_ADD", "register:40f0:8", ["const:b0efec:8", "const:4:8"]]
+ 00b0efec ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b0ef24 bytes 43300394
+ 00b0efec bytes 3d300394
- 00b0ef50 ["INT_ADD", "register:40f0:8", ["const:b0ef50:8", "const:4:8"]]
- 00b0ef50 ["CALL", null, ["callee:00bdb210:8"]]
+ 00b0f018 ["INT_ADD", "register:40f0:8", ["const:b0f018:8", "const:4:8"]]
+ 00b0f018 ["CALL", null, ["callee:00bdb210:8"]]
- 00b0ef50 bytes 84300394
+ 00b0f018 bytes 7e300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5028c5fbd124ef39d410a55f1cf5591"></a>

### [`00b0f350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f350.md) → [`00b0f418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md) _ZN11flatbuffers6Parser11ParseHexNumEiPm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf690.md) · 呼出先 11件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf740.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.90% / 新版 92.90%

CFGの説明率　旧版 36.92% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f5b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f5b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b0f680"
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
      "unmatched:00b0f3dc",
      "PARAM",
      [
        "storage",
        "002ad410",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0f3fc",
      "PARAM",
      [
        "storage",
        "002932cb",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0f4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0f5c4"
      ]
    ]
  ],
  "added": [
    [
      "00b0f4a4",
      "PARAM",
      [
        "storage",
        "002ad407",
        null,
        "string"
      ]
    ],
    [
      "00b0f4c4",
      "PARAM",
      [
        "storage",
        "00293358",
        null,
        "string"
      ]
    ],
    [
      "00b0f5ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0f5c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f3ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f350.md#insn-00b0f3ec) · [`00b0f418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f350.md#insn-00b0f418) · [`00b0f4cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f350.md#insn-00b0f4cc)
- 新版 [`00b0f4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md#insn-00b0f4b4) · [`00b0f4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md#insn-00b0f4e0) · [`00b0f594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md#insn-00b0f594)

~~~diff
- 00b0f3ec ["INT_ADD", "register:40f0:8", ["const:b0f3ec:8", "const:4:8"]]
- 00b0f3ec ["CALL", null, ["callee:00bdc130:8"]]
+ 00b0f4b4 ["INT_ADD", "register:40f0:8", ["const:b0f4b4:8", "const:4:8"]]
+ 00b0f4b4 ["CALL", null, ["callee:00bdc130:8"]]
- 00b0f3ec bytes 25330394
+ 00b0f4b4 bytes 1f330394
- 00b0f418 ["INT_ADD", "register:40f0:8", ["const:b0f418:8", "const:4:8"]]
- 00b0f418 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b0f4e0 ["INT_ADD", "register:40f0:8", ["const:b0f4e0:8", "const:4:8"]]
+ 00b0f4e0 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b0f418 bytes 062f0394
+ 00b0f4e0 bytes 002f0394
- 00b0f4cc ["INT_ADD", "register:40f0:8", ["const:b0f4cc:8", "const:4:8"]]
- 00b0f4cc ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b0f594 ["INT_ADD", "register:40f0:8", ["const:b0f594:8", "const:4:8"]]
+ 00b0f594 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b0f4cc bytes 9d2e0394
+ 00b0f594 bytes 972e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c28a2b747d0ca55a20d6cc013b167681"></a>

### [`00b0f62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f62c.md) → [`00b0f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md) _ZN11flatbuffers6Parser17SkipByteOrderMarkEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf810.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdf8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8d0.md)
- 新版 呼出元 1件 [`00bdf8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8c0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f67c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f774",
      "incomplete_value": true,
      "site": "00b0f788",
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
              "INT_ADD",
              [
                "leaf",
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f6ac",
      "incomplete_value": true,
      "site": "00b0f6c0",
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
              "INT_ADD",
              [
                "leaf",
                "const:d:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f778",
      "incomplete_value": true,
      "site": "00b0f78c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:ec1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f6b0",
      "incomplete_value": true,
      "site": "00b0f6c4",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:e34:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0f774",
      "READ",
      [
        "storage",
        "002a1e41",
        null,
        "string"
      ]
    ],
    [
      "00b0f778",
      "READ",
      [
        "storage",
        "002a1e34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f774",
      "READ",
      [
        "storage",
        "002a1ece",
        null,
        "string"
      ]
    ],
    [
      "00b0f778",
      "READ",
      [
        "storage",
        "002a1ec1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f62c.md#insn-00b0f67c) · [`00b0f65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f62c.md#insn-00b0f65c)
- 新版 [`00b0f744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md#insn-00b0f744) · [`00b0f724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md#insn-00b0f724)

~~~diff
- 00b0f67c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0f67c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0f67c bytes 880200f9
+ 00b0f744 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b0f744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b0f744 bytes 880200f9
- 00b0f65c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b0f65c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b0f724 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b0f724 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b0f65c bytes c1010054
+ 00b0f724 bytes c1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5b406803416fc9b6c336bc6d725980"></a>

### [`00b0f740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f740.md) → [`00b0f808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f808.md) _ZN11flatbuffers6Parser4NextEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf870.md) · 呼出先 13件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bdc080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdc080.md)
- 新版 呼出元 1件 [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md) · 呼出先 13件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.88% / 新版 81.88%

CFGの説明率　旧版 68.20% / 新版 68.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 13件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 12件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0f748"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0f744",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f748",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0f74c",
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
      "00b0f80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b0f810",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b0f814",
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

- 旧版 [`00b0f744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f740.md#insn-00b0f744) · [`00b0f748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f740.md#insn-00b0f748) · [`00b0f74c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0f/00b0f740.md#insn-00b0f74c)

~~~diff
- 00b0f744 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b0f744 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b0f744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b0f744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f744 bytes fc6f07a9
- 00b0f748 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b0f748 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b0f748 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b0f748 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f748 bytes fa6708a9
- 00b0f74c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b0f74c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b0f74c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b0f74c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0f74c bytes f85f09a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-662ab31abf3b90969f07a4021b8b9704"></a>

### [`00b10da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10da0.md) → [`00b10e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md) _ZN11flatbuffers6Parser6ExpectEi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8b0.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b10f94",
      "incomplete_value": false,
      "site": "00b10fb0",
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
            "const:456:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10ecc",
      "incomplete_value": false,
      "site": "00b10ee8",
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
            "const:4ea:8"
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
      "00b10efc",
      "DATA",
      [
        "storage",
        "00c105d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b10f94",
      "PARAM",
      [
        "storage",
        "002ae4ea",
        null,
        "string"
      ]
    ],
    [
      "00b11054",
      "DATA",
      [
        "storage",
        "00c10dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b10efc",
      "DATA",
      [
        "storage",
        "00c10680",
        null,
        "pointer"
      ]
    ],
    [
      "00b10f94",
      "PARAM",
      [
        "storage",
        "002ae456",
        null,
        "string"
      ]
    ],
    [
      "00b11054",
      "DATA",
      [
        "storage",
        "00c10e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10da0.md#insn-00b10ee8) · [`00b10de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10da0.md#insn-00b10de4) · [`00b10e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b10/00b10da0.md#insn-00b10e0c)
- 新版 [`00b10fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md#insn-00b10fb0) · [`00b10eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md#insn-00b10eac) · [`00b10ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md#insn-00b10ed4)

~~~diff
- 00b10ee8 ["INT_ADD", "register:40f0:8", ["const:b10ee8:8", "const:4:8"]]
- 00b10ee8 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b10fb0 ["INT_ADD", "register:40f0:8", ["const:b10fb0:8", "const:4:8"]]
+ 00b10fb0 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b10ee8 bytes 52280394
+ 00b10fb0 bytes 4c280394
- 00b10de4 ["INT_ADD", "register:40f0:8", ["const:b10de4:8", "const:4:8"]]
- 00b10de4 ["CALL", null, ["callee:00bdf920:8"]]
+ 00b10eac ["INT_ADD", "register:40f0:8", ["const:b10eac:8", "const:4:8"]]
+ 00b10eac ["CALL", null, ["callee:00bdf920:8"]]
- 00b10de4 bytes a33a0394
+ 00b10eac bytes 9d3a0394
- 00b10e0c ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00b10e0c ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00b10e0c ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00b10e0c ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00b10ed4 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00b10ed4 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00b10ed4 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00b10ed4 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00b10e0c bytes 5a433791
+ 00b10ed4 bytes 5a033a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3a4831c07de46842109e74f4554323"></a>

### [`00b115bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b115bc.md) → [`00b11684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md) _ZN11flatbuffers6Parser18LookupCreateStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf820.md) · 呼出先 16件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdf8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8d0.md) · 呼出先 16件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.83% / 新版 93.83%

CFGの説明率　旧版 80.34% / 新版 78.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b115f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1173c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b116b8"
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
      "unmatched:00b115f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b117d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b118dc"
      ]
    ],
    [
      "unmatched:00b11874",
      "PARAM",
      [
        "storage",
        "002a02b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b116b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b118a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b118dc"
      ]
    ],
    [
      "00b1193c",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b115f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b115bc.md#insn-00b115f0) · [`00b116b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b115bc.md#insn-00b116b8)
- 新版 [`00b11780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md#insn-00b11780) · [`00b116b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md#insn-00b116b8)

~~~diff
- 00b115f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b115f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b115f0 bytes e82700f9
- 00b116b8 ["BRANCH", null, ["local:b47:8"]]
+ 00b11780 ["BRANCH", null, ["local:b49:8"]]
- 00b116b8 bytes 96000014
+ 00b11780 bytes 96000014
+ 00b116b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
+ 00b116b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b116b8 bytes e82700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5826cc37bbf4268e6c4b9d049ac9bc92"></a>

### [`00b11acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11acc.md) → [`00b11b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md) _ZN11flatbuffers6Parser9ParseTypeERNS_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b11acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11acc.md) [`00bdf930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf930.md) · 呼出先 12件 [`00b11acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11acc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 2件 [`00b11b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md) [`00bdf9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9e0.md) · 呼出先 12件 [`00b11b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.42% / 新版 76.42%

CFGの説明率　旧版 40.99% / 新版 41.51%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11bf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b11cac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b11afc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b11b08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b11c40"
      ]
    ],
    [
      "unmatched:00b11b34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b11e18"
      ]
    ]
  ],
  "added": [
    [
      "00b11bc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b11bd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b11c40"
      ]
    ],
    [
      "00b11bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b11e18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b11afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11acc.md#insn-00b11afc) · [`00b11bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b11/00b11acc.md#insn-00b11bc4)
- 新版 [`00b11bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md#insn-00b11bc4)

~~~diff
- 00b11afc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b11afc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b11afc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b11afc bytes a9831bf8
- 00b11bc4 ["COPY", "tmp:0:8", ["const:e66:8"]]
- 00b11bc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b11bc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b11bc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b11bc4 bytes 29993991
+ 00b11bc4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b11bc4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
+ 00b11bc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b11bc4 bytes a9831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e37189d4ea1cf9e1de46ff418dda0ff"></a>

### [`00b12238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12238.md) → [`00b12300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12300.md) _ZN11flatbuffers6Parser8AddFieldERNS_9StructDefERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS_4TypeEPPNS_8FieldD

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8e0.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bdf990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf990.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 41.46% / 新版 42.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b122b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b122b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b122b8",
      "PARAM",
      [
        "storage",
        "002a74c6",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1230c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b123f8"
      ]
    ],
    [
      "00b12484",
      "READ",
      [
        "storage",
        "00c1b928",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b12380",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ],
    [
      "00b123d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b123f8"
      ]
    ],
    [
      "00b12484",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b12294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12238.md#insn-00b12294) · [`00b122b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12238.md#insn-00b122b0) · [`00b122bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12238.md#insn-00b122bc)

~~~diff
- 00b12294 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b12294 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b12294 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:50:8"]]
- 00b12294 ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00b12294 bytes 1f0d05f8
- 00b122b0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b122b0 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b122b0 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00b122b0 ["INT_ADD", "tmp:3:8", ["register:4000:8", "const:40:8"]]
- 00b122b0 bytes 1f2004a9
- 00b122bc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:80:8"]]
- 00b122bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b122bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b122bc bytes ff4200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eef990fe58d605d3a6124fbefe941699"></a>

### [`00b124b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b124b8.md) → [`00b12580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12580.md) _ZN11flatbuffers10InlineSizeERKNS_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf070.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdf070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf070.md)
- 新版 呼出元 1件 [`00bdf120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf120.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf120.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 46.15% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b125d4",
      "incomplete_value": true,
      "site": "00b125e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00b125f8",
      "READ",
      [
        "storage",
        "00c1b928",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b125f8",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1251c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b124b8.md#insn-00b1251c) · [`00b124e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b124b8.md#insn-00b124e0) · [`00b124ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b124b8.md#insn-00b124ec)
- 新版 [`00b125e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12580.md#insn-00b125e4) · [`00b125a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12580.md#insn-00b125a8) · [`00b125b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12580.md#insn-00b125b4)

~~~diff
- 00b1251c ["INT_ADD", "register:40f0:8", ["const:b1251c:8", "const:4:8"]]
- 00b1251c ["CALL", null, ["callee:00bdf120:8"]]
+ 00b125e4 ["INT_ADD", "register:40f0:8", ["const:b125e4:8", "const:4:8"]]
+ 00b125e4 ["CALL", null, ["callee:00bdf120:8"]]
- 00b1251c bytes d5320394
+ 00b125e4 bytes cf320394
- 00b124e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b124e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b125a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b125a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b124e0 bytes c1000054
+ 00b125a8 bytes c1000054
- 00b124ec ["INT_EQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
- 00b124ec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b125b4 ["INT_EQUAL", "tmp:0:1", ["register:4050:4", "const:0:4"]]
+ 00b125b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b124ec bytes 0a020034
+ 00b125b4 bytes 0a020034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25a164383315d54d47433274655c517"></a>

### [`00b1255c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b1255c.md) → [`00b12624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12624.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf160.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf210.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.91% / 新版 80.91%

CFGの説明率　旧版 36.84% / 新版 37.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 4件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b12564"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b12560",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b12564",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b12568",
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
      "00b12628",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b1262c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b12630",
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

- 旧版 [`00b12560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b1255c.md#insn-00b12560) · [`00b12564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b1255c.md#insn-00b12564) · [`00b12568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b1255c.md#insn-00b12568)

~~~diff
- 00b12560 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b12560 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b12560 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b12560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12560 bytes fc6f01a9
- 00b12564 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b12564 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b12564 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b12564 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12564 bytes fa6702a9
- 00b12568 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b12568 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b12568 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b12568 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b12568 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e5e5d9956a875cbbd0bfdbebd732f32"></a>

### [`00b12714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12714.md) → [`00b127dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md) _ZN11flatbuffers6Parser10ParseFieldERNS_9StructDefE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf650.md) · 呼出先 26件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdf700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf700.md) · 呼出先 26件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.66% / 新版 73.66%

CFGの説明率　旧版 35.29% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 35件, `store_condition` 3件, `store_value` 14件, `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 113件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b128d0",
      "incomplete_value": true,
      "site": "00b128e8",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12808",
      "incomplete_value": true,
      "site": "00b12820",
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
              "INT_ADD",
              [
                "leaf",
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b128d8",
      "incomplete_value": true,
      "site": "00b128e8",
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
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12810",
      "incomplete_value": true,
      "site": "00b12820",
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
              "INT_ADD",
              [
                "leaf",
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b128d0",
      "incomplete_value": true,
      "site": "00b128ec",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:650:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12808",
      "incomplete_value": true,
      "site": "00b12824",
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
                "const:297000:8"
              ],
              [
                "leaf",
                "const:5c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b128d0",
      "READ",
      [
        "storage",
        "002975c3",
        null,
        "string"
      ]
    ],
    [
      "00b128d0",
      "READ",
      [
        "storage",
        "002975d3",
        null,
        "string"
      ]
    ],
    [
      "00b128d8",
      "READ",
      [
        "storage",
        "002975e3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b128d0",
      "READ",
      [
        "storage",
        "00297650",
        null,
        "string"
      ]
    ],
    [
      "00b128d0",
      "READ",
      [
        "storage",
        "00297660",
        null,
        "string"
      ]
    ],
    [
      "00b128d8",
      "READ",
      [
        "storage",
        "00297670",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b12960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12714.md#insn-00b12960) · [`00b1296c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12714.md#insn-00b1296c) · [`00b129a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b12/00b12714.md#insn-00b129a8)
- 新版 [`00b12a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md#insn-00b12a28) · [`00b12a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md#insn-00b12a34) · [`00b12a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md#insn-00b12a70)

~~~diff
- 00b12960 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b12960 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b12960 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b12960 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b12a28 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b12a28 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b12a28 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b12a28 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b12960 bytes c8000037
+ 00b12a28 bytes c8000037
- 00b1296c ["CBRANCH", null, ["local:b32:8", "register:101:1"]]
+ 00b12a34 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
- 00b1296c bytes c0000054
+ 00b12a34 bytes c0000054
- 00b129a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b129a8 ["CBRANCH", null, ["local:b315:8", "tmp:0:1"]]
+ 00b12a70 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b12a70 ["CBRANCH", null, ["local:b319:8", "tmp:0:1"]]
- 00b129a8 bytes 419a0054
+ 00b12a70 bytes 419a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c32f92221c08bb9e5f270a3a72fcd60"></a>

### [`00b13cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b13/00b13cf8.md) → [`00b13dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13dc0.md) _ZNK11flatbuffers6Parser29SupportsAdvancedArrayFeaturesEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-aadad32ce0088300f2fc75a439690892"></a>

### [`00b13d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b13/00b13d30.md) → [`00b13df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md) _ZN11flatbuffers6Parser16ParseSingleValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf7f0.md) · 呼出先 34件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8a0.md) · 呼出先 34件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.05% / 新版 83.05%

CFGの説明率　旧版 31.45% / 新版 31.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `call_target` 1件, `store_condition` 10件, `unresolved_branch_alignment` 36件, `unresolved_call_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 33件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13d38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b13d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b13d38",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b13d3c",
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
      "00b13dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b13e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b13e04",
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

- 旧版 [`00b13d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b13/00b13d30.md#insn-00b13d34) · [`00b13d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b13/00b13d30.md#insn-00b13d38) · [`00b13d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b13/00b13d30.md#insn-00b13d3c)

~~~diff
- 00b13d34 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b13d34 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b13d34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b13d34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b13d34 bytes fc6f13a9
- 00b13d38 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b13d38 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b13d38 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b13d38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b13d38 bytes fa6714a9
- 00b13d3c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b13d3c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b13d3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b13d3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b13d3c bytes f85f15a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab3a1b63d3ed5a311a8fd32a197d9bef"></a>

### [`00b14dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14dc8.md) → [`00b14e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md) _ZNK11flatbuffers7EnumDef11FindByValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdfb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdfb20.md) · 呼出先 3件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdf4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4e0.md) [`00bdf4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf4f0.md)
- 新版 呼出元 1件 [`00bdfbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfbd0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf590.md) [`00bdf5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 32.35% / 新版 30.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14ee4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b14e40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b14f48"
      ]
    ],
    [
      "unmatched:00b14ee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b14fc4"
      ]
    ]
  ],
  "added": [
    [
      "00b14f08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b14f48"
      ]
    ],
    [
      "00b14fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b14fc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b14e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14dc8.md#insn-00b14e18) · [`00b14e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14dc8.md#insn-00b14e40) · [`00b14e64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14dc8.md#insn-00b14e64)
- 新版 [`00b14ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14e90.md#insn-00b14ee0)

~~~diff
- 00b14e18 ["INT_ADD", "register:40f0:8", ["const:b14e18:8", "const:4:8"]]
- 00b14e18 ["CALL", null, ["callee:00bdf5a0:8"]]
+ 00b14ee0 ["INT_ADD", "register:40f0:8", ["const:b14ee0:8", "const:4:8"]]
+ 00b14ee0 ["CALL", null, ["callee:00bdf5a0:8"]]
- 00b14e18 bytes b6290394
+ 00b14ee0 bytes b0290394
- 00b14e40 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b14e40 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b14e40 bytes 03020054
- 00b14e64 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b14e64 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b14e64 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b14e64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b14e64 bytes 2115819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-583b6af8d2f06dfb56bd3a5b9c765bb3"></a>

### [`00b14f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14f00.md) → [`00b14fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14fc8.md) _ZN11flatbuffers6Parser13ParseMetaDataEPNS_11SymbolTableINS_5ValueEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf720.md) · 呼出先 13件 [`00613fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00613/00613fbc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdf7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7d0.md) · 呼出先 13件 [`00613fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/00613fbc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.87% / 新版 78.87%

CFGの説明率　旧版 34.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b14f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1515c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b14f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b14f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00b15130",
      "PARAM",
      [
        "storage",
        "002a74c6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b15044",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00b15064",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00b15130",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b14f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14f00.md#insn-00b14f7c) · [`00b14f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14f00.md#insn-00b14f9c) · [`00b14fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b14/00b14f00.md#insn-00b14fe0)
- 新版 [`00b150a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14fc8.md#insn-00b150a8)

~~~diff
- 00b14f7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b14f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b14f7c bytes e80700f9
- 00b14f9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b14f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b14f9c bytes e00f803d
- 00b14fe0 ["INT_ADD", "register:40f0:8", ["const:b14fe0:8", "const:4:8"]]
- 00b14fe0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b150a8 ["INT_ADD", "register:40f0:8", ["const:b150a8:8", "const:4:8"]]
+ 00b150a8 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b14fe0 bytes d8170394
+ 00b150a8 bytes d2170394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-060de1277f216d007b6b1134ce026c43"></a>

### [`00b15254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15254.md) → [`00b1531c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1531c.md) _ZN11flatbuffers11SymbolTableINS_5ValueEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf120.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1d0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 62.73% / 新版 62.73%

CFGの説明率　旧版 3.51% / 新版 3.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 3件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15258"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15258"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1525c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b15258",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1525c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b15260",
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
      "00b15320",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b15324",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b15328",
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

- 旧版 [`00b15258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15254.md#insn-00b15258) · [`00b1525c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15254.md#insn-00b1525c) · [`00b15260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15254.md#insn-00b15260)

~~~diff
- 00b15258 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b15258 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b15258 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b15258 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15258 bytes fc6f01a9
- 00b1525c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1525c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1525c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b1525c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1525c bytes fa6702a9
- 00b15260 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b15260 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b15260 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b15260 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15260 bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8e456e7b8a75c69e43cedf35238f257"></a>

### [`00b1540c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b1540c.md) → [`00b154d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b154d4.md) _ZN11flatbuffers6Parser11ParseStringERNS_5ValueE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf6a0.md) · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf750.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.57% / 新版 90.57%

CFGの説明率　旧版 63.89% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b15410",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b15414",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b15418",
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
      "00b154d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b154dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b154e0",
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

- 旧版 [`00b15410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b1540c.md#insn-00b15410) · [`00b15414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b1540c.md#insn-00b15414) · [`00b15418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b1540c.md#insn-00b15418)

~~~diff
- 00b15410 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b15410 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b15410 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b15410 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15410 bytes fa6704a9
- 00b15414 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b15414 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b15414 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b15414 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15414 bytes f85f05a9
- 00b15418 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b15418 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b15418 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b15418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b15418 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2e1ae6fe2219daa8378ee4f812cace2"></a>

### [`00b155b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b155b4.md) → [`00b1567c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1567c.md) _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0b0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00bdf160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf160.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.32% / 新版 81.32%

CFGの説明率　旧版 40.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1569c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b155e8",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b155ec",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b15624",
      "DATA",
      [
        "storage",
        "00c11040",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b156b0",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b156b4",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b156ec",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b15624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b155b4.md#insn-00b15624) · [`00b15628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b155b4.md#insn-00b15628) · [`00b1569c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b155b4.md#insn-00b1569c)

~~~diff
- 00b15624 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b15624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b15624 bytes e84b00f9
- 00b15628 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b15628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b15628 bytes fb1300f9
- 00b1569c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 00b1569c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1569c bytes e083863c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ae25733c8efc1c3b8b16a82bc7da23"></a>

### [`00b15720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15720.md) → [`00b157e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b157e8.md) _ZN11flatbuffers6Parser10ParseCommaEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdf8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf8b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b15734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15720.md#insn-00b15734) · [`00b15740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15720.md#insn-00b15740) · [`00b15750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15720.md#insn-00b15750)
- 新版 [`00b157fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b157e8.md#insn-00b157fc) · [`00b15808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b157e8.md#insn-00b15808) · [`00b15818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b157e8.md#insn-00b15818)

~~~diff
- 00b15734 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b15734 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b157fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b157fc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b15734 bytes 09010035
+ 00b157fc bytes 09010035
- 00b15740 ["INT_ADD", "register:40f0:8", ["const:b15740:8", "const:4:8"]]
- 00b15740 ["CALL", null, ["callee:00bdf960:8"]]
+ 00b15808 ["INT_ADD", "register:40f0:8", ["const:b15808:8", "const:4:8"]]
+ 00b15808 ["CALL", null, ["callee:00bdf960:8"]]
- 00b15740 bytes 5c280394
+ 00b15808 bytes 56280394
- 00b15750 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b15750 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b15818 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b15818 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b15750 bytes 48000035
+ 00b15818 bytes 48000035
~~~


<a id="compare-3c725436bf62297f9b633dab92ae7a34"></a>

### [`00b15764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15764.md) → [`00b1582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md) _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEjb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b15764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15764.md) [`00bdf700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf700.md) · 呼出先 28件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00b15764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15764.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 2件 [`00b1582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md) [`00bdf7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7b0.md) · 呼出先 28件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00b1582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.92% / 新版 85.92%

CFGの説明率　旧版 41.98% / 新版 41.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b159c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b15a08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b15798",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b15884",
      "DATA",
      [
        "storage",
        "002f84c6",
        "switchD_00b157d0::switchdataD_002f84c6",
        "byte"
      ]
    ],
    [
      "unmatched:00b1580c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b15904"
      ]
    ]
  ],
  "added": [
    [
      "00b15860",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b15884",
      "DATA",
      [
        "storage",
        "002f84c6",
        "switchD_00b15898::switchdataD_002f84c6",
        "byte"
      ]
    ],
    [
      "00b158d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b15904"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b15798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15764.md#insn-00b15798) · [`00b15940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b15/00b15764.md#insn-00b15940)
- 新版 [`00b15860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md#insn-00b15860) · [`00b15a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md#insn-00b15a08)

~~~diff
- 00b15798 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b15798 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff98:8"]]
- 00b15798 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b15798 bytes a98319f8
+ 00b15860 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b15860 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffff98:8"]]
+ 00b15860 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b15860 bytes a98319f8
- 00b15940 ["INT_ADD", "register:40f0:8", ["const:b15940:8", "const:4:8"]]
- 00b15940 ["CALL", null, ["callee:00bdf750:8"]]
+ 00b15a08 ["INT_ADD", "register:40f0:8", ["const:b15a08:8", "const:4:8"]]
+ 00b15a08 ["CALL", null, ["callee:00bdf750:8"]]
- 00b15940 bytes 58270394
+ 00b15a08 bytes 52270394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ef1f39c1ef997e05d51f1da97d5c4b8"></a>

### [`00b16328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16328.md) → [`00b163f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md) _ZN11flatbuffers4atotIjEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf5e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5e0.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf690.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.59% / 新版 81.59%

CFGの説明率　旧版 40.00% / 新版 38.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1632c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1632c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16330"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1632c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b16330",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b16334",
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
      "00b163f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b163f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b163fc",
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

- 旧版 [`00b1632c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16328.md#insn-00b1632c) · [`00b16330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16328.md#insn-00b16330) · [`00b16334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16328.md#insn-00b16334)

~~~diff
- 00b1632c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1632c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1632c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b1632c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1632c bytes fc670da9
- 00b16330 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b16330 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b16330 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b16330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16330 bytes f85f0ea9
- 00b16334 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b16334 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b16334 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b16334 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16334 bytes f6570fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c188d8877bf3639fbfadf1f020915487"></a>

### [`00b1677c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b1677c.md) → [`00b16844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md) _ZN11flatbuffers6Parser16SkipAnyJsonValueEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b1677c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b1677c.md) [`00bdf800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf800.md) · 呼出先 9件 [`00b1677c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b1677c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 2件 [`00b16844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md) [`00bdf8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8b0.md) · 呼出先 9件 [`00b16844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16844.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 58.62% / 新版 60.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16780"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16784"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b16780",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b16784",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b16788",
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
      "00b16848",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b1684c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b16850",
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

- 旧版 [`00b16780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b1677c.md#insn-00b16780) · [`00b16784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b1677c.md#insn-00b16784) · [`00b16788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b1677c.md#insn-00b16788)

~~~diff
- 00b16780 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b16780 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b16780 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b16780 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16780 bytes fc6f03a9
- 00b16784 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b16784 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b16784 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b16784 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16784 bytes fa6704a9
- 00b16788 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b16788 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b16788 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b16788 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b16788 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a7feb0d23d666ea28db2d22708bdaf2"></a>

### [`00b16bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16bc0.md) → [`00b16c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md) _ZN11flatbuffers4atotIhEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5c0.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf670.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.26% / 新版 77.26%

CFGの説明率　旧版 37.36% / 新版 35.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b16d98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b16bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b16d84",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b16e48"
      ]
    ],
    [
      "00b16dc4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b16d3c"
      ]
    ]
  ],
  "added": [
    [
      "00b16cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b16d84",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b16f10"
      ]
    ],
    [
      "00b16dc4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b16e04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b16bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16bc0.md#insn-00b16bf0) · [`00b16cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b16/00b16bc0.md#insn-00b16cb8)
- 新版 [`00b16d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md#insn-00b16d80) · [`00b16cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md#insn-00b16cb8)

~~~diff
- 00b16bf0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b16bf0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b16bf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b16bf0 bytes a9831bf8
- 00b16cb8 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b16cb8 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
+ 00b16d80 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b16d80 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 00b16cb8 bytes 160c00b5
+ 00b16d80 bytes 160c00b5
+ 00b16cb8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b16cb8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
+ 00b16cb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00b16cb8 bytes a9831bf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5586d2dd92f9b919838b743cfa500b"></a>

### [`00b17054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md) → [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) _ZN11flatbuffers6Parser10ParseTableERKNS_9StructDefEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEPj

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf660.md) · 呼出先 37件 [`00b3fbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3f/00b3fbc0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdf710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf710.md) · 呼出先 37件 [`00b3fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fc88.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.79% / 新版 60.79%

CFGの説明率　旧版 35.08% / 新版 34.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_condition` 11件, `unresolved_branch_alignment` 121件, `unresolved_call_alignment` 32件, `unresolved_store_alignment` 85件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1706c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1706c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b17088"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1706c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b17088",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b170a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1719c"
      ]
    ]
  ],
  "added": [
    [
      "00b17134",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b17150",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b17170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1719c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1706c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md#insn-00b1706c) · [`00b17088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md#insn-00b17088) · [`00b17304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b17/00b17054.md#insn-00b17304)
- 新版 [`00b173cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md#insn-00b173cc)

~~~diff
- 00b1706c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b1706c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b1706c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00b1706c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1706c bytes fd7b13a9
- 00b17088 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b17088 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b17088 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b17088 bytes a9031af8
- 00b17304 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b17304 ["CBRANCH", null, ["local:b39:8", "tmp:0:1"]]
+ 00b173cc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b173cc ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00b17304 bytes a1000054
+ 00b173cc bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3216233f774b953fbfabfd6e65c8f0f8"></a>

### [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) → [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) _ZN11flatbuffers6Parser11ParseVectorERKNS_4TypeEPjPNS_8FieldDefEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf6b0.md) · 呼出先 32件 [`00b1cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md) [`00b1cd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md) [`00b40a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40a48.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bdf760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf760.md) · 呼出先 32件 [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) [`00b40b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40b10.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.39% / 新版 87.39%

CFGの説明率　旧版 64.94% / 新版 64.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b18ed0",
      "READ",
      [
        "storage",
        "00c1b928",
        null,
        "pointer"
      ]
    ],
    [
      "00b19078",
      "DATA",
      [
        "storage",
        "002f84e3",
        "switchD_00b18fb8::switchdataD_002f84e3",
        "byte"
      ]
    ],
    [
      "00b19080",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b1907c"
      ]
    ]
  ],
  "added": [
    [
      "00b18ed0",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b19078",
      "DATA",
      [
        "storage",
        "002f84e3",
        "switchD_00b19080::switchdataD_002f84e3",
        "byte"
      ]
    ],
    [
      "00b19080",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b19144"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b18fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md#insn-00b18fa8) · [`00b19034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md#insn-00b19034) · [`00b19048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md#insn-00b19048)
- 新版 [`00b19070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md#insn-00b19070)

~~~diff
- 00b18fa8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b18fa8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b18fa8 ["CBRANCH", null, ["local:b125:8", "tmp:1:1"]]
+ 00b19070 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b19070 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b19070 ["CBRANCH", null, ["local:b129:8", "tmp:1:1"]]
- 00b18fa8 bytes 481c0054
+ 00b19070 bytes 481c0054
- 00b19034 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b19034 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b19034 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b19034 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b19034 bytes 2a050037
- 00b19048 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b19048 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b19048 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b19048 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b19048 bytes 8a080037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71440dbb260d4448c49751e0d19d27ea"></a>

### [`00b1949c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md) → [`00b19564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19564.md) _ZN11flatbuffers6Parser10ParseArrayERNS_5ValueE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf640.md) · 呼出先 32件 [`00b40fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40fb0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6f0.md) · 呼出先 32件 [`00b41078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b41078.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.51% / 新版 89.51%

CFGの説明率　旧版 59.68% / 新版 60.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b19510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1951c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1951c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b19510",
      "WRITE",
      [
        "storage",
        "Stack[-0x158]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1951c",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1952c",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b195d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x158]",
        null,
        null
      ]
    ],
    [
      "00b195e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x150]",
        null,
        null
      ]
    ],
    [
      "00b195f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b19510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md#insn-00b19510) · [`00b1951c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md#insn-00b1951c) · [`00b1952c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b19/00b1949c.md#insn-00b1952c)

~~~diff
- 00b19510 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b19510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b19510 bytes e80700f9
- 00b1951c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b1951c ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b1951c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b1951c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1951c bytes e80301a9
- 00b1952c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b1952c ["COPY", "tmp:1:4", ["register:4048:4"]]
- 00b1952c ["COPY", "tmp:2:4", ["tmp:0:4"]]
- 00b1952c ["INT_ADD", "tmp:3:8", ["register:40e8:8", "const:ffffffffffffff80:8"]]
- 00b1952c bytes a97f3029
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3641ac33130bfad058e15e3b8c56981"></a>

### [`00b1a230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a230.md) → [`00b1a2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md) _ZN11flatbuffers4atotIaEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf590.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.22% / 新版 98.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1a47c",
      "incomplete_value": false,
      "site": "00b1a490",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a3b4",
      "incomplete_value": false,
      "site": "00b1a3c8",
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
            "const:216:8"
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
      "definition_site": "00b1a4a0",
      "incomplete_value": false,
      "site": "00b1a4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a3d8",
      "incomplete_value": false,
      "site": "00b1a3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1a588",
      "incomplete_value": false,
      "site": "00b1a59c",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a4c0",
      "incomplete_value": false,
      "site": "00b1a4d4",
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
            "const:216:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1a47c",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ],
    [
      "00b1a4a0",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "00b1a588",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1a47c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1a4a0",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1a588",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1a3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a230.md#insn-00b1a3c8) · [`00b1a3f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a230.md#insn-00b1a3f8) · [`00b1a468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a230.md#insn-00b1a468)
- 新版 [`00b1a490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md#insn-00b1a490) · [`00b1a4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md#insn-00b1a4c0) · [`00b1a530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md#insn-00b1a530)

~~~diff
- 00b1a3c8 ["INT_ADD", "register:40f0:8", ["const:b1a3c8:8", "const:4:8"]]
- 00b1a3c8 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1a490 ["INT_ADD", "register:40f0:8", ["const:b1a490:8", "const:4:8"]]
+ 00b1a490 ["CALL", null, ["callee:00bdc130:8"]]
- 00b1a3c8 bytes 2e070394
+ 00b1a490 bytes 28070394
- 00b1a3f8 ["INT_ADD", "register:40f0:8", ["const:b1a3f8:8", "const:4:8"]]
- 00b1a3f8 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1a4c0 ["INT_ADD", "register:40f0:8", ["const:b1a4c0:8", "const:4:8"]]
+ 00b1a4c0 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1a3f8 bytes 0e030394
+ 00b1a4c0 bytes 08030394
- 00b1a468 ["INT_ADD", "register:40f0:8", ["const:b1a468:8", "const:4:8"]]
- 00b1a468 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b1a530 ["INT_ADD", "register:40f0:8", ["const:b1a530:8", "const:4:8"]]
+ 00b1a530 ["CALL", null, ["callee:00bdb010:8"]]
- 00b1a468 bytes be020394
+ 00b1a530 bytes b8020394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f5e4dc6838ab1b996910c90d0bacba0"></a>

### [`00b1a770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a770.md) → [`00b1a838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md) _ZN11flatbuffers4atotIsEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf610.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6c0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.22% / 新版 98.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1a9bc",
      "incomplete_value": false,
      "site": "00b1a9d0",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a8f4",
      "incomplete_value": false,
      "site": "00b1a908",
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
            "const:216:8"
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
      "definition_site": "00b1a9e0",
      "incomplete_value": false,
      "site": "00b1aa00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a918",
      "incomplete_value": false,
      "site": "00b1a938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1aac8",
      "incomplete_value": false,
      "site": "00b1aadc",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1aa00",
      "incomplete_value": false,
      "site": "00b1aa14",
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
            "const:216:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1a9bc",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ],
    [
      "00b1a9e0",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "00b1aac8",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1a9bc",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1a9e0",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1aac8",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1a908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a770.md#insn-00b1a908) · [`00b1a938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a770.md#insn-00b1a938) · [`00b1a9a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1a770.md#insn-00b1a9a8)
- 新版 [`00b1a9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md#insn-00b1a9d0) · [`00b1aa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md#insn-00b1aa00) · [`00b1aa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md#insn-00b1aa70)

~~~diff
- 00b1a908 ["INT_ADD", "register:40f0:8", ["const:b1a908:8", "const:4:8"]]
- 00b1a908 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1a9d0 ["INT_ADD", "register:40f0:8", ["const:b1a9d0:8", "const:4:8"]]
+ 00b1a9d0 ["CALL", null, ["callee:00bdc130:8"]]
- 00b1a908 bytes de050394
+ 00b1a9d0 bytes d8050394
- 00b1a938 ["INT_ADD", "register:40f0:8", ["const:b1a938:8", "const:4:8"]]
- 00b1a938 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1aa00 ["INT_ADD", "register:40f0:8", ["const:b1aa00:8", "const:4:8"]]
+ 00b1aa00 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1a938 bytes be010394
+ 00b1aa00 bytes b8010394
- 00b1a9a8 ["INT_ADD", "register:40f0:8", ["const:b1a9a8:8", "const:4:8"]]
- 00b1a9a8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b1aa70 ["INT_ADD", "register:40f0:8", ["const:b1aa70:8", "const:4:8"]]
+ 00b1aa70 ["CALL", null, ["callee:00bdb010:8"]]
- 00b1a9a8 bytes 6e010394
+ 00b1aa70 bytes 68010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1994dc8ef3033df513774bf2ad84b9aa"></a>

### [`00b1abd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1abd4.md) → [`00b1ac9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md) _ZN11flatbuffers4atotItEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf620.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6d0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.34% / 新版 78.34%

CFGの説明率　旧版 45.65% / 新版 47.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ad80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1ada8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1ad98",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1ae5c"
      ]
    ],
    [
      "00b1add8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1ad50"
      ]
    ],
    [
      "unmatched:00b1ad4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb160"
      ]
    ]
  ],
  "added": [
    [
      "00b1ad98",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1af24"
      ]
    ],
    [
      "00b1add8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1ae18"
      ]
    ],
    [
      "00b1ae14",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb160"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1acb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1abd4.md#insn-00b1acb8) · [`00b1ace4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1abd4.md#insn-00b1ace4) · [`00b1acec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1a/00b1abd4.md#insn-00b1acec)
- 新版 [`00b1ad80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md#insn-00b1ad80) · [`00b1adac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md#insn-00b1adac) · [`00b1adb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md#insn-00b1adb4)

~~~diff
- 00b1acb8 ["CBRANCH", null, ["local:b39:8", "register:102:1"]]
+ 00b1ad80 ["CBRANCH", null, ["local:b37:8", "register:102:1"]]
- 00b1acb8 bytes a20b0054
+ 00b1ad80 bytes a20b0054
- 00b1ace4 ["INT_ADD", "register:40f0:8", ["const:b1ace4:8", "const:4:8"]]
- 00b1ace4 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b1adac ["INT_ADD", "register:40f0:8", ["const:b1adac:8", "const:4:8"]]
+ 00b1adac ["CALL", null, ["callee:00bdb140:8"]]
- 00b1ace4 bytes eb000394
+ 00b1adac bytes e5000394
- 00b1acec ["CBRANCH", null, ["local:b61:8", "register:102:1"]]
+ 00b1adb4 ["CBRANCH", null, ["local:b58:8", "register:102:1"]]
- 00b1acec bytes c2190054
+ 00b1adb4 bytes c2190054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d13a6cc6979ed0975f01a382977b6958"></a>

### [`00b1b158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b158.md) → [`00b1b220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md) _ZN11flatbuffers4atotIiEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5d0.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf680.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.32% / 新版 89.32%

CFGの説明率　旧版 68.13% / 新版 68.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b4b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b4b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1b32c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1b3e4"
      ]
    ],
    [
      "00b1b3a4",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ],
    [
      "00b1b3c8",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1b32c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1b4ac"
      ]
    ],
    [
      "00b1b3a4",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1b3c8",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1b2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b158.md#insn-00b1b2f0) · [`00b1b320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b158.md#insn-00b1b320) · [`00b1b390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b158.md#insn-00b1b390)
- 新版 [`00b1b3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md#insn-00b1b3b8) · [`00b1b3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md#insn-00b1b3e8) · [`00b1b458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md#insn-00b1b458)

~~~diff
- 00b1b2f0 ["INT_ADD", "register:40f0:8", ["const:b1b2f0:8", "const:4:8"]]
- 00b1b2f0 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1b3b8 ["INT_ADD", "register:40f0:8", ["const:b1b3b8:8", "const:4:8"]]
+ 00b1b3b8 ["CALL", null, ["callee:00bdc130:8"]]
- 00b1b2f0 bytes 64030394
+ 00b1b3b8 bytes 5e030394
- 00b1b320 ["INT_ADD", "register:40f0:8", ["const:b1b320:8", "const:4:8"]]
- 00b1b320 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1b3e8 ["INT_ADD", "register:40f0:8", ["const:b1b3e8:8", "const:4:8"]]
+ 00b1b3e8 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1b320 bytes 44ff0294
+ 00b1b3e8 bytes 3eff0294
- 00b1b390 ["INT_ADD", "register:40f0:8", ["const:b1b390:8", "const:4:8"]]
- 00b1b390 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b1b458 ["INT_ADD", "register:40f0:8", ["const:b1b458:8", "const:4:8"]]
+ 00b1b458 ["CALL", null, ["callee:00bdb010:8"]]
- 00b1b390 bytes f4fe0294
+ 00b1b458 bytes eefe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f069a31f91f43883b6925cbae95390b"></a>

### [`00b1b5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b5bc.md) → [`00b1b684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b684.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIiEEjT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf370.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf420.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 75.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b624"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b1b6ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b1b610",
      "incomplete_value": true,
      "site": "00b1b618",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b1b618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b5bc.md#insn-00b1b618) · [`00b1b624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b5bc.md#insn-00b1b624) · [`00b1b6a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b5bc.md#insn-00b1b6a4)
- 新版 [`00b1b6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b684.md#insn-00b1b6e0)

~~~diff
- 00b1b618 ["INT_ADD", "register:40f0:8", ["const:b1b618:8", "const:4:8"]]
- 00b1b618 ["CALL", null, ["callee:00bdf340:8"]]
+ 00b1b6e0 ["INT_ADD", "register:40f0:8", ["const:b1b6e0:8", "const:4:8"]]
+ 00b1b6e0 ["CALL", null, ["callee:00bdf340:8"]]
- 00b1b618 bytes 1e0f0394
+ 00b1b6e0 bytes 180f0394
- 00b1b624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00b1b624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1b624 bytes 681a00f9
- 00b1b6a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b1b6a4 ["RETURN", null, ["register:0:8"]]
- 00b1b6a4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e43e8ea08dfefe9d42f9246c9328bc2f"></a>

### [`00b1b6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b6a8.md) → [`00b1b770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b770.md) _ZN11flatbuffers17FlatBufferBuilder11PushElementIjEEjT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf380.md) · 呼出先 1件 [`00bdf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf290.md)
- 新版 呼出元 1件 [`00bdf430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf430.md) · 呼出先 1件 [`00bdf340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf340.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 38.10% / 新版 34.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b6a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b6ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b6ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1b6a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1b6ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1b6b0",
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
      "00b1b770",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b1b774",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b1b778",
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

- 旧版 [`00b1b6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b6a8.md#insn-00b1b6a8) · [`00b1b6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b6a8.md#insn-00b1b6ac) · [`00b1b6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b6a8.md#insn-00b1b6b0)

~~~diff
- 00b1b6a8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b1b6a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b1b6a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b1b6a8 bytes f50f1df8
- 00b1b6ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b1b6ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b1b6ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b1b6ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1b6ac bytes f44f01a9
- 00b1b6b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b1b6b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b1b6b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b1b6b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1b6b0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22781d3e9ba36dfdeed14cea4f1e55cb"></a>

### [`00b1b794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b794.md) → [`00b1b85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md) _ZN11flatbuffers4atotIlEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5f0.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6a0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.90% / 新版 62.90%

CFGの説明率　旧版 15.46% / 新版 17.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 4件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b798"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1b79c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1b798",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1b79c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1b7a0",
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
      "00b1b860",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b1b864",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b1b868",
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

- 旧版 [`00b1b798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b794.md#insn-00b1b798) · [`00b1b79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b794.md#insn-00b1b79c) · [`00b1b7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1b794.md#insn-00b1b7a0)

~~~diff
- 00b1b798 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1b798 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1b798 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b1b798 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1b798 bytes fc670da9
- 00b1b79c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1b79c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1b79c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b1b79c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1b79c bytes f85f0ea9
- 00b1b7a0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b1b7a0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b1b7a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b1b7a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1b7a0 bytes f6570fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e64fc56321df25ff6da0ea54c7aa05ef"></a>

### [`00b1bc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bc60.md) → [`00b1bd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md) _ZN11flatbuffers4atotImEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf600.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6b0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1be48",
      "incomplete_value": false,
      "site": "00b1be5c",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1bd80",
      "incomplete_value": false,
      "site": "00b1bd94",
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
            "const:216:8"
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
      "definition_site": "00b1be6c",
      "incomplete_value": false,
      "site": "00b1be8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1bda4",
      "incomplete_value": false,
      "site": "00b1bdc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1be9c",
      "incomplete_value": false,
      "site": "00b1beb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:492:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1bdd4",
      "incomplete_value": false,
      "site": "00b1bdf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:405:8"
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
      "00b1be48",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ],
    [
      "00b1be6c",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ],
    [
      "00b1be9c",
      "PARAM",
      [
        "storage",
        "00292405",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1be48",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1be6c",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1be9c",
      "PARAM",
      [
        "storage",
        "00292492",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1bd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bc60.md#insn-00b1bd94) · [`00b1bdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bc60.md#insn-00b1bdc4) · [`00b1bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1b/00b1bc60.md#insn-00b1bdf0)
- 新版 [`00b1be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md#insn-00b1be5c) · [`00b1be8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md#insn-00b1be8c) · [`00b1beb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md#insn-00b1beb8)

~~~diff
- 00b1bd94 ["INT_ADD", "register:40f0:8", ["const:b1bd94:8", "const:4:8"]]
- 00b1bd94 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1be5c ["INT_ADD", "register:40f0:8", ["const:b1be5c:8", "const:4:8"]]
+ 00b1be5c ["CALL", null, ["callee:00bdc130:8"]]
- 00b1bd94 bytes bb000394
+ 00b1be5c bytes b5000394
- 00b1bdc4 ["INT_ADD", "register:40f0:8", ["const:b1bdc4:8", "const:4:8"]]
- 00b1bdc4 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1be8c ["INT_ADD", "register:40f0:8", ["const:b1be8c:8", "const:4:8"]]
+ 00b1be8c ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1bdc4 bytes 9bfc0294
+ 00b1be8c bytes 95fc0294
- 00b1bdf0 ["INT_ADD", "register:40f0:8", ["const:b1bdf0:8", "const:4:8"]]
- 00b1bdf0 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1beb8 ["INT_ADD", "register:40f0:8", ["const:b1beb8:8", "const:4:8"]]
+ 00b1beb8 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1bdf0 bytes 90fc0294
+ 00b1beb8 bytes 8afc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-362ffe49d8513e15262b1fbb1452102a"></a>

### [`00b1c17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c17c.md) → [`00b1c244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md) _ZN11flatbuffers4atotIfEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5b0.md) · 呼出先 11件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1c318",
      "incomplete_value": false,
      "site": "00b1c32c",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c250",
      "incomplete_value": false,
      "site": "00b1c264",
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
            "const:216:8"
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
      "definition_site": "00b1c33c",
      "incomplete_value": false,
      "site": "00b1c35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c274",
      "incomplete_value": false,
      "site": "00b1c294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1c318",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ],
    [
      "00b1c33c",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1c318",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1c33c",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1c264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c17c.md#insn-00b1c264) · [`00b1c294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c17c.md#insn-00b1c294) · [`00b1c35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c17c.md#insn-00b1c35c)
- 新版 [`00b1c32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md#insn-00b1c32c) · [`00b1c35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md#insn-00b1c35c) · [`00b1c424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md#insn-00b1c424)

~~~diff
- 00b1c264 ["INT_ADD", "register:40f0:8", ["const:b1c264:8", "const:4:8"]]
- 00b1c264 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1c32c ["INT_ADD", "register:40f0:8", ["const:b1c32c:8", "const:4:8"]]
+ 00b1c32c ["CALL", null, ["callee:00bdc130:8"]]
- 00b1c264 bytes 87ff0294
+ 00b1c32c bytes 81ff0294
- 00b1c294 ["INT_ADD", "register:40f0:8", ["const:b1c294:8", "const:4:8"]]
- 00b1c294 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1c35c ["INT_ADD", "register:40f0:8", ["const:b1c35c:8", "const:4:8"]]
+ 00b1c35c ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1c294 bytes 67fb0294
+ 00b1c35c bytes 61fb0294
- 00b1c35c ["INT_ADD", "register:40f0:8", ["const:b1c35c:8", "const:4:8"]]
- 00b1c35c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b1c424 ["INT_ADD", "register:40f0:8", ["const:b1c424:8", "const:4:8"]]
+ 00b1c424 ["CALL", null, ["callee:00bdb040:8"]]
- 00b1c35c bytes 0dfb0294
+ 00b1c424 bytes 07fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75a8bc20aaebdf50dc1cf5a1b0858ab6"></a>

### [`00b1c450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c450.md) → [`00b1c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md) _ZN11flatbuffers4atotIdEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf5a0.md) · 呼出先 11件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf650.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1c5e8",
      "incomplete_value": false,
      "site": "00b1c5fc",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c520",
      "incomplete_value": false,
      "site": "00b1c534",
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
            "const:216:8"
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
      "definition_site": "00b1c60c",
      "incomplete_value": false,
      "site": "00b1c62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c544",
      "incomplete_value": false,
      "site": "00b1c564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:39b:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1c5e8",
      "PARAM",
      [
        "storage",
        "002a6216",
        null,
        "string"
      ]
    ],
    [
      "00b1c60c",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1c5e8",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1c60c",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1c534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c450.md#insn-00b1c534) · [`00b1c564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c450.md#insn-00b1c564) · [`00b1c62c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1c450.md#insn-00b1c62c)
- 新版 [`00b1c5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md#insn-00b1c5fc) · [`00b1c62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md#insn-00b1c62c) · [`00b1c6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md#insn-00b1c6f4)

~~~diff
- 00b1c534 ["INT_ADD", "register:40f0:8", ["const:b1c534:8", "const:4:8"]]
- 00b1c534 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1c5fc ["INT_ADD", "register:40f0:8", ["const:b1c5fc:8", "const:4:8"]]
+ 00b1c5fc ["CALL", null, ["callee:00bdc130:8"]]
- 00b1c534 bytes d3fe0294
+ 00b1c5fc bytes cdfe0294
- 00b1c564 ["INT_ADD", "register:40f0:8", ["const:b1c564:8", "const:4:8"]]
- 00b1c564 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b1c62c ["INT_ADD", "register:40f0:8", ["const:b1c62c:8", "const:4:8"]]
+ 00b1c62c ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b1c564 bytes b3fa0294
+ 00b1c62c bytes adfa0294
- 00b1c62c ["INT_ADD", "register:40f0:8", ["const:b1c62c:8", "const:4:8"]]
- 00b1c62c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b1c6f4 ["INT_ADD", "register:40f0:8", ["const:b1c6f4:8", "const:4:8"]]
+ 00b1c6f4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b1c62c bytes 59fa0294
+ 00b1c6f4 bytes 53fa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-382fed6155fdd4c0f28e40e8b31da3ea"></a>

### [`00b1cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md) → [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) FUN_00b1cd10

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md) · 呼出先 2件 [`00b1cc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md) [`00b40e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40e90.md)
- 新版 呼出元 2件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) · 呼出先 2件 [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) [`00b40f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1cda0",
      "incomplete_value": true,
      "site": "00b1cda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ccd8",
      "incomplete_value": true,
      "site": "00b1cce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1cda4",
      "incomplete_value": true,
      "site": "00b1cda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ccdc",
      "incomplete_value": true,
      "site": "00b1cce0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1cd9c",
      "incomplete_value": true,
      "site": "00b1cda8",
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
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ccd4",
      "incomplete_value": true,
      "site": "00b1cce0",
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
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1cd98",
      "READ",
      [
        "storage",
        "010a0e14",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cd9c",
      "READ",
      [
        "storage",
        "010a0e20",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b1cd98",
      "READ",
      [
        "storage",
        "010a0ed4",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cd9c",
      "READ",
      [
        "storage",
        "010a0ee0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1cce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md#insn-00b1cce0) · [`00b1cc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md#insn-00b1cc9c) · [`00b1ccd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cc48.md#insn-00b1ccd0)
- 新版 [`00b1cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md#insn-00b1cda8) · [`00b1cd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md#insn-00b1cd64) · [`00b1cd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md#insn-00b1cd98)

~~~diff
- 00b1cce0 ["INT_ADD", "register:40f0:8", ["const:b1cce0:8", "const:4:8"]]
- 00b1cce0 ["CALL", null, ["callee:00b40f58:8"]]
+ 00b1cda8 ["INT_ADD", "register:40f0:8", ["const:b1cda8:8", "const:4:8"]]
+ 00b1cda8 ["CALL", null, ["callee:00b40f58:8"]]
- 00b1cce0 bytes 6c900094
+ 00b1cda8 bytes 6c900094
- 00b1cc9c ["INT_ADD", "register:40f0:8", ["const:b1cc9c:8", "const:4:8"]]
- 00b1cc9c ["CALL", null, ["local:b0:8"]]
+ 00b1cd64 ["INT_ADD", "register:40f0:8", ["const:b1cd64:8", "const:4:8"]]
+ 00b1cd64 ["CALL", null, ["local:b0:8"]]
- 00b1cc9c bytes ebffff97
+ 00b1cd64 bytes ebffff97
- 00b1ccd0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e14:8"]]
- 00b1ccd0 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
- 00b1ccd0 ["INT_ZEXT", "register:4040:8", ["tmp:1:2"]]
+ 00b1cd98 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ed4:8"]]
+ 00b1cd98 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
+ 00b1cd98 ["INT_ZEXT", "register:4040:8", ["tmp:1:2"]]
- 00b1ccd0 bytes 082b5c79
+ 00b1cd98 bytes 08ab5d79
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc6b62fafaffef02546f68a893296e09"></a>

### [`00b1cd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md) → [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) FUN_00b1ce44

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b18c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b18/00b18c10.md) [`00b1cd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md) · 呼出先 2件 [`00b1cd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md) [`00b40e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b40/00b40e90.md)
- 新版 呼出元 2件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) · 呼出先 2件 [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) [`00b40f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1cf48",
      "incomplete_value": true,
      "site": "00b1cf4c",
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
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ce80",
      "incomplete_value": true,
      "site": "00b1ce84",
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
              "INT_ADD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1ced0",
      "READ",
      [
        "storage",
        "010a0e14",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cf48",
      "READ",
      [
        "storage",
        "010a0e20",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b1ced0",
      "READ",
      [
        "storage",
        "010a0ed4",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cf48",
      "READ",
      [
        "storage",
        "010a0ee0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1ce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md#insn-00b1ce84) · [`00b1cde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md#insn-00b1cde8) · [`00b1ce08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cd7c.md#insn-00b1ce08)
- 新版 [`00b1cf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md#insn-00b1cf4c) · [`00b1ceb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md#insn-00b1ceb0) · [`00b1ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md#insn-00b1ced0)

~~~diff
- 00b1ce84 ["INT_ADD", "register:40f0:8", ["const:b1ce84:8", "const:4:8"]]
- 00b1ce84 ["CALL", null, ["callee:00b40f58:8"]]
+ 00b1cf4c ["INT_ADD", "register:40f0:8", ["const:b1cf4c:8", "const:4:8"]]
+ 00b1cf4c ["CALL", null, ["callee:00b40f58:8"]]
- 00b1ce84 bytes 03900094
+ 00b1cf4c bytes 03900094
- 00b1cde8 ["INT_ADD", "register:40f0:8", ["const:b1cde8:8", "const:4:8"]]
- 00b1cde8 ["CALL", null, ["local:b0:8"]]
+ 00b1ceb0 ["INT_ADD", "register:40f0:8", ["const:b1ceb0:8", "const:4:8"]]
+ 00b1ceb0 ["CALL", null, ["local:b0:8"]]
- 00b1cde8 bytes e5ffff97
+ 00b1ceb0 bytes e5ffff97
- 00b1ce08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e14:8"]]
- 00b1ce08 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
- 00b1ce08 ["INT_ZEXT", "register:40c8:8", ["tmp:1:2"]]
+ 00b1ced0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ed4:8"]]
+ 00b1ced0 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
+ 00b1ced0 ["INT_ZEXT", "register:40c8:8", ["tmp:1:2"]]
- 00b1ce08 bytes b92a5c79
+ 00b1ced0 bytes b9aa5d79
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be56e2d0ef88185d1cab504876fffb09"></a>

### [`00b1cedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cedc.md) → [`00b1cfa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md) _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdf850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf850.md) · 呼出先 21件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf900.md) · 呼出先 21件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1d140",
      "incomplete_value": true,
      "site": "00b1d140",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:7b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1d078",
      "incomplete_value": true,
      "site": "00b1d078",
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
                "const:298000:8"
              ],
              [
                "leaf",
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1d134",
      "incomplete_value": true,
      "site": "00b1d160",
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
              [
                "leaf",
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1d06c",
      "incomplete_value": true,
      "site": "00b1d098",
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
              [
                "leaf",
                "const:7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1d1dc",
      "incomplete_value": true,
      "site": "00b1d1f8",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1d114",
      "incomplete_value": true,
      "site": "00b1d130",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:2f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1d130",
      "READ",
      [
        "storage",
        "00298725",
        null,
        "string"
      ]
    ],
    [
      "00b1d134",
      "READ",
      [
        "storage",
        "0029872c",
        null,
        "string"
      ]
    ],
    [
      "00b1d1dc",
      "READ",
      [
        "storage",
        "002ac2f1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1d130",
      "READ",
      [
        "storage",
        "002987b2",
        null,
        "string"
      ]
    ],
    [
      "00b1d134",
      "READ",
      [
        "storage",
        "002987b9",
        null,
        "string"
      ]
    ],
    [
      "00b1d1dc",
      "READ",
      [
        "storage",
        "002ac2e8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1cf3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cedc.md#insn-00b1cf3c) · [`00b1cf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cedc.md#insn-00b1cf60) · [`00b1cfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1c/00b1cedc.md#insn-00b1cfc0)
- 新版 [`00b1d004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md#insn-00b1d004) · [`00b1d028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md#insn-00b1d028) · [`00b1d088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md#insn-00b1d088)

~~~diff
- 00b1cf3c ["INT_ADD", "register:40f0:8", ["const:b1cf3c:8", "const:4:8"]]
- 00b1cf3c ["CALL", null, ["callee:00bdf7b0:8"]]
+ 00b1d004 ["INT_ADD", "register:40f0:8", ["const:b1d004:8", "const:4:8"]]
+ 00b1d004 ["CALL", null, ["callee:00bdf7b0:8"]]
- 00b1cf3c bytes f1090394
+ 00b1d004 bytes eb090394
- 00b1cf60 ["INT_ADD", "register:40f0:8", ["const:b1cf60:8", "const:4:8"]]
- 00b1cf60 ["CALL", null, ["callee:00bdf8b0:8"]]
+ 00b1d028 ["INT_ADD", "register:40f0:8", ["const:b1d028:8", "const:4:8"]]
+ 00b1d028 ["CALL", null, ["callee:00bdf8b0:8"]]
- 00b1cf60 bytes 280a0394
+ 00b1d028 bytes 220a0394
- 00b1cfc0 ["INT_ADD", "register:40f0:8", ["const:b1cfc0:8", "const:4:8"]]
- 00b1cfc0 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b1d088 ["INT_ADD", "register:40f0:8", ["const:b1d088:8", "const:4:8"]]
+ 00b1d088 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b1cfc0 bytes e0f70294
+ 00b1d088 bytes daf70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1a3c3a1baef0db79d186d8e19fceddf"></a>

### [`00b1d748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d748.md) → [`00b1d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md) _ZN11flatbuffers6Parser19ParseEnumFromStringERKNS_4TypeEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf830.md) · 呼出先 12件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8e0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 42.37% / 新版 42.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d9d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d9d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1d7fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1dc70"
      ]
    ],
    [
      "unmatched:00b1d8c8",
      "PARAM",
      [
        "storage",
        "0029de08",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b1d8dc",
      "PARAM",
      [
        "storage",
        "00291545",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1d8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1dc70"
      ]
    ],
    [
      "00b1d990",
      "PARAM",
      [
        "storage",
        "0029de95",
        null,
        "string"
      ]
    ],
    [
      "00b1d9a4",
      "PARAM",
      [
        "storage",
        "00291545",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d748.md#insn-00b1d7fc) · [`00b1d804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1d748.md#insn-00b1d804)
- 新版 [`00b1d8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md#insn-00b1d8cc) · [`00b1d8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md#insn-00b1d8c4)

~~~diff
- 00b1d7fc ["CBRANCH", null, ["local:b65:8", "register:101:1"]]
- 00b1d7fc bytes 601d0054
- 00b1d804 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b1d804 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b1d804 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b1d804 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b1d8cc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b1d8cc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b1d8cc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b1d8cc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b1d804 bytes e8000037
+ 00b1d8cc bytes e8000037
+ 00b1d8c4 ["CBRANCH", null, ["local:b67:8", "register:101:1"]]
+ 00b1d8c4 bytes 601d0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd580ef347988699f69acbef1f0efaa8"></a>

### [`00b1dc64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1dc64.md) → [`00b1dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1dd2c.md) _ZN11flatbuffers11NumToStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0d0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb2b0.md)
- 新版 呼出元 1件 [`00bdf180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf180.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.22% / 新版 52.22%

CFGの説明率　旧版 42.86% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dc68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dc68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1dc6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1dc68",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1dc6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1dc70",
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
      "00b1dd30",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b1dd34",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b1dd38",
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

- 旧版 [`00b1dc68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1dc64.md#insn-00b1dc68) · [`00b1dc6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1dc64.md#insn-00b1dc6c) · [`00b1dc70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1dc64.md#insn-00b1dc70)

~~~diff
- 00b1dc68 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1dc68 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b1dc68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b1dc68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1dc68 bytes fc6f14a9
- 00b1dc6c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1dc6c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1dc6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b1dc6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1dc6c bytes fa6715a9
- 00b1dc70 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1dc70 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1dc70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b1dc70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1dc70 bytes f85f16a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41004b0d913d8d1146f7fb11a25f2f80"></a>

### [`00b1ddcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1ddcc.md) → [`00b1de94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1de94.md) _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0e0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00bdf190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf190.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.64% / 新版 62.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1de38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1de3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1de40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1de00",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1de04",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b1de38",
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
      "00b1dec8",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b1decc",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b1df00",
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

- 旧版 [`00b1de38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1ddcc.md#insn-00b1de38) · [`00b1de3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1ddcc.md#insn-00b1de3c) · [`00b1de40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1ddcc.md#insn-00b1de40)

~~~diff
- 00b1de38 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b1de38 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b1de38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1de38 bytes a9031af8
- 00b1de3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00b1de3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1de3c bytes e84b00f9
- 00b1de40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b1de40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b1de40 bytes fb1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70fb17a07ca4891f646ee9c404f07261"></a>

### [`00b1df38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1df38.md) → [`00b1e000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e000.md) _ZN11flatbuffers11NumToStringItEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf0f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf0f0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb260.md) [`00bdb290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb290.md) [`00bdb340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb340.md)
- 新版 呼出元 1件 [`00bdf1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1a0.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1df3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1df3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1df40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1df3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1df40",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1df44",
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
      "00b1e004",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b1e008",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b1e00c",
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

- 旧版 [`00b1df3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1df38.md#insn-00b1df3c) · [`00b1df40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1df38.md#insn-00b1df40) · [`00b1df44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1d/00b1df38.md#insn-00b1df44)

~~~diff
- 00b1df3c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1df3c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b1df3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b1df3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1df3c bytes fc6f14a9
- 00b1df40 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1df40 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1df40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b1df40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1df40 bytes fa6715a9
- 00b1df44 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1df44 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1df44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b1df44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1df44 bytes f85f16a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6f5dab5a0bf0eb4551bbf2638087da6"></a>

### [`00b1e0a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e0a4.md) → [`00b1e16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md) _ZN11flatbuffers6Parser10TokenErrorEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf670.md) · 呼出先 10件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bdf720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf720.md) · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.93% / 新版 94.93%

CFGの説明率　旧版 80.00% / 新版 76.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b1e36c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1e238",
      "incomplete_value": true,
      "site": "00b1e23c",
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
      "definition_site": "00b1e170",
      "incomplete_value": true,
      "site": "00b1e174",
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
      "00b1e22c",
      "DATA",
      [
        "storage",
        "00c10dd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00b1e2dc",
      "PARAM",
      [
        "storage",
        "0029ffc4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b1e2a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1e38c"
      ]
    ]
  ],
  "added": [
    [
      "00b1e22c",
      "DATA",
      [
        "storage",
        "00c10e80",
        null,
        "undefined *"
      ]
    ],
    [
      "00b1e2dc",
      "PARAM",
      [
        "storage",
        "002a0051",
        null,
        "string"
      ]
    ],
    [
      "00b1e36c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1e38c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e0a4.md#insn-00b1e174) · [`00b1e224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e0a4.md#insn-00b1e224) · [`00b1e2a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e0a4.md#insn-00b1e2a4)
- 新版 [`00b1e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md#insn-00b1e23c) · [`00b1e2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md#insn-00b1e2ec)

~~~diff
- 00b1e174 ["INT_ADD", "register:40f0:8", ["const:b1e174:8", "const:4:8"]]
- 00b1e174 ["CALL", null, ["callee:00bdb140:8"]]
+ 00b1e23c ["INT_ADD", "register:40f0:8", ["const:b1e23c:8", "const:4:8"]]
+ 00b1e23c ["CALL", null, ["callee:00bdb140:8"]]
- 00b1e174 bytes c7f30294
+ 00b1e23c bytes c1f30294
- 00b1e224 ["INT_ADD", "register:40f0:8", ["const:b1e224:8", "const:4:8"]]
- 00b1e224 ["CALL", null, ["callee:00bdc130:8"]]
+ 00b1e2ec ["INT_ADD", "register:40f0:8", ["const:b1e2ec:8", "const:4:8"]]
+ 00b1e2ec ["CALL", null, ["callee:00bdc130:8"]]
- 00b1e224 bytes 97f70294
+ 00b1e2ec bytes 91f70294
- 00b1e2a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b1e2a4 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00b1e2a4 bytes 01010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d9521151dda43a8b98090fec73baeb4"></a>

### [`00b1e2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e2cc.md) → [`00b1e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md) _ZN11flatbuffers6Parser13ParseFunctionEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf710.md) · 呼出先 23件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00bdf7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7c0.md) · 呼出先 23件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.23% / 新版 77.23%

CFGの説明率　旧版 38.73% / 新版 39.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e378"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1e378",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1e400",
      "PARAM",
      [
        "storage",
        "002a0eaa",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b1e414",
      "PARAM",
      [
        "storage",
        "0029de01",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1e440",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00b1e4c8",
      "PARAM",
      [
        "storage",
        "002a0f37",
        null,
        "string"
      ]
    ],
    [
      "00b1e4dc",
      "PARAM",
      [
        "storage",
        "0029de8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e2cc.md#insn-00b1e36c) · [`00b1e378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e2cc.md#insn-00b1e378) · [`00b1e3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1e2cc.md#insn-00b1e3d8)
- 新版 [`00b1e434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md#insn-00b1e434) · [`00b1e4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md#insn-00b1e4a0)

~~~diff
- 00b1e36c ["INT_ADD", "register:40f0:8", ["const:b1e36c:8", "const:4:8"]]
- 00b1e36c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b1e434 ["INT_ADD", "register:40f0:8", ["const:b1e434:8", "const:4:8"]]
+ 00b1e434 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b1e36c bytes f5f20294
+ 00b1e434 bytes eff20294
- 00b1e378 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b1e378 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1e378 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffff70:8"]]
- 00b1e378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1e378 bytes a85f37a9
- 00b1e3d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b1e3d8 ["CBRANCH", null, ["local:b56:8", "tmp:0:1"]]
+ 00b1e4a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b1e4a0 ["CBRANCH", null, ["local:b57:8", "tmp:0:1"]]
- 00b1e3d8 bytes 281a0035
+ 00b1e4a0 bytes 281a0035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-549e42e0243c0b7223689fee1fb6b917"></a>

### [`00b1ec9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1ec9c.md) → [`00b1ed64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1ed64.md) _ZN11flatbuffers6Parser13TryTypedValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEibRNS_5ValueENS_8BaseTypeEPb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf740.md) · 呼出先 11件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bdf7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7f0.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.24% / 新版 84.24%

CFGの説明率　旧版 53.59% / 新版 56.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 28件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1eca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1eca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1eca4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1eca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1eca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1eca8",
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
      "00b1ed68",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b1ed6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b1ed70",
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

- 旧版 [`00b1eca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1ec9c.md#insn-00b1eca0) · [`00b1eca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1ec9c.md#insn-00b1eca4) · [`00b1eca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1e/00b1ec9c.md#insn-00b1eca8)

~~~diff
- 00b1eca0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1eca0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b1eca0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00b1eca0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1eca0 bytes fc6f14a9
- 00b1eca4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1eca4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1eca4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 00b1eca4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1eca4 bytes fa6715a9
- 00b1eca8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b1eca8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b1eca8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b1eca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1eca8 bytes f85f16a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f32806521c24706a4eeaaa5198df5b0"></a>

### [`00b1f2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f2a8.md) → [`00b1f370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f370.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf170.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bdf220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf220.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 63.89% / 新版 65.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f32c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f3f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b1f3f4"
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
      "unmatched:00b1f32c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f4cc"
      ]
    ],
    [
      "unmatched:00b1f3f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f4d4"
      ]
    ]
  ],
  "added": [
    [
      "00b1f3f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f4cc"
      ]
    ],
    [
      "00b1f4bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f4d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1f32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f2a8.md#insn-00b1f32c) · [`00b1f3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f2a8.md#insn-00b1f3f4)
- 新版 [`00b1f3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f370.md#insn-00b1f3f4)

~~~diff
- 00b1f32c ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00b1f32c ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00b1f32c bytes db0600b4
- 00b1f3f4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b1f3f4 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00b1f3f4 bytes c80000b4
+ 00b1f3f4 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
+ 00b1f3f4 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00b1f3f4 bytes db0600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da36df99a32651b318eae37a4a2433f"></a>

### [`00b1f738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f738.md) → [`00b1f800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f800.md) _ZN11flatbuffers6Parser9ParseEnumEbPPNS_7EnumDefE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdf900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf900.md) · 呼出先 28件 [`00b41724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b41/00b41724.md) [`00b42118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b42/00b42118.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bdf9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9b0.md) · 呼出先 28件 [`00b417ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b417ec.md) [`00b421e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b421e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.25% / 新版 87.25%

CFGの説明率　旧版 63.33% / 新版 63.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 8件, `store_value` 9件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 53件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f740"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1f73c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1f740",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1f744",
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
      "00b1f804",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00b1f808",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b1f80c",
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

- 旧版 [`00b1f73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f738.md#insn-00b1f73c) · [`00b1f740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f738.md#insn-00b1f740) · [`00b1f744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b1f/00b1f738.md#insn-00b1f744)

~~~diff
- 00b1f73c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:150:8"]]
- 00b1f73c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:8"]]
- 00b1f73c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:8:8"]]
- 00b1f73c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5100:8"]]
- 00b1f73c bytes e923156d
- 00b1f740 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b1f740 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b1f740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 00b1f740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1f740 bytes fc6f16a9
- 00b1f744 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b1f744 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b1f744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 00b1f744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1f744 bytes fa6717a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ffbd2076dfc91cea987944dc7a6f5af"></a>

### [`00b207e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b207e4.md) → [`00b208ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md) _ZN11flatbuffers6Parser9StartEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbPPNS_7EnumDefE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf940.md) · 呼出先 9件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bdf9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9f0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.24% / 新版 99.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b20a10",
      "incomplete_value": false,
      "site": "00b20a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:f7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b20948",
      "incomplete_value": false,
      "site": "00b20954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:eef:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b20a10",
      "PARAM",
      [
        "storage",
        "0029ceef",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b20a10",
      "PARAM",
      [
        "storage",
        "0029cf7c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b20954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b207e4.md#insn-00b20954) · [`00b20824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b207e4.md#insn-00b20824) · [`00b208ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b207e4.md#insn-00b208ac)
- 新版 [`00b20a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md#insn-00b20a1c) · [`00b208ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md#insn-00b208ec) · [`00b20974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md#insn-00b20974)

~~~diff
- 00b20954 ["INT_ADD", "register:40f0:8", ["const:b20954:8", "const:4:8"]]
- 00b20954 ["CALL", null, ["callee:00bdb210:8"]]
+ 00b20a1c ["INT_ADD", "register:40f0:8", ["const:b20a1c:8", "const:4:8"]]
+ 00b20a1c ["CALL", null, ["callee:00bdb210:8"]]
- 00b20954 bytes 03ea0294
+ 00b20a1c bytes fde90294
- 00b20824 ["INT_ADD", "register:40f0:8", ["const:b20824:8", "const:4:8"]]
- 00b20824 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b208ec ["INT_ADD", "register:40f0:8", ["const:b208ec:8", "const:4:8"]]
+ 00b208ec ["CALL", null, ["callee:00bdaff0:8"]]
- 00b20824 bytes c7e90294
+ 00b208ec bytes c1e90294
- 00b208ac ["INT_ADD", "register:40f0:8", ["const:b208ac:8", "const:4:8"]]
- 00b208ac ["CALL", null, ["callee:00bde1e0:8"]]
+ 00b20974 ["INT_ADD", "register:40f0:8", ["const:b20974:8", "const:4:8"]]
+ 00b20974 ["CALL", null, ["callee:00bde1e0:8"]]
- 00b208ac bytes 21f60294
+ 00b20974 bytes 1bf60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a69e62d8ac6c4ec6e76eff1e442a2004"></a>

### [`00b20aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20aec.md) → [`00b20bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md) _ZN11flatbuffers14EnumValBuilder21AssignEnumeratorValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdf280.md) · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf330.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b20cac",
      "incomplete_value": false,
      "site": "00b20cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:394:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b20be4",
      "incomplete_value": false,
      "site": "00b20bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:39b:8"
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
      "00b20cac",
      "PARAM",
      [
        "storage",
        "002a539b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b20cac",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b20bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20aec.md#insn-00b20bf4) · [`00b20b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20aec.md#insn-00b20b54) · [`00b20ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b20/00b20aec.md#insn-00b20ba8)
- 新版 [`00b20cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md#insn-00b20cbc) · [`00b20c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md#insn-00b20c1c) · [`00b20c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md#insn-00b20c70)

~~~diff
- 00b20bf4 ["INT_ADD", "register:40f0:8", ["const:b20bf4:8", "const:4:8"]]
- 00b20bf4 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00b20cbc ["INT_ADD", "register:40f0:8", ["const:b20cbc:8", "const:4:8"]]
+ 00b20cbc ["CALL", null, ["callee:00bdb0e0:8"]]
- 00b20bf4 bytes 0fe90294
+ 00b20cbc bytes 09e90294
- 00b20b54 ["INT_ADD", "register:40f0:8", ["const:b20b54:8", "const:4:8"]]
- 00b20b54 ["CALL", null, ["callee:00bdf5a0:8"]]
+ 00b20c1c ["INT_ADD", "register:40f0:8", ["const:b20c1c:8", "const:4:8"]]
+ 00b20c1c ["CALL", null, ["callee:00bdf5a0:8"]]
- 00b20b54 bytes 67fa0294
+ 00b20c1c bytes 61fa0294
- 00b20ba8 ["INT_ADD", "register:40f0:8", ["const:b20ba8:8", "const:4:8"]]
- 00b20ba8 ["CALL", null, ["callee:00bdf590:8"]]
+ 00b20c70 ["INT_ADD", "register:40f0:8", ["const:b20c70:8", "const:4:8"]]
+ 00b20c70 ["CALL", null, ["callee:00bdf590:8"]]
- 00b20ba8 bytes 4efa0294
+ 00b20c70 bytes 48fa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

