# v15.7.2 → v15.7.3 · 最優先の変更候補 (58)

[一覧の目次](README.md)

<a id="compare-4d083a3d69770d3c3906600702a7c5b9"></a>

### [`00ae124c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae124c.md) → [`00ae1314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1314.md) _ZN8firebase9analytics9TerminateEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd9f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9f0.md) · 呼出先 7件 [`00bddd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd70.md) [`00bddda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddda0.md) [`00bdde60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde60.md) [`00bddf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf80.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00bddaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaa0.md) · 呼出先 7件 [`00bdde20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde20.md) [`00bdde50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde50.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 20.21% / 新版 20.21%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 10件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae124c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae124c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1250",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae1254",
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
      "00ae1314",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae1318",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae131c",
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

- 旧版 [`00ae124c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae124c.md#insn-00ae124c) · [`00ae1250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae124c.md#insn-00ae1250) · [`00ae1254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae124c.md#insn-00ae1254)

~~~diff
- 00ae124c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae124c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae124c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae124c bytes f50f1df8
- 00ae1250 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae1250 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae1250 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae1250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1250 bytes f44f01a9
- 00ae1254 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae1254 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae1254 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae1254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1254 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-166b4093250673ee75e88ba50d70ec69"></a>

### [`00ae13c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae13c4.md) → [`00ae148c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md) _ZN8firebase9analytics29SetAnalyticsCollectionEnabledEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae14a0",
      "incomplete_value": true,
      "site": "00ae14a0",
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
      "definition_site": "00ae13d8",
      "incomplete_value": true,
      "site": "00ae13d8",
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
      "definition_site": "00ae14b8",
      "incomplete_value": true,
      "site": "00ae14c8",
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
                "const:108:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae13f0",
      "incomplete_value": true,
      "site": "00ae1400",
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
                "const:48:8"
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
      "definition_site": "00ae14bc",
      "incomplete_value": true,
      "site": "00ae14c8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae13f4",
      "incomplete_value": true,
      "site": "00ae1400",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:f80:8"
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
      "00ae149c",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae14b8",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae14bc",
      "READ",
      [
        "storage",
        "0109ff80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae149c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae14b8",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae14bc",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae13c4.md#insn-00ae1400) · [`00ae13d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae13c4.md#insn-00ae13d4) · [`00ae13e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae13c4.md#insn-00ae13e4)
- 新版 [`00ae14c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md#insn-00ae14c8) · [`00ae149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md#insn-00ae149c) · [`00ae14ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md#insn-00ae14ac)

~~~diff
- 00ae1400 ["INT_ADD", "register:40f0:8", ["const:ae1400:8", "const:4:8"]]
- 00ae1400 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae14c8 ["INT_ADD", "register:40f0:8", ["const:ae14c8:8", "const:4:8"]]
+ 00ae14c8 ["CALL", null, ["callee:00551e14:8"]]
- 00ae1400 bytes 85c2e997
+ 00ae14c8 bytes 53c2e997
- 00ae13d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
- 00ae13d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae149c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 00ae149c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae13d4 bytes 082140f9
+ 00ae149c bytes 088140f9
- 00ae13e4 ["INT_ADD", "register:40f0:8", ["const:ae13e4:8", "const:4:8"]]
- 00ae13e4 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00ae14ac ["INT_ADD", "register:40f0:8", ["const:ae14ac:8", "const:4:8"]]
+ 00ae14ac ["CALL", null, ["callee:00bde1b0:8"]]
- 00ae13e4 bytes 47f30394
+ 00ae14ac bytes 41f30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac7c1e6a96925274f7a91756d421dcd6"></a>

### [`00ae1428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1428.md) → [`00ae14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md) _ZN8firebase9analytics10SetConsentERKNSt6__ndk13mapINS0_11ConsentTypeENS0_13ConsentStatusENS1_4lessIS3_EENS1_9allocatorINS1_4pairIKS3_S4_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf60.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde010.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 67.67% / 新版 67.67%

CFGの説明率　旧版 44.64% / 新版 43.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 8件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae1514",
      "incomplete_value": true,
      "site": "00ae1514",
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
      "definition_site": "00ae144c",
      "incomplete_value": true,
      "site": "00ae144c",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1534"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae1510",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae1594",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00ae15bc",
      "DATA",
      [
        "storage",
        "002f59e9",
        "switchD_00ae14fc::switchdataD_002f59e9",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00ae1510",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae1594",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00ae15bc",
      "DATA",
      [
        "storage",
        "002f59e9",
        "switchD_00ae15c4::switchdataD_002f59e9",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae146c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1428.md#insn-00ae146c) · [`00ae14e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1428.md#insn-00ae14e0) · [`00ae1514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1428.md#insn-00ae1514)
- 新版 [`00ae1534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md#insn-00ae1534) · [`00ae15a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md#insn-00ae15a8)

~~~diff
- 00ae146c ["INT_ADD", "register:40f0:8", ["const:ae146c:8", "const:4:8"]]
- 00ae146c ["CALL", null, ["callee:00bde0e0:8"]]
+ 00ae1534 ["INT_ADD", "register:40f0:8", ["const:ae1534:8", "const:4:8"]]
+ 00ae1534 ["CALL", null, ["callee:00bde0e0:8"]]
- 00ae146c bytes f1f20394
+ 00ae1534 bytes ebf20394
- 00ae14e0 ["CBRANCH", null, ["local:b29:8", "register:101:1"]]
+ 00ae15a8 ["CBRANCH", null, ["local:b33:8", "register:101:1"]]
- 00ae14e0 bytes c0120054
+ 00ae15a8 bytes c0120054
- 00ae1514 ["COPY", "register:4000:8", ["register:4098:8"]]
- 00ae1514 bytes e00313aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-127fe54459ba72d25c9c81493f9dab09"></a>

### [`00ae19dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae19dc.md) → [`00ae1aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1aa4.md) _ZN8firebase9analytics17AddBundleToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae19dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae19dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae19e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae19dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae19e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae19e4",
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
      "00ae1aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae1aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae1aac",
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

- 旧版 [`00ae19dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae19dc.md#insn-00ae19dc) · [`00ae19e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae19dc.md#insn-00ae19e0) · [`00ae19e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae19dc.md#insn-00ae19e4)

~~~diff
- 00ae19dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae19dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae19dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae19dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae19dc bytes f657bda9
- 00ae19e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae19e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae19e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae19e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae19e0 bytes f44f01a9
- 00ae19e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae19e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae19e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae19e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae19e4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-568eec2bc7f0b5575bce81ce4582aa78"></a>

### [`00ae1a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1a54.md) → [`00ae1b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1b1c.md) _ZN8firebase9analytics23VectorOfMapsToArrayListEP7_JNIEnvRKNSt6__ndk16vectorINS_7VariantENS3_9allocatorIS5_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde0b0.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbb0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf30.md)
- 新版 呼出元 1件 [`00bde160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde160.md) · 呼出先 9件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bddc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bddfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae1b2c"
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
      "unmatched:00ae1a64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae1b8c",
      "PARAM",
      [
        "storage",
        "00295297",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae1ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1c04"
      ]
    ]
  ],
  "added": [
    [
      "00ae1b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae1b8c",
      "PARAM",
      [
        "storage",
        "00295324",
        null,
        "string"
      ]
    ],
    [
      "00ae1b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae1c04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1a54.md#insn-00ae1a64) · [`00ae1ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1a54.md#insn-00ae1ad4) · [`00ae1af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1a54.md#insn-00ae1af8)
- 新版 [`00ae1bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1b1c.md#insn-00ae1bc0)

~~~diff
- 00ae1a64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae1a64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae1a64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ae1a64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae1a64 bytes fd7b04a9
- 00ae1ad4 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00ae1ad4 bytes 40030054
- 00ae1af8 ["INT_ADD", "register:40f0:8", ["const:ae1af8:8", "const:4:8"]]
- 00ae1af8 ["CALL", null, ["callee:00bde140:8"]]
+ 00ae1bc0 ["INT_ADD", "register:40f0:8", ["const:ae1bc0:8", "const:4:8"]]
+ 00ae1bc0 ["CALL", null, ["callee:00bde140:8"]]
- 00ae1af8 bytes 66f10394
+ 00ae1bc0 bytes 60f10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40cd7eb1c3d9f6a10ef5e9b0dc49605c"></a>

### [`00ae1d14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1d14.md) → [`00ae1ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1ddc.md) _ZN8firebase9analytics18AddVariantToBundleEP7_JNIEnvP8_jobjectPKcRKNS_7VariantE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde0a0.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbb0.md) [`00bddbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbd0.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 1件 [`00bde150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde150.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bddc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) [`00bddc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 53.66% / 新版 62.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1d38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae1e00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae1db0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae1d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae20f0"
      ]
    ],
    [
      "unmatched:00ae1d48",
      "DATA",
      [
        "storage",
        "002f59ed",
        "switchD_00ae1d60::switchdataD_002f59ed",
        "byte"
      ]
    ],
    [
      "unmatched:00ae1dbc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde0c0"
      ]
    ]
  ],
  "added": [
    [
      "00ae1e00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae20f0"
      ]
    ],
    [
      "00ae1e10",
      "DATA",
      [
        "storage",
        "002f59ed",
        "switchD_00ae1e28::switchdataD_002f59ed",
        "byte"
      ]
    ],
    [
      "00ae1e84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde0c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1d14.md#insn-00ae1d38) · [`00ae1db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1d14.md#insn-00ae1db0) · [`00ae1dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae1/00ae1d14.md#insn-00ae1dbc)

~~~diff
- 00ae1d38 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ae1d38 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00ae1d38 ["CBRANCH", null, ["local:b30:8", "tmp:1:1"]]
- 00ae1d38 bytes 88170054
- 00ae1db0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1db0 ["INT_ADD", "register:40f0:8", ["const:ae1db0:8", "const:4:8"]]
- 00ae1db0 ["CALLIND", null, ["register:0:8"]]
- 00ae1db0 bytes 00013fd6
- 00ae1dbc ["INT_ADD", "register:40f0:8", ["const:ae1dbc:8", "const:4:8"]]
- 00ae1dbc ["CALL", null, ["callee:00bde0c0:8"]]
- 00ae1dbc bytes 95f00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-928fcf22a46f7c4bd819679aad308e85"></a>

### [`00ae2044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2044.md) → [`00ae210c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md) _ZN8firebase9analytics8LogEventEPKcS2_S2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.54% / 新版 84.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2128",
      "incomplete_value": true,
      "site": "00ae2128",
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
      "definition_site": "00ae2060",
      "incomplete_value": true,
      "site": "00ae2060",
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
    "new": null,
    "old": {
      "definition_site": "00ae2084",
      "incomplete_value": false,
      "site": "00ae2088",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae211c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae2124",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae213c",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2140",
      "READ",
      [
        "storage",
        "0109ff90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2124",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2204",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2208",
      "READ",
      [
        "storage",
        "010a0050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2044.md#insn-00ae2060) · [`00ae2088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2044.md#insn-00ae2088) · [`00ae211c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2044.md#insn-00ae211c)
- 新版 [`00ae2128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md#insn-00ae2128) · [`00ae2150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md#insn-00ae2150)

~~~diff
- 00ae2060 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae2060 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae2128 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae2128 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00ae2060 bytes 680a00b4
+ 00ae2128 bytes 680a00b4
- 00ae2088 ["INT_ADD", "register:40f0:8", ["const:ae2088:8", "const:4:8"]]
- 00ae2088 ["CALL", null, ["callee:00bde0c0:8"]]
+ 00ae2150 ["INT_ADD", "register:40f0:8", ["const:ae2150:8", "const:4:8"]]
+ 00ae2150 ["CALL", null, ["callee:00bde0c0:8"]]
- 00ae2088 bytes e2ef0394
+ 00ae2150 bytes dcef0394
- 00ae211c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae211c ["INT_ADD", "register:40f0:8", ["const:ae211c:8", "const:4:8"]]
- 00ae211c ["CALLIND", null, ["register:0:8"]]
- 00ae211c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1b57c68264044ebffebd1c4f463ea7"></a>

### [`00ae21c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae21c8.md) → [`00ae2290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md) _ZN8firebase9analytics8LogEventEPKcS2_d

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 82.56% / 新版 82.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae22ac",
      "incomplete_value": true,
      "site": "00ae22ac",
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
      "definition_site": "00ae21e4",
      "incomplete_value": true,
      "site": "00ae21e4",
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
      "definition_site": "00ae22d8",
      "incomplete_value": true,
      "site": "00ae22e4",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ae2244",
      "incomplete_value": true,
      "site": "00ae2258",
      "value": [
        "live",
        "register:4000:8"
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
      "00ae22a8",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2294",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2298",
      "READ",
      [
        "storage",
        "0109ff90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae22a8",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae235c",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2360",
      "READ",
      [
        "storage",
        "010a0050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae21e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae21c8.md#insn-00ae21e4) · [`00ae2200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae21c8.md#insn-00ae2200) · [`00ae221c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae21c8.md#insn-00ae221c)
- 新版 [`00ae22ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md#insn-00ae22ac) · [`00ae22c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md#insn-00ae22c8) · [`00ae22e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md#insn-00ae22e4)

~~~diff
- 00ae21e4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae21e4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00ae22ac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae22ac ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae21e4 bytes 080900b4
+ 00ae22ac bytes 080900b4
- 00ae2200 ["INT_ADD", "register:40f0:8", ["const:ae2200:8", "const:4:8"]]
- 00ae2200 ["CALL", null, ["callee:00bde0d0:8"]]
+ 00ae22c8 ["INT_ADD", "register:40f0:8", ["const:ae22c8:8", "const:4:8"]]
+ 00ae22c8 ["CALL", null, ["callee:00bde0d0:8"]]
- 00ae2200 bytes 88ef0394
+ 00ae22c8 bytes 82ef0394
- 00ae221c ["INT_ADD", "register:40f0:8", ["const:ae221c:8", "const:4:8"]]
- 00ae221c ["CALL", null, ["callee:0056681c:8"]]
+ 00ae22e4 ["INT_ADD", "register:40f0:8", ["const:ae22e4:8", "const:4:8"]]
+ 00ae22e4 ["CALL", null, ["callee:0056681c:8"]]
- 00ae221c bytes 8011ea97
+ 00ae22e4 bytes 4e11ea97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc91bd9a637c4af26cfea5f587a2496"></a>

### [`00ae2320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2320.md) → [`00ae23e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md) _ZN8firebase9analytics8LogEventEPKcS2_l

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde0e0.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 1件 [`00bde190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde190.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2404",
      "incomplete_value": true,
      "site": "00ae2404",
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
      "definition_site": "00ae233c",
      "incomplete_value": true,
      "site": "00ae233c",
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
    "new": null,
    "old": {
      "definition_site": "00ae2344",
      "incomplete_value": true,
      "site": "00ae2350",
      "value": [
        "live",
        "register:4040:8"
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
      "definition_site": "00ae2360",
      "incomplete_value": false,
      "site": "00ae2364",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
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
      "00ae2400",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae23ec",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae23f0",
      "READ",
      [
        "storage",
        "0109ff90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2400",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae24b4",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae24b8",
      "READ",
      [
        "storage",
        "010a0050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae233c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2320.md#insn-00ae233c) · [`00ae2350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2320.md#insn-00ae2350) · [`00ae2358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2320.md#insn-00ae2358)
- 新版 [`00ae2404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md#insn-00ae2404) · [`00ae2418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md#insn-00ae2418) · [`00ae2420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md#insn-00ae2420)

~~~diff
- 00ae233c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae233c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00ae2404 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae2404 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae233c bytes 080900b4
+ 00ae2404 bytes 080900b4
- 00ae2350 ["INT_ADD", "register:40f0:8", ["const:ae2350:8", "const:4:8"]]
- 00ae2350 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00ae2418 ["INT_ADD", "register:40f0:8", ["const:ae2418:8", "const:4:8"]]
+ 00ae2418 ["CALL", null, ["callee:00bde1b0:8"]]
- 00ae2350 bytes 6cef0394
+ 00ae2418 bytes 66ef0394
- 00ae2358 ["INT_ADD", "register:40f0:8", ["const:ae2358:8", "const:4:8"]]
- 00ae2358 ["CALL", null, ["callee:00bde0d0:8"]]
+ 00ae2420 ["INT_ADD", "register:40f0:8", ["const:ae2420:8", "const:4:8"]]
+ 00ae2420 ["CALL", null, ["callee:00bde0d0:8"]]
- 00ae2358 bytes 32ef0394
+ 00ae2420 bytes 2cef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4786ebd2ba5c2f774e172de420bb359"></a>

### [`00ae248c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae248c.md) → [`00ae2554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2554.md) _ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda40.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 1件 [`00bddaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaf0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2574",
      "incomplete_value": true,
      "site": "00ae2574",
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
      "definition_site": "00ae24ac",
      "incomplete_value": true,
      "site": "00ae24ac",
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
      "definition_site": "00ae2608",
      "incomplete_value": true,
      "site": "00ae2610",
      "value": [
        "live",
        "register:40c0:8"
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae260c",
      "incomplete_value": true,
      "site": "00ae2610",
      "value": [
        "live",
        "register:40c8:8"
      ]
    },
    "old": null,
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
      "00ae2570",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2608",
      "PARAM",
      [
        "storage",
        "002ad2b1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae256c",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2570",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2608",
      "PARAM",
      [
        "storage",
        "002ad2a8",
        null,
        "string"
      ]
    ],
    [
      "00ae2634",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae248c.md#insn-00ae2548) · [`00ae2584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae248c.md#insn-00ae2584) · [`00ae25a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae248c.md#insn-00ae25a0)
- 新版 [`00ae2610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2554.md#insn-00ae2610) · [`00ae264c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2554.md#insn-00ae264c) · [`00ae2668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2554.md#insn-00ae2668)

~~~diff
- 00ae2548 ["INT_ADD", "register:40f0:8", ["const:ae2548:8", "const:4:8"]]
- 00ae2548 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00ae2610 ["INT_ADD", "register:40f0:8", ["const:ae2610:8", "const:4:8"]]
+ 00ae2610 ["CALL", null, ["callee:00bdddf0:8"]]
- 00ae2548 bytes feed0394
+ 00ae2610 bytes f8ed0394
- 00ae2584 ["INT_ADD", "register:40f0:8", ["const:ae2584:8", "const:4:8"]]
- 00ae2584 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae264c ["INT_ADD", "register:40f0:8", ["const:ae264c:8", "const:4:8"]]
+ 00ae264c ["CALL", null, ["callee:00551e14:8"]]
- 00ae2584 bytes 24bee997
+ 00ae264c bytes f2bde997
- 00ae25a0 ["INT_ADD", "register:40f0:8", ["const:ae25a0:8", "const:4:8"]]
- 00ae25a0 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00ae2668 ["INT_ADD", "register:40f0:8", ["const:ae2668:8", "const:4:8"]]
+ 00ae2668 ["CALL", null, ["callee:00bdddf0:8"]]
- 00ae25a0 bytes e8ed0394
+ 00ae2668 bytes e2ed0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba7d0398bfa3beddc7713c8b2b4d0d68"></a>

### [`00ae2614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2614.md) → [`00ae26dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md) _ZN8firebase9analytics25SetDefaultEventParametersEPKNS0_9ParameterEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde0c0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde010.md)
- 新版 呼出元 1件 [`00bde170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde170.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 77.68% / 新版 77.68%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae26fc",
      "incomplete_value": true,
      "site": "00ae26fc",
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
      "definition_site": "00ae2634",
      "incomplete_value": true,
      "site": "00ae2634",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae26a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae276c"
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
      "00ae26f8",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae2750"
      ]
    ],
    [
      "00ae274c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae2750"
      ]
    ]
  ],
  "added": [
    [
      "00ae26f8",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2748",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae2818"
      ]
    ],
    [
      "00ae274c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae2818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae26a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2614.md#insn-00ae26a4) · [`00ae26b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2614.md#insn-00ae26b8) · [`00ae26e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2614.md#insn-00ae26e0)
- 新版 [`00ae2780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md#insn-00ae2780) · [`00ae27a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md#insn-00ae27a8)

~~~diff
- 00ae26a4 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00ae26a4 bytes a0060054
- 00ae26b8 ["INT_ADD", "register:40f0:8", ["const:ae26b8:8", "const:4:8"]]
- 00ae26b8 ["CALL", null, ["callee:00bde150:8"]]
+ 00ae2780 ["INT_ADD", "register:40f0:8", ["const:ae2780:8", "const:4:8"]]
+ 00ae2780 ["CALL", null, ["callee:00bde150:8"]]
- 00ae26b8 bytes 7aee0394
+ 00ae2780 bytes 74ee0394
- 00ae26e0 ["INT_ADD", "register:40f0:8", ["const:ae26e0:8", "const:4:8"]]
- 00ae26e0 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00ae27a8 ["INT_ADD", "register:40f0:8", ["const:ae27a8:8", "const:4:8"]]
+ 00ae27a8 ["CALL", null, ["callee:00bdddf0:8"]]
- 00ae26e0 bytes 98ed0394
+ 00ae27a8 bytes 92ed0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79851b60b6d07ed69ac8c6de16f46b6a"></a>

### [`00ae27e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae27e8.md) → [`00ae28b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae28b0.md) _ZN8firebase9analytics53InitiateOnDeviceConversionMeasurementWithEmailAddressEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda50.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb00.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae28b8",
      "incomplete_value": true,
      "site": "00ae28b8",
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
      "definition_site": "00ae27f0",
      "incomplete_value": true,
      "site": "00ae27f0",
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
      "00ae28b4",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae27fc",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae2800",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ],
  "added": [
    [
      "00ae28b4",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae28c4",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00ae28c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde130"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae27ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae27e8.md#insn-00ae27ec) · [`00ae27fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae27e8.md#insn-00ae27fc) · [`00ae2800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae27e8.md#insn-00ae2800)
- 新版 [`00ae28b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae28b0.md#insn-00ae28b4)

~~~diff
- 00ae27ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
- 00ae27ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae28b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 00ae28b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae27ec bytes 082140f9
+ 00ae28b4 bytes 088140f9
- 00ae27fc ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00ae27fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae27fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae27fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae27fc bytes 00800391
- 00ae2800 ["BRANCH", null, ["callee:00bde130:8"]]
- 00ae2800 bytes 20ee0314
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3fecfbed8fa4438e80cffa9d7350f8"></a>

### [`00ae2858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2858.md) → [`00ae2920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md) _ZN8firebase9analytics15SetUserPropertyEPKcS2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 69.23% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae293c",
      "incomplete_value": true,
      "site": "00ae293c",
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
      "definition_site": "00ae2874",
      "incomplete_value": true,
      "site": "00ae2874",
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
      "definition_site": "00ae29b0",
      "incomplete_value": true,
      "site": "00ae29c4",
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
                "const:108:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae28e8",
      "incomplete_value": true,
      "site": "00ae28fc",
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
                "const:48:8"
              ]
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
      "definition_site": "00ae29b4",
      "incomplete_value": true,
      "site": "00ae29c4",
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
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae28ec",
      "incomplete_value": true,
      "site": "00ae28fc",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:f98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae2938",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae28d0",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00ae29b0",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2938",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2998",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00ae29b0",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae28fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2858.md#insn-00ae28fc) · [`00ae291c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2858.md#insn-00ae291c) · [`00ae2870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2858.md#insn-00ae2870)
- 新版 [`00ae29c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md#insn-00ae29c4) · [`00ae29e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md#insn-00ae29e4) · [`00ae2938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md#insn-00ae2938)

~~~diff
- 00ae28fc ["INT_ADD", "register:40f0:8", ["const:ae28fc:8", "const:4:8"]]
- 00ae28fc ["CALL", null, ["callee:00551e14:8"]]
+ 00ae29c4 ["INT_ADD", "register:40f0:8", ["const:ae29c4:8", "const:4:8"]]
+ 00ae29c4 ["CALL", null, ["callee:00551e14:8"]]
- 00ae28fc bytes 46bde997
+ 00ae29c4 bytes 14bde997
- 00ae291c ["INT_ADD", "register:40f0:8", ["const:ae291c:8", "const:4:8"]]
- 00ae291c ["CALL", null, ["callee:00bdddf0:8"]]
+ 00ae29e4 ["INT_ADD", "register:40f0:8", ["const:ae29e4:8", "const:4:8"]]
+ 00ae29e4 ["CALL", null, ["callee:00bdddf0:8"]]
- 00ae291c bytes 09ed0394
+ 00ae29e4 bytes 03ed0394
- 00ae2870 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
- 00ae2870 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2938 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 00ae2938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2870 bytes 082140f9
+ 00ae2938 bytes 088140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da85274dcea029fe3d06f5a6adaf80b7"></a>

### [`00ae295c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae295c.md) → [`00ae2a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2a24.md) _ZN8firebase9analytics9SetUserIdEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda30.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00bddae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddae0.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.81% / 新版 69.81%

CFGの説明率　旧版 53.85% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae295c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2960"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae295c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2960",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2964",
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
      "00ae2a24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae2a28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae2a2c",
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

- 旧版 [`00ae295c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae295c.md#insn-00ae295c) · [`00ae2960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae295c.md#insn-00ae2960) · [`00ae2964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae295c.md#insn-00ae2964)

~~~diff
- 00ae295c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae295c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae295c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae295c bytes f50f1df8
- 00ae2960 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae2960 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae2960 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae2960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2960 bytes f44f01a9
- 00ae2964 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae2964 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae2964 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae2964 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2964 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa26061c6b80fc21f85131d30c10135"></a>

### [`00ae2a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a30.md) → [`00ae2af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md) _ZN8firebase9analytics25SetSessionTimeoutDurationEl

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdda20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda20.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00bddad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddad0.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2b0c",
      "incomplete_value": true,
      "site": "00ae2b0c",
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
      "definition_site": "00ae2a44",
      "incomplete_value": true,
      "site": "00ae2a44",
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
      "definition_site": "00ae2b24",
      "incomplete_value": true,
      "site": "00ae2b34",
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
                "const:108:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2a5c",
      "incomplete_value": true,
      "site": "00ae2a6c",
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
                "const:48:8"
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
      "definition_site": "00ae2b28",
      "incomplete_value": true,
      "site": "00ae2b34",
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2a60",
      "incomplete_value": true,
      "site": "00ae2a6c",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:fa8:8"
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
      "00ae2b08",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2a5c",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2a60",
      "READ",
      [
        "storage",
        "0109ffa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2b08",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b24",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b28",
      "READ",
      [
        "storage",
        "010a0068",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a30.md#insn-00ae2a44) · [`00ae2a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a30.md#insn-00ae2a6c) · [`00ae2a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a30.md#insn-00ae2a40)
- 新版 [`00ae2b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md#insn-00ae2b0c) · [`00ae2b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md#insn-00ae2b34) · [`00ae2b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md#insn-00ae2b08)

~~~diff
- 00ae2a44 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae2a44 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae2b0c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae2b0c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae2a44 bytes e80100b4
+ 00ae2b0c bytes e80100b4
- 00ae2a6c ["INT_ADD", "register:40f0:8", ["const:ae2a6c:8", "const:4:8"]]
- 00ae2a6c ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2b34 ["INT_ADD", "register:40f0:8", ["const:ae2b34:8", "const:4:8"]]
+ 00ae2b34 ["CALL", null, ["callee:00551e14:8"]]
- 00ae2a6c bytes eabce997
+ 00ae2b34 bytes b8bce997
- 00ae2a40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
- 00ae2a40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2b08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 00ae2b08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2a40 bytes 082140f9
+ 00ae2b08 bytes 088140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d82795090034149a25a1408780a5cd1"></a>

### [`00ae2a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a94.md) → [`00ae2b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md) _ZN8firebase9analytics18ResetAnalyticsDataEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2b70",
      "incomplete_value": true,
      "site": "00ae2b70",
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
      "definition_site": "00ae2aa8",
      "incomplete_value": true,
      "site": "00ae2aa8",
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
      "definition_site": "00ae2b80",
      "incomplete_value": true,
      "site": "00ae2b8c",
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
                "const:108:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2ab8",
      "incomplete_value": true,
      "site": "00ae2ac4",
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
                "const:48:8"
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
      "definition_site": "00ae2b84",
      "incomplete_value": true,
      "site": "00ae2b8c",
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
                "const:70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2abc",
      "incomplete_value": true,
      "site": "00ae2ac4",
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
                "const:109f000:8"
              ],
              [
                "leaf",
                "const:fb0:8"
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
      "00ae2b6c",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b80",
      "READ",
      [
        "storage",
        "010a0048",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b84",
      "READ",
      [
        "storage",
        "0109ffb0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2b6c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b80",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b84",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a94.md#insn-00ae2ac4) · [`00ae2aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a94.md#insn-00ae2aa4) · [`00ae2aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2a94.md#insn-00ae2aac)
- 新版 [`00ae2b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md#insn-00ae2b8c) · [`00ae2b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md#insn-00ae2b6c) · [`00ae2b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md#insn-00ae2b74)

~~~diff
- 00ae2ac4 ["INT_ADD", "register:40f0:8", ["const:ae2ac4:8", "const:4:8"]]
- 00ae2ac4 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2b8c ["INT_ADD", "register:40f0:8", ["const:ae2b8c:8", "const:4:8"]]
+ 00ae2b8c ["CALL", null, ["callee:00551e14:8"]]
- 00ae2ac4 bytes d4bce997
+ 00ae2b8c bytes a2bce997
- 00ae2aa4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:40:8"]]
- 00ae2aa4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2b6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
+ 00ae2b6c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2aa4 bytes 002140f9
+ 00ae2b6c bytes 008140f9
- 00ae2aac ["INT_ADD", "register:40f0:8", ["const:ae2aac:8", "const:4:8"]]
- 00ae2aac ["CALL", null, ["callee:00bde1b0:8"]]
+ 00ae2b74 ["INT_ADD", "register:40f0:8", ["const:ae2b74:8", "const:4:8"]]
+ 00ae2b74 ["CALL", null, ["callee:00bde1b0:8"]]
- 00ae2aac bytes 95ed0394
+ 00ae2b74 bytes 8fed0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df80ec2aebdfc2d3bdb0c70e18029e12"></a>

### [`00ae2b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2b00.md) → [`00ae2bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md) _ZN8firebase9analytics22GetAnalyticsInstanceIdEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 17件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00ae3268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3268.md) [`00ae3d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d00.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3330.md) [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 23.81% / 新版 22.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae2bec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2bf8",
      "incomplete_value": true,
      "site": "00ae2bf8",
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
      "definition_site": "00ae2b30",
      "incomplete_value": true,
      "site": "00ae2b30",
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
      "unmatched:00ae2b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00ae2bf4",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2c20",
      "READ",
      [
        "storage",
        "00c1b7b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae2bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00ae2bf4",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2c20",
      "READ",
      [
        "storage",
        "00c1b868",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2b00.md#insn-00ae2b24) · [`00ae2b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2b00.md#insn-00ae2b30) · [`00ae2b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2b00.md#insn-00ae2b6c)
- 新版 [`00ae2bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md#insn-00ae2bf8) · [`00ae2c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md#insn-00ae2c34)

~~~diff
- 00ae2b24 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ae2b24 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae2b24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae2b24 bytes a9831cf8
- 00ae2b30 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ae2b30 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00ae2bf8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00ae2bf8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae2b30 bytes e00700b4
+ 00ae2bf8 bytes e00700b4
- 00ae2b6c ["INT_ADD", "register:40f0:8", ["const:ae2b6c:8", "const:4:8"]]
- 00ae2b6c ["CALL", null, ["callee:00bddf70:8"]]
+ 00ae2c34 ["INT_ADD", "register:40f0:8", ["const:ae2c34:8", "const:4:8"]]
+ 00ae2c34 ["CALL", null, ["callee:00bddf70:8"]]
- 00ae2b6c bytes d5ec0394
+ 00ae2c34 bytes cfec0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ef37f693e69c79677f45992fbe10eb3"></a>

### [`00ae2d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2d54.md) → [`00ae2e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2e1c.md) _ZN8firebase9analytics32GetAnalyticsInstanceIdLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde0d0.md) · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bddd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd50.md)
- 新版 呼出元 1件 [`00bde180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde180.md) · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdde00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2d54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2d58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae2d54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2d58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2d5c",
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
      "00ae2e1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae2e20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae2e24",
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

- 旧版 [`00ae2d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2d54.md#insn-00ae2d54) · [`00ae2d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2d54.md#insn-00ae2d58) · [`00ae2d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2d54.md#insn-00ae2d5c)

~~~diff
- 00ae2d54 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae2d54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae2d54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae2d54 bytes f50f1df8
- 00ae2d58 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae2d58 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae2d58 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae2d58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2d58 bytes f44f01a9
- 00ae2d5c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae2d5c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae2d5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae2d5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2d5c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98694b96e2b13f3c50e8e761458b181f"></a>

### [`00ae2e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2e28.md) → [`00ae2ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2ef0.md) _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHand

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde40.md) · 呼出先 3件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bdde70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde70.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 1件 [`00bddef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddef0.md) · 呼出先 3件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf20.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2e28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2e2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2e2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae2e28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2e2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae2e30",
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
      "00ae2ef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae2ef4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae2ef8",
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

- 旧版 [`00ae2e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2e28.md#insn-00ae2e28) · [`00ae2e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2e28.md#insn-00ae2e2c) · [`00ae2e30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2e28.md#insn-00ae2e30)

~~~diff
- 00ae2e28 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae2e28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae2e28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae2e28 bytes f50f1df8
- 00ae2e2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae2e2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae2e2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae2e2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2e2c bytes f44f01a9
- 00ae2e30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae2e30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae2e30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae2e30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae2e30 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-469cde372e62ab5672953f6ee65437db"></a>

### [`00ae2ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2ec8.md) → [`00ae2f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md) _ZN8firebase9analytics12GetSessionIdEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00ae3940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3940.md) [`00ae3d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d38.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md) [`00ae3e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e00.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.84% / 新版 85.84%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 13件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2fc0",
      "incomplete_value": true,
      "site": "00ae2fc0",
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
      "definition_site": "00ae2ef8",
      "incomplete_value": true,
      "site": "00ae2ef8",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae2f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae305c"
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
      "00ae2fbc",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae2f10",
      "READ",
      [
        "storage",
        "00c1b7c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae2f10",
      "PARAM",
      [
        "storage",
        "00ae3d38",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIlEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae2fbc",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2fd8",
      "READ",
      [
        "storage",
        "00c1b870",
        null,
        "pointer"
      ]
    ],
    [
      "00ae2fd8",
      "PARAM",
      [
        "storage",
        "00ae3e00",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIlEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2ec8.md#insn-00ae2ef8) · [`00ae2f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2ec8.md#insn-00ae2f24) · [`00ae2f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2ec8.md#insn-00ae2f40)
- 新版 [`00ae2fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md#insn-00ae2fc0) · [`00ae2fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md#insn-00ae2fec)

~~~diff
- 00ae2ef8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00ae2ef8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00ae2fc0 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00ae2fc0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae2ef8 bytes c90600b4
+ 00ae2fc0 bytes c90600b4
- 00ae2f24 ["INT_ADD", "register:40f0:8", ["const:ae2f24:8", "const:4:8"]]
- 00ae2f24 ["CALL", null, ["callee:00bddf70:8"]]
+ 00ae2fec ["INT_ADD", "register:40f0:8", ["const:ae2fec:8", "const:4:8"]]
+ 00ae2fec ["CALL", null, ["callee:00bddf70:8"]]
- 00ae2f24 bytes e7eb0394
+ 00ae2fec bytes e1eb0394
- 00ae2f40 ["INT_ADD", "register:40f0:8", ["const:ae2f40:8", "const:4:8"]]
- 00ae2f40 ["CALL", null, ["callee:00bde1b0:8"]]
- 00ae2f40 bytes 70ec0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e6d427749f6dba87014c07db95da48"></a>

### [`00ae3190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3190.md) → [`00ae3258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md) _ZN8firebase9analytics22GetSessionIdLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bddd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdde00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde00.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae3274",
      "incomplete_value": true,
      "site": "00ae3274",
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
      "definition_site": "00ae31ac",
      "incomplete_value": true,
      "site": "00ae31ac",
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
    "new": null,
    "old": {
      "definition_site": "00ae31bc",
      "incomplete_value": true,
      "site": "00ae31c0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae32c8",
      "incomplete_value": false,
      "site": "00ae32cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:16d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae3200",
      "incomplete_value": false,
      "site": "00ae3204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:e0:8"
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
      "00ae326c",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae3200",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae326c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae32c8",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae31ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3190.md#insn-00ae31ac) · [`00ae31c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3190.md#insn-00ae31c0) · [`00ae3204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3190.md#insn-00ae3204)
- 新版 [`00ae3274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md#insn-00ae3274) · [`00ae3288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md#insn-00ae3288) · [`00ae32cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md#insn-00ae32cc)

~~~diff
- 00ae31ac ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00ae31ac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae3274 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00ae3274 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae31ac bytes 890200b4
+ 00ae3274 bytes 890200b4
- 00ae31c0 ["INT_ADD", "register:40f0:8", ["const:ae31c0:8", "const:4:8"]]
- 00ae31c0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00ae3288 ["INT_ADD", "register:40f0:8", ["const:ae3288:8", "const:4:8"]]
+ 00ae3288 ["CALL", null, ["callee:00bddbd0:8"]]
- 00ae31c0 bytes 58ea0394
+ 00ae3288 bytes 52ea0394
- 00ae3204 ["INT_ADD", "register:40f0:8", ["const:ae3204:8", "const:4:8"]]
- 00ae3204 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae32cc ["INT_ADD", "register:40f0:8", ["const:ae32cc:8", "const:4:8"]]
+ 00ae32cc ["CALL", null, ["callee:00bde130:8"]]
- 00ae3204 bytes 9feb0394
+ 00ae32cc bytes 99eb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-801250abaa7f8d58626ed62997d974c7"></a>

### [`00ae3268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3268.md) → [`00ae3330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3330.md) FUN_00ae3330

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ae2b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2b00.md) · 呼出先 12件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00ae2bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md) · 呼出先 12件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 45.24% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae32a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae336c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae32ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae32a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae32a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdde00"
      ]
    ],
    [
      "unmatched:00ae32ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae34b4"
      ]
    ]
  ],
  "added": [
    [
      "00ae336c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00ae3370",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdde00"
      ]
    ],
    [
      "00ae3374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae34b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae32a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3268.md#insn-00ae32a4) · [`00ae32a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3268.md#insn-00ae32a8) · [`00ae32ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3268.md#insn-00ae32ac)

~~~diff
- 00ae32a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00ae32a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ae32a4 bytes e82700f9
- 00ae32a8 ["INT_ADD", "register:40f0:8", ["const:ae32a8:8", "const:4:8"]]
- 00ae32a8 ["CALL", null, ["callee:00bdde00:8"]]
- 00ae32a8 bytes aaea0394
- 00ae32ac ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ae32ac ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00ae32ac bytes 000a00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad732275868a3006fc9efd964d876027"></a>

### [`00ae348c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae348c.md) → [`00ae3554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26Complet

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde00.md) · 呼出先 11件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00bddeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddeb0.md) · 呼出先 11件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae35c0",
      "incomplete_value": false,
      "site": "00ae35c4",
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
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae34f8",
      "incomplete_value": false,
      "site": "00ae34fc",
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
            "const:467:8"
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
      "00ae35c0",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae35c0",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae34fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae348c.md#insn-00ae34fc) · [`00ae34c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae348c.md#insn-00ae34c0) · [`00ae34cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae348c.md#insn-00ae34cc)
- 新版 [`00ae35c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md#insn-00ae35c4) · [`00ae3588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md#insn-00ae3588) · [`00ae3594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md#insn-00ae3594)

~~~diff
- 00ae34fc ["INT_ADD", "register:40f0:8", ["const:ae34fc:8", "const:4:8"]]
- 00ae34fc ["CALL", null, ["callee:00bde130:8"]]
+ 00ae35c4 ["INT_ADD", "register:40f0:8", ["const:ae35c4:8", "const:4:8"]]
+ 00ae35c4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae34fc bytes e1ea0394
+ 00ae35c4 bytes dbea0394
- 00ae34c0 ["INT_ADD", "register:40f0:8", ["const:ae34c0:8", "const:4:8"]]
- 00ae34c0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00ae3588 ["INT_ADD", "register:40f0:8", ["const:ae3588:8", "const:4:8"]]
+ 00ae3588 ["CALL", null, ["callee:00bddbd0:8"]]
- 00ae34c0 bytes 98e90394
+ 00ae3588 bytes 92e90394
- 00ae34cc ["INT_ADD", "register:40f0:8", ["const:ae34cc:8", "const:4:8"]]
- 00ae34cc ["CALL", null, ["callee:00bddfb0:8"]]
+ 00ae3594 ["INT_ADD", "register:40f0:8", ["const:ae3594:8", "const:4:8"]]
+ 00ae3594 ["CALL", null, ["callee:00bddfb0:8"]]
- 00ae34cc bytes 8dea0394
+ 00ae3594 bytes 87ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac5c19d1cb038d2a4df7431ed5c5ed1"></a>

### [`00ae3694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3694.md) → [`00ae375c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae375c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde120.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bde110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde110.md)
- 新版 呼出元 1件 [`00bde1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1d0.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 46.15% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae37a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae37a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae3868"
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
      "unmatched:00ae3714",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae37f0"
      ]
    ],
    [
      "00ae3834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae3784"
      ]
    ],
    [
      "unmatched:00ae3780",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdb160"
      ]
    ]
  ],
  "added": [
    [
      "00ae37dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae37f0"
      ]
    ],
    [
      "00ae3834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae384c"
      ]
    ],
    [
      "00ae3848",
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

- 旧版 [`00ae36c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3694.md#insn-00ae36c0) · [`00ae370c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3694.md#insn-00ae370c) · [`00ae3714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3694.md#insn-00ae3714)
- 新版 [`00ae3788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae375c.md#insn-00ae3788)

~~~diff
- 00ae36c0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ae36c0 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00ae3788 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00ae3788 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00ae36c0 bytes 23080054
+ 00ae3788 bytes 23080054
- 00ae370c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ae370c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ae370c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ae370c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00ae370c bytes 2831889a
- 00ae3714 ["CBRANCH", null, ["local:b8:8", "register:102:1"]]
- 00ae3714 bytes a2000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8541305f11c4953e3c337a2e23953b9"></a>

### [`00ae37cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae37cc.md) → [`00ae3894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3894.md) _ZN8firebase10FutureBaseaSERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdddf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddf0.md) · 呼出先 6件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde90.md)
- 新版 呼出元 1件 [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

CFGの説明率　旧版 7.14% / 新版 5.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae37fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3890"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae3940"
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
      "unmatched:00ae37fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae38f0"
      ]
    ],
    [
      "00ae38c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae396c"
      ]
    ],
    [
      "unmatched:00ae3890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae396c"
      ]
    ]
  ],
  "added": [
    [
      "00ae38c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae38f0"
      ]
    ],
    [
      "00ae3940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae396c"
      ]
    ],
    [
      "00ae3958",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae396c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae37fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae37cc.md#insn-00ae37fc) · [`00ae380c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae37cc.md#insn-00ae380c) · [`00ae384c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae37cc.md#insn-00ae384c)
- 新版 [`00ae3914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3894.md#insn-00ae3914)

~~~diff
- 00ae37fc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ae37fc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae37fc bytes 600100b4
- 00ae380c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae380c ["INT_ADD", "register:40f0:8", ["const:ae380c:8", "const:4:8"]]
- 00ae380c ["CALLIND", null, ["register:0:8"]]
- 00ae380c bytes 00013fd6
- 00ae384c ["INT_ADD", "register:40f0:8", ["const:ae384c:8", "const:4:8"]]
- 00ae384c ["CALL", null, ["callee:00bddf50:8"]]
+ 00ae3914 ["INT_ADD", "register:40f0:8", ["const:ae3914:8", "const:4:8"]]
+ 00ae3914 ["CALL", null, ["callee:00bddf50:8"]]
- 00ae384c bytes 95e90394
+ 00ae3914 bytes 8fe90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313bd18aced1a0d1cd987d22171d8eb2"></a>

### [`00ae3940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3940.md) → [`00ae3a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md) FUN_00ae3a08

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ae2ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae2/00ae2ec8.md) · 呼出先 9件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd50.md)
- 新版 呼出元 1件 [`00ae2f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bdde00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.40% / 新版 81.40%

CFGの説明率　旧版 36.67% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3948"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3944",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3948",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae394c",
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
      "00ae3a0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ae3a10",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ae3a14",
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

- 旧版 [`00ae3944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3940.md#insn-00ae3944) · [`00ae3948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3940.md#insn-00ae3948) · [`00ae394c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3940.md#insn-00ae394c)

~~~diff
- 00ae3944 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00ae3944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00ae3944 bytes f91300f9
- 00ae3948 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ae3948 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ae3948 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ae3948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3948 bytes f85f03a9
- 00ae394c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae394c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae394c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ae394c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae394c bytes f65704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fe89d237aea8dc40abac5e1263a2d44"></a>

### [`00ae3ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3ab8.md) → [`00ae3b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_i

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde30.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00bddee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddee0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.41% / 新版 90.41%

CFGの説明率　旧版 71.43% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae3bec",
      "incomplete_value": false,
      "site": "00ae3bf0",
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
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae3b24",
      "incomplete_value": false,
      "site": "00ae3b28",
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
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ae3ca0"
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
      "00ae3bec",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae3b98",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3b9c",
      "READ",
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
      "00ae3bec",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ],
    [
      "00ae3c60",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae3c64",
      "READ",
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

- 旧版 [`00ae3b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3ab8.md#insn-00ae3b28) · [`00ae3bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3ab8.md#insn-00ae3bd8)
- 新版 [`00ae3bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md#insn-00ae3bf0) · [`00ae3ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md#insn-00ae3ca0)

~~~diff
- 00ae3b28 ["INT_ADD", "register:40f0:8", ["const:ae3b28:8", "const:4:8"]]
- 00ae3b28 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae3bf0 ["INT_ADD", "register:40f0:8", ["const:ae3bf0:8", "const:4:8"]]
+ 00ae3bf0 ["CALL", null, ["callee:00bde130:8"]]
- 00ae3b28 bytes 56e90394
+ 00ae3bf0 bytes 50e90394
- 00ae3bd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae3bd8 ["RETURN", null, ["register:0:8"]]
- 00ae3bd8 bytes c0035fd6
+ 00ae3ca0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae3ca0 ["RETURN", null, ["register:0:8"]]
+ 00ae3ca0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45ef8a6252b468ed3efb720dad21f392"></a>

### [`00ae3bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3bdc.md) → [`00ae3ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3ca4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_i

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde10.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00bddec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddec0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.34% / 新版 75.34%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3bdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3be0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3be0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3bdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3be0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3be4",
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
      "00ae3ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ae3ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ae3cac",
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

- 旧版 [`00ae3bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3bdc.md#insn-00ae3bdc) · [`00ae3be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3bdc.md#insn-00ae3be0) · [`00ae3be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3bdc.md#insn-00ae3be4)

~~~diff
- 00ae3bdc ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00ae3bdc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00ae3bdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae3bdc bytes f90f1bf8
- 00ae3be0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ae3be0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ae3be0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae3be0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3be0 bytes f85f01a9
- 00ae3be4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae3be4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae3be4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae3be4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3be4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41108d2af48b1d0eca103f3b60fc9781"></a>

### [`00ae3d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d44.md) → [`00ae3e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e0c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIlZNS0_26CompleteWithResultInternalIlEEvRKNS_12FutureHandleEiPKcRKT_EUlPlE_EEvS5_i

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdde20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde20.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00bdded0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdded0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.56% / 新版 83.56%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3d48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3d48",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3d4c",
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
      "00ae3e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ae3e10",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ae3e14",
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

- 旧版 [`00ae3d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d44.md#insn-00ae3d44) · [`00ae3d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d44.md#insn-00ae3d48) · [`00ae3d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d44.md#insn-00ae3d4c)

~~~diff
- 00ae3d44 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00ae3d44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00ae3d44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae3d44 bytes f90f1bf8
- 00ae3d48 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ae3d48 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ae3d48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae3d48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3d48 bytes f85f01a9
- 00ae3d4c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae3d4c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae3d4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae3d4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae3d4c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef397eab4c939359db91887f6c7cdbd2"></a>

### [`00ae3e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md) → [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) FUN_00ae3f30

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00ae3e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e98.md) [`00ae4394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4394.md) [`00ae43c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae43c0.md) · 呼出先 2件 [`00ae4408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4408.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 3件 [`00ae3f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md) [`00ae445c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae445c.md) [`00ae4488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md) · 呼出先 2件 [`00ae44d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae3e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md#insn-00ae3e7c) · [`00ae3e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md#insn-00ae3e84) · [`00ae3e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md#insn-00ae3e94)
- 新版 [`00ae3f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md#insn-00ae3f44) · [`00ae3f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md#insn-00ae3f4c) · [`00ae3f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md#insn-00ae3f5c)

~~~diff
- 00ae3e7c ["INT_ADD", "register:40f0:8", ["const:ae3e7c:8", "const:4:8"]]
- 00ae3e7c ["CALL", null, ["callee:00ae44d0:8"]]
+ 00ae3f44 ["INT_ADD", "register:40f0:8", ["const:ae3f44:8", "const:4:8"]]
+ 00ae3f44 ["CALL", null, ["callee:00ae44d0:8"]]
- 00ae3e7c bytes 63010094
+ 00ae3f44 bytes 63010094
- 00ae3e84 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00ae3f4c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00ae3e84 bytes 80000054
+ 00ae3f4c bytes 80000054
- 00ae3e94 ["INT_ADD", "register:40f0:8", ["const:ae3e94:8", "const:4:8"]]
- 00ae3e94 ["CALL", null, ["callee:00bde270:8"]]
+ 00ae3f5c ["INT_ADD", "register:40f0:8", ["const:ae3f5c:8", "const:4:8"]]
+ 00ae3f5c ["CALL", null, ["callee:00bde270:8"]]
- 00ae3e94 bytes cbe80394
+ 00ae3f5c bytes c5e80394
~~~


<a id="compare-402715d834d94a6a839187365b8f803a"></a>

### [`00ae3e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e98.md) → [`00ae3f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md) _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md) · 呼出先 8件 [`00ae3e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md) · 呼出先 8件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.77% / 新版 73.77%

CFGの説明率　旧版 44.44% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3ec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae3f8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae3ed4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae3ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae3ec8",
      "READ",
      [
        "storage",
        "00c1b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ae3ed0",
      "READ",
      [
        "storage",
        "010a0058",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae3f8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00ae3f90",
      "READ",
      [
        "storage",
        "00c1b888",
        null,
        "pointer"
      ]
    ],
    [
      "00ae3f98",
      "READ",
      [
        "storage",
        "010a0118",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e98.md#insn-00ae3ec4) · [`00ae3ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e98.md#insn-00ae3ed4) · [`00ae3f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e98.md#insn-00ae3f30)
- 新版 [`00ae3ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md#insn-00ae3ff8)

~~~diff
- 00ae3ec4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00ae3ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ae3ec4 bytes e81700f9
- 00ae3ed4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00ae3ed4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae3ed4 bytes f30000b5
- 00ae3f30 ["INT_ADD", "register:40f0:8", ["const:ae3f30:8", "const:4:8"]]
- 00ae3f30 ["CALL", null, ["callee:00bde280:8"]]
+ 00ae3ff8 ["INT_ADD", "register:40f0:8", ["const:ae3ff8:8", "const:4:8"]]
+ 00ae3ff8 ["CALL", null, ["callee:00bde280:8"]]
- 00ae3f30 bytes a8e80394
+ 00ae3ff8 bytes a2e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7922b742b29ef703ddbb6998786fe36"></a>

### [`00ae41b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae41b8.md) → [`00ae4280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4280.md) _ZN8firebase8LogErrorEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 1件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.83% / 新版 26.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae41d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae41d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae41d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae41d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae41d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae41d8",
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
      "00ae4298",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00ae429c",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00ae42a0",
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

- 旧版 [`00ae41d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae41b8.md#insn-00ae41d0) · [`00ae41d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae41b8.md#insn-00ae41d4) · [`00ae41d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae41b8.md#insn-00ae41d8)

~~~diff
- 00ae41d0 ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00ae41d0 ["COPY", "tmp:1:8", ["register:4030:8"]]
- 00ae41d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a8:8"]]
- 00ae41d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae41d0 bytes e59b0aa9
- 00ae41d4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b8:8"]]
- 00ae41d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00ae41d4 bytes e75f00f9
- 00ae41d8 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00ae41d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ae41d8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ae41d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00ae41d8 bytes e00700ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8ce2c61ac6e125b1d445e8ae2ca1b71"></a>

### [`00ae425c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae425c.md) → [`00ae4324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4324.md) _ZN8firebase9LogAssertEPKcz

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1a0.md)
- 新版 呼出元 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.17% / 新版 73.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae42b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae42b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae42b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae42b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae42b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae42bc",
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
      "00ae437c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00ae4380",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00ae4384",
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

- 旧版 [`00ae42b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae425c.md#insn-00ae42b4) · [`00ae42b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae425c.md#insn-00ae42b8) · [`00ae42bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae425c.md#insn-00ae42bc)

~~~diff
- 00ae42b4 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00ae42b4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00ae42b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae42b4 bytes ad831ef8
- 00ae42b8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ae42b8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ae42b8 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae42b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae42b8 bytes abab3ca9
- 00ae42bc ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00ae42bc ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00ae42bc ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00ae42bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae42bc bytes aeb33da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8968a7ff3c7b26e9195cdb2ce908a808"></a>

### [`00ae43c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae43c0.md) → [`00ae4488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md) _ZN8firebase14LogGetCallbackEPPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ae3e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ae44b0",
      "incomplete_value": true,
      "site": "00ae44b4",
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
      "definition_site": "00ae43e8",
      "incomplete_value": true,
      "site": "00ae43ec",
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
      "definition_site": "00ae44a0",
      "incomplete_value": false,
      "site": "00ae44a4",
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
            "const:d5f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae43d8",
      "incomplete_value": false,
      "site": "00ae43dc",
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
            "const:cd2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae43d8",
      "PARAM",
      [
        "storage",
        "0029bcd2",
        null,
        "string"
      ]
    ],
    [
      "00ae44ac",
      "READ",
      [
        "storage",
        "00c1b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae44b0",
      "READ",
      [
        "storage",
        "010a0050",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae44a0",
      "PARAM",
      [
        "storage",
        "0029bd5f",
        null,
        "string"
      ]
    ],
    [
      "00ae44ac",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00ae44b0",
      "READ",
      [
        "storage",
        "010a0110",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae43dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae43c0.md#insn-00ae43dc) · [`00ae4404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae43c0.md#insn-00ae4404)
- 新版 [`00ae44a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md#insn-00ae44a4) · [`00ae44cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md#insn-00ae44cc)

~~~diff
- 00ae43dc ["INT_ADD", "register:40f0:8", ["const:ae43dc:8", "const:4:8"]]
- 00ae43dc ["CALL", null, ["callee:00bde130:8"]]
+ 00ae44a4 ["INT_ADD", "register:40f0:8", ["const:ae44a4:8", "const:4:8"]]
+ 00ae44a4 ["CALL", null, ["callee:00bde130:8"]]
- 00ae43dc bytes 29e70394
+ 00ae44a4 bytes 23e70394
- 00ae4404 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae4404 ["RETURN", null, ["register:0:8"]]
- 00ae4404 bytes c0035fd6
+ 00ae44cc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae44cc ["RETURN", null, ["register:0:8"]]
+ 00ae44cc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1d3dc7c03599586b8a7b1887dd74a24"></a>

### [`00ae4408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4408.md) → [`00ae44d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md) FUN_00ae44d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ae3e68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3e68.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde160.md)
- 新版 呼出元 1件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde210.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

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
      "site": "00ae4418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae445c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4418",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae445c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4460",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae44e0",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ],
    [
      "00ae4524",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00ae4528",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4408.md#insn-00ae4418) · [`00ae445c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4408.md#insn-00ae445c) · [`00ae4460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4408.md#insn-00ae4460)

~~~diff
- 00ae4418 ["COPY", "tmp:0:8", ["register:4010:8"]]
- 00ae4418 ["COPY", "tmp:1:8", ["register:4018:8"]]
- 00ae4418 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00ae4418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4418 bytes e20f08a9
- 00ae445c ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00ae445c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00ae445c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ae445c bytes ac831ef8
- 00ae4460 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00ae4460 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ae4460 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00ae4460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4460 bytes aaa73ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-814099b65a5e57e269caf9e7dcf05dd6"></a>

### [`00ae44a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44a4.md) → [`00ae456c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae456c.md) _INIT_270

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae4584",
      "incomplete_value": true,
      "site": "00ae4584",
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
              "LOAD"
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
      "definition_site": "00ae44bc",
      "incomplete_value": true,
      "site": "00ae44bc",
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
              "LOAD"
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
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae44e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ae45a8"
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
      "00ae457c",
      "READ",
      [
        "storage",
        "00c1b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae4580",
      "READ",
      [
        "storage",
        "010a0058",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00ae459c",
      "WRITE",
      [
        "storage",
        "010a0058",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae457c",
      "READ",
      [
        "storage",
        "00c1b888",
        null,
        "pointer"
      ]
    ],
    [
      "00ae4580",
      "READ",
      [
        "storage",
        "010a0118",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00ae459c",
      "WRITE",
      [
        "storage",
        "010a0118",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae44e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44a4.md#insn-00ae44e0) · [`00ae44b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae44a4.md#insn-00ae44b4)
- 新版 [`00ae45a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae456c.md#insn-00ae45a8) · [`00ae457c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae456c.md#insn-00ae457c)

~~~diff
- 00ae44e0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae44e0 ["RETURN", null, ["register:0:8"]]
- 00ae44e0 bytes c0035fd6
+ 00ae45a8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ae45a8 ["RETURN", null, ["register:0:8"]]
+ 00ae45a8 bytes c0035fd6
- 00ae44b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00ae44b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae457c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00ae457c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae44b4 bytes 94ee43f9
+ 00ae457c bytes 944644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9525ea7c2615edc80a99ab51165d13"></a>

### [`00ae4640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4640.md) → [`00ae4708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4708.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "site": "00ae466c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae4734"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae471c",
      "incomplete_value": true,
      "site": "00ae471c",
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
      "definition_site": "00ae4654",
      "incomplete_value": true,
      "site": "00ae4654",
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
      "00ae4718",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae4660",
      "PARAM",
      [
        "storage",
        "002a7d64",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae4664",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae4718",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4728",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae472c",
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

- 旧版 [`00ae4654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4640.md#insn-00ae4654) · [`00ae4664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4640.md#insn-00ae4664) · [`00ae466c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4640.md#insn-00ae466c)
- 新版 [`00ae471c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4708.md#insn-00ae471c)

~~~diff
- 00ae4654 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae4654 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae471c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae471c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae4654 bytes e80000b5
+ 00ae471c bytes e80000b5
- 00ae4664 ["INT_ADD", "register:40f0:8", ["const:ae4664:8", "const:4:8"]]
- 00ae4664 ["CALL", null, ["callee:00bde040:8"]]
- 00ae4664 bytes 4be60394
- 00ae466c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:268:8"]]
- 00ae466c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae466c bytes 603601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-731828e1332d90a4067c8d8811a5ae6d"></a>

### [`00ae4680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4680.md) → [`00ae4748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4748.md) _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassReq

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) · 呼出先 4件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md) [`00bde3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3b0.md) [`00bde5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde5f0.md)
- 新版 呼出元 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) · 呼出先 4件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) [`00bde460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde460.md) [`00bde6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.63% / 新版 77.63%

CFGの説明率　旧版 17.39% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4684"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4680",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4684",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4688",
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
      "00ae4748",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ae474c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae4750",
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

- 旧版 [`00ae4680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4680.md#insn-00ae4680) · [`00ae4684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4680.md#insn-00ae4684) · [`00ae4688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4680.md#insn-00ae4688)

~~~diff
- 00ae4680 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ae4680 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ae4680 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00ae4680 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae4680 bytes f85fbca9
- 00ae4684 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae4684 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae4684 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae4684 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4684 bytes f65701a9
- 00ae4688 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae4688 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae4688 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae4688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4688 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a452a8464ef5d051ba252b38d449c5d6"></a>

### [`00ae47b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47b0.md) → [`00ae4878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00ae48a4",
      "incomplete_value": true,
      "site": "00ae48a4",
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
      "definition_site": "00ae47dc",
      "incomplete_value": true,
      "site": "00ae47dc",
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
            "const:268:8"
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
      "definition_site": "00ae488c",
      "incomplete_value": true,
      "site": "00ae488c",
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
      "definition_site": "00ae47c4",
      "incomplete_value": true,
      "site": "00ae47c4",
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
      "definition_site": "00ae4894",
      "incomplete_value": false,
      "site": "00ae489c",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae47cc",
      "incomplete_value": false,
      "site": "00ae47d4",
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
            "const:d64:8"
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
      "00ae4888",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4894",
      "PARAM",
      [
        "storage",
        "002a7d64",
        null,
        "string"
      ]
    ],
    [
      "00ae48a4",
      "WRITE",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4888",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4894",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae48a4",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47b0.md#insn-00ae47d4) · [`00ae47dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47b0.md#insn-00ae47dc) · [`00ae47c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47b0.md#insn-00ae47c0)
- 新版 [`00ae489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md#insn-00ae489c) · [`00ae48a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md#insn-00ae48a4) · [`00ae4888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md#insn-00ae4888)

~~~diff
- 00ae47d4 ["INT_ADD", "register:40f0:8", ["const:ae47d4:8", "const:4:8"]]
- 00ae47d4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae489c ["INT_ADD", "register:40f0:8", ["const:ae489c:8", "const:4:8"]]
+ 00ae489c ["CALL", null, ["callee:00bde040:8"]]
- 00ae47d4 bytes efe50394
+ 00ae489c bytes e9e50394
- 00ae47dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:268:8"]]
- 00ae47dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae48a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00ae48a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae47dc bytes 603601f9
+ 00ae48a4 bytes 609601f9
- 00ae47c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:268:8"]]
- 00ae47c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae4888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
+ 00ae4888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae47c0 bytes 683641f9
+ 00ae4888 bytes 689641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f68df4ecc4715d30a31825fc51ef3bc"></a>

### [`00ae47f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47f0.md) → [`00ae48b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48b8.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "site": "00ae4820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae48e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae48cc",
      "incomplete_value": true,
      "site": "00ae48cc",
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
      "definition_site": "00ae4804",
      "incomplete_value": true,
      "site": "00ae4804",
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
      "00ae48c8",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae4810",
      "PARAM",
      [
        "storage",
        "002a7d64",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae4818",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae48c8",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae48d8",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae48e0",
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

- 旧版 [`00ae4804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47f0.md#insn-00ae4804) · [`00ae4818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47f0.md#insn-00ae4818) · [`00ae4820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae47f0.md#insn-00ae4820)
- 新版 [`00ae48cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48b8.md#insn-00ae48cc)

~~~diff
- 00ae4804 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae4804 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae48cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae48cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae4804 bytes 080100b5
+ 00ae48cc bytes 080100b5
- 00ae4818 ["INT_ADD", "register:40f0:8", ["const:ae4818:8", "const:4:8"]]
- 00ae4818 ["CALL", null, ["callee:00bde040:8"]]
- 00ae4818 bytes dee50394
- 00ae4820 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:268:8"]]
- 00ae4820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4820 bytes 603601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2fe4415169dd2694a62889ed204ba93"></a>

### [`00ae4834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4834.md) → [`00ae48fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48fc.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae4864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae492c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00ae4848",
      "incomplete_value": true,
      "site": "00ae4848",
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
      "00ae490c",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4910",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae4868"
      ]
    ],
    [
      "unmatched:00ae4850",
      "PARAM",
      [
        "storage",
        "002a7d64",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae490c",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4910",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae4930"
      ]
    ],
    [
      "00ae4918",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae485c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4834.md#insn-00ae485c) · [`00ae4864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4834.md#insn-00ae4864) · [`00ae4874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4834.md#insn-00ae4874)
- 新版 [`00ae4924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48fc.md#insn-00ae4924)

~~~diff
- 00ae485c ["INT_ADD", "register:40f0:8", ["const:ae485c:8", "const:4:8"]]
- 00ae485c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae4924 ["INT_ADD", "register:40f0:8", ["const:ae4924:8", "const:4:8"]]
+ 00ae4924 ["CALL", null, ["callee:00bde040:8"]]
- 00ae485c bytes cde50394
+ 00ae4924 bytes c7e50394
- 00ae4864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:268:8"]]
- 00ae4864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4864 bytes 603601f9
- 00ae4874 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae4874 ["RETURN", null, ["register:0:8"]]
- 00ae4874 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bac95f27e428bab935d509ff4a1b9cac"></a>

### [`00ae4884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4884.md) → [`00ae494c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae494c.md) _ZN8firebase4util12class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4888"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4884",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4888",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae488c",
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
      "00ae494c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae4950",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae4954",
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

- 旧版 [`00ae4884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4884.md#insn-00ae4884) · [`00ae4888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4884.md#insn-00ae4888) · [`00ae488c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4884.md#insn-00ae488c)

~~~diff
- 00ae4884 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae4884 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae4884 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae4884 bytes f50f1df8
- 00ae4888 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae4888 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae4888 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae4888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4888 bytes f44f01a9
- 00ae488c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae488c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae488c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae488c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae488c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-226f28678662f660054b869b9da227da"></a>

### [`00ae497c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae497c.md) → [`00ae4a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md) _ZN8firebase4util12class_loader12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00ae4a80",
      "incomplete_value": true,
      "site": "00ae4a80",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae49b8",
      "incomplete_value": true,
      "site": "00ae49b8",
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
            "const:270:8"
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
      "definition_site": "00ae4ad0",
      "incomplete_value": true,
      "site": "00ae4ad0",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4a08",
      "incomplete_value": true,
      "site": "00ae4a08",
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
            "const:268:8"
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
      "definition_site": "00ae4a5c",
      "incomplete_value": true,
      "site": "00ae4a5c",
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
      "definition_site": "00ae4994",
      "incomplete_value": true,
      "site": "00ae4994",
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
      "00ae4a58",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4a64",
      "READ",
      [
        "storage",
        "010a0270",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae4a80",
      "WRITE",
      [
        "storage",
        "010a0270",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae4a58",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4a64",
      "READ",
      [
        "storage",
        "010a0330",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae4a80",
      "WRITE",
      [
        "storage",
        "010a0330",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae49b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae497c.md#insn-00ae49b8) · [`00ae4a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae497c.md#insn-00ae4a04) · [`00ae4a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae497c.md#insn-00ae4a08)
- 新版 [`00ae4a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md#insn-00ae4a80) · [`00ae4acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md#insn-00ae4acc) · [`00ae4ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md#insn-00ae4ad0)

~~~diff
- 00ae49b8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae49b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae49b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:270:8"]]
- 00ae49b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae4a80 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae4a80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae4a80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:330:8"]]
+ 00ae4a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae49b8 bytes bfc20939
+ 00ae4a80 bytes bfc20c39
- 00ae4a04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4a04 ["INT_ADD", "register:40f0:8", ["const:ae4a04:8", "const:4:8"]]
- 00ae4a04 ["CALLIND", null, ["register:0:8"]]
+ 00ae4acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4acc ["INT_ADD", "register:40f0:8", ["const:ae4acc:8", "const:4:8"]]
+ 00ae4acc ["CALLIND", null, ["register:0:8"]]
- 00ae4a04 bytes 00013fd6
+ 00ae4acc bytes 00013fd6
- 00ae4a08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:268:8"]]
- 00ae4a08 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae4a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae4ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00ae4ad0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae4ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae4a08 bytes 9f3601f9
+ 00ae4ad0 bytes 9f9601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0741977f52770921666e80fec91e3466"></a>

### [`00ae4a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a1c.md) → [`00ae4ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4ae4.md) _ZN8firebase4util12class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae4a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4a20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae4a1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae4a30",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae4ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae4af8",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a1c.md#insn-00ae4a1c) · [`00ae4a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a1c.md#insn-00ae4a20) · [`00ae4a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a1c.md#insn-00ae4a38)

~~~diff
- 00ae4a1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae4a1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae4a1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae4a1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae4a1c bytes f44fbea9
- 00ae4a20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae4a20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae4a20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae4a20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae4a20 bytes fd7b01a9
- 00ae4a38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae4a38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae4a38 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c40f47720b5161b713429ee0245eb0f"></a>

### [`00ae4a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a8c.md) → [`00ae4b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md) _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md) · 呼出先 5件 [`00af14e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af14e8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) · 呼出先 5件 [`00af15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 76.77% / 新版 76.77%

CFGの説明率　旧版 35.59% / 新版 31.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4bd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae4c14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae4b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae4c5c"
      ]
    ],
    [
      "00ae4ba4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae4c7c"
      ]
    ],
    [
      "unmatched:00ae4bd8",
      "PARAM",
      [
        "storage",
        "002a0e42",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae4b9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae4d24"
      ]
    ],
    [
      "00ae4ba4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae4d44"
      ]
    ],
    [
      "00ae4ca0",
      "PARAM",
      [
        "storage",
        "002a0ecf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a8c.md#insn-00ae4adc) · [`00ae4b10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a8c.md#insn-00ae4b10) · [`00ae4b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a8c.md#insn-00ae4b78)
- 新版 [`00ae4ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md#insn-00ae4ba4) · [`00ae4bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md#insn-00ae4bd8) · [`00ae4c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md#insn-00ae4c40)

~~~diff
- 00ae4adc ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00ae4adc ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
+ 00ae4ba4 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00ae4ba4 ["CBRANCH", null, ["local:b43:8", "tmp:0:1"]]
- 00ae4adc bytes 160d00b4
+ 00ae4ba4 bytes 160d00b4
- 00ae4b10 ["COPY", "tmp:0:8", ["const:7d9:8"]]
- 00ae4b10 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 00ae4b10 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 00ae4b10 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 00ae4bd8 ["COPY", "tmp:0:8", ["const:866:8"]]
+ 00ae4bd8 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 00ae4bd8 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 00ae4bd8 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 00ae4b10 bytes 9c671f91
+ 00ae4bd8 bytes 9c9b2191
- 00ae4b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4b78 ["INT_ADD", "register:40f0:8", ["const:ae4b78:8", "const:4:8"]]
- 00ae4b78 ["CALLIND", null, ["register:0:8"]]
+ 00ae4c40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4c40 ["INT_ADD", "register:40f0:8", ["const:ae4c40:8", "const:4:8"]]
+ 00ae4c40 ["CALLIND", null, ["register:0:8"]]
- 00ae4b78 bytes 00013fd6
+ 00ae4c40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6445b2e79ed9ac37e13de608b108beb1"></a>

### [`00ae4d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4d34.md) → [`00ae4dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md) _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae4e3c",
      "incomplete_value": true,
      "site": "00ae4e3c",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4d74",
      "incomplete_value": true,
      "site": "00ae4d74",
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
            "const:268:8"
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
      "definition_site": "00ae4e18",
      "incomplete_value": true,
      "site": "00ae4e18",
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
      "definition_site": "00ae4d50",
      "incomplete_value": true,
      "site": "00ae4d50",
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
      "definition_site": "00ae4e20",
      "incomplete_value": false,
      "site": "00ae4e34",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4d58",
      "incomplete_value": false,
      "site": "00ae4d6c",
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
            "const:d64:8"
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
      "00ae4e10",
      "READ",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4e20",
      "PARAM",
      [
        "storage",
        "002a7d64",
        null,
        "string"
      ]
    ],
    [
      "00ae4e3c",
      "WRITE",
      [
        "storage",
        "010a0268",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4e10",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4e20",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae4e3c",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4d34.md#insn-00ae4d6c) · [`00ae4d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4d34.md#insn-00ae4d74) · [`00ae4d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4d34.md#insn-00ae4d48)
- 新版 [`00ae4e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md#insn-00ae4e34) · [`00ae4e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md#insn-00ae4e3c) · [`00ae4e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md#insn-00ae4e10)

~~~diff
- 00ae4d6c ["INT_ADD", "register:40f0:8", ["const:ae4d6c:8", "const:4:8"]]
- 00ae4d6c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae4e34 ["INT_ADD", "register:40f0:8", ["const:ae4e34:8", "const:4:8"]]
+ 00ae4e34 ["CALL", null, ["callee:00bde040:8"]]
- 00ae4d6c bytes 89e40394
+ 00ae4e34 bytes 83e40394
- 00ae4d74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:268:8"]]
- 00ae4d74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae4e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00ae4e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4d74 bytes 803601f9
+ 00ae4e3c bytes 809601f9
- 00ae4d48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:268:8"]]
- 00ae4d48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae4e10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
+ 00ae4e10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae4d48 bytes 813641f9
+ 00ae4e10 bytes 819641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eadf190719c008921bdee7353836fb7a"></a>

### [`00ae4da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4da4.md) → [`00ae4e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md) _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) · 呼出先 5件 [`00af14e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af14e8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) · 呼出先 5件 [`00af15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.26% / 新版 92.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae4ec4",
      "incomplete_value": false,
      "site": "00ae4ecc",
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
            "const:5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4dfc",
      "incomplete_value": false,
      "site": "00ae4e04",
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
            "const:61:8"
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
      "definition_site": "00ae5008",
      "incomplete_value": false,
      "site": "00ae500c",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4f40",
      "incomplete_value": false,
      "site": "00ae4f44",
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
            "const:68b:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae5030",
      "incomplete_value": false,
      "site": "00ae5034",
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
            "const:cd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4f68",
      "incomplete_value": false,
      "site": "00ae4f6c",
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
            "const:cde:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae4ec4",
      "PARAM",
      [
        "storage",
        "002a6061",
        null,
        "string"
      ]
    ],
    [
      "00ae4fb8",
      "PARAM",
      [
        "storage",
        "002a0e42",
        null,
        "string"
      ]
    ],
    [
      "00ae4fb8",
      "PARAM",
      [
        "storage",
        "002a9f78",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae4ec4",
      "PARAM",
      [
        "storage",
        "002a605a",
        null,
        "string"
      ]
    ],
    [
      "00ae4fb8",
      "PARAM",
      [
        "storage",
        "002a0ecf",
        null,
        "string"
      ]
    ],
    [
      "00ae4fb8",
      "PARAM",
      [
        "storage",
        "002a9f7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4da4.md#insn-00ae4e04) · [`00ae4ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4da4.md#insn-00ae4ea4) · [`00ae4ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4da4.md#insn-00ae4ecc)
- 新版 [`00ae4ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md#insn-00ae4ecc) · [`00ae4f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md#insn-00ae4f6c) · [`00ae4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md#insn-00ae4f94)

~~~diff
- 00ae4e04 ["INT_ADD", "register:40f0:8", ["const:ae4e04:8", "const:4:8"]]
- 00ae4e04 ["CALL", null, ["callee:00bde260:8"]]
+ 00ae4ecc ["INT_ADD", "register:40f0:8", ["const:ae4ecc:8", "const:4:8"]]
+ 00ae4ecc ["CALL", null, ["callee:00bde260:8"]]
- 00ae4e04 bytes ebe40394
+ 00ae4ecc bytes e5e40394
- 00ae4ea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4ea4 ["INT_ADD", "register:40f0:8", ["const:ae4ea4:8", "const:4:8"]]
- 00ae4ea4 ["CALLIND", null, ["register:0:8"]]
+ 00ae4f6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4f6c ["INT_ADD", "register:40f0:8", ["const:ae4f6c:8", "const:4:8"]]
+ 00ae4f6c ["CALLIND", null, ["register:0:8"]]
- 00ae4ea4 bytes 00013fd6
+ 00ae4f6c bytes 00013fd6
- 00ae4ecc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4ecc ["INT_ADD", "register:40f0:8", ["const:ae4ecc:8", "const:4:8"]]
- 00ae4ecc ["CALLIND", null, ["register:0:8"]]
+ 00ae4f94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4f94 ["INT_ADD", "register:40f0:8", ["const:ae4f94:8", "const:4:8"]]
+ 00ae4f94 ["CALLIND", null, ["register:0:8"]]
- 00ae4ecc bytes 00013fd6
+ 00ae4f94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4873a8397418072b662e863801524b28"></a>

### [`00ae5010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5010.md) → [`00ae50d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md) _ZN8firebase4util12class_loader10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae50f4",
      "incomplete_value": false,
      "site": "00ae50f8",
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
      "definition_site": "00ae502c",
      "incomplete_value": false,
      "site": "00ae5030",
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
      "definition_site": "00ae5104",
      "incomplete_value": true,
      "site": "00ae5110",
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
      "definition_site": "00ae503c",
      "incomplete_value": true,
      "site": "00ae5048",
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
      "00ae50f4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae5104",
      "DATA",
      [
        "storage",
        "010a0288",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae50f4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5104",
      "DATA",
      [
        "storage",
        "010a0348",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5010.md#insn-00ae5030) · [`00ae502c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5010.md#insn-00ae502c) · [`00ae5038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5010.md#insn-00ae5038)
- 新版 [`00ae50f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md#insn-00ae50f8) · [`00ae50f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md#insn-00ae50f4) · [`00ae5100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md#insn-00ae5100)

~~~diff
- 00ae5030 ["INT_ADD", "register:40f0:8", ["const:ae5030:8", "const:4:8"]]
- 00ae5030 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae50f8 ["INT_ADD", "register:40f0:8", ["const:ae50f8:8", "const:4:8"]]
+ 00ae50f8 ["CALL", null, ["callee:00bde130:8"]]
- 00ae5030 bytes 14e40394
+ 00ae50f8 bytes 0ee40394
- 00ae502c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae502c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae502c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae502c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae50f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae50f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae50f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae50f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae502c bytes 00c81791
+ 00ae50f4 bytes 00fc1991
- 00ae5038 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00ae5038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5100 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00ae5100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5038 bytes 08210a91
+ 00ae5100 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67ba40999e954e521d1e74f39616e3f2"></a>

### [`00ae508c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae508c.md) → [`00ae5154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00ae5180",
      "incomplete_value": true,
      "site": "00ae5180",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae50b8",
      "incomplete_value": true,
      "site": "00ae50b8",
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
            "const:290:8"
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
      "definition_site": "00ae5168",
      "incomplete_value": true,
      "site": "00ae5168",
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
      "definition_site": "00ae50a0",
      "incomplete_value": true,
      "site": "00ae50a0",
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
      "definition_site": "00ae5170",
      "incomplete_value": false,
      "site": "00ae5178",
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
            "const:f35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae50a8",
      "incomplete_value": false,
      "site": "00ae50b0",
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
            "const:ea8:8"
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
      "00ae5164",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5170",
      "PARAM",
      [
        "storage",
        "0029fea8",
        null,
        "string"
      ]
    ],
    [
      "00ae5180",
      "WRITE",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5164",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5170",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae5180",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae50b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae508c.md#insn-00ae50b0) · [`00ae50b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae508c.md#insn-00ae50b8) · [`00ae509c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae508c.md#insn-00ae509c)
- 新版 [`00ae5178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md#insn-00ae5178) · [`00ae5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md#insn-00ae5180) · [`00ae5164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md#insn-00ae5164)

~~~diff
- 00ae50b0 ["INT_ADD", "register:40f0:8", ["const:ae50b0:8", "const:4:8"]]
- 00ae50b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5178 ["INT_ADD", "register:40f0:8", ["const:ae5178:8", "const:4:8"]]
+ 00ae5178 ["CALL", null, ["callee:00bde040:8"]]
- 00ae50b0 bytes b8e30394
+ 00ae5178 bytes b2e30394
- 00ae50b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae50b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00ae5180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae50b8 bytes 604a01f9
+ 00ae5180 bytes 60aa01f9
- 00ae509c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae509c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00ae5164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae509c bytes 684a41f9
+ 00ae5164 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b253bd830fdac3d560fbf8e7f8ee8ad1"></a>

### [`00ae50cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae50cc.md) → [`00ae5194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae51c4",
      "incomplete_value": true,
      "site": "00ae51c4",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae50fc",
      "incomplete_value": true,
      "site": "00ae50fc",
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
            "const:290:8"
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
      "definition_site": "00ae51a8",
      "incomplete_value": true,
      "site": "00ae51a8",
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
      "definition_site": "00ae50e0",
      "incomplete_value": true,
      "site": "00ae50e0",
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
      "definition_site": "00ae51b4",
      "incomplete_value": false,
      "site": "00ae51bc",
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
            "const:f35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae50ec",
      "incomplete_value": false,
      "site": "00ae50f4",
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
            "const:ea8:8"
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
      "00ae51a4",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51b4",
      "PARAM",
      [
        "storage",
        "0029fea8",
        null,
        "string"
      ]
    ],
    [
      "00ae51c4",
      "WRITE",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae51a4",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51b4",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae51c4",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae50f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae50cc.md#insn-00ae50f4) · [`00ae50fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae50cc.md#insn-00ae50fc) · [`00ae50dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae50cc.md#insn-00ae50dc)
- 新版 [`00ae51bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md#insn-00ae51bc) · [`00ae51c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md#insn-00ae51c4) · [`00ae51a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md#insn-00ae51a4)

~~~diff
- 00ae50f4 ["INT_ADD", "register:40f0:8", ["const:ae50f4:8", "const:4:8"]]
- 00ae50f4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae51bc ["INT_ADD", "register:40f0:8", ["const:ae51bc:8", "const:4:8"]]
+ 00ae51bc ["CALL", null, ["callee:00bde040:8"]]
- 00ae50f4 bytes a7e30394
+ 00ae51bc bytes a1e30394
- 00ae50fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae50fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae51c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00ae51c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae50fc bytes 604a01f9
+ 00ae51c4 bytes 60aa01f9
- 00ae50dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae50dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae51a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00ae51a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae50dc bytes 684a41f9
+ 00ae51a4 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a1549236c8a26b5d34c6207c7760689"></a>

### [`00ae5110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5110.md) → [`00ae51d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5208",
      "incomplete_value": true,
      "site": "00ae5208",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5140",
      "incomplete_value": true,
      "site": "00ae5140",
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
            "const:290:8"
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
    "old": {
      "definition_site": "00ae5124",
      "incomplete_value": true,
      "site": "00ae5124",
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
      "definition_site": "00ae51f4",
      "incomplete_value": false,
      "site": "00ae5200",
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
            "const:f35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae512c",
      "incomplete_value": false,
      "site": "00ae5138",
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
            "const:ea8:8"
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
      "00ae51e8",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51f4",
      "PARAM",
      [
        "storage",
        "0029fea8",
        null,
        "string"
      ]
    ],
    [
      "00ae5208",
      "WRITE",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae51e8",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51f4",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae5208",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5110.md#insn-00ae5138) · [`00ae5140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5110.md#insn-00ae5140) · [`00ae5120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5110.md#insn-00ae5120)
- 新版 [`00ae5200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md#insn-00ae5200) · [`00ae5208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md#insn-00ae5208) · [`00ae51e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md#insn-00ae51e8)

~~~diff
- 00ae5138 ["INT_ADD", "register:40f0:8", ["const:ae5138:8", "const:4:8"]]
- 00ae5138 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5200 ["INT_ADD", "register:40f0:8", ["const:ae5200:8", "const:4:8"]]
+ 00ae5200 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5138 bytes 96e30394
+ 00ae5200 bytes 90e30394
- 00ae5140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae5140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00ae5208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5140 bytes 604a01f9
+ 00ae5208 bytes 60aa01f9
- 00ae5120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00ae5120 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae51e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00ae51e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5120 bytes 684a41f9
+ 00ae51e8 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b9a63f4c692f46a89edfb4fbc94018"></a>

### [`00ae5160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5160.md) → [`00ae5228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md) _ZN8firebase4util17jniresultcallback15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae52b0",
      "incomplete_value": true,
      "site": "00ae52b0",
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
      "definition_site": "00ae51e8",
      "incomplete_value": true,
      "site": "00ae51e8",
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
            "const:298:8"
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
      "definition_site": "00ae525c",
      "incomplete_value": true,
      "site": "00ae5268",
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5194",
      "incomplete_value": true,
      "site": "00ae51a0",
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
                "const:290:8"
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
      "00ae523c",
      "READ",
      [
        "storage",
        "010a0298",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae525c",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae52b0",
      "WRITE",
      [
        "storage",
        "010a0298",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae523c",
      "READ",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae525c",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae52b0",
      "WRITE",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae51a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5160.md#insn-00ae51a0) · [`00ae51e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5160.md#insn-00ae51e8) · [`00ae5174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5160.md#insn-00ae5174)
- 新版 [`00ae5268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md#insn-00ae5268) · [`00ae52b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md#insn-00ae52b0) · [`00ae523c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md#insn-00ae523c)

~~~diff
- 00ae51a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae51a0 ["INT_ADD", "register:40f0:8", ["const:ae51a0:8", "const:4:8"]]
- 00ae51a0 ["CALLIND", null, ["register:0:8"]]
+ 00ae5268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5268 ["INT_ADD", "register:40f0:8", ["const:ae5268:8", "const:4:8"]]
+ 00ae5268 ["CALLIND", null, ["register:0:8"]]
- 00ae51a0 bytes 00013fd6
+ 00ae5268 bytes 00013fd6
- 00ae51e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae51e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:298:8"]]
- 00ae51e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae52b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae52b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:358:8"]]
+ 00ae52b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae51e8 bytes a0620a39
+ 00ae52b0 bytes a0620d39
- 00ae5174 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:298:8"]]
- 00ae5174 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae5174 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae523c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:358:8"]]
+ 00ae523c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae523c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae5174 bytes a8624a39
+ 00ae523c bytes a8624d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c23fb5a8ec54abf04da27d97184a6790"></a>

### [`00ae51fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae51fc.md) → [`00ae52c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md) _ZN8firebase4util17jniresultcallback12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00ae5300",
      "incomplete_value": true,
      "site": "00ae5300",
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
      "definition_site": "00ae5238",
      "incomplete_value": true,
      "site": "00ae5238",
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
            "const:298:8"
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
      "definition_site": "00ae5350",
      "incomplete_value": true,
      "site": "00ae5350",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5288",
      "incomplete_value": true,
      "site": "00ae5288",
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
            "const:290:8"
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
      "definition_site": "00ae52dc",
      "incomplete_value": true,
      "site": "00ae52dc",
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
      "definition_site": "00ae5214",
      "incomplete_value": true,
      "site": "00ae5214",
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
      "00ae52d8",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae52e4",
      "READ",
      [
        "storage",
        "010a0298",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5300",
      "WRITE",
      [
        "storage",
        "010a0298",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae52d8",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae52e4",
      "READ",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5300",
      "WRITE",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae51fc.md#insn-00ae5238) · [`00ae5284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae51fc.md#insn-00ae5284) · [`00ae5288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae51fc.md#insn-00ae5288)
- 新版 [`00ae5300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md#insn-00ae5300) · [`00ae534c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md#insn-00ae534c) · [`00ae5350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md#insn-00ae5350)

~~~diff
- 00ae5238 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5238 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5238 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:298:8"]]
- 00ae5238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae5300 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae5300 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae5300 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
+ 00ae5300 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5238 bytes bf620a39
+ 00ae5300 bytes bf620d39
- 00ae5284 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5284 ["INT_ADD", "register:40f0:8", ["const:ae5284:8", "const:4:8"]]
- 00ae5284 ["CALLIND", null, ["register:0:8"]]
+ 00ae534c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae534c ["INT_ADD", "register:40f0:8", ["const:ae534c:8", "const:4:8"]]
+ 00ae534c ["CALLIND", null, ["register:0:8"]]
- 00ae5284 bytes 00013fd6
+ 00ae534c bytes 00013fd6
- 00ae5288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00ae5288 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae5288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae5350 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00ae5350 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae5350 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae5288 bytes 9f4a01f9
+ 00ae5350 bytes 9faa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffa2e747b8601415e88cb276f7a90b57"></a>

### [`00ae529c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae529c.md) → [`00ae5364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md) _ZN8firebase4util17jniresultcallback14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae53a4",
      "incomplete_value": true,
      "site": "00ae53a4",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae52dc",
      "incomplete_value": true,
      "site": "00ae52dc",
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
            "const:290:8"
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
      "definition_site": "00ae5380",
      "incomplete_value": true,
      "site": "00ae5380",
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
      "definition_site": "00ae52b8",
      "incomplete_value": true,
      "site": "00ae52b8",
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
      "definition_site": "00ae5388",
      "incomplete_value": false,
      "site": "00ae539c",
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
            "const:f35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae52c0",
      "incomplete_value": false,
      "site": "00ae52d4",
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
            "const:ea8:8"
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
      "00ae5378",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5388",
      "PARAM",
      [
        "storage",
        "0029fea8",
        null,
        "string"
      ]
    ],
    [
      "00ae53a4",
      "WRITE",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5378",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5388",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae53a4",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae52d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae529c.md#insn-00ae52d4) · [`00ae52dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae529c.md#insn-00ae52dc) · [`00ae52b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae529c.md#insn-00ae52b0)
- 新版 [`00ae539c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md#insn-00ae539c) · [`00ae53a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md#insn-00ae53a4) · [`00ae5378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md#insn-00ae5378)

~~~diff
- 00ae52d4 ["INT_ADD", "register:40f0:8", ["const:ae52d4:8", "const:4:8"]]
- 00ae52d4 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae539c ["INT_ADD", "register:40f0:8", ["const:ae539c:8", "const:4:8"]]
+ 00ae539c ["CALL", null, ["callee:00bde040:8"]]
- 00ae52d4 bytes 2fe30394
+ 00ae539c bytes 29e30394
- 00ae52dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00ae52dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae53a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00ae53a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae52dc bytes 804a01f9
+ 00ae53a4 bytes 80aa01f9
- 00ae52b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00ae52b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5378 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00ae5378 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae52b0 bytes 814a41f9
+ 00ae5378 bytes 81aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-513c24cbf44452f92b979d93af4f155c"></a>

### [`00ae5348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5348.md) → [`00ae5410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md) _ZN8firebase4util17jniresultcallback13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5450",
      "incomplete_value": true,
      "site": "00ae5450",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5388",
      "incomplete_value": true,
      "site": "00ae5388",
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
            "const:290:8"
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
      "definition_site": "00ae542c",
      "incomplete_value": true,
      "site": "00ae542c",
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
      "definition_site": "00ae5364",
      "incomplete_value": true,
      "site": "00ae5364",
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
      "definition_site": "00ae5434",
      "incomplete_value": false,
      "site": "00ae5448",
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
            "const:f35:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae536c",
      "incomplete_value": false,
      "site": "00ae5380",
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
            "const:ea8:8"
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
      "00ae5424",
      "READ",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5434",
      "PARAM",
      [
        "storage",
        "0029fea8",
        null,
        "string"
      ]
    ],
    [
      "00ae5450",
      "WRITE",
      [
        "storage",
        "010a0290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5424",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5434",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae5450",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5348.md#insn-00ae5380) · [`00ae5388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5348.md#insn-00ae5388) · [`00ae535c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5348.md#insn-00ae535c)
- 新版 [`00ae5448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md#insn-00ae5448) · [`00ae5450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md#insn-00ae5450) · [`00ae5424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md#insn-00ae5424)

~~~diff
- 00ae5380 ["INT_ADD", "register:40f0:8", ["const:ae5380:8", "const:4:8"]]
- 00ae5380 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5448 ["INT_ADD", "register:40f0:8", ["const:ae5448:8", "const:4:8"]]
+ 00ae5448 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5380 bytes 04e30394
+ 00ae5448 bytes fee20394
- 00ae5388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00ae5388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5450 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00ae5450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5388 bytes 804a01f9
+ 00ae5450 bytes 80aa01f9
- 00ae535c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00ae535c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5424 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00ae5424 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae535c bytes 814a41f9
+ 00ae5424 bytes 81aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ab26cb173619c4228c63fd82b607cb"></a>

### [`00ae53b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53b8.md) → [`00ae5480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md) _ZN8firebase4util17jniresultcallback10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae549c",
      "incomplete_value": false,
      "site": "00ae54a0",
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
      "definition_site": "00ae53d4",
      "incomplete_value": false,
      "site": "00ae53d8",
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
      "definition_site": "00ae54ac",
      "incomplete_value": true,
      "site": "00ae54b8",
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
      "definition_site": "00ae53e4",
      "incomplete_value": true,
      "site": "00ae53f0",
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
      "00ae549c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae54ac",
      "DATA",
      [
        "storage",
        "010a02b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae549c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae54ac",
      "DATA",
      [
        "storage",
        "010a0370",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae53d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53b8.md#insn-00ae53d8) · [`00ae53d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53b8.md#insn-00ae53d4) · [`00ae53e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53b8.md#insn-00ae53e0)
- 新版 [`00ae54a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md#insn-00ae54a0) · [`00ae549c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md#insn-00ae549c) · [`00ae54a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md#insn-00ae54a8)

~~~diff
- 00ae53d8 ["INT_ADD", "register:40f0:8", ["const:ae53d8:8", "const:4:8"]]
- 00ae53d8 ["CALL", null, ["callee:00bde130:8"]]
+ 00ae54a0 ["INT_ADD", "register:40f0:8", ["const:ae54a0:8", "const:4:8"]]
+ 00ae54a0 ["CALL", null, ["callee:00bde130:8"]]
- 00ae53d8 bytes 2ae30394
+ 00ae54a0 bytes 24e30394
- 00ae53d4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae53d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae53d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae53d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae549c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00ae549c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae549c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae549c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae53d4 bytes 00c81791
+ 00ae549c bytes 00fc1991
- 00ae53e0 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00ae53e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae53e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae53e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae54a8 ["COPY", "tmp:0:8", ["const:370:8"]]
+ 00ae54a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae54a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae54a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae53e0 bytes 08c10a91
+ 00ae54a8 bytes 08c10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01c90da611bd89e2b5f8a85b12e83d00"></a>

### [`00ae53f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53f4.md) → [`00ae54bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00ae54e8",
      "incomplete_value": true,
      "site": "00ae54e8",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5420",
      "incomplete_value": true,
      "site": "00ae5420",
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
            "const:2b8:8"
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
      "definition_site": "00ae54d0",
      "incomplete_value": true,
      "site": "00ae54d0",
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
      "definition_site": "00ae5408",
      "incomplete_value": true,
      "site": "00ae5408",
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
      "definition_site": "00ae54dc",
      "incomplete_value": false,
      "site": "00ae54e0",
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
            "const:2f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5414",
      "incomplete_value": false,
      "site": "00ae5418",
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
            "const:2fc:8"
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
      "00ae54cc",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae54dc",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ],
    [
      "00ae54e8",
      "WRITE",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae54cc",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae54dc",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "00ae54e8",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53f4.md#insn-00ae5418) · [`00ae5420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53f4.md#insn-00ae5420) · [`00ae5404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae53f4.md#insn-00ae5404)
- 新版 [`00ae54e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md#insn-00ae54e0) · [`00ae54e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md#insn-00ae54e8) · [`00ae54cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md#insn-00ae54cc)

~~~diff
- 00ae5418 ["INT_ADD", "register:40f0:8", ["const:ae5418:8", "const:4:8"]]
- 00ae5418 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae54e0 ["INT_ADD", "register:40f0:8", ["const:ae54e0:8", "const:4:8"]]
+ 00ae54e0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5418 bytes dee20394
+ 00ae54e0 bytes d8e20394
- 00ae5420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00ae5420 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae54e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
+ 00ae54e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5420 bytes 605e01f9
+ 00ae54e8 bytes 60be01f9
- 00ae5404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00ae5404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae54cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
+ 00ae54cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5404 bytes 685e41f9
+ 00ae54cc bytes 68be41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18af2b15e3cc43b3456ac0884c3fbd2b"></a>

### [`00ae5434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5434.md) → [`00ae54fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54fc.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae5460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae5528"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae5510",
      "incomplete_value": true,
      "site": "00ae5510",
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
      "definition_site": "00ae5448",
      "incomplete_value": true,
      "site": "00ae5448",
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
      "00ae550c",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5450",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5458",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae550c",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5518",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "00ae5520",
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

- 旧版 [`00ae5448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5434.md#insn-00ae5448) · [`00ae5458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5434.md#insn-00ae5458) · [`00ae5460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5434.md#insn-00ae5460)
- 新版 [`00ae5510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54fc.md#insn-00ae5510)

~~~diff
- 00ae5448 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5448 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae5510 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae5510 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5448 bytes e80000b5
+ 00ae5510 bytes e80000b5
- 00ae5458 ["INT_ADD", "register:40f0:8", ["const:ae5458:8", "const:4:8"]]
- 00ae5458 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5458 bytes cee20394
- 00ae5460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00ae5460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5460 bytes 605e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4504f39f75a2e4c5d07410d7e5aa54d7"></a>

### [`00ae5474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5474.md) → [`00ae553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae556c",
      "incomplete_value": true,
      "site": "00ae556c",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae54a4",
      "incomplete_value": true,
      "site": "00ae54a4",
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
            "const:2b8:8"
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
      "definition_site": "00ae5550",
      "incomplete_value": true,
      "site": "00ae5550",
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
      "definition_site": "00ae5488",
      "incomplete_value": true,
      "site": "00ae5488",
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
      "definition_site": "00ae555c",
      "incomplete_value": false,
      "site": "00ae5564",
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
            "const:2f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5494",
      "incomplete_value": false,
      "site": "00ae549c",
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
            "const:2fc:8"
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
      "00ae554c",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae555c",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ],
    [
      "00ae556c",
      "WRITE",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae554c",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae555c",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "00ae556c",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae549c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5474.md#insn-00ae549c) · [`00ae54a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5474.md#insn-00ae54a4) · [`00ae5484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5474.md#insn-00ae5484)
- 新版 [`00ae5564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md#insn-00ae5564) · [`00ae556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md#insn-00ae556c) · [`00ae554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md#insn-00ae554c)

~~~diff
- 00ae549c ["INT_ADD", "register:40f0:8", ["const:ae549c:8", "const:4:8"]]
- 00ae549c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5564 ["INT_ADD", "register:40f0:8", ["const:ae5564:8", "const:4:8"]]
+ 00ae5564 ["CALL", null, ["callee:00bde040:8"]]
- 00ae549c bytes bde20394
+ 00ae5564 bytes b7e20394
- 00ae54a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00ae54a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae556c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
+ 00ae556c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae54a4 bytes 605e01f9
+ 00ae556c bytes 60be01f9
- 00ae5484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00ae5484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae554c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
+ 00ae554c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5484 bytes 685e41f9
+ 00ae554c bytes 68be41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c90f32416dd56acee343735403b266ea"></a>

### [`00ae54b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae54b8.md) → [`00ae5580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae54e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae55b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00ae54cc",
      "incomplete_value": true,
      "site": "00ae54cc",
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
      "00ae5590",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae54d4",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae54e8",
      "WRITE",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5590",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae559c",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "00ae55b0",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae54cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae54b8.md#insn-00ae54cc) · [`00ae54e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae54b8.md#insn-00ae54e0) · [`00ae54e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae54b8.md#insn-00ae54e8)
- 新版 [`00ae5594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md#insn-00ae5594) · [`00ae55a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md#insn-00ae55a8)

~~~diff
- 00ae54cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae54cc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae5594 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae5594 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae54cc bytes 080100b5
+ 00ae5594 bytes 080100b5
- 00ae54e0 ["INT_ADD", "register:40f0:8", ["const:ae54e0:8", "const:4:8"]]
- 00ae54e0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae55a8 ["INT_ADD", "register:40f0:8", ["const:ae55a8:8", "const:4:8"]]
+ 00ae55a8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae54e0 bytes ace20394
+ 00ae55a8 bytes a6e20394
- 00ae54e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00ae54e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae54e8 bytes 605e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c747262a21493250d3f16749fda50c8d"></a>

### [`00ae5508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5508.md) → [`00ae55d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae55d0.md) _ZN8firebase4util26cppthreaddispatchercontext15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 25.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5508"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae550c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae550c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5508",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae550c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5510",
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
      "00ae55d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae55d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae55d8",
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

- 旧版 [`00ae5508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5508.md#insn-00ae5508) · [`00ae550c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5508.md#insn-00ae550c) · [`00ae5510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5508.md#insn-00ae5510)

~~~diff
- 00ae5508 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae5508 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae5508 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5508 bytes f50f1df8
- 00ae550c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae550c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae550c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae550c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae550c bytes f44f01a9
- 00ae5510 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5510 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5510 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae5510 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5510 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3bf97055adb4dcc6040126fd2eb8a08"></a>

### [`00ae55a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae55a4.md) → [`00ae566c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae566c.md) _ZN8firebase4util26cppthreaddispatchercontext12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 70.00% / 新版 77.78%

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
      "site": "00ae55e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae56f8",
      "incomplete_value": true,
      "site": "00ae56f8",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5630",
      "incomplete_value": true,
      "site": "00ae5630",
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
            "const:2b8:8"
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
      "site": "00ae56a8"
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
      "00ae5680",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae568c",
      "READ",
      [
        "storage",
        "010a02c0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae55e0",
      "WRITE",
      [
        "storage",
        "010a02c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5680",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae568c",
      "READ",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae56a8",
      "WRITE",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae55bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae55a4.md#insn-00ae55bc) · [`00ae55dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae55a4.md#insn-00ae55dc) · [`00ae55e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae55a4.md#insn-00ae55e0)
- 新版 [`00ae5684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae566c.md#insn-00ae5684)

~~~diff
- 00ae55bc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae55bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae5684 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae5684 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae55bc bytes c10300b4
+ 00ae5684 bytes c10300b4
- 00ae55dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae55dc ["INT_ADD", "register:40f0:8", ["const:ae55dc:8", "const:4:8"]]
- 00ae55dc ["CALLIND", null, ["register:0:8"]]
- 00ae55dc bytes 00013fd6
- 00ae55e0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae55e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae55e0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2c0:8"]]
- 00ae55e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae55e0 bytes bf020b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7748b6371d97592a3912b0bffc1891ef"></a>

### [`00ae5644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5644.md) → [`00ae570c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md) _ZN8firebase4util26cppthreaddispatchercontext14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae574c",
      "incomplete_value": true,
      "site": "00ae574c",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5684",
      "incomplete_value": true,
      "site": "00ae5684",
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
            "const:2b8:8"
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
      "definition_site": "00ae5728",
      "incomplete_value": true,
      "site": "00ae5728",
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
      "definition_site": "00ae5660",
      "incomplete_value": true,
      "site": "00ae5660",
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
      "definition_site": "00ae5730",
      "incomplete_value": false,
      "site": "00ae5744",
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
            "const:2f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5668",
      "incomplete_value": false,
      "site": "00ae567c",
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
            "const:2fc:8"
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
      "00ae5720",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5730",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ],
    [
      "00ae574c",
      "WRITE",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5720",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5730",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "00ae574c",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae567c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5644.md#insn-00ae567c) · [`00ae5684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5644.md#insn-00ae5684) · [`00ae5658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5644.md#insn-00ae5658)
- 新版 [`00ae5744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md#insn-00ae5744) · [`00ae574c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md#insn-00ae574c) · [`00ae5720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md#insn-00ae5720)

~~~diff
- 00ae567c ["INT_ADD", "register:40f0:8", ["const:ae567c:8", "const:4:8"]]
- 00ae567c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5744 ["INT_ADD", "register:40f0:8", ["const:ae5744:8", "const:4:8"]]
+ 00ae5744 ["CALL", null, ["callee:00bde040:8"]]
- 00ae567c bytes 45e20394
+ 00ae5744 bytes 3fe20394
- 00ae5684 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00ae5684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae574c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
+ 00ae574c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5684 bytes 805e01f9
+ 00ae574c bytes 80be01f9
- 00ae5658 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00ae5658 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
+ 00ae5720 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5658 bytes 815e41f9
+ 00ae5720 bytes 81be41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a602aefadb478d37068d4bd99e0af1e"></a>

### [`00ae56f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56f0.md) → [`00ae57b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md) _ZN8firebase4util26cppthreaddispatchercontext13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae57f8",
      "incomplete_value": true,
      "site": "00ae57f8",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5730",
      "incomplete_value": true,
      "site": "00ae5730",
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
            "const:2b8:8"
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
      "definition_site": "00ae57d4",
      "incomplete_value": true,
      "site": "00ae57d4",
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
      "definition_site": "00ae570c",
      "incomplete_value": true,
      "site": "00ae570c",
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
      "definition_site": "00ae57dc",
      "incomplete_value": false,
      "site": "00ae57f0",
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
            "const:2f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5714",
      "incomplete_value": false,
      "site": "00ae5728",
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
            "const:2fc:8"
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
      "00ae57cc",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae57dc",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ],
    [
      "00ae57f8",
      "WRITE",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae57cc",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae57dc",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ],
    [
      "00ae57f8",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56f0.md#insn-00ae5728) · [`00ae5730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56f0.md#insn-00ae5730) · [`00ae5704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae56f0.md#insn-00ae5704)
- 新版 [`00ae57f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md#insn-00ae57f0) · [`00ae57f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md#insn-00ae57f8) · [`00ae57cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md#insn-00ae57cc)

~~~diff
- 00ae5728 ["INT_ADD", "register:40f0:8", ["const:ae5728:8", "const:4:8"]]
- 00ae5728 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae57f0 ["INT_ADD", "register:40f0:8", ["const:ae57f0:8", "const:4:8"]]
+ 00ae57f0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5728 bytes 1ae20394
+ 00ae57f0 bytes 14e20394
- 00ae5730 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00ae5730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae57f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
+ 00ae57f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5730 bytes 805e01f9
+ 00ae57f8 bytes 80be01f9
- 00ae5704 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00ae5704 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae57cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
+ 00ae57cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5704 bytes 815e41f9
+ 00ae57cc bytes 81be41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f61c881e492a36efe665e885cdc8ed6"></a>

### [`00ae579c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae579c.md) → [`00ae5864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

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
      "definition_site": "00ae5890",
      "incomplete_value": true,
      "site": "00ae5890",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae57c8",
      "incomplete_value": true,
      "site": "00ae57c8",
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
            "const:2f0:8"
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
      "definition_site": "00ae5878",
      "incomplete_value": true,
      "site": "00ae5878",
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
      "definition_site": "00ae57b0",
      "incomplete_value": true,
      "site": "00ae57b0",
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
      "definition_site": "00ae5884",
      "incomplete_value": false,
      "site": "00ae5888",
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
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae57bc",
      "incomplete_value": false,
      "site": "00ae57c0",
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
            "const:fc4:8"
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
      "00ae5874",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5884",
      "PARAM",
      [
        "storage",
        "002a9fc4",
        null,
        "string"
      ]
    ],
    [
      "00ae5890",
      "WRITE",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5874",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5884",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ],
    [
      "00ae5890",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae57c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae579c.md#insn-00ae57c0) · [`00ae57c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae579c.md#insn-00ae57c8) · [`00ae57ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae579c.md#insn-00ae57ac)
- 新版 [`00ae5888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md#insn-00ae5888) · [`00ae5890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md#insn-00ae5890) · [`00ae5874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md#insn-00ae5874)

~~~diff
- 00ae57c0 ["INT_ADD", "register:40f0:8", ["const:ae57c0:8", "const:4:8"]]
- 00ae57c0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5888 ["INT_ADD", "register:40f0:8", ["const:ae5888:8", "const:4:8"]]
+ 00ae5888 ["CALL", null, ["callee:00bde040:8"]]
- 00ae57c0 bytes f4e10394
+ 00ae5888 bytes eee10394
- 00ae57c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae57c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae5890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae57c8 bytes 607a01f9
+ 00ae5890 bytes 60da01f9
- 00ae57ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae57ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae5874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae57ac bytes 687a41f9
+ 00ae5874 bytes 68da41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-320c351fe6a8e44cb1e7746264499c7a"></a>

### [`00ae57dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae57dc.md) → [`00ae58a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

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
      "definition_site": "00ae58d0",
      "incomplete_value": true,
      "site": "00ae58d0",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5808",
      "incomplete_value": true,
      "site": "00ae5808",
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
            "const:2f0:8"
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
      "definition_site": "00ae58b8",
      "incomplete_value": true,
      "site": "00ae58b8",
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
      "definition_site": "00ae57f0",
      "incomplete_value": true,
      "site": "00ae57f0",
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
      "definition_site": "00ae58c0",
      "incomplete_value": false,
      "site": "00ae58c8",
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
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae57f8",
      "incomplete_value": false,
      "site": "00ae5800",
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
            "const:fc4:8"
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
      "00ae58b4",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae58c0",
      "PARAM",
      [
        "storage",
        "002a9fc4",
        null,
        "string"
      ]
    ],
    [
      "00ae58d0",
      "WRITE",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae58b4",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae58c0",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ],
    [
      "00ae58d0",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae57dc.md#insn-00ae5800) · [`00ae5808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae57dc.md#insn-00ae5808) · [`00ae57ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae57dc.md#insn-00ae57ec)
- 新版 [`00ae58c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md#insn-00ae58c8) · [`00ae58d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md#insn-00ae58d0) · [`00ae58b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md#insn-00ae58b4)

~~~diff
- 00ae5800 ["INT_ADD", "register:40f0:8", ["const:ae5800:8", "const:4:8"]]
- 00ae5800 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae58c8 ["INT_ADD", "register:40f0:8", ["const:ae58c8:8", "const:4:8"]]
+ 00ae58c8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5800 bytes e4e10394
+ 00ae58c8 bytes dee10394
- 00ae5808 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae5808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae58d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae58d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5808 bytes 607a01f9
+ 00ae58d0 bytes 60da01f9
- 00ae57ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae57ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae58b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae58b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae57ec bytes 687a41f9
+ 00ae58b4 bytes 68da41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde70d31728632409990f808fa645a92"></a>

### [`00ae581c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae581c.md) → [`00ae58e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae5914",
      "incomplete_value": true,
      "site": "00ae5914",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae584c",
      "incomplete_value": true,
      "site": "00ae584c",
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
            "const:2f0:8"
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
      "definition_site": "00ae58f8",
      "incomplete_value": true,
      "site": "00ae58f8",
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
      "definition_site": "00ae5830",
      "incomplete_value": true,
      "site": "00ae5830",
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
      "definition_site": "00ae5904",
      "incomplete_value": false,
      "site": "00ae590c",
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
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae583c",
      "incomplete_value": false,
      "site": "00ae5844",
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
            "const:fc4:8"
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
      "00ae58f4",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5904",
      "PARAM",
      [
        "storage",
        "002a9fc4",
        null,
        "string"
      ]
    ],
    [
      "00ae5914",
      "WRITE",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae58f4",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5904",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ],
    [
      "00ae5914",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae581c.md#insn-00ae5844) · [`00ae584c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae581c.md#insn-00ae584c) · [`00ae582c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae581c.md#insn-00ae582c)
- 新版 [`00ae590c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md#insn-00ae590c) · [`00ae5914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md#insn-00ae5914) · [`00ae58f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md#insn-00ae58f4)

~~~diff
- 00ae5844 ["INT_ADD", "register:40f0:8", ["const:ae5844:8", "const:4:8"]]
- 00ae5844 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae590c ["INT_ADD", "register:40f0:8", ["const:ae590c:8", "const:4:8"]]
+ 00ae590c ["CALL", null, ["callee:00bde040:8"]]
- 00ae5844 bytes d3e10394
+ 00ae590c bytes cde10394
- 00ae584c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae584c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae5914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae584c bytes 607a01f9
+ 00ae5914 bytes 60da01f9
- 00ae582c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae582c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae58f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae58f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae582c bytes 687a41f9
+ 00ae58f4 bytes 68da41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb21713f9c55196d692e75a5d15af1bc"></a>

### [`00ae5860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5860.md) → [`00ae5928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5958",
      "incomplete_value": true,
      "site": "00ae5958",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5890",
      "incomplete_value": true,
      "site": "00ae5890",
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
            "const:2f0:8"
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
      "definition_site": "00ae593c",
      "incomplete_value": true,
      "site": "00ae593c",
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
      "definition_site": "00ae5874",
      "incomplete_value": true,
      "site": "00ae5874",
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
      "definition_site": "00ae5944",
      "incomplete_value": false,
      "site": "00ae5950",
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
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae587c",
      "incomplete_value": false,
      "site": "00ae5888",
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
            "const:fc4:8"
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
      "00ae5938",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5944",
      "PARAM",
      [
        "storage",
        "002a9fc4",
        null,
        "string"
      ]
    ],
    [
      "00ae5958",
      "WRITE",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5938",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5944",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ],
    [
      "00ae5958",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5860.md#insn-00ae5888) · [`00ae5890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5860.md#insn-00ae5890) · [`00ae5870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5860.md#insn-00ae5870)
- 新版 [`00ae5950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md#insn-00ae5950) · [`00ae5958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md#insn-00ae5958) · [`00ae5938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md#insn-00ae5938)

~~~diff
- 00ae5888 ["INT_ADD", "register:40f0:8", ["const:ae5888:8", "const:4:8"]]
- 00ae5888 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5950 ["INT_ADD", "register:40f0:8", ["const:ae5950:8", "const:4:8"]]
+ 00ae5950 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5888 bytes c2e10394
+ 00ae5950 bytes bce10394
- 00ae5890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae5890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae5958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5890 bytes 607a01f9
+ 00ae5958 bytes 60da01f9
- 00ae5870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00ae5870 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
+ 00ae5938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5870 bytes 687a41f9
+ 00ae5938 bytes 68da41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5ad2270e17548c3d9f992d35f0c2834"></a>

### [`00ae58b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae58b0.md) → [`00ae5978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md) _ZN8firebase4util19cppthreaddispatcher15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae5a00",
      "incomplete_value": true,
      "site": "00ae5a00",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5938",
      "incomplete_value": true,
      "site": "00ae5938",
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
            "const:2f8:8"
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
      "definition_site": "00ae59ac",
      "incomplete_value": true,
      "site": "00ae59b8",
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
                "const:3b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae58e4",
      "incomplete_value": true,
      "site": "00ae58f0",
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
                "const:2f0:8"
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
      "00ae598c",
      "READ",
      [
        "storage",
        "010a02f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae59ac",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a00",
      "WRITE",
      [
        "storage",
        "010a02f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae598c",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae59ac",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a00",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae58f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae58b0.md#insn-00ae58f0) · [`00ae5938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae58b0.md#insn-00ae5938) · [`00ae58c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae58b0.md#insn-00ae58c4)
- 新版 [`00ae59b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md#insn-00ae59b8) · [`00ae5a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md#insn-00ae5a00) · [`00ae598c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md#insn-00ae598c)

~~~diff
- 00ae58f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae58f0 ["INT_ADD", "register:40f0:8", ["const:ae58f0:8", "const:4:8"]]
- 00ae58f0 ["CALLIND", null, ["register:0:8"]]
+ 00ae59b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae59b8 ["INT_ADD", "register:40f0:8", ["const:ae59b8:8", "const:4:8"]]
+ 00ae59b8 ["CALLIND", null, ["register:0:8"]]
- 00ae58f0 bytes 00013fd6
+ 00ae59b8 bytes 00013fd6
- 00ae5938 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae5938 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2f8:8"]]
- 00ae5938 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae5a00 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae5a00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3b8:8"]]
+ 00ae5a00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae5938 bytes a0e20b39
+ 00ae5a00 bytes a0e20e39
- 00ae58c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2f8:8"]]
- 00ae58c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae58c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae598c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3b8:8"]]
+ 00ae598c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae598c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae58c4 bytes a8e24b39
+ 00ae598c bytes a8e24e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fa6a6240390cbd3a7c44bfa1c7f5e44"></a>

### [`00ae594c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae594c.md) → [`00ae5a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md) _ZN8firebase4util19cppthreaddispatcher12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 50.00% / 新版 55.56%

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
      "site": "00ae5988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae5aa0",
      "incomplete_value": true,
      "site": "00ae5aa0",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae59d8",
      "incomplete_value": true,
      "site": "00ae59d8",
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
            "const:2f0:8"
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
      "site": "00ae5a50"
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
      "00ae5a28",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae596c",
      "READ",
      [
        "storage",
        "010a02f8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae5988",
      "WRITE",
      [
        "storage",
        "010a02f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5a28",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a34",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5a50",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae594c.md#insn-00ae5964) · [`00ae5988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae594c.md#insn-00ae5988) · [`00ae59d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae594c.md#insn-00ae59d4)
- 新版 [`00ae5a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md#insn-00ae5a2c) · [`00ae5a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md#insn-00ae5a9c)

~~~diff
- 00ae5964 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5964 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00ae5a2c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00ae5a2c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae5964 bytes c10300b4
+ 00ae5a2c bytes c10300b4
- 00ae5988 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5988 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5988 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2f8:8"]]
- 00ae5988 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5988 bytes bfe20b39
- 00ae59d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae59d4 ["INT_ADD", "register:40f0:8", ["const:ae59d4:8", "const:4:8"]]
- 00ae59d4 ["CALLIND", null, ["register:0:8"]]
+ 00ae5a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5a9c ["INT_ADD", "register:40f0:8", ["const:ae5a9c:8", "const:4:8"]]
+ 00ae5a9c ["CALLIND", null, ["register:0:8"]]
- 00ae59d4 bytes 00013fd6
+ 00ae5a9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-162daaa84914cec3882ec9206e012aa6"></a>

### [`00ae59ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae59ec.md) → [`00ae5ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md) _ZN8firebase4util19cppthreaddispatcher14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5af4",
      "incomplete_value": true,
      "site": "00ae5af4",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5a2c",
      "incomplete_value": true,
      "site": "00ae5a2c",
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
            "const:2f0:8"
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
      "definition_site": "00ae5ad0",
      "incomplete_value": true,
      "site": "00ae5ad0",
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
      "definition_site": "00ae5a08",
      "incomplete_value": true,
      "site": "00ae5a08",
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
      "definition_site": "00ae5ad8",
      "incomplete_value": false,
      "site": "00ae5aec",
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
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5a10",
      "incomplete_value": false,
      "site": "00ae5a24",
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
            "const:fc4:8"
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
      "00ae5ac8",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ad8",
      "PARAM",
      [
        "storage",
        "002a9fc4",
        null,
        "string"
      ]
    ],
    [
      "00ae5af4",
      "WRITE",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5ac8",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ad8",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ],
    [
      "00ae5af4",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae59ec.md#insn-00ae5a24) · [`00ae5a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae59ec.md#insn-00ae5a2c) · [`00ae5a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae59ec.md#insn-00ae5a00)
- 新版 [`00ae5aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md#insn-00ae5aec) · [`00ae5af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md#insn-00ae5af4) · [`00ae5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md#insn-00ae5ac8)

~~~diff
- 00ae5a24 ["INT_ADD", "register:40f0:8", ["const:ae5a24:8", "const:4:8"]]
- 00ae5a24 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5aec ["INT_ADD", "register:40f0:8", ["const:ae5aec:8", "const:4:8"]]
+ 00ae5aec ["CALL", null, ["callee:00bde040:8"]]
- 00ae5a24 bytes 5be10394
+ 00ae5aec bytes 55e10394
- 00ae5a2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00ae5a2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5af4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
+ 00ae5af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5a2c bytes 807a01f9
+ 00ae5af4 bytes 80da01f9
- 00ae5a00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00ae5a00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5ac8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
+ 00ae5ac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5a00 bytes 817a41f9
+ 00ae5ac8 bytes 81da41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4689b8b31c7fd56f18dd015f95f2ab5"></a>

### [`00ae5a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a5c.md) → [`00ae5b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md) _ZN8firebase4util19cppthreaddispatcher11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae5b40",
      "incomplete_value": false,
      "site": "00ae5b44",
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
      "definition_site": "00ae5a78",
      "incomplete_value": false,
      "site": "00ae5a7c",
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
      "definition_site": "00ae5b50",
      "incomplete_value": true,
      "site": "00ae5b5c",
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
      "definition_site": "00ae5a88",
      "incomplete_value": true,
      "site": "00ae5a94",
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
      "00ae5b40",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae5b50",
      "DATA",
      [
        "storage",
        "010a0300",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5b40",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae5b50",
      "DATA",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a5c.md#insn-00ae5a7c) · [`00ae5a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a5c.md#insn-00ae5a78) · [`00ae5a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a5c.md#insn-00ae5a84)
- 新版 [`00ae5b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md#insn-00ae5b44) · [`00ae5b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md#insn-00ae5b40) · [`00ae5b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md#insn-00ae5b4c)

~~~diff
- 00ae5a7c ["INT_ADD", "register:40f0:8", ["const:ae5a7c:8", "const:4:8"]]
- 00ae5a7c ["CALL", null, ["callee:00bde130:8"]]
+ 00ae5b44 ["INT_ADD", "register:40f0:8", ["const:ae5b44:8", "const:4:8"]]
+ 00ae5b44 ["CALL", null, ["callee:00bde130:8"]]
- 00ae5a7c bytes 81e10394
+ 00ae5b44 bytes 7be10394
- 00ae5a78 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae5a78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5a78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5a78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5b40 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae5b40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5b40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5b40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5a78 bytes 001c1591
+ 00ae5b40 bytes 00501791
- 00ae5a84 ["COPY", "tmp:0:8", ["const:300:8"]]
- 00ae5a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5b4c ["COPY", "tmp:0:8", ["const:3c0:8"]]
+ 00ae5b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5a84 bytes 08010c91
+ 00ae5b4c bytes 08010f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-877681951c945332f7efc45b24384bff"></a>

### [`00ae5a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a98.md) → [`00ae5b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md) _ZN8firebase4util19cppthreaddispatcher13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5ba0",
      "incomplete_value": true,
      "site": "00ae5ba0",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ad8",
      "incomplete_value": true,
      "site": "00ae5ad8",
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
            "const:2f0:8"
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
      "definition_site": "00ae5b7c",
      "incomplete_value": true,
      "site": "00ae5b7c",
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
      "definition_site": "00ae5ab4",
      "incomplete_value": true,
      "site": "00ae5ab4",
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
      "definition_site": "00ae5b84",
      "incomplete_value": false,
      "site": "00ae5b98",
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
            "const:fca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5abc",
      "incomplete_value": false,
      "site": "00ae5ad0",
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
            "const:fc4:8"
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
      "00ae5b74",
      "READ",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5b84",
      "PARAM",
      [
        "storage",
        "002a9fc4",
        null,
        "string"
      ]
    ],
    [
      "00ae5ba0",
      "WRITE",
      [
        "storage",
        "010a02f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5b74",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5b84",
      "PARAM",
      [
        "storage",
        "002a9fca",
        null,
        "string"
      ]
    ],
    [
      "00ae5ba0",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a98.md#insn-00ae5ad0) · [`00ae5ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a98.md#insn-00ae5ad8) · [`00ae5aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5a98.md#insn-00ae5aac)
- 新版 [`00ae5b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md#insn-00ae5b98) · [`00ae5ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md#insn-00ae5ba0) · [`00ae5b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md#insn-00ae5b74)

~~~diff
- 00ae5ad0 ["INT_ADD", "register:40f0:8", ["const:ae5ad0:8", "const:4:8"]]
- 00ae5ad0 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5b98 ["INT_ADD", "register:40f0:8", ["const:ae5b98:8", "const:4:8"]]
+ 00ae5b98 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5ad0 bytes 30e10394
+ 00ae5b98 bytes 2ae10394
- 00ae5ad8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00ae5ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
+ 00ae5ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5ad8 bytes 807a01f9
+ 00ae5ba0 bytes 80da01f9
- 00ae5aac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00ae5aac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5b74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
+ 00ae5b74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5aac bytes 817a41f9
+ 00ae5b74 bytes 81da41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-185ad895705fa78f241044940128c431"></a>

### [`00ae5b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b44.md) → [`00ae5c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00ae5c38",
      "incomplete_value": true,
      "site": "00ae5c38",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5b70",
      "incomplete_value": true,
      "site": "00ae5b70",
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
            "const:318:8"
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
      "definition_site": "00ae5c20",
      "incomplete_value": true,
      "site": "00ae5c20",
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
      "definition_site": "00ae5b58",
      "incomplete_value": true,
      "site": "00ae5b58",
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
      "definition_site": "00ae5c2c",
      "incomplete_value": false,
      "site": "00ae5c30",
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
            "const:fae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5b64",
      "incomplete_value": false,
      "site": "00ae5b68",
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
            "const:fa8:8"
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
      "00ae5c1c",
      "READ",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5c2c",
      "PARAM",
      [
        "storage",
        "002aafa8",
        null,
        "string"
      ]
    ],
    [
      "00ae5c38",
      "WRITE",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5c1c",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5c2c",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ],
    [
      "00ae5c38",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b44.md#insn-00ae5b68) · [`00ae5b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b44.md#insn-00ae5b70) · [`00ae5b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b44.md#insn-00ae5b54)
- 新版 [`00ae5c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md#insn-00ae5c30) · [`00ae5c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md#insn-00ae5c38) · [`00ae5c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md#insn-00ae5c1c)

~~~diff
- 00ae5b68 ["INT_ADD", "register:40f0:8", ["const:ae5b68:8", "const:4:8"]]
- 00ae5b68 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5c30 ["INT_ADD", "register:40f0:8", ["const:ae5c30:8", "const:4:8"]]
+ 00ae5c30 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5b68 bytes 0ae10394
+ 00ae5c30 bytes 04e10394
- 00ae5b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00ae5b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00ae5c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5b70 bytes 608e01f9
+ 00ae5c38 bytes 60ee01f9
- 00ae5b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00ae5b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5c1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00ae5c1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5b54 bytes 688e41f9
+ 00ae5c1c bytes 68ee41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51e6a79b72cd612d3416a8a3a8aff5ea"></a>

### [`00ae5b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b84.md) → [`00ae5c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae5c78",
      "incomplete_value": true,
      "site": "00ae5c78",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5bb0",
      "incomplete_value": true,
      "site": "00ae5bb0",
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
            "const:318:8"
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
      "definition_site": "00ae5c60",
      "incomplete_value": true,
      "site": "00ae5c60",
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
      "definition_site": "00ae5b98",
      "incomplete_value": true,
      "site": "00ae5b98",
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
      "definition_site": "00ae5c68",
      "incomplete_value": false,
      "site": "00ae5c70",
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
            "const:fae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ba0",
      "incomplete_value": false,
      "site": "00ae5ba8",
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
            "const:fa8:8"
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
      "00ae5c5c",
      "READ",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5c68",
      "PARAM",
      [
        "storage",
        "002aafa8",
        null,
        "string"
      ]
    ],
    [
      "00ae5c78",
      "WRITE",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5c5c",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5c68",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ],
    [
      "00ae5c78",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b84.md#insn-00ae5ba8) · [`00ae5bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b84.md#insn-00ae5bb0) · [`00ae5b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5b84.md#insn-00ae5b94)
- 新版 [`00ae5c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md#insn-00ae5c70) · [`00ae5c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md#insn-00ae5c78) · [`00ae5c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md#insn-00ae5c5c)

~~~diff
- 00ae5ba8 ["INT_ADD", "register:40f0:8", ["const:ae5ba8:8", "const:4:8"]]
- 00ae5ba8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5c70 ["INT_ADD", "register:40f0:8", ["const:ae5c70:8", "const:4:8"]]
+ 00ae5c70 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5ba8 bytes fae00394
+ 00ae5c70 bytes f4e00394
- 00ae5bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00ae5bb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00ae5c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5bb0 bytes 608e01f9
+ 00ae5c78 bytes 60ee01f9
- 00ae5b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00ae5b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00ae5c5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5b94 bytes 688e41f9
+ 00ae5c5c bytes 68ee41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10bdb8961c205396768d34555ec3be70"></a>

### [`00ae5bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5bc4.md) → [`00ae5c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c8c.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "site": "00ae5bf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae5cbc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae5ca0",
      "incomplete_value": true,
      "site": "00ae5ca0",
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
      "definition_site": "00ae5bd8",
      "incomplete_value": true,
      "site": "00ae5bd8",
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
      "00ae5c9c",
      "READ",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ca0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae5bf8"
      ]
    ],
    [
      "unmatched:00ae5be4",
      "PARAM",
      [
        "storage",
        "002aafa8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae5c9c",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ca0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5cc0"
      ]
    ],
    [
      "00ae5cac",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5bc4.md#insn-00ae5bec) · [`00ae5bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5bc4.md#insn-00ae5bf4) · [`00ae5c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5bc4.md#insn-00ae5c04)

~~~diff
- 00ae5bec ["INT_ADD", "register:40f0:8", ["const:ae5bec:8", "const:4:8"]]
- 00ae5bec ["CALL", null, ["callee:00bde040:8"]]
- 00ae5bec bytes e9e00394
- 00ae5bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00ae5bf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5bf4 bytes 608e01f9
- 00ae5c04 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae5c04 ["RETURN", null, ["register:0:8"]]
- 00ae5c04 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116c13574caefe3e8aa0390e59d0e848"></a>

### [`00ae5c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c08.md) → [`00ae5cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 25.00%

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
      "site": "00ae5c38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae5d00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae5ce4",
      "incomplete_value": true,
      "site": "00ae5ce4",
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
      "definition_site": "00ae5c1c",
      "incomplete_value": true,
      "site": "00ae5c1c",
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
      "00ae5ce0",
      "READ",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5c24",
      "PARAM",
      [
        "storage",
        "002aafa8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5c38",
      "WRITE",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5ce0",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5cec",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ],
    [
      "00ae5d00",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c08.md#insn-00ae5c1c) · [`00ae5c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c08.md#insn-00ae5c30) · [`00ae5c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c08.md#insn-00ae5c38)
- 新版 [`00ae5ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md#insn-00ae5ce4) · [`00ae5cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md#insn-00ae5cf8)

~~~diff
- 00ae5c1c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5c1c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae5ce4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae5ce4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5c1c bytes 080100b5
+ 00ae5ce4 bytes 080100b5
- 00ae5c30 ["INT_ADD", "register:40f0:8", ["const:ae5c30:8", "const:4:8"]]
- 00ae5c30 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5cf8 ["INT_ADD", "register:40f0:8", ["const:ae5cf8:8", "const:4:8"]]
+ 00ae5cf8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5c30 bytes d8e00394
+ 00ae5cf8 bytes d2e00394
- 00ae5c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:318:8"]]
- 00ae5c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5c38 bytes 608e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d6267dd6fcb9246bf7f576dd2bf092f"></a>

### [`00ae5c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c58.md) → [`00ae5d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5d20.md) _ZN8firebase4util3log15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "site": "00ae5c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5c5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5c58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5c60",
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
      "00ae5d20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae5d24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae5d28",
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

- 旧版 [`00ae5c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c58.md#insn-00ae5c58) · [`00ae5c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c58.md#insn-00ae5c5c) · [`00ae5c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5c58.md#insn-00ae5c60)

~~~diff
- 00ae5c58 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae5c58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae5c58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5c58 bytes f50f1df8
- 00ae5c5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae5c5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae5c5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5c5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5c5c bytes f44f01a9
- 00ae5c60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5c60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5c60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae5c60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5c60 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce028f3a05ec049e525b21a3ed692948"></a>

### [`00ae5cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5cf4.md) → [`00ae5dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5dbc.md) _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.50% / 新版 72.50%

CFGの説明率　旧版 30.00% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5cf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5cf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5cf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5cfc",
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
      "00ae5dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae5dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae5dc4",
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

- 旧版 [`00ae5cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5cf4.md#insn-00ae5cf4) · [`00ae5cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5cf4.md#insn-00ae5cf8) · [`00ae5cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5cf4.md#insn-00ae5cfc)

~~~diff
- 00ae5cf4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae5cf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae5cf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5cf4 bytes f50f1df8
- 00ae5cf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae5cf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae5cf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5cf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5cf8 bytes f44f01a9
- 00ae5cfc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5cfc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5cfc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae5cfc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5cfc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2132659f07ba853e236dd567810b4fc8"></a>

### [`00ae5d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5d94.md) → [`00ae5e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5e5c.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00ae5dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae5e9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5db0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5da8",
      "READ",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5db0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5ea0"
      ]
    ],
    [
      "unmatched:00ae5db8",
      "PARAM",
      [
        "storage",
        "002aafa8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae5e70",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5e78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5ea0"
      ]
    ],
    [
      "00ae5e80",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5d94.md#insn-00ae5db0) · [`00ae5dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5d94.md#insn-00ae5dcc) · [`00ae5dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5d94.md#insn-00ae5dd4)
- 新版 [`00ae5e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5e5c.md#insn-00ae5e94)

~~~diff
- 00ae5db0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5db0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5db0 bytes 410100b5
- 00ae5dcc ["INT_ADD", "register:40f0:8", ["const:ae5dcc:8", "const:4:8"]]
- 00ae5dcc ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5e94 ["INT_ADD", "register:40f0:8", ["const:ae5e94:8", "const:4:8"]]
+ 00ae5e94 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5dcc bytes 71e00394
+ 00ae5e94 bytes 6be00394
- 00ae5dd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:318:8"]]
- 00ae5dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5dd4 bytes 808e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8ceca97c94ab943aba293313f1c9004"></a>

### [`00ae5e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e40.md) → [`00ae5f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f08.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae5e80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae5f48"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5e5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5e54",
      "READ",
      [
        "storage",
        "010a0318",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5e5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5f4c"
      ]
    ],
    [
      "unmatched:00ae5e64",
      "PARAM",
      [
        "storage",
        "002aafa8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae5f1c",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae5f4c"
      ]
    ],
    [
      "00ae5f2c",
      "PARAM",
      [
        "storage",
        "002aafae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e40.md#insn-00ae5e5c) · [`00ae5e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e40.md#insn-00ae5e78) · [`00ae5e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5e40.md#insn-00ae5e80)
- 新版 [`00ae5f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f08.md#insn-00ae5f40)

~~~diff
- 00ae5e5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae5e5c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5e5c bytes 410100b5
- 00ae5e78 ["INT_ADD", "register:40f0:8", ["const:ae5e78:8", "const:4:8"]]
- 00ae5e78 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae5f40 ["INT_ADD", "register:40f0:8", ["const:ae5f40:8", "const:4:8"]]
+ 00ae5f40 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5e78 bytes 46e00394
+ 00ae5f40 bytes 40e00394
- 00ae5e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:318:8"]]
- 00ae5e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5e80 bytes 808e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c10d563dc946727e53c9e50409f3ba18"></a>

### [`00ae5eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eec.md) → [`00ae5fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5fb4.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "site": "00ae5eec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae5ef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae5eec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae5ef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae5fc4",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5fb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae5fb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae5fc4",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5eec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eec.md#insn-00ae5eec) · [`00ae5ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eec.md#insn-00ae5ef0) · [`00ae5f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5eec.md#insn-00ae5f00)
- 新版 [`00ae5fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5fb4.md#insn-00ae5fc8)

~~~diff
- 00ae5eec ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae5eec ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae5eec ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae5eec bytes f30f1ef8
- 00ae5ef0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae5ef0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae5ef0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae5ef0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae5ef0 bytes fd7b01a9
- 00ae5f00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5f00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae5fc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae5fc8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae5f00 bytes e80000b5
+ 00ae5fc8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3d1a815c5ec6f27f683378a7c621720"></a>

### [`00ae5f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f2c.md) → [`00ae5ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ff4.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae5f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6020"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae6008",
      "incomplete_value": true,
      "site": "00ae6008",
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
      "definition_site": "00ae5f40",
      "incomplete_value": true,
      "site": "00ae5f40",
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
      "00ae6004",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5f48",
      "PARAM",
      [
        "storage",
        "0029ed92",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5f50",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae6004",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6010",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae6018",
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

- 旧版 [`00ae5f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f2c.md#insn-00ae5f40) · [`00ae5f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f2c.md#insn-00ae5f50) · [`00ae5f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f2c.md#insn-00ae5f58)
- 新版 [`00ae6008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ff4.md#insn-00ae6008)

~~~diff
- 00ae5f40 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5f40 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae6008 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6008 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5f40 bytes e80000b5
+ 00ae6008 bytes e80000b5
- 00ae5f50 ["INT_ADD", "register:40f0:8", ["const:ae5f50:8", "const:4:8"]]
- 00ae5f50 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5f50 bytes 10e00394
- 00ae5f58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00ae5f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5f58 bytes 609e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dafe62f344af29cef08c8eadf7ed696f"></a>

### [`00ae5f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f6c.md) → [`00ae6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6034.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae5f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6064"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae6048",
      "incomplete_value": true,
      "site": "00ae6048",
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
      "definition_site": "00ae5f80",
      "incomplete_value": true,
      "site": "00ae5f80",
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
      "00ae6044",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5f8c",
      "PARAM",
      [
        "storage",
        "0029ed92",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5f94",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae6044",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6054",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae605c",
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

- 旧版 [`00ae5f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f6c.md#insn-00ae5f80) · [`00ae5f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f6c.md#insn-00ae5f94) · [`00ae5f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5f6c.md#insn-00ae5f9c)
- 新版 [`00ae6048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6034.md#insn-00ae6048)

~~~diff
- 00ae5f80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5f80 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae6048 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6048 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5f80 bytes 080100b5
+ 00ae6048 bytes 080100b5
- 00ae5f94 ["INT_ADD", "register:40f0:8", ["const:ae5f94:8", "const:4:8"]]
- 00ae5f94 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5f94 bytes ffdf0394
- 00ae5f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00ae5f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5f9c bytes 609e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0758c5a013d7807a4a4e515adb6fb244"></a>

### [`00ae5fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5fb0.md) → [`00ae6078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00ae5fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae60a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae608c",
      "incomplete_value": true,
      "site": "00ae608c",
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
      "definition_site": "00ae5fc4",
      "incomplete_value": true,
      "site": "00ae5fc4",
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
      "00ae6088",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae5fcc",
      "PARAM",
      [
        "storage",
        "0029ed92",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae5fe0",
      "WRITE",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6088",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6094",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae60a8",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5fb0.md#insn-00ae5fc4) · [`00ae5fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5fb0.md#insn-00ae5fd8) · [`00ae5fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae5/00ae5fb0.md#insn-00ae5fe0)
- 新版 [`00ae608c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md#insn-00ae608c) · [`00ae60a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md#insn-00ae60a0)

~~~diff
- 00ae5fc4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae5fc4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae608c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae608c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae5fc4 bytes 080100b5
+ 00ae608c bytes 080100b5
- 00ae5fd8 ["INT_ADD", "register:40f0:8", ["const:ae5fd8:8", "const:4:8"]]
- 00ae5fd8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae60a0 ["INT_ADD", "register:40f0:8", ["const:ae60a0:8", "const:4:8"]]
+ 00ae60a0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae5fd8 bytes eedf0394
+ 00ae60a0 bytes e8df0394
- 00ae5fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:338:8"]]
- 00ae5fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5fe0 bytes 609e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bde7c28c741c9be155cd292021641db"></a>

### [`00ae6000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6000.md) → [`00ae60c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae60c8.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae6150",
      "incomplete_value": true,
      "site": "00ae6150",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6088",
      "incomplete_value": true,
      "site": "00ae6088",
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
            "const:340:8"
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
      "site": "00ae605c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae6124"
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
      "00ae60dc",
      "READ",
      [
        "storage",
        "010a0340",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae6034",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae605c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6148"
      ]
    ]
  ],
  "added": [
    [
      "00ae60dc",
      "READ",
      [
        "storage",
        "010a0400",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae60fc",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6148"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6000.md#insn-00ae6040) · [`00ae6054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6000.md#insn-00ae6054) · [`00ae605c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6000.md#insn-00ae605c)

~~~diff
- 00ae6040 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6040 ["INT_ADD", "register:40f0:8", ["const:ae6040:8", "const:4:8"]]
- 00ae6040 ["CALLIND", null, ["register:0:8"]]
- 00ae6040 bytes 00013fd6
- 00ae6054 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6054 ["INT_ADD", "register:40f0:8", ["const:ae6054:8", "const:4:8"]]
- 00ae6054 ["CALLIND", null, ["register:0:8"]]
- 00ae6054 bytes 00013fd6
- 00ae605c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00ae605c bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c084014e2e1284867bd52f4fa0c45612"></a>

### [`00ae613c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae613c.md) → [`00ae6204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6204.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00ae617c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6244"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6158"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6150",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6158",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6248"
      ]
    ],
    [
      "unmatched:00ae6160",
      "PARAM",
      [
        "storage",
        "0029ed92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae6218",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6248"
      ]
    ],
    [
      "00ae6228",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae613c.md#insn-00ae6158) · [`00ae6174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae613c.md#insn-00ae6174) · [`00ae617c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae613c.md#insn-00ae617c)
- 新版 [`00ae623c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6204.md#insn-00ae623c)

~~~diff
- 00ae6158 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6158 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6158 bytes 410100b5
- 00ae6174 ["INT_ADD", "register:40f0:8", ["const:ae6174:8", "const:4:8"]]
- 00ae6174 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae623c ["INT_ADD", "register:40f0:8", ["const:ae623c:8", "const:4:8"]]
+ 00ae623c ["CALL", null, ["callee:00bde040:8"]]
- 00ae6174 bytes 87df0394
+ 00ae623c bytes 81df0394
- 00ae617c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00ae617c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae617c bytes 809e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2b5c4b0d1a40688c50c804cc62dd45f"></a>

### [`00ae61ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61ac.md) → [`00ae6274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md) _ZN8firebase4util10uribuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae6290",
      "incomplete_value": false,
      "site": "00ae6294",
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
      "definition_site": "00ae61c8",
      "incomplete_value": false,
      "site": "00ae61cc",
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
      "definition_site": "00ae62a0",
      "incomplete_value": true,
      "site": "00ae62ac",
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
      "definition_site": "00ae61d8",
      "incomplete_value": true,
      "site": "00ae61e4",
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
      "00ae6290",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae62a0",
      "DATA",
      [
        "storage",
        "010a0348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6290",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae62a0",
      "DATA",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae61cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61ac.md#insn-00ae61cc) · [`00ae61c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61ac.md#insn-00ae61c8) · [`00ae61d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61ac.md#insn-00ae61d4)
- 新版 [`00ae6294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md#insn-00ae6294) · [`00ae6290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md#insn-00ae6290) · [`00ae629c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md#insn-00ae629c)

~~~diff
- 00ae61cc ["INT_ADD", "register:40f0:8", ["const:ae61cc:8", "const:4:8"]]
- 00ae61cc ["CALL", null, ["callee:00bde130:8"]]
+ 00ae6294 ["INT_ADD", "register:40f0:8", ["const:ae6294:8", "const:4:8"]]
+ 00ae6294 ["CALL", null, ["callee:00bde130:8"]]
- 00ae61cc bytes addf0394
+ 00ae6294 bytes a7df0394
- 00ae61c8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae61c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae61c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae61c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6290 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00ae6290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae61c8 bytes 001c1591
+ 00ae6290 bytes 00501791
- 00ae61d4 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00ae61d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae61d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae61d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae629c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 00ae629c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae629c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae629c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae61d4 bytes 08210d91
+ 00ae629c bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f129bbd20dced91a8111ca552265a0a6"></a>

### [`00ae61e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61e8.md) → [`00ae62b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae62b0.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00ae6228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae62f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6204"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae61fc",
      "READ",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6204",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae62f4"
      ]
    ],
    [
      "unmatched:00ae620c",
      "PARAM",
      [
        "storage",
        "0029ed92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae62c4",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae62cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae62f4"
      ]
    ],
    [
      "00ae62d4",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61e8.md#insn-00ae6204) · [`00ae6220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61e8.md#insn-00ae6220) · [`00ae6228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae61e8.md#insn-00ae6228)
- 新版 [`00ae62e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae62b0.md#insn-00ae62e8)

~~~diff
- 00ae6204 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6204 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6204 bytes 410100b5
- 00ae6220 ["INT_ADD", "register:40f0:8", ["const:ae6220:8", "const:4:8"]]
- 00ae6220 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae62e8 ["INT_ADD", "register:40f0:8", ["const:ae62e8:8", "const:4:8"]]
+ 00ae62e8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6220 bytes 5cdf0394
+ 00ae62e8 bytes 56df0394
- 00ae6228 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:338:8"]]
- 00ae6228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6228 bytes 809e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c3affee39154e4fe61242853a66d10"></a>

### [`00ae6294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6294.md) → [`00ae635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae635c.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00ae62c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6388"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae6370",
      "incomplete_value": true,
      "site": "00ae6370",
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
      "definition_site": "00ae62a8",
      "incomplete_value": true,
      "site": "00ae62a8",
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
      "00ae636c",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae62b4",
      "PARAM",
      [
        "storage",
        "002ac15f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae62b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae636c",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae637c",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      "00ae6380",
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

- 旧版 [`00ae62a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6294.md#insn-00ae62a8) · [`00ae62b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6294.md#insn-00ae62b8) · [`00ae62c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6294.md#insn-00ae62c0)
- 新版 [`00ae6370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae635c.md#insn-00ae6370)

~~~diff
- 00ae62a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae62a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00ae6370 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6370 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae62a8 bytes e80000b5
+ 00ae6370 bytes e80000b5
- 00ae62b8 ["INT_ADD", "register:40f0:8", ["const:ae62b8:8", "const:4:8"]]
- 00ae62b8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae62b8 bytes 36df0394
- 00ae62c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae62c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae62c0 bytes 60b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c1f4dfd810c62d65b51596538161dbf"></a>

### [`00ae62d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae62d4.md) → [`00ae639c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae639c.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae6300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae63c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae63b0",
      "incomplete_value": true,
      "site": "00ae63b0",
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
      "definition_site": "00ae62e8",
      "incomplete_value": true,
      "site": "00ae62e8",
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
      "00ae63ac",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae63b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae6304"
      ]
    ],
    [
      "unmatched:00ae62f0",
      "PARAM",
      [
        "storage",
        "002ac15f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae63ac",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae63b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae63cc"
      ]
    ],
    [
      "00ae63b8",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae62e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae62d4.md#insn-00ae62e8) · [`00ae62f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae62d4.md#insn-00ae62f8) · [`00ae6300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae62d4.md#insn-00ae6300)
- 新版 [`00ae63b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae639c.md#insn-00ae63b0)

~~~diff
- 00ae62e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae62e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae63b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae63b0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae62e8 bytes e80000b5
+ 00ae63b0 bytes e80000b5
- 00ae62f8 ["INT_ADD", "register:40f0:8", ["const:ae62f8:8", "const:4:8"]]
- 00ae62f8 ["CALL", null, ["callee:00bde040:8"]]
- 00ae62f8 bytes 26df0394
- 00ae6300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae6300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6300 bytes 60b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61aac49bc42a0ee54a20e4197d0afd66"></a>

### [`00ae6314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6314.md) → [`00ae63dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae63dc.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae6314"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6318"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6318"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6314",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6318",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae63ec",
      "READ",
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
      "00ae63dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae63e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae63ec",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6314.md#insn-00ae6314) · [`00ae6318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6314.md#insn-00ae6318) · [`00ae6328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6314.md#insn-00ae6328)
- 新版 [`00ae63f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae63dc.md#insn-00ae63f0)

~~~diff
- 00ae6314 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae6314 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6314 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6314 bytes f30f1ef8
- 00ae6318 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6318 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6318 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6318 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6318 bytes fd7b01a9
- 00ae6328 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6328 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00ae63f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae63f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae6328 bytes 080100b5
+ 00ae63f0 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da23b547dee895c6e49c109a6ad39614"></a>

### [`00ae6358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6358.md) → [`00ae6420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00ae6388"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6450"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00ae636c",
      "incomplete_value": true,
      "site": "00ae636c",
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
      "00ae6430",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6374",
      "PARAM",
      [
        "storage",
        "002ac15f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae6388",
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
      "00ae6430",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae643c",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ],
    [
      "00ae6450",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6358.md#insn-00ae6380) · [`00ae6388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6358.md#insn-00ae6388)
- 新版 [`00ae6448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md#insn-00ae6448) · [`00ae6450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md#insn-00ae6450)

~~~diff
- 00ae6380 ["INT_ADD", "register:40f0:8", ["const:ae6380:8", "const:4:8"]]
- 00ae6380 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6448 ["INT_ADD", "register:40f0:8", ["const:ae6448:8", "const:4:8"]]
+ 00ae6448 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6380 bytes 04df0394
+ 00ae6448 bytes fede0394
- 00ae6388 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
- 00ae6388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6388 bytes 60b601f9
+ 00ae6450 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
+ 00ae6450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6450 bytes 601602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27ba8469983e123906f7e7f74832a685"></a>

### [`00ae63a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae63a8.md) → [`00ae6470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6470.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 11.11% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae63a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae63ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae63ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae63a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae63ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae63b0",
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
      "00ae6470",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ae6474",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6478",
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

- 旧版 [`00ae63a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae63a8.md#insn-00ae63a8) · [`00ae63ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae63a8.md#insn-00ae63ac) · [`00ae63b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae63a8.md#insn-00ae63b0)

~~~diff
- 00ae63a8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae63a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae63a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae63a8 bytes f50f1df8
- 00ae63ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae63ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae63ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae63ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae63ac bytes f44f01a9
- 00ae63b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae63b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae63b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae63b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae63b0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8633151a37c14ddc23e21a8fcbc1123f"></a>

### [`00ae64e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae64e4.md) → [`00ae65ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae65ac.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00ae6524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae65ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6500"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae64f8",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6500",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae65f0"
      ]
    ],
    [
      "unmatched:00ae6508",
      "PARAM",
      [
        "storage",
        "002ac15f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae65c0",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae65c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae65f0"
      ]
    ],
    [
      "00ae65d0",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae64e4.md#insn-00ae6500) · [`00ae651c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae64e4.md#insn-00ae651c) · [`00ae6524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae64e4.md#insn-00ae6524)
- 新版 [`00ae65e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae65ac.md#insn-00ae65e4)

~~~diff
- 00ae6500 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae6500 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6500 bytes 410100b5
- 00ae651c ["INT_ADD", "register:40f0:8", ["const:ae651c:8", "const:4:8"]]
- 00ae651c ["CALL", null, ["callee:00bde040:8"]]
+ 00ae65e4 ["INT_ADD", "register:40f0:8", ["const:ae65e4:8", "const:4:8"]]
+ 00ae65e4 ["CALL", null, ["callee:00bde040:8"]]
- 00ae651c bytes 9dde0394
+ 00ae65e4 bytes 97de0394
- 00ae6524 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
- 00ae6524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6524 bytes 80b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abd63fdcf68942021ffcdb8b67462fc6"></a>

### [`00ae6590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6590.md) → [`00ae6658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6658.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00ae65d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6698"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae65ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae65a4",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae65ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae669c"
      ]
    ],
    [
      "unmatched:00ae65b4",
      "PARAM",
      [
        "storage",
        "002ac15f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae666c",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae669c"
      ]
    ],
    [
      "00ae667c",
      "PARAM",
      [
        "storage",
        "002ac156",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae65ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6590.md#insn-00ae65ac) · [`00ae65c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6590.md#insn-00ae65c8) · [`00ae65d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6590.md#insn-00ae65d0)
- 新版 [`00ae6690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6658.md#insn-00ae6690)

~~~diff
- 00ae65ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae65ac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae65ac bytes 410100b5
- 00ae65c8 ["INT_ADD", "register:40f0:8", ["const:ae65c8:8", "const:4:8"]]
- 00ae65c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6690 ["INT_ADD", "register:40f0:8", ["const:ae6690:8", "const:4:8"]]
+ 00ae6690 ["CALL", null, ["callee:00bde040:8"]]
- 00ae65c8 bytes 72de0394
+ 00ae6690 bytes 6cde0394
- 00ae65d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
- 00ae65d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae65d0 bytes 80b601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016afe6adbed466f320bf34d8358b634"></a>

### [`00ae663c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae663c.md) → [`00ae6704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6704.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae6730",
      "incomplete_value": true,
      "site": "00ae6730",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6668",
      "incomplete_value": true,
      "site": "00ae6668",
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
            "const:390:8"
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
      "unmatched:00ae6640",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae664c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6734"
      ]
    ]
  ],
  "added": [
    [
      "00ae6708",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6714",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6718",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae6734"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae663c.md#insn-00ae6640) · [`00ae6650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae663c.md#insn-00ae6650) · [`00ae6660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae663c.md#insn-00ae6660)
- 新版 [`00ae6728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6704.md#insn-00ae6728)

~~~diff
- 00ae6640 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6640 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6640 bytes fd7b01a9
- 00ae6650 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae6650 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae6650 bytes e80000b5
- 00ae6660 ["INT_ADD", "register:40f0:8", ["const:ae6660:8", "const:4:8"]]
- 00ae6660 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6728 ["INT_ADD", "register:40f0:8", ["const:ae6728:8", "const:4:8"]]
+ 00ae6728 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6660 bytes 4cde0394
+ 00ae6728 bytes 46de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-241d0552353c28fc9ec6ded24922cb0f"></a>

### [`00ae667c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae667c.md) → [`00ae6744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6744.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00ae66a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ae6770"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae6758",
      "incomplete_value": true,
      "site": "00ae6758",
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
      "definition_site": "00ae6690",
      "incomplete_value": true,
      "site": "00ae6690",
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
      "00ae6754",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae6698",
      "PARAM",
      [
        "storage",
        "0029fedf",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae66a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00ae6754",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6760",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae6768",
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

- 旧版 [`00ae66a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae667c.md#insn-00ae66a0) · [`00ae66a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae667c.md#insn-00ae66a8)
- 新版 [`00ae6768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6744.md#insn-00ae6768)

~~~diff
- 00ae66a0 ["INT_ADD", "register:40f0:8", ["const:ae66a0:8", "const:4:8"]]
- 00ae66a0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae66a0 bytes 3cde0394
- 00ae66a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
- 00ae66a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae66a8 bytes 60ca01f9
+ 00ae6768 ["INT_ADD", "register:40f0:8", ["const:ae6768:8", "const:4:8"]]
+ 00ae6768 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae6768 bytes 36de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e21cc328bf232b554ae9c014211c20ad"></a>

### [`00ae66bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae66bc.md) → [`00ae6784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6784.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 29.41% / 新版 29.41%

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
      "site": "00ae66bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae66c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae66c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae66bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae66c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6794",
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
      "00ae6784",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae6788",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae6794",
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

- 旧版 [`00ae66bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae66bc.md#insn-00ae66bc) · [`00ae66c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae66bc.md#insn-00ae66c0) · [`00ae66d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae66bc.md#insn-00ae66d0)
- 新版 [`00ae6798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6784.md#insn-00ae6798)

~~~diff
- 00ae66bc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae66bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae66bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae66bc bytes f30f1ef8
- 00ae66c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae66c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae66c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae66c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae66c0 bytes fd7b01a9
- 00ae66d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae66d0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00ae6798 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ae6798 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae66d0 bytes 080100b5
+ 00ae6798 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-869699b43b8dc5d78cb3514bac9abcd6"></a>

### [`00ae6700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6700.md) → [`00ae67c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae67c8.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00ae6700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6704"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae6704"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae6700",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae6704",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae67d8",
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
      "00ae67c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ae67cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ae67d8",
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

- 旧版 [`00ae6700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6700.md#insn-00ae6700) · [`00ae6704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6700.md#insn-00ae6704) · [`00ae6728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae6/00ae6700.md#insn-00ae6728)
- 新版 [`00ae67f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae67c8.md#insn-00ae67f0)

~~~diff
- 00ae6700 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae6700 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae6700 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae6700 bytes f30f1ef8
- 00ae6704 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae6704 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae6704 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae6704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae6704 bytes fd7b01a9
- 00ae6728 ["INT_ADD", "register:40f0:8", ["const:ae6728:8", "const:4:8"]]
- 00ae6728 ["CALL", null, ["callee:00bde040:8"]]
+ 00ae67f0 ["INT_ADD", "register:40f0:8", ["const:ae67f0:8", "const:4:8"]]
+ 00ae67f0 ["CALL", null, ["callee:00bde040:8"]]
- 00ae6728 bytes 1ade0394
+ 00ae67f0 bytes 14de0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

