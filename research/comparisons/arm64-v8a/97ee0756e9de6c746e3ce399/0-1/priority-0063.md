# v15.7.2 → v15.7.3 · 最優先の変更候補 (63)

[一覧の目次](README.md)

<a id="compare-4da65e6b4e088a4ae13bc418526a809e"></a>

### [`00afc428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc428.md) → [`00afc4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc4f0.md) _INIT_272

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.33% / 新版 53.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc428"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc42c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc42c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc428",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc42c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc454",
      "WRITE",
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
      "00afc4f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afc4f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afc51c",
      "WRITE",
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

- 旧版 [`00afc428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc428.md#insn-00afc428) · [`00afc42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc428.md#insn-00afc42c) · [`00afc444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc428.md#insn-00afc444)
- 新版 [`00afc50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc4f0.md#insn-00afc50c)

~~~diff
- 00afc428 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00afc428 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afc428 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc428 bytes f30f1ef8
- 00afc42c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc42c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc42c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc42c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc42c bytes fd7b01a9
- 00afc444 ["INT_ADD", "register:40f0:8", ["const:afc444:8", "const:4:8"]]
- 00afc444 ["CALL", null, ["callee:00bdddd0:8"]]
+ 00afc50c ["INT_ADD", "register:40f0:8", ["const:afc50c:8", "const:4:8"]]
+ 00afc50c ["CALL", null, ["callee:00bdddd0:8"]]
- 00afc444 bytes 37860394
+ 00afc50c bytes 31860394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aa439e9cb68f1f873c00f33114385bc"></a>

### [`00afc464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc464.md) → [`00afc52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc52c.md) _ZN8firebase15CleanupNotifierC1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcc0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 1件 [`00bddd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd70.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afc57c",
      "incomplete_value": true,
      "site": "00afc57c",
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
      "definition_site": "00afc4b4",
      "incomplete_value": true,
      "site": "00afc4b4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afc568",
      "incomplete_value": true,
      "site": "00afc56c",
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
      "definition_site": "00afc4a0",
      "incomplete_value": true,
      "site": "00afc4a4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00afc4b4"
      ],
      [
        "FALL_THROUGH",
        "00afc57c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00afc57c",
      "incomplete_value": true,
      "site": "00afc58c",
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
      "definition_site": "00afc4b4",
      "incomplete_value": true,
      "site": "00afc4c4",
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
      "00afc560",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00afc564",
      "READ",
      [
        "storage",
        "010a0c48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afc574",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afc560",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afc564",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afc574",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc464.md#insn-00afc4a4) · [`00afc4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc464.md#insn-00afc4b4) · [`00afc478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc464.md#insn-00afc478)
- 新版 [`00afc56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc52c.md#insn-00afc56c) · [`00afc57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc52c.md#insn-00afc57c) · [`00afc540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc52c.md#insn-00afc540)

~~~diff
- 00afc4a4 ["INT_ADD", "register:40f0:8", ["const:afc4a4:8", "const:4:8"]]
- 00afc4a4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afc56c ["INT_ADD", "register:40f0:8", ["const:afc56c:8", "const:4:8"]]
+ 00afc56c ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc4a4 bytes 9f850394
+ 00afc56c bytes 99850394
- 00afc4b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00afc4b4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00afc57c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00afc57c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00afc4b4 bytes 080100b5
+ 00afc57c bytes 080100b5
- 00afc478 ["INT_ADD", "register:40f0:8", ["const:afc478:8", "const:4:8"]]
- 00afc478 ["CALL", null, ["callee:00bdddd0:8"]]
+ 00afc540 ["INT_ADD", "register:40f0:8", ["const:afc540:8", "const:4:8"]]
+ 00afc540 ["CALL", null, ["callee:00bdddd0:8"]]
- 00afc478 bytes 2a860394
+ 00afc540 bytes 24860394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-980b133a11c4546c0895bac50922b1d1"></a>

### [`00afc4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc4e4.md) → [`00afc5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc5ac.md) _ZN8firebase15CleanupNotifierD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddcd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcd0.md) · 呼出先 8件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00bddd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd80.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 12.50% / 新版 10.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc534"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afc638",
      "incomplete_value": true,
      "site": "00afc638",
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
      "definition_site": "00afc570",
      "incomplete_value": true,
      "site": "00afc570",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc5a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc534",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc5dc"
      ]
    ],
    [
      "00afc61c",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00afc620",
      "READ",
      [
        "storage",
        "010a0c48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afc5fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afc5dc"
      ]
    ],
    [
      "00afc61c",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afc620",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc4e4.md#insn-00afc534) · [`00afc560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc4e4.md#insn-00afc560) · [`00afc570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc4e4.md#insn-00afc570)
- 新版 [`00afc628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc5ac.md#insn-00afc628) · [`00afc638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc5ac.md#insn-00afc638)

~~~diff
- 00afc534 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afc534 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00afc534 bytes 01ffff54
- 00afc560 ["INT_ADD", "register:40f0:8", ["const:afc560:8", "const:4:8"]]
- 00afc560 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afc628 ["INT_ADD", "register:40f0:8", ["const:afc628:8", "const:4:8"]]
+ 00afc628 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc560 bytes 70850394
+ 00afc628 bytes 6a850394
- 00afc570 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00afc570 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00afc638 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00afc638 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00afc570 bytes 350100b4
+ 00afc638 bytes 350100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e4a5f06e4fafe685538ecb4642f91f2"></a>

### [`00afc5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc5cc.md) → [`00afc694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc694.md) _ZN8firebase15CleanupNotifier10CleanupAllEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde810.md) · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00bde8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8c0.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc5cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc5d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc5d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc5cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc5d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc5d4",
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
      "00afc694",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afc698",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afc69c",
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

- 旧版 [`00afc5cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc5cc.md#insn-00afc5cc) · [`00afc5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc5cc.md#insn-00afc5d0) · [`00afc5d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc5cc.md#insn-00afc5d4)

~~~diff
- 00afc5cc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00afc5cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afc5cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc5cc bytes f50f1df8
- 00afc5d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc5d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc5d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc5d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc5d0 bytes f44f01a9
- 00afc5d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc5d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc5d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afc5d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc5d4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71d98b55eadfd41060ebb850afe0a673"></a>

### [`00afc63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc63c.md) → [`00afc704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc704.md) _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdebf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdebf0.md) · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bdebe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdebe0.md)
- 新版 呼出元 1件 [`00bdeca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeca0.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdec90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 36.84% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc63c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc63c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc63c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc640",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc644",
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
      "00afc704",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00afc708",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afc70c",
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

- 旧版 [`00afc63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc63c.md#insn-00afc63c) · [`00afc640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc63c.md#insn-00afc640) · [`00afc644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc63c.md#insn-00afc644)

~~~diff
- 00afc63c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afc63c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afc63c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00afc63c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc63c bytes f85fbca9
- 00afc640 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afc640 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afc640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afc640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc640 bytes f65701a9
- 00afc644 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc644 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc644 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afc644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc644 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f4c6e72de19dade38e64c8a0cfc28cb"></a>

### [`00afc910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc910.md) → [`00afc9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc9d8.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerEPS0_Pv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bdebe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdebe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdec90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec90.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afca0c",
      "incomplete_value": true,
      "site": "00afca0c",
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
      "definition_site": "00afc944",
      "incomplete_value": true,
      "site": "00afc944",
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
      "site": "00afc958"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00afca20"
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
      "00afc9e8",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00afc9f0",
      "READ",
      [
        "storage",
        "010a0c48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afca00",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afc9e8",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afc9f0",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afca00",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc910.md#insn-00afc930) · [`00afc944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc910.md#insn-00afc944) · [`00afc958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc910.md#insn-00afc958)
- 新版 [`00afc9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc9d8.md#insn-00afc9f8) · [`00afca0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc9d8.md#insn-00afca0c)

~~~diff
- 00afc930 ["INT_ADD", "register:40f0:8", ["const:afc930:8", "const:4:8"]]
- 00afc930 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afc9f8 ["INT_ADD", "register:40f0:8", ["const:afc9f8:8", "const:4:8"]]
+ 00afc9f8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc930 bytes 7c840394
+ 00afc9f8 bytes 76840394
- 00afc944 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00afc944 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00afca0c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00afca0c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00afc944 bytes c90100b4
+ 00afca0c bytes c90100b4
- 00afc958 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00afc958 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00afc958 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afc958 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afc958 bytes 0030899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e30827fb371f781f6d36717182f14d"></a>

### [`00afc98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc98c.md) → [`00afca54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afca54.md) _ZN8firebase15CleanupNotifier13RegisterOwnerEPS0_Pv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde820.md) · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bde8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8d0.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 53.57% / 新版 53.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 6件, `unresolved_branch_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afca74",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00afca80",
      "READ",
      [
        "storage",
        "010a0c48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afca90",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afca74",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afca80",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afca90",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc9ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc98c.md#insn-00afc9ac) · [`00afc9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc98c.md#insn-00afc9c0) · [`00afc9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc98c.md#insn-00afc9d8)
- 新版 [`00afca74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afca54.md#insn-00afca74) · [`00afca88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afca54.md#insn-00afca88)

~~~diff
- 00afc9ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00afc9ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afca74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:948:8"]]
+ 00afca74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc9ac bytes 084d44f9
+ 00afca74 bytes 08a544f9
- 00afc9c0 ["INT_ADD", "register:40f0:8", ["const:afc9c0:8", "const:4:8"]]
- 00afc9c0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afca88 ["INT_ADD", "register:40f0:8", ["const:afca88:8", "const:4:8"]]
+ 00afca88 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afc9c0 bytes 58840394
+ 00afca88 bytes 52840394
- 00afc9d8 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00afc9d8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00afc9d8 bytes 380400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8a78b09b0d5070c53a69bdc58475879"></a>

### [`00afcb88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcb88.md) → [`00afcc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcc50.md) _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nod

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdebe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdebe0.md) · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde650.md)
- 新版 呼出元 1件 [`00bdec90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec90.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 81.94% / 新版 81.94%

CFGの説明率　旧版 46.43% / 新版 44.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcbe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcc00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcc0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afcc64",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00afcc6c",
      "READ",
      [
        "storage",
        "010a0c48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afcc80",
      "READ",
      [
        "storage",
        "00c1b890",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afcc64",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afcc6c",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afcc80",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afcbac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcb88.md#insn-00afcbac) · [`00afcbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcb88.md#insn-00afcbe8) · [`00afcc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcb88.md#insn-00afcc00)
- 新版 [`00afcc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcc50.md#insn-00afcc74)

~~~diff
- 00afcbac ["INT_ADD", "register:40f0:8", ["const:afcbac:8", "const:4:8"]]
- 00afcbac ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afcc74 ["INT_ADD", "register:40f0:8", ["const:afcc74:8", "const:4:8"]]
+ 00afcc74 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afcbac bytes dd830394
+ 00afcc74 bytes d7830394
- 00afcbe8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00afcbe8 bytes e0000054
- 00afcc00 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00afcc00 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00afcc00 bytes 61ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00170565906027dac0bdf9bfbf254e6f"></a>

### [`00afcca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcca8.md) → [`00afcd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md) _ZN8firebase15CleanupNotifier11FindByOwnerEPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc90.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 53.33% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afccac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afcca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afccac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afcd80",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afcd70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afcd74",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afcd80",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afcca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcca8.md#insn-00afcca8) · [`00afccac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcca8.md#insn-00afccac) · [`00afccc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcca8.md#insn-00afccc8)
- 新版 [`00afcd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md#insn-00afcd90)

~~~diff
- 00afcca8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afcca8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afcca8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afcca8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afcca8 bytes f44fbea9
- 00afccac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afccac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afccac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afccac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afccac bytes fd7b01a9
- 00afccc8 ["INT_ADD", "register:40f0:8", ["const:afccc8:8", "const:4:8"]]
- 00afccc8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afcd90 ["INT_ADD", "register:40f0:8", ["const:afcd90:8", "const:4:8"]]
+ 00afcd90 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afccc8 bytes 96830394
+ 00afcd90 bytes 90830394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75b23face02312bae3a5c3b03016b985"></a>

### [`00afcd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd38.md) → [`00afce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tre

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec00.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdec00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec00.md)
- 新版 呼出元 1件 [`00bdecb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecb0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdecb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afcd38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd38.md#insn-00afcd38) · [`00afcd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd38.md#insn-00afcd54) · [`00afcd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd38.md#insn-00afcd60)
- 新版 [`00afce00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md#insn-00afce00) · [`00afce1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md#insn-00afce1c) · [`00afce28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce00.md#insn-00afce28)

~~~diff
- 00afcd38 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00afcd38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00afce00 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00afce00 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00afcd38 bytes e10100b4
+ 00afce00 bytes e10100b4
- 00afcd54 ["INT_ADD", "register:40f0:8", ["const:afcd54:8", "const:4:8"]]
- 00afcd54 ["CALL", null, ["callee:00bdecb0:8"]]
+ 00afce1c ["INT_ADD", "register:40f0:8", ["const:afce1c:8", "const:4:8"]]
+ 00afce1c ["CALL", null, ["callee:00bdecb0:8"]]
- 00afcd54 bytes ab870394
+ 00afce1c bytes a5870394
- 00afcd60 ["INT_ADD", "register:40f0:8", ["const:afcd60:8", "const:4:8"]]
- 00afcd60 ["CALL", null, ["callee:00bdecb0:8"]]
+ 00afce28 ["INT_ADD", "register:40f0:8", ["const:afce28:8", "const:4:8"]]
+ 00afce28 ["CALL", null, ["callee:00bdecb0:8"]]
- 00afcd60 bytes a8870394
+ 00afce28 bytes a2870394
~~~


<a id="compare-8391d1ace90d7b059ac03e5a3ced0eb1"></a>

### [`00afcd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd78.md) → [`00afce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec10.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdec10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec10.md)
- 新版 呼出元 1件 [`00bdecc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecc0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdecc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afcd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd78.md#insn-00afcd78) · [`00afcd94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd78.md#insn-00afcd94) · [`00afcda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcd78.md#insn-00afcda0)
- 新版 [`00afce40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md#insn-00afce40) · [`00afce5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md#insn-00afce5c) · [`00afce68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce40.md#insn-00afce68)

~~~diff
- 00afcd78 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00afcd78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00afce40 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00afce40 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00afcd78 bytes e10100b4
+ 00afce40 bytes e10100b4
- 00afcd94 ["INT_ADD", "register:40f0:8", ["const:afcd94:8", "const:4:8"]]
- 00afcd94 ["CALL", null, ["callee:00bdecc0:8"]]
+ 00afce5c ["INT_ADD", "register:40f0:8", ["const:afce5c:8", "const:4:8"]]
+ 00afce5c ["CALL", null, ["callee:00bdecc0:8"]]
- 00afcd94 bytes 9f870394
+ 00afce5c bytes 99870394
- 00afcda0 ["INT_ADD", "register:40f0:8", ["const:afcda0:8", "const:4:8"]]
- 00afcda0 ["CALL", null, ["callee:00bdecc0:8"]]
+ 00afce68 ["INT_ADD", "register:40f0:8", ["const:afce68:8", "const:4:8"]]
+ 00afce68 ["CALL", null, ["callee:00bdecc0:8"]]
- 00afcda0 bytes 9c870394
+ 00afce68 bytes 96870394
~~~


<a id="compare-7973f960b2178bc31dad6cbff5a8e07e"></a>

### [`00afcdb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdb8.md) → [`00afce80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce80.md) _INIT_273

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afce8c",
      "incomplete_value": false,
      "site": "00afce90",
      "value": [
        "leaf",
        "const:28:8"
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcdec"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afceb4"
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
      "00afcea4",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00afceac",
      "WRITE",
      [
        "storage",
        "010a0c48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afcea4",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afceac",
      "WRITE",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afcdc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdb8.md#insn-00afcdc8) · [`00afcdec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdb8.md#insn-00afcdec)
- 新版 [`00afce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce80.md#insn-00afce90) · [`00afceb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce80.md#insn-00afceb4)

~~~diff
- 00afcdc8 ["INT_ADD", "register:40f0:8", ["const:afcdc8:8", "const:4:8"]]
- 00afcdc8 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00afce90 ["INT_ADD", "register:40f0:8", ["const:afce90:8", "const:4:8"]]
+ 00afce90 ["CALL", null, ["callee:00bdaff0:8"]]
- 00afcdc8 bytes 5e780394
+ 00afce90 bytes 58780394
- 00afcdec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afcdec ["RETURN", null, ["register:0:8"]]
- 00afcdec bytes c0035fd6
+ 00afceb4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afceb4 ["RETURN", null, ["register:0:8"]]
+ 00afceb4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b7dfec1496e8480541557decebbf4a3"></a>

### [`00afcdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdf0.md) → [`00afceb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afceb8.md) _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdec30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afce00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcdf0.md#insn-00afce00)
- 新版 [`00afcec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afceb8.md#insn-00afcec8)

~~~diff
- 00afce00 ["INT_ADD", "register:40f0:8", ["const:afce00:8", "const:4:8"]]
- 00afce00 ["CALL", null, ["callee:00bdece0:8"]]
+ 00afcec8 ["INT_ADD", "register:40f0:8", ["const:afcec8:8", "const:4:8"]]
+ 00afcec8 ["CALL", null, ["callee:00bdece0:8"]]
- 00afce00 bytes 8c870394
+ 00afcec8 bytes 86870394
~~~


<a id="compare-62a5bd49ef0de3e8342651aabef42ed9"></a>

### [`00afcffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcffc.md) → [`00afd0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md) _ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00afd1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd020"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afd0e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd050"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd020",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afd1f4"
      ]
    ]
  ],
  "added": [
    [
      "00afd0e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00afd118",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afd1f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcffc.md#insn-00afd020) · [`00afd050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcffc.md#insn-00afd050) · [`00afd074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcffc.md#insn-00afd074)
- 新版 [`00afd13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md#insn-00afd13c)

~~~diff
- 00afd020 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00afd020 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afd020 bytes e80f00f9
- 00afd050 ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
- 00afd050 bytes e2060054
- 00afd074 ["INT_ADD", "register:40f0:8", ["const:afd074:8", "const:4:8"]]
- 00afd074 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00afd13c ["INT_ADD", "register:40f0:8", ["const:afd13c:8", "const:4:8"]]
+ 00afd13c ["CALL", null, ["callee:00bde6e0:8"]]
- 00afd074 bytes 6f850394
+ 00afd13c bytes 69850394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e3aab5afae9a43b86a369190930c57"></a>

### [`00afd130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd130.md) → [`00afd1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md) _ZN8firebase4PathC2ENSt6__ndk111__wrap_iterIPNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEESA_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00afd1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdec30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd134"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afd138"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afd134",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd138",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afd154",
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
      "00afd1fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afd200",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afd21c",
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

- 旧版 [`00afd134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd130.md#insn-00afd134) · [`00afd138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd130.md#insn-00afd138) · [`00afd154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd130.md#insn-00afd154)

~~~diff
- 00afd134 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afd134 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afd134 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afd134 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd134 bytes f44f02a9
- 00afd138 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afd138 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afd138 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00afd138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afd138 bytes fd7b03a9
- 00afd154 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00afd154 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afd154 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af5d36e7bb8b707061a849c090d059d"></a>

### [`00afd1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md) → [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) FUN_00afd268

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00afcffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afcffc.md) [`00afd130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd130.md) [`00afdb3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdb3c.md) [`00afdcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdcec.md) · 呼出先 3件 [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdb6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6a0.md) [`00bdec80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec80.md)
- 新版 呼出元 4件 [`00afd0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md) [`00afd1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md) [`00afdc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md) [`00afddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md) · 呼出先 3件 [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md) [`00bded30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 57.14% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afd2ac",
      "incomplete_value": false,
      "site": "00afd2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:8ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afd1e4",
      "incomplete_value": false,
      "site": "00afd1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:83d:8"
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
      "definition_site": "00afd2ec",
      "incomplete_value": true,
      "site": "00afd2f0",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00afd2e8",
      "incomplete_value": true,
      "site": "00afd2f0",
      "value": [
        "INT_SEXT",
        "8",
        [
          [
            "live",
            "register:4040:4"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afd2ac",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "00afd400",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00afd2ac",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ],
    [
      "00afd400",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md#insn-00afd1f0) · [`00afd2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md#insn-00afd2b8) · [`00afd2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md#insn-00afd2f0)
- 新版 [`00afd2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md#insn-00afd2b8) · [`00afd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md#insn-00afd380) · [`00afd3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md#insn-00afd3b8)

~~~diff
- 00afd1f0 ["INT_ADD", "register:40f0:8", ["const:afd1f0:8", "const:4:8"]]
- 00afd1f0 ["CALL", null, ["callee:00bded30:8"]]
+ 00afd2b8 ["INT_ADD", "register:40f0:8", ["const:afd2b8:8", "const:4:8"]]
+ 00afd2b8 ["CALL", null, ["callee:00bded30:8"]]
- 00afd1f0 bytes a4860394
+ 00afd2b8 bytes 9e860394
- 00afd2b8 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
+ 00afd380 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00afd2b8 bytes 00010054
+ 00afd380 bytes 00010054
- 00afd2f0 ["INT_ADD", "register:40f0:8", ["const:afd2f0:8", "const:4:8"]]
- 00afd2f0 ["CALL", null, ["callee:00bdb750:8"]]
+ 00afd3b8 ["INT_ADD", "register:40f0:8", ["const:afd3b8:8", "const:4:8"]]
+ 00afd3b8 ["CALL", null, ["callee:00bdb750:8"]]
- 00afd2f0 bytes ec780394
+ 00afd3b8 bytes e6780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ab4e358b52cab632b370427bffcf838"></a>

### [`00afd380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd380.md) → [`00afd448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md) _ZNK8firebase4Path8GetChildERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdec30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afd470",
      "incomplete_value": false,
      "site": "00afd47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:8ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afd3a8",
      "incomplete_value": false,
      "site": "00afd3b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:83d:8"
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
      "unmatched:00afd3a8",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00afd470",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd380.md#insn-00afd3b4) · [`00afd3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd380.md#insn-00afd3a8) · [`00afd3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd380.md#insn-00afd3d4)
- 新版 [`00afd47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md#insn-00afd47c) · [`00afd49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md#insn-00afd49c)

~~~diff
- 00afd3b4 ["INT_ADD", "register:40f0:8", ["const:afd3b4:8", "const:4:8"]]
- 00afd3b4 ["CALL", null, ["callee:00afa9c4:8"]]
+ 00afd47c ["INT_ADD", "register:40f0:8", ["const:afd47c:8", "const:4:8"]]
+ 00afd47c ["CALL", null, ["callee:00afa9c4:8"]]
- 00afd3b4 bytes 52f5ff97
+ 00afd47c bytes 52f5ff97
- 00afd3a8 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 00afd3a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00afd3a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00afd3a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00afd3a8 bytes 21f42091
- 00afd3d4 ["INT_ADD", "register:40f0:8", ["const:afd3d4:8", "const:4:8"]]
- 00afd3d4 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00afd49c ["INT_ADD", "register:40f0:8", ["const:afd49c:8", "const:4:8"]]
+ 00afd49c ["CALL", null, ["callee:00bdb0e0:8"]]
- 00afd3d4 bytes 17770394
+ 00afd49c bytes 11770394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f199241b8deb95976c8e980b61f6803d"></a>

### [`00afd444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd444.md) → [`00afd50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md) _ZNK8firebase4Path8GetChildERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afa8fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afa/00afa8fc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md) [`00bdec30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec30.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afd534",
      "incomplete_value": false,
      "site": "00afd540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:8ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afd46c",
      "incomplete_value": false,
      "site": "00afd478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:83d:8"
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
      "00afd534",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00afd534",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afd478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd444.md#insn-00afd478) · [`00afd46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd444.md#insn-00afd46c) · [`00afd498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd444.md#insn-00afd498)
- 新版 [`00afd540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md#insn-00afd540) · [`00afd534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md#insn-00afd534) · [`00afd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md#insn-00afd560)

~~~diff
- 00afd478 ["INT_ADD", "register:40f0:8", ["const:afd478:8", "const:4:8"]]
- 00afd478 ["CALL", null, ["callee:00afa9c4:8"]]
+ 00afd540 ["INT_ADD", "register:40f0:8", ["const:afd540:8", "const:4:8"]]
+ 00afd540 ["CALL", null, ["callee:00afa9c4:8"]]
- 00afd478 bytes 21f5ff97
+ 00afd540 bytes 21f5ff97
- 00afd46c ["COPY", "tmp:0:8", ["const:83d:8"]]
- 00afd46c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00afd46c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00afd46c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00afd534 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 00afd534 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00afd534 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00afd534 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00afd46c bytes 21f42091
+ 00afd534 bytes 21282391
- 00afd498 ["INT_ADD", "register:40f0:8", ["const:afd498:8", "const:4:8"]]
- 00afd498 ["CALL", null, ["callee:00bdb0e0:8"]]
+ 00afd560 ["INT_ADD", "register:40f0:8", ["const:afd560:8", "const:4:8"]]
+ 00afd560 ["CALL", null, ["callee:00bdb0e0:8"]]
- 00afd498 bytes e6760394
+ 00afd560 bytes e0760394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd5e8509f2644e63a4891378f1be38f3"></a>

### [`00afdb3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdb3c.md) → [`00afdc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md) _ZNK8firebase4Path17PopFrontDirectoryEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afd1a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afd1a0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdec30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec30.md) [`00bdec40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec40.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md) [`00bdecf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecf0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 26.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdb40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdb44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdb44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afdb40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afdb44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afdb48",
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
      "00afdc08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afdc0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afdc10",
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

- 旧版 [`00afdb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdb3c.md#insn-00afdb40) · [`00afdb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdb3c.md#insn-00afdb44) · [`00afdb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdb3c.md#insn-00afdb48)

~~~diff
- 00afdb40 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00afdb40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afdb40 bytes f52300f9
- 00afdb44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afdb44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afdb44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00afdb44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afdb44 bytes f44f05a9
- 00afdb48 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afdb48 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afdb48 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00afdb48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afdb48 bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5136277be5782cd277eb912e768bb71b"></a>

### [`00afdc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdc34.md) → [`00afdcfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdcfc.md) _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bdec20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bdecd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdecd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 22.73% / 新版 31.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdc38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdc3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afdc3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afdc38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afdc3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afdc40",
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
      "00afdd00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afdd04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afdd08",
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

- 旧版 [`00afdc38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdc34.md#insn-00afdc38) · [`00afdc3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdc34.md#insn-00afdc3c) · [`00afdc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afd/00afdc34.md#insn-00afdc40)

~~~diff
- 00afdc38 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00afdc38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afdc38 bytes f51b00f9
- 00afdc3c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afdc3c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afdc3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00afdc3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afdc3c bytes f44f04a9
- 00afdc40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afdc40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afdc40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00afdc40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afdc40 bytes fd7b05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f725f9f01b3b936468bde45a2e2faf89"></a>

### [`00afe698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe698.md) → [`00afe760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md) _ZN8firebase17FutureBackingDataD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdecd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdecd0.md) · 呼出先 10件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md)
- 新版 呼出元 1件 [`00bded80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded80.md) · 呼出先 10件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afe7bc",
      "incomplete_value": false,
      "site": "00afe7c0",
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
            "const:e2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afe6f4",
      "incomplete_value": false,
      "site": "00afe6f8",
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
            "const:d9d:8"
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
      "00afe7bc",
      "PARAM",
      [
        "storage",
        "002a1d9d",
        null,
        "string"
      ]
    ],
    [
      "00afe7f4",
      "READ",
      [
        "storage",
        "00c1b8a8",
        null,
        "pointer"
      ]
    ],
    [
      "00afe848",
      "READ",
      [
        "storage",
        "010a0c58",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afe7bc",
      "PARAM",
      [
        "storage",
        "002a1e2a",
        null,
        "string"
      ]
    ],
    [
      "00afe7f4",
      "READ",
      [
        "storage",
        "00c1b958",
        null,
        "pointer"
      ]
    ],
    [
      "00afe848",
      "READ",
      [
        "storage",
        "010a0d18",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afe6f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe698.md#insn-00afe6f8) · [`00afe6b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe698.md#insn-00afe6b4) · [`00afe6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afe698.md#insn-00afe6d0)
- 新版 [`00afe7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md#insn-00afe7c0) · [`00afe77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md#insn-00afe77c) · [`00afe798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md#insn-00afe798)

~~~diff
- 00afe6f8 ["INT_ADD", "register:40f0:8", ["const:afe6f8:8", "const:4:8"]]
- 00afe6f8 ["CALL", null, ["callee:00bde130:8"]]
+ 00afe7c0 ["INT_ADD", "register:40f0:8", ["const:afe7c0:8", "const:4:8"]]
+ 00afe7c0 ["CALL", null, ["callee:00bde130:8"]]
- 00afe6f8 bytes 627e0394
+ 00afe7c0 bytes 5c7e0394
- 00afe6b4 ["INT_ADD", "register:40f0:8", ["const:afe6b4:8", "const:4:8"]]
- 00afe6b4 ["CALL", null, ["callee:00bded70:8"]]
+ 00afe77c ["INT_ADD", "register:40f0:8", ["const:afe77c:8", "const:4:8"]]
+ 00afe77c ["CALL", null, ["callee:00bded70:8"]]
- 00afe6b4 bytes 83810394
+ 00afe77c bytes 7d810394
- 00afe6d0 ["INT_ADD", "register:40f0:8", ["const:afe6d0:8", "const:4:8"]]
- 00afe6d0 ["CALL", null, ["callee:00bde130:8"]]
+ 00afe798 ["INT_ADD", "register:40f0:8", ["const:afe798:8", "const:4:8"]]
+ 00afe798 ["CALL", null, ["callee:00bde130:8"]]
- 00afe6d0 bytes 6c7e0394
+ 00afe798 bytes 667e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f63614790689f80106ff974505bfcb7a"></a>

### [`00afea18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md) → [`00afeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md) _ZN8firebase26ReferenceCountedFutureImplD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md) [`00bded20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded20.md) · 呼出先 11件 [`00b011d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b011d4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb50.md)
- 新版 呼出元 2件 [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bdedd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md) · 呼出先 11件 [`00b0129c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 41.46% / 新版 34.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00afeb0c",
      "incomplete_value": true,
      "site": "00afeb10",
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
      "definition_site": "00afea44",
      "incomplete_value": true,
      "site": "00afea48",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afeb1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afeb4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afeb00",
      "READ",
      [
        "storage",
        "00c1b7b0",
        null,
        "pointer"
      ]
    ],
    [
      "00afeb10",
      "DATA",
      [
        "storage",
        "00c107a0",
        null,
        "undefined1[120]"
      ]
    ],
    [
      "unmatched:00afeb1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afebdc"
      ]
    ]
  ],
  "added": [
    [
      "00afeb00",
      "READ",
      [
        "storage",
        "00c1b860",
        null,
        "pointer"
      ]
    ],
    [
      "00afeb10",
      "DATA",
      [
        "storage",
        "00c10850",
        null,
        "undefined1[120]"
      ]
    ],
    [
      "00afebe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afebdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afea84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md#insn-00afea84) · [`00afeac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md#insn-00afeac4) · [`00afeb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afea18.md#insn-00afeb10)
- 新版 [`00afeb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md#insn-00afeb4c) · [`00afeb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md#insn-00afeb8c) · [`00afebd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md#insn-00afebd8)

~~~diff
- 00afea84 ["INT_ADD", "register:40f0:8", ["const:afea84:8", "const:4:8"]]
- 00afea84 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00afeb4c ["INT_ADD", "register:40f0:8", ["const:afeb4c:8", "const:4:8"]]
+ 00afeb4c ["CALL", null, ["callee:00bddbd0:8"]]
- 00afea84 bytes 277c0394
+ 00afeb4c bytes 217c0394
- 00afeac4 ["INT_ADD", "register:40f0:8", ["const:afeac4:8", "const:4:8"]]
- 00afeac4 ["CALL", null, ["callee:00bde8c0:8"]]
+ 00afeb8c ["INT_ADD", "register:40f0:8", ["const:afeb8c:8", "const:4:8"]]
+ 00afeb8c ["CALL", null, ["callee:00bde8c0:8"]]
- 00afeac4 bytes 537f0394
+ 00afeb8c bytes 4d7f0394
- 00afeb10 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00afeb10 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00afebd8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00afebd8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00afeb10 bytes a90000b4
+ 00afebd8 bytes a90000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-470ecbac52cab4d4b02ae0119e56b1f3"></a>

### [`00afec34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec34.md) → [`00afecfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afecfc.md) _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddec0.md) · 呼出先 11件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bddf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf70.md) · 呼出先 11件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.91% / 新版 81.91%

CFGの説明率　旧版 10.39% / 新版 12.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afeccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afed28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afedf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afecd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afeddc"
      ]
    ],
    [
      "unmatched:00afece0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afedc0"
      ]
    ],
    [
      "unmatched:00afecf4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00afecd8"
      ]
    ]
  ],
  "added": [
    [
      "00afed98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afeddc"
      ]
    ],
    [
      "00afeda8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00afedc0"
      ]
    ],
    [
      "00afedbc",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00afeda0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afecc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec34.md#insn-00afecc8) · [`00afeccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec34.md#insn-00afeccc) · [`00afecd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afec34.md#insn-00afecd0)

~~~diff
- 00afecc8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00afecc8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00afecc8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00afecc8 ["INT_ADD", "tmp:1:8", ["const:0:8", "const:1:8"]]
- 00afecc8 bytes 08359f9a
- 00afeccc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:10:8"]]
- 00afeccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00afeccc bytes 480b00f9
- 00afecd0 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00afecd0 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00afecd0 bytes 3b0200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d24a2cb0fe298af0c5743fc127aaa10"></a>

### [`00afef50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afef50.md) → [`00aff018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff018.md) _ZN8firebase10FutureBaseaSEOS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdec90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec90.md) · 呼出先 6件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md)
- 新版 呼出元 1件 [`00bded40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded40.md) · 呼出先 6件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 14.29% / 新版 12.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00afefc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aff08c"
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
      "unmatched:00afefc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff0a8"
      ]
    ],
    [
      "00aff0cc",
      "PARAM",
      [
        "storage",
        "00b00bf4",
        null,
        null
      ]
    ],
    [
      "00aff148",
      "PARAM",
      [
        "storage",
        "00b00bf4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aff08c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff0a8"
      ]
    ],
    [
      "00aff0cc",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ],
    [
      "00aff148",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afef78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afef50.md#insn-00afef78) · [`00afefa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afef50.md#insn-00afefa4) · [`00afefb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afe/00afef50.md#insn-00afefb0)
- 新版 [`00aff040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff018.md#insn-00aff040) · [`00aff078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff018.md#insn-00aff078)

~~~diff
- 00afef78 ["INT_ADD", "register:40f0:8", ["const:afef78:8", "const:4:8"]]
- 00afef78 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00aff040 ["INT_ADD", "register:40f0:8", ["const:aff040:8", "const:4:8"]]
+ 00aff040 ["CALL", null, ["callee:00bddbd0:8"]]
- 00afef78 bytes ea7a0394
+ 00aff040 bytes e47a0394
- 00afefa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afefa4 ["INT_ADD", "register:40f0:8", ["const:afefa4:8", "const:4:8"]]
- 00afefa4 ["CALLIND", null, ["register:0:8"]]
- 00afefa4 bytes 00013fd6
- 00afefb0 ["INT_ADD", "register:40f0:8", ["const:afefb0:8", "const:4:8"]]
- 00afefb0 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00aff078 ["INT_ADD", "register:40f0:8", ["const:aff078:8", "const:4:8"]]
+ 00aff078 ["CALL", null, ["callee:00bddbe0:8"]]
- 00afefb0 bytes e07a0394
+ 00aff078 bytes da7a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5514139f4dbc332ab059119d1262a520"></a>

### [`00aff108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff108.md) → [`00aff1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff1d0.md) _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-efff258289309934a8c2278584c3f572"></a>

### [`00aff110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff110.md) → [`00aff1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff1d8.md) _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddef0.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bddfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfa0.md) · 呼出先 2件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff128"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aff1f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aff12c",
      "incomplete_value": true,
      "site": "00aff138",
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aff1f4",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aff1f4",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff110.md#insn-00aff128) · [`00aff138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff110.md#insn-00aff138)
- 新版 [`00aff200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff1d8.md#insn-00aff200) · [`00aff1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff1d8.md#insn-00aff1f0)

~~~diff
- 00aff128 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aff128 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aff128 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00aff128 ["COPY", "register:4098:8", ["tmp:0:8"]]
- 00aff128 bytes 1301839a
- 00aff138 ["INT_ADD", "register:40f0:8", ["const:aff138:8", "const:4:8"]]
- 00aff138 ["CALL", null, ["callee:00bdb140:8"]]
+ 00aff200 ["INT_ADD", "register:40f0:8", ["const:aff200:8", "const:4:8"]]
+ 00aff200 ["CALL", null, ["callee:00bdb140:8"]]
- 00aff138 bytes d66f0394
+ 00aff200 bytes d06f0394
+ 00aff1f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00aff1f0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00aff1f0 ["COPY", "tmp:0:8", ["register:4018:8"]]
+ 00aff1f0 ["COPY", "register:4098:8", ["tmp:0:8"]]
+ 00aff1f0 bytes 1301839a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f061b65ee6deef709002a3b082f0c7"></a>

### [`00aff154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff154.md) → [`00aff21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff21c.md) _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) · 呼出先 4件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md)
- 新版 呼出元 1件 [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.79% / 新版 76.79%

CFGの説明率　旧版 26.92% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aff240"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff180"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff178",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff180",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff2cc"
      ]
    ],
    [
      "unmatched:00aff1a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bddbd0"
      ]
    ]
  ],
  "added": [
    [
      "00aff240",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00aff248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff2cc"
      ]
    ],
    [
      "00aff270",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bddbd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff154.md#insn-00aff178) · [`00aff180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff154.md#insn-00aff180) · [`00aff1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff154.md#insn-00aff1a8)

~~~diff
- 00aff178 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00aff178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aff178 bytes e80700f9
- 00aff180 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00aff180 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00aff180 bytes 380400b4
- 00aff1a8 ["INT_ADD", "register:40f0:8", ["const:aff1a8:8", "const:4:8"]]
- 00aff1a8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00aff1a8 bytes 5e7a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3afc1f67566376a536293ca7b913ea3"></a>

### [`00aff234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff234.md) → [`00aff2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff2fc.md) _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md) · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.55% / 新版 79.55%

CFGの説明率　旧版 25.00% / 新版 17.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff238"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff234",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff238",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff23c",
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
      "00aff2fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aff300",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aff304",
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

- 旧版 [`00aff234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff234.md#insn-00aff234) · [`00aff238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff234.md#insn-00aff238) · [`00aff23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff234.md#insn-00aff23c)

~~~diff
- 00aff234 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aff234 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aff234 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff234 bytes f50f1df8
- 00aff238 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff238 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff238 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff238 bytes f44f01a9
- 00aff23c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff23c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff23c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aff23c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff23c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84754858e4ec74fb21c9fc0e3d1a8436"></a>

### [`00aff2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff2e4.md) → [`00aff3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff3ac.md) _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf00.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bddfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfb0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.70% / 新版 69.70%

CFGの説明率　旧版 21.43% / 新版 10.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff2e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff2e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff2e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff2e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff2ec",
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
      "00aff3ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aff3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aff3b4",
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

- 旧版 [`00aff2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff2e4.md#insn-00aff2e4) · [`00aff2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff2e4.md#insn-00aff2e8) · [`00aff2ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff2e4.md#insn-00aff2ec)

~~~diff
- 00aff2e4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aff2e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aff2e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff2e4 bytes f50f1df8
- 00aff2e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff2e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff2e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff2e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff2e8 bytes f44f01a9
- 00aff2ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff2ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff2ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aff2ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff2ec bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebcdcaa1c521fd556358943a29b4e3e0"></a>

### [`00aff368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff368.md) → [`00aff430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff430.md) _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf10.md) · 呼出先 10件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bddfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfc0.md) · 呼出先 10件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.85% / 新版 85.85%

CFGの説明率　旧版 43.23% / 新版 41.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff36c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff36c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff36c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff370",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff374",
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
      "00aff434",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aff438",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aff43c",
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

- 旧版 [`00aff36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff368.md#insn-00aff36c) · [`00aff370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff368.md#insn-00aff370) · [`00aff374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff368.md#insn-00aff374)

~~~diff
- 00aff36c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aff36c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aff36c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00aff36c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff36c bytes fc6f05a9
- 00aff370 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aff370 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aff370 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00aff370 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff370 bytes fa6706a9
- 00aff374 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00aff374 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00aff374 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00aff374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff374 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e99a668693011686d2ae2ecb96ad494d"></a>

### [`00aff700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff700.md) → [`00aff7c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff7c8.md) _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bde0f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde0f0.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bde1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1a0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aff7e8",
      "incomplete_value": true,
      "site": "00aff7ec",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aff724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff700.md#insn-00aff724) · [`00aff718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff700.md#insn-00aff718)
- 新版 [`00aff7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff7c8.md#insn-00aff7ec) · [`00aff7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff7c8.md#insn-00aff7e0)

~~~diff
- 00aff724 ["INT_ADD", "register:40f0:8", ["const:aff724:8", "const:4:8"]]
- 00aff724 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00aff7ec ["INT_ADD", "register:40f0:8", ["const:aff7ec:8", "const:4:8"]]
+ 00aff7ec ["CALL", null, ["callee:00bddbe0:8"]]
- 00aff724 bytes 03790394
+ 00aff7ec bytes fd780394
- 00aff718 ["INT_ADD", "register:40f0:8", ["const:aff718:8", "const:4:8"]]
- 00aff718 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00aff7e0 ["INT_ADD", "register:40f0:8", ["const:aff7e0:8", "const:4:8"]]
+ 00aff7e0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00aff718 bytes 02790394
+ 00aff7e0 bytes fc780394
~~~


<a id="compare-dee4bc6811172cfc7033f3a3ebb25293"></a>

### [`00aff748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff748.md) → [`00aff810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md) FUN_00aff810

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aff738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff738.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00aff800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff800.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 35.29% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff760"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aff828"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00aff760"
      ],
      [
        "FALL_THROUGH",
        "00aff828"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aff828",
      "incomplete_value": true,
      "site": "00aff850",
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
      "definition_site": "00aff760",
      "incomplete_value": true,
      "site": "00aff788",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "live",
            "register:4000:8"
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
      "unmatched:00aff760",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff854"
      ]
    ]
  ],
  "added": [
    [
      "00aff828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff854"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff748.md#insn-00aff760) · [`00aff758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff748.md#insn-00aff758)
- 新版 [`00aff828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md#insn-00aff828) · [`00aff820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff810.md#insn-00aff820)

~~~diff
- 00aff760 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00aff760 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00aff760 bytes 600100b4
+ 00aff828 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00aff828 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00aff828 bytes 600100b4
- 00aff758 ["INT_ADD", "register:40f0:8", ["const:aff758:8", "const:4:8"]]
- 00aff758 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00aff820 ["INT_ADD", "register:40f0:8", ["const:aff820:8", "const:4:8"]]
+ 00aff820 ["CALL", null, ["callee:00bddbd0:8"]]
- 00aff758 bytes f2780394
+ 00aff820 bytes ec780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-348b827fc4f81b6aeabe116e80df9927"></a>

### [`00aff7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff7a4.md) → [`00aff86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff86c.md) _ZN8firebase26ReferenceCountedFutureImpl15ReferenceFutureERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 10.00% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff7ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff7f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff7fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff7f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff8a8"
      ]
    ],
    [
      "unmatched:00aff7fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff8d4"
      ]
    ],
    [
      "unmatched:00aff808",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff8dc"
      ]
    ]
  ],
  "added": [
    [
      "00aff8bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff8a8"
      ]
    ],
    [
      "00aff8c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff8d4"
      ]
    ],
    [
      "00aff8d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aff8dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aff7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff7a4.md#insn-00aff7c4) · [`00aff7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff7a4.md#insn-00aff7ec) · [`00aff7f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff7a4.md#insn-00aff7f4)
- 新版 [`00aff88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff86c.md#insn-00aff88c)

~~~diff
- 00aff7c4 ["INT_ADD", "register:40f0:8", ["const:aff7c4:8", "const:4:8"]]
- 00aff7c4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00aff88c ["INT_ADD", "register:40f0:8", ["const:aff88c:8", "const:4:8"]]
+ 00aff88c ["CALL", null, ["callee:00bddbd0:8"]]
- 00aff7c4 bytes d7780394
+ 00aff88c bytes d1780394
- 00aff7ec ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00aff7ec ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00aff7ec ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00aff7ec ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aff7ec bytes 0831899a
- 00aff7f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00aff7f4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00aff7f4 bytes 69ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-732cc8d4ef31e3a5e2cf8020b9b39a71"></a>

### [`00aff840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff840.md) → [`00aff908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00aff908.md) _ZN8firebase26ReferenceCountedFutureImpl13ReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde650.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 65.75% / 新版 65.75%

CFGの説明率　旧版 19.15% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff840"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff840"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff844"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff840",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff844",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff848",
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
      "00aff908",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aff90c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aff910",
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

- 旧版 [`00aff840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff840.md#insn-00aff840) · [`00aff844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff840.md#insn-00aff844) · [`00aff848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff840.md#insn-00aff848)

~~~diff
- 00aff840 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aff840 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aff840 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aff840 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff840 bytes f657bda9
- 00aff844 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff844 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff844 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff844 bytes f44f01a9
- 00aff848 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff848 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff848 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aff848 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff848 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ea416cf9bf1033af1085c2f9481c5ca"></a>

### [`00aff964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff964.md) → [`00affa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affa2c.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 30.00% / 新版 31.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff964"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aff968"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aff964",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff968",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aff96c",
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
      "00affa2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00affa30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00affa34",
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

- 旧版 [`00aff964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff964.md#insn-00aff964) · [`00aff968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff964.md#insn-00aff968) · [`00aff96c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00aff964.md#insn-00aff96c)

~~~diff
- 00aff964 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aff964 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aff964 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aff964 bytes f50f1df8
- 00aff968 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aff968 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aff968 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aff968 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff968 bytes f44f01a9
- 00aff96c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aff96c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aff96c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aff96c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aff96c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81308fddcb1696b40a330a381c6b0dd4"></a>

### [`00affa0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affa0c.md) → [`00affad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md) _ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 35.29% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00affa40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00affa54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00affb08"
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
      "unmatched:00affa40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affb3c"
      ]
    ],
    [
      "00affb24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00affa48"
      ]
    ]
  ],
  "added": [
    [
      "00affb08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affb3c"
      ]
    ],
    [
      "00affb24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affb10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00affa2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affa0c.md#insn-00affa2c) · [`00affa40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affa0c.md#insn-00affa40) · [`00affa54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affa0c.md#insn-00affa54)
- 新版 [`00affaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affad4.md#insn-00affaf4)

~~~diff
- 00affa2c ["INT_ADD", "register:40f0:8", ["const:affa2c:8", "const:4:8"]]
- 00affa2c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00affaf4 ["INT_ADD", "register:40f0:8", ["const:affaf4:8", "const:4:8"]]
+ 00affaf4 ["CALL", null, ["callee:00bddbd0:8"]]
- 00affa2c bytes 3d780394
+ 00affaf4 bytes 37780394
- 00affa40 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00affa40 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00affa40 bytes a90100b4
- 00affa54 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00affa54 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00affa54 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00affa54 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00affa54 bytes 0831899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41a7b82178fd0992ea9832ba2faae5b5"></a>

### [`00affab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affab4.md) → [`00affb7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affb7c.md) _ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 85.42% / 新版 85.42%

CFGの説明率　旧版 13.33% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00affae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00affbb0"
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
      "unmatched:00affae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00affb1c"
      ]
    ],
    [
      "00affbd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00affb1c"
      ]
    ],
    [
      "unmatched:00affb18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affc10"
      ]
    ]
  ],
  "added": [
    [
      "00affbb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affbe4"
      ]
    ],
    [
      "00affbd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affbe4"
      ]
    ],
    [
      "00affbe0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affc10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00affae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affab4.md#insn-00affae8) · [`00affb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affab4.md#insn-00affb18) · [`00affb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affab4.md#insn-00affb20)

~~~diff
- 00affae8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00affae8 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00affae8 bytes a90100b4
- 00affb18 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00affb18 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00affb18 ["CBRANCH", null, ["local:b20:8", "tmp:1:1"]]
- 00affb18 bytes 89010054
- 00affb20 ["INT_ADD", "register:40f0:8", ["const:affb20:8", "const:4:8"]]
- 00affb20 ["CALL", null, ["callee:00bddbe0:8"]]
- 00affb20 bytes 04780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-760ef3616434720dd9c1815616824cba"></a>

### [`00affb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affb74.md) → [`00affc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affc3c.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 7.41% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affb78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affb74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affb78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affba8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affca4"
      ]
    ]
  ],
  "added": [
    [
      "00affc3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00affc40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00affc70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00affca4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00affb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affb74.md#insn-00affb74) · [`00affb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affb74.md#insn-00affb78) · [`00affb94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affb74.md#insn-00affb94)
- 新版 [`00affc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affc3c.md#insn-00affc5c)

~~~diff
- 00affb74 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00affb74 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00affb74 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00affb74 bytes f50f1df8
- 00affb78 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00affb78 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00affb78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affb78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affb78 bytes f44f01a9
- 00affb94 ["INT_ADD", "register:40f0:8", ["const:affb94:8", "const:4:8"]]
- 00affb94 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00affc5c ["INT_ADD", "register:40f0:8", ["const:affc5c:8", "const:4:8"]]
+ 00affc5c ["CALL", null, ["callee:00bddbd0:8"]]
- 00affb94 bytes e3770394
+ 00affc5c bytes dd770394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa1347b7d553fbdaa2407b04951e8a05"></a>

### [`00affc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affc24.md) → [`00affcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affcec.md) _ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.82% / 新版 79.82%

CFGの説明率　旧版 5.77% / 新版 4.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affc24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affc24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affc28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affc24",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affc28",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affc2c",
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
      "00affcec",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00affcf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00affcf4",
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

- 旧版 [`00affc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affc24.md#insn-00affc24) · [`00affc28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affc24.md#insn-00affc28) · [`00affc2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affc24.md#insn-00affc2c)

~~~diff
- 00affc24 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00affc24 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00affc24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00affc24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00affc24 bytes fc6fbaa9
- 00affc28 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00affc28 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00affc28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affc28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affc28 bytes fa6701a9
- 00affc2c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00affc2c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00affc2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00affc2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affc2c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c239d1eed0edf952ede779009713033"></a>

### [`00affdd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affdd8.md) → [`00affea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affea0.md) _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.20% / 新版 79.20%

CFGの説明率　旧版 35.63% / 新版 43.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00affeb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00affeac",
      "DATA",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affeb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00affeb4",
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
      "00afff74",
      "DATA",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00afff78",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00afff7c",
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

- 旧版 [`00affeac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affdd8.md#insn-00affeac) · [`00affeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affdd8.md#insn-00affeb0) · [`00affeb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affdd8.md#insn-00affeb4)

~~~diff
- 00affeac ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00affeac ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00affeac ["COPY", "tmp:2:8", ["register:8:8"]]
- 00affeac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affeac bytes eb2f00a9
- 00affeb0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00affeb0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00affeb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00affeb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00affeb0 bytes ea2301a9
- 00affeb4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00affeb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00affeb4 bytes e91300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f32cd5435abb5c015fbfe3b002ac7a1"></a>

### [`00afffcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00afffcc.md) → [`00b00094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00094.md) _ZN8firebase26ReferenceCountedFutureImpl27AddCompletionCallbackLambdaERKNS_12FutureHandleENSt6__ndk18functionIFvRKNS_10FutureBaseEEEEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b001dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b001dc.md) [`00b00214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00214.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b002a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002a4.md) [`00b002dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b002dc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.55% / 新版 79.55%

CFGの説明率　旧版 17.65% / 新版 14.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afffcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afffd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afffd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afffcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afffd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afffd4",
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
      "00b00094",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b00098",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b0009c",
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

- 旧版 [`00afffcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00afffcc.md#insn-00afffcc) · [`00afffd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00afffcc.md#insn-00afffd0) · [`00afffd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00afffcc.md#insn-00afffd4)

~~~diff
- 00afffcc ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00afffcc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00afffcc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afffcc bytes f90f1bf8
- 00afffd0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00afffd0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00afffd0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afffd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afffd0 bytes f85f01a9
- 00afffd4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00afffd4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00afffd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afffd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afffd4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b92d2630032d25e85d928f8c28b70ed7"></a>

### [`00b00324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00324.md) → [`00b003ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b003ec.md) _ZNK8firebase26ReferenceCountedFutureImpl17IsRunningCallbackEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00328"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00324",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b00328",
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
      "00b003ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b003f0",
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

- 旧版 [`00b00324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00324.md#insn-00b00324) · [`00b00328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00324.md#insn-00b00328) · [`00b0033c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00324.md#insn-00b0033c)
- 新版 [`00b00404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b003ec.md#insn-00b00404)

~~~diff
- 00b00324 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b00324 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b00324 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b00324 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b00324 bytes f44fbea9
- 00b00328 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b00328 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b00328 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b00328 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b00328 bytes fd7b01a9
- 00b0033c ["INT_ADD", "register:40f0:8", ["const:b0033c:8", "const:4:8"]]
- 00b0033c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b00404 ["INT_ADD", "register:40f0:8", ["const:b00404:8", "const:4:8"]]
+ 00b00404 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b0033c bytes f9750394
+ 00b00404 bytes f3750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7e74c4aa3f01194526e3632ae2d1bc"></a>

### [`00b004b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b004b0.md) → [`00b00578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md) _ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdece0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdece0.md) · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bded90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded90.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b00628",
      "incomplete_value": false,
      "site": "00b0062c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00560",
      "incomplete_value": false,
      "site": "00b00564",
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
            "const:e2c:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b00628",
      "PARAM",
      [
        "storage",
        "002a7e2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b00628",
      "PARAM",
      [
        "storage",
        "002a7d98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b004b0.md#insn-00b00564) · [`00b004dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b004b0.md#insn-00b004dc) · [`00b004e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b004b0.md#insn-00b004e8)
- 新版 [`00b0062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md#insn-00b0062c) · [`00b005a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md#insn-00b005a4) · [`00b005b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md#insn-00b005b0)

~~~diff
- 00b00564 ["INT_ADD", "register:40f0:8", ["const:b00564:8", "const:4:8"]]
- 00b00564 ["CALL", null, ["callee:00bde130:8"]]
+ 00b0062c ["INT_ADD", "register:40f0:8", ["const:b0062c:8", "const:4:8"]]
+ 00b0062c ["CALL", null, ["callee:00bde130:8"]]
- 00b00564 bytes c7760394
+ 00b0062c bytes c1760394
- 00b004dc ["INT_ADD", "register:40f0:8", ["const:b004dc:8", "const:4:8"]]
- 00b004dc ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b005a4 ["INT_ADD", "register:40f0:8", ["const:b005a4:8", "const:4:8"]]
+ 00b005a4 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b004dc bytes 91750394
+ 00b005a4 bytes 8b750394
- 00b004e8 ["INT_ADD", "register:40f0:8", ["const:b004e8:8", "const:4:8"]]
- 00b004e8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b005b0 ["INT_ADD", "register:40f0:8", ["const:b005b0:8", "const:4:8"]]
+ 00b005b0 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b004e8 bytes 8e750394
+ 00b005b0 bytes 88750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2727d5b04c2e367636ca7a4aac7568ec"></a>

### [`00b00aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00aa8.md) → [`00b00b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded10.md) · 呼出先 2件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00bdedc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedc0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 84.62% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b00b88",
      "incomplete_value": true,
      "site": "00b00b90",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "00b00ac0",
      "incomplete_value": true,
      "site": "00b00ac8",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b00ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00aa8.md#insn-00b00ac8) · [`00b00ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00aa8.md#insn-00b00ac0) · [`00b00ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00aa8.md#insn-00b00ad4)
- 新版 [`00b00b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md#insn-00b00b90) · [`00b00b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00b70.md#insn-00b00b9c)

~~~diff
- 00b00ac8 ["INT_ADD", "register:40f0:8", ["const:b00ac8:8", "const:4:8"]]
- 00b00ac8 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b00b90 ["INT_ADD", "register:40f0:8", ["const:b00b90:8", "const:4:8"]]
+ 00b00b90 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b00ac8 bytes 16740394
+ 00b00b90 bytes 10740394
- 00b00ac0 ["COPY", "register:4000:8", ["register:4098:8"]]
- 00b00ac0 bytes e00313aa
- 00b00ad4 ["INT_ADD", "register:40f0:8", ["const:b00ad4:8", "const:4:8"]]
- 00b00ad4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b00b9c ["INT_ADD", "register:40f0:8", ["const:b00b9c:8", "const:4:8"]]
+ 00b00b9c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b00ad4 bytes 13740394
+ 00b00b9c bytes 0d740394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af40e064d972a9faabfd3a517abdb7a"></a>

### [`00b00cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00cac.md) → [`00b00d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00d74.md) _ZN8firebase12FutureHandleaSERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddea0.md) · 呼出先 3件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00bddf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf50.md) · 呼出先 3件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 14.29% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00cf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b00dc0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00cc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b00cc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b00db4"
      ]
    ],
    [
      "unmatched:00b00cfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b00df0"
      ]
    ],
    [
      "00b00de0",
      "PARAM",
      [
        "storage",
        "00b00bf4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b00d8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b00db4"
      ]
    ],
    [
      "00b00dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b00df0"
      ]
    ],
    [
      "00b00de0",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00cac.md#insn-00b00cc4) · [`00b00cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00cac.md#insn-00b00cd0) · [`00b00cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00cac.md#insn-00b00cf8)
- 新版 [`00b00d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00d74.md#insn-00b00d98)

~~~diff
- 00b00cc4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b00cc4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b00cc4 bytes 480100b4
- 00b00cd0 ["INT_ADD", "register:40f0:8", ["const:b00cd0:8", "const:4:8"]]
- 00b00cd0 ["CALL", null, ["callee:00bddd60:8"]]
+ 00b00d98 ["INT_ADD", "register:40f0:8", ["const:b00d98:8", "const:4:8"]]
+ 00b00d98 ["CALL", null, ["callee:00bddd60:8"]]
- 00b00cd0 bytes f8730394
+ 00b00d98 bytes f2730394
- 00b00cf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00b00cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b00cf8 bytes 600600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86a80fedaf0579c445b35bfa3d75d80f"></a>

### [`00b00d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d38.md) → [`00b00e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md) _ZN8firebase12FutureHandleC1EOS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdeca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeca0.md) · 呼出先 3件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00bded50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded50.md) · 呼出先 3件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b00e38",
      "incomplete_value": false,
      "site": "00b00e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00d70",
      "incomplete_value": false,
      "site": "00b00d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:bf4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b00e5c"
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
      "unmatched:00b00d70",
      "PARAM",
      [
        "storage",
        "00b00bf4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b00e38",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d38.md#insn-00b00d74) · [`00b00d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d38.md#insn-00b00d94)
- 新版 [`00b00e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md#insn-00b00e3c) · [`00b00e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md#insn-00b00e5c)

~~~diff
- 00b00d74 ["INT_ADD", "register:40f0:8", ["const:b00d74:8", "const:4:8"]]
- 00b00d74 ["CALL", null, ["callee:00bddd50:8"]]
+ 00b00e3c ["INT_ADD", "register:40f0:8", ["const:b00e3c:8", "const:4:8"]]
+ 00b00e3c ["CALL", null, ["callee:00bddd50:8"]]
- 00b00d74 bytes cb730394
+ 00b00e3c bytes c5730394
- 00b00d94 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b00d94 ["RETURN", null, ["register:0:8"]]
- 00b00d94 bytes c0035fd6
+ 00b00e5c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b00e5c ["RETURN", null, ["register:0:8"]]
+ 00b00e5c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd3ab5be7edfdb83d9448faf245e5f08"></a>

### [`00b00d98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d98.md) → [`00b00e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md) _ZN8firebase12FutureHandleaSEOS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdecb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdecb0.md) · 呼出先 3件 [`00b00bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bf4.md) [`00bddca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddca0.md) [`00bddcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcb0.md)
- 新版 呼出元 1件 [`00bded60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded60.md) · 呼出先 3件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b00ec4",
      "incomplete_value": false,
      "site": "00b00ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:cbc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00dfc",
      "incomplete_value": false,
      "site": "00b00e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:bf4:8"
          ]
        ]
      ]
    },
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
      "00b00ec4",
      "PARAM",
      [
        "storage",
        "00b00bf4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b00ec4",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d98.md#insn-00b00e04) · [`00b00dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d98.md#insn-00b00dbc) · [`00b00dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00d98.md#insn-00b00dd0)
- 新版 [`00b00ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md#insn-00b00ecc) · [`00b00e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md#insn-00b00e84) · [`00b00e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md#insn-00b00e98)

~~~diff
- 00b00e04 ["INT_ADD", "register:40f0:8", ["const:b00e04:8", "const:4:8"]]
- 00b00e04 ["CALL", null, ["callee:00bddd50:8"]]
+ 00b00ecc ["INT_ADD", "register:40f0:8", ["const:b00ecc:8", "const:4:8"]]
+ 00b00ecc ["CALL", null, ["callee:00bddd50:8"]]
- 00b00e04 bytes a7730394
+ 00b00ecc bytes a1730394
- 00b00dbc ["INT_ADD", "register:40f0:8", ["const:b00dbc:8", "const:4:8"]]
- 00b00dbc ["CALL", null, ["callee:00bddd60:8"]]
+ 00b00e84 ["INT_ADD", "register:40f0:8", ["const:b00e84:8", "const:4:8"]]
+ 00b00e84 ["CALL", null, ["callee:00bddd60:8"]]
- 00b00dbc bytes bd730394
+ 00b00e84 bytes b7730394
- 00b00dd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b00dd0 ["INT_ADD", "register:40f0:8", ["const:b00dd0:8", "const:4:8"]]
- 00b00dd0 ["CALLIND", null, ["register:0:8"]]
+ 00b00e98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b00e98 ["INT_ADD", "register:40f0:8", ["const:b00e98:8", "const:4:8"]]
+ 00b00e98 ["CALLIND", null, ["register:0:8"]]
- 00b00dd0 bytes 00013fd6
+ 00b00e98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e4ad2c025bcbb5043193e01a04cc9ed"></a>

### [`00b00e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e74.md) → [`00b00f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bded00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md) · 呼出先 8件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01004",
      "incomplete_value": false,
      "site": "00b01008",
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
      "definition_site": "00b00f3c",
      "incomplete_value": false,
      "site": "00b00f40",
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
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b01004",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "00b0101c",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b01004",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ],
    [
      "00b0101c",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e74.md#insn-00b00f40) · [`00b00ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e74.md#insn-00b00ea0) · [`00b00eac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00e74.md#insn-00b00eac)
- 新版 [`00b01008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md#insn-00b01008) · [`00b00f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md#insn-00b00f68) · [`00b00f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md#insn-00b00f74)

~~~diff
- 00b00f40 ["INT_ADD", "register:40f0:8", ["const:b00f40:8", "const:4:8"]]
- 00b00f40 ["CALL", null, ["callee:00bde130:8"]]
+ 00b01008 ["INT_ADD", "register:40f0:8", ["const:b01008:8", "const:4:8"]]
+ 00b01008 ["CALL", null, ["callee:00bde130:8"]]
- 00b00f40 bytes 50740394
+ 00b01008 bytes 4a740394
- 00b00ea0 ["INT_ADD", "register:40f0:8", ["const:b00ea0:8", "const:4:8"]]
- 00b00ea0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b00f68 ["INT_ADD", "register:40f0:8", ["const:b00f68:8", "const:4:8"]]
+ 00b00f68 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b00ea0 bytes 20730394
+ 00b00f68 bytes 1a730394
- 00b00eac ["INT_ADD", "register:40f0:8", ["const:b00eac:8", "const:4:8"]]
- 00b00eac ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b00f74 ["INT_ADD", "register:40f0:8", ["const:b00f74:8", "const:4:8"]]
+ 00b00f74 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b00eac bytes 1d730394
+ 00b00f74 bytes 17730394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-412ec8428702dc0f479627645b01f143"></a>

### [`00b01264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01264.md) → [`00b0132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md) _INIT_274

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b00bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b00/00b00bfc.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b00cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cc4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b01344",
      "incomplete_value": true,
      "site": "00b01344",
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0127c",
      "incomplete_value": true,
      "site": "00b0127c",
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
                "const:8a8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b01344",
      "incomplete_value": true,
      "site": "00b01344",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0127c",
      "incomplete_value": true,
      "site": "00b0127c",
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
            "const:8:8"
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
      "00b01334",
      "READ",
      [
        "storage",
        "00c1b8a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b01334",
      "PARAM",
      [
        "storage",
        "010a0c58",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b01338",
      "READ",
      [
        "storage",
        "00c1b8a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b01334",
      "READ",
      [
        "storage",
        "00c1b958",
        null,
        "pointer"
      ]
    ],
    [
      "00b01334",
      "PARAM",
      [
        "storage",
        "010a0d18",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b01338",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0126c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01264.md#insn-00b0126c) · [`00b01270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01264.md#insn-00b01270) · [`00b01278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01264.md#insn-00b01278)
- 新版 [`00b01334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md#insn-00b01334) · [`00b01338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md#insn-00b01338) · [`00b01340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md#insn-00b01340)

~~~diff
- 00b0126c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8a8:8"]]
- 00b0126c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01334 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:958:8"]]
+ 00b01334 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0126c bytes 215444f9
+ 00b01334 bytes 21ac44f9
- 00b01270 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8a0:8"]]
- 00b01270 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01338 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:950:8"]]
+ 00b01338 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b01270 bytes 005044f9
+ 00b01338 bytes 00a844f9
- 00b01278 ["COPY", "register:4010:8", ["const:be5ed0:8"]]
+ 00b01340 ["COPY", "register:4010:8", ["const:be5f80:8"]]
- 00b01278 bytes c2627210
+ 00b01340 bytes 02627210
~~~


<a id="compare-5c6dcba7298a398375d05d8b23f3cbd6"></a>

### [`00b012e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b012e8.md) → [`00b013b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md) _ZN8firebase17ModuleInitializerD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b013cc",
      "incomplete_value": true,
      "site": "00b013d0",
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
      "definition_site": "00b01304",
      "incomplete_value": true,
      "site": "00b01308",
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
      "00b013c4",
      "READ",
      [
        "storage",
        "00c1b8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b013d0",
      "DATA",
      [
        "storage",
        "00c108b8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b013c4",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00b013d0",
      "DATA",
      [
        "storage",
        "00c10968",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b012fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b012e8.md#insn-00b012fc) · [`00b0131c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b012e8.md#insn-00b0131c) · [`00b01324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b012e8.md#insn-00b01324)
- 新版 [`00b013c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md#insn-00b013c4) · [`00b013e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md#insn-00b013e4) · [`00b013ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md#insn-00b013ec)

~~~diff
- 00b012fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8d8:8"]]
- 00b012fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b013c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
+ 00b013c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b012fc bytes 086d44f9
+ 00b013c4 bytes 08c544f9
- 00b0131c ["INT_ADD", "register:40f0:8", ["const:b0131c:8", "const:4:8"]]
- 00b0131c ["CALL", null, ["callee:00bdb010:8"]]
+ 00b013e4 ["INT_ADD", "register:40f0:8", ["const:b013e4:8", "const:4:8"]]
+ 00b013e4 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0131c bytes 11670394
+ 00b013e4 bytes 0b670394
- 00b01324 ["INT_ADD", "register:40f0:8", ["const:b01324:8", "const:4:8"]]
- 00b01324 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b013ec ["INT_ADD", "register:40f0:8", ["const:b013ec:8", "const:4:8"]]
+ 00b013ec ["CALL", null, ["callee:00bddbf0:8"]]
- 00b01324 bytes 07720394
+ 00b013ec bytes 01720394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09dc89584c0045e8b85d4b6fd0568aa0"></a>

### [`00b01348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01348.md) → [`00b01410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md) _ZN8firebase17ModuleInitializerD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0142c",
      "incomplete_value": true,
      "site": "00b01430",
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
      "definition_site": "00b01364",
      "incomplete_value": true,
      "site": "00b01368",
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
      "00b01424",
      "READ",
      [
        "storage",
        "00c1b8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b01430",
      "DATA",
      [
        "storage",
        "00c108b8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b01424",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00b01430",
      "DATA",
      [
        "storage",
        "00c10968",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0135c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01348.md#insn-00b0135c) · [`00b0137c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01348.md#insn-00b0137c) · [`00b01384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01348.md#insn-00b01384)
- 新版 [`00b01424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md#insn-00b01424) · [`00b01444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md#insn-00b01444) · [`00b0144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md#insn-00b0144c)

~~~diff
- 00b0135c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8d8:8"]]
- 00b0135c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01424 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
+ 00b01424 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0135c bytes 086d44f9
+ 00b01424 bytes 08c544f9
- 00b0137c ["INT_ADD", "register:40f0:8", ["const:b0137c:8", "const:4:8"]]
- 00b0137c ["CALL", null, ["callee:00bdb010:8"]]
+ 00b01444 ["INT_ADD", "register:40f0:8", ["const:b01444:8", "const:4:8"]]
+ 00b01444 ["CALL", null, ["callee:00bdb010:8"]]
- 00b0137c bytes f9660394
+ 00b01444 bytes f3660394
- 00b01384 ["INT_ADD", "register:40f0:8", ["const:b01384:8", "const:4:8"]]
- 00b01384 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b0144c ["INT_ADD", "register:40f0:8", ["const:b0144c:8", "const:4:8"]]
+ 00b0144c ["CALL", null, ["callee:00bddbf0:8"]]
- 00b01384 bytes ef710394
+ 00b0144c bytes e9710394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba008d3dfb78f268fa1e8daa5752584"></a>

### [`00b013a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b013a8.md) → [`00b01470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPFNS_10InitResultES2_S3_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bdeda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeda0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdee50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b014fc",
      "incomplete_value": false,
      "site": "00b01500",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01434",
      "incomplete_value": false,
      "site": "00b01438",
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
            "const:dbf:8"
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
      "definition_site": "00b0150c",
      "incomplete_value": false,
      "site": "00b01510",
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
            "const:3b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01444",
      "incomplete_value": false,
      "site": "00b01448",
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
            "const:44b:8"
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
      "00b014fc",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b0150c",
      "PARAM",
      [
        "storage",
        "002ae44b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b014fc",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b0150c",
      "PARAM",
      [
        "storage",
        "002ae3b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b013a8.md#insn-00b01438) · [`00b01448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b013a8.md#insn-00b01448) · [`00b01404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b013a8.md#insn-00b01404)
- 新版 [`00b01500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md#insn-00b01500) · [`00b01510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md#insn-00b01510) · [`00b014cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md#insn-00b014cc)

~~~diff
- 00b01438 ["INT_ADD", "register:40f0:8", ["const:b01438:8", "const:4:8"]]
- 00b01438 ["CALL", null, ["callee:00bde130:8"]]
+ 00b01500 ["INT_ADD", "register:40f0:8", ["const:b01500:8", "const:4:8"]]
+ 00b01500 ["CALL", null, ["callee:00bde130:8"]]
- 00b01438 bytes 12730394
+ 00b01500 bytes 0c730394
- 00b01448 ["INT_ADD", "register:40f0:8", ["const:b01448:8", "const:4:8"]]
- 00b01448 ["CALL", null, ["callee:00bde130:8"]]
+ 00b01510 ["INT_ADD", "register:40f0:8", ["const:b01510:8", "const:4:8"]]
+ 00b01510 ["CALL", null, ["callee:00bde130:8"]]
- 00b01448 bytes 0e730394
+ 00b01510 bytes 08730394
- 00b01404 ["INT_ADD", "register:40f0:8", ["const:b01404:8", "const:4:8"]]
- 00b01404 ["CALL", null, ["callee:00bdee50:8"]]
+ 00b014cc ["INT_ADD", "register:40f0:8", ["const:b014cc:8", "const:4:8"]]
+ 00b014cc ["CALL", null, ["callee:00bdee50:8"]]
- 00b01404 bytes 67760394
+ 00b014cc bytes 61760394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e5390768d3a76c47e0f0813622c6f2"></a>

### [`00b01454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01454.md) → [`00b0151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdeda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeda0.md) · 呼出先 14件 [`00b01608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 1件 [`00bdee50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee50.md) · 呼出先 14件 [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0163c",
      "incomplete_value": false,
      "site": "00b01640",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01574",
      "incomplete_value": false,
      "site": "00b01578",
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
            "const:dbf:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0164c",
      "incomplete_value": false,
      "site": "00b01650",
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
            "const:1df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01584",
      "incomplete_value": false,
      "site": "00b01588",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0163c",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b0164c",
      "PARAM",
      [
        "storage",
        "002ac1e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0163c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b0164c",
      "PARAM",
      [
        "storage",
        "002ac1df",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b014c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01454.md#insn-00b014c0) · [`00b01578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01454.md#insn-00b01578) · [`00b01588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01454.md#insn-00b01588)
- 新版 [`00b01588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md#insn-00b01588) · [`00b01640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md#insn-00b01640) · [`00b01650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md#insn-00b01650)

~~~diff
- 00b014c0 ["INT_ADD", "register:40f0:8", ["const:b014c0:8", "const:4:8"]]
- 00b014c0 ["CALL", null, ["callee:00bddbf0:8"]]
+ 00b01588 ["INT_ADD", "register:40f0:8", ["const:b01588:8", "const:4:8"]]
+ 00b01588 ["CALL", null, ["callee:00bddbf0:8"]]
- 00b014c0 bytes a0710394
+ 00b01588 bytes 9a710394
- 00b01578 ["INT_ADD", "register:40f0:8", ["const:b01578:8", "const:4:8"]]
- 00b01578 ["CALL", null, ["callee:00bde130:8"]]
+ 00b01640 ["INT_ADD", "register:40f0:8", ["const:b01640:8", "const:4:8"]]
+ 00b01640 ["CALL", null, ["callee:00bde130:8"]]
- 00b01578 bytes c2720394
+ 00b01640 bytes bc720394
- 00b01588 ["INT_ADD", "register:40f0:8", ["const:b01588:8", "const:4:8"]]
- 00b01588 ["CALL", null, ["callee:00bde130:8"]]
+ 00b01650 ["INT_ADD", "register:40f0:8", ["const:b01650:8", "const:4:8"]]
+ 00b01650 ["CALL", null, ["callee:00bde130:8"]]
- 00b01588 bytes be720394
+ 00b01650 bytes b8720394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42bfa379e92ad159a358ae7e94638171"></a>

### [`00b01608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md) → [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) FUN_00b016d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b01454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01454.md) [`00b0278c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md) · 呼出先 12件 [`00b0278c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 2件 [`00b0151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md) [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) · 呼出先 12件 [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.48% / 新版 97.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b017a8",
      "incomplete_value": false,
      "site": "00b017ac",
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
            "const:db5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b016e0",
      "incomplete_value": false,
      "site": "00b016e4",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b017e8",
      "incomplete_value": false,
      "site": "00b01800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b02000:8"
          ],
          [
            "leaf",
            "const:854:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01720",
      "incomplete_value": false,
      "site": "00b01738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b02000:8"
          ],
          [
            "leaf",
            "const:78c:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01888",
      "incomplete_value": false,
      "site": "00b0189c",
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
            "const:c1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b017c0",
      "incomplete_value": false,
      "site": "00b017d4",
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
            "const:cb2:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b017a8",
      "PARAM",
      [
        "storage",
        "0029dd28",
        null,
        "string"
      ]
    ],
    [
      "00b017e8",
      "PARAM",
      [
        "storage",
        "00b0278c",
        null,
        null
      ]
    ],
    [
      "00b01888",
      "PARAM",
      [
        "storage",
        "002a8cb2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b017a8",
      "PARAM",
      [
        "storage",
        "0029ddb5",
        null,
        "string"
      ]
    ],
    [
      "00b017e8",
      "PARAM",
      [
        "storage",
        "00b02854",
        null,
        null
      ]
    ],
    [
      "00b01888",
      "PARAM",
      [
        "storage",
        "002a8c1e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b016e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md#insn-00b016e4) · [`00b01738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md#insn-00b01738) · [`00b017d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md#insn-00b017d4)
- 新版 [`00b017ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md#insn-00b017ac) · [`00b01800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md#insn-00b01800) · [`00b0189c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md#insn-00b0189c)

~~~diff
- 00b016e4 ["INT_ADD", "register:40f0:8", ["const:b016e4:8", "const:4:8"]]
- 00b016e4 ["CALL", null, ["callee:00bddf10:8"]]
+ 00b017ac ["INT_ADD", "register:40f0:8", ["const:b017ac:8", "const:4:8"]]
+ 00b017ac ["CALL", null, ["callee:00bddf10:8"]]
- 00b016e4 bytes df710394
+ 00b017ac bytes d9710394
- 00b01738 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b01738 ["INT_ADD", "register:40f0:8", ["const:b01738:8", "const:4:8"]]
- 00b01738 ["CALLIND", null, ["register:0:8"]]
+ 00b01800 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b01800 ["INT_ADD", "register:40f0:8", ["const:b01800:8", "const:4:8"]]
+ 00b01800 ["CALLIND", null, ["register:0:8"]]
- 00b01738 bytes 20013fd6
+ 00b01800 bytes 20013fd6
- 00b017d4 ["INT_ADD", "register:40f0:8", ["const:b017d4:8", "const:4:8"]]
- 00b017d4 ["CALL", null, ["callee:00bdedb0:8"]]
+ 00b0189c ["INT_ADD", "register:40f0:8", ["const:b0189c:8", "const:4:8"]]
+ 00b0189c ["CALL", null, ["callee:00bdedb0:8"]]
- 00b017d4 bytes 4b750394
+ 00b0189c bytes 45750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abcc9f15aae9cbd58eeab303b9620eaf"></a>

### [`00b01c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01c38.md) → [`00b01d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md) _ZN8firebase11AppCallback16SetEnabledByNameEPKcb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b01d54",
      "incomplete_value": true,
      "site": "00b01d54",
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
      "definition_site": "00b01c8c",
      "incomplete_value": true,
      "site": "00b01c8c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01d40",
      "incomplete_value": true,
      "site": "00b01d44",
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
      "definition_site": "00b01c78",
      "incomplete_value": true,
      "site": "00b01c7c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01e14",
      "incomplete_value": true,
      "site": "00b01e20",
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
            "const:e8b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01d4c",
      "incomplete_value": true,
      "site": "00b01d58",
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
            "const:dfe:8"
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
      "00b01d38",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b01d3c",
      "READ",
      [
        "storage",
        "010a0c70",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b01d4c",
      "READ",
      [
        "storage",
        "00c1b8b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b01d38",
      "READ",
      [
        "storage",
        "00c1b970",
        null,
        "pointer"
      ]
    ],
    [
      "00b01d3c",
      "READ",
      [
        "storage",
        "010a0d30",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b01d4c",
      "READ",
      [
        "storage",
        "00c1b968",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01c38.md#insn-00b01c7c) · [`00b01d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01c38.md#insn-00b01d58) · [`00b01d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01c38.md#insn-00b01d74)
- 新版 [`00b01d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md#insn-00b01d44) · [`00b01e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md#insn-00b01e20) · [`00b01e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md#insn-00b01e3c)

~~~diff
- 00b01c7c ["INT_ADD", "register:40f0:8", ["const:b01c7c:8", "const:4:8"]]
- 00b01c7c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b01d44 ["INT_ADD", "register:40f0:8", ["const:b01d44:8", "const:4:8"]]
+ 00b01d44 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b01c7c bytes a96f0394
+ 00b01d44 bytes a36f0394
- 00b01d58 ["INT_ADD", "register:40f0:8", ["const:b01d58:8", "const:4:8"]]
- 00b01d58 ["CALL", null, ["callee:00bde260:8"]]
+ 00b01e20 ["INT_ADD", "register:40f0:8", ["const:b01e20:8", "const:4:8"]]
+ 00b01e20 ["CALL", null, ["callee:00bde260:8"]]
- 00b01d58 bytes 16710394
+ 00b01e20 bytes 10710394
- 00b01d74 ["INT_ADD", "register:40f0:8", ["const:b01d74:8", "const:4:8"]]
- 00b01d74 ["CALL", null, ["callee:00bde260:8"]]
+ 00b01e3c ["INT_ADD", "register:40f0:8", ["const:b01e3c:8", "const:4:8"]]
+ 00b01e3c ["CALL", null, ["callee:00bde260:8"]]
- 00b01d74 bytes 0f710394
+ 00b01e3c bytes 09710394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f65d6c05b8892b3983da2d577113fe4"></a>

### [`00b01db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01db8.md) → [`00b01e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01e80.md) _ZN8firebase11AppCallback13SetEnabledAllEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b01eb8",
      "incomplete_value": true,
      "site": "00b01eb8",
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
      "definition_site": "00b01df0",
      "incomplete_value": true,
      "site": "00b01df0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01ea4",
      "incomplete_value": true,
      "site": "00b01ea8",
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
      "definition_site": "00b01ddc",
      "incomplete_value": true,
      "site": "00b01de0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01ed8",
      "incomplete_value": true,
      "site": "00b01edc",
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
            "const:382:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01e10",
      "incomplete_value": true,
      "site": "00b01e14",
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
            "const:38b:8"
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
      "00b01e98",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b01ea0",
      "READ",
      [
        "storage",
        "010a0c70",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b01eb0",
      "READ",
      [
        "storage",
        "00c1b8b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b01e98",
      "READ",
      [
        "storage",
        "00c1b970",
        null,
        "pointer"
      ]
    ],
    [
      "00b01ea0",
      "READ",
      [
        "storage",
        "010a0d30",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b01eb0",
      "READ",
      [
        "storage",
        "00c1b968",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01db8.md#insn-00b01de0) · [`00b01e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01db8.md#insn-00b01e14) · [`00b01dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01db8.md#insn-00b01dd0)
- 新版 [`00b01ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01e80.md#insn-00b01ea8) · [`00b01edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01e80.md#insn-00b01edc) · [`00b01e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01e80.md#insn-00b01e98)

~~~diff
- 00b01de0 ["INT_ADD", "register:40f0:8", ["const:b01de0:8", "const:4:8"]]
- 00b01de0 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b01ea8 ["INT_ADD", "register:40f0:8", ["const:b01ea8:8", "const:4:8"]]
+ 00b01ea8 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b01de0 bytes 506f0394
+ 00b01ea8 bytes 4a6f0394
- 00b01e14 ["INT_ADD", "register:40f0:8", ["const:b01e14:8", "const:4:8"]]
- 00b01e14 ["CALL", null, ["callee:00bde260:8"]]
+ 00b01edc ["INT_ADD", "register:40f0:8", ["const:b01edc:8", "const:4:8"]]
+ 00b01edc ["CALL", null, ["callee:00bde260:8"]]
- 00b01e14 bytes e7700394
+ 00b01edc bytes e1700394
- 00b01dd0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8c0:8"]]
- 00b01dd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01e98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:970:8"]]
+ 00b01e98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b01dd0 bytes 086144f9
+ 00b01e98 bytes 08b944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-303dfda8400c1d90574cacde4ca85a2f"></a>

### [`00b01ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01ee0.md) → [`00b01fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md) _ZN8firebase11AppCallback11AddCallbackEPS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc60.md) · 呼出先 11件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bddd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd10.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_store_alignment

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 83.72% / 新版 83.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02138"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b02200"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b01fe4",
      "incomplete_value": true,
      "site": "00b01fe4",
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
      "definition_site": "00b01f1c",
      "incomplete_value": true,
      "site": "00b01f1c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b01fdc",
      "READ",
      [
        "storage",
        "00c1b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b01fe0",
      "READ",
      [
        "storage",
        "010a0c68",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b02004",
      "WRITE",
      [
        "storage",
        "010a0c68",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b01fdc",
      "READ",
      [
        "storage",
        "00c1b968",
        null,
        "pointer"
      ]
    ],
    [
      "00b01fe0",
      "READ",
      [
        "storage",
        "010a0d28",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b02004",
      "WRITE",
      [
        "storage",
        "010a0d28",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01ee0.md#insn-00b01ff0) · [`00b02000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01ee0.md#insn-00b02000) · [`00b02040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01ee0.md#insn-00b02040)
- 新版 [`00b020b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md#insn-00b020b8) · [`00b020c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md#insn-00b020c8) · [`00b02108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md#insn-00b02108)

~~~diff
- 00b01ff0 ["INT_ADD", "register:40f0:8", ["const:b01ff0:8", "const:4:8"]]
- 00b01ff0 ["CALL", null, ["callee:00bddf10:8"]]
+ 00b020b8 ["INT_ADD", "register:40f0:8", ["const:b020b8:8", "const:4:8"]]
+ 00b020b8 ["CALL", null, ["callee:00bddf10:8"]]
- 00b01ff0 bytes 9c6f0394
+ 00b020b8 bytes 966f0394
- 00b02000 ["INT_ADD", "register:40f0:8", ["const:b02000:8", "const:4:8"]]
- 00b02000 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b020c8 ["INT_ADD", "register:40f0:8", ["const:b020c8:8", "const:4:8"]]
+ 00b020c8 ["CALL", null, ["callee:00bdb010:8"]]
- 00b02000 bytes d8630394
+ 00b020c8 bytes d2630394
- 00b02040 ["INT_ADD", "register:40f0:8", ["const:b02040:8", "const:4:8"]]
- 00b02040 ["CALL", null, ["callee:00bde260:8"]]
+ 00b02108 ["INT_ADD", "register:40f0:8", ["const:b02108:8", "const:4:8"]]
+ 00b02108 ["CALL", null, ["callee:00bde260:8"]]
- 00b02040 bytes 5c700394
+ 00b02108 bytes 56700394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd1d879150ce7ea33f54efdb98d2e92"></a>

### [`00b02154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02154.md) → [`00b0221c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b0221c.md) _ZN8firebase16StaticFutureData26CleanupFutureDataForModuleEPKv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded90.md) · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddcf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md) [`00bde650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde650.md)
- 新版 呼出元 1件 [`00bdee40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee40.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bde700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde700.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 77.78% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b02250",
      "incomplete_value": true,
      "site": "00b02250",
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
      "definition_site": "00b02188",
      "incomplete_value": true,
      "site": "00b02188",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b021c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b0228c"
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
      "00b02230",
      "READ",
      [
        "storage",
        "00c1b8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b02238",
      "READ",
      [
        "storage",
        "010a0c78",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b02248",
      "READ",
      [
        "storage",
        "00c1b8c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b02230",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ],
    [
      "00b02238",
      "READ",
      [
        "storage",
        "010a0d38",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b02248",
      "READ",
      [
        "storage",
        "00c1b978",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02154.md#insn-00b02178) · [`00b02180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02154.md#insn-00b02180) · [`00b02188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02154.md#insn-00b02188)
- 新版 [`00b02240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b0221c.md#insn-00b02240) · [`00b02248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b0221c.md#insn-00b02248) · [`00b02250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b0221c.md#insn-00b02250)

~~~diff
- 00b02178 ["INT_ADD", "register:40f0:8", ["const:b02178:8", "const:4:8"]]
- 00b02178 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b02240 ["INT_ADD", "register:40f0:8", ["const:b02240:8", "const:4:8"]]
+ 00b02240 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b02178 bytes 6a6e0394
+ 00b02240 bytes 646e0394
- 00b02180 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8c8:8"]]
- 00b02180 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b02248 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:978:8"]]
+ 00b02248 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b02180 bytes d66644f9
+ 00b02248 bytes d6be44f9
- 00b02188 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b02188 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00b02250 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b02250 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b02188 bytes 680600b4
+ 00b02250 bytes 680600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d489cd79cc252891cfff6abc58392497"></a>

### [`00b02268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02268.md) → [`00b02330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02330.md) _ZN8firebase16StaticFutureData22GetFutureDataForModuleEPKvi

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bded80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded80.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddce0.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md)
- 新版 呼出元 1件 [`00bdee30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee30.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 65.91% / 新版 67.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b02370",
      "incomplete_value": true,
      "site": "00b02370",
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
      "definition_site": "00b022a8",
      "incomplete_value": true,
      "site": "00b022a8",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02310"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02334"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0234c",
      "READ",
      [
        "storage",
        "00c1b8d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b02290",
      "READ",
      [
        "storage",
        "010a0c78",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b02368",
      "READ",
      [
        "storage",
        "00c1b8c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b0234c",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ],
    [
      "00b02358",
      "READ",
      [
        "storage",
        "010a0d38",
        "_ZN8firebase16StaticFutureData16s_futures_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b02368",
      "READ",
      [
        "storage",
        "00c1b978",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02268.md#insn-00b02298) · [`00b022a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02268.md#insn-00b022a8) · [`00b02310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02268.md#insn-00b02310)
- 新版 [`00b02360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02330.md#insn-00b02360) · [`00b02370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02330.md#insn-00b02370)

~~~diff
- 00b02298 ["INT_ADD", "register:40f0:8", ["const:b02298:8", "const:4:8"]]
- 00b02298 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b02360 ["INT_ADD", "register:40f0:8", ["const:b02360:8", "const:4:8"]]
+ 00b02360 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b02298 bytes 226e0394
+ 00b02360 bytes 1c6e0394
- 00b022a8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b022a8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b02370 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b02370 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b022a8 bytes 800000b4
+ 00b02370 bytes 800000b4
- 00b02310 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b02310 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00b02310 bytes 950600b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8be2ca0d8f01bea20d29a5275fd22a63"></a>

### [`00b02438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02438.md) → [`00b02500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02500.md) _ZN8firebase11SplitStringERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md) [`00bde6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde6d0.md) [`00bde870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde870.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bde780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde780.md) [`00bde920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde920.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.55% / 新版 79.55%

CFGの説明率　旧版 21.28% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 5件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02450"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0246c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02450",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0246c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b024b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b026dc"
      ]
    ]
  ],
  "added": [
    [
      "00b02518",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b02534",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b02578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b026dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02438.md#insn-00b02450) · [`00b0246c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02438.md#insn-00b0246c) · [`00b02484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02438.md#insn-00b02484)

~~~diff
- 00b02450 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b02450 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b02450 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b02450 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b02450 bytes fd7b07a9
- 00b0246c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b0246c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b0246c bytes e90f00f9
- 00b02484 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b02484 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b02484 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b02484 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:1:8"]]
- 00b02484 bytes 5b15809a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e4618bf5f3892bf902d2a83b6bd75db"></a>

### [`00b02648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02648.md) → [`00b02710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md) _ZN8firebase19CreateApiIdentifierEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdedb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdedb0.md) · 呼出先 2件 [`00b026e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b026e8.md) [`00bdb6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6a0.md)
- 新版 呼出元 1件 [`00bdee60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee60.md) · 呼出先 2件 [`00b027b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b027b0.md) [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.50% / 新版 72.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0264c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0264c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02648",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0264c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02650",
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
      "00b02710",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b02714",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b02718",
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

- 旧版 [`00b02648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02648.md#insn-00b02648) · [`00b0264c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02648.md#insn-00b0264c) · [`00b02650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02648.md#insn-00b02650)

~~~diff
- 00b02648 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b02648 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b02648 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b02648 bytes f70f1cf8
- 00b0264c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b0264c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0264c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0264c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0264c bytes f65701a9
- 00b02650 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b02650 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b02650 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b02650 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b02650 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17872d439b002716cdc8007850fb97eb"></a>

### [`00b026e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b026e8.md) → [`00b027b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b027b0.md) FUN_00b027b0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b02648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02648.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdee10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee10.md)
- 新版 呼出元 1件 [`00b02710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdeec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeec0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 36.59% / 新版 36.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02704"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02700",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02704",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02708",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b027c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ],
    [
      "00b027cc",
      "WRITE",
      [
        "storage",
        "Stack[-0xf0]",
        null,
        null
      ]
    ],
    [
      "00b027d0",
      "WRITE",
      [
        "storage",
        "Stack[-0xd0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b026e8.md#insn-00b02700) · [`00b02704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b026e8.md#insn-00b02704) · [`00b02708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b026e8.md#insn-00b02708)

~~~diff
- 00b02700 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b02700 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b02700 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b02700 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b02700 bytes e00700ad
- 00b02704 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b02704 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b02704 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b02704 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00b02704 bytes e20f01ad
- 00b02708 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b02708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b02708 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b02708 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50a0:16"]]
- 00b02708 bytes e41702ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39e68add285357fba0ef25ef45370184"></a>

### [`00b0278c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md) → [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) FUN_00b02854

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b01608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md) · 呼出先 12件 [`00b01608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b01/00b01608.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 1件 [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) · 呼出先 12件 [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b028d4",
      "incomplete_value": true,
      "site": "00b028d8",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b028e4",
      "incomplete_value": false,
      "site": "00b028e8",
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
            "const:de6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0281c",
      "incomplete_value": false,
      "site": "00b02820",
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
            "const:d59:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b028f4",
      "incomplete_value": true,
      "site": "00b028f8",
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
                "const:140:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b02888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0290c"
      ]
    ],
    [
      "00b028bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b02844"
      ]
    ],
    [
      "unmatched:00b0281c",
      "PARAM",
      [
        "storage",
        "0029dd59",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b02888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b02900"
      ]
    ],
    [
      "00b028bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0290c"
      ]
    ],
    [
      "00b028e4",
      "PARAM",
      [
        "storage",
        "0029dde6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md#insn-00b02810) · [`00b02820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md#insn-00b02820) · [`00b02830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b0278c.md#insn-00b02830)
- 新版 [`00b028d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md#insn-00b028d8) · [`00b028e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md#insn-00b028e8) · [`00b028f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md#insn-00b028f8)

~~~diff
- 00b02810 ["INT_ADD", "register:40f0:8", ["const:b02810:8", "const:4:8"]]
- 00b02810 ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b028d8 ["INT_ADD", "register:40f0:8", ["const:b028d8:8", "const:4:8"]]
+ 00b028d8 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b02810 bytes c86c0394
+ 00b028d8 bytes c26c0394
- 00b02820 ["INT_ADD", "register:40f0:8", ["const:b02820:8", "const:4:8"]]
- 00b02820 ["CALL", null, ["callee:00bde110:8"]]
+ 00b028e8 ["INT_ADD", "register:40f0:8", ["const:b028e8:8", "const:4:8"]]
+ 00b028e8 ["CALL", null, ["callee:00bde110:8"]]
- 00b02820 bytes 106e0394
+ 00b028e8 bytes 0a6e0394
- 00b02830 ["INT_ADD", "register:40f0:8", ["const:b02830:8", "const:4:8"]]
- 00b02830 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b028f8 ["INT_ADD", "register:40f0:8", ["const:b028f8:8", "const:4:8"]]
+ 00b028f8 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b02830 bytes 346e0394
+ 00b028f8 bytes 2e6e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f5d1f6c02442eabc3c9088590f61abd"></a>

### [`00b02d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02d5c.md) → [`00b02e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e24.md) _INIT_275

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b02e50",
      "incomplete_value": true,
      "site": "00b02e50",
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
                "const:970:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02d88",
      "incomplete_value": true,
      "site": "00b02d88",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b02e70",
      "incomplete_value": true,
      "site": "00b02e70",
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02da8",
      "incomplete_value": true,
      "site": "00b02da8",
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
                "const:8d0:8"
              ]
            ]
          ]
        ]
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
      "definition_site": "00b02d84",
      "incomplete_value": false,
      "site": "00b02d8c",
      "value": [
        "leaf",
        "const:28:8"
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
      "00b02e48",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b02e50",
      "WRITE",
      [
        "storage",
        "010a0c70",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b02e68",
      "READ",
      [
        "storage",
        "00c1b8d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b02e48",
      "READ",
      [
        "storage",
        "00c1b970",
        null,
        "pointer"
      ]
    ],
    [
      "00b02e50",
      "WRITE",
      [
        "storage",
        "010a0d30",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b02e68",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02d5c.md#insn-00b02d8c) · [`00b02d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02d5c.md#insn-00b02d6c) · [`00b02d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02d5c.md#insn-00b02d78)
- 新版 [`00b02e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e24.md#insn-00b02e54) · [`00b02e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e24.md#insn-00b02e34) · [`00b02e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e24.md#insn-00b02e40)

~~~diff
- 00b02d8c ["INT_ADD", "register:40f0:8", ["const:b02d8c:8", "const:4:8"]]
- 00b02d8c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b02e54 ["INT_ADD", "register:40f0:8", ["const:b02e54:8", "const:4:8"]]
+ 00b02e54 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b02d8c bytes 6d600394
+ 00b02e54 bytes 67600394
- 00b02d6c ["INT_ADD", "register:40f0:8", ["const:b02d6c:8", "const:4:8"]]
- 00b02d6c ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b02e34 ["INT_ADD", "register:40f0:8", ["const:b02e34:8", "const:4:8"]]
+ 00b02e34 ["CALL", null, ["callee:00bdaff0:8"]]
- 00b02d6c bytes 75600394
+ 00b02e34 bytes 6f600394
- 00b02d78 ["INT_ADD", "register:40f0:8", ["const:b02d78:8", "const:4:8"]]
- 00b02d78 ["CALL", null, ["callee:00bdddd0:8"]]
+ 00b02e40 ["INT_ADD", "register:40f0:8", ["const:b02e40:8", "const:4:8"]]
+ 00b02e40 ["CALL", null, ["callee:00bdddd0:8"]]
- 00b02d78 bytes ea6b0394
+ 00b02e40 bytes e46b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5524c634e6a77a87ea372d3d5a650464"></a>

### [`00b02db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02db4.md) → [`00b02e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md) _ZN8firebase7VariantaSERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9a0.md) · 呼出先 11件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) · 呼出先 11件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 75.12% / 新版 75.12%

CFGの説明率　旧版 65.28% / 新版 65.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b02fd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02e2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b02ed4",
      "DATA",
      [
        "storage",
        "002f6059",
        "switchD_00b02e14::switchdataD_002f6059",
        "byte"
      ]
    ],
    [
      "00b02edc",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00b02f3c"
      ]
    ],
    [
      "unmatched:00b02e28",
      "PARAM",
      [
        "storage",
        "0029dd89",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b02ed4",
      "DATA",
      [
        "storage",
        "002f6059",
        "switchD_00b02edc::switchdataD_002f6059",
        "byte"
      ]
    ],
    [
      "00b02edc",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00b030b0"
      ]
    ],
    [
      "00b02ef0",
      "PARAM",
      [
        "storage",
        "0029de16",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02db4.md#insn-00b02ddc) · [`00b02e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02db4.md#insn-00b02e2c) · [`00b02e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b02/00b02db4.md#insn-00b02e50)
- 新版 [`00b02ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md#insn-00b02ea4) · [`00b02f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md#insn-00b02f18)

~~~diff
- 00b02ddc ["CBRANCH", null, ["local:b43:8", "register:101:1"]]
+ 00b02ea4 ["CBRANCH", null, ["local:b44:8", "register:101:1"]]
- 00b02ddc bytes 80170054
+ 00b02ea4 bytes 80170054
- 00b02e2c ["INT_ADD", "register:40f0:8", ["const:b02e2c:8", "const:4:8"]]
- 00b02e2c ["CALL", null, ["callee:00bdddf0:8"]]
- 00b02e2c bytes c56b0394
- 00b02e50 ["INT_ADD", "register:40f0:8", ["const:b02e50:8", "const:4:8"]]
- 00b02e50 ["CALL", null, ["callee:00bde130:8"]]
+ 00b02f18 ["INT_ADD", "register:40f0:8", ["const:b02f18:8", "const:4:8"]]
+ 00b02f18 ["CALL", null, ["callee:00bde130:8"]]
- 00b02e50 bytes 8c6c0394
+ 00b02f18 bytes 866c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdff7cdd525361a72ff797a3bb2a9a51"></a>

### [`00b030f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b030f8.md) → [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) _ZN8firebase7Variant5ClearENS0_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b030f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b030f8.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) · 呼出先 6件 [`00b030f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b030f8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bdee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee70.md)
- 新版 呼出元 2件 [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) · 呼出先 6件 [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.71% / 新版 93.71%

CFGの説明率　旧版 65.38% / 新版 66.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b03420"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b031a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b031f8",
      "DATA",
      [
        "storage",
        "002f6064",
        "switchD_00b03138::switchdataD_002f6064",
        "byte"
      ]
    ],
    [
      "unmatched:00b031a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b03288"
      ]
    ],
    [
      "00b03284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b031a8"
      ]
    ]
  ],
  "added": [
    [
      "00b031f8",
      "DATA",
      [
        "storage",
        "002f6064",
        "switchD_00b03200::switchdataD_002f6064",
        "byte"
      ]
    ],
    [
      "00b0326c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b03288"
      ]
    ],
    [
      "00b03284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b03270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b031a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b030f8.md#insn-00b031a4) · [`00b03274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b030f8.md#insn-00b03274)
- 新版 [`00b0326c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md#insn-00b0326c) · [`00b0333c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md#insn-00b0333c)

~~~diff
- 00b031a4 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00b031a4 bytes e0000054
+ 00b0326c ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
+ 00b0326c bytes e0000054
- 00b03274 ["INT_ADD", "register:40f0:8", ["const:b03274:8", "const:4:8"]]
- 00b03274 ["CALL", null, ["local:b0:8"]]
+ 00b0333c ["INT_ADD", "register:40f0:8", ["const:b0333c:8", "const:4:8"]]
+ 00b0333c ["CALL", null, ["local:b0:8"]]
- 00b03274 bytes a1ffff97
+ 00b0333c bytes a1ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66b90cea0ca9c74df7182a82d84e83f9"></a>

### [`00b033b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b033b4.md) → [`00b0347c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0347c.md) _ZNK8firebase7Variant14mutable_stringEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee30.md) · 呼出先 3件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 1件 [`00bdeee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeee0.md) · 呼出先 3件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 82.81% / 新版 82.81%

CFGの説明率　旧版 58.33% / 新版 60.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03408"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b034dc",
      "incomplete_value": false,
      "site": "00b034e4",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03414",
      "incomplete_value": false,
      "site": "00b0341c",
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
            "const:46a:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03464"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b03498",
      "READ",
      [
        "storage",
        "00c1b8e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b03404",
      "PARAM",
      [
        "storage",
        "002ad3b0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b03408",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdddf0"
      ]
    ]
  ],
  "added": [
    [
      "00b03498",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b034cc",
      "PARAM",
      [
        "storage",
        "002ad3a7",
        null,
        "string"
      ]
    ],
    [
      "00b034d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdddf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b033b4.md#insn-00b03408) · [`00b0341c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b033b4.md#insn-00b0341c) · [`00b03464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b033b4.md#insn-00b03464)
- 新版 [`00b034e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0347c.md#insn-00b034e4)

~~~diff
- 00b03408 ["INT_ADD", "register:40f0:8", ["const:b03408:8", "const:4:8"]]
- 00b03408 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b03408 bytes 4e6a0394
- 00b0341c ["INT_ADD", "register:40f0:8", ["const:b0341c:8", "const:4:8"]]
- 00b0341c ["CALL", null, ["callee:00bde130:8"]]
+ 00b034e4 ["INT_ADD", "register:40f0:8", ["const:b034e4:8", "const:4:8"]]
+ 00b034e4 ["CALL", null, ["callee:00bde130:8"]]
- 00b0341c bytes 196b0394
+ 00b034e4 bytes 136b0394
- 00b03464 ["INT_ADD", "register:40f0:8", ["const:b03464:8", "const:4:8"]]
- 00b03464 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b03464 bytes 376a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e1092760c0dbf681fe21d47b760270a"></a>

### [`00b034b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b034b4.md) → [`00b0357c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md) _ZN8firebase7Variant16set_mutable_blobEPKvm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee20.md) · 呼出先 5件 [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bdeea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeea0.md)
- 新版 呼出元 1件 [`00bdeed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeed0.md) · 呼出先 5件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 28.57% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03514"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b035f0",
      "incomplete_value": false,
      "site": "00b035f8",
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
            "const:5c5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03528",
      "incomplete_value": false,
      "site": "00b03530",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b035f4",
      "incomplete_value": true,
      "site": "00b035f8",
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
              "LOAD",
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0352c",
      "incomplete_value": true,
      "site": "00b03530",
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
              "LOAD",
              "INT_LEFT"
            ]
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
      "unmatched:00b03510",
      "PARAM",
      [
        "storage",
        "002ab039",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b03514",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdddf0"
      ]
    ],
    [
      "unmatched:00b03520",
      "READ",
      [
        "storage",
        "00c1b8e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b035d8",
      "PARAM",
      [
        "storage",
        "002ab03f",
        null,
        "string"
      ]
    ],
    [
      "00b035dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdddf0"
      ]
    ],
    [
      "00b035e8",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b034b4.md#insn-00b03514) · [`00b03530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b034b4.md#insn-00b03530)
- 新版 [`00b035f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md#insn-00b035f8) · [`00b035dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md#insn-00b035dc)

~~~diff
- 00b03514 ["INT_ADD", "register:40f0:8", ["const:b03514:8", "const:4:8"]]
- 00b03514 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b03514 bytes 0b6a0394
- 00b03530 ["INT_ADD", "register:40f0:8", ["const:b03530:8", "const:4:8"]]
- 00b03530 ["CALL", null, ["callee:00bde130:8"]]
+ 00b035f8 ["INT_ADD", "register:40f0:8", ["const:b035f8:8", "const:4:8"]]
+ 00b035f8 ["CALL", null, ["callee:00bde130:8"]]
- 00b03530 bytes d46a0394
+ 00b035f8 bytes ce6a0394
+ 00b035dc ["INT_ADD", "register:40f0:8", ["const:b035dc:8", "const:4:8"]]
+ 00b035dc ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b035dc bytes 056a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-407c840dad917f6eb7ba82a1185624f8"></a>

### [`00b03548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03548.md) → [`00b03610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03610.md) _ZN8firebase7VariantaSEOS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8f0.md) · 呼出先 3件 [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) · 呼出先 3件 [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 19.23% / 新版 18.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b036fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b035ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0359c",
      "DATA",
      [
        "storage",
        "002f607a",
        "switchD_00b035a4::switchdataD_002f607a",
        "byte"
      ]
    ],
    [
      "unmatched:00b035ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b036e0"
      ]
    ],
    [
      "unmatched:00b035f4",
      "PARAM",
      [
        "storage",
        "002ab039",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b03664",
      "DATA",
      [
        "storage",
        "002f607a",
        "switchD_00b0366c::switchdataD_002f607a",
        "byte"
      ]
    ],
    [
      "00b036b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b036e0"
      ]
    ],
    [
      "00b036bc",
      "PARAM",
      [
        "storage",
        "002ab03f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b035ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03548.md#insn-00b035ec) · [`00b035f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03548.md#insn-00b035f8) · [`00b03614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03548.md#insn-00b03614)
- 新版 [`00b036dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03610.md#insn-00b036dc)

~~~diff
- 00b035ec ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00b035ec bytes 60010054
- 00b035f8 ["INT_ADD", "register:40f0:8", ["const:b035f8:8", "const:4:8"]]
- 00b035f8 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b035f8 bytes d2690394
- 00b03614 ["INT_ADD", "register:40f0:8", ["const:b03614:8", "const:4:8"]]
- 00b03614 ["CALL", null, ["callee:00bde130:8"]]
+ 00b036dc ["INT_ADD", "register:40f0:8", ["const:b036dc:8", "const:4:8"]]
+ 00b036dc ["CALL", null, ["callee:00bde130:8"]]
- 00b03614 bytes 9b6a0394
+ 00b036dc bytes 956a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c342c1b4abe6760d050fdea5a322e24"></a>

### [`00b03660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03660.md) → [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) _ZNK8firebase7VarianteqERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b03660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03660.md) [`00bdee40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee40.md) · 呼出先 5件 [`00b03660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03660.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 2件 [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) [`00bdeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeef0.md) · 呼出先 5件 [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 67.52% / 新版 67.52%

CFGの説明率　旧版 43.03% / 新版 43.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 25件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03664"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b03660",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03664",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03668",
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
      "00b03728",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b0372c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b03730",
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

- 旧版 [`00b03660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03660.md#insn-00b03660) · [`00b03664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03660.md#insn-00b03664) · [`00b03668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03660.md#insn-00b03668)

~~~diff
- 00b03660 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b03660 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00b03660 bytes e80f1cfc
- 00b03664 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b03664 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b03664 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b03664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03664 bytes f65701a9
- 00b03668 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b03668 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b03668 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b03668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03668 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a21c28317934fa3a375790306b9f26c"></a>

### [`00b03bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03bdc.md) → [`00b03ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md) _ZNK8firebase7VariantltERKS0_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde620.md) · 呼出先 5件 [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md) [`00bdee40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee40.md)
- 新版 呼出元 1件 [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) · 呼出先 5件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00bdeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeef0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.97% / 新版 61.97%

CFGの説明率　旧版 26.22% / 新版 26.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 28件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03bf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b03bf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03bf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b03cc8",
      "READ",
      [
        "storage",
        "00c1b8e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b03cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b03cbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b03cc8",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03bdc.md#insn-00b03bf0) · [`00b03bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03bdc.md#insn-00b03bf4) · [`00b03c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b03/00b03bdc.md#insn-00b03c00)
- 新版 [`00b03cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md#insn-00b03cc8)

~~~diff
- 00b03bf0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b03bf0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b03bf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b03bf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03bf0 bytes f44f05a9
- 00b03bf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b03bf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b03bf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b03bf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03bf4 bytes fd7b06a9
- 00b03c00 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:8e0:8"]]
- 00b03c00 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b03cc8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:990:8"]]
+ 00b03cc8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b03c00 bytes 7b7344f9
+ 00b03cc8 bytes 7bcb44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca5c9e248eb33231f9ba9c07b82141b5"></a>

### [`00b04448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04448.md) → [`00b04510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04510.md) _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbb0.md) · 呼出先 2件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) · 呼出先 2件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 37.50% / 新版 37.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0444c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b04448",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0444c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b04524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0446c"
      ]
    ]
  ],
  "added": [
    [
      "00b04510",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b04514",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b04524",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b04534"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04448.md#insn-00b04448) · [`00b0444c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04448.md#insn-00b0444c) · [`00b04468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04448.md#insn-00b04468)

~~~diff
- 00b04448 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b04448 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b04448 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b04448 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b04448 bytes f44fbea9
- 00b0444c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0444c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0444c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0444c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0444c bytes fd7b01a9
- 00b04468 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b04468 ["RETURN", null, ["register:0:8"]]
- 00b04468 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d47dc563c96aa04666a8b84fa1c249f"></a>

### [`00b044a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044a8.md) → [`00b04570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md) _ZNK8firebase7Variant18assert_is_not_typeENS0_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04598",
      "incomplete_value": false,
      "site": "00b045a0",
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
            "const:e16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b044d0",
      "incomplete_value": false,
      "site": "00b044d8",
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
            "const:d89:8"
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
      "00b04598",
      "PARAM",
      [
        "storage",
        "0029dd89",
        null,
        "string"
      ]
    ],
    [
      "00b045a8",
      "READ",
      [
        "storage",
        "00c1b8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b045b4",
      "PARAM",
      [
        "storage",
        "0029968e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b04598",
      "PARAM",
      [
        "storage",
        "0029de16",
        null,
        "string"
      ]
    ],
    [
      "00b045a8",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b045b4",
      "PARAM",
      [
        "storage",
        "0029971b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b044d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044a8.md#insn-00b044d8) · [`00b044d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044a8.md#insn-00b044d0) · [`00b044e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044a8.md#insn-00b044e0)
- 新版 [`00b045a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md#insn-00b045a0) · [`00b04598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md#insn-00b04598) · [`00b045a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md#insn-00b045a8)

~~~diff
- 00b044d8 ["INT_ADD", "register:40f0:8", ["const:b044d8:8", "const:4:8"]]
- 00b044d8 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b045a0 ["INT_ADD", "register:40f0:8", ["const:b045a0:8", "const:4:8"]]
+ 00b045a0 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b044d8 bytes 1a660394
+ 00b045a0 bytes 14660394
- 00b044d0 ["COPY", "tmp:0:8", ["const:d89:8"]]
- 00b044d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b044d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b044d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b04598 ["COPY", "tmp:0:8", ["const:e16:8"]]
+ 00b04598 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04598 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04598 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b044d0 bytes 00243691
+ 00b04598 bytes 00583891
- 00b044e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8e0:8"]]
- 00b044e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b045a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00b045a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b044e0 bytes 087144f9
+ 00b045a8 bytes 08c944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79eeb164fdb8616613008434c50665df"></a>

### [`00b044fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044fc.md) → [`00b045c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b045c4.md) _ZNK8firebase7Variant16assert_is_stringEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbd0.md) · 呼出先 2件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bddc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc80.md) · 呼出先 2件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04604",
      "incomplete_value": false,
      "site": "00b04608",
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
            "const:3a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0453c",
      "incomplete_value": false,
      "site": "00b04540",
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
            "const:3b0:8"
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
      "00b04604",
      "PARAM",
      [
        "storage",
        "002ad3b0",
        null,
        "string"
      ]
    ],
    [
      "00b04614",
      "READ",
      [
        "storage",
        "00c1b8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b04620",
      "PARAM",
      [
        "storage",
        "002ae46a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b04604",
      "PARAM",
      [
        "storage",
        "002ad3a7",
        null,
        "string"
      ]
    ],
    [
      "00b04614",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b04620",
      "PARAM",
      [
        "storage",
        "002ae3d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044fc.md#insn-00b04540) · [`00b0453c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044fc.md#insn-00b0453c) · [`00b0454c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b044fc.md#insn-00b0454c)
- 新版 [`00b04608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b045c4.md#insn-00b04608) · [`00b04604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b045c4.md#insn-00b04604) · [`00b04614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b045c4.md#insn-00b04614)

~~~diff
- 00b04540 ["INT_ADD", "register:40f0:8", ["const:b04540:8", "const:4:8"]]
- 00b04540 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b04608 ["INT_ADD", "register:40f0:8", ["const:b04608:8", "const:4:8"]]
+ 00b04608 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b04540 bytes 00660394
+ 00b04608 bytes fa650394
- 00b0453c ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00b0453c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0453c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0453c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b04604 ["COPY", "tmp:0:8", ["const:3a7:8"]]
+ 00b04604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0453c bytes 00c00e91
+ 00b04604 bytes 009c0e91
- 00b0454c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8e0:8"]]
- 00b0454c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b04614 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:990:8"]]
+ 00b04614 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0454c bytes 297144f9
+ 00b04614 bytes 29c944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d23a6c9bc004efd9d1aabc02079d225a"></a>

### [`00b04568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04568.md) → [`00b04630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04630.md) _ZNK8firebase7Variant14assert_is_blobEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde610.md) · 呼出先 2件 [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6c0.md) · 呼出先 2件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04660",
      "incomplete_value": false,
      "site": "00b04664",
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
            "const:3f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04598",
      "incomplete_value": false,
      "site": "00b0459c",
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
            "const:39:8"
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
      "00b04660",
      "PARAM",
      [
        "storage",
        "002ab039",
        null,
        "string"
      ]
    ],
    [
      "00b04670",
      "READ",
      [
        "storage",
        "00c1b8e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b0467c",
      "PARAM",
      [
        "storage",
        "00297538",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b04660",
      "PARAM",
      [
        "storage",
        "002ab03f",
        null,
        "string"
      ]
    ],
    [
      "00b04670",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b0467c",
      "PARAM",
      [
        "storage",
        "002975c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0459c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04568.md#insn-00b0459c) · [`00b04598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04568.md#insn-00b04598) · [`00b045a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04568.md#insn-00b045a8)
- 新版 [`00b04664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04630.md#insn-00b04664) · [`00b04660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04630.md#insn-00b04660) · [`00b04670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04630.md#insn-00b04670)

~~~diff
- 00b0459c ["INT_ADD", "register:40f0:8", ["const:b0459c:8", "const:4:8"]]
- 00b0459c ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b04664 ["INT_ADD", "register:40f0:8", ["const:b04664:8", "const:4:8"]]
+ 00b04664 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b0459c bytes e9650394
+ 00b04664 bytes e3650394
- 00b04598 ["COPY", "tmp:0:8", ["const:39:8"]]
- 00b04598 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b04598 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b04598 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b04660 ["COPY", "tmp:0:8", ["const:3f:8"]]
+ 00b04660 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04660 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04660 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b04598 bytes 00e40091
+ 00b04660 bytes 00fc0091
- 00b045a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8e0:8"]]
- 00b045a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b04670 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:990:8"]]
+ 00b04670 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b045a8 bytes 297144f9
+ 00b04670 bytes 29c944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be5ea4cfbec6dfe806b73b77b6e9495"></a>

### [`00b045c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b045c4.md) → [`00b0468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md) _ZNK8firebase7Variant8AsStringEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddbc0.md) · 呼出先 10件 [`00b04768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04768.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00bddc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc70.md) · 呼出先 10件 [`00b04830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04830.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.19% / 新版 96.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0471c",
      "incomplete_value": false,
      "site": "00b04724",
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
            "const:dec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04654",
      "incomplete_value": false,
      "site": "00b0465c",
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
            "const:d5f:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04750",
      "incomplete_value": false,
      "site": "00b04758",
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
            "const:74d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04688",
      "incomplete_value": false,
      "site": "00b04690",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b046d0",
      "DATA",
      [
        "storage",
        "002f60a8",
        "switchD_00b04614::switchdataD_002f60a8",
        "byte"
      ]
    ],
    [
      "00b0471c",
      "PARAM",
      [
        "storage",
        "0029cd5f",
        null,
        null
      ]
    ],
    [
      "00b04750",
      "PARAM",
      [
        "storage",
        "002996c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b046d0",
      "DATA",
      [
        "storage",
        "002f60a8",
        "switchD_00b046dc::switchdataD_002f60a8",
        "byte"
      ]
    ],
    [
      "00b0471c",
      "PARAM",
      [
        "storage",
        "0029cdec",
        null,
        null
      ]
    ],
    [
      "00b04750",
      "PARAM",
      [
        "storage",
        "0029974d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0465c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b045c4.md#insn-00b0465c) · [`00b04690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b045c4.md#insn-00b04690) · [`00b04724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b045c4.md#insn-00b04724)
- 新版 [`00b04724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md#insn-00b04724) · [`00b04758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md#insn-00b04758) · [`00b047ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md#insn-00b047ec)

~~~diff
- 00b0465c ["INT_ADD", "register:40f0:8", ["const:b0465c:8", "const:4:8"]]
- 00b0465c ["CALL", null, ["callee:00b04830:8"]]
+ 00b04724 ["INT_ADD", "register:40f0:8", ["const:b04724:8", "const:4:8"]]
+ 00b04724 ["CALL", null, ["callee:00b04830:8"]]
- 00b0465c bytes 43000094
+ 00b04724 bytes 43000094
- 00b04690 ["INT_ADD", "register:40f0:8", ["const:b04690:8", "const:4:8"]]
- 00b04690 ["CALL", null, ["callee:00b04830:8"]]
+ 00b04758 ["INT_ADD", "register:40f0:8", ["const:b04758:8", "const:4:8"]]
+ 00b04758 ["CALL", null, ["callee:00b04830:8"]]
- 00b04690 bytes 36000094
+ 00b04758 bytes 36000094
- 00b04724 ["INT_ADD", "register:40f0:8", ["const:b04724:8", "const:4:8"]]
- 00b04724 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b047ec ["INT_ADD", "register:40f0:8", ["const:b047ec:8", "const:4:8"]]
+ 00b047ec ["CALL", null, ["callee:00bdb010:8"]]
- 00b04724 bytes 0f5a0394
+ 00b047ec bytes 095a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-967230bb8083f6be3d1488392d20a4ef"></a>

### [`00b049ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b049ec.md) → [`00b04ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04ab4.md) _ZNK8firebase7Variant6AsBoolEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8e0.md) [`00bdee40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeef0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 57.14% / 新版 52.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04b20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b04be8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04b24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b04b20",
      "DATA",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b04b20",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b04b24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdeef0"
      ]
    ]
  ],
  "added": [
    [
      "00b04be8",
      "DATA",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04be8",
      "WRITE",
      [
        "storage",
        "Stack[-0xa8]",
        null,
        null
      ]
    ],
    [
      "00b04bec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bdeef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04a58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b049ec.md#insn-00b04a58) · [`00b04b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b049ec.md#insn-00b04b20) · [`00b04b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b049ec.md#insn-00b04b24)
- 新版 [`00b04b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04ab4.md#insn-00b04b20)

~~~diff
- 00b04a58 ["INT_ADD", "register:40f0:8", ["const:b04a58:8", "const:4:8"]]
- 00b04a58 ["CALL", null, ["callee:00bdd990:8"]]
+ 00b04b20 ["INT_ADD", "register:40f0:8", ["const:b04b20:8", "const:4:8"]]
+ 00b04b20 ["CALL", null, ["callee:00bdd990:8"]]
- 00b04a58 bytes a2630394
+ 00b04b20 bytes 9c630394
- 00b04b20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00b04b20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b04b20 bytes e82f00f9
- 00b04b24 ["INT_ADD", "register:40f0:8", ["const:b04b24:8", "const:4:8"]]
- 00b04b24 ["CALL", null, ["callee:00bdeef0:8"]]
- 00b04b24 bytes c7680394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055bc7a7861438b9cbcfccbda08fce24"></a>

### [`00b04c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04c50.md) → [`00b04d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d18.md) _ZN8firebase7Variant8TypeNameENS0_4TypeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde070.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde120.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.00% / 新版 68.00%

CFGの説明率　旧版 44.44% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04c7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b04d44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04d5c",
      "incomplete_value": false,
      "site": "00b04d60",
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
            "const:753:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04c94",
      "incomplete_value": false,
      "site": "00b04c98",
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
            "const:6c6:8"
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
      "00b04d28",
      "READ",
      [
        "storage",
        "010a0c8c",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b04c7c",
      "WRITE",
      [
        "storage",
        "010a0c8c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b04c9c"
      ]
    ]
  ],
  "added": [
    [
      "00b04d28",
      "READ",
      [
        "storage",
        "010a0d4c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04d44",
      "WRITE",
      [
        "storage",
        "010a0d4c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b04d64"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04c50.md#insn-00b04c7c) · [`00b04c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04c50.md#insn-00b04c98) · [`00b04cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04c50.md#insn-00b04cb0)
- 新版 [`00b04d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d18.md#insn-00b04d60)

~~~diff
- 00b04c7c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b04c7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:c8c:8"]]
- 00b04c7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b04c7c bytes 28313239
- 00b04c98 ["INT_ADD", "register:40f0:8", ["const:b04c98:8", "const:4:8"]]
- 00b04c98 ["CALL", null, ["callee:00bde130:8"]]
+ 00b04d60 ["INT_ADD", "register:40f0:8", ["const:b04d60:8", "const:4:8"]]
+ 00b04d60 ["CALL", null, ["callee:00bde130:8"]]
- 00b04c98 bytes fa640394
+ 00b04d60 bytes f4640394
- 00b04cb0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b04cb0 ["RETURN", null, ["register:0:8"]]
- 00b04cb0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ede4ea6321362c9685cf5f6849664c"></a>

### [`00b04e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04e9c.md) → [`00b04f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04f64.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE14__ass

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdee50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee50.md) · 呼出先 5件 [`00bdd9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9a0.md) [`00bde620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde620.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md) [`00bdee60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee60.md) [`00bdee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee70.md)
- 新版 呼出元 1件 [`00bdef00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef00.md) · 呼出先 5件 [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bdef10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef10.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 77.57% / 新版 78.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b04f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b04fdc"
      ]
    ],
    [
      "unmatched:00b04fa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05090"
      ]
    ],
    [
      "00b050cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0506c"
      ]
    ]
  ],
  "added": [
    [
      "00b04fec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b04fdc"
      ]
    ],
    [
      "00b05068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05090"
      ]
    ],
    [
      "00b050cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05134"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04e9c.md#insn-00b04f24) · [`00b04f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04e9c.md#insn-00b04f98) · [`00b04fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b04/00b04e9c.md#insn-00b04fa0)
- 新版 [`00b05060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04f64.md#insn-00b05060)

~~~diff
- 00b04f24 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b04f24 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b04f24 bytes 88ffffb5
- 00b04f98 ["BRANCH", null, ["local:b22:8"]]
+ 00b05060 ["BRANCH", null, ["local:b25:8"]]
- 00b04f98 bytes 0d000014
+ 00b05060 bytes 0d000014
- 00b04fa0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b04fa0 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 00b04fa0 bytes 480100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-265aee57ebfc9a7fc4e11156df74e71a"></a>

### [`00b052c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b052c8.md) → [`00b05390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05390.md) _ZN8firebase5MutexC2ENS0_4ModeE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bddd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md) · 呼出先 6件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bdeed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeed0.md) [`00bdeee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeee0.md) [`00bdeef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdeef0.md)
- 新版 呼出元 2件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdef80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef80.md) [`00bdef90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef90.md) [`00bdefa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefa0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.70% / 新版 61.70%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b052cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b052d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b052d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b052cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b052d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b052d4",
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
      "00b05394",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b05398",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b0539c",
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

- 旧版 [`00b052cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b052c8.md#insn-00b052cc) · [`00b052d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b052c8.md#insn-00b052d0) · [`00b052d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b052c8.md#insn-00b052d4)

~~~diff
- 00b052cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b052cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b052cc bytes f50b00f9
- 00b052d0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b052d0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b052d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b052d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b052d0 bytes f44f02a9
- 00b052d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b052d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b052d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b052d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b052d4 bytes fd7b03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8e041a052b28c5af2f977eb8803f15"></a>

### [`00b05404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05404.md) → [`00b054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054cc.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16Clas

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
      "site": "00b05430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b054f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b054e0",
      "incomplete_value": true,
      "site": "00b054e0",
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
      "definition_site": "00b05418",
      "incomplete_value": true,
      "site": "00b05418",
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
      "00b054dc",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05424",
      "PARAM",
      [
        "storage",
        "002a6114",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b05428",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b054dc",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b054ec",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b054f0",
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

- 旧版 [`00b05418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05404.md#insn-00b05418) · [`00b05428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05404.md#insn-00b05428) · [`00b05430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05404.md#insn-00b05430)
- 新版 [`00b054e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054cc.md#insn-00b054e0)

~~~diff
- 00b05418 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05418 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b054e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b054e0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b05418 bytes e80000b5
+ 00b054e0 bytes e80000b5
- 00b05428 ["INT_ADD", "register:40f0:8", ["const:b05428:8", "const:4:8"]]
- 00b05428 ["CALL", null, ["callee:00bde040:8"]]
- 00b05428 bytes da620394
- 00b05430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00b05430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05430 bytes 604a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82597ef4667dd57d16876f4d26d5e174"></a>

### [`00b05444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05444.md) → [`00b0550c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b05538",
      "incomplete_value": true,
      "site": "00b05538",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05470",
      "incomplete_value": true,
      "site": "00b05470",
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
            "const:c90:8"
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
      "definition_site": "00b05520",
      "incomplete_value": true,
      "site": "00b05520",
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
      "definition_site": "00b05458",
      "incomplete_value": true,
      "site": "00b05458",
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
      "definition_site": "00b05528",
      "incomplete_value": false,
      "site": "00b05530",
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
            "const:10d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05460",
      "incomplete_value": false,
      "site": "00b05468",
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
            "const:114:8"
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
      "00b0551c",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05528",
      "PARAM",
      [
        "storage",
        "002a6114",
        null,
        "string"
      ]
    ],
    [
      "00b05538",
      "WRITE",
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
      "00b0551c",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05528",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b05538",
      "WRITE",
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

- 旧版 [`00b05468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05444.md#insn-00b05468) · [`00b05470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05444.md#insn-00b05470) · [`00b05454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05444.md#insn-00b05454)
- 新版 [`00b05530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md#insn-00b05530) · [`00b05538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md#insn-00b05538) · [`00b0551c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md#insn-00b0551c)

~~~diff
- 00b05468 ["INT_ADD", "register:40f0:8", ["const:b05468:8", "const:4:8"]]
- 00b05468 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05530 ["INT_ADD", "register:40f0:8", ["const:b05530:8", "const:4:8"]]
+ 00b05530 ["CALL", null, ["callee:00bde040:8"]]
- 00b05468 bytes ca620394
+ 00b05530 bytes c4620394
- 00b05470 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00b05470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
+ 00b05538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05470 bytes 604a06f9
+ 00b05538 bytes 60aa06f9
- 00b05454 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00b05454 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0551c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
+ 00b0551c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05454 bytes 684a46f9
+ 00b0551c bytes 68aa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e0aa70348c8c8f185ff075cf5e71b0"></a>

### [`00b05484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05484.md) → [`00b0554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0554c.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00b054b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b0557c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b05560",
      "incomplete_value": true,
      "site": "00b05560",
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
      "definition_site": "00b05498",
      "incomplete_value": true,
      "site": "00b05498",
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
      "00b0555c",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b054a4",
      "PARAM",
      [
        "storage",
        "002a6114",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b054ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b0555c",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0556c",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b05574",
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

- 旧版 [`00b05498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05484.md#insn-00b05498) · [`00b054ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05484.md#insn-00b054ac) · [`00b054b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05484.md#insn-00b054b4)
- 新版 [`00b05560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0554c.md#insn-00b05560)

~~~diff
- 00b05498 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05498 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b05560 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b05560 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b05498 bytes 080100b5
+ 00b05560 bytes 080100b5
- 00b054ac ["INT_ADD", "register:40f0:8", ["const:b054ac:8", "const:4:8"]]
- 00b054ac ["CALL", null, ["callee:00bde040:8"]]
- 00b054ac bytes b9620394
- 00b054b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00b054b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b054b4 bytes 604a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-400b6da28de6121aec78ffed3890eef0"></a>

### [`00b054c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b054c8.md) → [`00b05590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b054f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b055c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b055a4",
      "incomplete_value": true,
      "site": "00b055a4",
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
      "definition_site": "00b054dc",
      "incomplete_value": true,
      "site": "00b054dc",
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
      "00b055a0",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b054e4",
      "PARAM",
      [
        "storage",
        "002a6114",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b054f8",
      "WRITE",
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
      "00b055a0",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b055ac",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b055c0",
      "WRITE",
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

- 旧版 [`00b054dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b054c8.md#insn-00b054dc) · [`00b054f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b054c8.md#insn-00b054f0) · [`00b054f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b054c8.md#insn-00b054f8)
- 新版 [`00b055a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md#insn-00b055a4) · [`00b055b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md#insn-00b055b8)

~~~diff
- 00b054dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b054dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b055a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b055a4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b054dc bytes 080100b5
+ 00b055a4 bytes 080100b5
- 00b054f0 ["INT_ADD", "register:40f0:8", ["const:b054f0:8", "const:4:8"]]
- 00b054f0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b055b8 ["INT_ADD", "register:40f0:8", ["const:b055b8:8", "const:4:8"]]
+ 00b055b8 ["CALL", null, ["callee:00bde040:8"]]
- 00b054f0 bytes a8620394
+ 00b055b8 bytes a2620394
- 00b054f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c90:8"]]
- 00b054f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b054f8 bytes 604a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b861314dd2ea226229db9049b624cdaa"></a>

### [`00b05518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05518.md) → [`00b055e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md) _ZN8firebase3app15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b05638"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05614",
      "incomplete_value": true,
      "site": "00b05620",
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0554c",
      "incomplete_value": true,
      "site": "00b05558",
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
                "const:c90:8"
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
      "00b055f4",
      "READ",
      [
        "storage",
        "010a0c98",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b0554c",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05570",
      "WRITE",
      [
        "storage",
        "010a0c98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b055f4",
      "READ",
      [
        "storage",
        "010a0d58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05614",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05638",
      "WRITE",
      [
        "storage",
        "010a0d58",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05518.md#insn-00b05558) · [`00b05570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05518.md#insn-00b05570)
- 新版 [`00b05620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md#insn-00b05620) · [`00b05638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md#insn-00b05638)

~~~diff
- 00b05558 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05558 ["INT_ADD", "register:40f0:8", ["const:b05558:8", "const:4:8"]]
- 00b05558 ["CALLIND", null, ["register:0:8"]]
+ 00b05620 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05620 ["INT_ADD", "register:40f0:8", ["const:b05620:8", "const:4:8"]]
+ 00b05620 ["CALLIND", null, ["register:0:8"]]
- 00b05558 bytes 00013fd6
+ 00b05620 bytes 00013fd6
- 00b05570 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05570 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c98:8"]]
- 00b05570 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05570 bytes a0623239
+ 00b05638 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b05638 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d58:8"]]
+ 00b05638 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b05638 bytes a0623539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5be4c2652a7de381cdcbb28e0124ea0"></a>

### [`00b05584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05584.md) → [`00b0564c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0564c.md) _ZN8firebase3app12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05588"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05584",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05588",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0558c",
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
      "00b0564c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b05650",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05654",
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

- 旧版 [`00b05584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05584.md#insn-00b05584) · [`00b05588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05584.md#insn-00b05588) · [`00b0558c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05584.md#insn-00b0558c)

~~~diff
- 00b05584 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b05584 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05584 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05584 bytes f50f1df8
- 00b05588 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05588 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05588 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05588 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05588 bytes f44f01a9
- 00b0558c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0558c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0558c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b0558c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0558c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0156db780807984d1c956ba066e5a36"></a>

### [`00b055f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b055f4.md) → [`00b056bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md) _ZN8firebase3app14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination

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
      "definition_site": "00b056fc",
      "incomplete_value": true,
      "site": "00b056fc",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05634",
      "incomplete_value": true,
      "site": "00b05634",
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
            "const:c90:8"
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
      "definition_site": "00b056d8",
      "incomplete_value": true,
      "site": "00b056d8",
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
      "definition_site": "00b05610",
      "incomplete_value": true,
      "site": "00b05610",
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
      "definition_site": "00b056e0",
      "incomplete_value": false,
      "site": "00b056f4",
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
            "const:10d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05618",
      "incomplete_value": false,
      "site": "00b0562c",
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
            "const:114:8"
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
      "00b056d0",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b056e0",
      "PARAM",
      [
        "storage",
        "002a6114",
        null,
        "string"
      ]
    ],
    [
      "00b056fc",
      "WRITE",
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
      "00b056d0",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b056e0",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b056fc",
      "WRITE",
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

- 旧版 [`00b0562c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b055f4.md#insn-00b0562c) · [`00b05634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b055f4.md#insn-00b05634) · [`00b05608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b055f4.md#insn-00b05608)
- 新版 [`00b056f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md#insn-00b056f4) · [`00b056fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md#insn-00b056fc) · [`00b056d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md#insn-00b056d0)

~~~diff
- 00b0562c ["INT_ADD", "register:40f0:8", ["const:b0562c:8", "const:4:8"]]
- 00b0562c ["CALL", null, ["callee:00bde040:8"]]
+ 00b056f4 ["INT_ADD", "register:40f0:8", ["const:b056f4:8", "const:4:8"]]
+ 00b056f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b0562c bytes 59620394
+ 00b056f4 bytes 53620394
- 00b05634 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00b05634 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b056fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
+ 00b056fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05634 bytes 804a06f9
+ 00b056fc bytes 80aa06f9
- 00b05608 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00b05608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b056d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
+ 00b056d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05608 bytes 814a46f9
+ 00b056d0 bytes 81aa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fab0febfff09a36f4705e50f4587064"></a>

### [`00b05664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05664.md) → [`00b0572c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md) _ZN8firebase3app11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b05748",
      "incomplete_value": false,
      "site": "00b0574c",
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
      "definition_site": "00b05680",
      "incomplete_value": false,
      "site": "00b05684",
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
      "definition_site": "00b05758",
      "incomplete_value": true,
      "site": "00b05764",
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
      "definition_site": "00b05690",
      "incomplete_value": true,
      "site": "00b0569c",
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
      "00b05748",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b05758",
      "DATA",
      [
        "storage",
        "010a0ca0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05748",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b05758",
      "DATA",
      [
        "storage",
        "010a0d60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05664.md#insn-00b05684) · [`00b05680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05664.md#insn-00b05680) · [`00b0568c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05664.md#insn-00b0568c)
- 新版 [`00b0574c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md#insn-00b0574c) · [`00b05748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md#insn-00b05748) · [`00b05754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md#insn-00b05754)

~~~diff
- 00b05684 ["INT_ADD", "register:40f0:8", ["const:b05684:8", "const:4:8"]]
- 00b05684 ["CALL", null, ["callee:00bde130:8"]]
+ 00b0574c ["INT_ADD", "register:40f0:8", ["const:b0574c:8", "const:4:8"]]
+ 00b0574c ["CALL", null, ["callee:00bde130:8"]]
- 00b05684 bytes 7f620394
+ 00b0574c bytes 79620394
- 00b05680 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b05680 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05680 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05680 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05748 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b05748 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05748 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05748 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05680 bytes 001c1591
+ 00b05748 bytes 00501791
- 00b0568c ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00b0568c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0568c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0568c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05754 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00b05754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0568c bytes 08813291
+ 00b05754 bytes 08813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d6b66b634538314733767e355789f44"></a>

### [`00b056a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b056a0.md) → [`00b05768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05768.md) _ZN8firebase3app13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b056e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b057a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b056bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b056b4",
      "READ",
      [
        "storage",
        "010a0c90",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b056bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b057ac"
      ]
    ],
    [
      "unmatched:00b056c4",
      "PARAM",
      [
        "storage",
        "002a6114",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0577c",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05784",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b057ac"
      ]
    ],
    [
      "00b0578c",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b056bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b056a0.md#insn-00b056bc) · [`00b056d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b056a0.md#insn-00b056d8) · [`00b056e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b056a0.md#insn-00b056e0)
- 新版 [`00b057a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05768.md#insn-00b057a0)

~~~diff
- 00b056bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b056bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b056bc bytes 410100b5
- 00b056d8 ["INT_ADD", "register:40f0:8", ["const:b056d8:8", "const:4:8"]]
- 00b056d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b057a0 ["INT_ADD", "register:40f0:8", ["const:b057a0:8", "const:4:8"]]
+ 00b057a0 ["CALL", null, ["callee:00bde040:8"]]
- 00b056d8 bytes 2e620394
+ 00b057a0 bytes 28620394
- 00b056e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00b056e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b056e0 bytes 804a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08cd946cb0ccc1c83debead4a93e04ff"></a>

### [`00b0578c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0578c.md) → [`00b05854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05854.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b057b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b05880"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b05868",
      "incomplete_value": true,
      "site": "00b05868",
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
      "definition_site": "00b057a0",
      "incomplete_value": true,
      "site": "00b057a0",
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
      "00b05864",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b057a8",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b057b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b05864",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05870",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b05878",
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

- 旧版 [`00b057a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0578c.md#insn-00b057a0) · [`00b057b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0578c.md#insn-00b057b0) · [`00b057b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0578c.md#insn-00b057b8)
- 新版 [`00b05868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05854.md#insn-00b05868)

~~~diff
- 00b057a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b057a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b05868 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b05868 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b057a0 bytes e80000b5
+ 00b05868 bytes e80000b5
- 00b057b0 ["INT_ADD", "register:40f0:8", ["const:b057b0:8", "const:4:8"]]
- 00b057b0 ["CALL", null, ["callee:00bde040:8"]]
- 00b057b0 bytes f8610394
- 00b057b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b057b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b057b8 bytes 607a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aafdb3a317ad3088916cee84f2d0336"></a>

### [`00b057cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b057cc.md) → [`00b05894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05894.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00b057fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b058c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b058a8",
      "incomplete_value": true,
      "site": "00b058a8",
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
      "definition_site": "00b057e0",
      "incomplete_value": true,
      "site": "00b057e0",
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
      "00b058a4",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b058a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b05800"
      ]
    ],
    [
      "unmatched:00b057ec",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b058a4",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b058a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b058c8"
      ]
    ],
    [
      "00b058b4",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b057e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b057cc.md#insn-00b057e0) · [`00b057f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b057cc.md#insn-00b057f4) · [`00b057fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b057cc.md#insn-00b057fc)
- 新版 [`00b058a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05894.md#insn-00b058a8)

~~~diff
- 00b057e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b057e0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b058a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b058a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b057e0 bytes 080100b5
+ 00b058a8 bytes 080100b5
- 00b057f4 ["INT_ADD", "register:40f0:8", ["const:b057f4:8", "const:4:8"]]
- 00b057f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b057f4 bytes e7610394
- 00b057fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
- 00b057fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b057fc bytes 607a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17023dfb99348f9ca9d2c6ed4bc96df1"></a>

### [`00b05810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05810.md) → [`00b058d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b058d8.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b05810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05814",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b058e8",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b058d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b058dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b058e8",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05810.md#insn-00b05810) · [`00b05814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05810.md#insn-00b05814) · [`00b05824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05810.md#insn-00b05824)
- 新版 [`00b058ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b058d8.md#insn-00b058ec)

~~~diff
- 00b05810 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b05810 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b05810 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05810 bytes f30f1ef8
- 00b05814 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05814 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05814 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05814 bytes fd7b01a9
- 00b05824 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05824 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b058ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b058ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b05824 bytes 080100b5
+ 00b058ec bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcedece890834950d30e5c215eb4c1d5"></a>

### [`00b05860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05860.md) → [`00b05928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md) _ZN8firebase15options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b05980",
      "incomplete_value": true,
      "site": "00b05980",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b058b8",
      "incomplete_value": true,
      "site": "00b058b8",
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
            "const:cf8:8"
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
      "definition_site": "00b0595c",
      "incomplete_value": true,
      "site": "00b05968",
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05894",
      "incomplete_value": true,
      "site": "00b058a0",
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
                "const:cf0:8"
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
      "00b0593c",
      "READ",
      [
        "storage",
        "010a0cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b0595c",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05980",
      "WRITE",
      [
        "storage",
        "010a0cf8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b0593c",
      "READ",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b0595c",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05980",
      "WRITE",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b058a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05860.md#insn-00b058a0) · [`00b058b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05860.md#insn-00b058b8) · [`00b05874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05860.md#insn-00b05874)
- 新版 [`00b05968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md#insn-00b05968) · [`00b05980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md#insn-00b05980) · [`00b0593c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md#insn-00b0593c)

~~~diff
- 00b058a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b058a0 ["INT_ADD", "register:40f0:8", ["const:b058a0:8", "const:4:8"]]
- 00b058a0 ["CALLIND", null, ["register:0:8"]]
+ 00b05968 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05968 ["INT_ADD", "register:40f0:8", ["const:b05968:8", "const:4:8"]]
+ 00b05968 ["CALLIND", null, ["register:0:8"]]
- 00b058a0 bytes 00013fd6
+ 00b05968 bytes 00013fd6
- 00b058b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b058b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cf8:8"]]
- 00b058b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b05980 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b05980 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:db8:8"]]
+ 00b05980 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b058b8 bytes a0e23339
+ 00b05980 bytes a0e23639
- 00b05874 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cf8:8"]]
- 00b05874 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b05874 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b0593c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db8:8"]]
+ 00b0593c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b0593c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b05874 bytes a8e27339
+ 00b0593c bytes a8e27639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e1c36b79009564d254e4d5aab7da47"></a>

### [`00b058cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b058cc.md) → [`00b05994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05994.md) _ZN8firebase15options_builder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b05908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b059d0"
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
      "00b059a8",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b059b4",
      "READ",
      [
        "storage",
        "010a0cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b059bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0590c"
      ]
    ]
  ],
  "added": [
    [
      "00b059a8",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b059b4",
      "READ",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b059bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b059d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b058e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b058cc.md#insn-00b058e4) · [`00b05908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b058cc.md#insn-00b05908) · [`00b05910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b058cc.md#insn-00b05910)
- 新版 [`00b059ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05994.md#insn-00b059ac)

~~~diff
- 00b058e4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b058e4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b059ac ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b059ac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b058e4 bytes 410200b4
+ 00b059ac bytes 410200b4
- 00b05908 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05908 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05908 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cf8:8"]]
- 00b05908 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05908 bytes bfe23339
- 00b05910 ["INT_ADD", "register:40f0:8", ["const:b05910:8", "const:4:8"]]
- 00b05910 ["CALL", null, ["callee:00bde090:8"]]
- 00b05910 bytes b4610394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f046cb60bae35910fdf6bc406096f13"></a>

### [`00b0593c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0593c.md) → [`00b05a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a04.md) _ZN8firebase15options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b0597c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b05a44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05958"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05950",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05958",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05a48"
      ]
    ],
    [
      "unmatched:00b05960",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b05a18",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05a20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05a48"
      ]
    ],
    [
      "00b05a28",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0593c.md#insn-00b05958) · [`00b05974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0593c.md#insn-00b05974) · [`00b0597c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b0593c.md#insn-00b0597c)
- 新版 [`00b05a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a04.md#insn-00b05a3c)

~~~diff
- 00b05958 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05958 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b05958 bytes 410100b5
- 00b05974 ["INT_ADD", "register:40f0:8", ["const:b05974:8", "const:4:8"]]
- 00b05974 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05a3c ["INT_ADD", "register:40f0:8", ["const:b05a3c:8", "const:4:8"]]
+ 00b05a3c ["CALL", null, ["callee:00bde040:8"]]
- 00b05974 bytes 87610394
+ 00b05a3c bytes 81610394
- 00b0597c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b0597c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b0597c bytes 807a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-533b341aec21592e1ba46a20c3d2ad53"></a>

### [`00b059ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059ac.md) → [`00b05a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md) _ZN8firebase15options_builder11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b05a90",
      "incomplete_value": false,
      "site": "00b05a94",
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
      "definition_site": "00b059c8",
      "incomplete_value": false,
      "site": "00b059cc",
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
      "definition_site": "00b05aa0",
      "incomplete_value": true,
      "site": "00b05aac",
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
      "definition_site": "00b059d8",
      "incomplete_value": true,
      "site": "00b059e4",
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
      "00b05a90",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b05aa0",
      "DATA",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05a90",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b05aa0",
      "DATA",
      [
        "storage",
        "010a0dc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b059cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059ac.md#insn-00b059cc) · [`00b059c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059ac.md#insn-00b059c8) · [`00b059d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059ac.md#insn-00b059d4)
- 新版 [`00b05a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md#insn-00b05a94) · [`00b05a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md#insn-00b05a90) · [`00b05a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md#insn-00b05a9c)

~~~diff
- 00b059cc ["INT_ADD", "register:40f0:8", ["const:b059cc:8", "const:4:8"]]
- 00b059cc ["CALL", null, ["callee:00bde130:8"]]
+ 00b05a94 ["INT_ADD", "register:40f0:8", ["const:b05a94:8", "const:4:8"]]
+ 00b05a94 ["CALL", null, ["callee:00bde130:8"]]
- 00b059cc bytes ad610394
+ 00b05a94 bytes a7610394
- 00b059c8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b059c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b059c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b059c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05a90 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b05a90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05a90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05a90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b059c8 bytes 001c1591
+ 00b05a90 bytes 00501791
- 00b059d4 ["COPY", "tmp:0:8", ["const:d00:8"]]
- 00b059d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b059d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b059d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05a9c ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 00b05a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b059d4 bytes 08013491
+ 00b05a9c bytes 08013791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd178697a539c7a5c50f28a0b67e75f"></a>

### [`00b059e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059e8.md) → [`00b05ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ab0.md) _ZN8firebase15options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b05a28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b05af0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05a04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b059fc",
      "READ",
      [
        "storage",
        "010a0cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05a04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05af4"
      ]
    ],
    [
      "unmatched:00b05a0c",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b05ac4",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b05af4"
      ]
    ],
    [
      "00b05ad4",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059e8.md#insn-00b05a04) · [`00b05a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059e8.md#insn-00b05a20) · [`00b05a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b059e8.md#insn-00b05a28)
- 新版 [`00b05ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ab0.md#insn-00b05ae8)

~~~diff
- 00b05a04 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b05a04 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b05a04 bytes 410100b5
- 00b05a20 ["INT_ADD", "register:40f0:8", ["const:b05a20:8", "const:4:8"]]
- 00b05a20 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05ae8 ["INT_ADD", "register:40f0:8", ["const:b05ae8:8", "const:4:8"]]
+ 00b05ae8 ["CALL", null, ["callee:00bde040:8"]]
- 00b05a20 bytes 5c610394
+ 00b05ae8 bytes 56610394
- 00b05a28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
- 00b05a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05a28 bytes 807a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c18a0b9b250d3bb348a21ae150db842c"></a>

### [`00b05a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05a94.md) → [`00b05b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16

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
      "definition_site": "00b05b88",
      "incomplete_value": true,
      "site": "00b05b88",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ac0",
      "incomplete_value": true,
      "site": "00b05ac0",
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
            "const:d48:8"
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
      "definition_site": "00b05b70",
      "incomplete_value": true,
      "site": "00b05b70",
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
      "definition_site": "00b05aa8",
      "incomplete_value": true,
      "site": "00b05aa8",
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
      "definition_site": "00b05b7c",
      "incomplete_value": false,
      "site": "00b05b80",
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
      "definition_site": "00b05ab4",
      "incomplete_value": false,
      "site": "00b05ab8",
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
      "00b05b6c",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05b7c",
      "PARAM",
      [
        "storage",
        "002a4f06",
        null,
        "string"
      ]
    ],
    [
      "00b05b88",
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
      "00b05b6c",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05b7c",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05b88",
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

- 旧版 [`00b05ab8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05a94.md#insn-00b05ab8) · [`00b05ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05a94.md#insn-00b05ac0) · [`00b05aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05a94.md#insn-00b05aa4)
- 新版 [`00b05b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md#insn-00b05b80) · [`00b05b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md#insn-00b05b88) · [`00b05b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md#insn-00b05b6c)

~~~diff
- 00b05ab8 ["INT_ADD", "register:40f0:8", ["const:b05ab8:8", "const:4:8"]]
- 00b05ab8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b05b80 ["INT_ADD", "register:40f0:8", ["const:b05b80:8", "const:4:8"]]
+ 00b05b80 ["CALL", null, ["callee:00bde040:8"]]
- 00b05ab8 bytes 36610394
+ 00b05b80 bytes 30610394
- 00b05ac0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b05ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05b88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
+ 00b05b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05ac0 bytes 60a606f9
+ 00b05b88 bytes 600607f9
- 00b05aa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b05aa4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
+ 00b05b6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05aa4 bytes 68a646f9
+ 00b05b6c bytes 680647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4909b62e573f0441f04d4685349db990"></a>

### [`00b05ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ad4.md) → [`00b05b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b9c.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

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
      "site": "00b05ad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05ad8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05ad4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05bac",
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
      "00b05b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05bac",
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

- 旧版 [`00b05ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ad4.md#insn-00b05ad4) · [`00b05ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ad4.md#insn-00b05ad8) · [`00b05ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05ad4.md#insn-00b05ae8)
- 新版 [`00b05bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b9c.md#insn-00b05bb0)

~~~diff
- 00b05ad4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b05ad4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b05ad4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05ad4 bytes f30f1ef8
- 00b05ad8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05ad8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05ad8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05ad8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05ad8 bytes fd7b01a9
- 00b05ae8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05ae8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b05bb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b05bb0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b05ae8 bytes e80000b5
+ 00b05bb0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb0d70f0129f2ec43653617f6f421fe2"></a>

### [`00b05b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b14.md) → [`00b05bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05bdc.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "site": "00b05b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b05c0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b05bf0",
      "incomplete_value": true,
      "site": "00b05bf0",
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
      "definition_site": "00b05b28",
      "incomplete_value": true,
      "site": "00b05b28",
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
      "00b05bec",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b05b34",
      "PARAM",
      [
        "storage",
        "002a4f06",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b05b3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b05bec",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05bfc",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05c04",
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

- 旧版 [`00b05b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b14.md#insn-00b05b28) · [`00b05b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b14.md#insn-00b05b3c) · [`00b05b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b05/00b05b14.md#insn-00b05b44)
- 新版 [`00b05bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05bdc.md#insn-00b05bf0)

~~~diff
- 00b05b28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b05b28 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b05bf0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b05bf0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b05b28 bytes 080100b5
+ 00b05bf0 bytes 080100b5
- 00b05b3c ["INT_ADD", "register:40f0:8", ["const:b05b3c:8", "const:4:8"]]
- 00b05b3c ["CALL", null, ["callee:00bde040:8"]]
- 00b05b3c bytes 15610394
- 00b05b44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
- 00b05b44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05b44 bytes 60a606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

