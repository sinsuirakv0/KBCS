# v15.7.2 → v15.7.3 · 最優先の変更候補 (59)

[一覧の目次](README.md)

<a id="compare-b89cbd9555ff1d69f74bc75a473f7b33"></a>

### [`00ae6750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6750.md) → [`00ae6818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6818.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 11.11% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6754"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6750",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6754",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6758",
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
      "00ae6818",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae681c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6820",
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

- 旧版 [`00ae6750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6750.md#insn-00ae6750) · [`00ae6754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6750.md#insn-00ae6754) · [`00ae6758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6750.md#insn-00ae6758)

~~~diff
- 00ae6750 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae6750 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae6750 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6750 bytes f50f1df8
- 00ae6754 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae6754 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae6754 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6754 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6754 bytes f44f01a9
- 00ae6758 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6758 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6758 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae6758 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6758 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64536822a5a851b44ff914613f7ee305"></a>

### [`00ae67ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae67ec.md) → [`00ae68b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae68b4.md) _ZN8firebase4util18file_output_stream12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 7.14% / 新版 9.09%

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
      "site": "00ae6828"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6878"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae68f0"
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
      "00ae68c8",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae68d4",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae6828",
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
      "00ae68c8",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae68d4",
      "READ",
      [
        "storage",
        "010a0458",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae68f0",
      "WRITE",
      [
        "storage",
        "010a0458",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae67ec.md#insn-00ae6804) · [`00ae6824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae67ec.md#insn-00ae6824) · [`00ae6828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae67ec.md#insn-00ae6828)
- 新版 `00ae68cc`（命令位置の公開資料なし）

~~~diff
- 00ae6804 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6804 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00ae68cc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae68cc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae6804 bytes c10300b4
+ 00ae68cc bytes c10300b4
- 00ae6824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6824 ["INT_ADD", "register:40f0:8", ["const:ae6824:8", "const:4:8"]]
- 00ae6824 ["CALLIND", null, ["register:0:8"]]
- 00ae6824 bytes 00013fd6
- 00ae6828 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6828 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6828 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:398:8"]]
- 00ae6828 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6828 bytes bf620e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e9fd7f07e944f99b68594c96ab6db8"></a>

### [`00ae688c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae688c.md) → [`00ae6954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6954.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae688c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae688c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae688c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6890",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae68a0",
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
      "00ae6954",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6958",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6968",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae688c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae688c.md#insn-00ae688c) · [`00ae6890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae688c.md#insn-00ae6890) · [`00ae68a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae688c.md#insn-00ae68a8)

~~~diff
- 00ae688c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae688c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae688c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae688c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae688c bytes f44fbea9
- 00ae6890 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6890 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6890 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6890 bytes fd7b01a9
- 00ae68a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae68a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae68a8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97b3d8373e90337627c3417492af8341"></a>

### [`00ae68fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae68fc.md) → [`00ae69c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae69c4.md) _ZN8firebase4util18file_output_stream11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae69e0",
      "incomplete_value": false,
      "site": "00ae69e4",
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
      "definition_site": "00ae6918",
      "incomplete_value": false,
      "site": "00ae691c",
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
      "definition_site": "00ae69f0",
      "incomplete_value": true,
      "site": "00ae69fc",
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
      "definition_site": "00ae6928",
      "incomplete_value": true,
      "site": "00ae6934",
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
      "00ae69e0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae69f0",
      "DATA",
      [
        "storage",
        "010a03a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae69e0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae69f0",
      "DATA",
      [
        "storage",
        "010a0460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae691c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae68fc.md#insn-00ae691c) · [`00ae6918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae68fc.md#insn-00ae6918) · [`00ae6924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae68fc.md#insn-00ae6924)
- 新版 `00ae69e4`（命令位置の公開資料なし） · `00ae69e0`（命令位置の公開資料なし） · `00ae69ec`（命令位置の公開資料なし）

~~~diff
- 00ae691c ["INT_ADD", "register:40f0:8", ["const:ae691c:8", "const:4:8"]]
- 00ae691c ["CALL", null, ["callee:00bde130:8"]]
+ 00ae69e4 ["INT_ADD", "register:40f0:8", ["const:ae69e4:8", "const:4:8"]]
+ 00ae69e4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae691c bytes d9dd0394
+ 00ae69e4 bytes d3dd0394
- 00ae6918 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae6918 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6918 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6918 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae69e0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae69e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae69e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae69e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6918 bytes 001c1591
+ 00ae69e0 bytes 00501791
- 00ae6924 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00ae6924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae69ec ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00ae69ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae69ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae69ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae6924 bytes 08810e91
+ 00ae69ec bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07a196636716539320bb11f188094e91"></a>

### [`00ae6938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6938.md) → [`00ae6a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a00.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae6978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6a40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6954"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae694c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6a44"
      ]
    ],
    [
      "unmatched:00ae695c",
      "PARAM",
      [
        "storage",
        "0029fedf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae6a14",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6a1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6a44"
      ]
    ],
    [
      "00ae6a24",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6938.md#insn-00ae6954) · [`00ae6970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6938.md#insn-00ae6970) · [`00ae6978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6938.md#insn-00ae6978)
- 新版 `00ae6a38`（命令位置の公開資料なし）

~~~diff
- 00ae6954 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6954 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6954 bytes 410100b5
- 00ae6970 ["INT_ADD", "register:40f0:8", ["const:ae6970:8", "const:4:8"]]
- 00ae6970 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6a38 ["INT_ADD", "register:40f0:8", ["const:ae6a38:8", "const:4:8"]]
+ 00ae6a38 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6970 bytes 88dd0394
+ 00ae6a38 bytes 82dd0394
- 00ae6978 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
- 00ae6978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6978 bytes 80ca01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c086ff8c9090febb31d9a660802e88"></a>

### [`00ae69a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69a8.md) → [`00ae6a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a70.md) _ZN8firebase4util18file_output_stream10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 53.33% / 新版 53.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae69bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae6a84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae6a8c",
      "incomplete_value": false,
      "site": "00ae6a90",
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
      "definition_site": "00ae69c4",
      "incomplete_value": false,
      "site": "00ae69c8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae69bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6a94"
      ]
    ],
    [
      "00ae6a8c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae6a9c",
      "DATA",
      [
        "storage",
        "010a03b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae6a84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6a94"
      ]
    ],
    [
      "00ae6a8c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6a9c",
      "DATA",
      [
        "storage",
        "010a0478",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae69bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69a8.md#insn-00ae69bc) · [`00ae69c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69a8.md#insn-00ae69c8)
- 新版 `00ae6a90`（命令位置の公開資料なし） · `00ae6a84`（命令位置の公開資料なし）

~~~diff
- 00ae69bc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae69bc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae69bc bytes 8b000054
- 00ae69c8 ["INT_ADD", "register:40f0:8", ["const:ae69c8:8", "const:4:8"]]
- 00ae69c8 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae6a90 ["INT_ADD", "register:40f0:8", ["const:ae6a90:8", "const:4:8"]]
+ 00ae6a90 ["CALL", null, ["callee:00bde130:8"]]
- 00ae69c8 bytes aedd0394
+ 00ae6a90 bytes a8dd0394
+ 00ae6a84 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00ae6a84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae6a84 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f228623c3ebef0ff10382e8f6ec04916"></a>

### [`00ae69e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69e4.md) → [`00ae6aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aac.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae69e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae69e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae69e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae69e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae69e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6abc",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6aac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6ab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6abc",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae69e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69e4.md#insn-00ae69e4) · [`00ae69e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69e4.md#insn-00ae69e8) · [`00ae69f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae69e4.md#insn-00ae69f8)
- 新版 `00ae6ac0`（命令位置の公開資料なし）

~~~diff
- 00ae69e4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae69e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae69e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae69e4 bytes f30f1ef8
- 00ae69e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae69e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae69e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae69e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae69e8 bytes fd7b01a9
- 00ae69f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae69f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae6ac0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6ac0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae69f8 bytes e80000b5
+ 00ae6ac0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-556de30d42f19e72ca66b7a18b34216a"></a>

### [`00ae6a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a24.md) → [`00ae6aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aec.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae6a24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6a28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6a24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6a28",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6afc",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6af0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6afc",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a24.md#insn-00ae6a24) · [`00ae6a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a24.md#insn-00ae6a28) · [`00ae6a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a24.md#insn-00ae6a48)

~~~diff
- 00ae6a24 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae6a24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6a24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6a24 bytes f30f1ef8
- 00ae6a28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6a28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6a28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6a28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6a28 bytes fd7b01a9
- 00ae6a48 ["INT_ADD", "register:40f0:8", ["const:ae6a48:8", "const:4:8"]]
- 00ae6a48 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6a48 bytes 52dd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97b80871f654a753e585bfeeb0dd2b56"></a>

### [`00ae6a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a64.md) → [`00ae6b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b2c.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

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
      "site": "00ae6a94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6b5c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae6b40",
      "incomplete_value": true,
      "site": "00ae6b40",
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
      "definition_site": "00ae6a78",
      "incomplete_value": true,
      "site": "00ae6a78",
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
      "00ae6b3c",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6a98"
      ]
    ],
    [
      "unmatched:00ae6a84",
      "PARAM",
      [
        "storage",
        "002a7d94",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae6b3c",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6b60"
      ]
    ],
    [
      "00ae6b4c",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a64.md#insn-00ae6a78) · [`00ae6a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a64.md#insn-00ae6a8c) · [`00ae6a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6a64.md#insn-00ae6a94)
- 新版 `00ae6b40`（命令位置の公開資料なし）

~~~diff
- 00ae6a78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6a78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae6b40 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6b40 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6a78 bytes 080100b5
+ 00ae6b40 bytes 080100b5
- 00ae6a8c ["INT_ADD", "register:40f0:8", ["const:ae6a8c:8", "const:4:8"]]
- 00ae6a8c ["CALL", null, ["callee:00bde040:8"]]
- 00ae6a8c bytes 41dd0394
- 00ae6a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3c0:8"]]
- 00ae6a94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6a94 bytes 60e201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1872d21dcf340ddf708470fb5bdf8e57"></a>

### [`00ae6aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aa8.md) → [`00ae6b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b70.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00ae6aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6aac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6aac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6aac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6b80",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6b80",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aa8.md#insn-00ae6aa8) · [`00ae6aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aa8.md#insn-00ae6aac) · [`00ae6abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6aa8.md#insn-00ae6abc)
- 新版 `00ae6b84`（命令位置の公開資料なし）

~~~diff
- 00ae6aa8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae6aa8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6aa8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6aa8 bytes f30f1ef8
- 00ae6aac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6aac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6aac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6aac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6aac bytes fd7b01a9
- 00ae6abc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6abc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae6b84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6b84 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6abc bytes 080100b5
+ 00ae6b84 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-661e1a7722fef398e2142cf09595fe24"></a>

### [`00ae6b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6b94.md) → [`00ae6c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6c5c.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 27.27% / 新版 33.33%

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
      "site": "00ae6bd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae6ce8",
      "incomplete_value": true,
      "site": "00ae6ce8",
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
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6c20",
      "incomplete_value": true,
      "site": "00ae6c20",
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
            "const:3c0:8"
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
      "site": "00ae6c98"
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
      "00ae6c70",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6c7c",
      "READ",
      [
        "storage",
        "010a03c8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae6bd0",
      "WRITE",
      [
        "storage",
        "010a03c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6c70",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6c7c",
      "READ",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6c98",
      "WRITE",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6b94.md#insn-00ae6bac) · [`00ae6bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6b94.md#insn-00ae6bd0) · [`00ae6c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6b94.md#insn-00ae6c1c)
- 新版 `00ae6c74`（命令位置の公開資料なし） · `00ae6ce4`（命令位置の公開資料なし）

~~~diff
- 00ae6bac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6bac ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00ae6c74 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae6c74 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae6bac bytes c10300b4
+ 00ae6c74 bytes c10300b4
- 00ae6bd0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6bd0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6bd0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3c8:8"]]
- 00ae6bd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6bd0 bytes bf220f39
- 00ae6c1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6c1c ["INT_ADD", "register:40f0:8", ["const:ae6c1c:8", "const:4:8"]]
- 00ae6c1c ["CALLIND", null, ["register:0:8"]]
+ 00ae6ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6ce4 ["INT_ADD", "register:40f0:8", ["const:ae6ce4:8", "const:4:8"]]
+ 00ae6ce4 ["CALLIND", null, ["register:0:8"]]
- 00ae6c1c bytes 00013fd6
+ 00ae6ce4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f5cd94db18507fa81a8f5da13b7ddd8"></a>

### [`00ae6c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6c34.md) → [`00ae6cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6cfc.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae6c74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6d3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6c50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6c48",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6c50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6d40"
      ]
    ],
    [
      "unmatched:00ae6c58",
      "PARAM",
      [
        "storage",
        "002a7d94",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae6d10",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6d18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6d40"
      ]
    ],
    [
      "00ae6d20",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6c34.md#insn-00ae6c50) · [`00ae6c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6c34.md#insn-00ae6c6c) · [`00ae6c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6c34.md#insn-00ae6c74)
- 新版 `00ae6d34`（命令位置の公開資料なし）

~~~diff
- 00ae6c50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6c50 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6c50 bytes 410100b5
- 00ae6c6c ["INT_ADD", "register:40f0:8", ["const:ae6c6c:8", "const:4:8"]]
- 00ae6c6c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6d34 ["INT_ADD", "register:40f0:8", ["const:ae6d34:8", "const:4:8"]]
+ 00ae6d34 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6c6c bytes c9dc0394
+ 00ae6d34 bytes c3dc0394
- 00ae6c74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c0:8"]]
- 00ae6c74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6c74 bytes 80e201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e80935bcd292eaf4490deebece00d76d"></a>

### [`00ae6ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ce0.md) → [`00ae6da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6da8.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae6d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6de8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6cfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6cf4",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6cfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6dec"
      ]
    ],
    [
      "unmatched:00ae6d04",
      "PARAM",
      [
        "storage",
        "002a7d94",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae6dbc",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6dec"
      ]
    ],
    [
      "00ae6dcc",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ce0.md#insn-00ae6cfc) · [`00ae6d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ce0.md#insn-00ae6d18) · [`00ae6d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ce0.md#insn-00ae6d20)
- 新版 `00ae6de0`（命令位置の公開資料なし）

~~~diff
- 00ae6cfc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6cfc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae6cfc bytes 410100b5
- 00ae6d18 ["INT_ADD", "register:40f0:8", ["const:ae6d18:8", "const:4:8"]]
- 00ae6d18 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6de0 ["INT_ADD", "register:40f0:8", ["const:ae6de0:8", "const:4:8"]]
+ 00ae6de0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6d18 bytes 9edc0394
+ 00ae6de0 bytes 98dc0394
- 00ae6d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3c0:8"]]
- 00ae6d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6d20 bytes 80e201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae038b3b808ba4e0f98bdc4be621d0be"></a>

### [`00ae6d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d8c.md) → [`00ae6e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e54.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae6e80",
      "incomplete_value": true,
      "site": "00ae6e80",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6db8",
      "incomplete_value": true,
      "site": "00ae6db8",
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
            "const:3e8:8"
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
      "definition_site": "00ae6e68",
      "incomplete_value": true,
      "site": "00ae6e68",
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
      "definition_site": "00ae6da0",
      "incomplete_value": true,
      "site": "00ae6da0",
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
      "definition_site": "00ae6e74",
      "incomplete_value": false,
      "site": "00ae6e78",
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
            "const:e51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6dac",
      "incomplete_value": false,
      "site": "00ae6db0",
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
            "const:e58:8"
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
      "00ae6e64",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6e74",
      "PARAM",
      [
        "storage",
        "002a4e58",
        null,
        "string"
      ]
    ],
    [
      "00ae6e80",
      "WRITE",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6e64",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6e74",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6e80",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d8c.md#insn-00ae6db0) · [`00ae6db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d8c.md#insn-00ae6db8) · [`00ae6d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6d8c.md#insn-00ae6d9c)
- 新版 `00ae6e78`（命令位置の公開資料なし） · `00ae6e80`（命令位置の公開資料なし） · `00ae6e64`（命令位置の公開資料なし）

~~~diff
- 00ae6db0 ["INT_ADD", "register:40f0:8", ["const:ae6db0:8", "const:4:8"]]
- 00ae6db0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6e78 ["INT_ADD", "register:40f0:8", ["const:ae6e78:8", "const:4:8"]]
+ 00ae6e78 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6db0 bytes 78dc0394
+ 00ae6e78 bytes 72dc0394
- 00ae6db8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6db8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00ae6e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6db8 bytes 60f601f9
+ 00ae6e80 bytes 605602f9
- 00ae6d9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6d9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6e64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00ae6e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6d9c bytes 68f641f9
+ 00ae6e64 bytes 685642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35252c0cab82494265d7bacd0d1b0c00"></a>

### [`00ae6dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6dcc.md) → [`00ae6e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e94.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae6ec0",
      "incomplete_value": true,
      "site": "00ae6ec0",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6df8",
      "incomplete_value": true,
      "site": "00ae6df8",
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
            "const:3e8:8"
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
      "definition_site": "00ae6ea8",
      "incomplete_value": true,
      "site": "00ae6ea8",
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
      "definition_site": "00ae6de0",
      "incomplete_value": true,
      "site": "00ae6de0",
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
      "definition_site": "00ae6eb0",
      "incomplete_value": false,
      "site": "00ae6eb8",
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
            "const:e51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6de8",
      "incomplete_value": false,
      "site": "00ae6df0",
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
            "const:e58:8"
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
      "00ae6ea4",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6eb0",
      "PARAM",
      [
        "storage",
        "002a4e58",
        null,
        "string"
      ]
    ],
    [
      "00ae6ec0",
      "WRITE",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6ea4",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6eb0",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6ec0",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6dcc.md#insn-00ae6df0) · [`00ae6df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6dcc.md#insn-00ae6df8) · [`00ae6ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6dcc.md#insn-00ae6ddc)
- 新版 `00ae6eb8`（命令位置の公開資料なし） · `00ae6ec0`（命令位置の公開資料なし） · `00ae6ea4`（命令位置の公開資料なし）

~~~diff
- 00ae6df0 ["INT_ADD", "register:40f0:8", ["const:ae6df0:8", "const:4:8"]]
- 00ae6df0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6eb8 ["INT_ADD", "register:40f0:8", ["const:ae6eb8:8", "const:4:8"]]
+ 00ae6eb8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6df0 bytes 68dc0394
+ 00ae6eb8 bytes 62dc0394
- 00ae6df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00ae6ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6df8 bytes 60f601f9
+ 00ae6ec0 bytes 605602f9
- 00ae6ddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6ddc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6ea4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00ae6ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6ddc bytes 68f641f9
+ 00ae6ea4 bytes 685642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02d53430185124e098a21bc2a448e5f5"></a>

### [`00ae6e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e0c.md) → [`00ae6ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6ed4.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae6e3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6f04"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae6ee8",
      "incomplete_value": true,
      "site": "00ae6ee8",
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
      "definition_site": "00ae6e20",
      "incomplete_value": true,
      "site": "00ae6e20",
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
      "00ae6ee4",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6ee8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6e40"
      ]
    ],
    [
      "unmatched:00ae6e2c",
      "PARAM",
      [
        "storage",
        "002a4e58",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae6ee4",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6ee8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6f08"
      ]
    ],
    [
      "00ae6ef4",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e0c.md#insn-00ae6e34) · [`00ae6e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e0c.md#insn-00ae6e3c) · [`00ae6e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e0c.md#insn-00ae6e4c)

~~~diff
- 00ae6e34 ["INT_ADD", "register:40f0:8", ["const:ae6e34:8", "const:4:8"]]
- 00ae6e34 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6e34 bytes 57dc0394
- 00ae6e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6e3c bytes 60f601f9
- 00ae6e4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae6e4c ["RETURN", null, ["register:0:8"]]
- 00ae6e4c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86faab2f14712a80a71b6b91f698b79b"></a>

### [`00ae6e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e50.md) → [`00ae6f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f18.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae6f48",
      "incomplete_value": true,
      "site": "00ae6f48",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e80",
      "incomplete_value": true,
      "site": "00ae6e80",
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
            "const:3e8:8"
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
    "old": {
      "definition_site": "00ae6e64",
      "incomplete_value": true,
      "site": "00ae6e64",
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
      "definition_site": "00ae6f34",
      "incomplete_value": false,
      "site": "00ae6f40",
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
            "const:e51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e6c",
      "incomplete_value": false,
      "site": "00ae6e78",
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
            "const:e58:8"
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
      "00ae6f28",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6f34",
      "PARAM",
      [
        "storage",
        "002a4e58",
        null,
        "string"
      ]
    ],
    [
      "00ae6f48",
      "WRITE",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6f28",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6f34",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6f48",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e50.md#insn-00ae6e78) · [`00ae6e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e50.md#insn-00ae6e80) · [`00ae6e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6e50.md#insn-00ae6e60)
- 新版 `00ae6f40`（命令位置の公開資料なし） · `00ae6f48`（命令位置の公開資料なし） · `00ae6f28`（命令位置の公開資料なし）

~~~diff
- 00ae6e78 ["INT_ADD", "register:40f0:8", ["const:ae6e78:8", "const:4:8"]]
- 00ae6e78 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6f40 ["INT_ADD", "register:40f0:8", ["const:ae6f40:8", "const:4:8"]]
+ 00ae6f40 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6e78 bytes 46dc0394
+ 00ae6f40 bytes 40dc0394
- 00ae6e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00ae6f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6e80 bytes 60f601f9
+ 00ae6f48 bytes 605602f9
- 00ae6e60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e8:8"]]
- 00ae6e60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6f28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00ae6f28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6e60 bytes 68f641f9
+ 00ae6f28 bytes 685642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a35b29a106848f1d56d74e8672c459fa"></a>

### [`00ae6ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ea0.md) → [`00ae6f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae6ff0",
      "incomplete_value": true,
      "site": "00ae6ff0",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f28",
      "incomplete_value": true,
      "site": "00ae6f28",
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
            "const:3f0:8"
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
      "definition_site": "00ae6f9c",
      "incomplete_value": true,
      "site": "00ae6fa8",
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
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ed4",
      "incomplete_value": true,
      "site": "00ae6ee0",
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
                "const:3e8:8"
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
    "new": null,
    "old": {
      "definition_site": "00ae6f14",
      "incomplete_value": true,
      "site": "00ae6f1c",
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
      "00ae6f7c",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6f9c",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6ff0",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6f7c",
      "READ",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6f9c",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6ff0",
      "WRITE",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ea0.md#insn-00ae6ee0) · [`00ae6f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ea0.md#insn-00ae6f1c) · [`00ae6f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6ea0.md#insn-00ae6f28)
- 新版 `00ae6fa8`（命令位置の公開資料なし） · `00ae6fe4`（命令位置の公開資料なし） · `00ae6ff0`（命令位置の公開資料なし）

~~~diff
- 00ae6ee0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6ee0 ["INT_ADD", "register:40f0:8", ["const:ae6ee0:8", "const:4:8"]]
- 00ae6ee0 ["CALLIND", null, ["register:0:8"]]
+ 00ae6fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6fa8 ["INT_ADD", "register:40f0:8", ["const:ae6fa8:8", "const:4:8"]]
+ 00ae6fa8 ["CALLIND", null, ["register:0:8"]]
- 00ae6ee0 bytes 00013fd6
+ 00ae6fa8 bytes 00013fd6
- 00ae6f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6f1c ["INT_ADD", "register:40f0:8", ["const:ae6f1c:8", "const:4:8"]]
- 00ae6f1c ["CALLIND", null, ["register:0:8"]]
+ 00ae6fe4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6fe4 ["INT_ADD", "register:40f0:8", ["const:ae6fe4:8", "const:4:8"]]
+ 00ae6fe4 ["CALLIND", null, ["register:0:8"]]
- 00ae6f1c bytes 00013fd6
+ 00ae6fe4 bytes 00013fd6
- 00ae6f28 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae6f28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3f0:8"]]
- 00ae6f28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae6ff0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae6ff0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4b0:8"]]
+ 00ae6ff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae6f28 bytes a0c20f39
+ 00ae6ff0 bytes a0c21239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f030510ca8d6ab2294f45d682c2d87a"></a>

### [`00ae6f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6f3c.md) → [`00ae7004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7004.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7040",
      "incomplete_value": true,
      "site": "00ae7040",
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
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f78",
      "incomplete_value": true,
      "site": "00ae6f78",
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
            "const:3f0:8"
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
      "site": "00ae6fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7090"
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
      "00ae7018",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7024",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7040",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7018",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7024",
      "READ",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7040",
      "WRITE",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6f3c.md#insn-00ae6f54) · [`00ae6f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6f3c.md#insn-00ae6f78) · [`00ae6fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6f3c.md#insn-00ae6fc4)
- 新版 `00ae701c`（命令位置の公開資料なし） · `00ae7040`（命令位置の公開資料なし）

~~~diff
- 00ae6f54 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6f54 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00ae701c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae701c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae6f54 bytes c10300b4
+ 00ae701c bytes c10300b4
- 00ae6f78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6f78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6f78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3f0:8"]]
- 00ae6f78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae7040 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae7040 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae7040 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
+ 00ae7040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6f78 bytes bfc20f39
+ 00ae7040 bytes bfc21239
- 00ae6fc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6fc4 ["INT_ADD", "register:40f0:8", ["const:ae6fc4:8", "const:4:8"]]
- 00ae6fc4 ["CALLIND", null, ["register:0:8"]]
- 00ae6fc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43c0627a0f524972912cb8d0d1b8b638"></a>

### [`00ae6fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6fdc.md) → [`00ae70a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae6fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6fe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6ff0",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae70a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae70a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae70b8",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6fdc.md#insn-00ae6fdc) · [`00ae6fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6fdc.md#insn-00ae6fe0) · [`00ae6ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6fdc.md#insn-00ae6ff8)

~~~diff
- 00ae6fdc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae6fdc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae6fdc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6fdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6fdc bytes f44fbea9
- 00ae6fe0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6fe0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6fe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6fe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6fe0 bytes fd7b01a9
- 00ae6ff8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6ff8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6ff8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4150e854f2bc7ee1eaf61479c9cd2eb2"></a>

### [`00ae7088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7088.md) → [`00ae7150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7150.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae7088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae708c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7088",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae708c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae709c",
      "READ",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7150",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae7154",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae7164",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7088.md#insn-00ae7088) · [`00ae708c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7088.md#insn-00ae708c) · [`00ae70a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7088.md#insn-00ae70a4)

~~~diff
- 00ae7088 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae7088 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae7088 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae7088 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7088 bytes f44fbea9
- 00ae708c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae708c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae708c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae708c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae708c bytes fd7b01a9
- 00ae70a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae70a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae70a4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ee2ba849c796bb14250c8e90bfdf4b0"></a>

### [`00ae7134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7134.md) → [`00ae71fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71fc.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae7160"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7228"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae7210",
      "incomplete_value": true,
      "site": "00ae7210",
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
      "definition_site": "00ae7148",
      "incomplete_value": true,
      "site": "00ae7148",
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
      "00ae720c",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7154",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7158",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae720c",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae721c",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      "00ae7220",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7134.md#insn-00ae7148) · [`00ae7158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7134.md#insn-00ae7158) · [`00ae7160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7134.md#insn-00ae7160)
- 新版 `00ae7210`（命令位置の公開資料なし）

~~~diff
- 00ae7148 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7148 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae7210 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae7210 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7148 bytes e80000b5
+ 00ae7210 bytes e80000b5
- 00ae7158 ["INT_ADD", "register:40f0:8", ["const:ae7158:8", "const:4:8"]]
- 00ae7158 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7158 bytes 8edb0394
- 00ae7160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:408:8"]]
- 00ae7160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7160 bytes 600602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b5a4a71bca39b1f066010b685d1c44"></a>

### [`00ae71b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71b4.md) → [`00ae727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae727c.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae72ac",
      "incomplete_value": true,
      "site": "00ae72ac",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae71e4",
      "incomplete_value": true,
      "site": "00ae71e4",
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
            "const:408:8"
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
      "definition_site": "00ae7290",
      "incomplete_value": true,
      "site": "00ae7290",
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
      "definition_site": "00ae71c8",
      "incomplete_value": true,
      "site": "00ae71c8",
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
      "definition_site": "00ae729c",
      "incomplete_value": false,
      "site": "00ae72a4",
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
    "old": {
      "definition_site": "00ae71d4",
      "incomplete_value": false,
      "site": "00ae71dc",
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
            "const:342:8"
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
      "00ae728c",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae729c",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ],
    [
      "00ae72ac",
      "WRITE",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae728c",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae729c",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      "00ae72ac",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae71dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71b4.md#insn-00ae71dc) · [`00ae71e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71b4.md#insn-00ae71e4) · [`00ae71c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71b4.md#insn-00ae71c4)
- 新版 `00ae72a4`（命令位置の公開資料なし） · `00ae72ac`（命令位置の公開資料なし） · `00ae728c`（命令位置の公開資料なし）

~~~diff
- 00ae71dc ["INT_ADD", "register:40f0:8", ["const:ae71dc:8", "const:4:8"]]
- 00ae71dc ["CALL", null, ["callee:00bde040:8"]]
+ 00ae72a4 ["INT_ADD", "register:40f0:8", ["const:ae72a4:8", "const:4:8"]]
+ 00ae72a4 ["CALL", null, ["callee:00bde040:8"]]
- 00ae71dc bytes 6ddb0394
+ 00ae72a4 bytes 67db0394
- 00ae71e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:408:8"]]
- 00ae71e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae72ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae71e4 bytes 600602f9
+ 00ae72ac bytes 606602f9
- 00ae71c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:408:8"]]
- 00ae71c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae728c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae728c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae71c4 bytes 680642f9
+ 00ae728c bytes 686642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3361f63ba83a59033875efad4c054348"></a>

### [`00ae71f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71f8.md) → [`00ae72c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae72c0.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7228",
      "incomplete_value": true,
      "site": "00ae7228",
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
            "const:408:8"
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
    "old": {
      "definition_site": "00ae720c",
      "incomplete_value": true,
      "site": "00ae720c",
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
      "definition_site": "00ae72dc",
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
    "old": {
      "definition_site": "00ae7214",
      "incomplete_value": false,
      "site": "00ae7220",
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
            "const:342:8"
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
      "00ae72d0",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae72dc",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ],
    [
      "00ae72f0",
      "WRITE",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae72d0",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae72dc",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ],
    [
      "00ae72f0",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71f8.md#insn-00ae7220) · [`00ae7228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71f8.md#insn-00ae7228) · [`00ae7208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae71f8.md#insn-00ae7208)
- 新版 `00ae72e8`（命令位置の公開資料なし） · `00ae72f0`（命令位置の公開資料なし） · `00ae72d0`（命令位置の公開資料なし）

~~~diff
- 00ae7220 ["INT_ADD", "register:40f0:8", ["const:ae7220:8", "const:4:8"]]
- 00ae7220 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae72e8 ["INT_ADD", "register:40f0:8", ["const:ae72e8:8", "const:4:8"]]
+ 00ae72e8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7220 bytes 5cdb0394
+ 00ae72e8 bytes 56db0394
- 00ae7228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:408:8"]]
- 00ae7228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae72f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae72f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7228 bytes 600602f9
+ 00ae72f0 bytes 606602f9
- 00ae7208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:408:8"]]
- 00ae7208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae72d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00ae72d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7208 bytes 680642f9
+ 00ae72d0 bytes 686642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41b4ff51c5b0adc59eaf180c20263e9a"></a>

### [`00ae7248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7248.md) → [`00ae7310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7310.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ae7248"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae724c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae724c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7248",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae724c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7250",
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
      "00ae7310",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae7314",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae7318",
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

- 旧版 [`00ae7248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7248.md#insn-00ae7248) · [`00ae724c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7248.md#insn-00ae724c) · [`00ae7250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7248.md#insn-00ae7250)

~~~diff
- 00ae7248 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae7248 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae7248 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7248 bytes f50f1df8
- 00ae724c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae724c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae724c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae724c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae724c bytes f44f01a9
- 00ae7250 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7250 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7250 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae7250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7250 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adcc4e209909fa9584c65e182cf597b2"></a>

### [`00ae72e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae72e4.md) → [`00ae73ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae73ac.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00ae7320"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae73e8"
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
      "00ae73c0",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae73cc",
      "READ",
      [
        "storage",
        "010a0410",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae7320",
      "WRITE",
      [
        "storage",
        "010a0410",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae73c0",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae73cc",
      "READ",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae73e8",
      "WRITE",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae72fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae72e4.md#insn-00ae72fc) · [`00ae7320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae72e4.md#insn-00ae7320) · [`00ae7358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae72e4.md#insn-00ae7358)
- 新版 `00ae73c4`（命令位置の公開資料なし）

~~~diff
- 00ae72fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae72fc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00ae73c4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae73c4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae72fc bytes c10300b4
+ 00ae73c4 bytes c10300b4
- 00ae7320 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7320 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7320 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:410:8"]]
- 00ae7320 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7320 bytes bf421039
- 00ae7358 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7358 ["INT_ADD", "register:40f0:8", ["const:ae7358:8", "const:4:8"]]
- 00ae7358 ["CALLIND", null, ["register:0:8"]]
- 00ae7358 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a740e5903bf25a36be0911acb8a5574c"></a>

### [`00ae7384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7384.md) → [`00ae744c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae744c.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae73c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae748c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae73a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7398",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae73a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7490"
      ]
    ],
    [
      "unmatched:00ae73a8",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae7460",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7490"
      ]
    ],
    [
      "00ae7470",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae73a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7384.md#insn-00ae73a0) · [`00ae73bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7384.md#insn-00ae73bc) · [`00ae73c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7384.md#insn-00ae73c4)
- 新版 `00ae7484`（命令位置の公開資料なし）

~~~diff
- 00ae73a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae73a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae73a0 bytes 410100b5
- 00ae73bc ["INT_ADD", "register:40f0:8", ["const:ae73bc:8", "const:4:8"]]
- 00ae73bc ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7484 ["INT_ADD", "register:40f0:8", ["const:ae7484:8", "const:4:8"]]
+ 00ae7484 ["CALL", null, ["callee:00bde040:8"]]
- 00ae73bc bytes f5da0394
+ 00ae7484 bytes efda0394
- 00ae73c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:408:8"]]
- 00ae73c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae73c4 bytes 800602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-316cd08d58834515facf8e23fb30ce57"></a>

### [`00ae7430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7430.md) → [`00ae74f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74f8.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae7470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7538"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae744c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7444",
      "READ",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae744c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae753c"
      ]
    ],
    [
      "unmatched:00ae7454",
      "PARAM",
      [
        "storage",
        "002ad342",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae750c",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7514",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae753c"
      ]
    ],
    [
      "00ae751c",
      "PARAM",
      [
        "storage",
        "002ad339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae744c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7430.md#insn-00ae744c) · [`00ae7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7430.md#insn-00ae7468) · [`00ae7470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7430.md#insn-00ae7470)
- 新版 `00ae7530`（命令位置の公開資料なし）

~~~diff
- 00ae744c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae744c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae744c bytes 410100b5
- 00ae7468 ["INT_ADD", "register:40f0:8", ["const:ae7468:8", "const:4:8"]]
- 00ae7468 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7530 ["INT_ADD", "register:40f0:8", ["const:ae7530:8", "const:4:8"]]
+ 00ae7530 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7468 bytes cada0394
+ 00ae7530 bytes c4da0394
- 00ae7470 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:408:8"]]
- 00ae7470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7470 bytes 800602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b8baa0e245ad5495bfa84790926d43"></a>

### [`00ae74dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74dc.md) → [`00ae75a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75a4.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae74dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae74e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae74e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae74dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae74e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae75b4",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae75a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae75a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae75b4",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae74dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74dc.md#insn-00ae74dc) · [`00ae74e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74dc.md#insn-00ae74e0) · [`00ae74f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae74dc.md#insn-00ae74f0)
- 新版 `00ae75b8`（命令位置の公開資料なし）

~~~diff
- 00ae74dc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae74dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae74dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae74dc bytes f30f1ef8
- 00ae74e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae74e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae74e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae74e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae74e0 bytes fd7b01a9
- 00ae74f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae74f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00ae75b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae75b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae74f0 bytes e80000b5
+ 00ae75b8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fcc8aee15be7bcf7b75aa4745563e6b"></a>

### [`00ae755c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae755c.md) → [`00ae7624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7624.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae758c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7654"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae7638",
      "incomplete_value": true,
      "site": "00ae7638",
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
      "definition_site": "00ae7570",
      "incomplete_value": true,
      "site": "00ae7570",
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
      "00ae7634",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae757c",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7584",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae7634",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7644",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae764c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae755c.md#insn-00ae7570) · [`00ae7584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae755c.md#insn-00ae7584) · [`00ae758c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae755c.md#insn-00ae758c)
- 新版 `00ae7638`（命令位置の公開資料なし）

~~~diff
- 00ae7570 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7570 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae7638 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae7638 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7570 bytes 080100b5
+ 00ae7638 bytes 080100b5
- 00ae7584 ["INT_ADD", "register:40f0:8", ["const:ae7584:8", "const:4:8"]]
- 00ae7584 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7584 bytes 83da0394
- 00ae758c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00ae758c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae758c bytes 603a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48c4f80c9466b498fe26a2559e38d53b"></a>

### [`00ae75a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75a0.md) → [`00ae7668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7668.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00ae75d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7698"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae75b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae75b0",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae75b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae769c"
      ]
    ],
    [
      "unmatched:00ae75bc",
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
      "00ae7678",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae767c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae769c"
      ]
    ],
    [
      "00ae7684",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae75b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75a0.md#insn-00ae75b4) · [`00ae75c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75a0.md#insn-00ae75c8) · [`00ae75d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75a0.md#insn-00ae75d0)
- 新版 `00ae7690`（命令位置の公開資料なし）

~~~diff
- 00ae75b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae75b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae75b4 bytes 080100b5
- 00ae75c8 ["INT_ADD", "register:40f0:8", ["const:ae75c8:8", "const:4:8"]]
- 00ae75c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7690 ["INT_ADD", "register:40f0:8", ["const:ae7690:8", "const:4:8"]]
+ 00ae7690 ["CALL", null, ["callee:00bde040:8"]]
- 00ae75c8 bytes 72da0394
+ 00ae7690 bytes 6cda0394
- 00ae75d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:470:8"]]
- 00ae75d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae75d0 bytes 603a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6884824ba6724000c59c08f40d9e29b9"></a>

### [`00ae75e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75e4.md) → [`00ae76ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76ac.md) _ZN8firebase4util10array_list8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf40.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bddff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddff0.md) · 呼出先 0件 

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae75e8",
      "incomplete_value": true,
      "site": "00ae75ec",
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
                "const:470:8"
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
      "unmatched:00ae75e8",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae76b0",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae75e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75e4.md#insn-00ae75e8)
- 新版 `00ae76b0`（命令位置の公開資料なし）

~~~diff
- 00ae75e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00ae75e8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae75e8 bytes 003942f9
+ 00ae76b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 00ae76b0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae76b0 bytes 009942f9
~~~


<a id="compare-8e98245c624c3f8727cb0dd0d2689bd5"></a>

### [`00ae75f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75f0.md) → [`00ae76b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76b8.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae75f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae75f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae75f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae75f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae75f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae75f8",
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
      "00ae76b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae76bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae76c0",
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

- 旧版 [`00ae75f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75f0.md#insn-00ae75f0) · [`00ae75f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75f0.md#insn-00ae75f4) · [`00ae75f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae75f0.md#insn-00ae75f8)

~~~diff
- 00ae75f0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae75f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae75f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae75f0 bytes f50f1df8
- 00ae75f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae75f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae75f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae75f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae75f4 bytes f44f01a9
- 00ae75f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae75f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae75f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae75f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae75f8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-583363e519672d8ededbe38dbc449ac2"></a>

### [`00ae768c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae768c.md) → [`00ae7754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7754.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 30.00% / 新版 30.00%

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
      "site": "00ae76c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae77e0",
      "incomplete_value": true,
      "site": "00ae77e0",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7718",
      "incomplete_value": true,
      "site": "00ae7718",
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
            "const:470:8"
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
      "site": "00ae7790"
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
      "00ae7768",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7774",
      "READ",
      [
        "storage",
        "010a0478",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae76c8",
      "WRITE",
      [
        "storage",
        "010a0478",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7768",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7774",
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7790",
      "WRITE",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae76c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae768c.md#insn-00ae76c8) · [`00ae76f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae768c.md#insn-00ae76f0) · [`00ae7714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae768c.md#insn-00ae7714)
- 新版 `00ae77dc`（命令位置の公開資料なし）

~~~diff
- 00ae76c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae76c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae76c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:478:8"]]
- 00ae76c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae76c8 bytes bfe21139
- 00ae76f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae76f0 ["INT_ADD", "register:40f0:8", ["const:ae76f0:8", "const:4:8"]]
- 00ae76f0 ["CALLIND", null, ["register:0:8"]]
- 00ae76f0 bytes 00013fd6
- 00ae7714 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7714 ["INT_ADD", "register:40f0:8", ["const:ae7714:8", "const:4:8"]]
- 00ae7714 ["CALLIND", null, ["register:0:8"]]
+ 00ae77dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae77dc ["INT_ADD", "register:40f0:8", ["const:ae77dc:8", "const:4:8"]]
+ 00ae77dc ["CALLIND", null, ["register:0:8"]]
- 00ae7714 bytes 00013fd6
+ 00ae77dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-146fb6ad37e39a4e51c6fd9d4c2d6d9e"></a>

### [`00ae772c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae772c.md) → [`00ae77f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae77f4.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae776c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7834"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7748"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7740",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7838"
      ]
    ],
    [
      "unmatched:00ae7750",
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
      "00ae7808",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7838"
      ]
    ],
    [
      "00ae7818",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae772c.md#insn-00ae7748) · [`00ae7764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae772c.md#insn-00ae7764) · [`00ae776c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae772c.md#insn-00ae776c)
- 新版 `00ae782c`（命令位置の公開資料なし）

~~~diff
- 00ae7748 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7748 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7748 bytes 410100b5
- 00ae7764 ["INT_ADD", "register:40f0:8", ["const:ae7764:8", "const:4:8"]]
- 00ae7764 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae782c ["INT_ADD", "register:40f0:8", ["const:ae782c:8", "const:4:8"]]
+ 00ae782c ["CALL", null, ["callee:00bde040:8"]]
- 00ae7764 bytes 0bda0394
+ 00ae782c bytes 05da0394
- 00ae776c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:470:8"]]
- 00ae776c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae776c bytes 803a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbafbc1f8d9a02312cb0c71f5e91c448"></a>

### [`00ae77d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae77d8.md) → [`00ae78a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae78a0.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae78e0",
      "incomplete_value": true,
      "site": "00ae78e0",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7818",
      "incomplete_value": true,
      "site": "00ae7818",
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
            "const:470:8"
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
      "definition_site": "00ae78bc",
      "incomplete_value": true,
      "site": "00ae78bc",
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
      "definition_site": "00ae77f4",
      "incomplete_value": true,
      "site": "00ae77f4",
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
      "definition_site": "00ae78c4",
      "incomplete_value": false,
      "site": "00ae78d8",
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
            "const:524:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae77fc",
      "incomplete_value": false,
      "site": "00ae7810",
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
      "00ae78b4",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae78c4",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae78e0",
      "WRITE",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae78b4",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae78c4",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae78e0",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae77d8.md#insn-00ae7810) · [`00ae7818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae77d8.md#insn-00ae7818) · [`00ae77ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae77d8.md#insn-00ae77ec)
- 新版 `00ae78d8`（命令位置の公開資料なし） · `00ae78e0`（命令位置の公開資料なし） · `00ae78b4`（命令位置の公開資料なし）

~~~diff
- 00ae7810 ["INT_ADD", "register:40f0:8", ["const:ae7810:8", "const:4:8"]]
- 00ae7810 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae78d8 ["INT_ADD", "register:40f0:8", ["const:ae78d8:8", "const:4:8"]]
+ 00ae78d8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7810 bytes e0d90394
+ 00ae78d8 bytes dad90394
- 00ae7818 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:470:8"]]
- 00ae7818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae78e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
+ 00ae78e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7818 bytes 803a02f9
+ 00ae78e0 bytes 809a02f9
- 00ae77ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:470:8"]]
- 00ae77ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae78b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
+ 00ae78b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae77ec bytes 813a42f9
+ 00ae78b4 bytes 819a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5708e7d9cbb77f61dc2802d3d7bc46fd"></a>

### [`00ae7848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7848.md) → [`00ae7910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7910.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae792c",
      "incomplete_value": false,
      "site": "00ae7930",
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
      "definition_site": "00ae7864",
      "incomplete_value": false,
      "site": "00ae7868",
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
      "definition_site": "00ae793c",
      "incomplete_value": true,
      "site": "00ae7948",
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
      "definition_site": "00ae7874",
      "incomplete_value": true,
      "site": "00ae7880",
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
      "00ae792c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae793c",
      "DATA",
      [
        "storage",
        "010a0498",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae792c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae793c",
      "DATA",
      [
        "storage",
        "010a0558",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7848.md#insn-00ae7868) · [`00ae7864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7848.md#insn-00ae7864) · [`00ae7870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7848.md#insn-00ae7870)
- 新版 `00ae7930`（命令位置の公開資料なし） · `00ae792c`（命令位置の公開資料なし） · `00ae7938`（命令位置の公開資料なし）

~~~diff
- 00ae7868 ["INT_ADD", "register:40f0:8", ["const:ae7868:8", "const:4:8"]]
- 00ae7868 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7930 ["INT_ADD", "register:40f0:8", ["const:ae7930:8", "const:4:8"]]
+ 00ae7930 ["CALL", null, ["callee:00bde130:8"]]
- 00ae7868 bytes 06da0394
+ 00ae7930 bytes 00da0394
- 00ae7864 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7864 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7864 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7864 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae792c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae792c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae792c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae792c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7864 bytes 00c81791
+ 00ae792c bytes 00fc1991
- 00ae7870 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00ae7870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae7938 ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00ae7938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7870 bytes 08611291
+ 00ae7938 bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7798c48a547a8f571a0a828f98c223f"></a>

### [`00ae7884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7884.md) → [`00ae794c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae794c.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae7978",
      "incomplete_value": true,
      "site": "00ae7978",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78b0",
      "incomplete_value": true,
      "site": "00ae78b0",
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
            "const:4a0:8"
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
      "definition_site": "00ae7960",
      "incomplete_value": true,
      "site": "00ae7960",
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
      "definition_site": "00ae7898",
      "incomplete_value": true,
      "site": "00ae7898",
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
      "definition_site": "00ae796c",
      "incomplete_value": false,
      "site": "00ae7970",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78a4",
      "incomplete_value": false,
      "site": "00ae78a8",
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
            "const:3cd:8"
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
      "00ae795c",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae796c",
      "PARAM",
      [
        "storage",
        "002ae3cd",
        null,
        "string"
      ]
    ],
    [
      "00ae7978",
      "WRITE",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae795c",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae796c",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      "00ae7978",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae78a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7884.md#insn-00ae78a8) · [`00ae78b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7884.md#insn-00ae78b0) · [`00ae7894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7884.md#insn-00ae7894)
- 新版 `00ae7970`（命令位置の公開資料なし） · `00ae7978`（命令位置の公開資料なし） · `00ae795c`（命令位置の公開資料なし）

~~~diff
- 00ae78a8 ["INT_ADD", "register:40f0:8", ["const:ae78a8:8", "const:4:8"]]
- 00ae78a8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7970 ["INT_ADD", "register:40f0:8", ["const:ae7970:8", "const:4:8"]]
+ 00ae7970 ["CALL", null, ["callee:00bde040:8"]]
- 00ae78a8 bytes bad90394
+ 00ae7970 bytes b4d90394
- 00ae78b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00ae78b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7978 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae7978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae78b0 bytes 605202f9
+ 00ae7978 bytes 60b202f9
- 00ae7894 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00ae7894 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae795c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00ae795c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7894 bytes 685242f9
+ 00ae795c bytes 68b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e665ffed645384a42f28b4136b7878b9"></a>

### [`00ae78c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae78c4.md) → [`00ae798c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae798c.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

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
      "site": "00ae78f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae79b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae79a0",
      "incomplete_value": true,
      "site": "00ae79a0",
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
      "definition_site": "00ae78d8",
      "incomplete_value": true,
      "site": "00ae78d8",
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
      "00ae799c",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae78f4"
      ]
    ],
    [
      "unmatched:00ae78e0",
      "PARAM",
      [
        "storage",
        "002ae3cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae799c",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae79bc"
      ]
    ],
    [
      "00ae79a8",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae78d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae78c4.md#insn-00ae78d8) · [`00ae78e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae78c4.md#insn-00ae78e8) · [`00ae78f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae78c4.md#insn-00ae78f0)
- 新版 `00ae79a0`（命令位置の公開資料なし）

~~~diff
- 00ae78d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae78d8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae79a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae79a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae78d8 bytes e80000b5
+ 00ae79a0 bytes e80000b5
- 00ae78e8 ["INT_ADD", "register:40f0:8", ["const:ae78e8:8", "const:4:8"]]
- 00ae78e8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae78e8 bytes aad90394
- 00ae78f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00ae78f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae78f0 bytes 605202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f5f7329a7b3c534be78545858fb75ff"></a>

### [`00ae7948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7948.md) → [`00ae7a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a10.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00ae7978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7a40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae795c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae7a20",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae795c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7a44"
      ]
    ],
    [
      "unmatched:00ae7964",
      "PARAM",
      [
        "storage",
        "002ae3cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae7a20",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7a24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7a44"
      ]
    ],
    [
      "00ae7a2c",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae795c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7948.md#insn-00ae795c) · [`00ae7970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7948.md#insn-00ae7970) · [`00ae7978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7948.md#insn-00ae7978)
- 新版 `00ae7a38`（命令位置の公開資料なし）

~~~diff
- 00ae795c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae795c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae795c bytes 080100b5
- 00ae7970 ["INT_ADD", "register:40f0:8", ["const:ae7970:8", "const:4:8"]]
- 00ae7970 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7a38 ["INT_ADD", "register:40f0:8", ["const:ae7a38:8", "const:4:8"]]
+ 00ae7a38 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7970 bytes 88d90394
+ 00ae7a38 bytes 82d90394
- 00ae7978 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00ae7978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7978 bytes 605202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5387528ff7f82a1c58e46ed71196434"></a>

### [`00ae7998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7998.md) → [`00ae7a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a60.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 20.00% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7ae8",
      "incomplete_value": true,
      "site": "00ae7ae8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a20",
      "incomplete_value": true,
      "site": "00ae7a20",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae79f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae7abc"
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
      "00ae7a74",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae79cc",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae79f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7ae0"
      ]
    ]
  ],
  "added": [
    [
      "00ae7a74",
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7a94",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7abc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7ae0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae79d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7998.md#insn-00ae79d8) · [`00ae79ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7998.md#insn-00ae79ec) · [`00ae79f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7998.md#insn-00ae79f4)
- 新版 `00ae7aa0`（命令位置の公開資料なし）

~~~diff
- 00ae79d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae79d8 ["INT_ADD", "register:40f0:8", ["const:ae79d8:8", "const:4:8"]]
- 00ae79d8 ["CALLIND", null, ["register:0:8"]]
+ 00ae7aa0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae7aa0 ["INT_ADD", "register:40f0:8", ["const:ae7aa0:8", "const:4:8"]]
+ 00ae7aa0 ["CALLIND", null, ["register:0:8"]]
- 00ae79d8 bytes 00013fd6
+ 00ae7aa0 bytes 00013fd6
- 00ae79ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae79ec ["INT_ADD", "register:40f0:8", ["const:ae79ec:8", "const:4:8"]]
- 00ae79ec ["CALLIND", null, ["register:0:8"]]
- 00ae79ec bytes 00013fd6
- 00ae79f4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00ae79f4 bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339f31c91210bbf81b6bedb337dd0ee8"></a>

### [`00ae7a34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7a34.md) → [`00ae7afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7afc.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 8.33% / 新版 9.09%

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
      "site": "00ae7a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7ac0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7b38"
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
      "00ae7b10",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7ac4"
      ]
    ],
    [
      "00ae7b1c",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7b10",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7b8c"
      ]
    ],
    [
      "00ae7b1c",
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7a34.md#insn-00ae7a70) · [`00ae7a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7a34.md#insn-00ae7a80) · [`00ae7aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7a34.md#insn-00ae7aa8)

~~~diff
- 00ae7a70 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7a70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7a70 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4a8:8"]]
- 00ae7a70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7a70 bytes bfa21239
- 00ae7a80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7a80 ["INT_ADD", "register:40f0:8", ["const:ae7a80:8", "const:4:8"]]
- 00ae7a80 ["CALLIND", null, ["register:0:8"]]
- 00ae7a80 bytes 00013fd6
- 00ae7aa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7aa8 ["INT_ADD", "register:40f0:8", ["const:ae7aa8:8", "const:4:8"]]
- 00ae7aa8 ["CALLIND", null, ["register:0:8"]]
- 00ae7aa8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63cef0409b8dc3f59d8fdb05948f9d69"></a>

### [`00ae7ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ad4.md) → [`00ae7b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7b9c.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7bdc",
      "incomplete_value": true,
      "site": "00ae7bdc",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b14",
      "incomplete_value": true,
      "site": "00ae7b14",
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
            "const:4a0:8"
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
      "definition_site": "00ae7bb8",
      "incomplete_value": true,
      "site": "00ae7bb8",
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
      "definition_site": "00ae7af0",
      "incomplete_value": true,
      "site": "00ae7af0",
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
      "definition_site": "00ae7bc0",
      "incomplete_value": false,
      "site": "00ae7bd4",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7af8",
      "incomplete_value": false,
      "site": "00ae7b0c",
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
            "const:3cd:8"
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
      "00ae7bb0",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7bc0",
      "PARAM",
      [
        "storage",
        "002ae3cd",
        null,
        "string"
      ]
    ],
    [
      "00ae7bdc",
      "WRITE",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7bb0",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7bc0",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      "00ae7bdc",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ad4.md#insn-00ae7b0c) · [`00ae7b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ad4.md#insn-00ae7b14) · [`00ae7ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ad4.md#insn-00ae7ae8)
- 新版 `00ae7bd4`（命令位置の公開資料なし） · `00ae7bdc`（命令位置の公開資料なし） · `00ae7bb0`（命令位置の公開資料なし）

~~~diff
- 00ae7b0c ["INT_ADD", "register:40f0:8", ["const:ae7b0c:8", "const:4:8"]]
- 00ae7b0c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7bd4 ["INT_ADD", "register:40f0:8", ["const:ae7bd4:8", "const:4:8"]]
+ 00ae7bd4 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7b0c bytes 21d90394
+ 00ae7bd4 bytes 1bd90394
- 00ae7b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00ae7b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7b14 bytes 805202f9
+ 00ae7bdc bytes 80b202f9
- 00ae7ae8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00ae7ae8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7bb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7bb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7ae8 bytes 815242f9
+ 00ae7bb0 bytes 81b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d45efd29cf8bc84a4bb0a16166f1403"></a>

### [`00ae7b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b80.md) → [`00ae7c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c48.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7c88",
      "incomplete_value": true,
      "site": "00ae7c88",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7bc0",
      "incomplete_value": true,
      "site": "00ae7bc0",
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
            "const:4a0:8"
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
      "definition_site": "00ae7c64",
      "incomplete_value": true,
      "site": "00ae7c64",
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
      "definition_site": "00ae7b9c",
      "incomplete_value": true,
      "site": "00ae7b9c",
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
      "definition_site": "00ae7c6c",
      "incomplete_value": false,
      "site": "00ae7c80",
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
            "const:339:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ba4",
      "incomplete_value": false,
      "site": "00ae7bb8",
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
            "const:3cd:8"
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
      "00ae7c5c",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7c6c",
      "PARAM",
      [
        "storage",
        "002ae3cd",
        null,
        "string"
      ]
    ],
    [
      "00ae7c88",
      "WRITE",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7c5c",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7c6c",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      "00ae7c88",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b80.md#insn-00ae7bb8) · [`00ae7bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b80.md#insn-00ae7bc0) · [`00ae7b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7b80.md#insn-00ae7b94)
- 新版 `00ae7c80`（命令位置の公開資料なし） · `00ae7c88`（命令位置の公開資料なし） · `00ae7c5c`（命令位置の公開資料なし）

~~~diff
- 00ae7bb8 ["INT_ADD", "register:40f0:8", ["const:ae7bb8:8", "const:4:8"]]
- 00ae7bb8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7c80 ["INT_ADD", "register:40f0:8", ["const:ae7c80:8", "const:4:8"]]
+ 00ae7c80 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7bb8 bytes f6d80394
+ 00ae7c80 bytes f0d80394
- 00ae7bc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00ae7bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7bc0 bytes 805202f9
+ 00ae7c88 bytes 80b202f9
- 00ae7b94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00ae7b94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7c5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00ae7c5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7b94 bytes 815242f9
+ 00ae7c5c bytes 81b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b37cfe0a24714564755c3731a748772f"></a>

### [`00ae7bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7bf0.md) → [`00ae7cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae7cd4",
      "incomplete_value": false,
      "site": "00ae7cd8",
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
      "definition_site": "00ae7c0c",
      "incomplete_value": false,
      "site": "00ae7c10",
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
      "definition_site": "00ae7ce4",
      "incomplete_value": true,
      "site": "00ae7cf0",
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
      "definition_site": "00ae7c1c",
      "incomplete_value": true,
      "site": "00ae7c28",
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
      "00ae7cd4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae7ce4",
      "DATA",
      [
        "storage",
        "010a04b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7cd4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae7ce4",
      "DATA",
      [
        "storage",
        "010a0578",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7bf0.md#insn-00ae7c10) · [`00ae7c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7bf0.md#insn-00ae7c0c) · [`00ae7c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7bf0.md#insn-00ae7c18)
- 新版 `00ae7cd8`（命令位置の公開資料なし） · `00ae7cd4`（命令位置の公開資料なし） · `00ae7ce0`（命令位置の公開資料なし）

~~~diff
- 00ae7c10 ["INT_ADD", "register:40f0:8", ["const:ae7c10:8", "const:4:8"]]
- 00ae7c10 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae7cd8 ["INT_ADD", "register:40f0:8", ["const:ae7cd8:8", "const:4:8"]]
+ 00ae7cd8 ["CALL", null, ["callee:00bde130:8"]]
- 00ae7c10 bytes 1cd90394
+ 00ae7cd8 bytes 16d90394
- 00ae7c0c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7c0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7c0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7c0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae7cd4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae7cd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7cd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7cd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7c0c bytes 00c81791
+ 00ae7cd4 bytes 00fc1991
- 00ae7c18 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00ae7c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae7ce0 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00ae7ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7c18 bytes 08e11291
+ 00ae7ce0 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6376f54aa040c13b6ef714837a6ac079"></a>

### [`00ae7c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c2c.md) → [`00ae7cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cf4.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae7d20",
      "incomplete_value": true,
      "site": "00ae7d20",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c58",
      "incomplete_value": true,
      "site": "00ae7c58",
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
            "const:4c0:8"
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
      "definition_site": "00ae7d08",
      "incomplete_value": true,
      "site": "00ae7d08",
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
      "definition_site": "00ae7c40",
      "incomplete_value": true,
      "site": "00ae7c40",
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
      "definition_site": "00ae7d14",
      "incomplete_value": false,
      "site": "00ae7d18",
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
            "const:669:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c4c",
      "incomplete_value": false,
      "site": "00ae7c50",
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
            "const:5dc:8"
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
      "00ae7d04",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d14",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae7d20",
      "WRITE",
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
      "00ae7d04",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d14",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7d20",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c2c.md#insn-00ae7c50) · [`00ae7c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c2c.md#insn-00ae7c58) · [`00ae7c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7c2c.md#insn-00ae7c3c)
- 新版 `00ae7d18`（命令位置の公開資料なし） · `00ae7d20`（命令位置の公開資料なし） · `00ae7d04`（命令位置の公開資料なし）

~~~diff
- 00ae7c50 ["INT_ADD", "register:40f0:8", ["const:ae7c50:8", "const:4:8"]]
- 00ae7c50 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7d18 ["INT_ADD", "register:40f0:8", ["const:ae7d18:8", "const:4:8"]]
+ 00ae7d18 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7c50 bytes d0d80394
+ 00ae7d18 bytes cad80394
- 00ae7c58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00ae7c58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7d20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00ae7d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7c58 bytes 606202f9
+ 00ae7d20 bytes 60c202f9
- 00ae7c3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00ae7c3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7d04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00ae7d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7c3c bytes 686242f9
+ 00ae7d04 bytes 68c242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5f8d508abe0e9f7716ab27bcaedb75"></a>

### [`00ae7cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cac.md) → [`00ae7d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae7cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7da4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae7d88",
      "incomplete_value": true,
      "site": "00ae7d88",
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
      "definition_site": "00ae7cc0",
      "incomplete_value": true,
      "site": "00ae7cc0",
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
      "00ae7d84",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7ccc",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7cd4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae7d84",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d94",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7d9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cac.md#insn-00ae7cc0) · [`00ae7cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cac.md#insn-00ae7cd4) · [`00ae7cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cac.md#insn-00ae7cdc)
- 新版 `00ae7d88`（命令位置の公開資料なし）

~~~diff
- 00ae7cc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7cc0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae7d88 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae7d88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7cc0 bytes 080100b5
+ 00ae7d88 bytes 080100b5
- 00ae7cd4 ["INT_ADD", "register:40f0:8", ["const:ae7cd4:8", "const:4:8"]]
- 00ae7cd4 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7cd4 bytes afd80394
- 00ae7cdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00ae7cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7cdc bytes 606202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-927081b28a3e389f2234503ebd6e3176"></a>

### [`00ae7cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cf0.md) → [`00ae7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae7cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7cf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7cf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae7dc8",
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
      "00ae7db8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae7dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae7dc8",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cf0.md#insn-00ae7cf0) · [`00ae7cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cf0.md#insn-00ae7cf4) · [`00ae7d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7cf0.md#insn-00ae7d18)
- 新版 `00ae7de0`（命令位置の公開資料なし）

~~~diff
- 00ae7cf0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae7cf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae7cf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7cf0 bytes f30f1ef8
- 00ae7cf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7cf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7cf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae7cf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7cf4 bytes fd7b01a9
- 00ae7d18 ["INT_ADD", "register:40f0:8", ["const:ae7d18:8", "const:4:8"]]
- 00ae7d18 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7de0 ["INT_ADD", "register:40f0:8", ["const:ae7de0:8", "const:4:8"]]
+ 00ae7de0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7d18 bytes 9ed80394
+ 00ae7de0 bytes 98d80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3c2e3366df8da30fb37248c6f6381a2"></a>

### [`00ae7d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7d40.md) → [`00ae7e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7e08.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 30.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7d40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7d44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7d48",
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
      "00ae7e08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae7e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae7e10",
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

- 旧版 [`00ae7d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7d40.md#insn-00ae7d40) · [`00ae7d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7d40.md#insn-00ae7d44) · [`00ae7d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7d40.md#insn-00ae7d48)

~~~diff
- 00ae7d40 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae7d40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae7d40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7d40 bytes f50f1df8
- 00ae7d44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae7d44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae7d44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae7d44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7d44 bytes f44f01a9
- 00ae7d48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7d48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7d48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae7d48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7d48 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4be8f4e95620cbad5a99606f49adc3"></a>

### [`00ae7ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ddc.md) → [`00ae7ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 50.00% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7e18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7f30",
      "incomplete_value": true,
      "site": "00ae7f30",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7e68",
      "incomplete_value": true,
      "site": "00ae7e68",
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7ee0"
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
      "00ae7eb8",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ec4",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae7e18",
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
      "00ae7eb8",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ec4",
      "READ",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7ee0",
      "WRITE",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ddc.md#insn-00ae7df4) · [`00ae7e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ddc.md#insn-00ae7e14) · [`00ae7e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7ddc.md#insn-00ae7e18)
- 新版 `00ae7ebc`（命令位置の公開資料なし）

~~~diff
- 00ae7df4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7df4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae7ebc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae7ebc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae7df4 bytes c10300b4
+ 00ae7ebc bytes c10300b4
- 00ae7e14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7e14 ["INT_ADD", "register:40f0:8", ["const:ae7e14:8", "const:4:8"]]
- 00ae7e14 ["CALLIND", null, ["register:0:8"]]
- 00ae7e14 bytes 00013fd6
- 00ae7e18 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7e18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7e18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4c8:8"]]
- 00ae7e18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7e18 bytes bf221339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d0ce1ac5b8a3a5db7c5d3ccde1a98f5"></a>

### [`00ae7e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7e7c.md) → [`00ae7f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7f44.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae7ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae7f84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7e98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7e90",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7e98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7f88"
      ]
    ],
    [
      "unmatched:00ae7ea0",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae7f58",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae7f88"
      ]
    ],
    [
      "00ae7f68",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7e7c.md#insn-00ae7e98) · [`00ae7eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7e7c.md#insn-00ae7eb4) · [`00ae7ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7e7c.md#insn-00ae7ebc)
- 新版 `00ae7f7c`（命令位置の公開資料なし）

~~~diff
- 00ae7e98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7e98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7e98 bytes 410100b5
- 00ae7eb4 ["INT_ADD", "register:40f0:8", ["const:ae7eb4:8", "const:4:8"]]
- 00ae7eb4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae7f7c ["INT_ADD", "register:40f0:8", ["const:ae7f7c:8", "const:4:8"]]
+ 00ae7f7c ["CALL", null, ["callee:00bde040:8"]]
- 00ae7eb4 bytes 37d80394
+ 00ae7f7c bytes 31d80394
- 00ae7ebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00ae7ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7ebc bytes 806202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02df887aaf3a5062cb6e12dce4adae4"></a>

### [`00ae7f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f28.md) → [`00ae7ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ff0.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae7f68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8030"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7f44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7f3c",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7f44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8034"
      ]
    ],
    [
      "unmatched:00ae7f4c",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae8004",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae800c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8034"
      ]
    ],
    [
      "00ae8014",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f28.md#insn-00ae7f44) · [`00ae7f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f28.md#insn-00ae7f60) · [`00ae7f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae7/00ae7f28.md#insn-00ae7f68)
- 新版 `00ae8028`（命令位置の公開資料なし）

~~~diff
- 00ae7f44 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7f44 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7f44 bytes 410100b5
- 00ae7f60 ["INT_ADD", "register:40f0:8", ["const:ae7f60:8", "const:4:8"]]
- 00ae7f60 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8028 ["INT_ADD", "register:40f0:8", ["const:ae8028:8", "const:4:8"]]
+ 00ae8028 ["CALL", null, ["callee:00bde040:8"]]
- 00ae7f60 bytes 0cd80394
+ 00ae8028 bytes 06d80394
- 00ae7f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00ae7f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7f68 bytes 806202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49186997ae699a8dc248998ea56c184e"></a>

### [`00ae8014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8014.md) → [`00ae80dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae80dc.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00ae8040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8108"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae80f0",
      "incomplete_value": true,
      "site": "00ae80f0",
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
      "definition_site": "00ae8028",
      "incomplete_value": true,
      "site": "00ae8028",
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
      "00ae80ec",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8030",
      "PARAM",
      [
        "storage",
        "002a8c8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae8038",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae80ec",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae80f8",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae8100",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8014.md#insn-00ae8038) · [`00ae8040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8014.md#insn-00ae8040)
- 新版 `00ae8100`（命令位置の公開資料なし）

~~~diff
- 00ae8038 ["INT_ADD", "register:40f0:8", ["const:ae8038:8", "const:4:8"]]
- 00ae8038 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8038 bytes d6d70394
- 00ae8040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae8040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8040 bytes 607602f9
+ 00ae8100 ["INT_ADD", "register:40f0:8", ["const:ae8100:8", "const:4:8"]]
+ 00ae8100 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8100 bytes d0d70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46319d9fe3925b2ecaf8b997acbfda72"></a>

### [`00ae8054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8054.md) → [`00ae811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae811c.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae8084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae814c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae8130",
      "incomplete_value": true,
      "site": "00ae8130",
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
      "definition_site": "00ae8068",
      "incomplete_value": true,
      "site": "00ae8068",
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
      "00ae812c",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8088"
      ]
    ],
    [
      "unmatched:00ae8074",
      "PARAM",
      [
        "storage",
        "002a8c8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae812c",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8150"
      ]
    ],
    [
      "00ae813c",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8054.md#insn-00ae8068) · [`00ae807c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8054.md#insn-00ae807c) · [`00ae8084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8054.md#insn-00ae8084)
- 新版 `00ae8130`（命令位置の公開資料なし）

~~~diff
- 00ae8068 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8068 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae8130 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae8130 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8068 bytes 080100b5
+ 00ae8130 bytes 080100b5
- 00ae807c ["INT_ADD", "register:40f0:8", ["const:ae807c:8", "const:4:8"]]
- 00ae807c ["CALL", null, ["callee:00bde040:8"]]
- 00ae807c bytes c5d70394
- 00ae8084 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae8084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8084 bytes 607602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16825224a963528f5c21497ba5477a48"></a>

### [`00ae8098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8098.md) → [`00ae8160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8160.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae80c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8190"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8174",
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
      "definition_site": "00ae80ac",
      "incomplete_value": true,
      "site": "00ae80ac",
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
      "00ae8170",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae80b4",
      "PARAM",
      [
        "storage",
        "002a8c8c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae80c8",
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
      "00ae8170",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae817c",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae8190",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae80ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8098.md#insn-00ae80ac) · [`00ae80c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8098.md#insn-00ae80c0) · [`00ae80c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8098.md#insn-00ae80c8)
- 新版 `00ae8174`（命令位置の公開資料なし） · `00ae8188`（命令位置の公開資料なし）

~~~diff
- 00ae80ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae80ac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae8174 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae8174 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae80ac bytes 080100b5
+ 00ae8174 bytes 080100b5
- 00ae80c0 ["INT_ADD", "register:40f0:8", ["const:ae80c0:8", "const:4:8"]]
- 00ae80c0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8188 ["INT_ADD", "register:40f0:8", ["const:ae8188:8", "const:4:8"]]
+ 00ae8188 ["CALL", null, ["callee:00bde040:8"]]
- 00ae80c0 bytes b4d70394
+ 00ae8188 bytes aed70394
- 00ae80c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
- 00ae80c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae80c8 bytes 607602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec48eedf6dbd6c299c2ff52c76a732b5"></a>

### [`00ae80e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae80e8.md) → [`00ae81b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae81b0.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8238",
      "incomplete_value": true,
      "site": "00ae8238",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8170",
      "incomplete_value": true,
      "site": "00ae8170",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae81e4",
      "incomplete_value": true,
      "site": "00ae81f0",
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
                "const:5a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae811c",
      "incomplete_value": true,
      "site": "00ae8128",
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
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8164"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae81c4",
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae81e4",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8238",
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
      "00ae81c4",
      "READ",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae81e4",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8238",
      "WRITE",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae80e8.md#insn-00ae8128) · [`00ae8164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae80e8.md#insn-00ae8164) · [`00ae8170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae80e8.md#insn-00ae8170)
- 新版 `00ae81f0`（命令位置の公開資料なし） · `00ae8238`（命令位置の公開資料なし）

~~~diff
- 00ae8128 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8128 ["INT_ADD", "register:40f0:8", ["const:ae8128:8", "const:4:8"]]
- 00ae8128 ["CALLIND", null, ["register:0:8"]]
+ 00ae81f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae81f0 ["INT_ADD", "register:40f0:8", ["const:ae81f0:8", "const:4:8"]]
+ 00ae81f0 ["CALLIND", null, ["register:0:8"]]
- 00ae8128 bytes 00013fd6
+ 00ae81f0 bytes 00013fd6
- 00ae8164 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8164 ["INT_ADD", "register:40f0:8", ["const:ae8164:8", "const:4:8"]]
- 00ae8164 ["CALLIND", null, ["register:0:8"]]
- 00ae8164 bytes 00013fd6
- 00ae8170 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae8170 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4f0:8"]]
- 00ae8170 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae8238 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae8238 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5b0:8"]]
+ 00ae8238 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae8170 bytes a0c21339
+ 00ae8238 bytes a0c21639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1055d4ce82205141fdfa894fea5493a4"></a>

### [`00ae8184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8184.md) → [`00ae824c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae824c.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8188"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8184",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8188",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae818c",
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
      "00ae824c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae8250",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8254",
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

- 旧版 [`00ae8184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8184.md#insn-00ae8184) · [`00ae8188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8184.md#insn-00ae8188) · [`00ae818c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8184.md#insn-00ae818c)

~~~diff
- 00ae8184 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae8184 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae8184 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8184 bytes f50f1df8
- 00ae8188 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae8188 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae8188 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8188 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8188 bytes f44f01a9
- 00ae818c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae818c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae818c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae818c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae818c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2260cc2a018e2979f0b4b20a9ce0710f"></a>

### [`00ae8224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8224.md) → [`00ae82ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae82ec.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae8264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae832c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8240"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8238",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8240",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8330"
      ]
    ],
    [
      "unmatched:00ae8248",
      "PARAM",
      [
        "storage",
        "002a8c8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae8300",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8330"
      ]
    ],
    [
      "00ae8310",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8224.md#insn-00ae8240) · [`00ae825c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8224.md#insn-00ae825c) · [`00ae8264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8224.md#insn-00ae8264)
- 新版 `00ae8324`（命令位置の公開資料なし）

~~~diff
- 00ae8240 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8240 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8240 bytes 410100b5
- 00ae825c ["INT_ADD", "register:40f0:8", ["const:ae825c:8", "const:4:8"]]
- 00ae825c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8324 ["INT_ADD", "register:40f0:8", ["const:ae8324:8", "const:4:8"]]
+ 00ae8324 ["CALL", null, ["callee:00bde040:8"]]
- 00ae825c bytes 4dd70394
+ 00ae8324 bytes 47d70394
- 00ae8264 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00ae8264 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8264 bytes 807602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85ea30673770f7fbb32aee8db72d1eaf"></a>

### [`00ae82d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae82d0.md) → [`00ae8398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8398.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae8310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae83d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae82ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae82e4",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae82ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae83dc"
      ]
    ],
    [
      "unmatched:00ae82f4",
      "PARAM",
      [
        "storage",
        "002a8c8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae83ac",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae83b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae83dc"
      ]
    ],
    [
      "00ae83bc",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae82ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae82d0.md#insn-00ae82ec) · [`00ae8308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae82d0.md#insn-00ae8308) · [`00ae8310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae82d0.md#insn-00ae8310)
- 新版 `00ae83d0`（命令位置の公開資料なし）

~~~diff
- 00ae82ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae82ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae82ec bytes 410100b5
- 00ae8308 ["INT_ADD", "register:40f0:8", ["const:ae8308:8", "const:4:8"]]
- 00ae8308 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae83d0 ["INT_ADD", "register:40f0:8", ["const:ae83d0:8", "const:4:8"]]
+ 00ae83d0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8308 bytes 22d70394
+ 00ae83d0 bytes 1cd70394
- 00ae8310 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
- 00ae8310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8310 bytes 807602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e50676b6bf4c29d99045374b7f4eef5"></a>

### [`00ae8340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8340.md) → [`00ae8408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8408.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae8424",
      "incomplete_value": false,
      "site": "00ae8428",
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
      "definition_site": "00ae835c",
      "incomplete_value": false,
      "site": "00ae8360",
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
      "definition_site": "00ae8434",
      "incomplete_value": true,
      "site": "00ae8440",
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
      "definition_site": "00ae836c",
      "incomplete_value": true,
      "site": "00ae8378",
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
      "00ae8424",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae8434",
      "DATA",
      [
        "storage",
        "010a0540",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae8424",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae8434",
      "DATA",
      [
        "storage",
        "010a0600",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8340.md#insn-00ae8360) · [`00ae835c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8340.md#insn-00ae835c) · [`00ae8368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8340.md#insn-00ae8368)
- 新版 `00ae8428`（命令位置の公開資料なし） · `00ae8424`（命令位置の公開資料なし） · `00ae8430`（命令位置の公開資料なし）

~~~diff
- 00ae8360 ["INT_ADD", "register:40f0:8", ["const:ae8360:8", "const:4:8"]]
- 00ae8360 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae8428 ["INT_ADD", "register:40f0:8", ["const:ae8428:8", "const:4:8"]]
+ 00ae8428 ["CALL", null, ["callee:00bde130:8"]]
- 00ae8360 bytes 48d70394
+ 00ae8428 bytes 42d70394
- 00ae835c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae835c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae835c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae835c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae8424 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae8424 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8424 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8424 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae835c bytes 00c81791
+ 00ae8424 bytes 00fc1991
- 00ae8368 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00ae8368 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8368 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8368 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae8430 ["COPY", "tmp:0:8", ["const:600:8"]]
+ 00ae8430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8368 bytes 08011591
+ 00ae8430 bytes 08011891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0bac0f2db9303fc07242599950a7a1a"></a>

### [`00ae83bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83bc.md) → [`00ae8484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8484.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 20.00% / 新版 33.33%

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
      "site": "00ae83e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae84b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae8498",
      "incomplete_value": true,
      "site": "00ae8498",
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
      "definition_site": "00ae83d0",
      "incomplete_value": true,
      "site": "00ae83d0",
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
      "00ae8494",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae83d8",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae83e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae8494",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae84a0",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae84a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae83d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83bc.md#insn-00ae83d0) · [`00ae83e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83bc.md#insn-00ae83e0) · [`00ae83e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83bc.md#insn-00ae83e8)
- 新版 `00ae8498`（命令位置の公開資料なし）

~~~diff
- 00ae83d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae83d0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00ae8498 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae8498 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae83d0 bytes e80000b5
+ 00ae8498 bytes e80000b5
- 00ae83e0 ["INT_ADD", "register:40f0:8", ["const:ae83e0:8", "const:4:8"]]
- 00ae83e0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae83e0 bytes ecd60394
- 00ae83e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00ae83e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae83e8 bytes 60a602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c97a74843acb40e89d0941243afc8186"></a>

### [`00ae83fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83fc.md) → [`00ae84c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae84c4.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae842c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae84f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae84d8",
      "incomplete_value": true,
      "site": "00ae84d8",
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
      "definition_site": "00ae8410",
      "incomplete_value": true,
      "site": "00ae8410",
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
      "00ae84d4",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae841c",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae8424",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae84d4",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae84e4",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae84ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83fc.md#insn-00ae8410) · [`00ae8424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83fc.md#insn-00ae8424) · [`00ae842c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae83fc.md#insn-00ae842c)
- 新版 `00ae84d8`（命令位置の公開資料なし）

~~~diff
- 00ae8410 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8410 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae84d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae84d8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8410 bytes 080100b5
+ 00ae84d8 bytes 080100b5
- 00ae8424 ["INT_ADD", "register:40f0:8", ["const:ae8424:8", "const:4:8"]]
- 00ae8424 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8424 bytes dbd60394
- 00ae842c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00ae842c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae842c bytes 60a602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80c4daf1e421ce1b930f2e3d28e75145"></a>

### [`00ae8440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8440.md) → [`00ae8508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8508.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae8470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8538"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae851c",
      "incomplete_value": true,
      "site": "00ae851c",
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
      "definition_site": "00ae8454",
      "incomplete_value": true,
      "site": "00ae8454",
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
      "00ae8518",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae845c",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae8470",
      "WRITE",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8518",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8524",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae8538",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8440.md#insn-00ae8454) · [`00ae8468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8440.md#insn-00ae8468) · [`00ae8470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8440.md#insn-00ae8470)
- 新版 `00ae851c`（命令位置の公開資料なし） · `00ae8530`（命令位置の公開資料なし）

~~~diff
- 00ae8454 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8454 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae851c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae851c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8454 bytes 080100b5
+ 00ae851c bytes 080100b5
- 00ae8468 ["INT_ADD", "register:40f0:8", ["const:ae8468:8", "const:4:8"]]
- 00ae8468 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8530 ["INT_ADD", "register:40f0:8", ["const:ae8530:8", "const:4:8"]]
+ 00ae8530 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8468 bytes cad60394
+ 00ae8530 bytes c4d60394
- 00ae8470 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
- 00ae8470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8470 bytes 60a602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f66d8f64ee893f30bab0eb307394e98a"></a>

### [`00ae852c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae852c.md) → [`00ae85f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae85f4.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

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
      "site": "00ae852c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8530"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8530"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae852c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8530",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8534",
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
      "00ae85f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae85f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae85fc",
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

- 旧版 [`00ae852c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae852c.md#insn-00ae852c) · [`00ae8530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae852c.md#insn-00ae8530) · [`00ae8534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae852c.md#insn-00ae8534)

~~~diff
- 00ae852c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae852c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae852c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae852c bytes f50f1df8
- 00ae8530 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae8530 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae8530 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8530 bytes f44f01a9
- 00ae8534 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8534 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8534 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae8534 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8534 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe11e3c072e5ce4a689affccbd307e9a"></a>

### [`00ae85cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae85cc.md) → [`00ae8694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8694.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae85cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae85cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae85d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae85cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae85d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae85e0",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8698",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae86a8",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae85cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae85cc.md#insn-00ae85cc) · [`00ae85d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae85cc.md#insn-00ae85d0) · [`00ae85e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae85cc.md#insn-00ae85e8)

~~~diff
- 00ae85cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae85cc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae85cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae85cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae85cc bytes f44fbea9
- 00ae85d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae85d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae85d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae85d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae85d0 bytes fd7b01a9
- 00ae85e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae85e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae85e8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b391c665dda15c21dd891629621e7577"></a>

### [`00ae8678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8678.md) → [`00ae8740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8740.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae86b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8780"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8694"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae868c",
      "READ",
      [
        "storage",
        "010a0548",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8694",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8784"
      ]
    ],
    [
      "unmatched:00ae869c",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae8754",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae875c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8784"
      ]
    ],
    [
      "00ae8764",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8678.md#insn-00ae8694) · [`00ae86b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8678.md#insn-00ae86b0) · [`00ae86b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8678.md#insn-00ae86b8)
- 新版 `00ae8778`（命令位置の公開資料なし）

~~~diff
- 00ae8694 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8694 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8694 bytes 410100b5
- 00ae86b0 ["INT_ADD", "register:40f0:8", ["const:ae86b0:8", "const:4:8"]]
- 00ae86b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8778 ["INT_ADD", "register:40f0:8", ["const:ae8778:8", "const:4:8"]]
+ 00ae8778 ["CALL", null, ["callee:00bde040:8"]]
- 00ae86b0 bytes 38d60394
+ 00ae8778 bytes 32d60394
- 00ae86b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
- 00ae86b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae86b8 bytes 80a602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0188988a0ccb073ee204d25a9ddbf2b6"></a>

### [`00ae87e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87e8.md) → [`00ae88b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae88b0.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae87e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae87ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae87ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae87e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae87ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae87f8",
      "READ",
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
      "00ae88b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae88b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae88c0",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae87e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87e8.md#insn-00ae87e8) · [`00ae87ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87e8.md#insn-00ae87ec) · [`00ae87fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae87e8.md#insn-00ae87fc)

~~~diff
- 00ae87e8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae87e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae87e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae87e8 bytes f30f1ef8
- 00ae87ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae87ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae87ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae87ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae87ec bytes fd7b01a9
- 00ae87fc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae87fc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae87fc bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d8a1fee0a12fc82214eb038fb94fa83"></a>

### [`00ae8a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8a20.md) → [`00ae8ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ae8.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae8a60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8b28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8a3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8a34",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8a3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8b2c"
      ]
    ],
    [
      "unmatched:00ae8a44",
      "PARAM",
      [
        "storage",
        "002aafea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae8afc",
      "READ",
      [
        "storage",
        "010a0630",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8b04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8b2c"
      ]
    ],
    [
      "00ae8b0c",
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8a20.md#insn-00ae8a3c) · [`00ae8a58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8a20.md#insn-00ae8a58) · [`00ae8a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8a20.md#insn-00ae8a60)
- 新版 `00ae8b20`（命令位置の公開資料なし）

~~~diff
- 00ae8a3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8a3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8a3c bytes 410100b5
- 00ae8a58 ["INT_ADD", "register:40f0:8", ["const:ae8a58:8", "const:4:8"]]
- 00ae8a58 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8b20 ["INT_ADD", "register:40f0:8", ["const:ae8b20:8", "const:4:8"]]
+ 00ae8b20 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8a58 bytes 4ed50394
+ 00ae8b20 bytes 48d50394
- 00ae8a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00ae8a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8a60 bytes 80ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65cc4afa8e13f0675fe3b2203753f939"></a>

### [`00ae8acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8acc.md) → [`00ae8b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8b94.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae8af8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8bc0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae8ba8",
      "incomplete_value": true,
      "site": "00ae8ba8",
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
      "definition_site": "00ae8ae0",
      "incomplete_value": true,
      "site": "00ae8ae0",
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
      "00ae8ba4",
      "READ",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8aec",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae8af0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae8ba4",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8bb4",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8bb8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8acc.md#insn-00ae8ae0) · [`00ae8af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8acc.md#insn-00ae8af0) · [`00ae8af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8acc.md#insn-00ae8af8)
- 新版 `00ae8ba8`（命令位置の公開資料なし）

~~~diff
- 00ae8ae0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8ae0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae8ba8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae8ba8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8ae0 bytes e80000b5
+ 00ae8ba8 bytes e80000b5
- 00ae8af0 ["INT_ADD", "register:40f0:8", ["const:ae8af0:8", "const:4:8"]]
- 00ae8af0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8af0 bytes 28d50394
- 00ae8af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00ae8af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8af8 bytes 60ce02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30120dea48274c052f4e0e9af0dff7bf"></a>

### [`00ae8b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b0c.md) → [`00ae8bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8bd4.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8b0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8b10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8b10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8b0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8b10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8b1c",
      "READ",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8bd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8bd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae8be4",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b0c.md#insn-00ae8b0c) · [`00ae8b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b0c.md#insn-00ae8b10) · [`00ae8b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b0c.md#insn-00ae8b20)

~~~diff
- 00ae8b0c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae8b0c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8b0c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8b0c bytes f30f1ef8
- 00ae8b10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8b10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8b10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8b10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8b10 bytes fd7b01a9
- 00ae8b20 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8b20 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae8b20 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc0aadb60e49e29c60dab20d9d9a1902"></a>

### [`00ae8b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b90.md) → [`00ae8c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c58.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae8c88",
      "incomplete_value": true,
      "site": "00ae8c88",
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
    "old": {
      "definition_site": "00ae8bc0",
      "incomplete_value": true,
      "site": "00ae8bc0",
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
      "definition_site": "00ae8c6c",
      "incomplete_value": true,
      "site": "00ae8c6c",
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
      "definition_site": "00ae8ba4",
      "incomplete_value": true,
      "site": "00ae8ba4",
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
      "definition_site": "00ae8c74",
      "incomplete_value": false,
      "site": "00ae8c80",
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
            "const:67b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bac",
      "incomplete_value": false,
      "site": "00ae8bb8",
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
            "const:5ee:8"
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
      "00ae8c68",
      "READ",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8c74",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00ae8c88",
      "WRITE",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8c68",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8c74",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ],
    [
      "00ae8c88",
      "WRITE",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b90.md#insn-00ae8bb8) · [`00ae8bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b90.md#insn-00ae8bc0) · [`00ae8ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8b90.md#insn-00ae8ba0)
- 新版 `00ae8c80`（命令位置の公開資料なし） · `00ae8c88`（命令位置の公開資料なし） · `00ae8c68`（命令位置の公開資料なし）

~~~diff
- 00ae8bb8 ["INT_ADD", "register:40f0:8", ["const:ae8bb8:8", "const:4:8"]]
- 00ae8bb8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8c80 ["INT_ADD", "register:40f0:8", ["const:ae8c80:8", "const:4:8"]]
+ 00ae8c80 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8bb8 bytes f6d40394
+ 00ae8c80 bytes f0d40394
- 00ae8bc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00ae8bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00ae8c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8bc0 bytes 60ce02f9
+ 00ae8c88 bytes 602e03f9
- 00ae8ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:598:8"]]
- 00ae8ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8c68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:658:8"]]
+ 00ae8c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8ba0 bytes 68ce42f9
+ 00ae8c68 bytes 682e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7af0ca6ec74edb39f34384546e6814"></a>

### [`00ae8bd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8bd4.md) → [`00ae8c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8c9c.md) _ZN8firebase4util11class_class8GetClassEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00ae8ca0",
      "incomplete_value": true,
      "site": "00ae8ca4",
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
                "const:658:8"
              ]
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
      "unmatched:00ae8bd8",
      "READ",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8ca0",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8bd4.md#insn-00ae8bd8)
- 新版 `00ae8ca0`（命令位置の公開資料なし）

~~~diff
- 00ae8bd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:598:8"]]
- 00ae8bd8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8bd8 bytes 00cd42f9
+ 00ae8ca0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:658:8"]]
+ 00ae8ca0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8ca0 bytes 002d43f9
~~~


<a id="compare-fc26ab39c5b90f4be39d477d8d29ea8c"></a>

### [`00ae8d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8d1c.md) → [`00ae8de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8de4.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8d20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8d1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8d30",
      "READ",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8de4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8de8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae8df8",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8d1c.md#insn-00ae8d1c) · [`00ae8d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8d1c.md#insn-00ae8d20) · [`00ae8d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8d1c.md#insn-00ae8d38)

~~~diff
- 00ae8d1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae8d1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae8d1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8d1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8d1c bytes f44fbea9
- 00ae8d20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8d20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8d20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8d20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8d20 bytes fd7b01a9
- 00ae8d38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8d38 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ae8d38 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c1716ba27d2ce284b7b8dc180ed1340"></a>

### [`00ae8dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8dc8.md) → [`00ae8e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8e90.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae8e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae8ed0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8de4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8ddc",
      "READ",
      [
        "storage",
        "010a0598",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8de4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8ed4"
      ]
    ],
    [
      "unmatched:00ae8dec",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae8ea4",
      "READ",
      [
        "storage",
        "010a0658",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8eac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae8ed4"
      ]
    ],
    [
      "00ae8eb4",
      "PARAM",
      [
        "storage",
        "0029867b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8de4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8dc8.md#insn-00ae8de4) · [`00ae8e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8dc8.md#insn-00ae8e00) · [`00ae8e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8dc8.md#insn-00ae8e08)
- 新版 `00ae8ec8`（命令位置の公開資料なし）

~~~diff
- 00ae8de4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8de4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8de4 bytes 410100b5
- 00ae8e00 ["INT_ADD", "register:40f0:8", ["const:ae8e00:8", "const:4:8"]]
- 00ae8e00 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae8ec8 ["INT_ADD", "register:40f0:8", ["const:ae8ec8:8", "const:4:8"]]
+ 00ae8ec8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8e00 bytes 64d40394
+ 00ae8ec8 bytes 5ed40394
- 00ae8e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:598:8"]]
- 00ae8e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8e08 bytes 80ce02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f143186733447a06cbcf7c393f38ec7f"></a>

### [`00ae8eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8eb4.md) → [`00ae8f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8f7c.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae8eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8eb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8eb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae8f8c",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae8f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae8f8c",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8eb4.md#insn-00ae8eb4) · [`00ae8eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8eb4.md#insn-00ae8eb8) · [`00ae8ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8eb4.md#insn-00ae8ec8)
- 新版 `00ae8f90`（命令位置の公開資料なし）

~~~diff
- 00ae8eb4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae8eb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8eb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8eb4 bytes f30f1ef8
- 00ae8eb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8eb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8eb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8eb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8eb8 bytes fd7b01a9
- 00ae8ec8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8ec8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae8f90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae8f90 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8ec8 bytes e80000b5
+ 00ae8f90 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-868945682f93a1dea0975eefd76c454b"></a>

### [`00ae8f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8f38.md) → [`00ae9000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9000.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9030",
      "incomplete_value": true,
      "site": "00ae9030",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f68",
      "incomplete_value": true,
      "site": "00ae8f68",
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
      "definition_site": "00ae9014",
      "incomplete_value": true,
      "site": "00ae9014",
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
      "definition_site": "00ae8f4c",
      "incomplete_value": true,
      "site": "00ae8f4c",
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
      "definition_site": "00ae901c",
      "incomplete_value": false,
      "site": "00ae9028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:e51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f54",
      "incomplete_value": false,
      "site": "00ae8f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:dc4:8"
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
      "00ae9010",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae901c",
      "PARAM",
      [
        "storage",
        "0029edc4",
        null,
        "string"
      ]
    ],
    [
      "00ae9030",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9010",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae901c",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ],
    [
      "00ae9030",
      "WRITE",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8f38.md#insn-00ae8f60) · [`00ae8f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8f38.md#insn-00ae8f68) · [`00ae8f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae8f38.md#insn-00ae8f48)
- 新版 `00ae9028`（命令位置の公開資料なし） · `00ae9030`（命令位置の公開資料なし） · `00ae9010`（命令位置の公開資料なし）

~~~diff
- 00ae8f60 ["INT_ADD", "register:40f0:8", ["const:ae8f60:8", "const:4:8"]]
- 00ae8f60 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9028 ["INT_ADD", "register:40f0:8", ["const:ae9028:8", "const:4:8"]]
+ 00ae9028 ["CALL", null, ["callee:00bde040:8"]]
- 00ae8f60 bytes 0cd40394
+ 00ae9028 bytes 06d40394
- 00ae8f68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae8f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00ae9030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8f68 bytes 60e202f9
+ 00ae9030 bytes 604203f9
- 00ae8f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae8f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00ae9010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8f48 bytes 68e242f9
+ 00ae9010 bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31bd5bf8bd3acc6038197c56b7f7ab6b"></a>

### [`00ae9024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9024.md) → [`00ae90ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae90ec.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 33.33% / 新版 27.27%

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
      "site": "00ae9060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae9178",
      "incomplete_value": true,
      "site": "00ae9178",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae90b0",
      "incomplete_value": true,
      "site": "00ae90b0",
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9128"
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
      "00ae9100",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae910c",
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9114",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae9064"
      ]
    ]
  ],
  "added": [
    [
      "00ae9100",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae910c",
      "READ",
      [
        "storage",
        "010a0688",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae9114",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae912c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9024.md#insn-00ae903c) · [`00ae9060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9024.md#insn-00ae9060) · [`00ae9070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9024.md#insn-00ae9070)
- 新版 `00ae9104`（命令位置の公開資料なし）

~~~diff
- 00ae903c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae903c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00ae9104 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae9104 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae903c bytes c10300b4
+ 00ae9104 bytes c10300b4
- 00ae9060 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9060 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9060 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
- 00ae9060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9060 bytes bf221739
- 00ae9070 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9070 ["INT_ADD", "register:40f0:8", ["const:ae9070:8", "const:4:8"]]
- 00ae9070 ["CALLIND", null, ["register:0:8"]]
- 00ae9070 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b50819b29c7c5653714b6b7e008b2302"></a>

### [`00ae90c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae90c4.md) → [`00ae918c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae918c.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae9104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae91cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae90e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae90d8",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae90e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae91d0"
      ]
    ],
    [
      "unmatched:00ae90e8",
      "PARAM",
      [
        "storage",
        "0029edc4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae91a0",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae91a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae91d0"
      ]
    ],
    [
      "00ae91b0",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae90e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae90c4.md#insn-00ae90e0) · [`00ae90fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae90c4.md#insn-00ae90fc) · [`00ae9104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae90c4.md#insn-00ae9104)
- 新版 `00ae91c4`（命令位置の公開資料なし）

~~~diff
- 00ae90e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae90e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae90e0 bytes 410100b5
- 00ae90fc ["INT_ADD", "register:40f0:8", ["const:ae90fc:8", "const:4:8"]]
- 00ae90fc ["CALL", null, ["callee:00bde040:8"]]
+ 00ae91c4 ["INT_ADD", "register:40f0:8", ["const:ae91c4:8", "const:4:8"]]
+ 00ae91c4 ["CALL", null, ["callee:00bde040:8"]]
- 00ae90fc bytes a5d30394
+ 00ae91c4 bytes 9fd30394
- 00ae9104 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae9104 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9104 bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbf3da1d5f15f4cb368af57df6dc000d"></a>

### [`00ae9134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9134.md) → [`00ae91fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae91fc.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae9218",
      "incomplete_value": false,
      "site": "00ae921c",
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
      "definition_site": "00ae9150",
      "incomplete_value": false,
      "site": "00ae9154",
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
      "definition_site": "00ae9228",
      "incomplete_value": true,
      "site": "00ae9234",
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
      "definition_site": "00ae9160",
      "incomplete_value": true,
      "site": "00ae916c",
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
      "00ae9218",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae9228",
      "DATA",
      [
        "storage",
        "010a05d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae9218",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae9228",
      "DATA",
      [
        "storage",
        "010a0690",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9134.md#insn-00ae9154) · [`00ae9150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9134.md#insn-00ae9150) · [`00ae915c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9134.md#insn-00ae915c)
- 新版 `00ae921c`（命令位置の公開資料なし） · `00ae9218`（命令位置の公開資料なし） · `00ae9224`（命令位置の公開資料なし）

~~~diff
- 00ae9154 ["INT_ADD", "register:40f0:8", ["const:ae9154:8", "const:4:8"]]
- 00ae9154 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae921c ["INT_ADD", "register:40f0:8", ["const:ae921c:8", "const:4:8"]]
+ 00ae921c ["CALL", null, ["callee:00bde130:8"]]
- 00ae9154 bytes cbd30394
+ 00ae921c bytes c5d30394
- 00ae9150 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae9150 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9150 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9150 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9218 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae9218 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9218 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9218 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9150 bytes 001c1591
+ 00ae9218 bytes 00501791
- 00ae915c ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00ae915c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae915c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae915c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9224 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00ae9224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae915c bytes 08411791
+ 00ae9224 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e671c85d20f4e388d9fe8b65256d90"></a>

### [`00ae9170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9170.md) → [`00ae9238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9238.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae91b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9278"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae918c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9184",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae918c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae927c"
      ]
    ],
    [
      "unmatched:00ae9194",
      "PARAM",
      [
        "storage",
        "0029edc4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae924c",
      "READ",
      [
        "storage",
        "010a0680",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9254",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae927c"
      ]
    ],
    [
      "00ae925c",
      "PARAM",
      [
        "storage",
        "0029ee51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae918c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9170.md#insn-00ae918c) · [`00ae91a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9170.md#insn-00ae91a8) · [`00ae91b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9170.md#insn-00ae91b0)
- 新版 `00ae9270`（命令位置の公開資料なし）

~~~diff
- 00ae918c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae918c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae918c bytes 410100b5
- 00ae91a8 ["INT_ADD", "register:40f0:8", ["const:ae91a8:8", "const:4:8"]]
- 00ae91a8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9270 ["INT_ADD", "register:40f0:8", ["const:ae9270:8", "const:4:8"]]
+ 00ae9270 ["CALL", null, ["callee:00bde040:8"]]
- 00ae91a8 bytes 7ad30394
+ 00ae9270 bytes 74d30394
- 00ae91b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae91b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae91b0 bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5559f2f847bf76640c91ef3bd6c9673d"></a>

### [`00ae91e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae91e0.md) → [`00ae92a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92a8.md) _ZN8firebase4util16content_resolver10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae92c4",
      "incomplete_value": false,
      "site": "00ae92c8",
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
      "definition_site": "00ae91fc",
      "incomplete_value": false,
      "site": "00ae9200",
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
      "definition_site": "00ae92d4",
      "incomplete_value": true,
      "site": "00ae92e0",
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
      "definition_site": "00ae920c",
      "incomplete_value": true,
      "site": "00ae9218",
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
      "00ae92c4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae92d4",
      "DATA",
      [
        "storage",
        "010a05e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae92c4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae92d4",
      "DATA",
      [
        "storage",
        "010a06a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae91e0.md#insn-00ae9200) · [`00ae91fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae91e0.md#insn-00ae91fc) · [`00ae9208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae91e0.md#insn-00ae9208)
- 新版 `00ae92c8`（命令位置の公開資料なし） · `00ae92c4`（命令位置の公開資料なし） · `00ae92d0`（命令位置の公開資料なし）

~~~diff
- 00ae9200 ["INT_ADD", "register:40f0:8", ["const:ae9200:8", "const:4:8"]]
- 00ae9200 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae92c8 ["INT_ADD", "register:40f0:8", ["const:ae92c8:8", "const:4:8"]]
+ 00ae92c8 ["CALL", null, ["callee:00bde130:8"]]
- 00ae9200 bytes a0d30394
+ 00ae92c8 bytes 9ad30394
- 00ae91fc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae91fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae91fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae91fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae92c4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae92c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae92c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae92c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae91fc bytes 00c81791
+ 00ae92c4 bytes 00fc1991
- 00ae9208 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00ae9208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae92d0 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00ae92d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae92d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae92d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9208 bytes 08811791
+ 00ae92d0 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02f4a92265cfd614ee5d0df38facef70"></a>

### [`00ae921c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae921c.md) → [`00ae92e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae92e4.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae9248"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9310"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae92f8",
      "incomplete_value": true,
      "site": "00ae92f8",
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
      "definition_site": "00ae9230",
      "incomplete_value": true,
      "site": "00ae9230",
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
      "00ae92f4",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae923c",
      "PARAM",
      [
        "storage",
        "0029dcc7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae9240",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae92f4",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9304",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9308",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae921c.md#insn-00ae9230) · [`00ae9240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae921c.md#insn-00ae9240) · [`00ae9248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae921c.md#insn-00ae9248)
- 新版 `00ae92f8`（命令位置の公開資料なし）

~~~diff
- 00ae9230 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae9230 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae92f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae92f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9230 bytes e80000b5
+ 00ae92f8 bytes e80000b5
- 00ae9240 ["INT_ADD", "register:40f0:8", ["const:ae9240:8", "const:4:8"]]
- 00ae9240 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9240 bytes 54d30394
- 00ae9248 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae9248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9248 bytes 60f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab042015ef21a530d218ea9e8b08eb46"></a>

### [`00ae925c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae925c.md) → [`00ae9324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9324.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae9288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9350"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae9338",
      "incomplete_value": true,
      "site": "00ae9338",
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
      "definition_site": "00ae9270",
      "incomplete_value": true,
      "site": "00ae9270",
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
      "00ae9334",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9278",
      "PARAM",
      [
        "storage",
        "0029dcc7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae9280",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae9334",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9340",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9348",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae925c.md#insn-00ae9270) · [`00ae9280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae925c.md#insn-00ae9280) · [`00ae9288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae925c.md#insn-00ae9288)
- 新版 `00ae9338`（命令位置の公開資料なし）

~~~diff
- 00ae9270 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae9270 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae9338 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae9338 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9270 bytes e80000b5
+ 00ae9338 bytes e80000b5
- 00ae9280 ["INT_ADD", "register:40f0:8", ["const:ae9280:8", "const:4:8"]]
- 00ae9280 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9280 bytes 44d30394
- 00ae9288 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae9288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9288 bytes 60f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d2f30815b6164736be7c6e43f110b81"></a>

### [`00ae929c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae929c.md) → [`00ae9364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9364.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9394",
      "incomplete_value": true,
      "site": "00ae9394",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae92cc",
      "incomplete_value": true,
      "site": "00ae92cc",
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
            "const:5e8:8"
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
      "definition_site": "00ae9378",
      "incomplete_value": true,
      "site": "00ae9378",
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
      "definition_site": "00ae92b0",
      "incomplete_value": true,
      "site": "00ae92b0",
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
      "definition_site": "00ae9384",
      "incomplete_value": false,
      "site": "00ae938c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:d54:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae92bc",
      "incomplete_value": false,
      "site": "00ae92c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:cc7:8"
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
      "00ae9374",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9384",
      "PARAM",
      [
        "storage",
        "0029dcc7",
        null,
        "string"
      ]
    ],
    [
      "00ae9394",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9374",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9384",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9394",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae92c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae929c.md#insn-00ae92c4) · [`00ae92cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae929c.md#insn-00ae92cc) · [`00ae92ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae929c.md#insn-00ae92ac)
- 新版 `00ae938c`（命令位置の公開資料なし） · `00ae9394`（命令位置の公開資料なし） · `00ae9374`（命令位置の公開資料なし）

~~~diff
- 00ae92c4 ["INT_ADD", "register:40f0:8", ["const:ae92c4:8", "const:4:8"]]
- 00ae92c4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
+ 00ae938c ["CALL", null, ["callee:00bde040:8"]]
- 00ae92c4 bytes 33d30394
+ 00ae938c bytes 2dd30394
- 00ae92cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae92cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00ae9394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae92cc bytes 60f602f9
+ 00ae9394 bytes 605603f9
- 00ae92ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae92ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9374 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00ae9374 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae92ac bytes 68f642f9
+ 00ae9374 bytes 685643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ff4ae253b564585040a5b2bb532621e"></a>

### [`00ae92e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae92e0.md) → [`00ae93a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93a8.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00ae9310"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae93d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae93bc",
      "incomplete_value": true,
      "site": "00ae93bc",
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
      "definition_site": "00ae92f4",
      "incomplete_value": true,
      "site": "00ae92f4",
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
      "00ae93b8",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae92fc",
      "PARAM",
      [
        "storage",
        "0029dcc7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae9310",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae93b8",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae93c4",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae93d8",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae92f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae92e0.md#insn-00ae92f4) · [`00ae9308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae92e0.md#insn-00ae9308) · [`00ae9310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae92e0.md#insn-00ae9310)
- 新版 `00ae93bc`（命令位置の公開資料なし） · `00ae93d0`（命令位置の公開資料なし）

~~~diff
- 00ae92f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae92f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae93bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae93bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae92f4 bytes 080100b5
+ 00ae93bc bytes 080100b5
- 00ae9308 ["INT_ADD", "register:40f0:8", ["const:ae9308:8", "const:4:8"]]
- 00ae9308 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae93d0 ["INT_ADD", "register:40f0:8", ["const:ae93d0:8", "const:4:8"]]
+ 00ae93d0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9308 bytes 22d30394
+ 00ae93d0 bytes 1cd30394
- 00ae9310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae9310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9310 bytes 60f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d2b704085bef03b82adb29a7629862"></a>

### [`00ae9330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9330.md) → [`00ae93f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae93f8.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00ae9480",
      "incomplete_value": true,
      "site": "00ae9480",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93b8",
      "incomplete_value": true,
      "site": "00ae93b8",
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
            "const:5f0:8"
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
      "definition_site": "00ae942c",
      "incomplete_value": true,
      "site": "00ae9438",
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
                "const:6a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9364",
      "incomplete_value": true,
      "site": "00ae9370",
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
                "const:5e8:8"
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
      "00ae940c",
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae942c",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9480",
      "WRITE",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae940c",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae942c",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9480",
      "WRITE",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9330.md#insn-00ae9370) · [`00ae93b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9330.md#insn-00ae93b8) · [`00ae9344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9330.md#insn-00ae9344)
- 新版 `00ae9438`（命令位置の公開資料なし） · `00ae9480`（命令位置の公開資料なし） · `00ae940c`（命令位置の公開資料なし）

~~~diff
- 00ae9370 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9370 ["INT_ADD", "register:40f0:8", ["const:ae9370:8", "const:4:8"]]
- 00ae9370 ["CALLIND", null, ["register:0:8"]]
+ 00ae9438 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae9438 ["INT_ADD", "register:40f0:8", ["const:ae9438:8", "const:4:8"]]
+ 00ae9438 ["CALLIND", null, ["register:0:8"]]
- 00ae9370 bytes 00013fd6
+ 00ae9438 bytes 00013fd6
- 00ae93b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae93b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae93b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae9480 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae9480 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6b0:8"]]
+ 00ae9480 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae93b8 bytes a0c21739
+ 00ae9480 bytes a0c21a39
- 00ae9344 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae9344 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae9344 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae940c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6b0:8"]]
+ 00ae940c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae940c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae9344 bytes a8c25739
+ 00ae940c bytes a8c25a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-939a275aa8a2eaef2e7e22662f9c5534"></a>

### [`00ae93cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae93cc.md) → [`00ae9494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9494.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9408"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae94d0"
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
      "00ae94a8",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae94b4",
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9408",
      "WRITE",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae94a8",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae94b4",
      "READ",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae94d0",
      "WRITE",
      [
        "storage",
        "010a06b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae93cc.md#insn-00ae9408) · [`00ae9454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae93cc.md#insn-00ae9454) · [`00ae9458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae93cc.md#insn-00ae9458)

~~~diff
- 00ae9408 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9408 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9408 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae9408 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9408 bytes bfc21739
- 00ae9454 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9454 ["INT_ADD", "register:40f0:8", ["const:ae9454:8", "const:4:8"]]
- 00ae9454 ["CALLIND", null, ["register:0:8"]]
- 00ae9454 bytes 00013fd6
- 00ae9458 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae9458 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae9458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae9458 bytes 9ff602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e13e04e0c0e0bce10407c12f08a21f8"></a>

### [`00ae946c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae946c.md) → [`00ae9534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9534.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae9574",
      "incomplete_value": true,
      "site": "00ae9574",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae94ac",
      "incomplete_value": true,
      "site": "00ae94ac",
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
            "const:5e8:8"
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
      "definition_site": "00ae9550",
      "incomplete_value": true,
      "site": "00ae9550",
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
      "definition_site": "00ae9488",
      "incomplete_value": true,
      "site": "00ae9488",
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
      "definition_site": "00ae9558",
      "incomplete_value": false,
      "site": "00ae956c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:d54:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9490",
      "incomplete_value": false,
      "site": "00ae94a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:cc7:8"
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
      "00ae9548",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9558",
      "PARAM",
      [
        "storage",
        "0029dcc7",
        null,
        "string"
      ]
    ],
    [
      "00ae9574",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9548",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9558",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ],
    [
      "00ae9574",
      "WRITE",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae94a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae946c.md#insn-00ae94a4) · [`00ae94ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae946c.md#insn-00ae94ac) · [`00ae9480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae946c.md#insn-00ae9480)
- 新版 `00ae956c`（命令位置の公開資料なし） · `00ae9574`（命令位置の公開資料なし） · `00ae9548`（命令位置の公開資料なし）

~~~diff
- 00ae94a4 ["INT_ADD", "register:40f0:8", ["const:ae94a4:8", "const:4:8"]]
- 00ae94a4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae956c ["INT_ADD", "register:40f0:8", ["const:ae956c:8", "const:4:8"]]
+ 00ae956c ["CALL", null, ["callee:00bde040:8"]]
- 00ae94a4 bytes bbd20394
+ 00ae956c bytes b5d20394
- 00ae94ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae94ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9574 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
+ 00ae9574 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae94ac bytes 80f602f9
+ 00ae9574 bytes 805603f9
- 00ae9480 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae9480 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9548 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
+ 00ae9548 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9480 bytes 81f642f9
+ 00ae9548 bytes 815643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b16967192e625344643bfe29d5899405"></a>

### [`00ae94dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae94dc.md) → [`00ae95a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95a4.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde5c0.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde670.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00ae95c0",
      "incomplete_value": false,
      "site": "00ae95c4",
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
      "definition_site": "00ae94f8",
      "incomplete_value": false,
      "site": "00ae94fc",
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
      "definition_site": "00ae95d0",
      "incomplete_value": true,
      "site": "00ae95dc",
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
      "definition_site": "00ae9508",
      "incomplete_value": true,
      "site": "00ae9514",
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
      "00ae95c0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae95d0",
      "DATA",
      [
        "storage",
        "010a05f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae95c0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae95d0",
      "DATA",
      [
        "storage",
        "010a06b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae94fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae94dc.md#insn-00ae94fc) · [`00ae94f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae94dc.md#insn-00ae94f8) · [`00ae9504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae94dc.md#insn-00ae9504)
- 新版 `00ae95c4`（命令位置の公開資料なし） · `00ae95c0`（命令位置の公開資料なし） · `00ae95cc`（命令位置の公開資料なし）

~~~diff
- 00ae94fc ["INT_ADD", "register:40f0:8", ["const:ae94fc:8", "const:4:8"]]
- 00ae94fc ["CALL", null, ["callee:00bde130:8"]]
+ 00ae95c4 ["INT_ADD", "register:40f0:8", ["const:ae95c4:8", "const:4:8"]]
+ 00ae95c4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae94fc bytes e1d20394
+ 00ae95c4 bytes dbd20394
- 00ae94f8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae94f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae94f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae94f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae95c0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae95c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae95c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae95c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae94f8 bytes 001c1591
+ 00ae95c0 bytes 00501791
- 00ae9504 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00ae9504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae95cc ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00ae95cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae95cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae95cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9504 bytes 08e11791
+ 00ae95cc bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-587e76857fffdb7d9b9b0e4b7827f043"></a>

### [`00ae9518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9518.md) → [`00ae95e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae95e0.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae9558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9620"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9534"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae952c",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9534",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9624"
      ]
    ],
    [
      "unmatched:00ae953c",
      "PARAM",
      [
        "storage",
        "0029dcc7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae95f4",
      "READ",
      [
        "storage",
        "010a06a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae95fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9624"
      ]
    ],
    [
      "00ae9604",
      "PARAM",
      [
        "storage",
        "0029dd54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9518.md#insn-00ae9534) · [`00ae9550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9518.md#insn-00ae9550) · [`00ae9558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9518.md#insn-00ae9558)
- 新版 `00ae9618`（命令位置の公開資料なし）

~~~diff
- 00ae9534 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9534 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9534 bytes 410100b5
- 00ae9550 ["INT_ADD", "register:40f0:8", ["const:ae9550:8", "const:4:8"]]
- 00ae9550 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9618 ["INT_ADD", "register:40f0:8", ["const:ae9618:8", "const:4:8"]]
+ 00ae9618 ["CALL", null, ["callee:00bde040:8"]]
- 00ae9550 bytes 90d20394
+ 00ae9618 bytes 8ad20394
- 00ae9558 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae9558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9558 bytes 80f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8660440fddd6bdcf0ee76a1c82d621f0"></a>

### [`00ae9588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9588.md) → [`00ae9650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9650.md) _ZN8firebase4util7context10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae966c",
      "incomplete_value": false,
      "site": "00ae9670",
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
      "definition_site": "00ae95a4",
      "incomplete_value": false,
      "site": "00ae95a8",
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
      "definition_site": "00ae967c",
      "incomplete_value": true,
      "site": "00ae9688",
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
      "definition_site": "00ae95b4",
      "incomplete_value": true,
      "site": "00ae95c0",
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
      "00ae966c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae967c",
      "DATA",
      [
        "storage",
        "010a0610",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae966c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae967c",
      "DATA",
      [
        "storage",
        "010a06d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae95a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9588.md#insn-00ae95a8) · [`00ae95a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9588.md#insn-00ae95a4) · [`00ae95b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9588.md#insn-00ae95b0)
- 新版 `00ae9670`（命令位置の公開資料なし） · `00ae966c`（命令位置の公開資料なし） · `00ae9678`（命令位置の公開資料なし）

~~~diff
- 00ae95a8 ["INT_ADD", "register:40f0:8", ["const:ae95a8:8", "const:4:8"]]
- 00ae95a8 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae9670 ["INT_ADD", "register:40f0:8", ["const:ae9670:8", "const:4:8"]]
+ 00ae9670 ["CALL", null, ["callee:00bde130:8"]]
- 00ae95a8 bytes b6d20394
+ 00ae9670 bytes b0d20394
- 00ae95a4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae95a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae95a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae95a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae966c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae966c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae966c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae966c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae95a4 bytes 00c81791
+ 00ae966c bytes 00fc1991
- 00ae95b0 ["COPY", "tmp:0:8", ["const:610:8"]]
- 00ae95b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae95b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae95b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9678 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00ae9678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae95b0 bytes 08411891
+ 00ae9678 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7987c5dd0a3f8553622fc556c946a785"></a>

### [`00ae95c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae95c4.md) → [`00ae968c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae968c.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae95f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae96b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae96a0",
      "incomplete_value": true,
      "site": "00ae96a0",
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
      "definition_site": "00ae95d8",
      "incomplete_value": true,
      "site": "00ae95d8",
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
      "00ae969c",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae96a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae95f4"
      ]
    ],
    [
      "unmatched:00ae95e4",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae969c",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae96a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae96bc"
      ]
    ],
    [
      "00ae96ac",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae95d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae95c4.md#insn-00ae95d8) · [`00ae95e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae95c4.md#insn-00ae95e8) · [`00ae95f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae95c4.md#insn-00ae95f0)
- 新版 `00ae96a0`（命令位置の公開資料なし）

~~~diff
- 00ae95d8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae95d8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae96a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae96a0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae95d8 bytes e80000b5
+ 00ae96a0 bytes e80000b5
- 00ae95e8 ["INT_ADD", "register:40f0:8", ["const:ae95e8:8", "const:4:8"]]
- 00ae95e8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae95e8 bytes 6ad20394
- 00ae95f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:618:8"]]
- 00ae95f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae95f0 bytes 600e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-399516c443012ed6df9b17f678273dcc"></a>

### [`00ae9644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9644.md) → [`00ae970c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae970c.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae973c",
      "incomplete_value": true,
      "site": "00ae973c",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9674",
      "incomplete_value": true,
      "site": "00ae9674",
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
            "const:618:8"
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
      "definition_site": "00ae9720",
      "incomplete_value": true,
      "site": "00ae9720",
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
      "definition_site": "00ae9658",
      "incomplete_value": true,
      "site": "00ae9658",
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
      "definition_site": "00ae972c",
      "incomplete_value": false,
      "site": "00ae9734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9664",
      "incomplete_value": false,
      "site": "00ae966c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
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
      "00ae971c",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae972c",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae973c",
      "WRITE",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae971c",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae972c",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae973c",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae966c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9644.md#insn-00ae966c) · [`00ae9674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9644.md#insn-00ae9674) · [`00ae9654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9644.md#insn-00ae9654)
- 新版 `00ae9734`（命令位置の公開資料なし） · `00ae973c`（命令位置の公開資料なし） · `00ae971c`（命令位置の公開資料なし）

~~~diff
- 00ae966c ["INT_ADD", "register:40f0:8", ["const:ae966c:8", "const:4:8"]]
- 00ae966c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9734 ["INT_ADD", "register:40f0:8", ["const:ae9734:8", "const:4:8"]]
+ 00ae9734 ["CALL", null, ["callee:00bde040:8"]]
- 00ae966c bytes 49d20394
+ 00ae9734 bytes 43d20394
- 00ae9674 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:618:8"]]
- 00ae9674 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae973c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 00ae973c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9674 bytes 600e03f9
+ 00ae973c bytes 606e03f9
- 00ae9654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:618:8"]]
- 00ae9654 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae971c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 00ae971c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9654 bytes 680e43f9
+ 00ae971c bytes 686e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac71656652d705eb05b9b5e2f83c45cc"></a>

### [`00ae9688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9688.md) → [`00ae9750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9750.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00ae9780",
      "incomplete_value": true,
      "site": "00ae9780",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96b8",
      "incomplete_value": true,
      "site": "00ae96b8",
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
            "const:618:8"
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
      "definition_site": "00ae9764",
      "incomplete_value": true,
      "site": "00ae9764",
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
      "definition_site": "00ae969c",
      "incomplete_value": true,
      "site": "00ae969c",
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
      "definition_site": "00ae976c",
      "incomplete_value": false,
      "site": "00ae9778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96a4",
      "incomplete_value": false,
      "site": "00ae96b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1bb:8"
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
      "00ae9760",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae976c",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00ae9780",
      "WRITE",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae9760",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae976c",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ],
    [
      "00ae9780",
      "WRITE",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae96b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9688.md#insn-00ae96b0) · [`00ae96b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9688.md#insn-00ae96b8) · [`00ae9698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9688.md#insn-00ae9698)
- 新版 `00ae9778`（命令位置の公開資料なし） · `00ae9780`（命令位置の公開資料なし） · `00ae9760`（命令位置の公開資料なし）

~~~diff
- 00ae96b0 ["INT_ADD", "register:40f0:8", ["const:ae96b0:8", "const:4:8"]]
- 00ae96b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9778 ["INT_ADD", "register:40f0:8", ["const:ae9778:8", "const:4:8"]]
+ 00ae9778 ["CALL", null, ["callee:00bde040:8"]]
- 00ae96b0 bytes 38d20394
+ 00ae9778 bytes 32d20394
- 00ae96b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:618:8"]]
- 00ae96b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae9780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 00ae9780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae96b8 bytes 600e03f9
+ 00ae9780 bytes 606e03f9
- 00ae9698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:618:8"]]
- 00ae9698 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae9760 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
+ 00ae9760 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae9698 bytes 680e43f9
+ 00ae9760 bytes 686e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-593c656a6e515c188b6510f9b57ba416"></a>

### [`00ae96d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae96d8.md) → [`00ae97a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae97a0.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00ae9828",
      "incomplete_value": true,
      "site": "00ae9828",
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
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9760",
      "incomplete_value": true,
      "site": "00ae9760",
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
            "const:620:8"
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
      "definition_site": "00ae97d4",
      "incomplete_value": true,
      "site": "00ae97e0",
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
                "const:6d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae970c",
      "incomplete_value": true,
      "site": "00ae9718",
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
                "const:618:8"
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
      "00ae97b4",
      "READ",
      [
        "storage",
        "010a0620",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae97d4",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9828",
      "WRITE",
      [
        "storage",
        "010a0620",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae97b4",
      "READ",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae97d4",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9828",
      "WRITE",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae96d8.md#insn-00ae9718) · [`00ae9760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae96d8.md#insn-00ae9760) · [`00ae96ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae96d8.md#insn-00ae96ec)
- 新版 `00ae97e0`（命令位置の公開資料なし） · `00ae9828`（命令位置の公開資料なし） · `00ae97b4`（命令位置の公開資料なし）

~~~diff
- 00ae9718 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9718 ["INT_ADD", "register:40f0:8", ["const:ae9718:8", "const:4:8"]]
- 00ae9718 ["CALLIND", null, ["register:0:8"]]
+ 00ae97e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae97e0 ["INT_ADD", "register:40f0:8", ["const:ae97e0:8", "const:4:8"]]
+ 00ae97e0 ["CALLIND", null, ["register:0:8"]]
- 00ae9718 bytes 00013fd6
+ 00ae97e0 bytes 00013fd6
- 00ae9760 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9760 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:620:8"]]
- 00ae9760 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae9828 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae9828 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e0:8"]]
+ 00ae9828 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9760 bytes a0821839
+ 00ae9828 bytes a0821b39
- 00ae96ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:620:8"]]
- 00ae96ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae96ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae97b4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6e0:8"]]
+ 00ae97b4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae97b4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae96ec bytes a8825839
+ 00ae97b4 bytes a8825b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546de8fc644a9cfb7c4c347a86ef8f0e"></a>

### [`00ae9774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9774.md) → [`00ae983c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae983c.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.50% / 新版 67.50%

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
      "site": "00ae97b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae9878"
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
      "00ae9850",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae9804"
      ]
    ],
    [
      "unmatched:00ae9794",
      "READ",
      [
        "storage",
        "010a0620",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae9850",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae9854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae98cc"
      ]
    ],
    [
      "00ae985c",
      "READ",
      [
        "storage",
        "010a06e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae978c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9774.md#insn-00ae978c) · [`00ae97b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9774.md#insn-00ae97b0) · [`00ae97d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9774.md#insn-00ae97d8)
- 新版 `00ae9854`（命令位置の公開資料なし）

~~~diff
- 00ae978c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae978c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae9854 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae9854 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae978c bytes c10300b4
+ 00ae9854 bytes c10300b4
- 00ae97b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae97b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae97b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:620:8"]]
- 00ae97b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae97b0 bytes bf821839
- 00ae97d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae97d8 ["INT_ADD", "register:40f0:8", ["const:ae97d8:8", "const:4:8"]]
- 00ae97d8 ["CALLIND", null, ["register:0:8"]]
- 00ae97d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b60655acf671fd3cfc9c980961129ac"></a>

### [`00ae9814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9814.md) → [`00ae98dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae98dc.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00ae9854"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae991c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9830"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9828",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9920"
      ]
    ],
    [
      "unmatched:00ae9838",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae98f0",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae98f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae9920"
      ]
    ],
    [
      "00ae9900",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9814.md#insn-00ae9830) · [`00ae984c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9814.md#insn-00ae984c) · [`00ae9854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9814.md#insn-00ae9854)
- 新版 `00ae9914`（命令位置の公開資料なし）

~~~diff
- 00ae9830 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9830 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9830 bytes 410100b5
- 00ae984c ["INT_ADD", "register:40f0:8", ["const:ae984c:8", "const:4:8"]]
- 00ae984c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae9914 ["INT_ADD", "register:40f0:8", ["const:ae9914:8", "const:4:8"]]
+ 00ae9914 ["CALL", null, ["callee:00bde040:8"]]
- 00ae984c bytes d1d10394
+ 00ae9914 bytes cbd10394
- 00ae9854 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:618:8"]]
- 00ae9854 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9854 bytes 800e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3b7f231cdd0584862d49c71e8093c0b"></a>

### [`00ae9884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9884.md) → [`00ae994c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae994c.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae9968",
      "incomplete_value": false,
      "site": "00ae996c",
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
      "definition_site": "00ae98a0",
      "incomplete_value": false,
      "site": "00ae98a4",
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
      "definition_site": "00ae9978",
      "incomplete_value": true,
      "site": "00ae9984",
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
      "definition_site": "00ae98b0",
      "incomplete_value": true,
      "site": "00ae98bc",
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
      "00ae9968",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae9978",
      "DATA",
      [
        "storage",
        "010a0628",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae9968",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae9978",
      "DATA",
      [
        "storage",
        "010a06e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae98a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9884.md#insn-00ae98a4) · [`00ae98a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9884.md#insn-00ae98a0) · [`00ae98ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9884.md#insn-00ae98ac)
- 新版 `00ae996c`（命令位置の公開資料なし） · `00ae9968`（命令位置の公開資料なし） · `00ae9974`（命令位置の公開資料なし）

~~~diff
- 00ae98a4 ["INT_ADD", "register:40f0:8", ["const:ae98a4:8", "const:4:8"]]
- 00ae98a4 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae996c ["INT_ADD", "register:40f0:8", ["const:ae996c:8", "const:4:8"]]
+ 00ae996c ["CALL", null, ["callee:00bde130:8"]]
- 00ae98a4 bytes f7d10394
+ 00ae996c bytes f1d10394
- 00ae98a0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae98a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae98a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae98a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9968 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae9968 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9968 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9968 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae98a0 bytes 001c1591
+ 00ae9968 bytes 00501791
- 00ae98ac ["COPY", "tmp:0:8", ["const:628:8"]]
- 00ae98ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae98ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae98ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9974 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00ae9974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae98ac bytes 08a11891
+ 00ae9974 bytes 08a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80c4208e83769eea33cd577d26074ea0"></a>

### [`00ae98c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae98c0.md) → [`00ae9988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9988.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae9900"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae99c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae98dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae98d4",
      "READ",
      [
        "storage",
        "010a0618",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae98dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae99cc"
      ]
    ],
    [
      "unmatched:00ae98e4",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae999c",
      "READ",
      [
        "storage",
        "010a06d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae99a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae99cc"
      ]
    ],
    [
      "00ae99ac",
      "PARAM",
      [
        "storage",
        "00294248",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae98dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae98c0.md#insn-00ae98dc) · [`00ae98f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae98c0.md#insn-00ae98f8) · [`00ae9900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae98c0.md#insn-00ae9900)
- 新版 `00ae99c0`（命令位置の公開資料なし）

~~~diff
- 00ae98dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae98dc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae98dc bytes 410100b5
- 00ae98f8 ["INT_ADD", "register:40f0:8", ["const:ae98f8:8", "const:4:8"]]
- 00ae98f8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae99c0 ["INT_ADD", "register:40f0:8", ["const:ae99c0:8", "const:4:8"]]
+ 00ae99c0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae98f8 bytes a6d10394
+ 00ae99c0 bytes a0d10394
- 00ae9900 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:618:8"]]
- 00ae9900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9900 bytes 800e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-628c53137980955dd3be649164dd6c4c"></a>

### [`00ae9930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9930.md) → [`00ae99f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae99f8.md) _ZN8firebase4util6cursor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae9a14",
      "incomplete_value": false,
      "site": "00ae9a18",
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
      "definition_site": "00ae994c",
      "incomplete_value": false,
      "site": "00ae9950",
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
      "definition_site": "00ae9a24",
      "incomplete_value": true,
      "site": "00ae9a30",
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
      "definition_site": "00ae995c",
      "incomplete_value": true,
      "site": "00ae9968",
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
      "00ae9a14",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae9a24",
      "DATA",
      [
        "storage",
        "010a0648",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae9a14",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae9a24",
      "DATA",
      [
        "storage",
        "010a0708",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9930.md#insn-00ae9950) · [`00ae994c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9930.md#insn-00ae994c) · [`00ae9958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae9/00ae9930.md#insn-00ae9958)
- 新版 `00ae9a18`（命令位置の公開資料なし） · `00ae9a14`（命令位置の公開資料なし） · `00ae9a20`（命令位置の公開資料なし）

~~~diff
- 00ae9950 ["INT_ADD", "register:40f0:8", ["const:ae9950:8", "const:4:8"]]
- 00ae9950 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae9a18 ["INT_ADD", "register:40f0:8", ["const:ae9a18:8", "const:4:8"]]
+ 00ae9a18 ["CALL", null, ["callee:00bde130:8"]]
- 00ae9950 bytes ccd10394
+ 00ae9a18 bytes c6d10394
- 00ae994c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae994c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae994c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae994c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae9a14 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae9a14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9a14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae9a14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae994c bytes 00c81791
+ 00ae9a14 bytes 00fc1991
- 00ae9958 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00ae9958 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9958 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae9958 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae9a20 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 00ae9a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae9a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae9958 bytes 08211991
+ 00ae9a20 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

