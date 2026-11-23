# v15.7.2 → v15.7.3 · 最優先の変更候補 (80)

[一覧の目次](README.md)

<a id="compare-2487fd1644a0d2e18bf3f24c470b5208"></a>

### [`00bd67b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd67b0.md) → [`00bd6878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md) FUN_00bd6878

採用 · 移動量 `+0xc8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd6588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6588.md) · 呼出先 3件 [`00bd67ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd67ec.md) [`00bdd3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd3b0.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 1件 [`00bd6650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6650.md) · 呼出先 3件 [`00bd68b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd68b4.md) [`00bdd460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd460.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd68a0",
      "incomplete_value": false,
      "site": "00bd68a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd67d8",
      "incomplete_value": false,
      "site": "00bd67d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "definition_site": "00bd6884",
      "incomplete_value": false,
      "site": "00bd6890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:954:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd67bc",
      "incomplete_value": false,
      "site": "00bd67c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:894:8"
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
      "definition_site": "00bd688c",
      "incomplete_value": false,
      "site": "00bd6890",
      "value": [
        "leaf",
        "const:bd68b4:8"
      ]
    },
    "old": {
      "definition_site": "00bd67c4",
      "incomplete_value": false,
      "site": "00bd67c8",
      "value": [
        "leaf",
        "const:bd67ec:8"
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
      "00bd6884",
      "PARAM",
      [
        "storage",
        "010a3894",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd688c",
      "PARAM",
      [
        "storage",
        "00bd67ec",
        null,
        null
      ]
    ],
    [
      "00bd68a0",
      "WRITE",
      [
        "storage",
        "010a3890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd6884",
      "PARAM",
      [
        "storage",
        "010a3954",
        null,
        "undefined4"
      ]
    ],
    [
      "00bd688c",
      "PARAM",
      [
        "storage",
        "00bd68b4",
        null,
        null
      ]
    ],
    [
      "00bd68a0",
      "WRITE",
      [
        "storage",
        "010a3950",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd67c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd67b0.md#insn-00bd67c8) · [`00bd67d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd67b0.md#insn-00bd67d8) · [`00bd67bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd67b0.md#insn-00bd67bc)
- 新版 [`00bd6890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md#insn-00bd6890) · [`00bd68a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md#insn-00bd68a0) · [`00bd6884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6878.md#insn-00bd6884)

~~~diff
- 00bd67c8 ["INT_ADD", "register:40f0:8", ["const:bd67c8:8", "const:4:8"]]
- 00bd67c8 ["CALL", null, ["callee:00bdd460:8"]]
+ 00bd6890 ["INT_ADD", "register:40f0:8", ["const:bd6890:8", "const:4:8"]]
+ 00bd6890 ["CALL", null, ["callee:00bdd460:8"]]
- 00bd67c8 bytes fa1a0094
+ 00bd6890 bytes f41a0094
- 00bd67d8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bd67d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:890:8"]]
- 00bd67d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd68a0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bd68a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:950:8"]]
+ 00bd68a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd67d8 bytes 09412239
+ 00bd68a0 bytes 09412539
- 00bd67bc ["COPY", "tmp:0:8", ["const:894:8"]]
- 00bd67bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bd67bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bd67bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd6884 ["COPY", "tmp:0:8", ["const:954:8"]]
+ 00bd6884 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6884 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd6884 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bd67bc bytes 00502291
+ 00bd6884 bytes 00502591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa478efd741aed142c6ee1198d23025c"></a>

### [`00bd68b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd68b4.md) → [`00bd6974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6974.md) _INIT_0

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be0130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0130.md) [`00be1e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e60.md) [`00be1e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md) [`00be1f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f10.md) [`00be1f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f20.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.79% / 新版 65.79%

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
      "site": "00bd68d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd693c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd68d4",
      "WRITE",
      [
        "storage",
        "010a38d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd68e8",
      "PARAM",
      [
        "storage",
        "002967c0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd68f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be1f20"
      ]
    ]
  ],
  "added": [
    [
      "00bd6994",
      "WRITE",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd69a8",
      "PARAM",
      [
        "storage",
        "0029684d",
        null,
        "string"
      ]
    ],
    [
      "00bd69b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00be1f20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd68d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd68b4.md#insn-00bd68d4) · [`00bd68f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd68b4.md#insn-00bd68f0) · [`00bd68f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd68b4.md#insn-00bd68f8)

~~~diff
- 00bd68d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd68d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd68d4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:8d0:8"]]
- 00bd68d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd68d4 bytes 3f412339
- 00bd68f0 ["INT_ADD", "register:40f0:8", ["const:bd68f0:8", "const:4:8"]]
- 00bd68f0 ["CALL", null, ["callee:00be1f20:8"]]
- 00bd68f0 bytes 602d0094
- 00bd68f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd68f8 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00bd68f8 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bd68f8 bytes cd010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16b7b3e70e44b7ae362e2f53322e177e"></a>

### [`00bd694c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd694c.md) → [`00bd6a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md) FUN_00bd6a0c

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bd6bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6bf8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00bd6cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md) · 呼出先 0件 

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd6cb0",
      "incomplete_value": false,
      "site": "00bd6cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6bf0",
      "incomplete_value": false,
      "site": "00bd6bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "unmatched:00bd69cc",
      "READ",
      [
        "storage",
        "002b1370",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6a24",
      "READ",
      [
        "storage",
        "002b1880",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6a68",
      "READ",
      [
        "storage",
        "002b0c50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd6a8c",
      "READ",
      [
        "storage",
        "002b1370",
        null,
        null
      ]
    ],
    [
      "00bd6ae4",
      "READ",
      [
        "storage",
        "002b1880",
        null,
        null
      ]
    ],
    [
      "00bd6b28",
      "READ",
      [
        "storage",
        "002b0c50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd694c.md#insn-00bd6bf0) · [`00bd69cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd694c.md#insn-00bd69cc) · [`00bd6a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd694c.md#insn-00bd6a24)
- 新版 [`00bd6cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md#insn-00bd6cb0)

~~~diff
- 00bd6bf0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8d8:8"]]
- 00bd6bf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bd6cb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:998:8"]]
+ 00bd6cb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd6bf0 bytes 286d04f9
+ 00bd6cb0 bytes 28cd04f9
- 00bd69cc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:370:8"]]
- 00bd69cc ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 00bd69cc ["COPY", "register:50d0:8", ["const:0:8"]]
- 00bd69cc ["COPY", "register:50d8:8", ["const:0:8"]]
- 00bd69cc bytes 46ddc03d
- 00bd6a24 ["INT_ADD", "tmp:0:8", ["register:4078:8", "const:880:8"]]
- 00bd6a24 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00bd6a24 ["COPY", "register:5010:8", ["const:0:8"]]
- 00bd6a24 ["COPY", "register:5018:8", ["const:0:8"]]
- 00bd6a24 bytes e021c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35790fadefa0ebc1321f893b83bd7e51"></a>

### [`00bd6bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6bf8.md) → [`00bd6cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md) _INIT_1

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd694c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd694c.md) [`00be0130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0130.md) [`00be1e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e60.md) [`00be1e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bd6a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6a0c.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md) [`00be1f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f10.md) [`00be1f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd6cc4",
      "incomplete_value": true,
      "site": "00bd6cc4",
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
      "definition_site": "00bd6c04",
      "incomplete_value": true,
      "site": "00bd6c04",
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
      "definition_site": "00bd6cdc",
      "incomplete_value": false,
      "site": "00bd6ce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:84d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6c1c",
      "incomplete_value": false,
      "site": "00bd6c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "00bd6cf4",
      "incomplete_value": false,
      "site": "00bd6d00",
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
            "const:acc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6c34",
      "incomplete_value": false,
      "site": "00bd6c40",
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
            "const:a3f:8"
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
      "00bd6cc0",
      "READ",
      [
        "storage",
        "010a38d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6cdc",
      "PARAM",
      [
        "storage",
        "002967c0",
        null,
        "string"
      ]
    ],
    [
      "00bd6cf4",
      "PARAM",
      [
        "storage",
        "00299a3f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6cc0",
      "READ",
      [
        "storage",
        "010a3998",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd6cdc",
      "PARAM",
      [
        "storage",
        "0029684d",
        null,
        "string"
      ]
    ],
    [
      "00bd6cf4",
      "PARAM",
      [
        "storage",
        "00299acc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6bf8.md#insn-00bd6c24) · [`00bd6c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6bf8.md#insn-00bd6c40) · [`00bd6c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6bf8.md#insn-00bd6c00)
- 新版 [`00bd6ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md#insn-00bd6ce4) · [`00bd6d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md#insn-00bd6d00) · [`00bd6cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6cb8.md#insn-00bd6cc0)

~~~diff
- 00bd6c24 ["INT_ADD", "register:40f0:8", ["const:bd6c24:8", "const:4:8"]]
- 00bd6c24 ["CALL", null, ["callee:00be1f20:8"]]
+ 00bd6ce4 ["INT_ADD", "register:40f0:8", ["const:bd6ce4:8", "const:4:8"]]
+ 00bd6ce4 ["CALL", null, ["callee:00be1f20:8"]]
- 00bd6c24 bytes 932c0094
+ 00bd6ce4 bytes 8f2c0094
- 00bd6c40 ["INT_ADD", "register:40f0:8", ["const:bd6c40:8", "const:4:8"]]
- 00bd6c40 ["CALL", null, ["callee:00be01e0:8"]]
+ 00bd6d00 ["INT_ADD", "register:40f0:8", ["const:bd6d00:8", "const:4:8"]]
+ 00bd6d00 ["CALL", null, ["callee:00be01e0:8"]]
- 00bd6c40 bytes 3c250094
+ 00bd6d00 bytes 38250094
- 00bd6c00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8d8:8"]]
- 00bd6c00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6cc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
+ 00bd6cc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bd6c00 bytes 086d44f9
+ 00bd6cc0 bytes 08cd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83e8a08da2f38400215684f38eec147b"></a>

### [`00bd6c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6c90.md) → [`00bd6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md) FUN_00bd6d50

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b73484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73484.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b7354c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b7354c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 42.86% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6cb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd6d74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bd6cb4"
      ],
      [
        "FALL_THROUGH",
        "00bd6d74"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bd6d74",
      "incomplete_value": true,
      "site": "00bd6d78",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "live",
            "register:101:1"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6cb4",
      "incomplete_value": true,
      "site": "00bd6cb8",
      "value": [
        "BOOL_NEGATE",
        "1",
        [
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6d58",
      "READ",
      [
        "storage",
        "010a38d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd6cb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6d80"
      ]
    ]
  ],
  "added": [
    [
      "00bd6d58",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6d74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6d80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6c90.md#insn-00bd6cb4) · [`00bd6c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6c90.md#insn-00bd6c98)
- 新版 [`00bd6d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md#insn-00bd6d74) · [`00bd6d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d50.md#insn-00bd6d58)

~~~diff
- 00bd6cb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd6cb4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd6cb4 bytes 61000054
+ 00bd6d74 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bd6d74 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bd6d74 bytes 61000054
- 00bd6c98 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8d0:8"]]
- 00bd6c98 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6c98 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00bd6d58 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:990:8"]]
+ 00bd6d58 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6d58 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6c98 bytes 10426339
+ 00bd6d58 bytes 10426639
~~~


<a id="compare-446010ae52770c2b97b8576599ab3516"></a>

### [`00bd6cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6cd0.md) → [`00bd6d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d90.md) FUN_00bd6d90

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 3件 [`00bbab14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab14.md) [`00bbab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab48.md) [`00bbab7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab7c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00bbabdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabdc.md) [`00bbac10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac10.md) [`00bbac44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac44.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 42.86% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bd6da0",
      "incomplete_value": true,
      "site": "00bd6da4",
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
            "register:4008:8"
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
      "00bd6d98",
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
      "00bd6d98",
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

- 旧版 [`00bd6cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6cd0.md#insn-00bd6cd8) · [`00bd6cdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6cd0.md#insn-00bd6cdc) · [`00bd6cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6cd0.md#insn-00bd6cf4)
- 新版 [`00bd6d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d90.md#insn-00bd6d98) · [`00bd6d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d90.md#insn-00bd6d9c) · [`00bd6db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6d90.md#insn-00bd6db4)

~~~diff
- 00bd6cd8 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8d0:8"]]
- 00bd6cd8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6cd8 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00bd6d98 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:990:8"]]
+ 00bd6d98 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bd6d98 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6cd8 bytes 10426339
+ 00bd6d98 bytes 10426639
- 00bd6cdc ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
- 00bd6cdc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd6d9c ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
+ 00bd6d9c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd6cdc bytes 70000034
+ 00bd6d9c bytes 70000034
- 00bd6cf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00bd6cf4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd6db4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
+ 00bd6db4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd6cf4 bytes d1ffff35
+ 00bd6db4 bytes d1ffff35
~~~


<a id="compare-c97fe31c18418eda638f887b7c34a427"></a>

### [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) → [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) FUN_00bd6e50

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1479件 [`00418394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b18.md) · 呼出先 0件 
- 新版 呼出元 1479件 [`00418394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6e74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd6e58",
      "READ",
      [
        "storage",
        "010a38d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd6db8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6e6c"
      ]
    ]
  ],
  "added": [
    [
      "00bd6e58",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd6e78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6e6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md#insn-00bd6db4) · [`00bd6db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md#insn-00bd6db8) · [`00bd6dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md#insn-00bd6dbc)

~~~diff
- 00bd6db4 ["COPY", "tmp:0:1", ["const:1:1"]]
- 00bd6db4 ["CALLOTHER", "tmp:1:1", ["const:3f:4", "register:4008:8", "const:10:1"]]
- 00bd6db4 ["BOOL_NEGATE", "tmp:2:1", ["tmp:1:1"]]
- 00bd6db4 ["CBRANCH", null, ["const:3:4", "tmp:2:1"]]
- 00bd6db4 bytes 31fc0fc8
- 00bd6db8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4078:4", "const:0:4"]]
- 00bd6db8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd6db8 bytes afffff35
- 00bd6dbc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6dbc ["RETURN", null, ["register:0:8"]]
- 00bd6dbc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91760ee239a752632b089057533d5bf6"></a>

### [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) → [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) FUN_00bd6e80

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd5128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5128.md) [`00bd534c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd534c.md) [`00bd54dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd54dc.md) · 呼出先 6件 [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) [`00bd7230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md) [`00bd72d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd72d8.md) [`00bd7440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7440.md) [`00bd7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md)
- 新版 呼出元 3件 [`00bd51f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd51f0.md) [`00bd5414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md) [`00bd55a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd55a4.md) · 呼出先 6件 [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) [`00bd7500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7500.md) [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 25.00% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6e84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd6f44"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd6e24",
      "incomplete_value": true,
      "site": "00bd6e2c",
      "value": [
        "live",
        "register:8:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md#insn-00bd6e2c) · [`00bd6e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md#insn-00bd6e84) · [`00bd6e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md#insn-00bd6e88)
- 新版 [`00bd6eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md#insn-00bd6eec) · [`00bd6f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md#insn-00bd6f48)

~~~diff
- 00bd6e2c ["INT_ADD", "register:40f0:8", ["const:bd6e2c:8", "const:4:8"]]
- 00bd6e2c ["CALL", null, ["callee:00bd7528:8"]]
+ 00bd6eec ["INT_ADD", "register:40f0:8", ["const:bd6eec:8", "const:4:8"]]
+ 00bd6eec ["CALL", null, ["callee:00bd7528:8"]]
- 00bd6e2c bytes 8f010094
+ 00bd6eec bytes 8f010094
- 00bd6e84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00bd6e84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd6e84 bytes 680e00f9
- 00bd6e88 ["INT_ADD", "register:40f0:8", ["const:bd6e88:8", "const:4:8"]]
- 00bd6e88 ["CALL", null, ["callee:00bd6f78:8"]]
+ 00bd6f48 ["INT_ADD", "register:40f0:8", ["const:bd6f48:8", "const:4:8"]]
+ 00bd6f48 ["CALL", null, ["callee:00bd6f78:8"]]
- 00bd6e88 bytes 0c000094
+ 00bd6f48 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af1b736556345673162f33dadc6366b"></a>

### [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) → [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) FUN_00bd6f78

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) · 呼出先 9件 [`00bd7230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md) [`00bd72d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd72d8.md) [`00bd7454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7454.md) [`00bd7468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7468.md) [`00bd74a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74a8.md)
- 新版 呼出元 2件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) · 呼出先 9件 [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) [`00bd7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7398.md) [`00bd7514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7514.md) [`00bd7528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7528.md) [`00bd7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7568.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 33.33% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6f30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fbc"
      ]
    ],
    [
      "unmatched:00bd6f6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fbc"
      ]
    ],
    [
      "unmatched:00bd6f78",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd6ff0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fbc"
      ]
    ],
    [
      "00bd702c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd6fbc"
      ]
    ],
    [
      "00bd7038",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md#insn-00bd6f00) · [`00bd6f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md#insn-00bd6f30) · [`00bd6f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md#insn-00bd6f50)
- 新版 [`00bd6fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md#insn-00bd6fc0)

~~~diff
- 00bd6f00 ["INT_ADD", "register:40f0:8", ["const:bd6f00:8", "const:4:8"]]
- 00bd6f00 ["CALL", null, ["callee:00bd7514:8"]]
+ 00bd6fc0 ["INT_ADD", "register:40f0:8", ["const:bd6fc0:8", "const:4:8"]]
+ 00bd6fc0 ["CALL", null, ["callee:00bd7514:8"]]
- 00bd6f00 bytes 55010094
+ 00bd6fc0 bytes 55010094
- 00bd6f30 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bd6f30 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd6f30 bytes 68feffb4
- 00bd6f50 ["COPY", "tmp:0:4", ["register:40b0:4"]]
- 00bd6f50 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bd6f50 ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00bd6f50 ["INT_ZEXT", "register:4008:8", ["tmp:0:4"]]
- 00bd6f50 bytes c102951a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-463b6eeaed76906e66a84c5459d19eaa"></a>

### [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) → [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) FUN_00bd70ac

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 253件 [`0043e5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e5d8.md) [`0043e940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043e940.md) [`00445124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445124.md) [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`00455270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00455/00455270.md) · 呼出先 7件 [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) [`00bd7070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md) [`00bdacd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdacd8.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md)
- 新版 呼出元 253件 [`0043e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e5d8.md) [`0043e940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e940.md) [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`00455270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00455/00455270.md) · 呼出先 7件 [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) [`00bdad98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdad98.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.88% / 新版 87.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd711c",
      "incomplete_value": true,
      "site": "00bd7120",
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
      "definition_site": "00bd705c",
      "incomplete_value": true,
      "site": "00bd7060",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7110",
      "incomplete_value": false,
      "site": "00bd7120",
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
            "const:605:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7050",
      "incomplete_value": false,
      "site": "00bd7060",
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
            "const:60e:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7118",
      "incomplete_value": false,
      "site": "00bd7120",
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
            "const:82d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7058",
      "incomplete_value": false,
      "site": "00bd7060",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7108",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7110",
      "PARAM",
      [
        "storage",
        "002ac60e",
        null,
        "string"
      ]
    ],
    [
      "00bd7118",
      "PARAM",
      [
        "storage",
        "002957a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7108",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7110",
      "PARAM",
      [
        "storage",
        "002ac605",
        null,
        "string"
      ]
    ],
    [
      "00bd7118",
      "PARAM",
      [
        "storage",
        "0029582d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md#insn-00bd7060) · [`00bd7008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md#insn-00bd7008) · [`00bd7020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md#insn-00bd7020)
- 新版 [`00bd7120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md#insn-00bd7120) · [`00bd70c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md#insn-00bd70c8) · [`00bd70e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md#insn-00bd70e0)

~~~diff
- 00bd7060 ["INT_ADD", "register:40f0:8", ["const:bd7060:8", "const:4:8"]]
- 00bd7060 ["CALL", null, ["callee:00be1f30:8"]]
+ 00bd7120 ["INT_ADD", "register:40f0:8", ["const:bd7120:8", "const:4:8"]]
+ 00bd7120 ["CALL", null, ["callee:00be1f30:8"]]
- 00bd7060 bytes 882b0094
+ 00bd7120 bytes 842b0094
- 00bd7008 ["INT_ADD", "register:40f0:8", ["const:bd7008:8", "const:4:8"]]
- 00bd7008 ["CALL", null, ["callee:00bdad98:8"]]
+ 00bd70c8 ["INT_ADD", "register:40f0:8", ["const:bd70c8:8", "const:4:8"]]
+ 00bd70c8 ["CALL", null, ["callee:00bdad98:8"]]
- 00bd7008 bytes 340f0094
+ 00bd70c8 bytes 340f0094
- 00bd7020 ["INT_ADD", "register:40f0:8", ["const:bd7020:8", "const:4:8"]]
- 00bd7020 ["CALL", null, ["callee:00bd6f78:8"]]
+ 00bd70e0 ["INT_ADD", "register:40f0:8", ["const:bd70e0:8", "const:4:8"]]
+ 00bd70e0 ["CALL", null, ["callee:00bd6f78:8"]]
- 00bd7020 bytes a6ffff97
+ 00bd70e0 bytes a6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac5bb22d9e5f2cca7719aaef91046134"></a>

### [`00bd7230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md) → [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) FUN_00bd72f0

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00bd6dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6dc0.md) [`00bd6eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6eb8.md) [`00bd7070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7070.md) · 呼出先 2件 [`00bd7cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 3件 [`00bd6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e80.md) [`00bd6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6f78.md) [`00bd7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7130.md) · 呼出先 2件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd731c",
      "incomplete_value": false,
      "site": "00bd731c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd725c",
      "incomplete_value": false,
      "site": "00bd725c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bd731c",
      "incomplete_value": false,
      "site": "00bd731c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd725c",
      "incomplete_value": false,
      "site": "00bd725c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bd7338",
      "value": [
        "live",
        "register:5020:16"
      ]
    },
    "old": {
      "definition_site": "00bd7264",
      "incomplete_value": true,
      "site": "00bd7278",
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
                "live",
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:130:8"
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
      "00bd731c",
      "DATA",
      [
        "storage",
        "00c1a118",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd731c",
      "DATA",
      [
        "storage",
        "010a38e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd731c",
      "DATA",
      [
        "storage",
        "00c1a1c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bd731c",
      "DATA",
      [
        "storage",
        "010a39a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md#insn-00bd7244) · [`00bd7248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md#insn-00bd7248) · [`00bd724c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md#insn-00bd724c)
- 新版 [`00bd7304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md#insn-00bd7304) · [`00bd730c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md#insn-00bd730c)

~~~diff
- 00bd7244 ["COPY", "tmp:0:8", ["const:118:8"]]
- 00bd7244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd7244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bd7304 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00bd7304 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7304 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bd7304 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd7244 bytes 08610491
+ 00bd7304 bytes 08210791
- 00bd7248 ["COPY", "register:4048:8", ["const:10a3000:8"]]
- 00bd7248 bytes 69260090
- 00bd724c ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00bd724c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd724c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd724c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bd730c ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00bd730c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd730c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bd730c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd724c bytes 29812391
+ 00bd730c bytes 29812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b3c6afdf20ff4ab249c66219ed94bc9"></a>

### [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) → [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) FUN_00bd7590

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd7cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md) [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) [`00bda9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md) · 呼出先 3件 [`00bd7660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md) [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md)
- 新版 呼出元 3件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 呼出先 3件 [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 48.28% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd74d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd74d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd74d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd74d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd74d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd74dc",
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
      "00bd7594",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bd7598",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd759c",
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

- 旧版 [`00bd74d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md#insn-00bd74d4) · [`00bd74d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md#insn-00bd74d8) · [`00bd74dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md#insn-00bd74dc)

~~~diff
- 00bd74d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd74d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd74d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bd74d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd74d4 bytes fd7bbaa9
- 00bd74d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd74d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00bd74d8 bytes fb0b00f9
- 00bd74dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bd74dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bd74dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd74dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd74dc bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1fb18c52d36ab5731b3ccd696d18d85"></a>

### [`00bd7660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md) → [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) FUN_00bd7720

採用 · 移動量 `+0xc0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) [`00bda7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md) · 呼出先 6件 [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md)
- 新版 呼出元 2件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) · 呼出先 6件 [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.39% / 新版 85.39%

CFGの説明率　旧版 45.95% / 新版 47.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 7件, `store_destination` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7774"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd7784",
      "DATA",
      [
        "storage",
        "002ac661",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd772c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd79b4"
      ]
    ],
    [
      "unmatched:00bd7778",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7868"
      ]
    ]
  ],
  "added": [
    [
      "00bd7784",
      "DATA",
      [
        "storage",
        "002ac658",
        null,
        "string"
      ]
    ],
    [
      "00bd77ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd79b4"
      ]
    ],
    [
      "00bd7838",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7868"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd76c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md#insn-00bd76c8) · [`00bd772c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md#insn-00bd772c) · [`00bd7768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md#insn-00bd7768)
- 新版 [`00bd7788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md#insn-00bd7788)

~~~diff
- 00bd76c8 ["BRANCH", null, ["local:b51:8"]]
+ 00bd7788 ["BRANCH", null, ["local:b49:8"]]
- 00bd76c8 bytes 84000014
+ 00bd7788 bytes 84000014
- 00bd772c ["CBRANCH", null, ["local:b52:8", "register:101:1"]]
- 00bd772c bytes 400e0054
- 00bd7768 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd7768 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd7768 ["COPY", "tmp:2:4", ["const:0:4"]]
- 00bd7768 ["COPY", "tmp:3:4", ["register:4058:4"]]
- 00bd7768 bytes 6b819f1a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-405439d4d670f9cc37e9e78f41ea4fc7"></a>

### [`00bd797c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd797c.md) → [`00bd7a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7a3c.md) FUN_00bd7a3c

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 60.00% / 新版 65.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd799c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd7a5c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00bd7a4c",
      "incomplete_value": false,
      "site": "00bd7a54",
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
            "const:a4a:8"
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
      "unmatched:00bd799c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7aa4"
      ]
    ],
    [
      "unmatched:00bd7a3c",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7a44",
      "PARAM",
      [
        "storage",
        "0029f21f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7a5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd7aa4"
      ]
    ],
    [
      "00bd7afc",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7b04",
      "PARAM",
      [
        "storage",
        "0029f2ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd797c.md#insn-00bd7994) · [`00bd799c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd797c.md#insn-00bd799c) · [`00bd7a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd797c.md#insn-00bd7a54)
- 新版 [`00bd7a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7a3c.md#insn-00bd7a54) · [`00bd7b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7a3c.md#insn-00bd7b14)

~~~diff
- 00bd7994 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
+ 00bd7a54 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00bd7994 bytes a0030054
+ 00bd7a54 bytes a0030054
- 00bd799c ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00bd799c bytes 40020054
- 00bd7a54 ["INT_ADD", "register:40f0:8", ["const:bd7a54:8", "const:4:8"]]
- 00bd7a54 ["CALL", null, ["callee:00be1f30:8"]]
+ 00bd7b14 ["INT_ADD", "register:40f0:8", ["const:bd7b14:8", "const:4:8"]]
+ 00bd7b14 ["CALL", null, ["callee:00be1f30:8"]]
- 00bd7a54 bytes 0b290094
+ 00bd7b14 bytes 07290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b969da9286c46b9f1bd9a3c991761869"></a>

### [`00bd7a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7a64.md) → [`00bd7b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md) FUN_00bd7b24

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 81.82% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7bf8",
      "incomplete_value": true,
      "site": "00bd7bfc",
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
      "definition_site": "00bd7b38",
      "incomplete_value": true,
      "site": "00bd7b3c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7bec",
      "incomplete_value": false,
      "site": "00bd7bfc",
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
            "const:2de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7b2c",
      "incomplete_value": false,
      "site": "00bd7b3c",
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
            "const:2e5:8"
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
      "definition_site": "00bd7bf4",
      "incomplete_value": false,
      "site": "00bd7bfc",
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
            "const:ad7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7b34",
      "incomplete_value": false,
      "site": "00bd7b3c",
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
            "const:a4a:8"
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
      "unmatched:00bd7b20",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7b24",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7b2c",
      "PARAM",
      [
        "storage",
        "002a52e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd7be0",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "00bd7be4",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd7bec",
      "PARAM",
      [
        "storage",
        "002a52de",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7a64.md#insn-00bd7a7c) · [`00bd7b3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7a64.md#insn-00bd7b3c) · [`00bd7a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7a64.md#insn-00bd7a88)
- 新版 [`00bd7b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md#insn-00bd7b3c) · [`00bd7bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md#insn-00bd7bfc) · [`00bd7b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7b24.md#insn-00bd7b48)

~~~diff
- 00bd7a7c ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
+ 00bd7b3c ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00bd7a7c bytes a0030054
+ 00bd7b3c bytes a0030054
- 00bd7b3c ["INT_ADD", "register:40f0:8", ["const:bd7b3c:8", "const:4:8"]]
- 00bd7b3c ["CALL", null, ["callee:00be1f30:8"]]
+ 00bd7bfc ["INT_ADD", "register:40f0:8", ["const:bd7bfc:8", "const:4:8"]]
+ 00bd7bfc ["CALL", null, ["callee:00be1f30:8"]]
- 00bd7b3c bytes d1280094
+ 00bd7bfc bytes cd280094
- 00bd7a88 ["BRANCH", null, ["local:b13:8"]]
+ 00bd7b48 ["BRANCH", null, ["local:b14:8"]]
- 00bd7a88 bytes 14000014
+ 00bd7b48 bytes 14000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2c149de381bb338aadea48d2e521f1d"></a>

### [`00bd7c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7c70.md) → [`00bd7d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7d30.md) FUN_00bd7d30

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7c70.md#insn-00bd7c78)
- 新版 [`00bd7d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7d30.md#insn-00bd7d38)

~~~diff
- 00bd7c78 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bd7c78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd7d38 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00bd7d38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bd7c78 bytes c8000034
+ 00bd7d38 bytes c8000034
~~~


<a id="compare-2e30847442f6364762865aeaafd8970f"></a>

### [`00bd7cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md) → [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) FUN_00bd7db8

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7230.md) · 呼出先 10件 [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) [`00bd84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md) [`00bda2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md) [`00bda59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda59c.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bd72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd72f0.md) · 呼出先 10件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) [`00bda65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 94.41% / 新版 94.41%

CFGの説明率　旧版 57.89% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd7f7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd7e08",
      "incomplete_value": false,
      "site": "00bd7e18",
      "value": [
        "leaf",
        "const:bda65c:8"
      ]
    },
    "old": {
      "definition_site": "00bd7d48",
      "incomplete_value": false,
      "site": "00bd7d58",
      "value": [
        "leaf",
        "const:bda59c:8"
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
      "00bd7e08",
      "PARAM",
      [
        "storage",
        "00bda59c",
        null,
        null
      ]
    ],
    [
      "00bd7e44",
      "PARAM",
      [
        "storage",
        "010a38e4",
        null,
        null
      ]
    ],
    [
      "00bd7e54",
      "READ",
      [
        "storage",
        "00c248c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bd7e08",
      "PARAM",
      [
        "storage",
        "00bda65c",
        null,
        null
      ]
    ],
    [
      "00bd7e44",
      "PARAM",
      [
        "storage",
        "010a39a4",
        null,
        null
      ]
    ],
    [
      "00bd7e54",
      "READ",
      [
        "storage",
        "00c24978",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md#insn-00bd7d58) · [`00bd7d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md#insn-00bd7d88) · [`00bd7dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md#insn-00bd7dd0)
- 新版 [`00bd7e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md#insn-00bd7e18) · [`00bd7e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md#insn-00bd7e48) · [`00bd7e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md#insn-00bd7e90)

~~~diff
- 00bd7d58 ["INT_ADD", "register:40f0:8", ["const:bd7d58:8", "const:4:8"]]
- 00bd7d58 ["CALL", null, ["callee:00be1f60:8"]]
+ 00bd7e18 ["INT_ADD", "register:40f0:8", ["const:bd7e18:8", "const:4:8"]]
+ 00bd7e18 ["CALL", null, ["callee:00be1f60:8"]]
- 00bd7d58 bytes 56280094
+ 00bd7e18 bytes 52280094
- 00bd7d88 ["INT_ADD", "register:40f0:8", ["const:bd7d88:8", "const:4:8"]]
- 00bd7d88 ["CALL", null, ["callee:00be1f70:8"]]
+ 00bd7e48 ["INT_ADD", "register:40f0:8", ["const:bd7e48:8", "const:4:8"]]
+ 00bd7e48 ["CALL", null, ["callee:00be1f70:8"]]
- 00bd7d88 bytes 4e280094
+ 00bd7e48 bytes 4a280094
- 00bd7dd0 ["INT_ADD", "register:40f0:8", ["const:bd7dd0:8", "const:4:8"]]
- 00bd7dd0 ["CALL", null, ["callee:00be1f50:8"]]
+ 00bd7e90 ["INT_ADD", "register:40f0:8", ["const:bd7e90:8", "const:4:8"]]
+ 00bd7e90 ["CALL", null, ["callee:00be1f50:8"]]
- 00bd7dd0 bytes 34280094
+ 00bd7e90 bytes 30280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26638f32b6a64e44493e6eada4141e8e"></a>

### [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) → [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) FUN_00bd8120

採用 · 移動量 `+0xc0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7b80.md) · 呼出先 11件 [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) [`00bd84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md) [`00bd906c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd906c.md) [`00bd91a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd91a0.md) [`00bd9904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md)
- 新版 呼出元 1件 [`00bd7c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7c40.md) · 呼出先 11件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bd912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md) [`00bd9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9260.md) [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.32% / 新版 85.32%

CFGの説明率　旧版 59.26% / 新版 59.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd8458"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd81f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd81f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8474"
      ]
    ],
    [
      "unmatched:00bd8238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd82a0"
      ]
    ],
    [
      "unmatched:00bd82f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8510"
      ]
    ]
  ],
  "added": [
    [
      "00bd82b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8474"
      ]
    ],
    [
      "00bd82f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd82a0"
      ]
    ],
    [
      "00bd83b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd8510"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd80ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md#insn-00bd80ac) · [`00bd81f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md#insn-00bd81f0) · [`00bd8238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md#insn-00bd8238)
- 新版 [`00bd816c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md#insn-00bd816c)

~~~diff
- 00bd80ac ["INT_ADD", "register:40f0:8", ["const:bd80ac:8", "const:4:8"]]
- 00bd80ac ["CALL", null, ["callee:00bd7590:8"]]
+ 00bd816c ["INT_ADD", "register:40f0:8", ["const:bd816c:8", "const:4:8"]]
+ 00bd816c ["CALL", null, ["callee:00bd7590:8"]]
- 00bd80ac bytes 09fdff97
+ 00bd816c bytes 09fdff97
- 00bd81f0 ["CBRANCH", null, ["local:b58:8", "register:101:1"]]
- 00bd81f0 bytes 200e0054
- 00bd8238 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd8238 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bd8238 bytes 41fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e699ef31a040630fc31f20323e54cdd0"></a>

### [`00bd84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md) → [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) FUN_00bd85b4

採用 · 移動量 `+0xc0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd7cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md) [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) [`00bda2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md) · 呼出先 8件 [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md)
- 新版 呼出元 3件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) · 呼出先 8件 [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.22% / 新版 60.22%

CFGの説明率　旧版 27.17% / 新版 27.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 20件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd850c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd850c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8544"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd850c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8544",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8550",
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
      "00bd85cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd8604",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00bd8610",
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

- 旧版 [`00bd850c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md#insn-00bd850c) · [`00bd8544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md#insn-00bd8544) · [`00bd8550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md#insn-00bd8550)

~~~diff
- 00bd850c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd850c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd850c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bd850c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd850c bytes f44f05a9
- 00bd8544 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd8544 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bd8544 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00bd8544 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8544 bytes a8a73ca9
- 00bd8550 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd8550 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00bd8550 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00bd8550 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8550 bytes a8af3da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-770904b767cb57496977055c242c19a1"></a>

### [`00bd906c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd906c.md) → [`00bd912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md) FUN_00bd912c

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) · 呼出先 5件 [`00bd9904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) · 呼出先 5件 [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 84.42% / 新版 84.42%

CFGの説明率　旧版 75.86% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd924c",
      "incomplete_value": true,
      "site": "00bd9250",
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
      "definition_site": "00bd918c",
      "incomplete_value": true,
      "site": "00bd9190",
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
            "const:130:8"
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
      "definition_site": "00bd9234",
      "incomplete_value": false,
      "site": "00bd9250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:82b:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9240",
      "incomplete_value": false,
      "site": "00bd9250",
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
            "const:2ac:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00bd9174",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd9178",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd9180",
      "PARAM",
      [
        "storage",
        "0029f21f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd9234",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "00bd9238",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd9240",
      "PARAM",
      [
        "storage",
        "0029f2ac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd906c.md#insn-00bd9190) · [`00bd9090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd906c.md#insn-00bd9090) · [`00bd90a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd906c.md#insn-00bd90a8)
- 新版 [`00bd9250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md#insn-00bd9250) · [`00bd9150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md#insn-00bd9150) · [`00bd9168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md#insn-00bd9168)

~~~diff
- 00bd9190 ["INT_ADD", "register:40f0:8", ["const:bd9190:8", "const:4:8"]]
- 00bd9190 ["CALL", null, ["callee:00be1f30:8"]]
+ 00bd9250 ["INT_ADD", "register:40f0:8", ["const:bd9250:8", "const:4:8"]]
+ 00bd9250 ["CALL", null, ["callee:00be1f30:8"]]
- 00bd9190 bytes 3c230094
+ 00bd9250 bytes 38230094
- 00bd9090 ["BRANCH", null, ["local:b20:8"]]
+ 00bd9150 ["BRANCH", null, ["local:b19:8"]]
- 00bd9090 bytes 2c000014
+ 00bd9150 bytes 2c000014
- 00bd90a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd90a8 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
+ 00bd9168 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00bd9168 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00bd90a8 bytes c1040054
+ 00bd9168 bytes c1040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aba930bb07c7ba49cc4ccd2ea063e19"></a>

### [`00bd91a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd91a0.md) → [`00bd9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9260.md) FUN_00bd9260

採用 · 移動量 `+0xc0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) · 呼出先 5件 [`00bd9904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) · 呼出先 5件 [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 71.79% / 新版 75.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd936c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd9430",
      "incomplete_value": true,
      "site": "00bd9434",
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
            "const:130:8"
          ]
        ]
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
      "definition_site": "00bd945c",
      "incomplete_value": true,
      "site": "00bd9460",
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
      "definition_site": "00bd939c",
      "incomplete_value": true,
      "site": "00bd93a0",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd9338",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd9354",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd935c",
      "PARAM",
      [
        "storage",
        "0029e16a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd93f8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd9414",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bd941c",
      "PARAM",
      [
        "storage",
        "0029e1f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd91ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd91a0.md#insn-00bd91ec) · [`00bd936c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd91a0.md#insn-00bd936c)
- 新版 [`00bd92ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9260.md#insn-00bd92ac)

~~~diff
- 00bd91ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd91ec ["RETURN", null, ["register:0:8"]]
- 00bd91ec bytes c0035fd6
+ 00bd92ac ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00bd92ac ["RETURN", null, ["register:0:8"]]
+ 00bd92ac bytes c0035fd6
- 00bd936c ["INT_ADD", "register:40f0:8", ["const:bd936c:8", "const:4:8"]]
- 00bd936c ["CALL", null, ["callee:00be1f30:8"]]
- 00bd936c bytes c5220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be8f6f87157d171321d7a48eb2a7661"></a>

### [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) → [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) FUN_00bd9470

採用 · 移動量 `+0xc0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) [`00bd7660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md) [`00bd84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md) [`00bda6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md) [`00bda7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md) · 呼出先 5件 [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 6件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bda78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) · 呼出先 5件 [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 69.60% / 新版 69.60%

CFGの説明率　旧版 47.50% / 新版 48.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd95e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd93e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd93e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd95fc"
      ]
    ],
    [
      "unmatched:00bd93e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd961c"
      ]
    ],
    [
      "unmatched:00bd93f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd95bc"
      ]
    ]
  ],
  "added": [
    [
      "00bd94a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd95fc"
      ]
    ],
    [
      "00bd94a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd961c"
      ]
    ],
    [
      "00bd94b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd95bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd93e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md#insn-00bd93e0) · [`00bd93e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md#insn-00bd93e8) · [`00bd93f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md#insn-00bd93f0)

~~~diff
- 00bd93e0 ["CBRANCH", null, ["local:b35:8", "register:101:1"]]
- 00bd93e0 bytes e00a0054
- 00bd93e8 ["CBRANCH", null, ["local:b37:8", "register:101:1"]]
- 00bd93e8 bytes a00b0054
- 00bd93f0 ["CBRANCH", null, ["local:b29:8", "register:101:1"]]
- 00bd93f0 bytes 60080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-463e5d09ccd83e75b9de1bafa18d7fad"></a>

### [`00bd9904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md) → [`00bd99c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md) FUN_00bd99c4

採用 · 移動量 `+0xc0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd8060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd8060.md) [`00bd906c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd906c.md) [`00bd91a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd91a0.md) · 呼出先 5件 [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 3件 [`00bd8120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd8120.md) [`00bd912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd912c.md) [`00bd9260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9260.md) · 呼出先 5件 [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.76% / 新版 73.76%

CFGの説明率　旧版 51.84% / 新版 51.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9c18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9d98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd9a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bda184"
      ]
    ],
    [
      "00bd9a70",
      "DATA",
      [
        "storage",
        "002fdff8",
        "switchD_00bd99b8::switchdataD_002fdff8",
        "ushort"
      ]
    ],
    [
      "00bd9a78",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00bda184"
      ]
    ]
  ],
  "added": [
    [
      "00bd9a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda244"
      ]
    ],
    [
      "00bd9a70",
      "DATA",
      [
        "storage",
        "002fdff8",
        "switchD_00bd9a78::switchdataD_002fdff8",
        "ushort"
      ]
    ],
    [
      "00bd9a78",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00bda244"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9a18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md#insn-00bd9a18) · [`00bd9a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd9904.md#insn-00bd9a38)
- 新版 [`00bd9a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd99c4.md#insn-00bd9a38)

~~~diff
- 00bd9a18 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd9a18 ["COPY", "tmp:1:1", ["tmp:0:1"]]
- 00bd9a18 ["COPY", "tmp:2:1", ["const:0:1"]]
- 00bd9a18 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
- 00bd9a18 bytes c0314d7a
- 00bd9a38 ["CBRANCH", null, ["local:b34:8", "register:101:1"]]
- 00bd9a38 bytes a0040054
+ 00bd9a38 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 00bd9a38 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00bd9a38 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00bd9a38 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00bd9a38 bytes 5ae33f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-798c531b13c6e59efb99f91406e436b0"></a>

### [`00bda2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md) → [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) FUN_00bda388

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md) · 呼出先 10件 [`00bd84f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd8/00bd84f4.md) [`00bda7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md) [`00bda9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md) [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) · 呼出先 10件 [`00bd85b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd8/00bd85b4.md) [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.24% / 新版 76.24%

CFGの説明率　旧版 15.25% / 新版 15.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 5件, `store_destination` 2件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bda600",
      "incomplete_value": true,
      "site": "00bda600",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda540",
      "incomplete_value": true,
      "site": "00bda540",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bda604",
      "incomplete_value": true,
      "site": "00bda604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda544",
      "incomplete_value": true,
      "site": "00bda544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda54c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bda324",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda404"
      ]
    ],
    [
      "00bda40c",
      "PARAM",
      [
        "storage",
        "010a38e4",
        null,
        null
      ]
    ],
    [
      "00bda41c",
      "READ",
      [
        "storage",
        "00c248c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bda3e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda404"
      ]
    ],
    [
      "00bda40c",
      "PARAM",
      [
        "storage",
        "010a39a4",
        null,
        null
      ]
    ],
    [
      "00bda41c",
      "READ",
      [
        "storage",
        "00c24978",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda31c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md#insn-00bda31c) · [`00bda324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md#insn-00bda324) · [`00bda33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md#insn-00bda33c)
- 新版 [`00bda3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md#insn-00bda3dc) · [`00bda3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md#insn-00bda3fc)

~~~diff
- 00bda31c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00bda31c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bda31c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bda31c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00bda3dc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00bda3dc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00bda3dc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00bda3dc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00bda31c bytes e0080037
+ 00bda3dc bytes e0080037
- 00bda324 ["INT_EQUAL", "tmp:0:1", ["register:4010:8", "const:0:8"]]
- 00bda324 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bda324 bytes 020100b4
- 00bda33c ["INT_ADD", "register:40f0:8", ["const:bda33c:8", "const:4:8"]]
- 00bda33c ["CALL", null, ["callee:00bdaa74:8"]]
+ 00bda3fc ["INT_ADD", "register:40f0:8", ["const:bda3fc:8", "const:4:8"]]
+ 00bda3fc ["CALL", null, ["callee:00bdaa74:8"]]
- 00bda33c bytes 9e010094
+ 00bda3fc bytes 9e010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01fdbcaf6f14ab7b6b3d4f4e5162f2c8"></a>

### [`00bda59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda59c.md) → [`00bda65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md) FUN_00bda65c

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7cf8.md) · 呼出先 1件 [`00bda6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md)
- 新版 呼出元 1件 [`00bd7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7db8.md) · 呼出先 1件 [`00bda78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda754",
      "incomplete_value": true,
      "site": "00bda76c",
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
            "register:4098:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda760",
      "incomplete_value": true,
      "site": "00bda76c",
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
            "live",
            "register:40b0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda764",
      "incomplete_value": true,
      "site": "00bda76c",
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
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bda6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda59c.md#insn-00bda6ac) · [`00bda660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda59c.md#insn-00bda660)
- 新版 [`00bda76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md#insn-00bda76c) · [`00bda720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md#insn-00bda720)

~~~diff
- 00bda6ac ["INT_ADD", "register:40f0:8", ["const:bda6ac:8", "const:4:8"]]
- 00bda6ac ["CALL", null, ["callee:00bda78c:8"]]
+ 00bda76c ["INT_ADD", "register:40f0:8", ["const:bda76c:8", "const:4:8"]]
+ 00bda76c ["CALL", null, ["callee:00bda78c:8"]]
- 00bda6ac bytes 08000094
+ 00bda76c bytes 08000094
- 00bda660 ["BRANCH", null, ["local:b12:8"]]
+ 00bda720 ["BRANCH", null, ["local:b11:8"]]
- 00bda660 bytes 05000014
+ 00bda720 bytes 05000014
~~~


<a id="compare-2d5b0c4f596256509b18e091d59a2c71"></a>

### [`00bda6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md) → [`00bda78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) FUN_00bda78c

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bda59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda59c.md) [`00bda9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md) · 呼出先 4件 [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 2件 [`00bda65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda65c.md) [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 呼出先 4件 [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 90.28% / 新版 90.28%

CFGの説明率　旧版 57.14% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda728"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bda7e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bda7d4",
      "incomplete_value": true,
      "site": "00bda7d8",
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
      "definition_site": "00bda714",
      "incomplete_value": true,
      "site": "00bda718",
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
      "00bda7c8",
      "PARAM",
      [
        "storage",
        "002a4200",
        null,
        "string"
      ]
    ],
    [
      "00bda7cc",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bda728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda840"
      ]
    ]
  ],
  "added": [
    [
      "00bda7c8",
      "PARAM",
      [
        "storage",
        "002a41f9",
        null,
        "string"
      ]
    ],
    [
      "00bda7cc",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bda7e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda840"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md#insn-00bda718) · [`00bda728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md#insn-00bda728) · [`00bda754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md#insn-00bda754)
- 新版 [`00bda7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md#insn-00bda7d8) · [`00bda814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md#insn-00bda814)

~~~diff
- 00bda718 ["INT_ADD", "register:40f0:8", ["const:bda718:8", "const:4:8"]]
- 00bda718 ["CALL", null, ["callee:00be1f30:8"]]
+ 00bda7d8 ["INT_ADD", "register:40f0:8", ["const:bda7d8:8", "const:4:8"]]
+ 00bda7d8 ["CALL", null, ["callee:00be1f30:8"]]
- 00bda718 bytes da1d0094
+ 00bda7d8 bytes d61d0094
- 00bda728 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bda728 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bda728 bytes c1020054
- 00bda754 ["INT_ADD", "register:40f0:8", ["const:bda754:8", "const:4:8"]]
- 00bda754 ["CALL", null, ["callee:00bd9470:8"]]
+ 00bda814 ["INT_ADD", "register:40f0:8", ["const:bda814:8", "const:4:8"]]
+ 00bda814 ["CALL", null, ["callee:00bd9470:8"]]
- 00bda754 bytes 17fbff97
+ 00bda814 bytes 17fbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf76fc2e50dbd9ee92688a2e0e37df9"></a>

### [`00bda7ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md) → [`00bda8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md) FUN_00bda8ac

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bda2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md) · 呼出先 3件 [`00bd7660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd7660.md) [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bd973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd973c.md)
- 新版 呼出元 1件 [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) · 呼出先 3件 [`00bd7720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7720.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bd97fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd97fc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 47.22% / 新版 47.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bda934"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda82c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bda82c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdaa30"
      ]
    ],
    [
      "unmatched:00bda874",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bda8f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda908"
      ]
    ]
  ],
  "added": [
    [
      "00bda8ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bdaa30"
      ]
    ],
    [
      "00bda934",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00bda9b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bda908"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md#insn-00bda82c) · [`00bda874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md#insn-00bda874) · [`00bda8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda7ec.md#insn-00bda8ec)
- 新版 [`00bda9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda8ac.md#insn-00bda9ac)

~~~diff
- 00bda82c ["CBRANCH", null, ["local:b19:8", "register:102:1"]]
- 00bda82c bytes 220a0054
- 00bda874 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00bda874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bda874 bytes e80700f9
- 00bda8ec ["INT_ADD", "register:40f0:8", ["const:bda8ec:8", "const:4:8"]]
- 00bda8ec ["CALL", null, ["callee:00bd9470:8"]]
+ 00bda9ac ["INT_ADD", "register:40f0:8", ["const:bda9ac:8", "const:4:8"]]
+ 00bda9ac ["CALL", null, ["callee:00bd9470:8"]]
- 00bda8ec bytes b1faff97
+ 00bda9ac bytes b1faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31dafd9ce0d0c8e31e14becae35d3e69"></a>

### [`00bda9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md) → [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) FUN_00bdaa74

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bda2c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda2c8.md) · 呼出先 4件 [`00bd74d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd7/00bd74d0.md) [`00bd93b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd9/00bd93b0.md) [`00bda6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda6cc.md) [`00bdab1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md)
- 新版 呼出元 1件 [`00bda388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda388.md) · 呼出先 4件 [`00bd7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd7590.md) [`00bd9470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd9/00bd9470.md) [`00bda78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bda78c.md) [`00bdabdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 36.36% / 新版 34.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaa68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdab28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdaafc",
      "incomplete_value": true,
      "site": "00bdab18",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bdaa58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md#insn-00bdaa58) · [`00bdaa68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md#insn-00bdaa68) · [`00bdaab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md#insn-00bdaab4)
- 新版 [`00bdab18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md#insn-00bdab18) · [`00bdab74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md#insn-00bdab74)

~~~diff
- 00bdaa58 ["INT_ADD", "register:40f0:8", ["const:bdaa58:8", "const:4:8"]]
- 00bdaa58 ["CALL", null, ["callee:00bd9470:8"]]
+ 00bdab18 ["INT_ADD", "register:40f0:8", ["const:bdab18:8", "const:4:8"]]
+ 00bdab18 ["CALL", null, ["callee:00bd9470:8"]]
- 00bdaa58 bytes 56faff97
+ 00bdab18 bytes 56faff97
- 00bdaa68 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00bdaa68 ["CBRANCH", null, ["const:2:4", "register:102:1"]]
- 00bdaa68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bdaa68 ["COPY", "register:40d8:8", ["tmp:0:8"]]
- 00bdaa68 bytes bb22889a
- 00bdaab4 ["INT_ADD", "register:40f0:8", ["const:bdaab4:8", "const:4:8"]]
- 00bdaab4 ["CALL", null, ["callee:00bd9470:8"]]
+ 00bdab74 ["INT_ADD", "register:40f0:8", ["const:bdab74:8", "const:4:8"]]
+ 00bdab74 ["CALL", null, ["callee:00bd9470:8"]]
- 00bdaab4 bytes 3ffaff97
+ 00bdab74 bytes 3ffaff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ad743562ae5ed670db46bfd55bb578f"></a>

### [`00bdab1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md) → [`00bdabdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md) FUN_00bdabdc

採用 · 移動量 `+0xc0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bda9b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bda9b4.md) · 呼出先 4件 [`00bdd260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd260.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e80.md) [`010a58b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00bdaa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaa74.md) · 呼出先 4件 [`00bdd310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd310.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be1f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1f30.md) [`010a58b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a58b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 46.43% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdabc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bdac8c",
      "incomplete_value": true,
      "site": "00bdac90",
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
            "const:130:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdac08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdabb0",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdabb8",
      "PARAM",
      [
        "storage",
        "00299a8f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bdabc0",
      "PARAM",
      [
        "storage",
        "002a9219",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bdac70",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdac78",
      "PARAM",
      [
        "storage",
        "00299b1c",
        null,
        "string"
      ]
    ],
    [
      "00bdac80",
      "PARAM",
      [
        "storage",
        "002a9185",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdab50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md#insn-00bdab50) · [`00bdab54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md#insn-00bdab54) · [`00bdab80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md#insn-00bdab80)
- 新版 [`00bdac10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md#insn-00bdac10) · [`00bdac14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md#insn-00bdac14)

~~~diff
- 00bdab50 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 00bdac10 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00bdab50 bytes a0010054
+ 00bdac10 bytes a0010054
- 00bdab54 ["BRANCH", null, ["local:b15:8"]]
+ 00bdac14 ["BRANCH", null, ["local:b14:8"]]
- 00bdab54 bytes 14000014
+ 00bdac14 bytes 14000014
- 00bdab80 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bdab80 ["RETURN", null, ["register:0:8"]]
- 00bdab80 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2effd8f32a4890254855832e6ece5383"></a>

### [`00bdae10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdae10.md) → [`00bdaec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaec8.md) _ZnwmSt11align_val_t

採用 · 移動量 `+0xb8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1e00.md) · 呼出先 6件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdbaf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbaf0.md) [`00be1d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1d20.md)
- 新版 呼出元 1件 [`00be1eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1eb0.md) · 呼出先 6件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdbba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbba0.md) [`00be1dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1dd0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 80.56% / 新版 80.56%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdae2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdae34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bdaee4"
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
      "unmatched:00bdae94",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bdae94",
      "PARAM",
      [
        "storage",
        "00c167f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00bdae98",
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
      "00bdaf4c",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "00bdaf4c",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bdaf50",
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

- 旧版 [`00bdae2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdae10.md#insn-00bdae2c) · [`00bdae34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdae10.md#insn-00bdae34) · [`00bdae48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdae10.md#insn-00bdae48)
- 新版 [`00bdaf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaec8.md#insn-00bdaf00)

~~~diff
- 00bdae2c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdae2c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bdae2c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00bdae2c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bdae2c bytes 13849f9a
- 00bdae34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdae34 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bdae34 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00bdae34 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bdae34 bytes 3480889a
- 00bdae48 ["INT_ADD", "register:40f0:8", ["const:bdae48:8", "const:4:8"]]
- 00bdae48 ["CALL", null, ["callee:00be1ec0:8"]]
+ 00bdaf00 ["INT_ADD", "register:40f0:8", ["const:bdaf00:8", "const:4:8"]]
+ 00bdaf00 ["CALL", null, ["callee:00be1ec0:8"]]
- 00bdae48 bytes f21b0094
+ 00bdaf00 bytes f01b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

