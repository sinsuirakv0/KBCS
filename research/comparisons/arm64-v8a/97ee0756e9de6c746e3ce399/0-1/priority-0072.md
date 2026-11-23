# v15.7.2 → v15.7.3 · 最優先の変更候補 (72)

[一覧の目次](README.md)

<a id="compare-46742fff696bbfe4f377c6f4a577294a"></a>

### [`00b66f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f50.md) → [`00b67018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67018.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b66f50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66f54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66f54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b67028",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67018",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6701c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b67028",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f50.md#insn-00b66f50) · [`00b66f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f50.md#insn-00b66f54) · [`00b66f64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f50.md#insn-00b66f64)
- 新版 [`00b6702c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67018.md#insn-00b6702c)

~~~diff
- 00b66f50 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b66f50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b66f50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b66f50 bytes f30f1ef8
- 00b66f54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66f54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66f54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b66f54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66f54 bytes fd7b01a9
- 00b66f64 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b66f64 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b6702c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6702c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66f64 bytes 080100b5
+ 00b6702c bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7acddfc64d54cc4279de11c902362192"></a>

### [`00b6707c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6707c.md) → [`00b67144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67144.md) _ZN8firebase4auth8timeunit14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00b670bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b67184"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67098"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b67090",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b67098",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67188"
      ]
    ],
    [
      "unmatched:00b670a0",
      "PARAM",
      [
        "storage",
        "002a3027",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b67158",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67188"
      ]
    ],
    [
      "00b67168",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6707c.md#insn-00b67098) · [`00b670b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6707c.md#insn-00b670b4) · [`00b670bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6707c.md#insn-00b670bc)
- 新版 [`00b6717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67144.md#insn-00b6717c)

~~~diff
- 00b67098 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b67098 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b67098 bytes 410100b5
- 00b670b4 ["INT_ADD", "register:40f0:8", ["const:b670b4:8", "const:4:8"]]
- 00b670b4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6717c ["INT_ADD", "register:40f0:8", ["const:b6717c:8", "const:4:8"]]
+ 00b6717c ["CALL", null, ["callee:00bde040:8"]]
- 00b670b4 bytes b7db0194
+ 00b6717c bytes b1db0194
- 00b670bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b670bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b670bc bytes 80aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a7f1da166dc269ca4de3fe2f3ef4621"></a>

### [`00b67128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67128.md) → [`00b671f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671f0.md) _ZN8firebase4auth8timeunit13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b67168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b67230"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67144"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6713c",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b67144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67234"
      ]
    ],
    [
      "unmatched:00b6714c",
      "PARAM",
      [
        "storage",
        "002a3027",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b67204",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6720c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67234"
      ]
    ],
    [
      "00b67214",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67128.md#insn-00b67144) · [`00b67160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67128.md#insn-00b67160) · [`00b67168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67128.md#insn-00b67168)
- 新版 [`00b67228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b671f0.md#insn-00b67228)

~~~diff
- 00b67144 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b67144 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b67144 bytes 410100b5
- 00b67160 ["INT_ADD", "register:40f0:8", ["const:b67160:8", "const:4:8"]]
- 00b67160 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67228 ["INT_ADD", "register:40f0:8", ["const:b67228:8", "const:4:8"]]
+ 00b67228 ["CALL", null, ["callee:00bde040:8"]]
- 00b67160 bytes 8cdb0194
+ 00b67228 bytes 86db0194
- 00b67168 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00b67168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67168 bytes 80aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc5a313022a4e050997f7193a192654"></a>

### [`00b67198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67198.md) → [`00b67260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md) _ZN8firebase4auth8timeunit10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6727c",
      "incomplete_value": false,
      "site": "00b67280",
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
      "definition_site": "00b671b4",
      "incomplete_value": false,
      "site": "00b671b8",
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
      "definition_site": "00b6728c",
      "incomplete_value": true,
      "site": "00b67298",
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
      "definition_site": "00b671c4",
      "incomplete_value": true,
      "site": "00b671d0",
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
      "00b6727c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6728c",
      "DATA",
      [
        "storage",
        "010a1768",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6727c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6728c",
      "DATA",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b671b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67198.md#insn-00b671b8) · [`00b671b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67198.md#insn-00b671b4) · [`00b671c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67198.md#insn-00b671c0)
- 新版 [`00b67280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md#insn-00b67280) · [`00b6727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md#insn-00b6727c) · [`00b67288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67260.md#insn-00b67288)

~~~diff
- 00b671b8 ["INT_ADD", "register:40f0:8", ["const:b671b8:8", "const:4:8"]]
- 00b671b8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b67280 ["INT_ADD", "register:40f0:8", ["const:b67280:8", "const:4:8"]]
+ 00b67280 ["CALL", null, ["callee:00bde130:8"]]
- 00b671b8 bytes b2db0194
+ 00b67280 bytes acdb0194
- 00b671b4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b671b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b671b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b671b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6727c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b6727c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6727c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6727c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b671b4 bytes 00c81791
+ 00b6727c bytes 00fc1991
- 00b671c0 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00b671c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b671c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b671c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67288 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00b67288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b671c0 bytes 08a11d91
+ 00b67288 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6869b886144ddfcdcfebd66c0ffca229"></a>

### [`00b67214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67214.md) → [`00b672dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b672dc.md) _ZN8firebase4auth26phone_auth_options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67218"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67218"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b67214",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b67218",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b672ec",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b672dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b672e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b672ec",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67214.md#insn-00b67214) · [`00b67218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67214.md#insn-00b67218) · [`00b67228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67214.md#insn-00b67228)
- 新版 [`00b672f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b672dc.md#insn-00b672f0)

~~~diff
- 00b67214 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b67214 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b67214 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b67214 bytes f30f1ef8
- 00b67218 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b67218 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b67218 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b67218 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b67218 bytes fd7b01a9
- 00b67228 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b67228 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b672f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b672f0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b67228 bytes e80000b5
+ 00b672f0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7037e960283aef7d9bb4e46a031ef4d"></a>

### [`00b67254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67254.md) → [`00b6731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6734c",
      "incomplete_value": true,
      "site": "00b6734c",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67284",
      "incomplete_value": true,
      "site": "00b67284",
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
            "const:770:8"
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
      "definition_site": "00b67330",
      "incomplete_value": true,
      "site": "00b67330",
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
      "definition_site": "00b67268",
      "incomplete_value": true,
      "site": "00b67268",
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
        "00b67268"
      ],
      [
        "FALL_THROUGH",
        "00b67330"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67330",
      "incomplete_value": true,
      "site": "00b6734c",
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
      "definition_site": "00b67268",
      "incomplete_value": true,
      "site": "00b67284",
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
      "00b6732c",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6734c",
      "WRITE",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6732c",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6734c",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67254.md#insn-00b67284) · [`00b67264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67254.md#insn-00b67264) · [`00b6727c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67254.md#insn-00b6727c)
- 新版 [`00b6734c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md#insn-00b6734c) · [`00b6732c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md#insn-00b6732c) · [`00b67344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6731c.md#insn-00b67344)

~~~diff
- 00b67284 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00b67284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6734c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b6734c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67284 bytes 60ba03f9
+ 00b6734c bytes 601a04f9
- 00b67264 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00b67264 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6732c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b6732c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67264 bytes 68ba43f9
+ 00b6732c bytes 681a44f9
- 00b6727c ["INT_ADD", "register:40f0:8", ["const:b6727c:8", "const:4:8"]]
- 00b6727c ["CALL", null, ["callee:00bde040:8"]]
+ 00b67344 ["INT_ADD", "register:40f0:8", ["const:b67344:8", "const:4:8"]]
+ 00b67344 ["CALL", null, ["callee:00bde040:8"]]
- 00b6727c bytes 45db0194
+ 00b67344 bytes 3fdb0194
~~~


<a id="compare-3baa4732520f0c501e62ce3547440589"></a>

### [`00b67298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67298.md) → [`00b67360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67360.md) _ZN8firebase4auth26phone_auth_options_builder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b672c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b67390"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b67374",
      "incomplete_value": true,
      "site": "00b67374",
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
      "definition_site": "00b672ac",
      "incomplete_value": true,
      "site": "00b672ac",
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
      "00b67370",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b672cc"
      ]
    ],
    [
      "unmatched:00b672c8",
      "WRITE",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67370",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67394"
      ]
    ],
    [
      "00b67390",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b672c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67298.md#insn-00b672c8) · [`00b672d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67298.md#insn-00b672d8)
- 新版 [`00b67390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67360.md#insn-00b67390)

~~~diff
- 00b672c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:770:8"]]
- 00b672c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b672c8 bytes 60ba03f9
- 00b672d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b672d8 ["RETURN", null, ["register:0:8"]]
- 00b672d8 bytes c0035fd6
+ 00b67390 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
+ 00b67390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67390 bytes 601a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d56bfa313121fce6dd5da764fb309709"></a>

### [`00b672e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672e8.md) → [`00b673b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md) _ZN8firebase4auth26phone_auth_options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67408",
      "incomplete_value": true,
      "site": "00b67408",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67340",
      "incomplete_value": true,
      "site": "00b67340",
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
            "const:778:8"
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
      "definition_site": "00b673e4",
      "incomplete_value": true,
      "site": "00b673f0",
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
                "const:10a1000:8"
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
    "old": {
      "definition_site": "00b6731c",
      "incomplete_value": true,
      "site": "00b67328",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:770:8"
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
      "00b673c4",
      "READ",
      [
        "storage",
        "010a1778",
        null,
        "undefined1"
      ]
    ],
    [
      "00b673e4",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67408",
      "WRITE",
      [
        "storage",
        "010a1778",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b673c4",
      "READ",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b673e4",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67408",
      "WRITE",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672e8.md#insn-00b67328) · [`00b67340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672e8.md#insn-00b67340) · [`00b672fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b672e8.md#insn-00b672fc)
- 新版 [`00b673f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md#insn-00b673f0) · [`00b67408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md#insn-00b67408) · [`00b673c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b673b0.md#insn-00b673c4)

~~~diff
- 00b67328 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67328 ["INT_ADD", "register:40f0:8", ["const:b67328:8", "const:4:8"]]
- 00b67328 ["CALLIND", null, ["register:0:8"]]
+ 00b673f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b673f0 ["INT_ADD", "register:40f0:8", ["const:b673f0:8", "const:4:8"]]
+ 00b673f0 ["CALLIND", null, ["register:0:8"]]
- 00b67328 bytes 00013fd6
+ 00b673f0 bytes 00013fd6
- 00b67340 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67340 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:778:8"]]
- 00b67340 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67408 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67408 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
+ 00b67408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67340 bytes a0e21d39
+ 00b67408 bytes a0e22039
- 00b672fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
- 00b672fc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b672fc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b673c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:838:8"]]
+ 00b673c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b673c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b672fc bytes a8e25d39
+ 00b673c4 bytes a8e26039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79ce090dfeaf35f022b240bce9ceca8e"></a>

### [`00b67354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67354.md) → [`00b6741c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md) _ZN8firebase4auth26phone_auth_options_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b67458",
      "incomplete_value": true,
      "site": "00b67458",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67390",
      "incomplete_value": true,
      "site": "00b67390",
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
            "const:778:8"
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
      "definition_site": "00b67478",
      "incomplete_value": true,
      "site": "00b67478",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b673b0",
      "incomplete_value": true,
      "site": "00b673b0",
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
            "const:770:8"
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
      "definition_site": "00b67434",
      "incomplete_value": true,
      "site": "00b67434",
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
      "definition_site": "00b6736c",
      "incomplete_value": true,
      "site": "00b6736c",
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
      "00b67430",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6743c",
      "READ",
      [
        "storage",
        "010a1778",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67458",
      "WRITE",
      [
        "storage",
        "010a1778",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67430",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6743c",
      "READ",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67458",
      "WRITE",
      [
        "storage",
        "010a1838",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67354.md#insn-00b67390) · [`00b673ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67354.md#insn-00b673ac) · [`00b673b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67354.md#insn-00b673b0)
- 新版 [`00b67458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md#insn-00b67458) · [`00b67474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md#insn-00b67474) · [`00b67478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6741c.md#insn-00b67478)

~~~diff
- 00b67390 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67390 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67390 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:778:8"]]
- 00b67390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67458 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67458 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67458 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
+ 00b67458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67390 bytes bfe21d39
+ 00b67458 bytes bfe22039
- 00b673ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b673ac ["INT_ADD", "register:40f0:8", ["const:b673ac:8", "const:4:8"]]
- 00b673ac ["CALLIND", null, ["register:0:8"]]
+ 00b67474 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67474 ["INT_ADD", "register:40f0:8", ["const:b67474:8", "const:4:8"]]
+ 00b67474 ["CALLIND", null, ["register:0:8"]]
- 00b673ac bytes 00013fd6
+ 00b67474 bytes 00013fd6
- 00b673b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
- 00b673b0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b673b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b67478 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b67478 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b67478 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b673b0 bytes 9fba03f9
+ 00b67478 bytes 9f1a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd63d4e7fb4ceb6f1ef74b204dfb0aa2"></a>

### [`00b673c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b673c4.md) → [`00b6748c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md) _ZN8firebase4auth26phone_auth_options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b674cc",
      "incomplete_value": true,
      "site": "00b674cc",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67404",
      "incomplete_value": true,
      "site": "00b67404",
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
            "const:770:8"
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
      "definition_site": "00b674a8",
      "incomplete_value": true,
      "site": "00b674a8",
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
      "definition_site": "00b673e0",
      "incomplete_value": true,
      "site": "00b673e0",
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
        "00b673e0"
      ],
      [
        "FALL_THROUGH",
        "00b674a8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b674a8",
      "incomplete_value": true,
      "site": "00b674cc",
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
      "definition_site": "00b673e0",
      "incomplete_value": true,
      "site": "00b67404",
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
      "00b674a0",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b674cc",
      "WRITE",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b674e0",
      "PARAM",
      [
        "storage",
        "00c123e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b674a0",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b674cc",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b674e0",
      "PARAM",
      [
        "storage",
        "00c12498",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b673c4.md#insn-00b67404) · [`00b673d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b673c4.md#insn-00b673d8) · [`00b673fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b673c4.md#insn-00b673fc)
- 新版 [`00b674cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md#insn-00b674cc) · [`00b674a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md#insn-00b674a0) · [`00b674c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6748c.md#insn-00b674c4)

~~~diff
- 00b67404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
- 00b67404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b674cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b674cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67404 bytes 80ba03f9
+ 00b674cc bytes 801a04f9
- 00b673d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
- 00b673d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b674a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b674a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b673d8 bytes 81ba43f9
+ 00b674a0 bytes 811a44f9
- 00b673fc ["INT_ADD", "register:40f0:8", ["const:b673fc:8", "const:4:8"]]
- 00b673fc ["CALL", null, ["callee:00bde040:8"]]
+ 00b674c4 ["INT_ADD", "register:40f0:8", ["const:b674c4:8", "const:4:8"]]
+ 00b674c4 ["CALL", null, ["callee:00bde040:8"]]
- 00b673fc bytes e5da0194
+ 00b674c4 bytes dfda0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd6b9ee5814bacb599c34d51c584b57"></a>

### [`00b67434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67434.md) → [`00b674fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md) _ZN8firebase4auth26phone_auth_options_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67518",
      "incomplete_value": false,
      "site": "00b6751c",
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
      "definition_site": "00b67450",
      "incomplete_value": false,
      "site": "00b67454",
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
      "definition_site": "00b67528",
      "incomplete_value": true,
      "site": "00b67534",
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
      "definition_site": "00b67460",
      "incomplete_value": true,
      "site": "00b6746c",
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
      "00b67518",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67528",
      "DATA",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67518",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67528",
      "DATA",
      [
        "storage",
        "010a1840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67434.md#insn-00b67454) · [`00b67450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67434.md#insn-00b67450) · [`00b6745c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67434.md#insn-00b6745c)
- 新版 [`00b6751c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md#insn-00b6751c) · [`00b67518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md#insn-00b67518) · [`00b67524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b674fc.md#insn-00b67524)

~~~diff
- 00b67454 ["INT_ADD", "register:40f0:8", ["const:b67454:8", "const:4:8"]]
- 00b67454 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6751c ["INT_ADD", "register:40f0:8", ["const:b6751c:8", "const:4:8"]]
+ 00b6751c ["CALL", null, ["callee:00bde130:8"]]
- 00b67454 bytes 0bdb0194
+ 00b6751c bytes 05db0194
- 00b67450 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b67450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67518 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b67518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67450 bytes 001c1591
+ 00b67518 bytes 00501791
- 00b6745c ["COPY", "tmp:0:8", ["const:780:8"]]
- 00b6745c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6745c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6745c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67524 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00b67524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6745c bytes 08011e91
+ 00b67524 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25c2dbfb8114e9c83ef2194c5dd5c0b8"></a>

### [`00b67470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67470.md) → [`00b67538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md) _ZN8firebase4auth26phone_auth_options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67578",
      "incomplete_value": true,
      "site": "00b67578",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b674b0",
      "incomplete_value": true,
      "site": "00b674b0",
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
            "const:770:8"
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
      "definition_site": "00b67554",
      "incomplete_value": true,
      "site": "00b67554",
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
      "definition_site": "00b6748c",
      "incomplete_value": true,
      "site": "00b6748c",
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
        "00b6748c"
      ],
      [
        "FALL_THROUGH",
        "00b67554"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67554",
      "incomplete_value": true,
      "site": "00b67578",
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
      "definition_site": "00b6748c",
      "incomplete_value": true,
      "site": "00b674b0",
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
      "00b6754c",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67578",
      "WRITE",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67590",
      "PARAM",
      [
        "storage",
        "010a17c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6754c",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67578",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67590",
      "PARAM",
      [
        "storage",
        "010a1880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b674b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67470.md#insn-00b674b0) · [`00b67484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67470.md#insn-00b67484) · [`00b674a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67470.md#insn-00b674a8)
- 新版 [`00b67578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md#insn-00b67578) · [`00b6754c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md#insn-00b6754c) · [`00b67570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67538.md#insn-00b67570)

~~~diff
- 00b674b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
- 00b674b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67578 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b67578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b674b0 bytes 80ba03f9
+ 00b67578 bytes 801a04f9
- 00b67484 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:770:8"]]
- 00b67484 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6754c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
+ 00b6754c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67484 bytes 81ba43f9
+ 00b6754c bytes 811a44f9
- 00b674a8 ["INT_ADD", "register:40f0:8", ["const:b674a8:8", "const:4:8"]]
- 00b674a8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67570 ["INT_ADD", "register:40f0:8", ["const:b67570:8", "const:4:8"]]
+ 00b67570 ["CALL", null, ["callee:00bde040:8"]]
- 00b674a8 bytes bada0194
+ 00b67570 bytes b4da0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0bfbae60c13db6d548c22e72f2c0d17"></a>

### [`00b674e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b674e0.md) → [`00b675a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md) _ZN8firebase4auth26phone_auth_options_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b675c4",
      "incomplete_value": false,
      "site": "00b675c8",
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
      "definition_site": "00b674fc",
      "incomplete_value": false,
      "site": "00b67500",
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
      "definition_site": "00b675d4",
      "incomplete_value": true,
      "site": "00b675e0",
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
      "definition_site": "00b6750c",
      "incomplete_value": true,
      "site": "00b67518",
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
      "00b675c4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b675d4",
      "DATA",
      [
        "storage",
        "010a17c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b675c4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b675d4",
      "DATA",
      [
        "storage",
        "010a1880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b674e0.md#insn-00b67500) · [`00b674fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b674e0.md#insn-00b674fc) · [`00b67508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b674e0.md#insn-00b67508)
- 新版 [`00b675c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md#insn-00b675c8) · [`00b675c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md#insn-00b675c4) · [`00b675d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675a8.md#insn-00b675d0)

~~~diff
- 00b67500 ["INT_ADD", "register:40f0:8", ["const:b67500:8", "const:4:8"]]
- 00b67500 ["CALL", null, ["callee:00bde130:8"]]
+ 00b675c8 ["INT_ADD", "register:40f0:8", ["const:b675c8:8", "const:4:8"]]
+ 00b675c8 ["CALL", null, ["callee:00bde130:8"]]
- 00b67500 bytes e0da0194
+ 00b675c8 bytes dada0194
- 00b674fc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b674fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b674fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b674fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b675c4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b675c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b675c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b675c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b674fc bytes 00c81791
+ 00b675c4 bytes 00fc1991
- 00b67508 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00b67508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b675d0 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00b675d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b675d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b675d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67508 bytes 08011f91
+ 00b675d0 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0659baecc5c9b8db2432ac40f9ebc121"></a>

### [`00b6751c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6751c.md) → [`00b675e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00b67610",
      "incomplete_value": true,
      "site": "00b67610",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67548",
      "incomplete_value": true,
      "site": "00b67548",
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
            "const:7c8:8"
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
      "definition_site": "00b675f8",
      "incomplete_value": true,
      "site": "00b675f8",
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
      "definition_site": "00b67530",
      "incomplete_value": true,
      "site": "00b67530",
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
      "definition_site": "00b67604",
      "incomplete_value": false,
      "site": "00b67608",
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
            "const:5f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6753c",
      "incomplete_value": false,
      "site": "00b67540",
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
            "const:56c:8"
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
      "00b675f4",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67604",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67610",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b675f4",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67604",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67610",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6751c.md#insn-00b67540) · [`00b67548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6751c.md#insn-00b67548) · [`00b6752c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6751c.md#insn-00b6752c)
- 新版 [`00b67608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md#insn-00b67608) · [`00b67610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md#insn-00b67610) · [`00b675f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b675e4.md#insn-00b675f4)

~~~diff
- 00b67540 ["INT_ADD", "register:40f0:8", ["const:b67540:8", "const:4:8"]]
- 00b67540 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67608 ["INT_ADD", "register:40f0:8", ["const:b67608:8", "const:4:8"]]
+ 00b67608 ["CALL", null, ["callee:00bde040:8"]]
- 00b67540 bytes 94da0194
+ 00b67608 bytes 8eda0194
- 00b67548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b67548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b67610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67548 bytes 60e603f9
+ 00b67610 bytes 604604f9
- 00b6752c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b6752c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b675f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b675f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6752c bytes 68e643f9
+ 00b675f4 bytes 684644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dd285b315bf7f772a178c44698ba1c5"></a>

### [`00b6755c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6755c.md) → [`00b67624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md) _ZN8firebase4auth17phoneauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00b67650",
      "incomplete_value": true,
      "site": "00b67650",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67588",
      "incomplete_value": true,
      "site": "00b67588",
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
            "const:7c8:8"
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
      "definition_site": "00b67638",
      "incomplete_value": true,
      "site": "00b67638",
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
      "definition_site": "00b67570",
      "incomplete_value": true,
      "site": "00b67570",
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
      "definition_site": "00b67640",
      "incomplete_value": false,
      "site": "00b67648",
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
            "const:5f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67578",
      "incomplete_value": false,
      "site": "00b67580",
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
            "const:56c:8"
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
      "00b67634",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67640",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67650",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67634",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67640",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67650",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6755c.md#insn-00b67580) · [`00b67588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6755c.md#insn-00b67588) · [`00b6756c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6755c.md#insn-00b6756c)
- 新版 [`00b67648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md#insn-00b67648) · [`00b67650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md#insn-00b67650) · [`00b67634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67624.md#insn-00b67634)

~~~diff
- 00b67580 ["INT_ADD", "register:40f0:8", ["const:b67580:8", "const:4:8"]]
- 00b67580 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67648 ["INT_ADD", "register:40f0:8", ["const:b67648:8", "const:4:8"]]
+ 00b67648 ["CALL", null, ["callee:00bde040:8"]]
- 00b67580 bytes 84da0194
+ 00b67648 bytes 7eda0194
- 00b67588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b67588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b67650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67588 bytes 60e603f9
+ 00b67650 bytes 604604f9
- 00b6756c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b6756c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b67634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6756c bytes 68e643f9
+ 00b67634 bytes 684644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489f19facfcafb26fdb1364ca39971d2"></a>

### [`00b6759c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6759c.md) → [`00b67664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b67694",
      "incomplete_value": true,
      "site": "00b67694",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675cc",
      "incomplete_value": true,
      "site": "00b675cc",
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
            "const:7c8:8"
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
      "definition_site": "00b67678",
      "incomplete_value": true,
      "site": "00b67678",
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
      "definition_site": "00b675b0",
      "incomplete_value": true,
      "site": "00b675b0",
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
      "definition_site": "00b67684",
      "incomplete_value": false,
      "site": "00b6768c",
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
            "const:5f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675bc",
      "incomplete_value": false,
      "site": "00b675c4",
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
            "const:56c:8"
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
      "00b67674",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67684",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67694",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67674",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67684",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67694",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b675c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6759c.md#insn-00b675c4) · [`00b675cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6759c.md#insn-00b675cc) · [`00b675ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6759c.md#insn-00b675ac)
- 新版 [`00b6768c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md#insn-00b6768c) · [`00b67694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md#insn-00b67694) · [`00b67674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67664.md#insn-00b67674)

~~~diff
- 00b675c4 ["INT_ADD", "register:40f0:8", ["const:b675c4:8", "const:4:8"]]
- 00b675c4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6768c ["INT_ADD", "register:40f0:8", ["const:b6768c:8", "const:4:8"]]
+ 00b6768c ["CALL", null, ["callee:00bde040:8"]]
- 00b675c4 bytes 73da0194
+ 00b6768c bytes 6dda0194
- 00b675cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b675cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67694 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b67694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b675cc bytes 60e603f9
+ 00b67694 bytes 604604f9
- 00b675ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b675ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67674 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b67674 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b675ac bytes 68e643f9
+ 00b67674 bytes 684644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92c4642dd88dd0f853c675fb788060a2"></a>

### [`00b675e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b675e0.md) → [`00b676a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md) _ZN8firebase4auth17phoneauthprovider10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b676d8",
      "incomplete_value": true,
      "site": "00b676d8",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67610",
      "incomplete_value": true,
      "site": "00b67610",
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
            "const:7c8:8"
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
      "definition_site": "00b676bc",
      "incomplete_value": true,
      "site": "00b676bc",
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
      "definition_site": "00b675f4",
      "incomplete_value": true,
      "site": "00b675f4",
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
      "definition_site": "00b676c4",
      "incomplete_value": false,
      "site": "00b676d0",
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
            "const:5f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b675fc",
      "incomplete_value": false,
      "site": "00b67608",
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
            "const:56c:8"
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
      "00b676b8",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b676c4",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b676d8",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b676b8",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b676c4",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b676d8",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b675e0.md#insn-00b67608) · [`00b67610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b675e0.md#insn-00b67610) · [`00b675f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b675e0.md#insn-00b675f0)
- 新版 [`00b676d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md#insn-00b676d0) · [`00b676d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md#insn-00b676d8) · [`00b676b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676a8.md#insn-00b676b8)

~~~diff
- 00b67608 ["INT_ADD", "register:40f0:8", ["const:b67608:8", "const:4:8"]]
- 00b67608 ["CALL", null, ["callee:00bde040:8"]]
+ 00b676d0 ["INT_ADD", "register:40f0:8", ["const:b676d0:8", "const:4:8"]]
+ 00b676d0 ["CALL", null, ["callee:00bde040:8"]]
- 00b67608 bytes 62da0194
+ 00b676d0 bytes 5cda0194
- 00b67610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b67610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b676d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b676d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67610 bytes 60e603f9
+ 00b676d8 bytes 604604f9
- 00b675f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c8:8"]]
- 00b675f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b676b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b676b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b675f0 bytes 68e643f9
+ 00b676b8 bytes 684644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fd76cdb617497888f0fa03c282f1fe9"></a>

### [`00b67630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67630.md) → [`00b676f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md) _ZN8firebase4auth17phoneauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67750",
      "incomplete_value": true,
      "site": "00b67750",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67688",
      "incomplete_value": true,
      "site": "00b67688",
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
            "const:7d0:8"
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
      "definition_site": "00b6772c",
      "incomplete_value": true,
      "site": "00b67738",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:888:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67664",
      "incomplete_value": true,
      "site": "00b67670",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7c8:8"
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
      "00b6770c",
      "READ",
      [
        "storage",
        "010a17d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6772c",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67750",
      "WRITE",
      [
        "storage",
        "010a17d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6770c",
      "READ",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6772c",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67750",
      "WRITE",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67630.md#insn-00b67670) · [`00b67688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67630.md#insn-00b67688) · [`00b67644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67630.md#insn-00b67644)
- 新版 [`00b67738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md#insn-00b67738) · [`00b67750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md#insn-00b67750) · [`00b6770c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b676f8.md#insn-00b6770c)

~~~diff
- 00b67670 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67670 ["INT_ADD", "register:40f0:8", ["const:b67670:8", "const:4:8"]]
- 00b67670 ["CALLIND", null, ["register:0:8"]]
+ 00b67738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67738 ["INT_ADD", "register:40f0:8", ["const:b67738:8", "const:4:8"]]
+ 00b67738 ["CALLIND", null, ["register:0:8"]]
- 00b67670 bytes 00013fd6
+ 00b67738 bytes 00013fd6
- 00b67688 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67688 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d0:8"]]
- 00b67688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67750 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67750 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:890:8"]]
+ 00b67750 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67688 bytes a0421f39
+ 00b67750 bytes a0422239
- 00b67644 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7d0:8"]]
- 00b67644 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b67644 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6770c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:890:8"]]
+ 00b6770c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6770c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b67644 bytes a8425f39
+ 00b6770c bytes a8426239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8655ee34bd15ae2b09878493da7f1929"></a>

### [`00b6769c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6769c.md) → [`00b67764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md) _ZN8firebase4auth17phoneauthprovider12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b677a0",
      "incomplete_value": true,
      "site": "00b677a0",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676d8",
      "incomplete_value": true,
      "site": "00b676d8",
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
            "const:7d0:8"
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
      "definition_site": "00b677c0",
      "incomplete_value": true,
      "site": "00b677c0",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b676f8",
      "incomplete_value": true,
      "site": "00b676f8",
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
            "const:7c8:8"
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
      "definition_site": "00b6777c",
      "incomplete_value": true,
      "site": "00b6777c",
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
      "definition_site": "00b676b4",
      "incomplete_value": true,
      "site": "00b676b4",
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
      "00b67778",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67784",
      "READ",
      [
        "storage",
        "010a17d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b677a0",
      "WRITE",
      [
        "storage",
        "010a17d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67778",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67784",
      "READ",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b677a0",
      "WRITE",
      [
        "storage",
        "010a1890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b676d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6769c.md#insn-00b676d8) · [`00b676f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6769c.md#insn-00b676f4) · [`00b676f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6769c.md#insn-00b676f8)
- 新版 [`00b677a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md#insn-00b677a0) · [`00b677bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md#insn-00b677bc) · [`00b677c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67764.md#insn-00b677c0)

~~~diff
- 00b676d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b676d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b676d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d0:8"]]
- 00b676d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b677a0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b677a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b677a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
+ 00b677a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b676d8 bytes bf421f39
+ 00b677a0 bytes bf422239
- 00b676f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b676f4 ["INT_ADD", "register:40f0:8", ["const:b676f4:8", "const:4:8"]]
- 00b676f4 ["CALLIND", null, ["register:0:8"]]
+ 00b677bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b677bc ["INT_ADD", "register:40f0:8", ["const:b677bc:8", "const:4:8"]]
+ 00b677bc ["CALLIND", null, ["register:0:8"]]
- 00b676f4 bytes 00013fd6
+ 00b677bc bytes 00013fd6
- 00b676f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b676f8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b676f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b677c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b677c0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b677c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b676f8 bytes 9fe603f9
+ 00b677c0 bytes 9f4604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ec879e0d2d336cab3a486b6a3e9777e"></a>

### [`00b6770c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6770c.md) → [`00b677d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md) _ZN8firebase4auth17phoneauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67814",
      "incomplete_value": true,
      "site": "00b67814",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6774c",
      "incomplete_value": true,
      "site": "00b6774c",
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
            "const:7c8:8"
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
      "definition_site": "00b677f0",
      "incomplete_value": true,
      "site": "00b677f0",
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
      "definition_site": "00b67728",
      "incomplete_value": true,
      "site": "00b67728",
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
      "definition_site": "00b677f8",
      "incomplete_value": false,
      "site": "00b6780c",
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
            "const:5f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67730",
      "incomplete_value": false,
      "site": "00b67744",
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
            "const:56c:8"
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
      "00b677e8",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b677f8",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b67814",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b677e8",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b677f8",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b67814",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6770c.md#insn-00b67744) · [`00b6774c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6770c.md#insn-00b6774c) · [`00b67720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6770c.md#insn-00b67720)
- 新版 [`00b6780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md#insn-00b6780c) · [`00b67814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md#insn-00b67814) · [`00b677e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b677d4.md#insn-00b677e8)

~~~diff
- 00b67744 ["INT_ADD", "register:40f0:8", ["const:b67744:8", "const:4:8"]]
- 00b67744 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6780c ["INT_ADD", "register:40f0:8", ["const:b6780c:8", "const:4:8"]]
+ 00b6780c ["CALL", null, ["callee:00bde040:8"]]
- 00b67744 bytes 13da0194
+ 00b6780c bytes 0dda0194
- 00b6774c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b6774c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67814 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b67814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6774c bytes 80e603f9
+ 00b67814 bytes 804604f9
- 00b67720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b67720 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b677e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b677e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67720 bytes 81e643f9
+ 00b677e8 bytes 814644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87a1cdcc00882010fe2fda8dcd44b156"></a>

### [`00b6777c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6777c.md) → [`00b67844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md) _ZN8firebase4auth17phoneauthprovider11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67860",
      "incomplete_value": false,
      "site": "00b67864",
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
      "definition_site": "00b67798",
      "incomplete_value": false,
      "site": "00b6779c",
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
      "definition_site": "00b67870",
      "incomplete_value": true,
      "site": "00b6787c",
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
      "definition_site": "00b677a8",
      "incomplete_value": true,
      "site": "00b677b4",
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
      "00b67860",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67870",
      "DATA",
      [
        "storage",
        "010a17d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67860",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67870",
      "DATA",
      [
        "storage",
        "010a1898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6779c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6777c.md#insn-00b6779c) · [`00b67798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6777c.md#insn-00b67798) · [`00b677a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b6777c.md#insn-00b677a4)
- 新版 [`00b67864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md#insn-00b67864) · [`00b67860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md#insn-00b67860) · [`00b6786c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67844.md#insn-00b6786c)

~~~diff
- 00b6779c ["INT_ADD", "register:40f0:8", ["const:b6779c:8", "const:4:8"]]
- 00b6779c ["CALL", null, ["callee:00bde130:8"]]
+ 00b67864 ["INT_ADD", "register:40f0:8", ["const:b67864:8", "const:4:8"]]
+ 00b67864 ["CALL", null, ["callee:00bde130:8"]]
- 00b6779c bytes 39da0194
+ 00b67864 bytes 33da0194
- 00b67798 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b67798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67860 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b67860 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67860 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67860 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67798 bytes 001c1591
+ 00b67860 bytes 00501791
- 00b677a4 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00b677a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b677a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b677a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6786c ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00b6786c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6786c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6786c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b677a4 bytes 08611f91
+ 00b6786c bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e196f21fa6597e84d2a4036751cc09b"></a>

### [`00b677b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b677b8.md) → [`00b67880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md) _ZN8firebase4auth17phoneauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b678c0",
      "incomplete_value": true,
      "site": "00b678c0",
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
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677f8",
      "incomplete_value": true,
      "site": "00b677f8",
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
            "const:7c8:8"
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
      "definition_site": "00b6789c",
      "incomplete_value": true,
      "site": "00b6789c",
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
      "definition_site": "00b677d4",
      "incomplete_value": true,
      "site": "00b677d4",
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
      "definition_site": "00b678a4",
      "incomplete_value": false,
      "site": "00b678b8",
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
            "const:5f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b677dc",
      "incomplete_value": false,
      "site": "00b677f0",
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
            "const:56c:8"
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
      "00b67894",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b678a4",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b678c0",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67894",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b678a4",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ],
    [
      "00b678c0",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b677f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b677b8.md#insn-00b677f0) · [`00b677f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b677b8.md#insn-00b677f8) · [`00b677cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b677b8.md#insn-00b677cc)
- 新版 [`00b678b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md#insn-00b678b8) · [`00b678c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md#insn-00b678c0) · [`00b67894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67880.md#insn-00b67894)

~~~diff
- 00b677f0 ["INT_ADD", "register:40f0:8", ["const:b677f0:8", "const:4:8"]]
- 00b677f0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b678b8 ["INT_ADD", "register:40f0:8", ["const:b678b8:8", "const:4:8"]]
+ 00b678b8 ["CALL", null, ["callee:00bde040:8"]]
- 00b677f0 bytes e8d90194
+ 00b678b8 bytes e2d90194
- 00b677f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b677f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b678c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b678c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b677f8 bytes 80e603f9
+ 00b678c0 bytes 804604f9
- 00b677cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00b677cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b67894 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b677cc bytes 81e643f9
+ 00b67894 bytes 814644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-667e135680d7f8bb8a1941ed12bd201f"></a>

### [`00b67828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67828.md) → [`00b678f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md) _ZN8firebase4auth17phoneauthprovider10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6790c",
      "incomplete_value": false,
      "site": "00b67910",
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
      "definition_site": "00b67844",
      "incomplete_value": false,
      "site": "00b67848",
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
      "definition_site": "00b6791c",
      "incomplete_value": true,
      "site": "00b67928",
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
      "definition_site": "00b67854",
      "incomplete_value": true,
      "site": "00b67860",
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
      "00b6790c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6791c",
      "DATA",
      [
        "storage",
        "010a17f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6790c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6791c",
      "DATA",
      [
        "storage",
        "010a18b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67828.md#insn-00b67848) · [`00b67844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67828.md#insn-00b67844) · [`00b67850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67828.md#insn-00b67850)
- 新版 [`00b67910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md#insn-00b67910) · [`00b6790c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md#insn-00b6790c) · [`00b67918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b678f0.md#insn-00b67918)

~~~diff
- 00b67848 ["INT_ADD", "register:40f0:8", ["const:b67848:8", "const:4:8"]]
- 00b67848 ["CALL", null, ["callee:00bde130:8"]]
+ 00b67910 ["INT_ADD", "register:40f0:8", ["const:b67910:8", "const:4:8"]]
+ 00b67910 ["CALL", null, ["callee:00bde130:8"]]
- 00b67848 bytes 0eda0194
+ 00b67910 bytes 08da0194
- 00b67844 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6790c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b6790c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6790c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6790c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67844 bytes 00c81791
+ 00b6790c bytes 00fc1991
- 00b67850 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00b67850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67918 ["COPY", "tmp:0:8", ["const:8b0:8"]]
+ 00b67918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67850 bytes 08c11f91
+ 00b67918 bytes 08c12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1612fd8dfa7483381cc407ab91eb26c4"></a>

### [`00b67864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67864.md) → [`00b6792c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b67958",
      "incomplete_value": true,
      "site": "00b67958",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67890",
      "incomplete_value": true,
      "site": "00b67890",
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
            "const:7f8:8"
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
      "definition_site": "00b67940",
      "incomplete_value": true,
      "site": "00b67940",
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
      "definition_site": "00b67878",
      "incomplete_value": true,
      "site": "00b67878",
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
        "00b67878"
      ],
      [
        "FALL_THROUGH",
        "00b67940"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67940",
      "incomplete_value": true,
      "site": "00b67958",
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
      "definition_site": "00b67878",
      "incomplete_value": true,
      "site": "00b67890",
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
      "00b6793c",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67958",
      "WRITE",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6793c",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67958",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67864.md#insn-00b67890) · [`00b67874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67864.md#insn-00b67874) · [`00b67888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67864.md#insn-00b67888)
- 新版 [`00b67958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md#insn-00b67958) · [`00b6793c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md#insn-00b6793c) · [`00b67950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6792c.md#insn-00b67950)

~~~diff
- 00b67890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b67890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b67958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67890 bytes 60fe03f9
+ 00b67958 bytes 605e04f9
- 00b67874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b67874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6793c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b6793c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67874 bytes 68fe43f9
+ 00b6793c bytes 685e44f9
- 00b67888 ["INT_ADD", "register:40f0:8", ["const:b67888:8", "const:4:8"]]
- 00b67888 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67950 ["INT_ADD", "register:40f0:8", ["const:b67950:8", "const:4:8"]]
+ 00b67950 ["CALL", null, ["callee:00bde040:8"]]
- 00b67888 bytes c2d90194
+ 00b67950 bytes bcd90194
~~~


<a id="compare-1854853617ce38fb976df2e8a69f1c3a"></a>

### [`00b678a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678a4.md) → [`00b6796c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md) _ZN8firebase4auth21oauthprovider_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b67998",
      "incomplete_value": true,
      "site": "00b67998",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b678d0",
      "incomplete_value": true,
      "site": "00b678d0",
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
            "const:7f8:8"
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
      "definition_site": "00b67980",
      "incomplete_value": true,
      "site": "00b67980",
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
      "definition_site": "00b678b8",
      "incomplete_value": true,
      "site": "00b678b8",
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
        "00b678b8"
      ],
      [
        "FALL_THROUGH",
        "00b67980"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67980",
      "incomplete_value": true,
      "site": "00b67998",
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
      "definition_site": "00b678b8",
      "incomplete_value": true,
      "site": "00b678d0",
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
      "00b6797c",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67998",
      "WRITE",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6797c",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67998",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b678d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678a4.md#insn-00b678d0) · [`00b678b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678a4.md#insn-00b678b4) · [`00b678c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678a4.md#insn-00b678c8)
- 新版 [`00b67998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md#insn-00b67998) · [`00b6797c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md#insn-00b6797c) · [`00b67990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b6796c.md#insn-00b67990)

~~~diff
- 00b678d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b678d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b67998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b678d0 bytes 60fe03f9
+ 00b67998 bytes 605e04f9
- 00b678b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b678b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6797c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b6797c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b678b4 bytes 68fe43f9
+ 00b6797c bytes 685e44f9
- 00b678c8 ["INT_ADD", "register:40f0:8", ["const:b678c8:8", "const:4:8"]]
- 00b678c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67990 ["INT_ADD", "register:40f0:8", ["const:b67990:8", "const:4:8"]]
+ 00b67990 ["CALL", null, ["callee:00bde040:8"]]
- 00b678c8 bytes b2d90194
+ 00b67990 bytes acd90194
~~~


<a id="compare-83c7022f964106617f0c4e784369e02b"></a>

### [`00b678e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678e4.md) → [`00b679ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b679dc",
      "incomplete_value": true,
      "site": "00b679dc",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67914",
      "incomplete_value": true,
      "site": "00b67914",
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
            "const:7f8:8"
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
      "definition_site": "00b679c0",
      "incomplete_value": true,
      "site": "00b679c0",
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
      "definition_site": "00b678f8",
      "incomplete_value": true,
      "site": "00b678f8",
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
        "00b678f8"
      ],
      [
        "FALL_THROUGH",
        "00b679c0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b679c0",
      "incomplete_value": true,
      "site": "00b679dc",
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
      "definition_site": "00b678f8",
      "incomplete_value": true,
      "site": "00b67914",
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
      "00b679bc",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b679dc",
      "WRITE",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b679bc",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b679dc",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678e4.md#insn-00b67914) · [`00b678f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678e4.md#insn-00b678f4) · [`00b6790c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b678e4.md#insn-00b6790c)
- 新版 [`00b679dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md#insn-00b679dc) · [`00b679bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md#insn-00b679bc) · [`00b679d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679ac.md#insn-00b679d4)

~~~diff
- 00b67914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b67914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b679dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b679dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67914 bytes 60fe03f9
+ 00b679dc bytes 605e04f9
- 00b678f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b678f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b679bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b679bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b678f4 bytes 68fe43f9
+ 00b679bc bytes 685e44f9
- 00b6790c ["INT_ADD", "register:40f0:8", ["const:b6790c:8", "const:4:8"]]
- 00b6790c ["CALL", null, ["callee:00bde040:8"]]
+ 00b679d4 ["INT_ADD", "register:40f0:8", ["const:b679d4:8", "const:4:8"]]
+ 00b679d4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6790c bytes a1d90194
+ 00b679d4 bytes 9bd90194
~~~


<a id="compare-b6538493cee07d4e498a4e31383637d1"></a>

### [`00b67928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67928.md) → [`00b679f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md) _ZN8firebase4auth21oauthprovider_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67a20",
      "incomplete_value": true,
      "site": "00b67a20",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67958",
      "incomplete_value": true,
      "site": "00b67958",
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
            "const:7f8:8"
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
      "definition_site": "00b67a04",
      "incomplete_value": true,
      "site": "00b67a04",
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
      "definition_site": "00b6793c",
      "incomplete_value": true,
      "site": "00b6793c",
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
        "00b6793c"
      ],
      [
        "FALL_THROUGH",
        "00b67a04"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67a04",
      "incomplete_value": true,
      "site": "00b67a20",
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
      "definition_site": "00b6793c",
      "incomplete_value": true,
      "site": "00b67958",
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
      "00b67a00",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a20",
      "WRITE",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67a00",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a20",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67928.md#insn-00b67958) · [`00b67938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67928.md#insn-00b67938) · [`00b67950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67928.md#insn-00b67950)
- 新版 [`00b67a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md#insn-00b67a20) · [`00b67a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md#insn-00b67a00) · [`00b67a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b679f0.md#insn-00b67a18)

~~~diff
- 00b67958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b67958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b67a20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67958 bytes 60fe03f9
+ 00b67a20 bytes 605e04f9
- 00b67938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7f8:8"]]
- 00b67938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67a00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
+ 00b67a00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67938 bytes 68fe43f9
+ 00b67a00 bytes 685e44f9
- 00b67950 ["INT_ADD", "register:40f0:8", ["const:b67950:8", "const:4:8"]]
- 00b67950 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67a18 ["INT_ADD", "register:40f0:8", ["const:b67a18:8", "const:4:8"]]
+ 00b67a18 ["CALL", null, ["callee:00bde040:8"]]
- 00b67950 bytes 90d90194
+ 00b67a18 bytes 8ad90194
~~~


<a id="compare-8f47d5f13b8fc665a7a06e1e6301b306"></a>

### [`00b67978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67978.md) → [`00b67a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md) _ZN8firebase4auth21oauthprovider_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67a98",
      "incomplete_value": true,
      "site": "00b67a98",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679d0",
      "incomplete_value": true,
      "site": "00b679d0",
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
            "const:800:8"
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
      "definition_site": "00b67a74",
      "incomplete_value": true,
      "site": "00b67a80",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b679ac",
      "incomplete_value": true,
      "site": "00b679b8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7f8:8"
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
      "00b67a54",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67a74",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a98",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67a54",
      "READ",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67a74",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67a98",
      "WRITE",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b679b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67978.md#insn-00b679b8) · [`00b679d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67978.md#insn-00b679d0) · [`00b6798c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67978.md#insn-00b6798c)
- 新版 [`00b67a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md#insn-00b67a80) · [`00b67a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md#insn-00b67a98) · [`00b67a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67a40.md#insn-00b67a54)

~~~diff
- 00b679b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b679b8 ["INT_ADD", "register:40f0:8", ["const:b679b8:8", "const:4:8"]]
- 00b679b8 ["CALLIND", null, ["register:0:8"]]
+ 00b67a80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67a80 ["INT_ADD", "register:40f0:8", ["const:b67a80:8", "const:4:8"]]
+ 00b67a80 ["CALLIND", null, ["register:0:8"]]
- 00b679b8 bytes 00013fd6
+ 00b67a80 bytes 00013fd6
- 00b679d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b679d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:800:8"]]
- 00b679d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67a98 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67a98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8c0:8"]]
+ 00b67a98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b679d0 bytes a0022039
+ 00b67a98 bytes a0022339
- 00b6798c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:800:8"]]
- 00b6798c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6798c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b67a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8c0:8"]]
+ 00b67a54 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b67a54 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6798c bytes a8026039
+ 00b67a54 bytes a8026339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a49d8b6ec3bc386d0fe82424299f4b"></a>

### [`00b679e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b679e4.md) → [`00b67aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md) _ZN8firebase4auth21oauthprovider_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b67ae8",
      "incomplete_value": true,
      "site": "00b67ae8",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a20",
      "incomplete_value": true,
      "site": "00b67a20",
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
            "const:800:8"
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
      "definition_site": "00b67b08",
      "incomplete_value": true,
      "site": "00b67b08",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a40",
      "incomplete_value": true,
      "site": "00b67a40",
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
            "const:7f8:8"
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
      "definition_site": "00b67ac4",
      "incomplete_value": true,
      "site": "00b67ac4",
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
      "definition_site": "00b679fc",
      "incomplete_value": true,
      "site": "00b679fc",
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
      "00b67ac0",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67acc",
      "READ",
      [
        "storage",
        "010a1800",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67ae8",
      "WRITE",
      [
        "storage",
        "010a1800",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67ac0",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67acc",
      "READ",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67ae8",
      "WRITE",
      [
        "storage",
        "010a18c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b679e4.md#insn-00b67a20) · [`00b67a3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b679e4.md#insn-00b67a3c) · [`00b67a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b679e4.md#insn-00b67a40)
- 新版 [`00b67ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md#insn-00b67ae8) · [`00b67b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md#insn-00b67b04) · [`00b67b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67aac.md#insn-00b67b08)

~~~diff
- 00b67a20 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67a20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67a20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:800:8"]]
- 00b67a20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67ae8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67ae8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67ae8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8c0:8"]]
+ 00b67ae8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67a20 bytes bf022039
+ 00b67ae8 bytes bf022339
- 00b67a3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67a3c ["INT_ADD", "register:40f0:8", ["const:b67a3c:8", "const:4:8"]]
- 00b67a3c ["CALLIND", null, ["register:0:8"]]
+ 00b67b04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67b04 ["INT_ADD", "register:40f0:8", ["const:b67b04:8", "const:4:8"]]
+ 00b67b04 ["CALLIND", null, ["register:0:8"]]
- 00b67a3c bytes 00013fd6
+ 00b67b04 bytes 00013fd6
- 00b67a40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b67a40 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b67a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b67b08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00b67b08 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b67b08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b67a40 bytes 9ffe03f9
+ 00b67b08 bytes 9f5e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04d0b6fe5568529acaebeb5417c50db9"></a>

### [`00b67a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67a54.md) → [`00b67b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md) _ZN8firebase4auth21oauthprovider_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67b5c",
      "incomplete_value": true,
      "site": "00b67b5c",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67a94",
      "incomplete_value": true,
      "site": "00b67a94",
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
            "const:7f8:8"
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
      "definition_site": "00b67b38",
      "incomplete_value": true,
      "site": "00b67b38",
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
      "definition_site": "00b67a70",
      "incomplete_value": true,
      "site": "00b67a70",
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
        "00b67a70"
      ],
      [
        "FALL_THROUGH",
        "00b67b38"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67b38",
      "incomplete_value": true,
      "site": "00b67b5c",
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
      "definition_site": "00b67a70",
      "incomplete_value": true,
      "site": "00b67a94",
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
      "00b67b30",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b5c",
      "WRITE",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b70",
      "PARAM",
      [
        "storage",
        "00c124f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b67b30",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b5c",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67b70",
      "PARAM",
      [
        "storage",
        "00c125a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67a54.md#insn-00b67a94) · [`00b67a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67a54.md#insn-00b67a68) · [`00b67a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67a54.md#insn-00b67a8c)
- 新版 [`00b67b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md#insn-00b67b5c) · [`00b67b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md#insn-00b67b30) · [`00b67b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b1c.md#insn-00b67b54)

~~~diff
- 00b67a94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b67a94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67b5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00b67b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67a94 bytes 80fe03f9
+ 00b67b5c bytes 805e04f9
- 00b67a68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b67a68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67b30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00b67b30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67a68 bytes 81fe43f9
+ 00b67b30 bytes 815e44f9
- 00b67a8c ["INT_ADD", "register:40f0:8", ["const:b67a8c:8", "const:4:8"]]
- 00b67a8c ["CALL", null, ["callee:00bde040:8"]]
+ 00b67b54 ["INT_ADD", "register:40f0:8", ["const:b67b54:8", "const:4:8"]]
+ 00b67b54 ["CALL", null, ["callee:00bde040:8"]]
- 00b67a8c bytes 41d90194
+ 00b67b54 bytes 3bd90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3b9d8997681e3821d8bfb9963c44883"></a>

### [`00b67ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ac4.md) → [`00b67b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md) _ZN8firebase4auth21oauthprovider_builder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67ba8",
      "incomplete_value": false,
      "site": "00b67bac",
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
      "definition_site": "00b67ae0",
      "incomplete_value": false,
      "site": "00b67ae4",
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
      "definition_site": "00b67bb8",
      "incomplete_value": true,
      "site": "00b67bc4",
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
      "definition_site": "00b67af0",
      "incomplete_value": true,
      "site": "00b67afc",
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
      "00b67ba8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67bb8",
      "DATA",
      [
        "storage",
        "010a1808",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67ba8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67bb8",
      "DATA",
      [
        "storage",
        "010a18c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ac4.md#insn-00b67ae4) · [`00b67ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ac4.md#insn-00b67ae0) · [`00b67aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ac4.md#insn-00b67aec)
- 新版 [`00b67bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md#insn-00b67bac) · [`00b67ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md#insn-00b67ba8) · [`00b67bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67b8c.md#insn-00b67bb4)

~~~diff
- 00b67ae4 ["INT_ADD", "register:40f0:8", ["const:b67ae4:8", "const:4:8"]]
- 00b67ae4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b67bac ["INT_ADD", "register:40f0:8", ["const:b67bac:8", "const:4:8"]]
+ 00b67bac ["CALL", null, ["callee:00bde130:8"]]
- 00b67ae4 bytes 67d90194
+ 00b67bac bytes 61d90194
- 00b67ae0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b67ae0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ae0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ae0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67ba8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b67ba8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67ba8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67ba8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67ae0 bytes 001c1591
+ 00b67ba8 bytes 00501791
- 00b67aec ["COPY", "tmp:0:8", ["const:808:8"]]
- 00b67aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67bb4 ["COPY", "tmp:0:8", ["const:8c8:8"]]
+ 00b67bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67aec bytes 08212091
+ 00b67bb4 bytes 08212391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89e4467c1becae034f15f49dc087697d"></a>

### [`00b67b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b00.md) → [`00b67bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md) _ZN8firebase4auth21oauthprovider_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b67c08",
      "incomplete_value": true,
      "site": "00b67c08",
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
            "const:8b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67b40",
      "incomplete_value": true,
      "site": "00b67b40",
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
            "const:7f8:8"
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
      "definition_site": "00b67be4",
      "incomplete_value": true,
      "site": "00b67be4",
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
      "definition_site": "00b67b1c",
      "incomplete_value": true,
      "site": "00b67b1c",
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
        "00b67b1c"
      ],
      [
        "FALL_THROUGH",
        "00b67be4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b67be4",
      "incomplete_value": true,
      "site": "00b67c08",
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
      "definition_site": "00b67b1c",
      "incomplete_value": true,
      "site": "00b67b40",
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
      "00b67bdc",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c08",
      "WRITE",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c20",
      "PARAM",
      [
        "storage",
        "010a1820",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67bdc",
      "READ",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c08",
      "WRITE",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c20",
      "PARAM",
      [
        "storage",
        "010a18e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b00.md#insn-00b67b40) · [`00b67b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b00.md#insn-00b67b14) · [`00b67b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b00.md#insn-00b67b38)
- 新版 [`00b67c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md#insn-00b67c08) · [`00b67bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md#insn-00b67bdc) · [`00b67c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67bc8.md#insn-00b67c00)

~~~diff
- 00b67b40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b67b40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67c08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00b67c08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67b40 bytes 80fe03f9
+ 00b67c08 bytes 805e04f9
- 00b67b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b67b14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00b67bdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67b14 bytes 81fe43f9
+ 00b67bdc bytes 815e44f9
- 00b67b38 ["INT_ADD", "register:40f0:8", ["const:b67b38:8", "const:4:8"]]
- 00b67b38 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67c00 ["INT_ADD", "register:40f0:8", ["const:b67c00:8", "const:4:8"]]
+ 00b67c00 ["CALL", null, ["callee:00bde040:8"]]
- 00b67b38 bytes 16d90194
+ 00b67c00 bytes 10d90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e8d0bd350066c9b9e79068ddc956e03"></a>

### [`00b67b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b70.md) → [`00b67c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md) _ZN8firebase4auth21oauthprovider_builder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b67c54",
      "incomplete_value": false,
      "site": "00b67c58",
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
      "definition_site": "00b67b8c",
      "incomplete_value": false,
      "site": "00b67b90",
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
      "definition_site": "00b67c64",
      "incomplete_value": true,
      "site": "00b67c70",
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
      "definition_site": "00b67b9c",
      "incomplete_value": true,
      "site": "00b67ba8",
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
      "00b67c54",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b67c64",
      "DATA",
      [
        "storage",
        "010a1820",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67c54",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b67c64",
      "DATA",
      [
        "storage",
        "010a18e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b70.md#insn-00b67b90) · [`00b67b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b70.md#insn-00b67b8c) · [`00b67b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67b70.md#insn-00b67b98)
- 新版 [`00b67c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md#insn-00b67c58) · [`00b67c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md#insn-00b67c54) · [`00b67c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c38.md#insn-00b67c60)

~~~diff
- 00b67b90 ["INT_ADD", "register:40f0:8", ["const:b67b90:8", "const:4:8"]]
- 00b67b90 ["CALL", null, ["callee:00bde130:8"]]
+ 00b67c58 ["INT_ADD", "register:40f0:8", ["const:b67c58:8", "const:4:8"]]
+ 00b67c58 ["CALL", null, ["callee:00bde130:8"]]
- 00b67b90 bytes 3cd90194
+ 00b67c58 bytes 36d90194
- 00b67b8c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67b8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67b8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67b8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67c54 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b67c54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67c54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67c54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67b8c bytes 00c81791
+ 00b67c54 bytes 00fc1991
- 00b67b98 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00b67b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67c60 ["COPY", "tmp:0:8", ["const:8e0:8"]]
+ 00b67c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67b98 bytes 08812091
+ 00b67c60 bytes 08812391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-727a4999e9c52cd5af4c8091e34de1f4"></a>

### [`00b67bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bac.md) → [`00b67c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00b67ca0",
      "incomplete_value": true,
      "site": "00b67ca0",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67bd8",
      "incomplete_value": true,
      "site": "00b67bd8",
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
            "const:828:8"
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
      "definition_site": "00b67c88",
      "incomplete_value": true,
      "site": "00b67c88",
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
      "definition_site": "00b67bc0",
      "incomplete_value": true,
      "site": "00b67bc0",
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
      "definition_site": "00b67c94",
      "incomplete_value": false,
      "site": "00b67c98",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67bcc",
      "incomplete_value": false,
      "site": "00b67bd0",
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
            "const:2aa:8"
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
      "00b67c84",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c94",
      "PARAM",
      [
        "storage",
        "002ab2aa",
        null,
        "string"
      ]
    ],
    [
      "00b67ca0",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67c84",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67c94",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00b67ca0",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bac.md#insn-00b67bd0) · [`00b67bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bac.md#insn-00b67bd8) · [`00b67bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bac.md#insn-00b67bbc)
- 新版 [`00b67c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md#insn-00b67c98) · [`00b67ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md#insn-00b67ca0) · [`00b67c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67c74.md#insn-00b67c84)

~~~diff
- 00b67bd0 ["INT_ADD", "register:40f0:8", ["const:b67bd0:8", "const:4:8"]]
- 00b67bd0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67c98 ["INT_ADD", "register:40f0:8", ["const:b67c98:8", "const:4:8"]]
+ 00b67c98 ["CALL", null, ["callee:00bde040:8"]]
- 00b67bd0 bytes f0d80194
+ 00b67c98 bytes ead80194
- 00b67bd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67bd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67ca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67bd8 bytes 601604f9
+ 00b67ca0 bytes 607604f9
- 00b67bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67c84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67c84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67bbc bytes 681644f9
+ 00b67c84 bytes 687644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77b53675ef26f9721feed885b4b0cb1c"></a>

### [`00b67bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bec.md) → [`00b67cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00b67ce0",
      "incomplete_value": true,
      "site": "00b67ce0",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c18",
      "incomplete_value": true,
      "site": "00b67c18",
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
            "const:828:8"
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
      "definition_site": "00b67cc8",
      "incomplete_value": true,
      "site": "00b67cc8",
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
      "definition_site": "00b67c00",
      "incomplete_value": true,
      "site": "00b67c00",
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
      "definition_site": "00b67cd0",
      "incomplete_value": false,
      "site": "00b67cd8",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c08",
      "incomplete_value": false,
      "site": "00b67c10",
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
            "const:2aa:8"
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
      "00b67cc4",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67cd0",
      "PARAM",
      [
        "storage",
        "002ab2aa",
        null,
        "string"
      ]
    ],
    [
      "00b67ce0",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67cc4",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67cd0",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00b67ce0",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bec.md#insn-00b67c10) · [`00b67c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bec.md#insn-00b67c18) · [`00b67bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67bec.md#insn-00b67bfc)
- 新版 [`00b67cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md#insn-00b67cd8) · [`00b67ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md#insn-00b67ce0) · [`00b67cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cb4.md#insn-00b67cc4)

~~~diff
- 00b67c10 ["INT_ADD", "register:40f0:8", ["const:b67c10:8", "const:4:8"]]
- 00b67c10 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67cd8 ["INT_ADD", "register:40f0:8", ["const:b67cd8:8", "const:4:8"]]
+ 00b67cd8 ["CALL", null, ["callee:00bde040:8"]]
- 00b67c10 bytes e0d80194
+ 00b67cd8 bytes dad80194
- 00b67c18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67c18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67c18 bytes 601604f9
+ 00b67ce0 bytes 607604f9
- 00b67bfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67bfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67cc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67cc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67bfc bytes 681644f9
+ 00b67cc4 bytes 687644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e73b834d518016a170326fce575ff7c"></a>

### [`00b67c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c2c.md) → [`00b67cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b67d24",
      "incomplete_value": true,
      "site": "00b67d24",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c5c",
      "incomplete_value": true,
      "site": "00b67c5c",
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
            "const:828:8"
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
      "definition_site": "00b67d08",
      "incomplete_value": true,
      "site": "00b67d08",
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
      "definition_site": "00b67c40",
      "incomplete_value": true,
      "site": "00b67c40",
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
      "definition_site": "00b67d14",
      "incomplete_value": false,
      "site": "00b67d1c",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c4c",
      "incomplete_value": false,
      "site": "00b67c54",
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
            "const:2aa:8"
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
      "00b67d04",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d14",
      "PARAM",
      [
        "storage",
        "002ab2aa",
        null,
        "string"
      ]
    ],
    [
      "00b67d24",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67d04",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d14",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00b67d24",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c2c.md#insn-00b67c54) · [`00b67c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c2c.md#insn-00b67c5c) · [`00b67c3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c2c.md#insn-00b67c3c)
- 新版 [`00b67d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md#insn-00b67d1c) · [`00b67d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md#insn-00b67d24) · [`00b67d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67cf4.md#insn-00b67d04)

~~~diff
- 00b67c54 ["INT_ADD", "register:40f0:8", ["const:b67c54:8", "const:4:8"]]
- 00b67c54 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67d1c ["INT_ADD", "register:40f0:8", ["const:b67d1c:8", "const:4:8"]]
+ 00b67d1c ["CALL", null, ["callee:00bde040:8"]]
- 00b67c54 bytes cfd80194
+ 00b67d1c bytes c9d80194
- 00b67c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67c5c bytes 601604f9
+ 00b67d24 bytes 607604f9
- 00b67c3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67c3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67c3c bytes 681644f9
+ 00b67d04 bytes 687644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-223dd0ad4aa7bfd6f2a7a3a7d1847605"></a>

### [`00b67c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c70.md) → [`00b67d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67d68",
      "incomplete_value": true,
      "site": "00b67d68",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ca0",
      "incomplete_value": true,
      "site": "00b67ca0",
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
            "const:828:8"
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
      "definition_site": "00b67d4c",
      "incomplete_value": true,
      "site": "00b67d4c",
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
      "definition_site": "00b67c84",
      "incomplete_value": true,
      "site": "00b67c84",
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
      "definition_site": "00b67d54",
      "incomplete_value": false,
      "site": "00b67d60",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67c8c",
      "incomplete_value": false,
      "site": "00b67c98",
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
            "const:2aa:8"
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
      "00b67d48",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d54",
      "PARAM",
      [
        "storage",
        "002ab2aa",
        null,
        "string"
      ]
    ],
    [
      "00b67d68",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67d48",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67d54",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00b67d68",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c70.md#insn-00b67c98) · [`00b67ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c70.md#insn-00b67ca0) · [`00b67c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67c70.md#insn-00b67c80)
- 新版 [`00b67d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md#insn-00b67d60) · [`00b67d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md#insn-00b67d68) · [`00b67d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d38.md#insn-00b67d48)

~~~diff
- 00b67c98 ["INT_ADD", "register:40f0:8", ["const:b67c98:8", "const:4:8"]]
- 00b67c98 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67d60 ["INT_ADD", "register:40f0:8", ["const:b67d60:8", "const:4:8"]]
+ 00b67d60 ["CALL", null, ["callee:00bde040:8"]]
- 00b67c98 bytes bed80194
+ 00b67d60 bytes b8d80194
- 00b67ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67ca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67d68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ca0 bytes 601604f9
+ 00b67d68 bytes 607604f9
- 00b67c80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b67c80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
+ 00b67d48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67c80 bytes 681644f9
+ 00b67d48 bytes 687644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4a70c796c4038abbdb6060fe0d9f85e"></a>

### [`00b67cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67cc0.md) → [`00b67d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md) _ZN8firebase4auth31oauthprovider_credentialbuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b67de0",
      "incomplete_value": true,
      "site": "00b67de0",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d18",
      "incomplete_value": true,
      "site": "00b67d18",
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
            "const:830:8"
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
      "definition_site": "00b67dbc",
      "incomplete_value": true,
      "site": "00b67dc8",
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
                "const:10a1000:8"
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
      "definition_site": "00b67cf4",
      "incomplete_value": true,
      "site": "00b67d00",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:828:8"
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
      "00b67d9c",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67dbc",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67de0",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67d9c",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67dbc",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67de0",
      "WRITE",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67cc0.md#insn-00b67d00) · [`00b67d18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67cc0.md#insn-00b67d18) · [`00b67cd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67cc0.md#insn-00b67cd4)
- 新版 [`00b67dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md#insn-00b67dc8) · [`00b67de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md#insn-00b67de0) · [`00b67d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67d88.md#insn-00b67d9c)

~~~diff
- 00b67d00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67d00 ["INT_ADD", "register:40f0:8", ["const:b67d00:8", "const:4:8"]]
- 00b67d00 ["CALLIND", null, ["register:0:8"]]
+ 00b67dc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67dc8 ["INT_ADD", "register:40f0:8", ["const:b67dc8:8", "const:4:8"]]
+ 00b67dc8 ["CALLIND", null, ["register:0:8"]]
- 00b67d00 bytes 00013fd6
+ 00b67dc8 bytes 00013fd6
- 00b67d18 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b67d18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:830:8"]]
- 00b67d18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b67de0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b67de0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f0:8"]]
+ 00b67de0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b67d18 bytes a0c22039
+ 00b67de0 bytes a0c22339
- 00b67cd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:830:8"]]
- 00b67cd4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b67cd4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b67d9c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f0:8"]]
+ 00b67d9c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b67d9c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b67cd4 bytes a8c26039
+ 00b67d9c bytes a8c26339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21a10ba643a0eb38622839fd380e5099"></a>

### [`00b67d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d2c.md) → [`00b67df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b67e30",
      "incomplete_value": true,
      "site": "00b67e30",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d68",
      "incomplete_value": true,
      "site": "00b67d68",
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
            "const:830:8"
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
      "definition_site": "00b67e50",
      "incomplete_value": true,
      "site": "00b67e50",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67d88",
      "incomplete_value": true,
      "site": "00b67d88",
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
            "const:828:8"
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
      "definition_site": "00b67e0c",
      "incomplete_value": true,
      "site": "00b67e0c",
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
      "definition_site": "00b67d44",
      "incomplete_value": true,
      "site": "00b67d44",
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
      "00b67e08",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e14",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67e30",
      "WRITE",
      [
        "storage",
        "010a1830",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b67e08",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e14",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b67e30",
      "WRITE",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d2c.md#insn-00b67d68) · [`00b67d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d2c.md#insn-00b67d84) · [`00b67d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d2c.md#insn-00b67d88)
- 新版 [`00b67e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md#insn-00b67e30) · [`00b67e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md#insn-00b67e4c) · [`00b67e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67df4.md#insn-00b67e50)

~~~diff
- 00b67d68 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b67d68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b67d68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:830:8"]]
- 00b67d68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b67e30 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b67e30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b67e30 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f0:8"]]
+ 00b67e30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b67d68 bytes bfc22039
+ 00b67e30 bytes bfc22339
- 00b67d84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b67d84 ["INT_ADD", "register:40f0:8", ["const:b67d84:8", "const:4:8"]]
- 00b67d84 ["CALLIND", null, ["register:0:8"]]
+ 00b67e4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b67e4c ["INT_ADD", "register:40f0:8", ["const:b67e4c:8", "const:4:8"]]
+ 00b67e4c ["CALLIND", null, ["register:0:8"]]
- 00b67d84 bytes 00013fd6
+ 00b67e4c bytes 00013fd6
- 00b67d88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b67d88 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b67d88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b67e50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00b67e50 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b67e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b67d88 bytes 9f1604f9
+ 00b67e50 bytes 9f7604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d678f762d973338b3220b9077cfc330"></a>

### [`00b67d9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d9c.md) → [`00b67e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md) _ZN8firebase4auth31oauthprovider_credentialbuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67ea4",
      "incomplete_value": true,
      "site": "00b67ea4",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67ddc",
      "incomplete_value": true,
      "site": "00b67ddc",
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
            "const:828:8"
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
      "definition_site": "00b67e80",
      "incomplete_value": true,
      "site": "00b67e80",
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
      "definition_site": "00b67db8",
      "incomplete_value": true,
      "site": "00b67db8",
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
      "definition_site": "00b67e88",
      "incomplete_value": false,
      "site": "00b67e9c",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67dc0",
      "incomplete_value": false,
      "site": "00b67dd4",
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
            "const:2aa:8"
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
      "00b67e78",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e88",
      "PARAM",
      [
        "storage",
        "002ab2aa",
        null,
        "string"
      ]
    ],
    [
      "00b67ea4",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67e78",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67e88",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00b67ea4",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d9c.md#insn-00b67dd4) · [`00b67ddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d9c.md#insn-00b67ddc) · [`00b67db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67d9c.md#insn-00b67db0)
- 新版 [`00b67e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md#insn-00b67e9c) · [`00b67ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md#insn-00b67ea4) · [`00b67e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67e64.md#insn-00b67e78)

~~~diff
- 00b67dd4 ["INT_ADD", "register:40f0:8", ["const:b67dd4:8", "const:4:8"]]
- 00b67dd4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67e9c ["INT_ADD", "register:40f0:8", ["const:b67e9c:8", "const:4:8"]]
+ 00b67e9c ["CALL", null, ["callee:00bde040:8"]]
- 00b67dd4 bytes 6fd80194
+ 00b67e9c bytes 69d80194
- 00b67ddc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b67ddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67ea4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00b67ea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67ddc bytes 801604f9
+ 00b67ea4 bytes 807604f9
- 00b67db0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b67db0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67e78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00b67e78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67db0 bytes 811644f9
+ 00b67e78 bytes 817644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b658f900bc487ed2b56052da55c0c3e1"></a>

### [`00b67e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e0c.md) → [`00b67ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md) _ZN8firebase4auth31oauthprovider_credentialbuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b67ef0",
      "incomplete_value": false,
      "site": "00b67ef4",
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
      "definition_site": "00b67e28",
      "incomplete_value": false,
      "site": "00b67e2c",
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
      "definition_site": "00b67f00",
      "incomplete_value": true,
      "site": "00b67f0c",
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
      "definition_site": "00b67e38",
      "incomplete_value": true,
      "site": "00b67e44",
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
      "00b67ef0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b67f00",
      "DATA",
      [
        "storage",
        "010a1838",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67ef0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b67f00",
      "DATA",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e0c.md#insn-00b67e2c) · [`00b67e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e0c.md#insn-00b67e28) · [`00b67e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e0c.md#insn-00b67e34)
- 新版 [`00b67ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md#insn-00b67ef4) · [`00b67ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md#insn-00b67ef0) · [`00b67efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ed4.md#insn-00b67efc)

~~~diff
- 00b67e2c ["INT_ADD", "register:40f0:8", ["const:b67e2c:8", "const:4:8"]]
- 00b67e2c ["CALL", null, ["callee:00bde130:8"]]
+ 00b67ef4 ["INT_ADD", "register:40f0:8", ["const:b67ef4:8", "const:4:8"]]
+ 00b67ef4 ["CALL", null, ["callee:00bde130:8"]]
- 00b67e2c bytes 95d80194
+ 00b67ef4 bytes 8fd80194
- 00b67e28 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b67e28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67e28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67e28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67ef0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b67ef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67ef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67ef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67e28 bytes 001c1591
+ 00b67ef0 bytes 00501791
- 00b67e34 ["COPY", "tmp:0:8", ["const:838:8"]]
- 00b67e34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67e34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67e34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67efc ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00b67efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67e34 bytes 08e12091
+ 00b67efc bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9c9d3cfa165f4e847890b0460937ce"></a>

### [`00b67e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e48.md) → [`00b67f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md) _ZN8firebase4auth31oauthprovider_credentialbuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b67f50",
      "incomplete_value": true,
      "site": "00b67f50",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e88",
      "incomplete_value": true,
      "site": "00b67e88",
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
            "const:828:8"
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
      "definition_site": "00b67f2c",
      "incomplete_value": true,
      "site": "00b67f2c",
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
      "definition_site": "00b67e64",
      "incomplete_value": true,
      "site": "00b67e64",
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
      "definition_site": "00b67f34",
      "incomplete_value": false,
      "site": "00b67f48",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67e6c",
      "incomplete_value": false,
      "site": "00b67e80",
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
            "const:2aa:8"
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
      "00b67f24",
      "READ",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67f34",
      "PARAM",
      [
        "storage",
        "002ab2aa",
        null,
        "string"
      ]
    ],
    [
      "00b67f50",
      "WRITE",
      [
        "storage",
        "010a1828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67f24",
      "READ",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67f34",
      "PARAM",
      [
        "storage",
        "002ab2b0",
        null,
        "string"
      ]
    ],
    [
      "00b67f50",
      "WRITE",
      [
        "storage",
        "010a18e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e48.md#insn-00b67e80) · [`00b67e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e48.md#insn-00b67e88) · [`00b67e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67e48.md#insn-00b67e5c)
- 新版 [`00b67f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md#insn-00b67f48) · [`00b67f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md#insn-00b67f50) · [`00b67f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f10.md#insn-00b67f24)

~~~diff
- 00b67e80 ["INT_ADD", "register:40f0:8", ["const:b67e80:8", "const:4:8"]]
- 00b67e80 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67f48 ["INT_ADD", "register:40f0:8", ["const:b67f48:8", "const:4:8"]]
+ 00b67f48 ["CALL", null, ["callee:00bde040:8"]]
- 00b67e80 bytes 44d80194
+ 00b67f48 bytes 3ed80194
- 00b67e88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b67e88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67f50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00b67f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67e88 bytes 801604f9
+ 00b67f50 bytes 807604f9
- 00b67e5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b67e5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67f24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
+ 00b67f24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67e5c bytes 811644f9
+ 00b67f24 bytes 817644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed3ed49b2ab0f0196e9aa3e56a335f1"></a>

### [`00b67eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67eb8.md) → [`00b67f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md) _ZN8firebase4auth31oauthprovider_credentialbuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b67f9c",
      "incomplete_value": false,
      "site": "00b67fa0",
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
      "definition_site": "00b67ed4",
      "incomplete_value": false,
      "site": "00b67ed8",
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
      "definition_site": "00b67fac",
      "incomplete_value": true,
      "site": "00b67fb8",
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
      "definition_site": "00b67ee4",
      "incomplete_value": true,
      "site": "00b67ef0",
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
      "00b67f9c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b67fac",
      "DATA",
      [
        "storage",
        "010a1858",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b67f9c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b67fac",
      "DATA",
      [
        "storage",
        "010a1918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67eb8.md#insn-00b67ed8) · [`00b67ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67eb8.md#insn-00b67ed4) · [`00b67ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67eb8.md#insn-00b67ee0)
- 新版 [`00b67fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md#insn-00b67fa0) · [`00b67f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md#insn-00b67f9c) · [`00b67fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67f80.md#insn-00b67fa8)

~~~diff
- 00b67ed8 ["INT_ADD", "register:40f0:8", ["const:b67ed8:8", "const:4:8"]]
- 00b67ed8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b67fa0 ["INT_ADD", "register:40f0:8", ["const:b67fa0:8", "const:4:8"]]
+ 00b67fa0 ["CALL", null, ["callee:00bde130:8"]]
- 00b67ed8 bytes 6ad80194
+ 00b67fa0 bytes 64d80194
- 00b67ed4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b67ed4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ed4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b67ed4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b67f9c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b67f9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67f9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b67f9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b67ed4 bytes 00c81791
+ 00b67f9c bytes 00fc1991
- 00b67ee0 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00b67ee0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b67ee0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b67ee0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b67fa8 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00b67fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b67fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b67ee0 bytes 08612191
+ 00b67fa8 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfb07b4501c8314c346435ccf1ab77c5"></a>

### [`00b67ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ef4.md) → [`00b67fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b67fe8",
      "incomplete_value": true,
      "site": "00b67fe8",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f20",
      "incomplete_value": true,
      "site": "00b67f20",
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
            "const:860:8"
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
      "definition_site": "00b67fd0",
      "incomplete_value": true,
      "site": "00b67fd0",
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
      "definition_site": "00b67f08",
      "incomplete_value": true,
      "site": "00b67f08",
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
      "definition_site": "00b67fdc",
      "incomplete_value": false,
      "site": "00b67fe0",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f14",
      "incomplete_value": false,
      "site": "00b67f18",
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
            "const:f4b:8"
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
      "00b67fcc",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67fdc",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b67fe8",
      "WRITE",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b67fcc",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b67fdc",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b67fe8",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ef4.md#insn-00b67f18) · [`00b67f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ef4.md#insn-00b67f20) · [`00b67f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67ef4.md#insn-00b67f04)
- 新版 [`00b67fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md#insn-00b67fe0) · [`00b67fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md#insn-00b67fe8) · [`00b67fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67fbc.md#insn-00b67fcc)

~~~diff
- 00b67f18 ["INT_ADD", "register:40f0:8", ["const:b67f18:8", "const:4:8"]]
- 00b67f18 ["CALL", null, ["callee:00bde040:8"]]
+ 00b67fe0 ["INT_ADD", "register:40f0:8", ["const:b67fe0:8", "const:4:8"]]
+ 00b67fe0 ["CALL", null, ["callee:00bde040:8"]]
- 00b67f18 bytes 1ed80194
+ 00b67fe0 bytes 18d80194
- 00b67f20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b67fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b67fe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67f20 bytes 603204f9
+ 00b67fe8 bytes 609204f9
- 00b67f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67f04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b67fcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b67fcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67f04 bytes 683244f9
+ 00b67fcc bytes 689244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4760c126b1fb11639f690ba8dc20eb3e"></a>

### [`00b67f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f34.md) → [`00b67ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md) _ZN8firebase4auth8auth_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b68028",
      "incomplete_value": true,
      "site": "00b68028",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f60",
      "incomplete_value": true,
      "site": "00b67f60",
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
            "const:860:8"
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
      "definition_site": "00b68010",
      "incomplete_value": true,
      "site": "00b68010",
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
      "definition_site": "00b67f48",
      "incomplete_value": true,
      "site": "00b67f48",
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
      "definition_site": "00b68018",
      "incomplete_value": false,
      "site": "00b68020",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f50",
      "incomplete_value": false,
      "site": "00b67f58",
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
            "const:f4b:8"
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
      "00b6800c",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68018",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b68028",
      "WRITE",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6800c",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68018",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b68028",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f34.md#insn-00b67f58) · [`00b67f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f34.md#insn-00b67f60) · [`00b67f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f34.md#insn-00b67f44)
- 新版 [`00b68020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md#insn-00b68020) · [`00b68028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md#insn-00b68028) · [`00b6800c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b67/00b67ffc.md#insn-00b6800c)

~~~diff
- 00b67f58 ["INT_ADD", "register:40f0:8", ["const:b67f58:8", "const:4:8"]]
- 00b67f58 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68020 ["INT_ADD", "register:40f0:8", ["const:b68020:8", "const:4:8"]]
+ 00b68020 ["CALL", null, ["callee:00bde040:8"]]
- 00b67f58 bytes 0ed80194
+ 00b68020 bytes 08d80194
- 00b67f60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67f60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b68028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67f60 bytes 603204f9
+ 00b68028 bytes 609204f9
- 00b67f44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67f44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6800c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b6800c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67f44 bytes 683244f9
+ 00b6800c bytes 689244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab7a62efc99d00a195034adac8a0a41c"></a>

### [`00b67f74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f74.md) → [`00b6803c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6806c",
      "incomplete_value": true,
      "site": "00b6806c",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67fa4",
      "incomplete_value": true,
      "site": "00b67fa4",
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
            "const:860:8"
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
      "definition_site": "00b68050",
      "incomplete_value": true,
      "site": "00b68050",
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
      "definition_site": "00b67f88",
      "incomplete_value": true,
      "site": "00b67f88",
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
      "definition_site": "00b6805c",
      "incomplete_value": false,
      "site": "00b68064",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67f94",
      "incomplete_value": false,
      "site": "00b67f9c",
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
            "const:f4b:8"
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
      "00b6804c",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6805c",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b6806c",
      "WRITE",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6804c",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6805c",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b6806c",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f74.md#insn-00b67f9c) · [`00b67fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f74.md#insn-00b67fa4) · [`00b67f84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67f74.md#insn-00b67f84)
- 新版 [`00b68064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md#insn-00b68064) · [`00b6806c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md#insn-00b6806c) · [`00b6804c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6803c.md#insn-00b6804c)

~~~diff
- 00b67f9c ["INT_ADD", "register:40f0:8", ["const:b67f9c:8", "const:4:8"]]
- 00b67f9c ["CALL", null, ["callee:00bde040:8"]]
+ 00b68064 ["INT_ADD", "register:40f0:8", ["const:b68064:8", "const:4:8"]]
+ 00b68064 ["CALL", null, ["callee:00bde040:8"]]
- 00b67f9c bytes fdd70194
+ 00b68064 bytes f7d70194
- 00b67fa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67fa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6806c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b6806c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67fa4 bytes 603204f9
+ 00b6806c bytes 609204f9
- 00b67f84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67f84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6804c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b6804c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67f84 bytes 683244f9
+ 00b6804c bytes 689244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-008762f9f8c2c6d521039a63f8a03320"></a>

### [`00b67fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67fb8.md) → [`00b68080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md) _ZN8firebase4auth8auth_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b680b0",
      "incomplete_value": true,
      "site": "00b680b0",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67fe8",
      "incomplete_value": true,
      "site": "00b67fe8",
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
            "const:860:8"
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
      "definition_site": "00b68094",
      "incomplete_value": true,
      "site": "00b68094",
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
      "definition_site": "00b67fcc",
      "incomplete_value": true,
      "site": "00b67fcc",
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
      "definition_site": "00b6809c",
      "incomplete_value": false,
      "site": "00b680a8",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b67fd4",
      "incomplete_value": false,
      "site": "00b67fe0",
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
            "const:f4b:8"
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
      "00b68090",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6809c",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b680b0",
      "WRITE",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68090",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6809c",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b680b0",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67fb8.md#insn-00b67fe0) · [`00b67fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67fb8.md#insn-00b67fe8) · [`00b67fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b67/00b67fb8.md#insn-00b67fc8)
- 新版 [`00b680a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md#insn-00b680a8) · [`00b680b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md#insn-00b680b0) · [`00b68090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68080.md#insn-00b68090)

~~~diff
- 00b67fe0 ["INT_ADD", "register:40f0:8", ["const:b67fe0:8", "const:4:8"]]
- 00b67fe0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b680a8 ["INT_ADD", "register:40f0:8", ["const:b680a8:8", "const:4:8"]]
+ 00b680a8 ["CALL", null, ["callee:00bde040:8"]]
- 00b67fe0 bytes ecd70194
+ 00b680a8 bytes e6d70194
- 00b67fe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67fe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b680b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b680b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b67fe8 bytes 603204f9
+ 00b680b0 bytes 609204f9
- 00b67fc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:860:8"]]
- 00b67fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b68090 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b67fc8 bytes 683244f9
+ 00b68090 bytes 689244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30338246cfb144c0f2244621f0cbcc6a"></a>

### [`00b68008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68008.md) → [`00b680d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md) _ZN8firebase4auth8auth_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b68128",
      "incomplete_value": true,
      "site": "00b68128",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68060",
      "incomplete_value": true,
      "site": "00b68060",
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
            "const:868:8"
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
      "definition_site": "00b68104",
      "incomplete_value": true,
      "site": "00b68110",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6803c",
      "incomplete_value": true,
      "site": "00b68048",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:860:8"
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
      "00b680e4",
      "READ",
      [
        "storage",
        "010a1868",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68104",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68128",
      "WRITE",
      [
        "storage",
        "010a1868",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b680e4",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68104",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68128",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68008.md#insn-00b68048) · [`00b68060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68008.md#insn-00b68060) · [`00b6801c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68008.md#insn-00b6801c)
- 新版 [`00b68110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md#insn-00b68110) · [`00b68128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md#insn-00b68128) · [`00b680e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b680d0.md#insn-00b680e4)

~~~diff
- 00b68048 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68048 ["INT_ADD", "register:40f0:8", ["const:b68048:8", "const:4:8"]]
- 00b68048 ["CALLIND", null, ["register:0:8"]]
+ 00b68110 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68110 ["INT_ADD", "register:40f0:8", ["const:b68110:8", "const:4:8"]]
+ 00b68110 ["CALLIND", null, ["register:0:8"]]
- 00b68048 bytes 00013fd6
+ 00b68110 bytes 00013fd6
- 00b68060 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b68060 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:868:8"]]
- 00b68060 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b68128 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b68128 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
+ 00b68128 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68060 bytes a0a22139
+ 00b68128 bytes a0a22439
- 00b6801c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:868:8"]]
- 00b6801c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6801c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b680e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:928:8"]]
+ 00b680e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b680e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6801c bytes a8a26139
+ 00b680e4 bytes a8a26439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9d703cbef09bf1a7b7fa84c7978d8d2"></a>

### [`00b68074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68074.md) → [`00b6813c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md) _ZN8firebase4auth8auth_idp12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b68178",
      "incomplete_value": true,
      "site": "00b68178",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b680b0",
      "incomplete_value": true,
      "site": "00b680b0",
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
            "const:868:8"
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
      "definition_site": "00b68198",
      "incomplete_value": true,
      "site": "00b68198",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b680d0",
      "incomplete_value": true,
      "site": "00b680d0",
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
            "const:860:8"
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
      "definition_site": "00b68154",
      "incomplete_value": true,
      "site": "00b68154",
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
      "definition_site": "00b6808c",
      "incomplete_value": true,
      "site": "00b6808c",
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
      "00b68150",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6815c",
      "READ",
      [
        "storage",
        "010a1868",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68178",
      "WRITE",
      [
        "storage",
        "010a1868",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68150",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6815c",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68178",
      "WRITE",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b680b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68074.md#insn-00b680b0) · [`00b680cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68074.md#insn-00b680cc) · [`00b680d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68074.md#insn-00b680d0)
- 新版 [`00b68178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md#insn-00b68178) · [`00b68194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md#insn-00b68194) · [`00b68198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6813c.md#insn-00b68198)

~~~diff
- 00b680b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b680b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b680b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:868:8"]]
- 00b680b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b68178 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b68178 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b68178 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
+ 00b68178 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b680b0 bytes bfa22139
+ 00b68178 bytes bfa22439
- 00b680cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b680cc ["INT_ADD", "register:40f0:8", ["const:b680cc:8", "const:4:8"]]
- 00b680cc ["CALLIND", null, ["register:0:8"]]
+ 00b68194 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68194 ["INT_ADD", "register:40f0:8", ["const:b68194:8", "const:4:8"]]
+ 00b68194 ["CALLIND", null, ["register:0:8"]]
- 00b680cc bytes 00013fd6
+ 00b68194 bytes 00013fd6
- 00b680d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b680d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b680d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b68198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b68198 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b68198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b680d0 bytes 9f3204f9
+ 00b68198 bytes 9f9204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fc788087ee209b2e56495e29e1bd668"></a>

### [`00b680e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b680e4.md) → [`00b681ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md) _ZN8firebase4auth8auth_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b681ec",
      "incomplete_value": true,
      "site": "00b681ec",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68124",
      "incomplete_value": true,
      "site": "00b68124",
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
            "const:860:8"
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
      "definition_site": "00b681c8",
      "incomplete_value": true,
      "site": "00b681c8",
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
      "definition_site": "00b68100",
      "incomplete_value": true,
      "site": "00b68100",
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
      "definition_site": "00b681d0",
      "incomplete_value": false,
      "site": "00b681e4",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68108",
      "incomplete_value": false,
      "site": "00b6811c",
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
            "const:f4b:8"
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
      "00b681c0",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681d0",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b681ec",
      "WRITE",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b681c0",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b681d0",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b681ec",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6811c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b680e4.md#insn-00b6811c) · [`00b68124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b680e4.md#insn-00b68124) · [`00b680f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b680e4.md#insn-00b680f8)
- 新版 [`00b681e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md#insn-00b681e4) · [`00b681ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md#insn-00b681ec) · [`00b681c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b681ac.md#insn-00b681c0)

~~~diff
- 00b6811c ["INT_ADD", "register:40f0:8", ["const:b6811c:8", "const:4:8"]]
- 00b6811c ["CALL", null, ["callee:00bde040:8"]]
+ 00b681e4 ["INT_ADD", "register:40f0:8", ["const:b681e4:8", "const:4:8"]]
+ 00b681e4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6811c bytes 9dd70194
+ 00b681e4 bytes 97d70194
- 00b68124 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b68124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b681ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b681ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68124 bytes 803204f9
+ 00b681ec bytes 809204f9
- 00b680f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b680f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b681c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b681c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b680f8 bytes 813244f9
+ 00b681c0 bytes 819244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e49b401a981ed55f74210b9bc8e4aa"></a>

### [`00b68154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68154.md) → [`00b6821c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md) _ZN8firebase4auth8auth_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b68238",
      "incomplete_value": false,
      "site": "00b6823c",
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
      "definition_site": "00b68170",
      "incomplete_value": false,
      "site": "00b68174",
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
      "definition_site": "00b68248",
      "incomplete_value": true,
      "site": "00b68254",
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
      "definition_site": "00b68180",
      "incomplete_value": true,
      "site": "00b6818c",
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
      "00b68238",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b68248",
      "DATA",
      [
        "storage",
        "010a1870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68238",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b68248",
      "DATA",
      [
        "storage",
        "010a1930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68154.md#insn-00b68174) · [`00b68170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68154.md#insn-00b68170) · [`00b6817c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68154.md#insn-00b6817c)
- 新版 [`00b6823c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md#insn-00b6823c) · [`00b68238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md#insn-00b68238) · [`00b68244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6821c.md#insn-00b68244)

~~~diff
- 00b68174 ["INT_ADD", "register:40f0:8", ["const:b68174:8", "const:4:8"]]
- 00b68174 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6823c ["INT_ADD", "register:40f0:8", ["const:b6823c:8", "const:4:8"]]
+ 00b6823c ["CALL", null, ["callee:00bde130:8"]]
- 00b68174 bytes c3d70194
+ 00b6823c bytes bdd70194
- 00b68170 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b68170 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68170 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68170 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68238 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b68238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68170 bytes 001c1591
+ 00b68238 bytes 00501791
- 00b6817c ["COPY", "tmp:0:8", ["const:870:8"]]
- 00b6817c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6817c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6817c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68244 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00b68244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6817c bytes 08c12191
+ 00b68244 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7d27d39cf20eee4df674ee09a443c3a"></a>

### [`00b68190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68190.md) → [`00b68258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md) _ZN8firebase4auth8auth_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68298",
      "incomplete_value": true,
      "site": "00b68298",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b681d0",
      "incomplete_value": true,
      "site": "00b681d0",
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
            "const:860:8"
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
      "definition_site": "00b68274",
      "incomplete_value": true,
      "site": "00b68274",
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
      "definition_site": "00b681ac",
      "incomplete_value": true,
      "site": "00b681ac",
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
      "definition_site": "00b6827c",
      "incomplete_value": false,
      "site": "00b68290",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b681b4",
      "incomplete_value": false,
      "site": "00b681c8",
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
            "const:f4b:8"
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
      "00b6826c",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6827c",
      "PARAM",
      [
        "storage",
        "0029bf4b",
        null,
        "string"
      ]
    ],
    [
      "00b68298",
      "WRITE",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6826c",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6827c",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b68298",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b681c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68190.md#insn-00b681c8) · [`00b681d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68190.md#insn-00b681d0) · [`00b681a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68190.md#insn-00b681a4)
- 新版 [`00b68290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md#insn-00b68290) · [`00b68298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md#insn-00b68298) · [`00b6826c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68258.md#insn-00b6826c)

~~~diff
- 00b681c8 ["INT_ADD", "register:40f0:8", ["const:b681c8:8", "const:4:8"]]
- 00b681c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68290 ["INT_ADD", "register:40f0:8", ["const:b68290:8", "const:4:8"]]
+ 00b68290 ["CALL", null, ["callee:00bde040:8"]]
- 00b681c8 bytes 72d70194
+ 00b68290 bytes 6cd70194
- 00b681d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b681d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68298 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b68298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b681d0 bytes 803204f9
+ 00b68298 bytes 809204f9
- 00b681a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b681a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6826c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b6826c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b681a4 bytes 813244f9
+ 00b6826c bytes 819244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68e0d3addf5159e0cf7ba0dbf9b00015"></a>

### [`00b68200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68200.md) → [`00b682c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md) _ZN8firebase4auth8auth_idp10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b682e4",
      "incomplete_value": false,
      "site": "00b682e8",
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
      "definition_site": "00b6821c",
      "incomplete_value": false,
      "site": "00b68220",
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
      "definition_site": "00b682f4",
      "incomplete_value": true,
      "site": "00b68300",
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
      "definition_site": "00b6822c",
      "incomplete_value": true,
      "site": "00b68238",
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
      "00b682e4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b682f4",
      "DATA",
      [
        "storage",
        "010a1878",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b682e4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b682f4",
      "DATA",
      [
        "storage",
        "010a1938",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68200.md#insn-00b68220) · [`00b6821c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68200.md#insn-00b6821c) · [`00b68228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68200.md#insn-00b68228)
- 新版 [`00b682e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md#insn-00b682e8) · [`00b682e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md#insn-00b682e4) · [`00b682f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b682c8.md#insn-00b682f0)

~~~diff
- 00b68220 ["INT_ADD", "register:40f0:8", ["const:b68220:8", "const:4:8"]]
- 00b68220 ["CALL", null, ["callee:00bde130:8"]]
+ 00b682e8 ["INT_ADD", "register:40f0:8", ["const:b682e8:8", "const:4:8"]]
+ 00b682e8 ["CALL", null, ["callee:00bde130:8"]]
- 00b68220 bytes 98d70194
+ 00b682e8 bytes 92d70194
- 00b6821c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6821c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6821c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6821c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b682e4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b682e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b682e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b682e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6821c bytes 00c81791
+ 00b682e4 bytes 00fc1991
- 00b68228 ["COPY", "tmp:0:8", ["const:878:8"]]
- 00b68228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b682f0 ["COPY", "tmp:0:8", ["const:938:8"]]
+ 00b682f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b682f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b682f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68228 bytes 08e12191
+ 00b682f0 bytes 08e12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a332b8f438dc8f687d47a26e4a52cf12"></a>

### [`00b6823c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6823c.md) → [`00b68304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b68330",
      "incomplete_value": true,
      "site": "00b68330",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68268",
      "incomplete_value": true,
      "site": "00b68268",
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
            "const:880:8"
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
      "definition_site": "00b68318",
      "incomplete_value": true,
      "site": "00b68318",
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
      "definition_site": "00b68250",
      "incomplete_value": true,
      "site": "00b68250",
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
      "definition_site": "00b68324",
      "incomplete_value": false,
      "site": "00b68328",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6825c",
      "incomplete_value": false,
      "site": "00b68260",
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
            "const:8e1:8"
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
      "00b68314",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68324",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b68330",
      "WRITE",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68314",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68324",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b68330",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6823c.md#insn-00b68260) · [`00b68268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6823c.md#insn-00b68268) · [`00b6824c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6823c.md#insn-00b6824c)
- 新版 [`00b68328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md#insn-00b68328) · [`00b68330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md#insn-00b68330) · [`00b68314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68304.md#insn-00b68314)

~~~diff
- 00b68260 ["INT_ADD", "register:40f0:8", ["const:b68260:8", "const:4:8"]]
- 00b68260 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68328 ["INT_ADD", "register:40f0:8", ["const:b68328:8", "const:4:8"]]
+ 00b68328 ["CALL", null, ["callee:00bde040:8"]]
- 00b68260 bytes 4cd70194
+ 00b68328 bytes 46d70194
- 00b68268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b68268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b68330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68268 bytes 604204f9
+ 00b68330 bytes 60a204f9
- 00b6824c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b6824c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b68314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6824c bytes 684244f9
+ 00b68314 bytes 68a244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-844cc4a71dda207e5d9524737d9c62e5"></a>

### [`00b6827c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6827c.md) → [`00b68344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md) _ZN8firebase4auth8user_idp19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b68370",
      "incomplete_value": true,
      "site": "00b68370",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b682a8",
      "incomplete_value": true,
      "site": "00b682a8",
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
            "const:880:8"
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
      "definition_site": "00b68358",
      "incomplete_value": true,
      "site": "00b68358",
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
      "definition_site": "00b68290",
      "incomplete_value": true,
      "site": "00b68290",
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
      "definition_site": "00b68360",
      "incomplete_value": false,
      "site": "00b68368",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68298",
      "incomplete_value": false,
      "site": "00b682a0",
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
            "const:8e1:8"
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
      "00b68354",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68360",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b68370",
      "WRITE",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68354",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68360",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b68370",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b682a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6827c.md#insn-00b682a0) · [`00b682a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6827c.md#insn-00b682a8) · [`00b6828c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6827c.md#insn-00b6828c)
- 新版 [`00b68368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md#insn-00b68368) · [`00b68370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md#insn-00b68370) · [`00b68354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68344.md#insn-00b68354)

~~~diff
- 00b682a0 ["INT_ADD", "register:40f0:8", ["const:b682a0:8", "const:4:8"]]
- 00b682a0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68368 ["INT_ADD", "register:40f0:8", ["const:b68368:8", "const:4:8"]]
+ 00b68368 ["CALL", null, ["callee:00bde040:8"]]
- 00b682a0 bytes 3cd70194
+ 00b68368 bytes 36d70194
- 00b682a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b682a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b68370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b682a8 bytes 604204f9
+ 00b68370 bytes 60a204f9
- 00b6828c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b6828c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b68354 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6828c bytes 684244f9
+ 00b68354 bytes 68a244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a54430ecc7bd485d3c55fc39fb2463f"></a>

### [`00b682bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b682bc.md) → [`00b68384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b683b4",
      "incomplete_value": true,
      "site": "00b683b4",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b682ec",
      "incomplete_value": true,
      "site": "00b682ec",
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
            "const:880:8"
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
      "definition_site": "00b68398",
      "incomplete_value": true,
      "site": "00b68398",
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
      "definition_site": "00b682d0",
      "incomplete_value": true,
      "site": "00b682d0",
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
      "definition_site": "00b683a4",
      "incomplete_value": false,
      "site": "00b683ac",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b682dc",
      "incomplete_value": false,
      "site": "00b682e4",
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
            "const:8e1:8"
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
      "00b68394",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683a4",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b683b4",
      "WRITE",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68394",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683a4",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b683b4",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b682e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b682bc.md#insn-00b682e4) · [`00b682ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b682bc.md#insn-00b682ec) · [`00b682cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b682bc.md#insn-00b682cc)
- 新版 [`00b683ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md#insn-00b683ac) · [`00b683b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md#insn-00b683b4) · [`00b68394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68384.md#insn-00b68394)

~~~diff
- 00b682e4 ["INT_ADD", "register:40f0:8", ["const:b682e4:8", "const:4:8"]]
- 00b682e4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b683ac ["INT_ADD", "register:40f0:8", ["const:b683ac:8", "const:4:8"]]
+ 00b683ac ["CALL", null, ["callee:00bde040:8"]]
- 00b682e4 bytes 2bd70194
+ 00b683ac bytes 25d70194
- 00b682ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b682ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b683b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b683b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b682ec bytes 604204f9
+ 00b683b4 bytes 60a204f9
- 00b682cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b682cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b68394 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b682cc bytes 684244f9
+ 00b68394 bytes 68a244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9d538e9fda485a74454fc442ffc9d40"></a>

### [`00b68300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68300.md) → [`00b683c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md) _ZN8firebase4auth8user_idp10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b683f8",
      "incomplete_value": true,
      "site": "00b683f8",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68330",
      "incomplete_value": true,
      "site": "00b68330",
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
            "const:880:8"
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
      "definition_site": "00b683dc",
      "incomplete_value": true,
      "site": "00b683dc",
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
      "definition_site": "00b68314",
      "incomplete_value": true,
      "site": "00b68314",
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
      "definition_site": "00b683e4",
      "incomplete_value": false,
      "site": "00b683f0",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6831c",
      "incomplete_value": false,
      "site": "00b68328",
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
            "const:8e1:8"
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
      "00b683d8",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683e4",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b683f8",
      "WRITE",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b683d8",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b683e4",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b683f8",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68300.md#insn-00b68328) · [`00b68330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68300.md#insn-00b68330) · [`00b68310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68300.md#insn-00b68310)
- 新版 [`00b683f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md#insn-00b683f0) · [`00b683f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md#insn-00b683f8) · [`00b683d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b683c8.md#insn-00b683d8)

~~~diff
- 00b68328 ["INT_ADD", "register:40f0:8", ["const:b68328:8", "const:4:8"]]
- 00b68328 ["CALL", null, ["callee:00bde040:8"]]
+ 00b683f0 ["INT_ADD", "register:40f0:8", ["const:b683f0:8", "const:4:8"]]
+ 00b683f0 ["CALL", null, ["callee:00bde040:8"]]
- 00b68328 bytes 1ad70194
+ 00b683f0 bytes 14d70194
- 00b68330 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b68330 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b683f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b683f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68330 bytes 604204f9
+ 00b683f8 bytes 60a204f9
- 00b68310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b68310 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b683d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b683d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68310 bytes 684244f9
+ 00b683d8 bytes 68a244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbdf34e3ecd55569493715ca7a54867f"></a>

### [`00b68350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68350.md) → [`00b68418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md) _ZN8firebase4auth8user_idp15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b68470",
      "incomplete_value": true,
      "site": "00b68470",
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
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b683a8",
      "incomplete_value": true,
      "site": "00b683a8",
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
            "const:888:8"
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
      "definition_site": "00b6844c",
      "incomplete_value": true,
      "site": "00b68458",
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
                "const:10a1000:8"
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
    "old": {
      "definition_site": "00b68384",
      "incomplete_value": true,
      "site": "00b68390",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:880:8"
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
      "00b6842c",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6844c",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68470",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6842c",
      "READ",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6844c",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68470",
      "WRITE",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68350.md#insn-00b68390) · [`00b683a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68350.md#insn-00b683a8) · [`00b68364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68350.md#insn-00b68364)
- 新版 [`00b68458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md#insn-00b68458) · [`00b68470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md#insn-00b68470) · [`00b6842c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68418.md#insn-00b6842c)

~~~diff
- 00b68390 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68390 ["INT_ADD", "register:40f0:8", ["const:b68390:8", "const:4:8"]]
- 00b68390 ["CALLIND", null, ["register:0:8"]]
+ 00b68458 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68458 ["INT_ADD", "register:40f0:8", ["const:b68458:8", "const:4:8"]]
+ 00b68458 ["CALLIND", null, ["register:0:8"]]
- 00b68390 bytes 00013fd6
+ 00b68458 bytes 00013fd6
- 00b683a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b683a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:888:8"]]
- 00b683a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b68470 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b68470 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:948:8"]]
+ 00b68470 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b683a8 bytes a0222239
+ 00b68470 bytes a0222539
- 00b68364 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:888:8"]]
- 00b68364 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b68364 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6842c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:948:8"]]
+ 00b6842c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6842c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b68364 bytes a8226239
+ 00b6842c bytes a8226539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fe9bcdf5c355ef7de53e3d1d125fde"></a>

### [`00b683bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b683bc.md) → [`00b68484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md) _ZN8firebase4auth8user_idp12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b684c0",
      "incomplete_value": true,
      "site": "00b684c0",
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
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b683f8",
      "incomplete_value": true,
      "site": "00b683f8",
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
            "const:888:8"
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
      "definition_site": "00b684e0",
      "incomplete_value": true,
      "site": "00b684e0",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68418",
      "incomplete_value": true,
      "site": "00b68418",
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
            "const:880:8"
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
      "definition_site": "00b6849c",
      "incomplete_value": true,
      "site": "00b6849c",
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
      "definition_site": "00b683d4",
      "incomplete_value": true,
      "site": "00b683d4",
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
      "00b68498",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b684a4",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b684c0",
      "WRITE",
      [
        "storage",
        "010a1888",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68498",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b684a4",
      "READ",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ],
    [
      "00b684c0",
      "WRITE",
      [
        "storage",
        "010a1948",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b683f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b683bc.md#insn-00b683f8) · [`00b68414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b683bc.md#insn-00b68414) · [`00b68418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b683bc.md#insn-00b68418)
- 新版 [`00b684c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md#insn-00b684c0) · [`00b684dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md#insn-00b684dc) · [`00b684e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68484.md#insn-00b684e0)

~~~diff
- 00b683f8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b683f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b683f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:888:8"]]
- 00b683f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b684c0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b684c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b684c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:948:8"]]
+ 00b684c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b683f8 bytes bf222239
+ 00b684c0 bytes bf222539
- 00b68414 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68414 ["INT_ADD", "register:40f0:8", ["const:b68414:8", "const:4:8"]]
- 00b68414 ["CALLIND", null, ["register:0:8"]]
+ 00b684dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b684dc ["INT_ADD", "register:40f0:8", ["const:b684dc:8", "const:4:8"]]
+ 00b684dc ["CALLIND", null, ["register:0:8"]]
- 00b68414 bytes 00013fd6
+ 00b684dc bytes 00013fd6
- 00b68418 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b68418 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b68418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b684e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b684e0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b684e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b68418 bytes 9f4204f9
+ 00b684e0 bytes 9fa204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-769aa67fbdc6ce4c1584969976e8e3d4"></a>

### [`00b6842c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6842c.md) → [`00b684f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md) _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68534",
      "incomplete_value": true,
      "site": "00b68534",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6846c",
      "incomplete_value": true,
      "site": "00b6846c",
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
            "const:880:8"
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
      "definition_site": "00b68510",
      "incomplete_value": true,
      "site": "00b68510",
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
      "definition_site": "00b68448",
      "incomplete_value": true,
      "site": "00b68448",
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
      "definition_site": "00b68518",
      "incomplete_value": false,
      "site": "00b6852c",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68450",
      "incomplete_value": false,
      "site": "00b68464",
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
            "const:8e1:8"
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
      "00b68508",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68518",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b68534",
      "WRITE",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68508",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68518",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b68534",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6842c.md#insn-00b68464) · [`00b6846c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6842c.md#insn-00b6846c) · [`00b68440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6842c.md#insn-00b68440)
- 新版 [`00b6852c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md#insn-00b6852c) · [`00b68534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md#insn-00b68534) · [`00b68508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b684f4.md#insn-00b68508)

~~~diff
- 00b68464 ["INT_ADD", "register:40f0:8", ["const:b68464:8", "const:4:8"]]
- 00b68464 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6852c ["INT_ADD", "register:40f0:8", ["const:b6852c:8", "const:4:8"]]
+ 00b6852c ["CALL", null, ["callee:00bde040:8"]]
- 00b68464 bytes cbd60194
+ 00b6852c bytes c5d60194
- 00b6846c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b6846c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68534 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b68534 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6846c bytes 804204f9
+ 00b68534 bytes 80a204f9
- 00b68440 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b68440 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68508 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b68508 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68440 bytes 814244f9
+ 00b68508 bytes 81a244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58fac2b7798b120ec1c2e2872427a7a"></a>

### [`00b6849c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6849c.md) → [`00b68564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md) _ZN8firebase4auth8user_idp11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b68580",
      "incomplete_value": false,
      "site": "00b68584",
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
      "definition_site": "00b684b8",
      "incomplete_value": false,
      "site": "00b684bc",
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
      "definition_site": "00b68590",
      "incomplete_value": true,
      "site": "00b6859c",
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
      "definition_site": "00b684c8",
      "incomplete_value": true,
      "site": "00b684d4",
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
      "00b68580",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b68590",
      "DATA",
      [
        "storage",
        "010a1890",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68580",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b68590",
      "DATA",
      [
        "storage",
        "010a1950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b684bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6849c.md#insn-00b684bc) · [`00b684b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6849c.md#insn-00b684b8) · [`00b684c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6849c.md#insn-00b684c4)
- 新版 [`00b68584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md#insn-00b68584) · [`00b68580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md#insn-00b68580) · [`00b6858c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68564.md#insn-00b6858c)

~~~diff
- 00b684bc ["INT_ADD", "register:40f0:8", ["const:b684bc:8", "const:4:8"]]
- 00b684bc ["CALL", null, ["callee:00bde130:8"]]
+ 00b68584 ["INT_ADD", "register:40f0:8", ["const:b68584:8", "const:4:8"]]
+ 00b68584 ["CALL", null, ["callee:00bde130:8"]]
- 00b684bc bytes f1d60194
+ 00b68584 bytes ebd60194
- 00b684b8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b684b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b684b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b684b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68580 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b68580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b684b8 bytes 001c1591
+ 00b68580 bytes 00501791
- 00b684c4 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00b684c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b684c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b684c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6858c ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00b6858c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6858c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6858c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b684c4 bytes 08412291
+ 00b6858c bytes 08412591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c54f74f94a4582eccfd3424e33125694"></a>

### [`00b684d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b684d8.md) → [`00b685a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md) _ZN8firebase4auth8user_idp13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b685e0",
      "incomplete_value": true,
      "site": "00b685e0",
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
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68518",
      "incomplete_value": true,
      "site": "00b68518",
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
            "const:880:8"
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
      "definition_site": "00b685bc",
      "incomplete_value": true,
      "site": "00b685bc",
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
      "definition_site": "00b684f4",
      "incomplete_value": true,
      "site": "00b684f4",
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
      "definition_site": "00b685c4",
      "incomplete_value": false,
      "site": "00b685d8",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b684fc",
      "incomplete_value": false,
      "site": "00b68510",
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
            "const:8e1:8"
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
      "00b685b4",
      "READ",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b685c4",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b685e0",
      "WRITE",
      [
        "storage",
        "010a1880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b685b4",
      "READ",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b685c4",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b685e0",
      "WRITE",
      [
        "storage",
        "010a1940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b684d8.md#insn-00b68510) · [`00b68518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b684d8.md#insn-00b68518) · [`00b684ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b684d8.md#insn-00b684ec)
- 新版 [`00b685d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md#insn-00b685d8) · [`00b685e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md#insn-00b685e0) · [`00b685b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b685a0.md#insn-00b685b4)

~~~diff
- 00b68510 ["INT_ADD", "register:40f0:8", ["const:b68510:8", "const:4:8"]]
- 00b68510 ["CALL", null, ["callee:00bde040:8"]]
+ 00b685d8 ["INT_ADD", "register:40f0:8", ["const:b685d8:8", "const:4:8"]]
+ 00b685d8 ["CALL", null, ["callee:00bde040:8"]]
- 00b68510 bytes a0d60194
+ 00b685d8 bytes 9ad60194
- 00b68518 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b68518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b685e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b685e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68518 bytes 804204f9
+ 00b685e0 bytes 80a204f9
- 00b684ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b684ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b685b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b685b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b684ec bytes 814244f9
+ 00b685b4 bytes 81a244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-609416ceb636e07863cf632ca3641f1e"></a>

### [`00b68548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68548.md) → [`00b68610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md) _ZN8firebase4auth8user_idp10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6862c",
      "incomplete_value": false,
      "site": "00b68630",
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
      "definition_site": "00b68564",
      "incomplete_value": false,
      "site": "00b68568",
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
      "definition_site": "00b6863c",
      "incomplete_value": true,
      "site": "00b68648",
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
      "definition_site": "00b68574",
      "incomplete_value": true,
      "site": "00b68580",
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
      "00b6862c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6863c",
      "DATA",
      [
        "storage",
        "010a18a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6862c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6863c",
      "DATA",
      [
        "storage",
        "010a1960",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68548.md#insn-00b68568) · [`00b68564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68548.md#insn-00b68564) · [`00b68570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68548.md#insn-00b68570)
- 新版 [`00b68630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md#insn-00b68630) · [`00b6862c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md#insn-00b6862c) · [`00b68638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68610.md#insn-00b68638)

~~~diff
- 00b68568 ["INT_ADD", "register:40f0:8", ["const:b68568:8", "const:4:8"]]
- 00b68568 ["CALL", null, ["callee:00bde130:8"]]
+ 00b68630 ["INT_ADD", "register:40f0:8", ["const:b68630:8", "const:4:8"]]
+ 00b68630 ["CALL", null, ["callee:00bde130:8"]]
- 00b68568 bytes c6d60194
+ 00b68630 bytes c0d60194
- 00b68564 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b68564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6862c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b6862c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6862c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6862c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68564 bytes 00c81791
+ 00b6862c bytes 00fc1991
- 00b68570 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00b68570 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68570 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68570 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68638 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00b68638 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68638 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68638 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68570 bytes 08812291
+ 00b68638 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd4a286ed777fcc1d1855227e19b47b"></a>

### [`00b68584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68584.md) → [`00b6864c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

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
      "definition_site": "00b68678",
      "incomplete_value": true,
      "site": "00b68678",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b685b0",
      "incomplete_value": true,
      "site": "00b685b0",
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
            "const:8a8:8"
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
      "definition_site": "00b68660",
      "incomplete_value": true,
      "site": "00b68660",
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
      "definition_site": "00b68598",
      "incomplete_value": true,
      "site": "00b68598",
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
      "definition_site": "00b6866c",
      "incomplete_value": false,
      "site": "00b68670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b685a4",
      "incomplete_value": false,
      "site": "00b685a8",
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
            "const:f9e:8"
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
      "00b6865c",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6866c",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b68678",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6865c",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6866c",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68678",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b685a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68584.md#insn-00b685a8) · [`00b685b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68584.md#insn-00b685b0) · [`00b68594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68584.md#insn-00b68594)
- 新版 [`00b68670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md#insn-00b68670) · [`00b68678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md#insn-00b68678) · [`00b6865c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6864c.md#insn-00b6865c)

~~~diff
- 00b685a8 ["INT_ADD", "register:40f0:8", ["const:b685a8:8", "const:4:8"]]
- 00b685a8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68670 ["INT_ADD", "register:40f0:8", ["const:b68670:8", "const:4:8"]]
+ 00b68670 ["CALL", null, ["callee:00bde040:8"]]
- 00b685a8 bytes 7ad60194
+ 00b68670 bytes 74d60194
- 00b685b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b685b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b68678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b685b0 bytes 605604f9
+ 00b68678 bytes 60b604f9
- 00b68594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b68594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6865c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b6865c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68594 bytes 685644f9
+ 00b6865c bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90294bd2f7c215567600dc764028af44"></a>

### [`00b685c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b685c4.md) → [`00b6868c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md) _ZN8firebase4auth8jniphone19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b686b8",
      "incomplete_value": true,
      "site": "00b686b8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b685f0",
      "incomplete_value": true,
      "site": "00b685f0",
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
            "const:8a8:8"
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
      "definition_site": "00b686a0",
      "incomplete_value": true,
      "site": "00b686a0",
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
      "definition_site": "00b685d8",
      "incomplete_value": true,
      "site": "00b685d8",
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
      "definition_site": "00b686a8",
      "incomplete_value": false,
      "site": "00b686b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b685e0",
      "incomplete_value": false,
      "site": "00b685e8",
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
            "const:f9e:8"
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
      "00b6869c",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686a8",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b686b8",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6869c",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686a8",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b686b8",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b685e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b685c4.md#insn-00b685e8) · [`00b685f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b685c4.md#insn-00b685f0) · [`00b685d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b685c4.md#insn-00b685d4)
- 新版 [`00b686b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md#insn-00b686b0) · [`00b686b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md#insn-00b686b8) · [`00b6869c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6868c.md#insn-00b6869c)

~~~diff
- 00b685e8 ["INT_ADD", "register:40f0:8", ["const:b685e8:8", "const:4:8"]]
- 00b685e8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b686b0 ["INT_ADD", "register:40f0:8", ["const:b686b0:8", "const:4:8"]]
+ 00b686b0 ["CALL", null, ["callee:00bde040:8"]]
- 00b685e8 bytes 6ad60194
+ 00b686b0 bytes 64d60194
- 00b685f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b685f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b686b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b686b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b685f0 bytes 605604f9
+ 00b686b8 bytes 60b604f9
- 00b685d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b685d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6869c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b6869c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b685d4 bytes 685644f9
+ 00b6869c bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62ca8a98fdcd2b9e56d0f51a1b058c30"></a>

### [`00b68604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68604.md) → [`00b686cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b686fc",
      "incomplete_value": true,
      "site": "00b686fc",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68634",
      "incomplete_value": true,
      "site": "00b68634",
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
            "const:8a8:8"
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
      "definition_site": "00b686e0",
      "incomplete_value": true,
      "site": "00b686e0",
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
      "definition_site": "00b68618",
      "incomplete_value": true,
      "site": "00b68618",
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
      "definition_site": "00b686ec",
      "incomplete_value": false,
      "site": "00b686f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68624",
      "incomplete_value": false,
      "site": "00b6862c",
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
            "const:f9e:8"
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
      "00b686dc",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686ec",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b686fc",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b686dc",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b686ec",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b686fc",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6862c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68604.md#insn-00b6862c) · [`00b68634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68604.md#insn-00b68634) · [`00b68614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68604.md#insn-00b68614)
- 新版 [`00b686f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md#insn-00b686f4) · [`00b686fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md#insn-00b686fc) · [`00b686dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b686cc.md#insn-00b686dc)

~~~diff
- 00b6862c ["INT_ADD", "register:40f0:8", ["const:b6862c:8", "const:4:8"]]
- 00b6862c ["CALL", null, ["callee:00bde040:8"]]
+ 00b686f4 ["INT_ADD", "register:40f0:8", ["const:b686f4:8", "const:4:8"]]
+ 00b686f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6862c bytes 59d60194
+ 00b686f4 bytes 53d60194
- 00b68634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b68634 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b686fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b686fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68634 bytes 605604f9
+ 00b686fc bytes 60b604f9
- 00b68614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b68614 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b686dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b686dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68614 bytes 685644f9
+ 00b686dc bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a86a60383967ec2d8fec2837af70485"></a>

### [`00b68648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68648.md) → [`00b68710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md) _ZN8firebase4auth8jniphone10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68740",
      "incomplete_value": true,
      "site": "00b68740",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68678",
      "incomplete_value": true,
      "site": "00b68678",
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
            "const:8a8:8"
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
      "definition_site": "00b68724",
      "incomplete_value": true,
      "site": "00b68724",
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
      "definition_site": "00b6865c",
      "incomplete_value": true,
      "site": "00b6865c",
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
      "definition_site": "00b6872c",
      "incomplete_value": false,
      "site": "00b68738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68664",
      "incomplete_value": false,
      "site": "00b68670",
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
            "const:f9e:8"
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
      "00b68720",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6872c",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b68740",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68720",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6872c",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68740",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68648.md#insn-00b68670) · [`00b68678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68648.md#insn-00b68678) · [`00b68658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68648.md#insn-00b68658)
- 新版 [`00b68738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md#insn-00b68738) · [`00b68740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md#insn-00b68740) · [`00b68720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68710.md#insn-00b68720)

~~~diff
- 00b68670 ["INT_ADD", "register:40f0:8", ["const:b68670:8", "const:4:8"]]
- 00b68670 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68738 ["INT_ADD", "register:40f0:8", ["const:b68738:8", "const:4:8"]]
+ 00b68738 ["CALL", null, ["callee:00bde040:8"]]
- 00b68670 bytes 48d60194
+ 00b68738 bytes 42d60194
- 00b68678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b68678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b68740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68678 bytes 605604f9
+ 00b68740 bytes 60b604f9
- 00b68658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b68658 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b68720 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68658 bytes 685644f9
+ 00b68720 bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdb9b212c1df1084fcd89a34dd6f081e"></a>

### [`00b68698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68698.md) → [`00b68760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md) _ZN8firebase4auth8jniphone15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b687b8",
      "incomplete_value": true,
      "site": "00b687b8",
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
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686f0",
      "incomplete_value": true,
      "site": "00b686f0",
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
            "const:8b0:8"
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
      "definition_site": "00b68794",
      "incomplete_value": true,
      "site": "00b687a0",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b686cc",
      "incomplete_value": true,
      "site": "00b686d8",
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
                "const:10a1000:8"
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
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b68774",
      "READ",
      [
        "storage",
        "010a18b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68794",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b687b8",
      "WRITE",
      [
        "storage",
        "010a18b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68774",
      "READ",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68794",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b687b8",
      "WRITE",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b686d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68698.md#insn-00b686d8) · [`00b686f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68698.md#insn-00b686f0) · [`00b686ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68698.md#insn-00b686ac)
- 新版 [`00b687a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md#insn-00b687a0) · [`00b687b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md#insn-00b687b8) · [`00b68774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68760.md#insn-00b68774)

~~~diff
- 00b686d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b686d8 ["INT_ADD", "register:40f0:8", ["const:b686d8:8", "const:4:8"]]
- 00b686d8 ["CALLIND", null, ["register:0:8"]]
+ 00b687a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b687a0 ["INT_ADD", "register:40f0:8", ["const:b687a0:8", "const:4:8"]]
+ 00b687a0 ["CALLIND", null, ["register:0:8"]]
- 00b686d8 bytes 00013fd6
+ 00b687a0 bytes 00013fd6
- 00b686f0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b686f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b0:8"]]
- 00b686f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b687b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b687b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
+ 00b687b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b686f0 bytes a0c22239
+ 00b687b8 bytes a0c22539
- 00b686ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8b0:8"]]
- 00b686ac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b686ac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b68774 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
+ 00b68774 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b68774 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b686ac bytes a8c26239
+ 00b68774 bytes a8c26539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-306e0bcccb93bb3fa0fba1cb9cb457d4"></a>

### [`00b68704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68704.md) → [`00b687cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md) _ZN8firebase4auth8jniphone12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b68808",
      "incomplete_value": true,
      "site": "00b68808",
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
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68740",
      "incomplete_value": true,
      "site": "00b68740",
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
            "const:8b0:8"
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
      "definition_site": "00b68828",
      "incomplete_value": true,
      "site": "00b68828",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68760",
      "incomplete_value": true,
      "site": "00b68760",
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
            "const:8a8:8"
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
      "definition_site": "00b687e4",
      "incomplete_value": true,
      "site": "00b687e4",
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
      "definition_site": "00b6871c",
      "incomplete_value": true,
      "site": "00b6871c",
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
      "00b687e0",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b687ec",
      "READ",
      [
        "storage",
        "010a18b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68808",
      "WRITE",
      [
        "storage",
        "010a18b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b687e0",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b687ec",
      "READ",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68808",
      "WRITE",
      [
        "storage",
        "010a1970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68704.md#insn-00b68740) · [`00b6875c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68704.md#insn-00b6875c) · [`00b68760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68704.md#insn-00b68760)
- 新版 [`00b68808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md#insn-00b68808) · [`00b68824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md#insn-00b68824) · [`00b68828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b687cc.md#insn-00b68828)

~~~diff
- 00b68740 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68740 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68740 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
- 00b68740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b68808 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b68808 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b68808 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:970:8"]]
+ 00b68808 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68740 bytes bfc22239
+ 00b68808 bytes bfc22539
- 00b6875c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6875c ["INT_ADD", "register:40f0:8", ["const:b6875c:8", "const:4:8"]]
- 00b6875c ["CALLIND", null, ["register:0:8"]]
+ 00b68824 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68824 ["INT_ADD", "register:40f0:8", ["const:b68824:8", "const:4:8"]]
+ 00b68824 ["CALLIND", null, ["register:0:8"]]
- 00b6875c bytes 00013fd6
+ 00b68824 bytes 00013fd6
- 00b68760 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b68760 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b68760 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b68828 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b68828 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b68828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b68760 bytes 9f5604f9
+ 00b68828 bytes 9fb604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56309107fa18b15a1234962d0287c889"></a>

### [`00b68774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68774.md) → [`00b6883c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md) _ZN8firebase4auth8jniphone14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6887c",
      "incomplete_value": true,
      "site": "00b6887c",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b687b4",
      "incomplete_value": true,
      "site": "00b687b4",
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
            "const:8a8:8"
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
      "definition_site": "00b68858",
      "incomplete_value": true,
      "site": "00b68858",
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
      "definition_site": "00b68790",
      "incomplete_value": true,
      "site": "00b68790",
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
      "definition_site": "00b68860",
      "incomplete_value": false,
      "site": "00b68874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68798",
      "incomplete_value": false,
      "site": "00b687ac",
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
            "const:f9e:8"
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
      "00b68850",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68860",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b6887c",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68850",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68860",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b6887c",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b687ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68774.md#insn-00b687ac) · [`00b687b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68774.md#insn-00b687b4) · [`00b68788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68774.md#insn-00b68788)
- 新版 [`00b68874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md#insn-00b68874) · [`00b6887c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md#insn-00b6887c) · [`00b68850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b6883c.md#insn-00b68850)

~~~diff
- 00b687ac ["INT_ADD", "register:40f0:8", ["const:b687ac:8", "const:4:8"]]
- 00b687ac ["CALL", null, ["callee:00bde040:8"]]
+ 00b68874 ["INT_ADD", "register:40f0:8", ["const:b68874:8", "const:4:8"]]
+ 00b68874 ["CALL", null, ["callee:00bde040:8"]]
- 00b687ac bytes f9d50194
+ 00b68874 bytes f3d50194
- 00b687b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b687b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6887c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b6887c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b687b4 bytes 805604f9
+ 00b6887c bytes 80b604f9
- 00b68788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b68788 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68850 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b68850 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68788 bytes 815644f9
+ 00b68850 bytes 81b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d56aa52ffc9145b40a31adcad620aa"></a>

### [`00b687e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b687e4.md) → [`00b688ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md) _ZN8firebase4auth8jniphone11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b688c8",
      "incomplete_value": false,
      "site": "00b688cc",
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
      "definition_site": "00b68800",
      "incomplete_value": false,
      "site": "00b68804",
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
      "definition_site": "00b688d8",
      "incomplete_value": true,
      "site": "00b688e4",
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
      "definition_site": "00b68810",
      "incomplete_value": true,
      "site": "00b6881c",
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
      "00b688c8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b688d8",
      "DATA",
      [
        "storage",
        "010a18b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b688c8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b688d8",
      "DATA",
      [
        "storage",
        "010a1978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b687e4.md#insn-00b68804) · [`00b68800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b687e4.md#insn-00b68800) · [`00b6880c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b687e4.md#insn-00b6880c)
- 新版 [`00b688cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md#insn-00b688cc) · [`00b688c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md#insn-00b688c8) · [`00b688d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688ac.md#insn-00b688d4)

~~~diff
- 00b68804 ["INT_ADD", "register:40f0:8", ["const:b68804:8", "const:4:8"]]
- 00b68804 ["CALL", null, ["callee:00bde130:8"]]
+ 00b688cc ["INT_ADD", "register:40f0:8", ["const:b688cc:8", "const:4:8"]]
+ 00b688cc ["CALL", null, ["callee:00bde130:8"]]
- 00b68804 bytes 1fd60194
+ 00b688cc bytes 19d60194
- 00b68800 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b68800 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68800 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68800 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b688c8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b688c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b688c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b688c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68800 bytes 001c1591
+ 00b688c8 bytes 00501791
- 00b6880c ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 00b6880c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6880c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6880c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b688d4 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00b688d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b688d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b688d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6880c bytes 08e12291
+ 00b688d4 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baf491c487f857822799d101718460a3"></a>

### [`00b68820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68820.md) → [`00b688e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md) _ZN8firebase4auth8jniphone13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68928",
      "incomplete_value": true,
      "site": "00b68928",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68860",
      "incomplete_value": true,
      "site": "00b68860",
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
            "const:8a8:8"
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
      "definition_site": "00b68904",
      "incomplete_value": true,
      "site": "00b68904",
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
      "definition_site": "00b6883c",
      "incomplete_value": true,
      "site": "00b6883c",
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
      "definition_site": "00b6890c",
      "incomplete_value": false,
      "site": "00b68920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68844",
      "incomplete_value": false,
      "site": "00b68858",
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
            "const:f9e:8"
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
      "00b688fc",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6890c",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b68928",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b688fc",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6890c",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68928",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68820.md#insn-00b68858) · [`00b68860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68820.md#insn-00b68860) · [`00b68834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68820.md#insn-00b68834)
- 新版 [`00b68920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md#insn-00b68920) · [`00b68928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md#insn-00b68928) · [`00b688fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b688e8.md#insn-00b688fc)

~~~diff
- 00b68858 ["INT_ADD", "register:40f0:8", ["const:b68858:8", "const:4:8"]]
- 00b68858 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68920 ["INT_ADD", "register:40f0:8", ["const:b68920:8", "const:4:8"]]
+ 00b68920 ["CALL", null, ["callee:00bde040:8"]]
- 00b68858 bytes ced50194
+ 00b68920 bytes c8d50194
- 00b68860 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b68860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68928 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b68928 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68860 bytes 805604f9
+ 00b68928 bytes 80b604f9
- 00b68834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b68834 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b688fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b688fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68834 bytes 815644f9
+ 00b688fc bytes 81b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44ef05338c2b477e57549ea25ff1a52b"></a>

### [`00b68890`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68890.md) → [`00b68958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md) _ZN8firebase4auth8jniphone10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b68974",
      "incomplete_value": false,
      "site": "00b68978",
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
      "definition_site": "00b688ac",
      "incomplete_value": false,
      "site": "00b688b0",
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
      "definition_site": "00b68984",
      "incomplete_value": true,
      "site": "00b68990",
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
      "definition_site": "00b688bc",
      "incomplete_value": true,
      "site": "00b688c8",
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
      "00b68974",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b68984",
      "DATA",
      [
        "storage",
        "010a18c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68974",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b68984",
      "DATA",
      [
        "storage",
        "010a1988",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b688b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68890.md#insn-00b688b0) · [`00b688ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68890.md#insn-00b688ac) · [`00b688b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68890.md#insn-00b688b8)
- 新版 [`00b68978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md#insn-00b68978) · [`00b68974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md#insn-00b68974) · [`00b68980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68958.md#insn-00b68980)

~~~diff
- 00b688b0 ["INT_ADD", "register:40f0:8", ["const:b688b0:8", "const:4:8"]]
- 00b688b0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b68978 ["INT_ADD", "register:40f0:8", ["const:b68978:8", "const:4:8"]]
+ 00b68978 ["CALL", null, ["callee:00bde130:8"]]
- 00b688b0 bytes f4d50194
+ 00b68978 bytes eed50194
- 00b688ac ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b688ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b688ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b688ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68974 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b68974 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68974 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68974 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b688ac bytes 00c81791
+ 00b68974 bytes 00fc1991
- 00b688b8 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00b688b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b688b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b688b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68980 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 00b68980 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68980 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68980 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b688b8 bytes 08212391
+ 00b68980 bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5b7eee6714081d4da46b5be544b21fa"></a>

### [`00b688cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b688cc.md) → [`00b68994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b689c0",
      "incomplete_value": true,
      "site": "00b689c0",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b688f8",
      "incomplete_value": true,
      "site": "00b688f8",
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
            "const:8d0:8"
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
      "definition_site": "00b689a8",
      "incomplete_value": true,
      "site": "00b689a8",
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
      "definition_site": "00b688e0",
      "incomplete_value": true,
      "site": "00b688e0",
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
      "definition_site": "00b689b4",
      "incomplete_value": false,
      "site": "00b689b8",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b688ec",
      "incomplete_value": false,
      "site": "00b688f0",
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
            "const:1fa:8"
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
      "00b689a4",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b689b4",
      "PARAM",
      [
        "storage",
        "002a51fa",
        null,
        "string"
      ]
    ],
    [
      "00b689c0",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b689a4",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b689b4",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b689c0",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b688f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b688cc.md#insn-00b688f0) · [`00b688f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b688cc.md#insn-00b688f8) · [`00b688dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b688cc.md#insn-00b688dc)
- 新版 [`00b689b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md#insn-00b689b8) · [`00b689c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md#insn-00b689c0) · [`00b689a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68994.md#insn-00b689a4)

~~~diff
- 00b688f0 ["INT_ADD", "register:40f0:8", ["const:b688f0:8", "const:4:8"]]
- 00b688f0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b689b8 ["INT_ADD", "register:40f0:8", ["const:b689b8:8", "const:4:8"]]
+ 00b689b8 ["CALL", null, ["callee:00bde040:8"]]
- 00b688f0 bytes a8d50194
+ 00b689b8 bytes a2d50194
- 00b688f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b688f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b689c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b689c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b688f8 bytes 606a04f9
+ 00b689c0 bytes 60ca04f9
- 00b688dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b688dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b689a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b689a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b688dc bytes 686a44f9
+ 00b689a4 bytes 68ca44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3172fcb3b60a358e91e3da2650deef0c"></a>

### [`00b6890c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6890c.md) → [`00b689d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md) _ZN8firebase4auth15phonecredential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b68a00",
      "incomplete_value": true,
      "site": "00b68a00",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68938",
      "incomplete_value": true,
      "site": "00b68938",
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
            "const:8d0:8"
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
      "definition_site": "00b689e8",
      "incomplete_value": true,
      "site": "00b689e8",
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
      "definition_site": "00b68920",
      "incomplete_value": true,
      "site": "00b68920",
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
      "definition_site": "00b689f0",
      "incomplete_value": false,
      "site": "00b689f8",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68928",
      "incomplete_value": false,
      "site": "00b68930",
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
            "const:1fa:8"
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
      "00b689e4",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b689f0",
      "PARAM",
      [
        "storage",
        "002a51fa",
        null,
        "string"
      ]
    ],
    [
      "00b68a00",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b689e4",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b689f0",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68a00",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6890c.md#insn-00b68930) · [`00b68938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6890c.md#insn-00b68938) · [`00b6891c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6890c.md#insn-00b6891c)
- 新版 [`00b689f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md#insn-00b689f8) · [`00b68a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md#insn-00b68a00) · [`00b689e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b689d4.md#insn-00b689e4)

~~~diff
- 00b68930 ["INT_ADD", "register:40f0:8", ["const:b68930:8", "const:4:8"]]
- 00b68930 ["CALL", null, ["callee:00bde040:8"]]
+ 00b689f8 ["INT_ADD", "register:40f0:8", ["const:b689f8:8", "const:4:8"]]
+ 00b689f8 ["CALL", null, ["callee:00bde040:8"]]
- 00b68930 bytes 98d50194
+ 00b689f8 bytes 92d50194
- 00b68938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b68938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68a00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b68a00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68938 bytes 606a04f9
+ 00b68a00 bytes 60ca04f9
- 00b6891c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b6891c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b689e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b689e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6891c bytes 686a44f9
+ 00b689e4 bytes 68ca44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9daa30c22ad6eaf085d248a498bf9b5"></a>

### [`00b6894c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6894c.md) → [`00b68a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b68a44",
      "incomplete_value": true,
      "site": "00b68a44",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6897c",
      "incomplete_value": true,
      "site": "00b6897c",
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
            "const:8d0:8"
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
      "definition_site": "00b68a28",
      "incomplete_value": true,
      "site": "00b68a28",
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
      "definition_site": "00b68960",
      "incomplete_value": true,
      "site": "00b68960",
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
      "definition_site": "00b68a34",
      "incomplete_value": false,
      "site": "00b68a3c",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6896c",
      "incomplete_value": false,
      "site": "00b68974",
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
            "const:1fa:8"
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
      "00b68a24",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a34",
      "PARAM",
      [
        "storage",
        "002a51fa",
        null,
        "string"
      ]
    ],
    [
      "00b68a44",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68a24",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a34",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68a44",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6894c.md#insn-00b68974) · [`00b6897c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6894c.md#insn-00b6897c) · [`00b6895c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b6894c.md#insn-00b6895c)
- 新版 [`00b68a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md#insn-00b68a3c) · [`00b68a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md#insn-00b68a44) · [`00b68a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a14.md#insn-00b68a24)

~~~diff
- 00b68974 ["INT_ADD", "register:40f0:8", ["const:b68974:8", "const:4:8"]]
- 00b68974 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68a3c ["INT_ADD", "register:40f0:8", ["const:b68a3c:8", "const:4:8"]]
+ 00b68a3c ["CALL", null, ["callee:00bde040:8"]]
- 00b68974 bytes 87d50194
+ 00b68a3c bytes 81d50194
- 00b6897c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b6897c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68a44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b68a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6897c bytes 606a04f9
+ 00b68a44 bytes 60ca04f9
- 00b6895c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b6895c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68a24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b68a24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6895c bytes 686a44f9
+ 00b68a24 bytes 68ca44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2d82ff8bababbc5fc01b49d110c4ef7"></a>

### [`00b68990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68990.md) → [`00b68a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md) _ZN8firebase4auth15phonecredential10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68a88",
      "incomplete_value": true,
      "site": "00b68a88",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b689c0",
      "incomplete_value": true,
      "site": "00b689c0",
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
            "const:8d0:8"
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
      "definition_site": "00b68a6c",
      "incomplete_value": true,
      "site": "00b68a6c",
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
      "definition_site": "00b689a4",
      "incomplete_value": true,
      "site": "00b689a4",
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
      "definition_site": "00b68a74",
      "incomplete_value": false,
      "site": "00b68a80",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b689ac",
      "incomplete_value": false,
      "site": "00b689b8",
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
            "const:1fa:8"
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
      "00b68a68",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a74",
      "PARAM",
      [
        "storage",
        "002a51fa",
        null,
        "string"
      ]
    ],
    [
      "00b68a88",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68a68",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68a74",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68a88",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b689b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68990.md#insn-00b689b8) · [`00b689c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68990.md#insn-00b689c0) · [`00b689a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68990.md#insn-00b689a0)
- 新版 [`00b68a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md#insn-00b68a80) · [`00b68a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md#insn-00b68a88) · [`00b68a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68a58.md#insn-00b68a68)

~~~diff
- 00b689b8 ["INT_ADD", "register:40f0:8", ["const:b689b8:8", "const:4:8"]]
- 00b689b8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68a80 ["INT_ADD", "register:40f0:8", ["const:b68a80:8", "const:4:8"]]
+ 00b68a80 ["CALL", null, ["callee:00bde040:8"]]
- 00b689b8 bytes 76d50194
+ 00b68a80 bytes 70d50194
- 00b689c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b689c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b68a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b689c0 bytes 606a04f9
+ 00b68a88 bytes 60ca04f9
- 00b689a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b689a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:990:8"]]
+ 00b68a68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b689a0 bytes 686a44f9
+ 00b68a68 bytes 68ca44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bbd955b12d4e665ec6be0a4ea426fed"></a>

### [`00b689e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b689e0.md) → [`00b68aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md) _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b68b00",
      "incomplete_value": true,
      "site": "00b68b00",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68a38",
      "incomplete_value": true,
      "site": "00b68a38",
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
            "const:8d8:8"
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
      "definition_site": "00b68adc",
      "incomplete_value": true,
      "site": "00b68ae8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68a14",
      "incomplete_value": true,
      "site": "00b68a20",
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
                "const:10a1000:8"
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
      "00b68abc",
      "READ",
      [
        "storage",
        "010a18d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68adc",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b00",
      "WRITE",
      [
        "storage",
        "010a18d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68abc",
      "READ",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68adc",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b00",
      "WRITE",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b689e0.md#insn-00b68a20) · [`00b68a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b689e0.md#insn-00b68a38) · [`00b689f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b689e0.md#insn-00b689f4)
- 新版 [`00b68ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md#insn-00b68ae8) · [`00b68b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md#insn-00b68b00) · [`00b68abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68aa8.md#insn-00b68abc)

~~~diff
- 00b68a20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68a20 ["INT_ADD", "register:40f0:8", ["const:b68a20:8", "const:4:8"]]
- 00b68a20 ["CALLIND", null, ["register:0:8"]]
+ 00b68ae8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68ae8 ["INT_ADD", "register:40f0:8", ["const:b68ae8:8", "const:4:8"]]
+ 00b68ae8 ["CALLIND", null, ["register:0:8"]]
- 00b68a20 bytes 00013fd6
+ 00b68ae8 bytes 00013fd6
- 00b68a38 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b68a38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d8:8"]]
- 00b68a38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b68b00 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b68b00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:998:8"]]
+ 00b68b00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68a38 bytes a0622339
+ 00b68b00 bytes a0622639
- 00b689f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d8:8"]]
- 00b689f4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b689f4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b68abc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:998:8"]]
+ 00b68abc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b68abc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b689f4 bytes a8626339
+ 00b68abc bytes a8626639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bb20e05f65fb659587d49ae99b18bc0"></a>

### [`00b68a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68a4c.md) → [`00b68b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md) _ZN8firebase4auth15phonecredential12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b68b50",
      "incomplete_value": true,
      "site": "00b68b50",
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
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68a88",
      "incomplete_value": true,
      "site": "00b68a88",
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
            "const:8d8:8"
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
      "definition_site": "00b68b70",
      "incomplete_value": true,
      "site": "00b68b70",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68aa8",
      "incomplete_value": true,
      "site": "00b68aa8",
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
            "const:8d0:8"
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
      "definition_site": "00b68b2c",
      "incomplete_value": true,
      "site": "00b68b2c",
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
      "definition_site": "00b68a64",
      "incomplete_value": true,
      "site": "00b68a64",
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
      "00b68b28",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b34",
      "READ",
      [
        "storage",
        "010a18d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68b50",
      "WRITE",
      [
        "storage",
        "010a18d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b68b28",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68b34",
      "READ",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ],
    [
      "00b68b50",
      "WRITE",
      [
        "storage",
        "010a1998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68a4c.md#insn-00b68a88) · [`00b68aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68a4c.md#insn-00b68aa4) · [`00b68aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68a4c.md#insn-00b68aa8)
- 新版 [`00b68b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md#insn-00b68b50) · [`00b68b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md#insn-00b68b6c) · [`00b68b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b14.md#insn-00b68b70)

~~~diff
- 00b68a88 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b68a88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b68a88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d8:8"]]
- 00b68a88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b68b50 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b68b50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b68b50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:998:8"]]
+ 00b68b50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b68a88 bytes bf622339
+ 00b68b50 bytes bf622639
- 00b68aa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68aa4 ["INT_ADD", "register:40f0:8", ["const:b68aa4:8", "const:4:8"]]
- 00b68aa4 ["CALLIND", null, ["register:0:8"]]
+ 00b68b6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b68b6c ["INT_ADD", "register:40f0:8", ["const:b68b6c:8", "const:4:8"]]
+ 00b68b6c ["CALLIND", null, ["register:0:8"]]
- 00b68aa4 bytes 00013fd6
+ 00b68b6c bytes 00013fd6
- 00b68aa8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b68aa8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b68aa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b68b70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
+ 00b68b70 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b68b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b68aa8 bytes 9f6a04f9
+ 00b68b70 bytes 9fca04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab63974cfc21088641336e8985fe987e"></a>

### [`00b68abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68abc.md) → [`00b68b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md) _ZN8firebase4auth15phonecredential14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68bc4",
      "incomplete_value": true,
      "site": "00b68bc4",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68afc",
      "incomplete_value": true,
      "site": "00b68afc",
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
            "const:8d0:8"
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
      "definition_site": "00b68ba0",
      "incomplete_value": true,
      "site": "00b68ba0",
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
      "definition_site": "00b68ad8",
      "incomplete_value": true,
      "site": "00b68ad8",
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
      "definition_site": "00b68ba8",
      "incomplete_value": false,
      "site": "00b68bbc",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68ae0",
      "incomplete_value": false,
      "site": "00b68af4",
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
            "const:1fa:8"
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
      "00b68b98",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68ba8",
      "PARAM",
      [
        "storage",
        "002a51fa",
        null,
        "string"
      ]
    ],
    [
      "00b68bc4",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68b98",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68ba8",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68bc4",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68abc.md#insn-00b68af4) · [`00b68afc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68abc.md#insn-00b68afc) · [`00b68ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68abc.md#insn-00b68ad0)
- 新版 [`00b68bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md#insn-00b68bbc) · [`00b68bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md#insn-00b68bc4) · [`00b68b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68b84.md#insn-00b68b98)

~~~diff
- 00b68af4 ["INT_ADD", "register:40f0:8", ["const:b68af4:8", "const:4:8"]]
- 00b68af4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68bbc ["INT_ADD", "register:40f0:8", ["const:b68bbc:8", "const:4:8"]]
+ 00b68bbc ["CALL", null, ["callee:00bde040:8"]]
- 00b68af4 bytes 27d50194
+ 00b68bbc bytes 21d50194
- 00b68afc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b68afc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68bc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
+ 00b68bc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68afc bytes 806a04f9
+ 00b68bc4 bytes 80ca04f9
- 00b68ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b68ad0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68b98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
+ 00b68b98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68ad0 bytes 816a44f9
+ 00b68b98 bytes 81ca44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96c41a657ff34d652b7b944b8834ea6c"></a>

### [`00b68b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b2c.md) → [`00b68bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md) _ZN8firebase4auth15phonecredential11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b68c10",
      "incomplete_value": false,
      "site": "00b68c14",
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
      "definition_site": "00b68b48",
      "incomplete_value": false,
      "site": "00b68b4c",
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
      "definition_site": "00b68c20",
      "incomplete_value": true,
      "site": "00b68c2c",
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
      "definition_site": "00b68b58",
      "incomplete_value": true,
      "site": "00b68b64",
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
      "00b68c10",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b68c20",
      "DATA",
      [
        "storage",
        "010a18e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68c10",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b68c20",
      "DATA",
      [
        "storage",
        "010a19a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b2c.md#insn-00b68b4c) · [`00b68b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b2c.md#insn-00b68b48) · [`00b68b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b2c.md#insn-00b68b54)
- 新版 [`00b68c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md#insn-00b68c14) · [`00b68c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md#insn-00b68c10) · [`00b68c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68bf4.md#insn-00b68c1c)

~~~diff
- 00b68b4c ["INT_ADD", "register:40f0:8", ["const:b68b4c:8", "const:4:8"]]
- 00b68b4c ["CALL", null, ["callee:00bde130:8"]]
+ 00b68c14 ["INT_ADD", "register:40f0:8", ["const:b68c14:8", "const:4:8"]]
+ 00b68c14 ["CALL", null, ["callee:00bde130:8"]]
- 00b68b4c bytes 4dd50194
+ 00b68c14 bytes 47d50194
- 00b68b48 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b68b48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68b48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68b48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68c10 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b68c10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68c10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68c10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68b48 bytes 001c1591
+ 00b68c10 bytes 00501791
- 00b68b54 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00b68b54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68b54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68b54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68c1c ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00b68c1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68c1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68c1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68b54 bytes 08812391
+ 00b68c1c bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a62ab8710ef71cd663d99e37a11c6d84"></a>

### [`00b68b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b68.md) → [`00b68c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md) _ZN8firebase4auth15phonecredential13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b68c70",
      "incomplete_value": true,
      "site": "00b68c70",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68ba8",
      "incomplete_value": true,
      "site": "00b68ba8",
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
            "const:8d0:8"
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
      "definition_site": "00b68c4c",
      "incomplete_value": true,
      "site": "00b68c4c",
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
      "definition_site": "00b68b84",
      "incomplete_value": true,
      "site": "00b68b84",
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
      "definition_site": "00b68c54",
      "incomplete_value": false,
      "site": "00b68c68",
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
            "const:1f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68b8c",
      "incomplete_value": false,
      "site": "00b68ba0",
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
            "const:1fa:8"
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
      "00b68c44",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68c54",
      "PARAM",
      [
        "storage",
        "002a51fa",
        null,
        "string"
      ]
    ],
    [
      "00b68c70",
      "WRITE",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68c44",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68c54",
      "PARAM",
      [
        "storage",
        "002a51f3",
        null,
        "string"
      ]
    ],
    [
      "00b68c70",
      "WRITE",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b68.md#insn-00b68ba0) · [`00b68ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b68.md#insn-00b68ba8) · [`00b68b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68b68.md#insn-00b68b7c)
- 新版 [`00b68c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md#insn-00b68c68) · [`00b68c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md#insn-00b68c70) · [`00b68c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68c30.md#insn-00b68c44)

~~~diff
- 00b68ba0 ["INT_ADD", "register:40f0:8", ["const:b68ba0:8", "const:4:8"]]
- 00b68ba0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b68c68 ["INT_ADD", "register:40f0:8", ["const:b68c68:8", "const:4:8"]]
+ 00b68c68 ["CALL", null, ["callee:00bde040:8"]]
- 00b68ba0 bytes fcd40194
+ 00b68c68 bytes f6d40194
- 00b68ba8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b68ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68c70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
+ 00b68c70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68ba8 bytes 806a04f9
+ 00b68c70 bytes 80ca04f9
- 00b68b7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b68b7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b68c44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:990:8"]]
+ 00b68c44 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b68b7c bytes 816a44f9
+ 00b68c44 bytes 81ca44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cff64d42ece7a2c5224e9ae61b1f972f"></a>

### [`00b68bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68bd8.md) → [`00b68ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md) _ZN8firebase4auth15phonecredential10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b68cbc",
      "incomplete_value": false,
      "site": "00b68cc0",
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
      "definition_site": "00b68bf4",
      "incomplete_value": false,
      "site": "00b68bf8",
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
      "definition_site": "00b68ccc",
      "incomplete_value": true,
      "site": "00b68cd8",
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
      "definition_site": "00b68c04",
      "incomplete_value": true,
      "site": "00b68c10",
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
      "00b68cbc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b68ccc",
      "DATA",
      [
        "storage",
        "010a18e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b68cbc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b68ccc",
      "DATA",
      [
        "storage",
        "010a19a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68bd8.md#insn-00b68bf8) · [`00b68bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68bd8.md#insn-00b68bf4) · [`00b68c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68bd8.md#insn-00b68c00)
- 新版 [`00b68cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md#insn-00b68cc0) · [`00b68cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md#insn-00b68cbc) · [`00b68cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68ca0.md#insn-00b68cc8)

~~~diff
- 00b68bf8 ["INT_ADD", "register:40f0:8", ["const:b68bf8:8", "const:4:8"]]
- 00b68bf8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b68cc0 ["INT_ADD", "register:40f0:8", ["const:b68cc0:8", "const:4:8"]]
+ 00b68cc0 ["CALL", null, ["callee:00bde130:8"]]
- 00b68bf8 bytes 22d50194
+ 00b68cc0 bytes 1cd50194
- 00b68bf4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b68bf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b68bf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b68bf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b68cbc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b68cbc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68cbc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b68cbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b68bf4 bytes 00c81791
+ 00b68cbc bytes 00fc1991
- 00b68c00 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00b68c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b68c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b68c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b68cc8 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 00b68cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b68cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b68c00 bytes 08a12391
+ 00b68cc8 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdc3a9fcd518c6cf862a8170cc798555"></a>

### [`00b68c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68c14.md) → [`00b68cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md) _ZN8firebase4auth24CacheCredentialMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0bb0.md) · 呼出先 4件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c60.md) · 呼出先 4件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 80.29% / 新版 80.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 61件, `store_condition` 1件, `store_destination` 18件

アドレスに依存する影響 `branch_value` 16件, `call_argument_candidate` 1件, `store_condition` 16件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b68d1c",
      "incomplete_value": true,
      "site": "00b68d1c",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68c54",
      "incomplete_value": true,
      "site": "00b68c54",
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
            "const:8a8:8"
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
      "definition_site": "00b68d94",
      "incomplete_value": true,
      "site": "00b68d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:970:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68ccc",
      "incomplete_value": true,
      "site": "00b68ccc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b68dd0",
      "incomplete_value": true,
      "site": "00b68dd0",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b68d08",
      "incomplete_value": true,
      "site": "00b68d08",
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
            "const:640:8"
          ]
        ]
      ]
    },
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
      "00b68cf4",
      "READ",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68d04",
      "PARAM",
      [
        "storage",
        "002a1f9e",
        null,
        "string"
      ]
    ],
    [
      "00b68d1c",
      "WRITE",
      [
        "storage",
        "010a18a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b68cf4",
      "READ",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b68d04",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "00b68d1c",
      "WRITE",
      [
        "storage",
        "010a1968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b68c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68c14.md#insn-00b68c54) · [`00b68ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68c14.md#insn-00b68ccc) · [`00b68d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b68/00b68c14.md#insn-00b68d08)
- 新版 [`00b68d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md#insn-00b68d1c) · [`00b68d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md#insn-00b68d94) · [`00b68dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b68/00b68cdc.md#insn-00b68dd0)

~~~diff
- 00b68c54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8a8:8"]]
- 00b68c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68d1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:968:8"]]
+ 00b68d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68c54 bytes a05604f9
+ 00b68d1c bytes a0b604f9
- 00b68ccc ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b68ccc ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:8b0:8"]]
- 00b68ccc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b68d94 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00b68d94 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "const:970:8"]]
+ 00b68d94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b68ccc bytes c8c22239
+ 00b68d94 bytes c8c22539
- 00b68d08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:640:8"]]
- 00b68d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b68dd0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:700:8"]]
+ 00b68dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b68d08 bytes a02203f9
+ 00b68dd0 bytes a08203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ab5c944ef56fcf8843757db2b2eb51"></a>

### [`00b69280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69280.md) → [`00b69348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69348.md) _ZN8firebase4auth24ReleaseCredentialClassesEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0bc0.md) · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c70.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 17.07% / 新版 17.07%

CFGの説明率　旧版 9.52% / 新版 9.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 28件, `unresolved_call_alignment` 45件, `unresolved_store_alignment` 30件

アドレスに依存する影響 `branch_value` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b692bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b692dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b69308"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6935c",
      "READ",
      [
        "storage",
        "010a1860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b692e0"
      ]
    ],
    [
      "00b6936c",
      "READ",
      [
        "storage",
        "010a1868",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6935c",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b69364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b693a8"
      ]
    ],
    [
      "00b6936c",
      "READ",
      [
        "storage",
        "010a1928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b692bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69280.md#insn-00b692bc) · [`00b692dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69280.md#insn-00b692dc) · [`00b69308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69280.md#insn-00b69308)

~~~diff
- 00b692bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b692bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b692bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:868:8"]]
- 00b692bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b692bc bytes bfa22139
- 00b692dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:860:8"]]
- 00b692dc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b692dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b692dc bytes 9f3204f9
- 00b69308 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b69308 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b69308 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
- 00b69308 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b69308 bytes bf221939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3a4553268846f05f0abea67796947aa"></a>

### [`00b697b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b697b8.md) → [`00b69880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md) _ZN8firebase4auth10CredentialD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bddaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaa0.md) [`00be0d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d00.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 2件 [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00be0db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0db0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b698a8",
      "incomplete_value": false,
      "site": "00b698ac",
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
      "definition_site": "00b697e0",
      "incomplete_value": false,
      "site": "00b697e4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b698a8",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b698a8",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b697e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b697b8.md#insn-00b697e4) · [`00b697d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b697b8.md#insn-00b697d0) · [`00b697e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b697b8.md#insn-00b697e0)
- 新版 [`00b698ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md#insn-00b698ac) · [`00b69898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md#insn-00b69898) · [`00b698a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69880.md#insn-00b698a8)

~~~diff
- 00b697e4 ["INT_ADD", "register:40f0:8", ["const:b697e4:8", "const:4:8"]]
- 00b697e4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b698ac ["INT_ADD", "register:40f0:8", ["const:b698ac:8", "const:4:8"]]
+ 00b698ac ["CALL", null, ["callee:00bde130:8"]]
- 00b697e4 bytes 27d20194
+ 00b698ac bytes 21d20194
- 00b697d0 ["INT_ADD", "register:40f0:8", ["const:b697d0:8", "const:4:8"]]
- 00b697d0 ["CALL", null, ["callee:00bde390:8"]]
+ 00b69898 ["INT_ADD", "register:40f0:8", ["const:b69898:8", "const:4:8"]]
+ 00b69898 ["CALL", null, ["callee:00bde390:8"]]
- 00b697d0 bytes c4d20194
+ 00b69898 bytes bed20194
- 00b697e0 ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b697e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b697e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b697e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b698a8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b698a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b698a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b698a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b697e0 bytes 00fc3691
+ 00b698a8 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1f63070412ebce76b4c79dbbb337ea"></a>

### [`00b6983c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6983c.md) → [`00b69904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69904.md) _ZN8firebase4auth10CredentialC1ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be0c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b69860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6983c.md#insn-00b69860)
- 新版 [`00b69928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69904.md#insn-00b69928)

~~~diff
- 00b69860 ["INT_ADD", "register:40f0:8", ["const:b69860:8", "const:4:8"]]
- 00b69860 ["CALL", null, ["callee:00be0d10:8"]]
+ 00b69928 ["INT_ADD", "register:40f0:8", ["const:b69928:8", "const:4:8"]]
+ 00b69928 ["CALL", null, ["callee:00be0d10:8"]]
- 00b69860 bytes 00dd0194
+ 00b69928 bytes fadc0194
~~~


<a id="compare-2980d6e8fc512334fe464721da7f985f"></a>

### [`00b6988c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6988c.md) → [`00b69954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md) _ZN8firebase4auth10CredentialaSERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c60.md) · 呼出先 4件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 1件 [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md) · 呼出先 4件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6998c",
      "incomplete_value": false,
      "site": "00b69990",
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
      "definition_site": "00b698c4",
      "incomplete_value": false,
      "site": "00b698c8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6998c",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6998c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b698c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6988c.md#insn-00b698c8) · [`00b698b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6988c.md#insn-00b698b4) · [`00b698c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6988c.md#insn-00b698c4)
- 新版 [`00b69990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md#insn-00b69990) · [`00b6997c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md#insn-00b6997c) · [`00b6998c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69954.md#insn-00b6998c)

~~~diff
- 00b698c8 ["INT_ADD", "register:40f0:8", ["const:b698c8:8", "const:4:8"]]
- 00b698c8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b69990 ["INT_ADD", "register:40f0:8", ["const:b69990:8", "const:4:8"]]
+ 00b69990 ["CALL", null, ["callee:00bde130:8"]]
- 00b698c8 bytes eed10194
+ 00b69990 bytes e8d10194
- 00b698b4 ["INT_ADD", "register:40f0:8", ["const:b698b4:8", "const:4:8"]]
- 00b698b4 ["CALL", null, ["callee:00bde390:8"]]
+ 00b6997c ["INT_ADD", "register:40f0:8", ["const:b6997c:8", "const:4:8"]]
+ 00b6997c ["CALL", null, ["callee:00bde390:8"]]
- 00b698b4 bytes 8bd20194
+ 00b6997c bytes 85d20194
- 00b698c4 ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b698c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b698c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b698c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6998c ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b6998c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6998c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6998c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b698c4 bytes 00fc3691
+ 00b6998c bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14c8f8e7c513cbe22d8db33d440376ac"></a>

### [`00b6995c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6995c.md) → [`00b69a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md) _ZNK8firebase4auth10Credential8providerEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.97% / 新版 96.97%

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
      "definition_site": "00b69a4c",
      "incomplete_value": false,
      "site": "00b69a50",
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
      "definition_site": "00b69984",
      "incomplete_value": false,
      "site": "00b69988",
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
      "definition_site": "00b69a68",
      "incomplete_value": true,
      "site": "00b69a70",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b699a0",
      "incomplete_value": true,
      "site": "00b699a8",
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
                "const:10a1000:8"
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
      "00b69a4c",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b69a68",
      "READ",
      [
        "storage",
        "010a1650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69a4c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b69a68",
      "READ",
      [
        "storage",
        "010a1710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6995c.md#insn-00b69988) · [`00b699a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6995c.md#insn-00b699a8) · [`00b69974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b6995c.md#insn-00b69974)
- 新版 [`00b69a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md#insn-00b69a50) · [`00b69a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md#insn-00b69a70) · [`00b69a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69a24.md#insn-00b69a3c)

~~~diff
- 00b69988 ["INT_ADD", "register:40f0:8", ["const:b69988:8", "const:4:8"]]
- 00b69988 ["CALL", null, ["callee:00bde130:8"]]
+ 00b69a50 ["INT_ADD", "register:40f0:8", ["const:b69a50:8", "const:4:8"]]
+ 00b69a50 ["CALL", null, ["callee:00bde130:8"]]
- 00b69988 bytes bed10194
+ 00b69a50 bytes b8d10194
- 00b699a8 ["INT_ADD", "register:40f0:8", ["const:b699a8:8", "const:4:8"]]
- 00b699a8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b69a70 ["INT_ADD", "register:40f0:8", ["const:b69a70:8", "const:4:8"]]
+ 00b69a70 ["CALL", null, ["callee:0047495c:8"]]
- 00b699a8 bytes ed2be497
+ 00b69a70 bytes bb2be497
- 00b69974 ["INT_ADD", "register:40f0:8", ["const:b69974:8", "const:4:8"]]
- 00b69974 ["CALL", null, ["callee:00bde390:8"]]
+ 00b69a3c ["INT_ADD", "register:40f0:8", ["const:b69a3c:8", "const:4:8"]]
+ 00b69a3c ["CALL", null, ["callee:00bde390:8"]]
- 00b69974 bytes 5bd20194
+ 00b69a3c bytes 55d20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c34bbcf7e10671e8f7090bd551c43f54"></a>

### [`00b699f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b699f0.md) → [`00b69ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md) _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b69b10",
      "incomplete_value": false,
      "site": "00b69b14",
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
      "definition_site": "00b69a48",
      "incomplete_value": false,
      "site": "00b69a4c",
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
      "definition_site": "00b69b54",
      "incomplete_value": true,
      "site": "00b69b6c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:720:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69a8c",
      "incomplete_value": true,
      "site": "00b69aa4",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:660:8"
              ]
            ]
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
      "definition_site": "00b69b58",
      "incomplete_value": true,
      "site": "00b69b6c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:730:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69a90",
      "incomplete_value": true,
      "site": "00b69aa4",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:670:8"
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
      "00b69af4",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b69bbc"
      ]
    ],
    [
      "00b69b10",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b69af4",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b69c84"
      ]
    ],
    [
      "00b69b10",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b699f0.md#insn-00b69a2c) · [`00b69a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b699f0.md#insn-00b69a4c) · [`00b69aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b699f0.md#insn-00b69aa4)
- 新版 [`00b69af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md#insn-00b69af4) · [`00b69b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md#insn-00b69b14) · [`00b69b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69ab8.md#insn-00b69b6c)

~~~diff
- 00b69a2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8f0:8"]]
- 00b69a2c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b69a2c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b69af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
+ 00b69af4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b69af4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b69a2c bytes 08c16339
+ 00b69af4 bytes 08c16639
- 00b69a4c ["INT_ADD", "register:40f0:8", ["const:b69a4c:8", "const:4:8"]]
- 00b69a4c ["CALL", null, ["callee:00bde130:8"]]
+ 00b69b14 ["INT_ADD", "register:40f0:8", ["const:b69b14:8", "const:4:8"]]
+ 00b69b14 ["CALL", null, ["callee:00bde130:8"]]
- 00b69a4c bytes 8dd10194
+ 00b69b14 bytes 87d10194
- 00b69aa4 ["INT_ADD", "register:40f0:8", ["const:b69aa4:8", "const:4:8"]]
- 00b69aa4 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b69b6c ["INT_ADD", "register:40f0:8", ["const:b69b6c:8", "const:4:8"]]
+ 00b69b6c ["CALL", null, ["callee:00bddcf0:8"]]
- 00b69aa4 bytes 67d00194
+ 00b69b6c bytes 61d00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28eaf5c164728927a1b90a7ee9708c85"></a>

### [`00b69d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69d34.md) → [`00b69dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md) _ZNK8firebase4auth19PhoneAuthCredential8sms_codeEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b69e2c",
      "incomplete_value": false,
      "site": "00b69e30",
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
      "definition_site": "00b69d64",
      "incomplete_value": false,
      "site": "00b69d68",
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
      "definition_site": "00b69e44",
      "incomplete_value": true,
      "site": "00b69e4c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:9a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69d7c",
      "incomplete_value": true,
      "site": "00b69d84",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:8e0:8"
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
      "00b69e2c",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b69e44",
      "READ",
      [
        "storage",
        "010a18e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69e2c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b69e44",
      "READ",
      [
        "storage",
        "010a19a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69d34.md#insn-00b69d68) · [`00b69d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69d34.md#insn-00b69d84) · [`00b69d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69d34.md#insn-00b69d54)
- 新版 [`00b69e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md#insn-00b69e30) · [`00b69e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md#insn-00b69e4c) · [`00b69e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69dfc.md#insn-00b69e1c)

~~~diff
- 00b69d68 ["INT_ADD", "register:40f0:8", ["const:b69d68:8", "const:4:8"]]
- 00b69d68 ["CALL", null, ["callee:00bde130:8"]]
+ 00b69e30 ["INT_ADD", "register:40f0:8", ["const:b69e30:8", "const:4:8"]]
+ 00b69e30 ["CALL", null, ["callee:00bde130:8"]]
- 00b69d68 bytes c6d00194
+ 00b69e30 bytes c0d00194
- 00b69d84 ["INT_ADD", "register:40f0:8", ["const:b69d84:8", "const:4:8"]]
- 00b69d84 ["CALL", null, ["callee:0047495c:8"]]
+ 00b69e4c ["INT_ADD", "register:40f0:8", ["const:b69e4c:8", "const:4:8"]]
+ 00b69e4c ["CALL", null, ["callee:0047495c:8"]]
- 00b69d84 bytes f62ae497
+ 00b69e4c bytes c42ae497
- 00b69d54 ["INT_ADD", "register:40f0:8", ["const:b69d54:8", "const:4:8"]]
- 00b69d54 ["CALL", null, ["callee:00bde390:8"]]
+ 00b69e1c ["INT_ADD", "register:40f0:8", ["const:b69e1c:8", "const:4:8"]]
+ 00b69e1c ["CALL", null, ["callee:00bde390:8"]]
- 00b69d54 bytes 63d10194
+ 00b69e1c bytes 5dd10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e7860ac95af6c03741fdecb0acbb24"></a>

### [`00b69dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69dbc.md) → [`00b69e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md) _ZN8firebase4auth26InternalAuthResultProvider13GetCredentialEP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ca0.md) · 呼出先 3件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 1件 [`00be0d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d50.md) · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b69eb0",
      "incomplete_value": false,
      "site": "00b69eb4",
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
      "definition_site": "00b69de8",
      "incomplete_value": false,
      "site": "00b69dec",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b69eb0",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b69eb0",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69dbc.md#insn-00b69dec) · [`00b69dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69dbc.md#insn-00b69dd8) · [`00b69de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69dbc.md#insn-00b69de8)
- 新版 [`00b69eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md#insn-00b69eb4) · [`00b69ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md#insn-00b69ea0) · [`00b69eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69e84.md#insn-00b69eb0)

~~~diff
- 00b69dec ["INT_ADD", "register:40f0:8", ["const:b69dec:8", "const:4:8"]]
- 00b69dec ["CALL", null, ["callee:00bde130:8"]]
+ 00b69eb4 ["INT_ADD", "register:40f0:8", ["const:b69eb4:8", "const:4:8"]]
+ 00b69eb4 ["CALL", null, ["callee:00bde130:8"]]
- 00b69dec bytes a5d00194
+ 00b69eb4 bytes 9fd00194
- 00b69dd8 ["INT_ADD", "register:40f0:8", ["const:b69dd8:8", "const:4:8"]]
- 00b69dd8 ["CALL", null, ["callee:00bde390:8"]]
+ 00b69ea0 ["INT_ADD", "register:40f0:8", ["const:b69ea0:8", "const:4:8"]]
+ 00b69ea0 ["CALL", null, ["callee:00bde390:8"]]
- 00b69dd8 bytes 42d10194
+ 00b69ea0 bytes 3cd10194
- 00b69de8 ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b69de8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b69de8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b69de8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b69eb0 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b69eb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b69eb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b69eb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b69de8 bytes 00fc3691
+ 00b69eb0 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc6f183df974fe9742f0b8360a7f3f31"></a>

### [`00b69e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69e4c.md) → [`00b69f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md) _ZN8firebase4auth20FacebookAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b69f50",
      "incomplete_value": false,
      "site": "00b69f54",
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
      "definition_site": "00b69e88",
      "incomplete_value": false,
      "site": "00b69e8c",
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
      "definition_site": "00b69f7c",
      "incomplete_value": true,
      "site": "00b69f90",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69eb4",
      "incomplete_value": true,
      "site": "00b69ec8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:680:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b69f80",
      "incomplete_value": true,
      "site": "00b69f90",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:750:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b69eb8",
      "incomplete_value": true,
      "site": "00b69ec8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
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
      "00b69f34",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69f50",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b69f7c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b69f34",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b69f50",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b69f7c",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69e4c.md#insn-00b69e8c) · [`00b69ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69e4c.md#insn-00b69ec8) · [`00b69f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69e4c.md#insn-00b69f10)
- 新版 [`00b69f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md#insn-00b69f54) · [`00b69f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md#insn-00b69f90) · [`00b69fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b69/00b69f14.md#insn-00b69fd8)

~~~diff
- 00b69e8c ["INT_ADD", "register:40f0:8", ["const:b69e8c:8", "const:4:8"]]
- 00b69e8c ["CALL", null, ["callee:00bde130:8"]]
+ 00b69f54 ["INT_ADD", "register:40f0:8", ["const:b69f54:8", "const:4:8"]]
+ 00b69f54 ["CALL", null, ["callee:00bde130:8"]]
- 00b69e8c bytes 7dd00194
+ 00b69f54 bytes 77d00194
- 00b69ec8 ["INT_ADD", "register:40f0:8", ["const:b69ec8:8", "const:4:8"]]
- 00b69ec8 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b69f90 ["INT_ADD", "register:40f0:8", ["const:b69f90:8", "const:4:8"]]
+ 00b69f90 ["CALL", null, ["callee:00bddcf0:8"]]
- 00b69ec8 bytes 5ecf0194
+ 00b69f90 bytes 58cf0194
- 00b69f10 ["INT_ADD", "register:40f0:8", ["const:b69f10:8", "const:4:8"]]
- 00b69f10 ["CALL", null, ["callee:00bde130:8"]]
+ 00b69fd8 ["INT_ADD", "register:40f0:8", ["const:b69fd8:8", "const:4:8"]]
+ 00b69fd8 ["CALL", null, ["callee:00bde130:8"]]
- 00b69f10 bytes 5cd00194
+ 00b69fd8 bytes 56d00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38703a77d69d4fdcb5fc2f37094e63bd"></a>

### [`00b69f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69f98.md) → [`00b6a060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a060.md) _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdad94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdad94.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_count, store_count

命令の説明率　旧版 67.86% / 新版 22.89%

CFGの説明率　旧版 40.00% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 3件, `call_count` 10件, `return_count` 1件, `store_count` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6a188"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6a18c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6a190"
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
      "00b6a078",
      "CONDITIONAL_JUMP",
      [
        "unresolved_target",
        "00b6a098"
      ]
    ],
    [
      "00b6a080",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a084",
      "CONDITIONAL_JUMP",
      [
        "unresolved_target",
        "00b6a0a4"
      ]
    ]
  ],
  "added": [
    [
      "00b6a078",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a160"
      ]
    ],
    [
      "00b6a080",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a16c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b69fd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69f98.md#insn-00b69fd8) · [`00b69fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b69/00b69f98.md#insn-00b69fe0)
- 新版 [`00b6a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a060.md#insn-00b6a0a0)

~~~diff
- 00b69fd8 ["INT_ADD", "register:40f0:8", ["const:b69fd8:8", "const:4:8"]]
- 00b69fd8 ["CALL", null, ["callee:00bde130:8"]]
- 00b69fd8 bytes 2ad00194
- 00b69fe0 ["INT_ADD", "register:40f0:8", ["const:b69fe0:8", "const:4:8"]]
- 00b69fe0 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b69fe0 bytes 48d00194
+ 00b6a0a0 ["INT_ADD", "register:40f0:8", ["const:b6a0a0:8", "const:4:8"]]
+ 00b6a0a0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6a0a0 bytes 24d00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02dd865044f4de14f7ab86f20bc881bb"></a>

### [`00b6a0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a0e4.md) → [`00b6a1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md) _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdda80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda80.md) · 呼出先 6件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00bddb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb30.md) · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a1e8",
      "incomplete_value": false,
      "site": "00b6a1ec",
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
      "definition_site": "00b6a120",
      "incomplete_value": false,
      "site": "00b6a124",
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
      "definition_site": "00b6a24c",
      "incomplete_value": false,
      "site": "00b6a250",
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
            "const:1c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a184",
      "incomplete_value": false,
      "site": "00b6a188",
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
            "const:1ce:8"
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
      "definition_site": "00b6a278",
      "incomplete_value": true,
      "site": "00b6a28c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a1b0",
      "incomplete_value": true,
      "site": "00b6a1c4",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6a1c4",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a1e8",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b6a24c",
      "PARAM",
      [
        "storage",
        "002a71ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a1c4",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a1e8",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6a24c",
      "PARAM",
      [
        "storage",
        "002a71c7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a0e4.md#insn-00b6a0fc) · [`00b6a124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a0e4.md#insn-00b6a124) · [`00b6a188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a0e4.md#insn-00b6a188)
- 新版 [`00b6a1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md#insn-00b6a1c4) · [`00b6a1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md#insn-00b6a1ec) · [`00b6a250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a1ac.md#insn-00b6a250)

~~~diff
- 00b6a0fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8f0:8"]]
- 00b6a0fc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6a0fc ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 00b6a1c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b0:8"]]
+ 00b6a1c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6a1c4 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 00b6a0fc bytes 29c16339
+ 00b6a1c4 bytes 29c16639
- 00b6a124 ["INT_ADD", "register:40f0:8", ["const:b6a124:8", "const:4:8"]]
- 00b6a124 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6a1ec ["INT_ADD", "register:40f0:8", ["const:b6a1ec:8", "const:4:8"]]
+ 00b6a1ec ["CALL", null, ["callee:00bde130:8"]]
- 00b6a124 bytes d7cf0194
+ 00b6a1ec bytes d1cf0194
- 00b6a188 ["INT_ADD", "register:40f0:8", ["const:b6a188:8", "const:4:8"]]
- 00b6a188 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b6a250 ["INT_ADD", "register:40f0:8", ["const:b6a250:8", "const:4:8"]]
+ 00b6a250 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b6a188 bytes eece0194
+ 00b6a250 bytes e8ce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d70b2ad26fbbcc9fd466b044d549497"></a>

### [`00b6a288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a288.md) → [`00b6a350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md) _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a38c",
      "incomplete_value": false,
      "site": "00b6a390",
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
      "definition_site": "00b6a2c4",
      "incomplete_value": false,
      "site": "00b6a2c8",
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
      "definition_site": "00b6a3b8",
      "incomplete_value": true,
      "site": "00b6a3cc",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a2f0",
      "incomplete_value": true,
      "site": "00b6a304",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:6e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a3bc",
      "incomplete_value": true,
      "site": "00b6a3cc",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a2f4",
      "incomplete_value": true,
      "site": "00b6a304",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:6f0:8"
              ]
            ]
          ]
        ]
      ]
    },
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
      "00b6a370",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a394"
      ]
    ],
    [
      "00b6a38c",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a370",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a374",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a45c"
      ]
    ],
    [
      "00b6a38c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a288.md#insn-00b6a2c8) · [`00b6a304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a288.md#insn-00b6a304) · [`00b6a34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a288.md#insn-00b6a34c)
- 新版 [`00b6a390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md#insn-00b6a390) · [`00b6a3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md#insn-00b6a3cc) · [`00b6a414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a350.md#insn-00b6a414)

~~~diff
- 00b6a2c8 ["INT_ADD", "register:40f0:8", ["const:b6a2c8:8", "const:4:8"]]
- 00b6a2c8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6a390 ["INT_ADD", "register:40f0:8", ["const:b6a390:8", "const:4:8"]]
+ 00b6a390 ["CALL", null, ["callee:00bde130:8"]]
- 00b6a2c8 bytes 6ecf0194
+ 00b6a390 bytes 68cf0194
- 00b6a304 ["INT_ADD", "register:40f0:8", ["const:b6a304:8", "const:4:8"]]
- 00b6a304 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b6a3cc ["INT_ADD", "register:40f0:8", ["const:b6a3cc:8", "const:4:8"]]
+ 00b6a3cc ["CALL", null, ["callee:00bddcf0:8"]]
- 00b6a304 bytes 4fce0194
+ 00b6a3cc bytes 49ce0194
- 00b6a34c ["INT_ADD", "register:40f0:8", ["const:b6a34c:8", "const:4:8"]]
- 00b6a34c ["CALL", null, ["callee:00bde130:8"]]
+ 00b6a414 ["INT_ADD", "register:40f0:8", ["const:b6a414:8", "const:4:8"]]
+ 00b6a414 ["CALL", null, ["callee:00bde130:8"]]
- 00b6a34c bytes 4dcf0194
+ 00b6a414 bytes 47cf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118bb4c4ea26d6d698d280301abc31bd"></a>

### [`00b6a3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a3d4.md) → [`00b6a49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md) _ZN8firebase4auth19TwitterAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.85% / 新版 94.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a4e0",
      "incomplete_value": false,
      "site": "00b6a4e4",
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
      "definition_site": "00b6a418",
      "incomplete_value": false,
      "site": "00b6a41c",
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
      "definition_site": "00b6a524",
      "incomplete_value": true,
      "site": "00b6a53c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a45c",
      "incomplete_value": true,
      "site": "00b6a474",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:700:8"
              ]
            ]
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
      "definition_site": "00b6a528",
      "incomplete_value": true,
      "site": "00b6a53c",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a460",
      "incomplete_value": true,
      "site": "00b6a474",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:710:8"
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
      "00b6a4c4",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a4e0",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b6a524",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6a4c4",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a4e0",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6a524",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a3d4.md#insn-00b6a408) · [`00b6a41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a3d4.md#insn-00b6a41c) · [`00b6a474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a3d4.md#insn-00b6a474)
- 新版 [`00b6a4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md#insn-00b6a4d0) · [`00b6a4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md#insn-00b6a4e4) · [`00b6a53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a49c.md#insn-00b6a53c)

~~~diff
- 00b6a408 ["INT_ADD", "register:40f0:8", ["const:b6a408:8", "const:4:8"]]
- 00b6a408 ["CALL", null, ["callee:00bde390:8"]]
+ 00b6a4d0 ["INT_ADD", "register:40f0:8", ["const:b6a4d0:8", "const:4:8"]]
+ 00b6a4d0 ["CALL", null, ["callee:00bde390:8"]]
- 00b6a408 bytes b6cf0194
+ 00b6a4d0 bytes b0cf0194
- 00b6a41c ["INT_ADD", "register:40f0:8", ["const:b6a41c:8", "const:4:8"]]
- 00b6a41c ["CALL", null, ["callee:00bde130:8"]]
+ 00b6a4e4 ["INT_ADD", "register:40f0:8", ["const:b6a4e4:8", "const:4:8"]]
+ 00b6a4e4 ["CALL", null, ["callee:00bde130:8"]]
- 00b6a41c bytes 19cf0194
+ 00b6a4e4 bytes 13cf0194
- 00b6a474 ["INT_ADD", "register:40f0:8", ["const:b6a474:8", "const:4:8"]]
- 00b6a474 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b6a53c ["INT_ADD", "register:40f0:8", ["const:b6a53c:8", "const:4:8"]]
+ 00b6a53c ["CALL", null, ["callee:00bddcf0:8"]]
- 00b6a474 bytes f3cd0194
+ 00b6a53c bytes edcd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa830c52d68e696430dd1160a08fd16"></a>

### [`00b6a558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a558.md) → [`00b6a620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 83.19% / 新版 83.19%

CFGの説明率　旧版 47.83% / 新版 42.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a670",
      "incomplete_value": false,
      "site": "00b6a674",
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
      "definition_site": "00b6a5a8",
      "incomplete_value": false,
      "site": "00b6a5ac",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a5c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a6cc",
      "incomplete_value": true,
      "site": "00b6a6e8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a604",
      "incomplete_value": true,
      "site": "00b6a620",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:720:8"
              ]
            ]
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
      "00b6a654",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a6d8"
      ]
    ],
    [
      "unmatched:00b6a5a8",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a654",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a7a0"
      ]
    ],
    [
      "00b6a670",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a57c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a558.md#insn-00b6a57c) · [`00b6a5ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a558.md#insn-00b6a5ac) · [`00b6a5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a558.md#insn-00b6a5c8)
- 新版 [`00b6a644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md#insn-00b6a644) · [`00b6a674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a620.md#insn-00b6a674)

~~~diff
- 00b6a57c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6a57c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00b6a644 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b6a644 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b6a57c bytes 810a00b4
+ 00b6a644 bytes 810a00b4
- 00b6a5ac ["INT_ADD", "register:40f0:8", ["const:b6a5ac:8", "const:4:8"]]
- 00b6a5ac ["CALL", null, ["callee:00bde130:8"]]
+ 00b6a674 ["INT_ADD", "register:40f0:8", ["const:b6a674:8", "const:4:8"]]
+ 00b6a674 ["CALL", null, ["callee:00bde130:8"]]
- 00b6a5ac bytes b5ce0194
+ 00b6a674 bytes afce0194
- 00b6a5c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6a5c8 ["INT_ADD", "register:40f0:8", ["const:b6a5c8:8", "const:4:8"]]
- 00b6a5c8 ["CALLIND", null, ["register:0:8"]]
- 00b6a5c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-379e11c9911cc602cd67f34419b5eb99"></a>

### [`00b6a71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a71c.md) → [`00b6a7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a7e4.md) _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 64.86% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 4件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a774"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a790"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6a894",
      "incomplete_value": true,
      "site": "00b6a8a8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6a7cc",
      "incomplete_value": true,
      "site": "00b6a7e0",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:720:8"
              ]
            ]
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
      "00b6a818",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a81c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6a8b0"
      ]
    ],
    [
      "unmatched:00b6a770",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6a818",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6a81c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6a978"
      ]
    ],
    [
      "00b6a838",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6a774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a71c.md#insn-00b6a774) · [`00b6a790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a71c.md#insn-00b6a790) · [`00b6a7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a71c.md#insn-00b6a7e0)
- 新版 [`00b6a8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6a7e4.md#insn-00b6a8a8)

~~~diff
- 00b6a774 ["INT_ADD", "register:40f0:8", ["const:b6a774:8", "const:4:8"]]
- 00b6a774 ["CALL", null, ["callee:00bde130:8"]]
- 00b6a774 bytes 43ce0194
- 00b6a790 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6a790 ["INT_ADD", "register:40f0:8", ["const:b6a790:8", "const:4:8"]]
- 00b6a790 ["CALLIND", null, ["register:0:8"]]
- 00b6a790 bytes 00013fd6
- 00b6a7e0 ["INT_ADD", "register:40f0:8", ["const:b6a7e0:8", "const:4:8"]]
- 00b6a7e0 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b6a8a8 ["INT_ADD", "register:40f0:8", ["const:b6a8a8:8", "const:4:8"]]
+ 00b6a8a8 ["CALL", null, ["callee:00bddcf0:8"]]
- 00b6a7e0 bytes 18cd0194
+ 00b6a8a8 bytes 12cd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c31b12019a8cc447e728e49c713366"></a>

### [`00b6a9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a9dc.md) → [`00b6aaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md) _ZN8firebase4auth22GameCenterAuthProvider13GetCredentialEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00b6c9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c9f4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00b6cabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cabc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6aab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6ab78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6aa30",
      "incomplete_value": true,
      "site": "00b6aa38",
      "value": [
        "live",
        "register:40a0:8"
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
      "00b6aaec",
      "READ",
      [
        "storage",
        "00c1bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00b6aaec",
      "PARAM",
      [
        "storage",
        "00b6c9f4",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "unmatched:00b6aa60",
      "PARAM",
      [
        "storage",
        "002a9013",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6aaec",
      "READ",
      [
        "storage",
        "00c1bbb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6aaec",
      "PARAM",
      [
        "storage",
        "00b6cabc",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10CredentialEEEvPv",
        null
      ]
    ],
    [
      "00b6ab28",
      "PARAM",
      [
        "storage",
        "002a8f7f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6aa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a9dc.md#insn-00b6aa38) · [`00b6aa74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a9dc.md#insn-00b6aa74) · [`00b6aa88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6a9dc.md#insn-00b6aa88)
- 新版 [`00b6ab00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md#insn-00b6ab00) · [`00b6ab3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md#insn-00b6ab3c) · [`00b6ab50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aaa4.md#insn-00b6ab50)

~~~diff
- 00b6aa38 ["INT_ADD", "register:40f0:8", ["const:b6aa38:8", "const:4:8"]]
- 00b6aa38 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b6ab00 ["INT_ADD", "register:40f0:8", ["const:b6ab00:8", "const:4:8"]]
+ 00b6ab00 ["CALL", null, ["callee:00bddf70:8"]]
- 00b6aa38 bytes 22cd0194
+ 00b6ab00 bytes 1ccd0194
- 00b6aa74 ["INT_ADD", "register:40f0:8", ["const:b6aa74:8", "const:4:8"]]
- 00b6aa74 ["CALL", null, ["callee:00be0d80:8"]]
+ 00b6ab3c ["INT_ADD", "register:40f0:8", ["const:b6ab3c:8", "const:4:8"]]
+ 00b6ab3c ["CALL", null, ["callee:00be0d80:8"]]
- 00b6aa74 bytes 97d80194
+ 00b6ab3c bytes 91d80194
- 00b6aa88 ["INT_ADD", "register:40f0:8", ["const:b6aa88:8", "const:4:8"]]
- 00b6aa88 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6ab50 ["INT_ADD", "register:40f0:8", ["const:b6ab50:8", "const:4:8"]]
+ 00b6ab50 ["CALL", null, ["callee:00bde130:8"]]
- 00b6aa88 bytes 7ecd0194
+ 00b6ab50 bytes 78cd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

