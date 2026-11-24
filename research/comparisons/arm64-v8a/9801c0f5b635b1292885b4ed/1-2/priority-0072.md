# v16.0.0 → v16.0.1 · 最優先の変更候補 (72)

[一覧の目次](README.md)

<a id="compare-53f9e546b4ce163a6d5fec21d93cabf4"></a>

### [`00b49af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49af8.md) → [`00b49f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f20.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b49b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49f60"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b49b14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b49b0c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b49b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49f64"
      ]
    ],
    [
      "unmatched:00b49b1c",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49f34",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49f3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49f64"
      ]
    ],
    [
      "00b49f44",
      "PARAM",
      [
        "storage",
        "002a841e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49af8.md#insn-00b49b14) · [`00b49b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49af8.md#insn-00b49b30) · [`00b49b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49af8.md#insn-00b49b38)
- 新版 [`00b49f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f20.md#insn-00b49f58)

~~~diff
- 00b49b14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b49b14 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49b14 bytes 410100b5
- 00b49b30 ["INT_ADD", "register:40f0:8", ["const:b49b30:8", "const:4:8"]]
- 00b49b30 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49f58 ["INT_ADD", "register:40f0:8", ["const:b49f58:8", "const:4:8"]]
+ 00b49f58 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49b30 bytes f8430494
+ 00b49f58 bytes ee430494
- 00b49b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:610:8"]]
- 00b49b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49b38 bytes 800a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edefdffd88bea725fd42b518efa5108c"></a>

### [`00b49b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49b68.md) → [`00b49f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b49fac",
      "incomplete_value": false,
      "site": "00b49fb0",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49b84",
      "incomplete_value": false,
      "site": "00b49b88",
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
            "const:451:8"
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
      "definition_site": "00b49fbc",
      "incomplete_value": true,
      "site": "00b49fc8",
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
      "definition_site": "00b49b94",
      "incomplete_value": true,
      "site": "00b49ba0",
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
      "00b49fac",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b49fbc",
      "DATA",
      [
        "storage",
        "01125638",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49fac",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b49fbc",
      "DATA",
      [
        "storage",
        "01125a38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49b68.md#insn-00b49b88) · [`00b49b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49b68.md#insn-00b49b84) · [`00b49b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49b68.md#insn-00b49b90)
- 新版 [`00b49fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md#insn-00b49fb0) · [`00b49fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md#insn-00b49fac) · [`00b49fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49f90.md#insn-00b49fb8)

~~~diff
- 00b49b88 ["INT_ADD", "register:40f0:8", ["const:b49b88:8", "const:4:8"]]
- 00b49b88 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b49fb0 ["INT_ADD", "register:40f0:8", ["const:b49fb0:8", "const:4:8"]]
+ 00b49fb0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b49b88 bytes 1e440494
+ 00b49fb0 bytes 14440494
- 00b49b84 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b49b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49fac ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b49fac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49fac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49fac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49b84 bytes 00441191
+ 00b49fac bytes 00781491
- 00b49b90 ["COPY", "tmp:0:8", ["const:638:8"]]
- 00b49b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b49fb8 ["COPY", "tmp:0:8", ["const:a38:8"]]
+ 00b49fb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49fb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b49fb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49b90 bytes 08e11891
+ 00b49fb8 bytes 08e12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b147df54d2226c0a095c09debe238bc"></a>

### [`00b49ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ba4.md) → [`00b49fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b49ff8",
      "incomplete_value": true,
      "site": "00b49ff8",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49bd0",
      "incomplete_value": true,
      "site": "00b49bd0",
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
            "const:640:8"
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
      "definition_site": "00b49fe0",
      "incomplete_value": true,
      "site": "00b49fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49bb8",
      "incomplete_value": true,
      "site": "00b49bb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49fec",
      "incomplete_value": false,
      "site": "00b49ff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49bc4",
      "incomplete_value": false,
      "site": "00b49bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c34:8"
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
      "00b49fdc",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fec",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b49ff8",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49fdc",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fec",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b49ff8",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ba4.md#insn-00b49bc8) · [`00b49bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ba4.md#insn-00b49bd0) · [`00b49bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ba4.md#insn-00b49bb4)
- 新版 [`00b49ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md#insn-00b49ff0) · [`00b49ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md#insn-00b49ff8) · [`00b49fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b49/00b49fcc.md#insn-00b49fdc)

~~~diff
- 00b49bc8 ["INT_ADD", "register:40f0:8", ["const:b49bc8:8", "const:4:8"]]
- 00b49bc8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b49ff0 ["INT_ADD", "register:40f0:8", ["const:b49ff0:8", "const:4:8"]]
+ 00b49ff0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49bc8 bytes d2430494
+ 00b49ff0 bytes c8430494
- 00b49bd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b49bd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49ff8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b49ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49bd0 bytes 602203f9
+ 00b49ff8 bytes 602205f9
- 00b49bb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b49bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b49fdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49bb4 bytes 682243f9
+ 00b49fdc bytes 682245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e0c67cbc9aeca88a781ae01b19df9ec"></a>

### [`00b49be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49be4.md) → [`00b4a00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a038",
      "incomplete_value": true,
      "site": "00b4a038",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49c10",
      "incomplete_value": true,
      "site": "00b49c10",
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
            "const:640:8"
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
      "definition_site": "00b4a020",
      "incomplete_value": true,
      "site": "00b4a020",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49bf8",
      "incomplete_value": true,
      "site": "00b49bf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a028",
      "incomplete_value": false,
      "site": "00b4a030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49c00",
      "incomplete_value": false,
      "site": "00b49c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c34:8"
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
      "00b4a01c",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a028",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b4a038",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a01c",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a028",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a038",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49be4.md#insn-00b49c08) · [`00b49c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49be4.md#insn-00b49c10) · [`00b49bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49be4.md#insn-00b49bf4)
- 新版 [`00b4a030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md#insn-00b4a030) · [`00b4a038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md#insn-00b4a038) · [`00b4a01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a00c.md#insn-00b4a01c)

~~~diff
- 00b49c08 ["INT_ADD", "register:40f0:8", ["const:b49c08:8", "const:4:8"]]
- 00b49c08 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a030 ["INT_ADD", "register:40f0:8", ["const:b4a030:8", "const:4:8"]]
+ 00b4a030 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49c08 bytes c2430494
+ 00b4a030 bytes b8430494
- 00b49c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b49c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a038 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b4a038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49c10 bytes 602203f9
+ 00b4a038 bytes 602205f9
- 00b49bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b49bf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a01c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b4a01c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49bf4 bytes 682243f9
+ 00b4a01c bytes 682245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53fba39b079cd13c3d14da183772d6df"></a>

### [`00b49c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c24.md) → [`00b4a04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a04c.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "00b49c54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4a07c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4a060",
      "incomplete_value": true,
      "site": "00b4a060",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49c38",
      "incomplete_value": true,
      "site": "00b49c38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4a05c",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b49c44",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b49c4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b4a05c",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a06c",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a074",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c24.md#insn-00b49c38) · [`00b49c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c24.md#insn-00b49c4c) · [`00b49c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c24.md#insn-00b49c54)
- 新版 [`00b4a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a04c.md#insn-00b4a060)

~~~diff
- 00b49c38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b49c38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4a060 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4a060 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b49c38 bytes 080100b5
+ 00b4a060 bytes 080100b5
- 00b49c4c ["INT_ADD", "register:40f0:8", ["const:b49c4c:8", "const:4:8"]]
- 00b49c4c ["CALL", null, ["callee:00c5af10:8"]]
- 00b49c4c bytes b1430494
- 00b49c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b49c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49c54 bytes 602203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a6aade25f33802a49c746d1b531bfc4"></a>

### [`00b49c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c68.md) → [`00b4a090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a090.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b49c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4a0c0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4a0a4",
      "incomplete_value": true,
      "site": "00b4a0a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49c7c",
      "incomplete_value": true,
      "site": "00b49c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4a0a0",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a0a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b49c9c"
      ]
    ],
    [
      "unmatched:00b49c84",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a0a0",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a0a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4a0c4"
      ]
    ],
    [
      "00b4a0ac",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c68.md#insn-00b49c90) · [`00b49c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c68.md#insn-00b49c98) · [`00b49ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c68.md#insn-00b49ca8)
- 新版 [`00b4a0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a090.md#insn-00b4a0b8)

~~~diff
- 00b49c90 ["INT_ADD", "register:40f0:8", ["const:b49c90:8", "const:4:8"]]
- 00b49c90 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a0b8 ["INT_ADD", "register:40f0:8", ["const:b4a0b8:8", "const:4:8"]]
+ 00b4a0b8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49c90 bytes a0430494
+ 00b4a0b8 bytes 96430494
- 00b49c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b49c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49c98 bytes 602203f9
- 00b49ca8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b49ca8 ["RETURN", null, ["register:0:8"]]
- 00b49ca8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-def041c56b11ab4c0babad41411dec3c"></a>

### [`00b49cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49cb8.md) → [`00b4a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4a168",
      "incomplete_value": true,
      "site": "00b4a168",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d40",
      "incomplete_value": true,
      "site": "00b49d40",
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
            "const:648:8"
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
      "definition_site": "00b4a114",
      "incomplete_value": true,
      "site": "00b4a120",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49cec",
      "incomplete_value": true,
      "site": "00b49cf8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:640:8"
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
      "00b4a0f4",
      "READ",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b49cec",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a168",
      "WRITE",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a0f4",
      "READ",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a114",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a168",
      "WRITE",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49cb8.md#insn-00b49cf8) · [`00b49d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49cb8.md#insn-00b49d40) · [`00b49ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49cb8.md#insn-00b49ccc)
- 新版 [`00b4a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md#insn-00b4a120) · [`00b4a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md#insn-00b4a168) · [`00b4a0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a0e0.md#insn-00b4a0f4)

~~~diff
- 00b49cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49cf8 ["INT_ADD", "register:40f0:8", ["const:b49cf8:8", "const:4:8"]]
- 00b49cf8 ["CALLIND", null, ["register:0:8"]]
+ 00b4a120 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a120 ["INT_ADD", "register:40f0:8", ["const:b4a120:8", "const:4:8"]]
+ 00b4a120 ["CALLIND", null, ["register:0:8"]]
- 00b49cf8 bytes 00013fd6
+ 00b4a120 bytes 00013fd6
- 00b49d40 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49d40 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
- 00b49d40 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a168 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a168 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a48:8"]]
+ 00b4a168 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49d40 bytes a0221939
+ 00b4a168 bytes a0222939
- 00b49ccc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
- 00b49ccc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b49ccc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4a0f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a48:8"]]
+ 00b4a0f4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a0f4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b49ccc bytes a8225939
+ 00b4a0f4 bytes a8226939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0873a70a343578516217880ff8dd11c"></a>

### [`00b49d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49d54.md) → [`00b4a17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a1b8",
      "incomplete_value": true,
      "site": "00b4a1b8",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d90",
      "incomplete_value": true,
      "site": "00b49d90",
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
            "const:648:8"
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
      "definition_site": "00b4a208",
      "incomplete_value": true,
      "site": "00b4a208",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49de0",
      "incomplete_value": true,
      "site": "00b49de0",
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
            "const:640:8"
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
      "definition_site": "00b4a194",
      "incomplete_value": true,
      "site": "00b4a194",
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
      "definition_site": "00b49d6c",
      "incomplete_value": true,
      "site": "00b49d6c",
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
      "00b4a190",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a19c",
      "READ",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a1b8",
      "WRITE",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a190",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a19c",
      "READ",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a1b8",
      "WRITE",
      [
        "storage",
        "01125a48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49d54.md#insn-00b49d90) · [`00b49ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49d54.md#insn-00b49ddc) · [`00b49de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49d54.md#insn-00b49de0)
- 新版 [`00b4a1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md#insn-00b4a1b8) · [`00b4a204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md#insn-00b4a204) · [`00b4a208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a17c.md#insn-00b4a208)

~~~diff
- 00b49d90 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49d90 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49d90 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
- 00b49d90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a1b8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a1b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a1b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a48:8"]]
+ 00b4a1b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49d90 bytes bf221939
+ 00b4a1b8 bytes bf222939
- 00b49ddc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49ddc ["INT_ADD", "register:40f0:8", ["const:b49ddc:8", "const:4:8"]]
- 00b49ddc ["CALLIND", null, ["register:0:8"]]
+ 00b4a204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a204 ["INT_ADD", "register:40f0:8", ["const:b4a204:8", "const:4:8"]]
+ 00b4a204 ["CALLIND", null, ["register:0:8"]]
- 00b49ddc bytes 00013fd6
+ 00b4a204 bytes 00013fd6
- 00b49de0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b49de0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b49de0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a208 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b49de0 bytes 9f2203f9
+ 00b4a208 bytes 9f2205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7d3b8f0adde602c329ff43665f63ab6"></a>

### [`00b49df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49df4.md) → [`00b4a21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4a25c",
      "incomplete_value": true,
      "site": "00b4a25c",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49e34",
      "incomplete_value": true,
      "site": "00b49e34",
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
            "const:640:8"
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
      "definition_site": "00b4a238",
      "incomplete_value": true,
      "site": "00b4a238",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49e10",
      "incomplete_value": true,
      "site": "00b49e10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a240",
      "incomplete_value": false,
      "site": "00b4a254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49e18",
      "incomplete_value": false,
      "site": "00b49e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c34:8"
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
      "00b4a230",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a240",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b4a25c",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a230",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a240",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a25c",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49df4.md#insn-00b49e2c) · [`00b49e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49df4.md#insn-00b49e34) · [`00b49e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49df4.md#insn-00b49e08)
- 新版 [`00b4a254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md#insn-00b4a254) · [`00b4a25c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md#insn-00b4a25c) · [`00b4a230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a21c.md#insn-00b4a230)

~~~diff
- 00b49e2c ["INT_ADD", "register:40f0:8", ["const:b49e2c:8", "const:4:8"]]
- 00b49e2c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a254 ["INT_ADD", "register:40f0:8", ["const:b4a254:8", "const:4:8"]]
+ 00b4a254 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49e2c bytes 39430494
+ 00b4a254 bytes 2f430494
- 00b49e34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b49e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a25c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a25c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49e34 bytes 802203f9
+ 00b4a25c bytes 802205f9
- 00b49e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b49e08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a230 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49e08 bytes 812243f9
+ 00b4a230 bytes 812245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9830408e5171772db6cf32f246aecf0d"></a>

### [`00b49e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49e64.md) → [`00b4a28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ae90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae90.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b290.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4a2a8",
      "incomplete_value": false,
      "site": "00b4a2ac",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49e80",
      "incomplete_value": false,
      "site": "00b49e84",
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
            "const:29a:8"
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
      "definition_site": "00b4a2b8",
      "incomplete_value": true,
      "site": "00b4a2c4",
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
      "definition_site": "00b49e90",
      "incomplete_value": true,
      "site": "00b49e9c",
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
      "00b4a2a8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4a2b8",
      "DATA",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a2a8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4a2b8",
      "DATA",
      [
        "storage",
        "01125a50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49e64.md#insn-00b49e84) · [`00b49e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49e64.md#insn-00b49e80) · [`00b49e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49e64.md#insn-00b49e8c)
- 新版 [`00b4a2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md#insn-00b4a2ac) · [`00b4a2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md#insn-00b4a2a8) · [`00b4a2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a28c.md#insn-00b4a2b4)

~~~diff
- 00b49e84 ["INT_ADD", "register:40f0:8", ["const:b49e84:8", "const:4:8"]]
- 00b49e84 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4a2ac ["INT_ADD", "register:40f0:8", ["const:b4a2ac:8", "const:4:8"]]
+ 00b4a2ac ["CALL", null, ["callee:00c5b000:8"]]
- 00b49e84 bytes 5f430494
+ 00b4a2ac bytes 55430494
- 00b49e80 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b49e80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49e80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49e80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a2a8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4a2a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a2a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a2a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49e80 bytes 00680a91
+ 00b4a2a8 bytes 009c0d91
- 00b49e8c ["COPY", "tmp:0:8", ["const:650:8"]]
- 00b49e8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49e8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49e8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a2b4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00b4a2b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a2b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a2b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49e8c bytes 08411991
+ 00b4a2b4 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95434d6e32c4434ed13dd7e122ae7ead"></a>

### [`00b49ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ea0.md) → [`00b4a2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a308",
      "incomplete_value": true,
      "site": "00b4a308",
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
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ee0",
      "incomplete_value": true,
      "site": "00b49ee0",
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
            "const:640:8"
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
      "definition_site": "00b4a2e4",
      "incomplete_value": true,
      "site": "00b4a2e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49ebc",
      "incomplete_value": true,
      "site": "00b49ebc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a2ec",
      "incomplete_value": false,
      "site": "00b4a300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ec4",
      "incomplete_value": false,
      "site": "00b49ed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:c34:8"
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
      "00b4a2dc",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a2ec",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b4a308",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a2dc",
      "READ",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a2ec",
      "PARAM",
      [
        "storage",
        "002b7c74",
        null,
        "string"
      ]
    ],
    [
      "00b4a308",
      "WRITE",
      [
        "storage",
        "01125a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ea0.md#insn-00b49ed8) · [`00b49ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ea0.md#insn-00b49ee0) · [`00b49eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ea0.md#insn-00b49eb4)
- 新版 [`00b4a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md#insn-00b4a300) · [`00b4a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md#insn-00b4a308) · [`00b4a2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a2c8.md#insn-00b4a2dc)

~~~diff
- 00b49ed8 ["INT_ADD", "register:40f0:8", ["const:b49ed8:8", "const:4:8"]]
- 00b49ed8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a300 ["INT_ADD", "register:40f0:8", ["const:b4a300:8", "const:4:8"]]
+ 00b4a300 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49ed8 bytes 0e430494
+ 00b4a300 bytes 04430494
- 00b49ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b49ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49ee0 bytes 802203f9
+ 00b4a308 bytes 802205f9
- 00b49eb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b49eb4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a2dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a2dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49eb4 bytes 812243f9
+ 00b4a2dc bytes 812245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1964d2d293f80cbdf804026a2b4511f"></a>

### [`00b49f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f10.md) → [`00b4a338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4a354",
      "incomplete_value": false,
      "site": "00b4a358",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f2c",
      "incomplete_value": false,
      "site": "00b49f30",
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
            "const:451:8"
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
      "definition_site": "00b4a364",
      "incomplete_value": true,
      "site": "00b4a370",
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
      "definition_site": "00b49f3c",
      "incomplete_value": true,
      "site": "00b49f48",
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
      "00b4a354",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4a364",
      "DATA",
      [
        "storage",
        "01125660",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a354",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4a364",
      "DATA",
      [
        "storage",
        "01125a60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f10.md#insn-00b49f30) · [`00b49f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f10.md#insn-00b49f2c) · [`00b49f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f10.md#insn-00b49f38)
- 新版 [`00b4a358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md#insn-00b4a358) · [`00b4a354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md#insn-00b4a354) · [`00b4a360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a338.md#insn-00b4a360)

~~~diff
- 00b49f30 ["INT_ADD", "register:40f0:8", ["const:b49f30:8", "const:4:8"]]
- 00b49f30 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4a358 ["INT_ADD", "register:40f0:8", ["const:b4a358:8", "const:4:8"]]
+ 00b4a358 ["CALL", null, ["callee:00c5b000:8"]]
- 00b49f30 bytes 34430494
+ 00b4a358 bytes 2a430494
- 00b49f2c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b49f2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49f2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49f2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a354 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4a354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49f2c bytes 00441191
+ 00b4a354 bytes 00781491
- 00b49f38 ["COPY", "tmp:0:8", ["const:660:8"]]
- 00b49f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b49f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b49f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a360 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00b4a360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b49f38 bytes 08811991
+ 00b4a360 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d28c0e002508c0acd7935091f8961650"></a>

### [`00b49f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f4c.md) → [`00b4a374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a3a0",
      "incomplete_value": true,
      "site": "00b4a3a0",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f78",
      "incomplete_value": true,
      "site": "00b49f78",
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
            "const:668:8"
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
      "definition_site": "00b4a388",
      "incomplete_value": true,
      "site": "00b4a388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49f60",
      "incomplete_value": true,
      "site": "00b49f60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a394",
      "incomplete_value": false,
      "site": "00b4a398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f6c",
      "incomplete_value": false,
      "site": "00b49f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
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
      "00b4a384",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a394",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a3a0",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a384",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a394",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a3a0",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f4c.md#insn-00b49f70) · [`00b49f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f4c.md#insn-00b49f78) · [`00b49f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f4c.md#insn-00b49f5c)
- 新版 [`00b4a398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md#insn-00b4a398) · [`00b4a3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md#insn-00b4a3a0) · [`00b4a384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a374.md#insn-00b4a384)

~~~diff
- 00b49f70 ["INT_ADD", "register:40f0:8", ["const:b49f70:8", "const:4:8"]]
- 00b49f70 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a398 ["INT_ADD", "register:40f0:8", ["const:b4a398:8", "const:4:8"]]
+ 00b4a398 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49f70 bytes e8420494
+ 00b4a398 bytes de420494
- 00b49f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b49f78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a3a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a3a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49f78 bytes 603603f9
+ 00b4a3a0 bytes 603605f9
- 00b49f5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b49f5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a384 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a384 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49f5c bytes 683643f9
+ 00b4a384 bytes 683645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a9c60089f1a6437abd248fb8237c1b"></a>

### [`00b49f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f8c.md) → [`00b4a3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a3e0",
      "incomplete_value": true,
      "site": "00b4a3e0",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49fb8",
      "incomplete_value": true,
      "site": "00b49fb8",
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
            "const:668:8"
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
      "definition_site": "00b4a3c8",
      "incomplete_value": true,
      "site": "00b4a3c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49fa0",
      "incomplete_value": true,
      "site": "00b49fa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a3d0",
      "incomplete_value": false,
      "site": "00b4a3d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49fa8",
      "incomplete_value": false,
      "site": "00b49fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
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
      "00b4a3c4",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a3d0",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a3e0",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a3c4",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a3d0",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a3e0",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f8c.md#insn-00b49fb0) · [`00b49fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f8c.md#insn-00b49fb8) · [`00b49f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f8c.md#insn-00b49f9c)
- 新版 [`00b4a3d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md#insn-00b4a3d8) · [`00b4a3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md#insn-00b4a3e0) · [`00b4a3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3b4.md#insn-00b4a3c4)

~~~diff
- 00b49fb0 ["INT_ADD", "register:40f0:8", ["const:b49fb0:8", "const:4:8"]]
- 00b49fb0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a3d8 ["INT_ADD", "register:40f0:8", ["const:b4a3d8:8", "const:4:8"]]
+ 00b4a3d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b49fb0 bytes d8420494
+ 00b4a3d8 bytes ce420494
- 00b49fb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b49fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a3e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49fb8 bytes 603603f9
+ 00b4a3e0 bytes 603605f9
- 00b49f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b49f9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a3c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a3c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49f9c bytes 683643f9
+ 00b4a3c4 bytes 683645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3970a0d7a4e4fc714aa6c8a49cb08c3"></a>

### [`00b49fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49fcc.md) → [`00b4a3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a424",
      "incomplete_value": true,
      "site": "00b4a424",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ffc",
      "incomplete_value": true,
      "site": "00b49ffc",
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
            "const:668:8"
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
      "definition_site": "00b4a408",
      "incomplete_value": true,
      "site": "00b4a408",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b49fe0",
      "incomplete_value": true,
      "site": "00b49fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a414",
      "incomplete_value": false,
      "site": "00b4a41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49fec",
      "incomplete_value": false,
      "site": "00b49ff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
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
      "00b4a404",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a414",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a424",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a404",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a414",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a424",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49fcc.md#insn-00b49ff4) · [`00b49ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49fcc.md#insn-00b49ffc) · [`00b49fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49fcc.md#insn-00b49fdc)
- 新版 [`00b4a41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md#insn-00b4a41c) · [`00b4a424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md#insn-00b4a424) · [`00b4a404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a3f4.md#insn-00b4a404)

~~~diff
- 00b49ff4 ["INT_ADD", "register:40f0:8", ["const:b49ff4:8", "const:4:8"]]
- 00b49ff4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a41c ["INT_ADD", "register:40f0:8", ["const:b4a41c:8", "const:4:8"]]
+ 00b4a41c ["CALL", null, ["callee:00c5af10:8"]]
- 00b49ff4 bytes c7420494
+ 00b4a41c bytes bd420494
- 00b49ffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b49ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49ffc bytes 603603f9
+ 00b4a424 bytes 603605f9
- 00b49fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b49fdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b49fdc bytes 683643f9
+ 00b4a404 bytes 683645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85f0372d9e3cc2faa315fbce1902983c"></a>

### [`00b4a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a010.md) → [`00b4a438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a468",
      "incomplete_value": true,
      "site": "00b4a468",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a040",
      "incomplete_value": true,
      "site": "00b4a040",
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
            "const:668:8"
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
      "definition_site": "00b4a44c",
      "incomplete_value": true,
      "site": "00b4a44c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a024",
      "incomplete_value": true,
      "site": "00b4a024",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a454",
      "incomplete_value": false,
      "site": "00b4a460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a02c",
      "incomplete_value": false,
      "site": "00b4a038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
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
      "00b4a448",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a454",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a468",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a448",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a454",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a468",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a010.md#insn-00b4a038) · [`00b4a040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a010.md#insn-00b4a040) · [`00b4a020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a010.md#insn-00b4a020)
- 新版 [`00b4a460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md#insn-00b4a460) · [`00b4a468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md#insn-00b4a468) · [`00b4a448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a438.md#insn-00b4a448)

~~~diff
- 00b4a038 ["INT_ADD", "register:40f0:8", ["const:b4a038:8", "const:4:8"]]
- 00b4a038 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a460 ["INT_ADD", "register:40f0:8", ["const:b4a460:8", "const:4:8"]]
+ 00b4a460 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a038 bytes b6420494
+ 00b4a460 bytes ac420494
- 00b4a040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b4a040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a040 bytes 603603f9
+ 00b4a468 bytes 603605f9
- 00b4a020 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
- 00b4a020 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a448 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a020 bytes 683643f9
+ 00b4a448 bytes 683645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4afe24ef34366e5e90b58489ae9da0f9"></a>

### [`00b4a060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md) → [`00b4a488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a510",
      "incomplete_value": true,
      "site": "00b4a510",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0e8",
      "incomplete_value": true,
      "site": "00b4a0e8",
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
            "const:670:8"
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
      "definition_site": "00b4a4bc",
      "incomplete_value": true,
      "site": "00b4a4c8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a094",
      "incomplete_value": true,
      "site": "00b4a0a0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:668:8"
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
      "00b4a49c",
      "READ",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a4bc",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a510",
      "WRITE",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a49c",
      "READ",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a4bc",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a510",
      "WRITE",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md#insn-00b4a0a0) · [`00b4a0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md#insn-00b4a0e8) · [`00b4a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md#insn-00b4a074)
- 新版 [`00b4a4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md#insn-00b4a4c8) · [`00b4a510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md#insn-00b4a510) · [`00b4a49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a488.md#insn-00b4a49c)

~~~diff
- 00b4a0a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a0a0 ["INT_ADD", "register:40f0:8", ["const:b4a0a0:8", "const:4:8"]]
- 00b4a0a0 ["CALLIND", null, ["register:0:8"]]
+ 00b4a4c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a4c8 ["INT_ADD", "register:40f0:8", ["const:b4a4c8:8", "const:4:8"]]
+ 00b4a4c8 ["CALLIND", null, ["register:0:8"]]
- 00b4a0a0 bytes 00013fd6
+ 00b4a4c8 bytes 00013fd6
- 00b4a0e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a0e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:670:8"]]
- 00b4a0e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a510 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a510 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a70:8"]]
+ 00b4a510 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a0e8 bytes a0c21939
+ 00b4a510 bytes a0c22939
- 00b4a074 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:670:8"]]
- 00b4a074 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4a074 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4a49c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
+ 00b4a49c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a49c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4a074 bytes a8c25939
+ 00b4a49c bytes a8c26939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4907de1ed349f2f9108cfb389f495af8"></a>

### [`00b4a0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a0fc.md) → [`00b4a524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a560",
      "incomplete_value": true,
      "site": "00b4a560",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a138",
      "incomplete_value": true,
      "site": "00b4a138",
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
            "const:670:8"
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
      "definition_site": "00b4a5b0",
      "incomplete_value": true,
      "site": "00b4a5b0",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a188",
      "incomplete_value": true,
      "site": "00b4a188",
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
            "const:668:8"
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
      "definition_site": "00b4a53c",
      "incomplete_value": true,
      "site": "00b4a53c",
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
      "definition_site": "00b4a114",
      "incomplete_value": true,
      "site": "00b4a114",
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
      "00b4a538",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a544",
      "READ",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a560",
      "WRITE",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a538",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a544",
      "READ",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a560",
      "WRITE",
      [
        "storage",
        "01125a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a0fc.md#insn-00b4a138) · [`00b4a184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a0fc.md#insn-00b4a184) · [`00b4a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a0fc.md#insn-00b4a188)
- 新版 [`00b4a560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md#insn-00b4a560) · [`00b4a5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md#insn-00b4a5ac) · [`00b4a5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a524.md#insn-00b4a5b0)

~~~diff
- 00b4a138 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a138 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a138 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:670:8"]]
- 00b4a138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a560 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a560 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a560 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a70:8"]]
+ 00b4a560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a138 bytes bfc21939
+ 00b4a560 bytes bfc22939
- 00b4a184 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a184 ["INT_ADD", "register:40f0:8", ["const:b4a184:8", "const:4:8"]]
- 00b4a184 ["CALLIND", null, ["register:0:8"]]
+ 00b4a5ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a5ac ["INT_ADD", "register:40f0:8", ["const:b4a5ac:8", "const:4:8"]]
+ 00b4a5ac ["CALLIND", null, ["register:0:8"]]
- 00b4a184 bytes 00013fd6
+ 00b4a5ac bytes 00013fd6
- 00b4a188 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b4a188 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a5b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a5b0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a5b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a188 bytes 9f3603f9
+ 00b4a5b0 bytes 9f3605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb531e843813775fc1c3a25897b2c5b3"></a>

### [`00b4a19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a19c.md) → [`00b4a5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4a604",
      "incomplete_value": true,
      "site": "00b4a604",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a1dc",
      "incomplete_value": true,
      "site": "00b4a1dc",
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
            "const:668:8"
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
      "definition_site": "00b4a5e0",
      "incomplete_value": true,
      "site": "00b4a5e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a1b8",
      "incomplete_value": true,
      "site": "00b4a1b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a5e8",
      "incomplete_value": false,
      "site": "00b4a5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a1c0",
      "incomplete_value": false,
      "site": "00b4a1d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
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
      "00b4a5d8",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5e8",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a604",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a5d8",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5e8",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a604",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a19c.md#insn-00b4a1d4) · [`00b4a1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a19c.md#insn-00b4a1dc) · [`00b4a1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a19c.md#insn-00b4a1b0)
- 新版 [`00b4a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md#insn-00b4a5fc) · [`00b4a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md#insn-00b4a604) · [`00b4a5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a5c4.md#insn-00b4a5d8)

~~~diff
- 00b4a1d4 ["INT_ADD", "register:40f0:8", ["const:b4a1d4:8", "const:4:8"]]
- 00b4a1d4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a5fc ["INT_ADD", "register:40f0:8", ["const:b4a5fc:8", "const:4:8"]]
+ 00b4a5fc ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a1d4 bytes 4f420494
+ 00b4a5fc bytes 45420494
- 00b4a1dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b4a1dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a1dc bytes 803603f9
+ 00b4a604 bytes 803605f9
- 00b4a1b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b4a1b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a5d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a5d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a1b0 bytes 813643f9
+ 00b4a5d8 bytes 813645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54d67e3bc3b0eeae9957742b96685cd6"></a>

### [`00b4a20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a20c.md) → [`00b4a634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4a650",
      "incomplete_value": false,
      "site": "00b4a654",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a228",
      "incomplete_value": false,
      "site": "00b4a22c",
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
            "const:29a:8"
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
      "definition_site": "00b4a660",
      "incomplete_value": true,
      "site": "00b4a66c",
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
      "definition_site": "00b4a238",
      "incomplete_value": true,
      "site": "00b4a244",
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
      "00b4a650",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4a660",
      "DATA",
      [
        "storage",
        "01125678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a650",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4a660",
      "DATA",
      [
        "storage",
        "01125a78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a20c.md#insn-00b4a22c) · [`00b4a228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a20c.md#insn-00b4a228) · [`00b4a234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a20c.md#insn-00b4a234)
- 新版 [`00b4a654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md#insn-00b4a654) · [`00b4a650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md#insn-00b4a650) · [`00b4a65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a634.md#insn-00b4a65c)

~~~diff
- 00b4a22c ["INT_ADD", "register:40f0:8", ["const:b4a22c:8", "const:4:8"]]
- 00b4a22c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4a654 ["INT_ADD", "register:40f0:8", ["const:b4a654:8", "const:4:8"]]
+ 00b4a654 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4a22c bytes 75420494
+ 00b4a654 bytes 6b420494
- 00b4a228 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4a228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a650 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4a650 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a650 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a650 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a228 bytes 00680a91
+ 00b4a650 bytes 009c0d91
- 00b4a234 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00b4a234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a65c ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00b4a65c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a65c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a65c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a234 bytes 08e11991
+ 00b4a65c bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c39e6948921d3f0a54f1e231042567b"></a>

### [`00b4a248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a248.md) → [`00b4a670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a6b0",
      "incomplete_value": true,
      "site": "00b4a6b0",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a288",
      "incomplete_value": true,
      "site": "00b4a288",
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
            "const:668:8"
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
      "definition_site": "00b4a68c",
      "incomplete_value": true,
      "site": "00b4a68c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a264",
      "incomplete_value": true,
      "site": "00b4a264",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a694",
      "incomplete_value": false,
      "site": "00b4a6a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a26c",
      "incomplete_value": false,
      "site": "00b4a280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
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
      "00b4a684",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a694",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a6b0",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a684",
      "READ",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a694",
      "PARAM",
      [
        "storage",
        "002c1b11",
        null,
        "string"
      ]
    ],
    [
      "00b4a6b0",
      "WRITE",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a248.md#insn-00b4a280) · [`00b4a288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a248.md#insn-00b4a288) · [`00b4a25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a248.md#insn-00b4a25c)
- 新版 [`00b4a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md#insn-00b4a6a8) · [`00b4a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md#insn-00b4a6b0) · [`00b4a684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a670.md#insn-00b4a684)

~~~diff
- 00b4a280 ["INT_ADD", "register:40f0:8", ["const:b4a280:8", "const:4:8"]]
- 00b4a280 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a6a8 ["INT_ADD", "register:40f0:8", ["const:b4a6a8:8", "const:4:8"]]
+ 00b4a6a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a280 bytes 24420494
+ 00b4a6a8 bytes 1a420494
- 00b4a288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b4a288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a6b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a6b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a288 bytes 803603f9
+ 00b4a6b0 bytes 803605f9
- 00b4a25c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
- 00b4a25c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a684 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a684 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a25c bytes 813643f9
+ 00b4a684 bytes 813645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-233bb4ea4fd5de2d0c207180a5880ceb"></a>

### [`00b4a2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2b8.md) → [`00b4a6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4a6fc",
      "incomplete_value": false,
      "site": "00b4a700",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a2d4",
      "incomplete_value": false,
      "site": "00b4a2d8",
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
            "const:451:8"
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
      "definition_site": "00b4a70c",
      "incomplete_value": true,
      "site": "00b4a718",
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
      "definition_site": "00b4a2e4",
      "incomplete_value": true,
      "site": "00b4a2f0",
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
      "00b4a6fc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4a70c",
      "DATA",
      [
        "storage",
        "01125688",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a6fc",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4a70c",
      "DATA",
      [
        "storage",
        "01125a88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2b8.md#insn-00b4a2d8) · [`00b4a2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2b8.md#insn-00b4a2d4) · [`00b4a2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2b8.md#insn-00b4a2e0)
- 新版 [`00b4a700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md#insn-00b4a700) · [`00b4a6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md#insn-00b4a6fc) · [`00b4a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a6e0.md#insn-00b4a708)

~~~diff
- 00b4a2d8 ["INT_ADD", "register:40f0:8", ["const:b4a2d8:8", "const:4:8"]]
- 00b4a2d8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4a700 ["INT_ADD", "register:40f0:8", ["const:b4a700:8", "const:4:8"]]
+ 00b4a700 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4a2d8 bytes 4a420494
+ 00b4a700 bytes 40420494
- 00b4a2d4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4a2d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a2d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a2d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a6fc ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4a6fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a6fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a6fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a2d4 bytes 00441191
+ 00b4a6fc bytes 00781491
- 00b4a2e0 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00b4a2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4a708 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00b4a708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4a708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a2e0 bytes 08211a91
+ 00b4a708 bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c6011698733a152ba16c8bbbac2e2e5"></a>

### [`00b4a2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2f4.md) → [`00b4a71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a748",
      "incomplete_value": true,
      "site": "00b4a748",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a320",
      "incomplete_value": true,
      "site": "00b4a320",
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
            "const:690:8"
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
      "definition_site": "00b4a730",
      "incomplete_value": true,
      "site": "00b4a730",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a308",
      "incomplete_value": true,
      "site": "00b4a308",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a73c",
      "incomplete_value": false,
      "site": "00b4a740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a314",
      "incomplete_value": false,
      "site": "00b4a318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c36:8"
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
      "00b4a72c",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a73c",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a748",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a72c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a73c",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a748",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2f4.md#insn-00b4a318) · [`00b4a320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2f4.md#insn-00b4a320) · [`00b4a304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2f4.md#insn-00b4a304)
- 新版 [`00b4a740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md#insn-00b4a740) · [`00b4a748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md#insn-00b4a748) · [`00b4a72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a71c.md#insn-00b4a72c)

~~~diff
- 00b4a318 ["INT_ADD", "register:40f0:8", ["const:b4a318:8", "const:4:8"]]
- 00b4a318 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a740 ["INT_ADD", "register:40f0:8", ["const:b4a740:8", "const:4:8"]]
+ 00b4a740 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a318 bytes fe410494
+ 00b4a740 bytes f4410494
- 00b4a320 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a320 bytes 604a03f9
+ 00b4a748 bytes 604a05f9
- 00b4a304 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a304 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a72c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a72c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a304 bytes 684a43f9
+ 00b4a72c bytes 684a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd5c3063a61d32757004c7d609dc2cf8"></a>

### [`00b4a334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a334.md) → [`00b4a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a788",
      "incomplete_value": true,
      "site": "00b4a788",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a360",
      "incomplete_value": true,
      "site": "00b4a360",
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
            "const:690:8"
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
      "definition_site": "00b4a770",
      "incomplete_value": true,
      "site": "00b4a770",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a348",
      "incomplete_value": true,
      "site": "00b4a348",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a778",
      "incomplete_value": false,
      "site": "00b4a780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a350",
      "incomplete_value": false,
      "site": "00b4a358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c36:8"
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
      "00b4a76c",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a778",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a788",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a76c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a778",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a788",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a334.md#insn-00b4a358) · [`00b4a360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a334.md#insn-00b4a360) · [`00b4a344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a334.md#insn-00b4a344)
- 新版 [`00b4a780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md#insn-00b4a780) · [`00b4a788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md#insn-00b4a788) · [`00b4a76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a75c.md#insn-00b4a76c)

~~~diff
- 00b4a358 ["INT_ADD", "register:40f0:8", ["const:b4a358:8", "const:4:8"]]
- 00b4a358 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a780 ["INT_ADD", "register:40f0:8", ["const:b4a780:8", "const:4:8"]]
+ 00b4a780 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a358 bytes ee410494
+ 00b4a780 bytes e4410494
- 00b4a360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a360 bytes 604a03f9
+ 00b4a788 bytes 604a05f9
- 00b4a344 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a344 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a76c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a76c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a344 bytes 684a43f9
+ 00b4a76c bytes 684a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe2791d0906e7489a505d6b67fbca58"></a>

### [`00b4a374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a374.md) → [`00b4a79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a7cc",
      "incomplete_value": true,
      "site": "00b4a7cc",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3a4",
      "incomplete_value": true,
      "site": "00b4a3a4",
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
            "const:690:8"
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
      "definition_site": "00b4a7b0",
      "incomplete_value": true,
      "site": "00b4a7b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a388",
      "incomplete_value": true,
      "site": "00b4a388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a7bc",
      "incomplete_value": false,
      "site": "00b4a7c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a394",
      "incomplete_value": false,
      "site": "00b4a39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c36:8"
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
      "00b4a7ac",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7bc",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a7cc",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a7ac",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7bc",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a7cc",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a374.md#insn-00b4a39c) · [`00b4a3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a374.md#insn-00b4a3a4) · [`00b4a384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a374.md#insn-00b4a384)
- 新版 [`00b4a7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md#insn-00b4a7c4) · [`00b4a7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md#insn-00b4a7cc) · [`00b4a7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a79c.md#insn-00b4a7ac)

~~~diff
- 00b4a39c ["INT_ADD", "register:40f0:8", ["const:b4a39c:8", "const:4:8"]]
- 00b4a39c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a7c4 ["INT_ADD", "register:40f0:8", ["const:b4a7c4:8", "const:4:8"]]
+ 00b4a7c4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a39c bytes dd410494
+ 00b4a7c4 bytes d3410494
- 00b4a3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a7cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a3a4 bytes 604a03f9
+ 00b4a7cc bytes 604a05f9
- 00b4a384 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a384 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a7ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a7ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a384 bytes 684a43f9
+ 00b4a7ac bytes 684a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17fbbdce0f87370db567313502345699"></a>

### [`00b4a3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a3b8.md) → [`00b4a7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4a810",
      "incomplete_value": true,
      "site": "00b4a810",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3e8",
      "incomplete_value": true,
      "site": "00b4a3e8",
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
            "const:690:8"
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
      "definition_site": "00b4a7f4",
      "incomplete_value": true,
      "site": "00b4a7f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a3cc",
      "incomplete_value": true,
      "site": "00b4a3cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a7fc",
      "incomplete_value": false,
      "site": "00b4a808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3d4",
      "incomplete_value": false,
      "site": "00b4a3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c36:8"
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
      "00b4a7f0",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7fc",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a810",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a7f0",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7fc",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a810",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a3b8.md#insn-00b4a3e0) · [`00b4a3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a3b8.md#insn-00b4a3e8) · [`00b4a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a3b8.md#insn-00b4a3c8)
- 新版 [`00b4a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md#insn-00b4a808) · [`00b4a810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md#insn-00b4a810) · [`00b4a7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a7e0.md#insn-00b4a7f0)

~~~diff
- 00b4a3e0 ["INT_ADD", "register:40f0:8", ["const:b4a3e0:8", "const:4:8"]]
- 00b4a3e0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a808 ["INT_ADD", "register:40f0:8", ["const:b4a808:8", "const:4:8"]]
+ 00b4a808 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a3e0 bytes cc410494
+ 00b4a808 bytes c2410494
- 00b4a3e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a3e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a3e8 bytes 604a03f9
+ 00b4a810 bytes 604a05f9
- 00b4a3c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
- 00b4a3c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a7f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a90:8"]]
+ 00b4a7f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a3c8 bytes 684a43f9
+ 00b4a7f0 bytes 684a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd5378ee1ec674beb76798bb40952fe0"></a>

### [`00b4a408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a408.md) → [`00b4a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md) _ZN8firebase4util4file15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a8b8",
      "incomplete_value": true,
      "site": "00b4a8b8",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a490",
      "incomplete_value": true,
      "site": "00b4a490",
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
            "const:698:8"
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
      "definition_site": "00b4a864",
      "incomplete_value": true,
      "site": "00b4a870",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a43c",
      "incomplete_value": true,
      "site": "00b4a448",
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
                "const:1125000:8"
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
      "00b4a844",
      "READ",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a864",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a8b8",
      "WRITE",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a844",
      "READ",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a864",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a8b8",
      "WRITE",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a408.md#insn-00b4a448) · [`00b4a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a408.md#insn-00b4a490) · [`00b4a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a408.md#insn-00b4a41c)
- 新版 [`00b4a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md#insn-00b4a870) · [`00b4a8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md#insn-00b4a8b8) · [`00b4a844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a830.md#insn-00b4a844)

~~~diff
- 00b4a448 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a448 ["INT_ADD", "register:40f0:8", ["const:b4a448:8", "const:4:8"]]
- 00b4a448 ["CALLIND", null, ["register:0:8"]]
+ 00b4a870 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a870 ["INT_ADD", "register:40f0:8", ["const:b4a870:8", "const:4:8"]]
+ 00b4a870 ["CALLIND", null, ["register:0:8"]]
- 00b4a448 bytes 00013fd6
+ 00b4a870 bytes 00013fd6
- 00b4a490 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a490 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:698:8"]]
- 00b4a490 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a8b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a8b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a98:8"]]
+ 00b4a8b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a490 bytes a0621a39
+ 00b4a8b8 bytes a0622a39
- 00b4a41c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:698:8"]]
- 00b4a41c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4a41c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4a844 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a98:8"]]
+ 00b4a844 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a844 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4a41c bytes a8625a39
+ 00b4a844 bytes a8626a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b4d8c72c1ee50fa824fe194f4e0d4b"></a>

### [`00b4a4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a4a4.md) → [`00b4a8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md) _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a908",
      "incomplete_value": true,
      "site": "00b4a908",
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
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4e0",
      "incomplete_value": true,
      "site": "00b4a4e0",
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
            "const:698:8"
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
      "definition_site": "00b4a958",
      "incomplete_value": true,
      "site": "00b4a958",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a530",
      "incomplete_value": true,
      "site": "00b4a530",
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
            "const:690:8"
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
      "definition_site": "00b4a8e4",
      "incomplete_value": true,
      "site": "00b4a8e4",
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
      "definition_site": "00b4a4bc",
      "incomplete_value": true,
      "site": "00b4a4bc",
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
      "00b4a8e0",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a8ec",
      "READ",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a908",
      "WRITE",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a8e0",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a8ec",
      "READ",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a908",
      "WRITE",
      [
        "storage",
        "01125a98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a4a4.md#insn-00b4a4e0) · [`00b4a52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a4a4.md#insn-00b4a52c) · [`00b4a530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a4a4.md#insn-00b4a530)
- 新版 [`00b4a908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md#insn-00b4a908) · [`00b4a954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md#insn-00b4a954) · [`00b4a958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a8cc.md#insn-00b4a958)

~~~diff
- 00b4a4e0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a4e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a4e0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:698:8"]]
- 00b4a4e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a908 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a908 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a908 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a98:8"]]
+ 00b4a908 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a4e0 bytes bf621a39
+ 00b4a908 bytes bf622a39
- 00b4a52c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a52c ["INT_ADD", "register:40f0:8", ["const:b4a52c:8", "const:4:8"]]
- 00b4a52c ["CALLIND", null, ["register:0:8"]]
+ 00b4a954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a954 ["INT_ADD", "register:40f0:8", ["const:b4a954:8", "const:4:8"]]
+ 00b4a954 ["CALLIND", null, ["register:0:8"]]
- 00b4a52c bytes 00013fd6
+ 00b4a954 bytes 00013fd6
- 00b4a530 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
- 00b4a530 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a530 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a958 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
+ 00b4a958 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a530 bytes 9f4a03f9
+ 00b4a958 bytes 9f4a05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e16b21353a74aecc4563d12e3d6ba127"></a>

### [`00b4a544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a544.md) → [`00b4a96c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md) _ZN8firebase4util4file14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4a9ac",
      "incomplete_value": true,
      "site": "00b4a9ac",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a584",
      "incomplete_value": true,
      "site": "00b4a584",
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
            "const:690:8"
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
      "definition_site": "00b4a988",
      "incomplete_value": true,
      "site": "00b4a988",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a560",
      "incomplete_value": true,
      "site": "00b4a560",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a990",
      "incomplete_value": false,
      "site": "00b4a9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a568",
      "incomplete_value": false,
      "site": "00b4a57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c36:8"
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
      "00b4a980",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a990",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a9ac",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a980",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a990",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4a9ac",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a544.md#insn-00b4a57c) · [`00b4a584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a544.md#insn-00b4a584) · [`00b4a558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a544.md#insn-00b4a558)
- 新版 [`00b4a9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md#insn-00b4a9a4) · [`00b4a9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md#insn-00b4a9ac) · [`00b4a980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a96c.md#insn-00b4a980)

~~~diff
- 00b4a57c ["INT_ADD", "register:40f0:8", ["const:b4a57c:8", "const:4:8"]]
- 00b4a57c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4a9a4 ["INT_ADD", "register:40f0:8", ["const:b4a9a4:8", "const:4:8"]]
+ 00b4a9a4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a57c bytes 65410494
+ 00b4a9a4 bytes 5b410494
- 00b4a584 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
- 00b4a584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a9ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
+ 00b4a9ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a584 bytes 804a03f9
+ 00b4a9ac bytes 804a05f9
- 00b4a558 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
- 00b4a558 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a980 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
+ 00b4a980 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a558 bytes 814a43f9
+ 00b4a980 bytes 814a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61593930965b3c0a3b585d64b84973e9"></a>

### [`00b4a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5b4.md) → [`00b4a9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md) _ZN8firebase4util4file11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b110.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b510.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4a9f8",
      "incomplete_value": false,
      "site": "00b4a9fc",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a5d0",
      "incomplete_value": false,
      "site": "00b4a5d4",
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
            "const:29a:8"
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
      "definition_site": "00b4aa08",
      "incomplete_value": true,
      "site": "00b4aa14",
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
      "definition_site": "00b4a5e0",
      "incomplete_value": true,
      "site": "00b4a5ec",
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
      "00b4a9f8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4aa08",
      "DATA",
      [
        "storage",
        "011256a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a9f8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4aa08",
      "DATA",
      [
        "storage",
        "01125aa0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5b4.md#insn-00b4a5d4) · [`00b4a5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5b4.md#insn-00b4a5d0) · [`00b4a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5b4.md#insn-00b4a5dc)
- 新版 [`00b4a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md#insn-00b4a9fc) · [`00b4a9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md#insn-00b4a9f8) · [`00b4aa04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4a9dc.md#insn-00b4aa04)

~~~diff
- 00b4a5d4 ["INT_ADD", "register:40f0:8", ["const:b4a5d4:8", "const:4:8"]]
- 00b4a5d4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4a9fc ["INT_ADD", "register:40f0:8", ["const:b4a9fc:8", "const:4:8"]]
+ 00b4a9fc ["CALL", null, ["callee:00c5b000:8"]]
- 00b4a5d4 bytes 8b410494
+ 00b4a9fc bytes 81410494
- 00b4a5d0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4a5d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a5d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a5d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a9f8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4a9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a5d0 bytes 00680a91
+ 00b4a9f8 bytes 009c0d91
- 00b4a5dc ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00b4a5dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a5dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a5dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4aa04 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 00b4aa04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4aa04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4aa04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a5dc bytes 08811a91
+ 00b4aa04 bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c2a248d73816464b4fca4b8cfc7662c"></a>

### [`00b4a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5f0.md) → [`00b4aa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md) _ZN8firebase4util4file13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4aa58",
      "incomplete_value": true,
      "site": "00b4aa58",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a630",
      "incomplete_value": true,
      "site": "00b4a630",
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
            "const:690:8"
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
      "definition_site": "00b4aa34",
      "incomplete_value": true,
      "site": "00b4aa34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a60c",
      "incomplete_value": true,
      "site": "00b4a60c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4aa3c",
      "incomplete_value": false,
      "site": "00b4aa50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a614",
      "incomplete_value": false,
      "site": "00b4a628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:c36:8"
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
      "00b4aa2c",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa3c",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4aa58",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa2c",
      "READ",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa3c",
      "PARAM",
      [
        "storage",
        "002b6c76",
        null,
        "string"
      ]
    ],
    [
      "00b4aa58",
      "WRITE",
      [
        "storage",
        "01125a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5f0.md#insn-00b4a628) · [`00b4a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5f0.md#insn-00b4a630) · [`00b4a604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5f0.md#insn-00b4a604)
- 新版 [`00b4aa50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md#insn-00b4aa50) · [`00b4aa58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md#insn-00b4aa58) · [`00b4aa2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa18.md#insn-00b4aa2c)

~~~diff
- 00b4a628 ["INT_ADD", "register:40f0:8", ["const:b4a628:8", "const:4:8"]]
- 00b4a628 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4aa50 ["INT_ADD", "register:40f0:8", ["const:b4aa50:8", "const:4:8"]]
+ 00b4aa50 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a628 bytes 3a410494
+ 00b4aa50 bytes 30410494
- 00b4a630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
- 00b4a630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aa58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
+ 00b4aa58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a630 bytes 804a03f9
+ 00b4aa58 bytes 804a05f9
- 00b4a604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
- 00b4a604 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aa2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a90:8"]]
+ 00b4aa2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a604 bytes 814a43f9
+ 00b4aa2c bytes 814a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54b35e93b48192f5018faf68722423df"></a>

### [`00b4a660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a660.md) → [`00b4aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md) _ZN8firebase4util4file10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4aaa4",
      "incomplete_value": false,
      "site": "00b4aaa8",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a67c",
      "incomplete_value": false,
      "site": "00b4a680",
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
            "const:451:8"
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
      "definition_site": "00b4aab4",
      "incomplete_value": true,
      "site": "00b4aac0",
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
      "definition_site": "00b4a68c",
      "incomplete_value": true,
      "site": "00b4a698",
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
      "00b4aaa4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4aab4",
      "DATA",
      [
        "storage",
        "011256e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4aaa4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4aab4",
      "DATA",
      [
        "storage",
        "01125ae0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a660.md#insn-00b4a680) · [`00b4a67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a660.md#insn-00b4a67c) · [`00b4a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a660.md#insn-00b4a688)
- 新版 [`00b4aaa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md#insn-00b4aaa8) · [`00b4aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md#insn-00b4aaa4) · [`00b4aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aa88.md#insn-00b4aab0)

~~~diff
- 00b4a680 ["INT_ADD", "register:40f0:8", ["const:b4a680:8", "const:4:8"]]
- 00b4a680 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4aaa8 ["INT_ADD", "register:40f0:8", ["const:b4aaa8:8", "const:4:8"]]
+ 00b4aaa8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4a680 bytes 60410494
+ 00b4aaa8 bytes 56410494
- 00b4a67c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4a67c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a67c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a67c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4aaa4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4aaa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aaa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aaa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a67c bytes 00441191
+ 00b4aaa4 bytes 00781491
- 00b4a688 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 00b4a688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4aab0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 00b4aab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4aab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4aab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a688 bytes 08811b91
+ 00b4aab0 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa8f5decba15b10390a596318d599fd"></a>

### [`00b4a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a69c.md) → [`00b4aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4aaf0",
      "incomplete_value": true,
      "site": "00b4aaf0",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a6c8",
      "incomplete_value": true,
      "site": "00b4a6c8",
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
            "const:6e8:8"
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
      "definition_site": "00b4aad8",
      "incomplete_value": true,
      "site": "00b4aad8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a6b0",
      "incomplete_value": true,
      "site": "00b4a6b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4aae4",
      "incomplete_value": false,
      "site": "00b4aae8",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a6bc",
      "incomplete_value": false,
      "site": "00b4a6c0",
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
            "const:4b3:8"
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
      "00b4aad4",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aae4",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4aaf0",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aad4",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aae4",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4aaf0",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a69c.md#insn-00b4a6c0) · [`00b4a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a69c.md#insn-00b4a6c8) · [`00b4a6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a69c.md#insn-00b4a6ac)
- 新版 [`00b4aae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md#insn-00b4aae8) · [`00b4aaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md#insn-00b4aaf0) · [`00b4aad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aac4.md#insn-00b4aad4)

~~~diff
- 00b4a6c0 ["INT_ADD", "register:40f0:8", ["const:b4a6c0:8", "const:4:8"]]
- 00b4a6c0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4aae8 ["INT_ADD", "register:40f0:8", ["const:b4aae8:8", "const:4:8"]]
+ 00b4aae8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a6c0 bytes 14410494
+ 00b4aae8 bytes 0a410494
- 00b4a6c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aaf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4aaf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a6c8 bytes 607603f9
+ 00b4aaf0 bytes 607605f9
- 00b4a6ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a6ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4aad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a6ac bytes 687643f9
+ 00b4aad4 bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a742a9fdb991d166b59484d05162e2dc"></a>

### [`00b4a6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a6dc.md) → [`00b4ab04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4ab30",
      "incomplete_value": true,
      "site": "00b4ab30",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a708",
      "incomplete_value": true,
      "site": "00b4a708",
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
            "const:6e8:8"
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
      "definition_site": "00b4ab18",
      "incomplete_value": true,
      "site": "00b4ab18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a6f0",
      "incomplete_value": true,
      "site": "00b4a6f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ab20",
      "incomplete_value": false,
      "site": "00b4ab28",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a6f8",
      "incomplete_value": false,
      "site": "00b4a700",
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
            "const:4b3:8"
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
      "00b4ab14",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab20",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4ab30",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab14",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab20",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ab30",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a6dc.md#insn-00b4a700) · [`00b4a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a6dc.md#insn-00b4a708) · [`00b4a6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a6dc.md#insn-00b4a6ec)
- 新版 [`00b4ab28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md#insn-00b4ab28) · [`00b4ab30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md#insn-00b4ab30) · [`00b4ab14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab04.md#insn-00b4ab14)

~~~diff
- 00b4a700 ["INT_ADD", "register:40f0:8", ["const:b4a700:8", "const:4:8"]]
- 00b4a700 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ab28 ["INT_ADD", "register:40f0:8", ["const:b4ab28:8", "const:4:8"]]
+ 00b4ab28 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a700 bytes 04410494
+ 00b4ab28 bytes fa400494
- 00b4a708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4ab30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a708 bytes 607603f9
+ 00b4ab30 bytes 607605f9
- 00b4a6ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a6ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ab14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4ab14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a6ec bytes 687643f9
+ 00b4ab14 bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c06163345eb3890d02ee09392484952"></a>

### [`00b4a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a71c.md) → [`00b4ab44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4ab74",
      "incomplete_value": true,
      "site": "00b4ab74",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a74c",
      "incomplete_value": true,
      "site": "00b4a74c",
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
            "const:6e8:8"
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
      "definition_site": "00b4ab58",
      "incomplete_value": true,
      "site": "00b4ab58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a730",
      "incomplete_value": true,
      "site": "00b4a730",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ab64",
      "incomplete_value": false,
      "site": "00b4ab6c",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a73c",
      "incomplete_value": false,
      "site": "00b4a744",
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
            "const:4b3:8"
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
      "00b4ab54",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab64",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4ab74",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab54",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab64",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ab74",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a71c.md#insn-00b4a744) · [`00b4a74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a71c.md#insn-00b4a74c) · [`00b4a72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a71c.md#insn-00b4a72c)
- 新版 [`00b4ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md#insn-00b4ab6c) · [`00b4ab74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md#insn-00b4ab74) · [`00b4ab54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab44.md#insn-00b4ab54)

~~~diff
- 00b4a744 ["INT_ADD", "register:40f0:8", ["const:b4a744:8", "const:4:8"]]
- 00b4a744 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ab6c ["INT_ADD", "register:40f0:8", ["const:b4ab6c:8", "const:4:8"]]
+ 00b4ab6c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a744 bytes f3400494
+ 00b4ab6c bytes e9400494
- 00b4a74c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4ab74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a74c bytes 607603f9
+ 00b4ab74 bytes 607605f9
- 00b4a72c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a72c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ab54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4ab54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a72c bytes 687643f9
+ 00b4ab54 bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce7ac00e82c877941d41fb4332a8798e"></a>

### [`00b4a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a760.md) → [`00b4ab88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4abb8",
      "incomplete_value": true,
      "site": "00b4abb8",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a790",
      "incomplete_value": true,
      "site": "00b4a790",
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
            "const:6e8:8"
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
      "definition_site": "00b4ab9c",
      "incomplete_value": true,
      "site": "00b4ab9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a774",
      "incomplete_value": true,
      "site": "00b4a774",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4aba4",
      "incomplete_value": false,
      "site": "00b4abb0",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a77c",
      "incomplete_value": false,
      "site": "00b4a788",
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
            "const:4b3:8"
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
      "00b4ab98",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aba4",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4abb8",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab98",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aba4",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4abb8",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a760.md#insn-00b4a788) · [`00b4a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a760.md#insn-00b4a790) · [`00b4a770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a760.md#insn-00b4a770)
- 新版 [`00b4abb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md#insn-00b4abb0) · [`00b4abb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md#insn-00b4abb8) · [`00b4ab98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ab88.md#insn-00b4ab98)

~~~diff
- 00b4a788 ["INT_ADD", "register:40f0:8", ["const:b4a788:8", "const:4:8"]]
- 00b4a788 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4abb0 ["INT_ADD", "register:40f0:8", ["const:b4abb0:8", "const:4:8"]]
+ 00b4abb0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a788 bytes e2400494
+ 00b4abb0 bytes d8400494
- 00b4a790 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4abb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4abb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a790 bytes 607603f9
+ 00b4abb8 bytes 607605f9
- 00b4a770 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00b4a770 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ab98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae8:8"]]
+ 00b4ab98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a770 bytes 687643f9
+ 00b4ab98 bytes 687645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37172003f755ac64fbe366ada49faf6b"></a>

### [`00b4a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a7b0.md) → [`00b4abd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md) _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4ac60",
      "incomplete_value": true,
      "site": "00b4ac60",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a838",
      "incomplete_value": true,
      "site": "00b4a838",
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
            "const:6f0:8"
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
      "definition_site": "00b4ac0c",
      "incomplete_value": true,
      "site": "00b4ac18",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7e4",
      "incomplete_value": true,
      "site": "00b4a7f0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:6e8:8"
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
      "00b4abec",
      "READ",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac0c",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac60",
      "WRITE",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4abec",
      "READ",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac0c",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac60",
      "WRITE",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a7b0.md#insn-00b4a7f0) · [`00b4a838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a7b0.md#insn-00b4a838) · [`00b4a7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a7b0.md#insn-00b4a7c4)
- 新版 [`00b4ac18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md#insn-00b4ac18) · [`00b4ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md#insn-00b4ac60) · [`00b4abec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4abd8.md#insn-00b4abec)

~~~diff
- 00b4a7f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a7f0 ["INT_ADD", "register:40f0:8", ["const:b4a7f0:8", "const:4:8"]]
- 00b4a7f0 ["CALLIND", null, ["register:0:8"]]
+ 00b4ac18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ac18 ["INT_ADD", "register:40f0:8", ["const:b4ac18:8", "const:4:8"]]
+ 00b4ac18 ["CALLIND", null, ["register:0:8"]]
- 00b4a7f0 bytes 00013fd6
+ 00b4ac18 bytes 00013fd6
- 00b4a838 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a838 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6f0:8"]]
- 00b4a838 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ac60 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ac60 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:af0:8"]]
+ 00b4ac60 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a838 bytes a0c21b39
+ 00b4ac60 bytes a0c22b39
- 00b4a7c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6f0:8"]]
- 00b4a7c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4a7c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4abec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:af0:8"]]
+ 00b4abec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4abec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4a7c4 bytes a8c25b39
+ 00b4abec bytes a8c26b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-351951b22aa4040ecd19e47ea9cefb31"></a>

### [`00b4a84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a84c.md) → [`00b4ac74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md) _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4acb0",
      "incomplete_value": true,
      "site": "00b4acb0",
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
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a888",
      "incomplete_value": true,
      "site": "00b4a888",
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
            "const:6f0:8"
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
      "definition_site": "00b4ad00",
      "incomplete_value": true,
      "site": "00b4ad00",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a8d8",
      "incomplete_value": true,
      "site": "00b4a8d8",
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
            "const:6e8:8"
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
      "definition_site": "00b4ac8c",
      "incomplete_value": true,
      "site": "00b4ac8c",
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
      "definition_site": "00b4a864",
      "incomplete_value": true,
      "site": "00b4a864",
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
      "00b4ac88",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac94",
      "READ",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4acb0",
      "WRITE",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ac88",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac94",
      "READ",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4acb0",
      "WRITE",
      [
        "storage",
        "01125af0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a84c.md#insn-00b4a888) · [`00b4a8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a84c.md#insn-00b4a8d4) · [`00b4a8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a84c.md#insn-00b4a8d8)
- 新版 [`00b4acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md#insn-00b4acb0) · [`00b4acfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md#insn-00b4acfc) · [`00b4ad00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ac74.md#insn-00b4ad00)

~~~diff
- 00b4a888 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a888 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a888 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
- 00b4a888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4acb0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4acb0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4acb0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:af0:8"]]
+ 00b4acb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a888 bytes bfc21b39
+ 00b4acb0 bytes bfc22b39
- 00b4a8d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a8d4 ["INT_ADD", "register:40f0:8", ["const:b4a8d4:8", "const:4:8"]]
- 00b4a8d4 ["CALLIND", null, ["register:0:8"]]
+ 00b4acfc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4acfc ["INT_ADD", "register:40f0:8", ["const:b4acfc:8", "const:4:8"]]
+ 00b4acfc ["CALLIND", null, ["register:0:8"]]
- 00b4a8d4 bytes 00013fd6
+ 00b4acfc bytes 00013fd6
- 00b4a8d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b4a8d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a8d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4ad00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00b4ad00 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4ad00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a8d8 bytes 9f7603f9
+ 00b4ad00 bytes 9f7605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27863e5fae6f5b183f30ed75da457954"></a>

### [`00b4a8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a8ec.md) → [`00b4ad14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md) _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4ad54",
      "incomplete_value": true,
      "site": "00b4ad54",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a92c",
      "incomplete_value": true,
      "site": "00b4a92c",
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
            "const:6e8:8"
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
      "definition_site": "00b4ad30",
      "incomplete_value": true,
      "site": "00b4ad30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a908",
      "incomplete_value": true,
      "site": "00b4a908",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ad38",
      "incomplete_value": false,
      "site": "00b4ad4c",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a910",
      "incomplete_value": false,
      "site": "00b4a924",
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
            "const:4b3:8"
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
      "00b4ad28",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad38",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4ad54",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad28",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad38",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ad54",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a8ec.md#insn-00b4a924) · [`00b4a92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a8ec.md#insn-00b4a92c) · [`00b4a900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a8ec.md#insn-00b4a900)
- 新版 [`00b4ad4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md#insn-00b4ad4c) · [`00b4ad54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md#insn-00b4ad54) · [`00b4ad28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad14.md#insn-00b4ad28)

~~~diff
- 00b4a924 ["INT_ADD", "register:40f0:8", ["const:b4a924:8", "const:4:8"]]
- 00b4a924 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ad4c ["INT_ADD", "register:40f0:8", ["const:b4ad4c:8", "const:4:8"]]
+ 00b4ad4c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a924 bytes 7b400494
+ 00b4ad4c bytes 71400494
- 00b4a92c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b4a92c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ad54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00b4ad54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a92c bytes 807603f9
+ 00b4ad54 bytes 807605f9
- 00b4a900 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b4a900 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ad28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00b4ad28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a900 bytes 817643f9
+ 00b4ad28 bytes 817645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fce2514cb291d84162548e08012de9c6"></a>

### [`00b4a95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a95c.md) → [`00b4ad84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md) _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4ada0",
      "incomplete_value": false,
      "site": "00b4ada4",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a978",
      "incomplete_value": false,
      "site": "00b4a97c",
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
            "const:29a:8"
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
      "definition_site": "00b4adb0",
      "incomplete_value": true,
      "site": "00b4adbc",
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
      "definition_site": "00b4a988",
      "incomplete_value": true,
      "site": "00b4a994",
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
      "00b4ada0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4adb0",
      "DATA",
      [
        "storage",
        "011256f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ada0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4adb0",
      "DATA",
      [
        "storage",
        "01125af8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a95c.md#insn-00b4a97c) · [`00b4a978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a95c.md#insn-00b4a978) · [`00b4a984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a95c.md#insn-00b4a984)
- 新版 [`00b4ada4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md#insn-00b4ada4) · [`00b4ada0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md#insn-00b4ada0) · [`00b4adac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ad84.md#insn-00b4adac)

~~~diff
- 00b4a97c ["INT_ADD", "register:40f0:8", ["const:b4a97c:8", "const:4:8"]]
- 00b4a97c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4ada4 ["INT_ADD", "register:40f0:8", ["const:b4ada4:8", "const:4:8"]]
+ 00b4ada4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4a97c bytes a1400494
+ 00b4ada4 bytes 97400494
- 00b4a978 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4a978 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a978 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a978 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ada0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4ada0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ada0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ada0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a978 bytes 00680a91
+ 00b4ada0 bytes 009c0d91
- 00b4a984 ["COPY", "tmp:0:8", ["const:6f8:8"]]
- 00b4a984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4a984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4adac ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00b4adac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4adac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4adac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4a984 bytes 08e11b91
+ 00b4adac bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4900d8949f1e268ff596225b3cef76b"></a>

### [`00b4a998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a998.md) → [`00b4adc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md) _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4ae00",
      "incomplete_value": true,
      "site": "00b4ae00",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a9d8",
      "incomplete_value": true,
      "site": "00b4a9d8",
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
            "const:6e8:8"
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
      "definition_site": "00b4addc",
      "incomplete_value": true,
      "site": "00b4addc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4a9b4",
      "incomplete_value": true,
      "site": "00b4a9b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ade4",
      "incomplete_value": false,
      "site": "00b4adf8",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a9bc",
      "incomplete_value": false,
      "site": "00b4a9d0",
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
            "const:4b3:8"
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
      "00b4add4",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ade4",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4ae00",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4add4",
      "READ",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ade4",
      "PARAM",
      [
        "storage",
        "002a9580",
        null,
        "string"
      ]
    ],
    [
      "00b4ae00",
      "WRITE",
      [
        "storage",
        "01125ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a998.md#insn-00b4a9d0) · [`00b4a9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a998.md#insn-00b4a9d8) · [`00b4a9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a998.md#insn-00b4a9ac)
- 新版 [`00b4adf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md#insn-00b4adf8) · [`00b4ae00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md#insn-00b4ae00) · [`00b4add4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4adc0.md#insn-00b4add4)

~~~diff
- 00b4a9d0 ["INT_ADD", "register:40f0:8", ["const:b4a9d0:8", "const:4:8"]]
- 00b4a9d0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4adf8 ["INT_ADD", "register:40f0:8", ["const:b4adf8:8", "const:4:8"]]
+ 00b4adf8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4a9d0 bytes 50400494
+ 00b4adf8 bytes 46400494
- 00b4a9d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b4a9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ae00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00b4ae00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a9d8 bytes 807603f9
+ 00b4ae00 bytes 807605f9
- 00b4a9ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00b4a9ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4add4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae8:8"]]
+ 00b4add4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4a9ac bytes 817643f9
+ 00b4add4 bytes 817645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b167e326763be31d8a9f3e1b1cf4c843"></a>

### [`00b4aa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa08.md) → [`00b4ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae30.md) _ZN8firebase4util11float_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4ae4c",
      "incomplete_value": false,
      "site": "00b4ae50",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa24",
      "incomplete_value": false,
      "site": "00b4aa28",
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
            "const:451:8"
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
      "definition_site": "00b4ae5c",
      "incomplete_value": true,
      "site": "00b4ae68",
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
      "definition_site": "00b4aa34",
      "incomplete_value": true,
      "site": "00b4aa40",
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
      "00b4ae4c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4ae5c",
      "DATA",
      [
        "storage",
        "01125708",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ae4c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4ae5c",
      "DATA",
      [
        "storage",
        "01125b08",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa08.md#insn-00b4aa28) · [`00b4aa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa08.md#insn-00b4aa24) · [`00b4aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa08.md#insn-00b4aa30)
- 新版 [`00b4ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae30.md#insn-00b4ae50) · [`00b4ae4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae30.md#insn-00b4ae4c) · [`00b4ae58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae30.md#insn-00b4ae58)

~~~diff
- 00b4aa28 ["INT_ADD", "register:40f0:8", ["const:b4aa28:8", "const:4:8"]]
- 00b4aa28 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4ae50 ["INT_ADD", "register:40f0:8", ["const:b4ae50:8", "const:4:8"]]
+ 00b4ae50 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4aa28 bytes 76400494
+ 00b4ae50 bytes 6c400494
- 00b4aa24 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4aa24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aa24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aa24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae4c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4ae4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4aa24 bytes 00441191
+ 00b4ae4c bytes 00781491
- 00b4aa30 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00b4aa30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4aa30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4aa30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae58 ["COPY", "tmp:0:8", ["const:b08:8"]]
+ 00b4ae58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4aa30 bytes 08211c91
+ 00b4ae58 bytes 08212c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f08ee31f2fefd7175819c2ce191a5fb8"></a>

### [`00b4aa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa44.md) → [`00b4ae6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae6c.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4aa70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ae98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ae80",
      "incomplete_value": true,
      "site": "00b4ae80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4aa58",
      "incomplete_value": true,
      "site": "00b4aa58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4ae7c",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4aa64",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4aa68",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae7c",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae8c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4ae90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa44.md#insn-00b4aa58) · [`00b4aa68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa44.md#insn-00b4aa68) · [`00b4aa70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa44.md#insn-00b4aa70)
- 新版 [`00b4ae80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4ae6c.md#insn-00b4ae80)

~~~diff
- 00b4aa58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aa58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4ae80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4ae80 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4aa58 bytes e80000b5
+ 00b4ae80 bytes e80000b5
- 00b4aa68 ["INT_ADD", "register:40f0:8", ["const:b4aa68:8", "const:4:8"]]
- 00b4aa68 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4aa68 bytes 2a400494
- 00b4aa70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00b4aa70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aa70 bytes 608a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8b0731fb7147da3cbfac2377557d2f"></a>

### [`00b4aa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa84.md) → [`00b4aeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeac.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4aa84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aa88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aa88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aa84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aa88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4aebc",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aeac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4aeb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4aebc",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa84.md#insn-00b4aa84) · [`00b4aa88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa84.md#insn-00b4aa88) · [`00b4aa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa84.md#insn-00b4aa98)
- 新版 [`00b4aec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeac.md#insn-00b4aec0)

~~~diff
- 00b4aa84 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4aa84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4aa84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4aa84 bytes f30f1ef8
- 00b4aa88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4aa88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4aa88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4aa88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aa88 bytes fd7b01a9
- 00b4aa98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aa98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4aec0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4aec0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4aa98 bytes e80000b5
+ 00b4aec0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee6f09a44cef9029ce0a8af70033b15"></a>

### [`00b4aac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aac4.md) → [`00b4aeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4af1c",
      "incomplete_value": true,
      "site": "00b4af1c",
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
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aaf4",
      "incomplete_value": true,
      "site": "00b4aaf4",
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
            "const:710:8"
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
      "definition_site": "00b4af00",
      "incomplete_value": true,
      "site": "00b4af00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4aad8",
      "incomplete_value": true,
      "site": "00b4aad8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4af0c",
      "incomplete_value": false,
      "site": "00b4af14",
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
            "const:7e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aae4",
      "incomplete_value": false,
      "site": "00b4aaec",
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
            "const:70a:8"
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
      "00b4aefc",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af0c",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4af1c",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aefc",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af0c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4af1c",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aac4.md#insn-00b4aaec) · [`00b4aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aac4.md#insn-00b4aaf4) · [`00b4aad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aac4.md#insn-00b4aad4)
- 新版 [`00b4af14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md#insn-00b4af14) · [`00b4af1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md#insn-00b4af1c) · [`00b4aefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4aeec.md#insn-00b4aefc)

~~~diff
- 00b4aaec ["INT_ADD", "register:40f0:8", ["const:b4aaec:8", "const:4:8"]]
- 00b4aaec ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4af14 ["INT_ADD", "register:40f0:8", ["const:b4af14:8", "const:4:8"]]
+ 00b4af14 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4aaec bytes 09400494
+ 00b4af14 bytes ff3f0494
- 00b4aaf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00b4aaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4af1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
+ 00b4af1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aaf4 bytes 608a03f9
+ 00b4af1c bytes 608a05f9
- 00b4aad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00b4aad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aefc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
+ 00b4aefc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aad4 bytes 688a43f9
+ 00b4aefc bytes 688a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6822af50f5470c9c7f1a14122d5d781"></a>

### [`00b4ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab08.md) → [`00b4af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4af60",
      "incomplete_value": true,
      "site": "00b4af60",
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
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab38",
      "incomplete_value": true,
      "site": "00b4ab38",
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
            "const:710:8"
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
      "definition_site": "00b4af44",
      "incomplete_value": true,
      "site": "00b4af44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ab1c",
      "incomplete_value": true,
      "site": "00b4ab1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4af4c",
      "incomplete_value": false,
      "site": "00b4af58",
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
            "const:7e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab24",
      "incomplete_value": false,
      "site": "00b4ab30",
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
            "const:70a:8"
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
      "00b4af40",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af4c",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4af60",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4af40",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af4c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4af60",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab08.md#insn-00b4ab30) · [`00b4ab38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab08.md#insn-00b4ab38) · [`00b4ab18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab08.md#insn-00b4ab18)
- 新版 [`00b4af58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md#insn-00b4af58) · [`00b4af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md#insn-00b4af60) · [`00b4af40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af30.md#insn-00b4af40)

~~~diff
- 00b4ab30 ["INT_ADD", "register:40f0:8", ["const:b4ab30:8", "const:4:8"]]
- 00b4ab30 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4af58 ["INT_ADD", "register:40f0:8", ["const:b4af58:8", "const:4:8"]]
+ 00b4af58 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ab30 bytes f83f0494
+ 00b4af58 bytes ee3f0494
- 00b4ab38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00b4ab38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4af60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
+ 00b4af60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab38 bytes 608a03f9
+ 00b4af60 bytes 608a05f9
- 00b4ab18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
- 00b4ab18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4af40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
+ 00b4af40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab18 bytes 688a43f9
+ 00b4af40 bytes 688a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a1d4f6f3a603d8a6fde3aab9ee3ae18"></a>

### [`00b4ab58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab58.md) → [`00b4af80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md) _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b008",
      "incomplete_value": true,
      "site": "00b4b008",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abe0",
      "incomplete_value": true,
      "site": "00b4abe0",
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
            "const:718:8"
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
      "definition_site": "00b4afb4",
      "incomplete_value": true,
      "site": "00b4afc0",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab8c",
      "incomplete_value": true,
      "site": "00b4ab98",
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
                "const:1125000:8"
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
      "00b4af94",
      "READ",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4afb4",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b008",
      "WRITE",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4af94",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4afb4",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b008",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab58.md#insn-00b4ab98) · [`00b4abe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab58.md#insn-00b4abe0) · [`00b4ab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab58.md#insn-00b4ab6c)
- 新版 [`00b4afc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md#insn-00b4afc0) · [`00b4b008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md#insn-00b4b008) · [`00b4af94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4a/00b4af80.md#insn-00b4af94)

~~~diff
- 00b4ab98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ab98 ["INT_ADD", "register:40f0:8", ["const:b4ab98:8", "const:4:8"]]
- 00b4ab98 ["CALLIND", null, ["register:0:8"]]
+ 00b4afc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4afc0 ["INT_ADD", "register:40f0:8", ["const:b4afc0:8", "const:4:8"]]
+ 00b4afc0 ["CALLIND", null, ["register:0:8"]]
- 00b4ab98 bytes 00013fd6
+ 00b4afc0 bytes 00013fd6
- 00b4abe0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4abe0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:718:8"]]
- 00b4abe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b008 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b008 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b18:8"]]
+ 00b4b008 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4abe0 bytes a0621c39
+ 00b4b008 bytes a0622c39
- 00b4ab6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:718:8"]]
- 00b4ab6c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab6c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4af94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b18:8"]]
+ 00b4af94 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4af94 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4ab6c bytes a8625c39
+ 00b4af94 bytes a8626c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-502f2cafbd25698926b3888a6f3785c9"></a>

### [`00b4abf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4abf4.md) → [`00b4b01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md) _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 60.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b058",
      "incomplete_value": true,
      "site": "00b4b058",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac30",
      "incomplete_value": true,
      "site": "00b4ac30",
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
            "const:718:8"
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
      "site": "00b4ac80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b0a8"
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
      "00b4b030",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b03c",
      "READ",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b058",
      "WRITE",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b030",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b03c",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b058",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4abf4.md#insn-00b4ac0c) · [`00b4ac30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4abf4.md#insn-00b4ac30) · [`00b4ac7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4abf4.md#insn-00b4ac7c)
- 新版 [`00b4b034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md#insn-00b4b034) · [`00b4b058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b01c.md#insn-00b4b058)

~~~diff
- 00b4ac0c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4ac0c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b4b034 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4b034 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b4ac0c bytes c10300b4
+ 00b4b034 bytes c10300b4
- 00b4ac30 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4ac30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4ac30 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:718:8"]]
- 00b4ac30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b058 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b058 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b058 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b18:8"]]
+ 00b4b058 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4ac30 bytes bf621c39
+ 00b4b058 bytes bf622c39
- 00b4ac7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ac7c ["INT_ADD", "register:40f0:8", ["const:b4ac7c:8", "const:4:8"]]
- 00b4ac7c ["CALLIND", null, ["register:0:8"]]
- 00b4ac7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90b81ca2436d5cf758a4c9c7e7b56746"></a>

### [`00b4ac94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ac94.md) → [`00b4b0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b0bc.md) _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00b4acd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b0fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4acb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aca8",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4acb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b100"
      ]
    ],
    [
      "unmatched:00b4acb8",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b0d0",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b100"
      ]
    ],
    [
      "00b4b0e0",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4acb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ac94.md#insn-00b4acb0) · [`00b4accc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ac94.md#insn-00b4accc) · [`00b4acd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ac94.md#insn-00b4acd4)
- 新版 [`00b4b0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b0bc.md#insn-00b4b0f4)

~~~diff
- 00b4acb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4acb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4acb0 bytes 410100b5
- 00b4accc ["INT_ADD", "register:40f0:8", ["const:b4accc:8", "const:4:8"]]
- 00b4accc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b0f4 ["INT_ADD", "register:40f0:8", ["const:b4b0f4:8", "const:4:8"]]
+ 00b4b0f4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4accc bytes 913f0494
+ 00b4b0f4 bytes 873f0494
- 00b4acd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00b4acd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4acd4 bytes 808a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f5f6337fff38b2055085494e5da77cd"></a>

### [`00b4ad04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad04.md) → [`00b4b12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md) _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5abb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abb0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5afb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afb0.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4b148",
      "incomplete_value": false,
      "site": "00b4b14c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad20",
      "incomplete_value": false,
      "site": "00b4ad24",
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
            "const:29a:8"
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
      "definition_site": "00b4b158",
      "incomplete_value": true,
      "site": "00b4b164",
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
      "definition_site": "00b4ad30",
      "incomplete_value": true,
      "site": "00b4ad3c",
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
      "00b4b148",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4b158",
      "DATA",
      [
        "storage",
        "01125720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b148",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4b158",
      "DATA",
      [
        "storage",
        "01125b20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad04.md#insn-00b4ad24) · [`00b4ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad04.md#insn-00b4ad20) · [`00b4ad2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad04.md#insn-00b4ad2c)
- 新版 [`00b4b14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md#insn-00b4b14c) · [`00b4b148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md#insn-00b4b148) · [`00b4b154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b12c.md#insn-00b4b154)

~~~diff
- 00b4ad24 ["INT_ADD", "register:40f0:8", ["const:b4ad24:8", "const:4:8"]]
- 00b4ad24 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4b14c ["INT_ADD", "register:40f0:8", ["const:b4b14c:8", "const:4:8"]]
+ 00b4b14c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4ad24 bytes b73f0494
+ 00b4b14c bytes ad3f0494
- 00b4ad20 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4ad20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ad20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ad20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b148 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4b148 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b148 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b148 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ad20 bytes 00680a91
+ 00b4b148 bytes 009c0d91
- 00b4ad2c ["COPY", "tmp:0:8", ["const:720:8"]]
- 00b4ad2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ad2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ad2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b154 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00b4b154 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b154 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b154 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4ad2c bytes 08811c91
+ 00b4b154 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c608f1e2f046a52259cbdbe9ed3802d"></a>

### [`00b4ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad40.md) → [`00b4b168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md) _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b1a8",
      "incomplete_value": true,
      "site": "00b4b1a8",
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
            "const:b10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad80",
      "incomplete_value": true,
      "site": "00b4ad80",
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
            "const:710:8"
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
      "definition_site": "00b4b184",
      "incomplete_value": true,
      "site": "00b4b184",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ad5c",
      "incomplete_value": true,
      "site": "00b4ad5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b18c",
      "incomplete_value": false,
      "site": "00b4b1a0",
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
            "const:7e6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad64",
      "incomplete_value": false,
      "site": "00b4ad78",
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
            "const:70a:8"
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
      "00b4b17c",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b18c",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4b1a8",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b17c",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b18c",
      "PARAM",
      [
        "storage",
        "002a67e6",
        null,
        "string"
      ]
    ],
    [
      "00b4b1a8",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad40.md#insn-00b4ad78) · [`00b4ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad40.md#insn-00b4ad80) · [`00b4ad54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad40.md#insn-00b4ad54)
- 新版 [`00b4b1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md#insn-00b4b1a0) · [`00b4b1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md#insn-00b4b1a8) · [`00b4b17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b168.md#insn-00b4b17c)

~~~diff
- 00b4ad78 ["INT_ADD", "register:40f0:8", ["const:b4ad78:8", "const:4:8"]]
- 00b4ad78 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b1a0 ["INT_ADD", "register:40f0:8", ["const:b4b1a0:8", "const:4:8"]]
+ 00b4b1a0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ad78 bytes 663f0494
+ 00b4b1a0 bytes 5c3f0494
- 00b4ad80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00b4ad80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b1a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
+ 00b4b1a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ad80 bytes 808a03f9
+ 00b4b1a8 bytes 808a05f9
- 00b4ad54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00b4ad54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b17c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
+ 00b4b17c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ad54 bytes 818a43f9
+ 00b4b17c bytes 818a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91d11000f45909a750749af0998ebc6a"></a>

### [`00b4adb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adb0.md) → [`00b4b1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md) _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4b1f4",
      "incomplete_value": false,
      "site": "00b4b1f8",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4adcc",
      "incomplete_value": false,
      "site": "00b4add0",
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
            "const:451:8"
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
      "definition_site": "00b4b204",
      "incomplete_value": true,
      "site": "00b4b210",
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
      "definition_site": "00b4addc",
      "incomplete_value": true,
      "site": "00b4ade8",
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
      "00b4b1f4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4b204",
      "DATA",
      [
        "storage",
        "01125728",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b1f4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4b204",
      "DATA",
      [
        "storage",
        "01125b28",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4add0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adb0.md#insn-00b4add0) · [`00b4adcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adb0.md#insn-00b4adcc) · [`00b4add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adb0.md#insn-00b4add8)
- 新版 [`00b4b1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md#insn-00b4b1f8) · [`00b4b1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md#insn-00b4b1f4) · [`00b4b200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b1d8.md#insn-00b4b200)

~~~diff
- 00b4add0 ["INT_ADD", "register:40f0:8", ["const:b4add0:8", "const:4:8"]]
- 00b4add0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4b1f8 ["INT_ADD", "register:40f0:8", ["const:b4b1f8:8", "const:4:8"]]
+ 00b4b1f8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4add0 bytes 8c3f0494
+ 00b4b1f8 bytes 823f0494
- 00b4adcc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4adcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4adcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4adcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b1f4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4b1f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b1f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b1f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4adcc bytes 00441191
+ 00b4b1f4 bytes 00781491
- 00b4add8 ["COPY", "tmp:0:8", ["const:728:8"]]
- 00b4add8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4add8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4add8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b200 ["COPY", "tmp:0:8", ["const:b28:8"]]
+ 00b4b200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4add8 bytes 08a11c91
+ 00b4b200 bytes 08a12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb97fa384438372c708f4bf7b018959d"></a>

### [`00b4adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adec.md) → [`00b4b214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b240",
      "incomplete_value": true,
      "site": "00b4b240",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae18",
      "incomplete_value": true,
      "site": "00b4ae18",
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
            "const:730:8"
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
      "definition_site": "00b4b228",
      "incomplete_value": true,
      "site": "00b4b228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ae00",
      "incomplete_value": true,
      "site": "00b4ae00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b234",
      "incomplete_value": false,
      "site": "00b4b238",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae0c",
      "incomplete_value": false,
      "site": "00b4ae10",
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
            "const:365:8"
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
      "00b4b224",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b234",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4b240",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b224",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b234",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b240",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adec.md#insn-00b4ae10) · [`00b4ae18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adec.md#insn-00b4ae18) · [`00b4adfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adec.md#insn-00b4adfc)
- 新版 [`00b4b238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md#insn-00b4b238) · [`00b4b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md#insn-00b4b240) · [`00b4b224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md#insn-00b4b224)

~~~diff
- 00b4ae10 ["INT_ADD", "register:40f0:8", ["const:b4ae10:8", "const:4:8"]]
- 00b4ae10 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b238 ["INT_ADD", "register:40f0:8", ["const:b4b238:8", "const:4:8"]]
+ 00b4b238 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ae10 bytes 403f0494
+ 00b4b238 bytes 363f0494
- 00b4ae18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
- 00b4ae18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b240 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
+ 00b4b240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae18 bytes 609a03f9
+ 00b4b240 bytes 609a05f9
- 00b4adfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
- 00b4adfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
+ 00b4b224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4adfc bytes 689a43f9
+ 00b4b224 bytes 689a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35df3a5dd308badbbf7ec6b7372b72f9"></a>

### [`00b4ae2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae2c.md) → [`00b4b254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b280",
      "incomplete_value": true,
      "site": "00b4b280",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae58",
      "incomplete_value": true,
      "site": "00b4ae58",
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
            "const:730:8"
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
      "definition_site": "00b4b268",
      "incomplete_value": true,
      "site": "00b4b268",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ae40",
      "incomplete_value": true,
      "site": "00b4ae40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b270",
      "incomplete_value": false,
      "site": "00b4b278",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae48",
      "incomplete_value": false,
      "site": "00b4ae50",
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
            "const:365:8"
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
      "00b4b264",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b270",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4b280",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b264",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b270",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b280",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae2c.md#insn-00b4ae50) · [`00b4ae58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae2c.md#insn-00b4ae58) · [`00b4ae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae2c.md#insn-00b4ae3c)
- 新版 [`00b4b278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md#insn-00b4b278) · [`00b4b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md#insn-00b4b280) · [`00b4b264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b254.md#insn-00b4b264)

~~~diff
- 00b4ae50 ["INT_ADD", "register:40f0:8", ["const:b4ae50:8", "const:4:8"]]
- 00b4ae50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b278 ["INT_ADD", "register:40f0:8", ["const:b4b278:8", "const:4:8"]]
+ 00b4b278 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ae50 bytes 303f0494
+ 00b4b278 bytes 263f0494
- 00b4ae58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
- 00b4ae58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b280 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
+ 00b4b280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae58 bytes 609a03f9
+ 00b4b280 bytes 609a05f9
- 00b4ae3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
- 00b4ae3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b264 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b30:8"]]
+ 00b4b264 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ae3c bytes 689a43f9
+ 00b4b264 bytes 689a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-117a256bb9e38c1ce2cb289cd5abb846"></a>

### [`00b4ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae6c.md) → [`00b4b294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b294.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4ae9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b2c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b2a8",
      "incomplete_value": true,
      "site": "00b4b2a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ae80",
      "incomplete_value": true,
      "site": "00b4ae80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4b2a4",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4aea0"
      ]
    ],
    [
      "unmatched:00b4ae8c",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b2a4",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b2c8"
      ]
    ],
    [
      "00b4b2b4",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae6c.md#insn-00b4ae94) · [`00b4ae9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae6c.md#insn-00b4ae9c) · [`00b4aeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae6c.md#insn-00b4aeac)

~~~diff
- 00b4ae94 ["INT_ADD", "register:40f0:8", ["const:b4ae94:8", "const:4:8"]]
- 00b4ae94 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ae94 bytes 1f3f0494
- 00b4ae9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
- 00b4ae9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae9c bytes 609a03f9
- 00b4aeac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4aeac ["RETURN", null, ["register:0:8"]]
- 00b4aeac bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f996286a007f8150e57e9cc41ab2e74f"></a>

### [`00b4aeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aeb0.md) → [`00b4b2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b2d8.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4aeb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aeb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4aeb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4aeb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4aeb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b2e8",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b2d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b2e8",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aeb0.md#insn-00b4aeb0) · [`00b4aeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aeb0.md#insn-00b4aeb4) · [`00b4aec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aeb0.md#insn-00b4aec4)
- 新版 [`00b4b2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b2d8.md#insn-00b4b2ec)

~~~diff
- 00b4aeb0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4aeb0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4aeb0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4aeb0 bytes f30f1ef8
- 00b4aeb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4aeb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4aeb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4aeb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4aeb4 bytes fd7b01a9
- 00b4aec4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4aec4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4b2ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4b2ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4aec4 bytes 080100b5
+ 00b4b2ec bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2717233242245d07af2acdb46216565d"></a>

### [`00b4af00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af00.md) → [`00b4b328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b328.md) _ZN8firebase4util13integer_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 57.14% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b3b0",
      "incomplete_value": true,
      "site": "00b4b3b0",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af88",
      "incomplete_value": true,
      "site": "00b4af88",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4af40"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4af54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b33c",
      "READ",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4af34",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b3b0",
      "WRITE",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b33c",
      "READ",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b35c",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b3b0",
      "WRITE",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af00.md#insn-00b4af40) · [`00b4af54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af00.md#insn-00b4af54) · [`00b4af88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af00.md#insn-00b4af88)
- 新版 [`00b4b3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b328.md#insn-00b4b3b0)

~~~diff
- 00b4af40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4af40 ["INT_ADD", "register:40f0:8", ["const:b4af40:8", "const:4:8"]]
- 00b4af40 ["CALLIND", null, ["register:0:8"]]
- 00b4af40 bytes 00013fd6
- 00b4af54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4af54 ["INT_ADD", "register:40f0:8", ["const:b4af54:8", "const:4:8"]]
- 00b4af54 ["CALLIND", null, ["register:0:8"]]
- 00b4af54 bytes 00013fd6
- 00b4af88 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4af88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:738:8"]]
- 00b4af88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b3b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b3b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b38:8"]]
+ 00b4b3b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4af88 bytes a0e21c39
+ 00b4b3b0 bytes a0e22c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d12a09ea8a4fae3c2a47b4e8ed52f00"></a>

### [`00b4af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af9c.md) → [`00b4b3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md) _ZN8firebase4util13integer_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b400",
      "incomplete_value": true,
      "site": "00b4b400",
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
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afd8",
      "incomplete_value": true,
      "site": "00b4afd8",
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
            "const:738:8"
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
      "definition_site": "00b4b450",
      "incomplete_value": true,
      "site": "00b4b450",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b028",
      "incomplete_value": true,
      "site": "00b4b028",
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
            "const:730:8"
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
      "definition_site": "00b4b3dc",
      "incomplete_value": true,
      "site": "00b4b3dc",
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
      "definition_site": "00b4afb4",
      "incomplete_value": true,
      "site": "00b4afb4",
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
      "00b4b3d8",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b3e4",
      "READ",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b400",
      "WRITE",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b3d8",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b3e4",
      "READ",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b400",
      "WRITE",
      [
        "storage",
        "01125b38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4afd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af9c.md#insn-00b4afd8) · [`00b4b024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af9c.md#insn-00b4b024) · [`00b4b028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af9c.md#insn-00b4b028)
- 新版 [`00b4b400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md#insn-00b4b400) · [`00b4b44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md#insn-00b4b44c) · [`00b4b450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b3c4.md#insn-00b4b450)

~~~diff
- 00b4afd8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4afd8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4afd8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:738:8"]]
- 00b4afd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b400 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b400 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b400 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b38:8"]]
+ 00b4b400 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4afd8 bytes bfe21c39
+ 00b4b400 bytes bfe22c39
- 00b4b024 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b024 ["INT_ADD", "register:40f0:8", ["const:b4b024:8", "const:4:8"]]
- 00b4b024 ["CALLIND", null, ["register:0:8"]]
+ 00b4b44c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b44c ["INT_ADD", "register:40f0:8", ["const:b4b44c:8", "const:4:8"]]
+ 00b4b44c ["CALLIND", null, ["register:0:8"]]
- 00b4b024 bytes 00013fd6
+ 00b4b44c bytes 00013fd6
- 00b4b028 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:730:8"]]
- 00b4b028 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b450 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
+ 00b4b450 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b028 bytes 9f9a03f9
+ 00b4b450 bytes 9f9a05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ebede08569e01c95771e7651554f1d2"></a>

### [`00b4b03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b03c.md) → [`00b4b464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md) _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4b4a4",
      "incomplete_value": true,
      "site": "00b4b4a4",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b07c",
      "incomplete_value": true,
      "site": "00b4b07c",
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
            "const:730:8"
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
      "definition_site": "00b4b480",
      "incomplete_value": true,
      "site": "00b4b480",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b058",
      "incomplete_value": true,
      "site": "00b4b058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b488",
      "incomplete_value": false,
      "site": "00b4b49c",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b060",
      "incomplete_value": false,
      "site": "00b4b074",
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
            "const:365:8"
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
      "00b4b478",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b488",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4b4a4",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b478",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b488",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b4a4",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b03c.md#insn-00b4b074) · [`00b4b07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b03c.md#insn-00b4b07c) · [`00b4b050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b03c.md#insn-00b4b050)
- 新版 [`00b4b49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md#insn-00b4b49c) · [`00b4b4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md#insn-00b4b4a4) · [`00b4b478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b464.md#insn-00b4b478)

~~~diff
- 00b4b074 ["INT_ADD", "register:40f0:8", ["const:b4b074:8", "const:4:8"]]
- 00b4b074 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b49c ["INT_ADD", "register:40f0:8", ["const:b4b49c:8", "const:4:8"]]
+ 00b4b49c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b074 bytes a73e0494
+ 00b4b49c bytes 9d3e0494
- 00b4b07c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:730:8"]]
- 00b4b07c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b4a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
+ 00b4b4a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b07c bytes 809a03f9
+ 00b4b4a4 bytes 809a05f9
- 00b4b050 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:730:8"]]
- 00b4b050 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b478 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
+ 00b4b478 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b050 bytes 819a43f9
+ 00b4b478 bytes 819a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a82f96e8eb58bdb2c880e57866a4089"></a>

### [`00b4b0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0e8.md) → [`00b4b510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md) _ZN8firebase4util13integer_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b550",
      "incomplete_value": true,
      "site": "00b4b550",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b128",
      "incomplete_value": true,
      "site": "00b4b128",
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
            "const:730:8"
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
      "definition_site": "00b4b52c",
      "incomplete_value": true,
      "site": "00b4b52c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b104",
      "incomplete_value": true,
      "site": "00b4b104",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b534",
      "incomplete_value": false,
      "site": "00b4b548",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b10c",
      "incomplete_value": false,
      "site": "00b4b120",
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
            "const:365:8"
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
      "00b4b524",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b534",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4b550",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b524",
      "READ",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b534",
      "PARAM",
      [
        "storage",
        "002a8432",
        null,
        "string"
      ]
    ],
    [
      "00b4b550",
      "WRITE",
      [
        "storage",
        "01125b30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0e8.md#insn-00b4b120) · [`00b4b128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0e8.md#insn-00b4b128) · [`00b4b0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0e8.md#insn-00b4b0fc)
- 新版 [`00b4b548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md#insn-00b4b548) · [`00b4b550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md#insn-00b4b550) · [`00b4b524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b510.md#insn-00b4b524)

~~~diff
- 00b4b120 ["INT_ADD", "register:40f0:8", ["const:b4b120:8", "const:4:8"]]
- 00b4b120 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b548 ["INT_ADD", "register:40f0:8", ["const:b4b548:8", "const:4:8"]]
+ 00b4b548 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b120 bytes 7c3e0494
+ 00b4b548 bytes 723e0494
- 00b4b128 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:730:8"]]
- 00b4b128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
+ 00b4b550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b128 bytes 809a03f9
+ 00b4b550 bytes 809a05f9
- 00b4b0fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:730:8"]]
- 00b4b0fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b524 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b30:8"]]
+ 00b4b524 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b0fc bytes 819a43f9
+ 00b4b524 bytes 819a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4106b8e99173a01addcf65971eba5df9"></a>

### [`00b4b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b194.md) → [`00b4b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b5e8",
      "incomplete_value": true,
      "site": "00b4b5e8",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b1c0",
      "incomplete_value": true,
      "site": "00b4b1c0",
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
            "const:758:8"
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
      "definition_site": "00b4b5d0",
      "incomplete_value": true,
      "site": "00b4b5d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b1a8",
      "incomplete_value": true,
      "site": "00b4b1a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b5dc",
      "incomplete_value": false,
      "site": "00b4b5e0",
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
            "const:a31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b1b4",
      "incomplete_value": false,
      "site": "00b4b1b8",
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
            "const:964:8"
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
      "00b4b5cc",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5dc",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b5e8",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b5cc",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5dc",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b5e8",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b194.md#insn-00b4b1b8) · [`00b4b1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b194.md#insn-00b4b1c0) · [`00b4b1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b194.md#insn-00b4b1a4)
- 新版 [`00b4b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md#insn-00b4b5e0) · [`00b4b5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md#insn-00b4b5e8) · [`00b4b5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5bc.md#insn-00b4b5cc)

~~~diff
- 00b4b1b8 ["INT_ADD", "register:40f0:8", ["const:b4b1b8:8", "const:4:8"]]
- 00b4b1b8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b5e0 ["INT_ADD", "register:40f0:8", ["const:b4b5e0:8", "const:4:8"]]
+ 00b4b5e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b1b8 bytes 563e0494
+ 00b4b5e0 bytes 4c3e0494
- 00b4b1c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b1c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b5e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b5e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b1c0 bytes 60ae03f9
+ 00b4b5e8 bytes 60ae05f9
- 00b4b1a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b1a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b5cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b5cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b1a4 bytes 68ae43f9
+ 00b4b5cc bytes 68ae45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e8235f7ae5612fcf88c42538bf17dc"></a>

### [`00b4b1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b1d4.md) → [`00b4b5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b628",
      "incomplete_value": true,
      "site": "00b4b628",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b200",
      "incomplete_value": true,
      "site": "00b4b200",
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
            "const:758:8"
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
      "definition_site": "00b4b610",
      "incomplete_value": true,
      "site": "00b4b610",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b1e8",
      "incomplete_value": true,
      "site": "00b4b1e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b618",
      "incomplete_value": false,
      "site": "00b4b620",
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
            "const:a31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b1f0",
      "incomplete_value": false,
      "site": "00b4b1f8",
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
            "const:964:8"
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
      "00b4b60c",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b618",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b628",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b60c",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b618",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b628",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b1d4.md#insn-00b4b1f8) · [`00b4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b1d4.md#insn-00b4b200) · [`00b4b1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b1d4.md#insn-00b4b1e4)
- 新版 [`00b4b620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md#insn-00b4b620) · [`00b4b628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md#insn-00b4b628) · [`00b4b60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b5fc.md#insn-00b4b60c)

~~~diff
- 00b4b1f8 ["INT_ADD", "register:40f0:8", ["const:b4b1f8:8", "const:4:8"]]
- 00b4b1f8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b620 ["INT_ADD", "register:40f0:8", ["const:b4b620:8", "const:4:8"]]
+ 00b4b620 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b1f8 bytes 463e0494
+ 00b4b620 bytes 3c3e0494
- 00b4b200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b628 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b200 bytes 60ae03f9
+ 00b4b628 bytes 60ae05f9
- 00b4b1e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b1e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b60c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b60c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b1e4 bytes 68ae43f9
+ 00b4b60c bytes 68ae45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cface3234efe6a09b217072df17c916"></a>

### [`00b4b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b214.md) → [`00b4b63c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b66c",
      "incomplete_value": true,
      "site": "00b4b66c",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b244",
      "incomplete_value": true,
      "site": "00b4b244",
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
            "const:758:8"
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
      "definition_site": "00b4b650",
      "incomplete_value": true,
      "site": "00b4b650",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b228",
      "incomplete_value": true,
      "site": "00b4b228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b65c",
      "incomplete_value": false,
      "site": "00b4b664",
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
            "const:a31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b234",
      "incomplete_value": false,
      "site": "00b4b23c",
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
            "const:964:8"
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
      "00b4b64c",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b65c",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b66c",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b64c",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b65c",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b66c",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b23c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b214.md#insn-00b4b23c) · [`00b4b244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b214.md#insn-00b4b244) · [`00b4b224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b214.md#insn-00b4b224)
- 新版 [`00b4b664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md#insn-00b4b664) · [`00b4b66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md#insn-00b4b66c) · [`00b4b64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b63c.md#insn-00b4b64c)

~~~diff
- 00b4b23c ["INT_ADD", "register:40f0:8", ["const:b4b23c:8", "const:4:8"]]
- 00b4b23c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b664 ["INT_ADD", "register:40f0:8", ["const:b4b664:8", "const:4:8"]]
+ 00b4b664 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b23c bytes 353e0494
+ 00b4b664 bytes 2b3e0494
- 00b4b244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b66c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b66c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b244 bytes 60ae03f9
+ 00b4b66c bytes 60ae05f9
- 00b4b224 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b224 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b64c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b64c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b224 bytes 68ae43f9
+ 00b4b64c bytes 68ae45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9fdcd36a1af9382b326bbe76df6b3d1"></a>

### [`00b4b258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b258.md) → [`00b4b680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b6b0",
      "incomplete_value": true,
      "site": "00b4b6b0",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b288",
      "incomplete_value": true,
      "site": "00b4b288",
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
            "const:758:8"
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
      "definition_site": "00b4b694",
      "incomplete_value": true,
      "site": "00b4b694",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b26c",
      "incomplete_value": true,
      "site": "00b4b26c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b69c",
      "incomplete_value": false,
      "site": "00b4b6a8",
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
            "const:a31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b274",
      "incomplete_value": false,
      "site": "00b4b280",
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
            "const:964:8"
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
      "00b4b690",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b69c",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b6b0",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b690",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b69c",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b6b0",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b258.md#insn-00b4b280) · [`00b4b288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b258.md#insn-00b4b288) · [`00b4b268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b258.md#insn-00b4b268)
- 新版 [`00b4b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md#insn-00b4b6a8) · [`00b4b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md#insn-00b4b6b0) · [`00b4b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b680.md#insn-00b4b690)

~~~diff
- 00b4b280 ["INT_ADD", "register:40f0:8", ["const:b4b280:8", "const:4:8"]]
- 00b4b280 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b6a8 ["INT_ADD", "register:40f0:8", ["const:b4b6a8:8", "const:4:8"]]
+ 00b4b6a8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b280 bytes 243e0494
+ 00b4b6a8 bytes 1a3e0494
- 00b4b288 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b6b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b6b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b288 bytes 60ae03f9
+ 00b4b6b0 bytes 60ae05f9
- 00b4b268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
- 00b4b268 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b690 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b58:8"]]
+ 00b4b690 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b268 bytes 68ae43f9
+ 00b4b690 bytes 68ae45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86e4c4d83e31623e3331404cb6fdc13a"></a>

### [`00b4b2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b2a8.md) → [`00b4b6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md) _ZN8firebase4util6intent15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b758",
      "incomplete_value": true,
      "site": "00b4b758",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b330",
      "incomplete_value": true,
      "site": "00b4b330",
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
            "const:760:8"
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
      "definition_site": "00b4b704",
      "incomplete_value": true,
      "site": "00b4b710",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b2dc",
      "incomplete_value": true,
      "site": "00b4b2e8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:758:8"
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
      "00b4b6e4",
      "READ",
      [
        "storage",
        "01125760",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b704",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b758",
      "WRITE",
      [
        "storage",
        "01125760",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b6e4",
      "READ",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b704",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b758",
      "WRITE",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b2a8.md#insn-00b4b2e8) · [`00b4b330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b2a8.md#insn-00b4b330) · [`00b4b2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b2a8.md#insn-00b4b2bc)
- 新版 [`00b4b710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md#insn-00b4b710) · [`00b4b758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md#insn-00b4b758) · [`00b4b6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b6d0.md#insn-00b4b6e4)

~~~diff
- 00b4b2e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b2e8 ["INT_ADD", "register:40f0:8", ["const:b4b2e8:8", "const:4:8"]]
- 00b4b2e8 ["CALLIND", null, ["register:0:8"]]
+ 00b4b710 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b710 ["INT_ADD", "register:40f0:8", ["const:b4b710:8", "const:4:8"]]
+ 00b4b710 ["CALLIND", null, ["register:0:8"]]
- 00b4b2e8 bytes 00013fd6
+ 00b4b710 bytes 00013fd6
- 00b4b330 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b330 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:760:8"]]
- 00b4b330 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b758 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b758 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b60:8"]]
+ 00b4b758 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b330 bytes a0821d39
+ 00b4b758 bytes a0822d39
- 00b4b2bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:760:8"]]
- 00b4b2bc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4b2bc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4b6e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b60:8"]]
+ 00b4b6e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b6e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4b2bc bytes a8825d39
+ 00b4b6e4 bytes a8826d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac833826941a75567537b1fe6ba8b2d8"></a>

### [`00b4b344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b344.md) → [`00b4b76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md) _ZN8firebase4util6intent12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b7a8",
      "incomplete_value": true,
      "site": "00b4b7a8",
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
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b380",
      "incomplete_value": true,
      "site": "00b4b380",
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
            "const:760:8"
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
      "definition_site": "00b4b7f8",
      "incomplete_value": true,
      "site": "00b4b7f8",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b3d0",
      "incomplete_value": true,
      "site": "00b4b3d0",
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
            "const:758:8"
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
      "definition_site": "00b4b784",
      "incomplete_value": true,
      "site": "00b4b784",
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
      "definition_site": "00b4b35c",
      "incomplete_value": true,
      "site": "00b4b35c",
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
      "00b4b780",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b78c",
      "READ",
      [
        "storage",
        "01125760",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b7a8",
      "WRITE",
      [
        "storage",
        "01125760",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b780",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b78c",
      "READ",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b7a8",
      "WRITE",
      [
        "storage",
        "01125b60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b344.md#insn-00b4b380) · [`00b4b3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b344.md#insn-00b4b3cc) · [`00b4b3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b344.md#insn-00b4b3d0)
- 新版 [`00b4b7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md#insn-00b4b7a8) · [`00b4b7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md#insn-00b4b7f4) · [`00b4b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b76c.md#insn-00b4b7f8)

~~~diff
- 00b4b380 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b380 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b380 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:760:8"]]
- 00b4b380 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b7a8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b7a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b7a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b60:8"]]
+ 00b4b7a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b380 bytes bf821d39
+ 00b4b7a8 bytes bf822d39
- 00b4b3cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b3cc ["INT_ADD", "register:40f0:8", ["const:b4b3cc:8", "const:4:8"]]
- 00b4b3cc ["CALLIND", null, ["register:0:8"]]
+ 00b4b7f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b7f4 ["INT_ADD", "register:40f0:8", ["const:b4b7f4:8", "const:4:8"]]
+ 00b4b7f4 ["CALLIND", null, ["register:0:8"]]
- 00b4b3cc bytes 00013fd6
+ 00b4b7f4 bytes 00013fd6
- 00b4b3d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b4b3d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b3d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b7f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
+ 00b4b7f8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b7f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b3d0 bytes 9fae03f9
+ 00b4b7f8 bytes 9fae05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8da23f8122dc7b88f304dc4223b37943"></a>

### [`00b4b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b3e4.md) → [`00b4b80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md) _ZN8firebase4util6intent14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4b84c",
      "incomplete_value": true,
      "site": "00b4b84c",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b424",
      "incomplete_value": true,
      "site": "00b4b424",
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
            "const:758:8"
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
      "definition_site": "00b4b828",
      "incomplete_value": true,
      "site": "00b4b828",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b400",
      "incomplete_value": true,
      "site": "00b4b400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b830",
      "incomplete_value": false,
      "site": "00b4b844",
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
            "const:a31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b408",
      "incomplete_value": false,
      "site": "00b4b41c",
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
            "const:964:8"
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
      "00b4b820",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b830",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b84c",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b820",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b830",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b84c",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b3e4.md#insn-00b4b41c) · [`00b4b424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b3e4.md#insn-00b4b424) · [`00b4b3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b3e4.md#insn-00b4b3f8)
- 新版 [`00b4b844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md#insn-00b4b844) · [`00b4b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md#insn-00b4b84c) · [`00b4b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b80c.md#insn-00b4b820)

~~~diff
- 00b4b41c ["INT_ADD", "register:40f0:8", ["const:b4b41c:8", "const:4:8"]]
- 00b4b41c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b844 ["INT_ADD", "register:40f0:8", ["const:b4b844:8", "const:4:8"]]
+ 00b4b844 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b41c bytes bd3d0494
+ 00b4b844 bytes b33d0494
- 00b4b424 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b4b424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b84c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
+ 00b4b84c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b424 bytes 80ae03f9
+ 00b4b84c bytes 80ae05f9
- 00b4b3f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b4b3f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b820 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
+ 00b4b820 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b3f8 bytes 81ae43f9
+ 00b4b820 bytes 81ae45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b71a490f0a9ecd8407e2f925916db2bb"></a>

### [`00b4b454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b454.md) → [`00b4b87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md) _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b130.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b530.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4b898",
      "incomplete_value": false,
      "site": "00b4b89c",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b470",
      "incomplete_value": false,
      "site": "00b4b474",
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
            "const:29a:8"
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
      "definition_site": "00b4b8a8",
      "incomplete_value": true,
      "site": "00b4b8b4",
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
      "definition_site": "00b4b480",
      "incomplete_value": true,
      "site": "00b4b48c",
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
      "00b4b898",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4b8a8",
      "DATA",
      [
        "storage",
        "01125768",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b898",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4b8a8",
      "DATA",
      [
        "storage",
        "01125b68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b454.md#insn-00b4b474) · [`00b4b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b454.md#insn-00b4b470) · [`00b4b47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b454.md#insn-00b4b47c)
- 新版 [`00b4b89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md#insn-00b4b89c) · [`00b4b898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md#insn-00b4b898) · [`00b4b8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b87c.md#insn-00b4b8a4)

~~~diff
- 00b4b474 ["INT_ADD", "register:40f0:8", ["const:b4b474:8", "const:4:8"]]
- 00b4b474 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4b89c ["INT_ADD", "register:40f0:8", ["const:b4b89c:8", "const:4:8"]]
+ 00b4b89c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4b474 bytes e33d0494
+ 00b4b89c bytes d93d0494
- 00b4b470 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4b470 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b470 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b470 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b898 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4b898 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b898 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b898 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b470 bytes 00680a91
+ 00b4b898 bytes 009c0d91
- 00b4b47c ["COPY", "tmp:0:8", ["const:768:8"]]
- 00b4b47c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b47c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b47c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b8a4 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00b4b8a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b8a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b8a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b47c bytes 08a11d91
+ 00b4b8a4 bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0594e97889cf40fe71821086d68f325"></a>

### [`00b4b490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b490.md) → [`00b4b8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md) _ZN8firebase4util6intent13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b8f8",
      "incomplete_value": true,
      "site": "00b4b8f8",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b4d0",
      "incomplete_value": true,
      "site": "00b4b4d0",
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
            "const:758:8"
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
      "definition_site": "00b4b8d4",
      "incomplete_value": true,
      "site": "00b4b8d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b4ac",
      "incomplete_value": true,
      "site": "00b4b4ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b8dc",
      "incomplete_value": false,
      "site": "00b4b8f0",
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
            "const:a31:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b4b4",
      "incomplete_value": false,
      "site": "00b4b4c8",
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
            "const:964:8"
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
      "00b4b8cc",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b8dc",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b8f8",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b8cc",
      "READ",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b8dc",
      "PARAM",
      [
        "storage",
        "002a2a31",
        null,
        "string"
      ]
    ],
    [
      "00b4b8f8",
      "WRITE",
      [
        "storage",
        "01125b58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b490.md#insn-00b4b4c8) · [`00b4b4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b490.md#insn-00b4b4d0) · [`00b4b4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b490.md#insn-00b4b4a4)
- 新版 [`00b4b8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md#insn-00b4b8f0) · [`00b4b8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md#insn-00b4b8f8) · [`00b4b8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b8b8.md#insn-00b4b8cc)

~~~diff
- 00b4b4c8 ["INT_ADD", "register:40f0:8", ["const:b4b4c8:8", "const:4:8"]]
- 00b4b4c8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b8f0 ["INT_ADD", "register:40f0:8", ["const:b4b8f0:8", "const:4:8"]]
+ 00b4b8f0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b4c8 bytes 923d0494
+ 00b4b8f0 bytes 883d0494
- 00b4b4d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b4b4d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b8f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
+ 00b4b8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b4d0 bytes 80ae03f9
+ 00b4b8f8 bytes 80ae05f9
- 00b4b4a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00b4b4a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b8cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
+ 00b4b8cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b4a4 bytes 81ae43f9
+ 00b4b8cc bytes 81ae45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f711229b6f9691e059dac4eca878d8"></a>

### [`00b4b500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b500.md) → [`00b4b928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md) _ZN8firebase4util6intent10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4b944",
      "incomplete_value": false,
      "site": "00b4b948",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b51c",
      "incomplete_value": false,
      "site": "00b4b520",
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
            "const:451:8"
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
      "definition_site": "00b4b954",
      "incomplete_value": true,
      "site": "00b4b960",
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
      "definition_site": "00b4b52c",
      "incomplete_value": true,
      "site": "00b4b538",
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
      "00b4b944",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4b954",
      "DATA",
      [
        "storage",
        "01125790",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b944",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4b954",
      "DATA",
      [
        "storage",
        "01125b90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b500.md#insn-00b4b520) · [`00b4b51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b500.md#insn-00b4b51c) · [`00b4b528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b500.md#insn-00b4b528)
- 新版 [`00b4b948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md#insn-00b4b948) · [`00b4b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md#insn-00b4b944) · [`00b4b950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b928.md#insn-00b4b950)

~~~diff
- 00b4b520 ["INT_ADD", "register:40f0:8", ["const:b4b520:8", "const:4:8"]]
- 00b4b520 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4b948 ["INT_ADD", "register:40f0:8", ["const:b4b948:8", "const:4:8"]]
+ 00b4b948 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4b520 bytes b83d0494
+ 00b4b948 bytes ae3d0494
- 00b4b51c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4b51c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b51c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b51c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b944 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4b944 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b944 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b944 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b51c bytes 00441191
+ 00b4b944 bytes 00781491
- 00b4b528 ["COPY", "tmp:0:8", ["const:790:8"]]
- 00b4b528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b950 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 00b4b950 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b950 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b950 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b528 bytes 08411e91
+ 00b4b950 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4eca5d1c63d13432651f812c85ad41e"></a>

### [`00b4b53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b53c.md) → [`00b4b964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b990",
      "incomplete_value": true,
      "site": "00b4b990",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b568",
      "incomplete_value": true,
      "site": "00b4b568",
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
            "const:798:8"
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
      "definition_site": "00b4b978",
      "incomplete_value": true,
      "site": "00b4b978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b550",
      "incomplete_value": true,
      "site": "00b4b550",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b984",
      "incomplete_value": false,
      "site": "00b4b988",
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
            "const:976:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b55c",
      "incomplete_value": false,
      "site": "00b4b560",
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
            "const:8a9:8"
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
      "00b4b974",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b984",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4b990",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b974",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b984",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4b990",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b53c.md#insn-00b4b560) · [`00b4b568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b53c.md#insn-00b4b568) · [`00b4b54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b53c.md#insn-00b4b54c)
- 新版 [`00b4b988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md#insn-00b4b988) · [`00b4b990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md#insn-00b4b990) · [`00b4b974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b964.md#insn-00b4b974)

~~~diff
- 00b4b560 ["INT_ADD", "register:40f0:8", ["const:b4b560:8", "const:4:8"]]
- 00b4b560 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b988 ["INT_ADD", "register:40f0:8", ["const:b4b988:8", "const:4:8"]]
+ 00b4b988 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b560 bytes 6c3d0494
+ 00b4b988 bytes 623d0494
- 00b4b568 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b568 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4b990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b568 bytes 60ce03f9
+ 00b4b990 bytes 60ce05f9
- 00b4b54c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b54c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4b974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b54c bytes 68ce43f9
+ 00b4b974 bytes 68ce45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81240f232c7b50dad6b750ec7c194f37"></a>

### [`00b4b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b57c.md) → [`00b4b9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4b9d0",
      "incomplete_value": true,
      "site": "00b4b9d0",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b5a8",
      "incomplete_value": true,
      "site": "00b4b5a8",
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
            "const:798:8"
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
      "definition_site": "00b4b9b8",
      "incomplete_value": true,
      "site": "00b4b9b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b590",
      "incomplete_value": true,
      "site": "00b4b590",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b9c0",
      "incomplete_value": false,
      "site": "00b4b9c8",
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
            "const:976:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b598",
      "incomplete_value": false,
      "site": "00b4b5a0",
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
            "const:8a9:8"
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
      "00b4b9b4",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b9c0",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4b9d0",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b9b4",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b9c0",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4b9d0",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b57c.md#insn-00b4b5a0) · [`00b4b5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b57c.md#insn-00b4b5a8) · [`00b4b58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b57c.md#insn-00b4b58c)
- 新版 [`00b4b9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md#insn-00b4b9c8) · [`00b4b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md#insn-00b4b9d0) · [`00b4b9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9a4.md#insn-00b4b9b4)

~~~diff
- 00b4b5a0 ["INT_ADD", "register:40f0:8", ["const:b4b5a0:8", "const:4:8"]]
- 00b4b5a0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4b9c8 ["INT_ADD", "register:40f0:8", ["const:b4b9c8:8", "const:4:8"]]
+ 00b4b9c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b5a0 bytes 5c3d0494
+ 00b4b9c8 bytes 523d0494
- 00b4b5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b9d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4b9d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b5a8 bytes 60ce03f9
+ 00b4b9d0 bytes 60ce05f9
- 00b4b58c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b58c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b9b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4b9b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b58c bytes 68ce43f9
+ 00b4b9b4 bytes 68ce45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e89b339b358dfd6e0aa783f57de74324"></a>

### [`00b4b5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b5bc.md) → [`00b4b9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4ba14",
      "incomplete_value": true,
      "site": "00b4ba14",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b5ec",
      "incomplete_value": true,
      "site": "00b4b5ec",
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
            "const:798:8"
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
      "definition_site": "00b4b9f8",
      "incomplete_value": true,
      "site": "00b4b9f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b5d0",
      "incomplete_value": true,
      "site": "00b4b5d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ba04",
      "incomplete_value": false,
      "site": "00b4ba0c",
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
            "const:976:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b5dc",
      "incomplete_value": false,
      "site": "00b4b5e4",
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
            "const:8a9:8"
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
      "00b4b9f4",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba04",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4ba14",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b9f4",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba04",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4ba14",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b5bc.md#insn-00b4b5e4) · [`00b4b5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b5bc.md#insn-00b4b5ec) · [`00b4b5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b5bc.md#insn-00b4b5cc)
- 新版 [`00b4ba0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md#insn-00b4ba0c) · [`00b4ba14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md#insn-00b4ba14) · [`00b4b9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b9e4.md#insn-00b4b9f4)

~~~diff
- 00b4b5e4 ["INT_ADD", "register:40f0:8", ["const:b4b5e4:8", "const:4:8"]]
- 00b4b5e4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ba0c ["INT_ADD", "register:40f0:8", ["const:b4ba0c:8", "const:4:8"]]
+ 00b4ba0c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b5e4 bytes 4b3d0494
+ 00b4ba0c bytes 413d0494
- 00b4b5ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ba14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4ba14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b5ec bytes 60ce03f9
+ 00b4ba14 bytes 60ce05f9
- 00b4b5cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b5cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b9f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4b9f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b5cc bytes 68ce43f9
+ 00b4b9f4 bytes 68ce45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a0b1db8d056ebcac3c7b5303207b143"></a>

### [`00b4b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b600.md) → [`00b4ba28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4ba58",
      "incomplete_value": true,
      "site": "00b4ba58",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b630",
      "incomplete_value": true,
      "site": "00b4b630",
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
            "const:798:8"
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
      "definition_site": "00b4ba3c",
      "incomplete_value": true,
      "site": "00b4ba3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b614",
      "incomplete_value": true,
      "site": "00b4b614",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4ba44",
      "incomplete_value": false,
      "site": "00b4ba50",
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
            "const:976:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b61c",
      "incomplete_value": false,
      "site": "00b4b628",
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
            "const:8a9:8"
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
      "00b4ba38",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba44",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4ba58",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba38",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba44",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4ba58",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b600.md#insn-00b4b628) · [`00b4b630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b600.md#insn-00b4b630) · [`00b4b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b600.md#insn-00b4b610)
- 新版 [`00b4ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md#insn-00b4ba50) · [`00b4ba58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md#insn-00b4ba58) · [`00b4ba38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba28.md#insn-00b4ba38)

~~~diff
- 00b4b628 ["INT_ADD", "register:40f0:8", ["const:b4b628:8", "const:4:8"]]
- 00b4b628 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ba50 ["INT_ADD", "register:40f0:8", ["const:b4ba50:8", "const:4:8"]]
+ 00b4ba50 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b628 bytes 3a3d0494
+ 00b4ba50 bytes 303d0494
- 00b4b630 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ba58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4ba58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b630 bytes 60ce03f9
+ 00b4ba58 bytes 60ce05f9
- 00b4b610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
- 00b4b610 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ba38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b98:8"]]
+ 00b4ba38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b610 bytes 68ce43f9
+ 00b4ba38 bytes 68ce45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d62ff10d97ea8446e126fa6182d83102"></a>

### [`00b4b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b650.md) → [`00b4ba78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md) _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4bb00",
      "incomplete_value": true,
      "site": "00b4bb00",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b6d8",
      "incomplete_value": true,
      "site": "00b4b6d8",
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
            "const:7a0:8"
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
      "definition_site": "00b4baac",
      "incomplete_value": true,
      "site": "00b4bab8",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b684",
      "incomplete_value": true,
      "site": "00b4b690",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:798:8"
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
      "00b4ba8c",
      "READ",
      [
        "storage",
        "011257a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4baac",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb00",
      "WRITE",
      [
        "storage",
        "011257a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba8c",
      "READ",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4baac",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb00",
      "WRITE",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b650.md#insn-00b4b690) · [`00b4b6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b650.md#insn-00b4b6d8) · [`00b4b664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b650.md#insn-00b4b664)
- 新版 [`00b4bab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md#insn-00b4bab8) · [`00b4bb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md#insn-00b4bb00) · [`00b4ba8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4ba78.md#insn-00b4ba8c)

~~~diff
- 00b4b690 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b690 ["INT_ADD", "register:40f0:8", ["const:b4b690:8", "const:4:8"]]
- 00b4b690 ["CALLIND", null, ["register:0:8"]]
+ 00b4bab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bab8 ["INT_ADD", "register:40f0:8", ["const:b4bab8:8", "const:4:8"]]
+ 00b4bab8 ["CALLIND", null, ["register:0:8"]]
- 00b4b690 bytes 00013fd6
+ 00b4bab8 bytes 00013fd6
- 00b4b6d8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b6d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7a0:8"]]
- 00b4b6d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4bb00 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4bb00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ba0:8"]]
+ 00b4bb00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b6d8 bytes a0821e39
+ 00b4bb00 bytes a0822e39
- 00b4b664 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a0:8"]]
- 00b4b664 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4b664 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4ba8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ba0:8"]]
+ 00b4ba8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ba8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4b664 bytes a8825e39
+ 00b4ba8c bytes a8826e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f76629c0bcf66e600e06bc72cdc2b3"></a>

### [`00b4b6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b6ec.md) → [`00b4bb14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md) _ZN8firebase4util8iterable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4bb50",
      "incomplete_value": true,
      "site": "00b4bb50",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b728",
      "incomplete_value": true,
      "site": "00b4b728",
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
            "const:7a0:8"
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
      "definition_site": "00b4bba0",
      "incomplete_value": true,
      "site": "00b4bba0",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b778",
      "incomplete_value": true,
      "site": "00b4b778",
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
            "const:798:8"
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
      "definition_site": "00b4bb2c",
      "incomplete_value": true,
      "site": "00b4bb2c",
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
      "definition_site": "00b4b704",
      "incomplete_value": true,
      "site": "00b4b704",
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
      "00b4bb28",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb34",
      "READ",
      [
        "storage",
        "011257a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bb50",
      "WRITE",
      [
        "storage",
        "011257a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bb28",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb34",
      "READ",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bb50",
      "WRITE",
      [
        "storage",
        "01125ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b6ec.md#insn-00b4b728) · [`00b4b774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b6ec.md#insn-00b4b774) · [`00b4b778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b6ec.md#insn-00b4b778)
- 新版 [`00b4bb50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md#insn-00b4bb50) · [`00b4bb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md#insn-00b4bb9c) · [`00b4bba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bb14.md#insn-00b4bba0)

~~~diff
- 00b4b728 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b728 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b728 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7a0:8"]]
- 00b4b728 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4bb50 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4bb50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4bb50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ba0:8"]]
+ 00b4bb50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b728 bytes bf821e39
+ 00b4bb50 bytes bf822e39
- 00b4b774 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b774 ["INT_ADD", "register:40f0:8", ["const:b4b774:8", "const:4:8"]]
- 00b4b774 ["CALLIND", null, ["register:0:8"]]
+ 00b4bb9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bb9c ["INT_ADD", "register:40f0:8", ["const:b4bb9c:8", "const:4:8"]]
+ 00b4bb9c ["CALLIND", null, ["register:0:8"]]
- 00b4b774 bytes 00013fd6
+ 00b4bb9c bytes 00013fd6
- 00b4b778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00b4b778 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b778 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
+ 00b4bba0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b778 bytes 9fce03f9
+ 00b4bba0 bytes 9fce05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a37b404ffd1b165842b4d31c28413593"></a>

### [`00b4b78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b78c.md) → [`00b4bbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md) _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4bbf4",
      "incomplete_value": true,
      "site": "00b4bbf4",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b7cc",
      "incomplete_value": true,
      "site": "00b4b7cc",
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
            "const:798:8"
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
      "definition_site": "00b4bbd0",
      "incomplete_value": true,
      "site": "00b4bbd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b7a8",
      "incomplete_value": true,
      "site": "00b4b7a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bbd8",
      "incomplete_value": false,
      "site": "00b4bbec",
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
            "const:976:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b7b0",
      "incomplete_value": false,
      "site": "00b4b7c4",
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
            "const:8a9:8"
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
      "00b4bbc8",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbd8",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4bbf4",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bbc8",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbd8",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4bbf4",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b78c.md#insn-00b4b7c4) · [`00b4b7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b78c.md#insn-00b4b7cc) · [`00b4b7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b78c.md#insn-00b4b7a0)
- 新版 [`00b4bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md#insn-00b4bbec) · [`00b4bbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md#insn-00b4bbf4) · [`00b4bbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bbb4.md#insn-00b4bbc8)

~~~diff
- 00b4b7c4 ["INT_ADD", "register:40f0:8", ["const:b4b7c4:8", "const:4:8"]]
- 00b4b7c4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bbec ["INT_ADD", "register:40f0:8", ["const:b4bbec:8", "const:4:8"]]
+ 00b4bbec ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b7c4 bytes d33c0494
+ 00b4bbec bytes c93c0494
- 00b4b7cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00b4b7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bbf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
+ 00b4bbf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b7cc bytes 80ce03f9
+ 00b4bbf4 bytes 80ce05f9
- 00b4b7a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00b4b7a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bbc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
+ 00b4bbc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b7a0 bytes 81ce43f9
+ 00b4bbc8 bytes 81ce45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c11b1b14ea65f2f18b4f6c3791199e1"></a>

### [`00b4b7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b7fc.md) → [`00b4bc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md) _ZN8firebase4util8iterable11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4bc40",
      "incomplete_value": false,
      "site": "00b4bc44",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b818",
      "incomplete_value": false,
      "site": "00b4b81c",
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
            "const:29a:8"
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
      "definition_site": "00b4bc50",
      "incomplete_value": true,
      "site": "00b4bc5c",
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
      "definition_site": "00b4b828",
      "incomplete_value": true,
      "site": "00b4b834",
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
      "00b4bc40",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4bc50",
      "DATA",
      [
        "storage",
        "011257a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4bc40",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4bc50",
      "DATA",
      [
        "storage",
        "01125ba8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b7fc.md#insn-00b4b81c) · [`00b4b818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b7fc.md#insn-00b4b818) · [`00b4b824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b7fc.md#insn-00b4b824)
- 新版 [`00b4bc44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md#insn-00b4bc44) · [`00b4bc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md#insn-00b4bc40) · [`00b4bc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc24.md#insn-00b4bc4c)

~~~diff
- 00b4b81c ["INT_ADD", "register:40f0:8", ["const:b4b81c:8", "const:4:8"]]
- 00b4b81c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4bc44 ["INT_ADD", "register:40f0:8", ["const:b4bc44:8", "const:4:8"]]
+ 00b4bc44 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4b81c bytes f93c0494
+ 00b4bc44 bytes ef3c0494
- 00b4b818 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4b818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bc40 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4bc40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bc40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bc40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b818 bytes 00680a91
+ 00b4bc40 bytes 009c0d91
- 00b4b824 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 00b4b824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4bc4c ["COPY", "tmp:0:8", ["const:ba8:8"]]
+ 00b4bc4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bc4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bc4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b824 bytes 08a11e91
+ 00b4bc4c bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc8156acced2d93f4e0bafb82df8906"></a>

### [`00b4b838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b838.md) → [`00b4bc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md) _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4bca0",
      "incomplete_value": true,
      "site": "00b4bca0",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b878",
      "incomplete_value": true,
      "site": "00b4b878",
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
            "const:798:8"
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
      "definition_site": "00b4bc7c",
      "incomplete_value": true,
      "site": "00b4bc7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b854",
      "incomplete_value": true,
      "site": "00b4b854",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bc84",
      "incomplete_value": false,
      "site": "00b4bc98",
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
            "const:976:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b85c",
      "incomplete_value": false,
      "site": "00b4b870",
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
            "const:8a9:8"
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
      "00b4bc74",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc84",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4bca0",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bc74",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc84",
      "PARAM",
      [
        "storage",
        "0029f976",
        null,
        "string"
      ]
    ],
    [
      "00b4bca0",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b838.md#insn-00b4b870) · [`00b4b878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b838.md#insn-00b4b878) · [`00b4b84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b838.md#insn-00b4b84c)
- 新版 [`00b4bc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md#insn-00b4bc98) · [`00b4bca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md#insn-00b4bca0) · [`00b4bc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bc60.md#insn-00b4bc74)

~~~diff
- 00b4b870 ["INT_ADD", "register:40f0:8", ["const:b4b870:8", "const:4:8"]]
- 00b4b870 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bc98 ["INT_ADD", "register:40f0:8", ["const:b4bc98:8", "const:4:8"]]
+ 00b4bc98 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b870 bytes a83c0494
+ 00b4bc98 bytes 9e3c0494
- 00b4b878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00b4b878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
+ 00b4bca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b878 bytes 80ce03f9
+ 00b4bca0 bytes 80ce05f9
- 00b4b84c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
- 00b4b84c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bc74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b98:8"]]
+ 00b4bc74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b84c bytes 81ce43f9
+ 00b4bc74 bytes 81ce45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58df640bed32477031ec8feb9fca98ed"></a>

### [`00b4b8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8a8.md) → [`00b4bcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md) _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4bcec",
      "incomplete_value": false,
      "site": "00b4bcf0",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b8c4",
      "incomplete_value": false,
      "site": "00b4b8c8",
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
            "const:451:8"
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
      "definition_site": "00b4bcfc",
      "incomplete_value": true,
      "site": "00b4bd08",
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
      "definition_site": "00b4b8d4",
      "incomplete_value": true,
      "site": "00b4b8e0",
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
      "00b4bcec",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4bcfc",
      "DATA",
      [
        "storage",
        "011257b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4bcec",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4bcfc",
      "DATA",
      [
        "storage",
        "01125bb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8a8.md#insn-00b4b8c8) · [`00b4b8c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8a8.md#insn-00b4b8c4) · [`00b4b8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8a8.md#insn-00b4b8d0)
- 新版 [`00b4bcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md#insn-00b4bcf0) · [`00b4bcec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md#insn-00b4bcec) · [`00b4bcf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bcd0.md#insn-00b4bcf8)

~~~diff
- 00b4b8c8 ["INT_ADD", "register:40f0:8", ["const:b4b8c8:8", "const:4:8"]]
- 00b4b8c8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4bcf0 ["INT_ADD", "register:40f0:8", ["const:b4bcf0:8", "const:4:8"]]
+ 00b4bcf0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4b8c8 bytes ce3c0494
+ 00b4bcf0 bytes c43c0494
- 00b4b8c4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4b8c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b8c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b8c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bcec ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4bcec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bcec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bcec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b8c4 bytes 00441191
+ 00b4bcec bytes 00781491
- 00b4b8d0 ["COPY", "tmp:0:8", ["const:7b0:8"]]
- 00b4b8d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b8d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b8d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4bcf8 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00b4bcf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bcf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bcf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b8d0 bytes 08c11e91
+ 00b4bcf8 bytes 08c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56e5ac94b34169461a6d8da2215ec654"></a>

### [`00b4b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8e4.md) → [`00b4bd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4bd38",
      "incomplete_value": true,
      "site": "00b4bd38",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b910",
      "incomplete_value": true,
      "site": "00b4b910",
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
            "const:7b8:8"
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
      "definition_site": "00b4bd20",
      "incomplete_value": true,
      "site": "00b4bd20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b8f8",
      "incomplete_value": true,
      "site": "00b4b8f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bd2c",
      "incomplete_value": false,
      "site": "00b4bd30",
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
            "const:157:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b904",
      "incomplete_value": false,
      "site": "00b4b908",
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
            "const:7b:8"
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
      "00b4bd1c",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd2c",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4bd38",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd1c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd2c",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4bd38",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8e4.md#insn-00b4b908) · [`00b4b910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8e4.md#insn-00b4b910) · [`00b4b8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8e4.md#insn-00b4b8f4)
- 新版 [`00b4bd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md#insn-00b4bd30) · [`00b4bd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md#insn-00b4bd38) · [`00b4bd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd0c.md#insn-00b4bd1c)

~~~diff
- 00b4b908 ["INT_ADD", "register:40f0:8", ["const:b4b908:8", "const:4:8"]]
- 00b4b908 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bd30 ["INT_ADD", "register:40f0:8", ["const:b4bd30:8", "const:4:8"]]
+ 00b4bd30 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b908 bytes 823c0494
+ 00b4bd30 bytes 783c0494
- 00b4b910 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bd38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bd38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b910 bytes 60de03f9
+ 00b4bd38 bytes 60de05f9
- 00b4b8f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b8f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bd1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bd1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b8f4 bytes 68de43f9
+ 00b4bd1c bytes 68de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-651596a0401743172915f7f28e895496"></a>

### [`00b4b924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b924.md) → [`00b4bd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4bd78",
      "incomplete_value": true,
      "site": "00b4bd78",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b950",
      "incomplete_value": true,
      "site": "00b4b950",
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
            "const:7b8:8"
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
      "definition_site": "00b4bd60",
      "incomplete_value": true,
      "site": "00b4bd60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b938",
      "incomplete_value": true,
      "site": "00b4b938",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bd68",
      "incomplete_value": false,
      "site": "00b4bd70",
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
            "const:157:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b940",
      "incomplete_value": false,
      "site": "00b4b948",
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
            "const:7b:8"
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
      "00b4bd5c",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd68",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4bd78",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd5c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd68",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4bd78",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b924.md#insn-00b4b948) · [`00b4b950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b924.md#insn-00b4b950) · [`00b4b934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b924.md#insn-00b4b934)
- 新版 [`00b4bd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md#insn-00b4bd70) · [`00b4bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md#insn-00b4bd78) · [`00b4bd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd4c.md#insn-00b4bd5c)

~~~diff
- 00b4b948 ["INT_ADD", "register:40f0:8", ["const:b4b948:8", "const:4:8"]]
- 00b4b948 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bd70 ["INT_ADD", "register:40f0:8", ["const:b4bd70:8", "const:4:8"]]
+ 00b4bd70 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b948 bytes 723c0494
+ 00b4bd70 bytes 683c0494
- 00b4b950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bd78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bd78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b950 bytes 60de03f9
+ 00b4bd78 bytes 60de05f9
- 00b4b934 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b934 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bd5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bd5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b934 bytes 68de43f9
+ 00b4bd5c bytes 68de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f38f328f6ba044c65d081eb86f4010"></a>

### [`00b4b964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b964.md) → [`00b4bd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4bdbc",
      "incomplete_value": true,
      "site": "00b4bdbc",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b994",
      "incomplete_value": true,
      "site": "00b4b994",
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
            "const:7b8:8"
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
      "definition_site": "00b4bda0",
      "incomplete_value": true,
      "site": "00b4bda0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b978",
      "incomplete_value": true,
      "site": "00b4b978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bdac",
      "incomplete_value": false,
      "site": "00b4bdb4",
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
            "const:157:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b984",
      "incomplete_value": false,
      "site": "00b4b98c",
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
            "const:7b:8"
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
      "00b4bd9c",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdac",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4bdbc",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd9c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdac",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4bdbc",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b964.md#insn-00b4b98c) · [`00b4b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b964.md#insn-00b4b994) · [`00b4b974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b964.md#insn-00b4b974)
- 新版 [`00b4bdb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md#insn-00b4bdb4) · [`00b4bdbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md#insn-00b4bdbc) · [`00b4bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bd8c.md#insn-00b4bd9c)

~~~diff
- 00b4b98c ["INT_ADD", "register:40f0:8", ["const:b4b98c:8", "const:4:8"]]
- 00b4b98c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bdb4 ["INT_ADD", "register:40f0:8", ["const:b4bdb4:8", "const:4:8"]]
+ 00b4bdb4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b98c bytes 613c0494
+ 00b4bdb4 bytes 573c0494
- 00b4b994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bdbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bdbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b994 bytes 60de03f9
+ 00b4bdbc bytes 60de05f9
- 00b4b974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bd9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bd9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b974 bytes 68de43f9
+ 00b4bd9c bytes 68de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56faa93f126215f7fab779548dc5ed06"></a>

### [`00b4b9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9a8.md) → [`00b4bdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4be00",
      "incomplete_value": true,
      "site": "00b4be00",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b9d8",
      "incomplete_value": true,
      "site": "00b4b9d8",
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
            "const:7b8:8"
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
      "definition_site": "00b4bde4",
      "incomplete_value": true,
      "site": "00b4bde4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4b9bc",
      "incomplete_value": true,
      "site": "00b4b9bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bdec",
      "incomplete_value": false,
      "site": "00b4bdf8",
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
            "const:157:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b9c4",
      "incomplete_value": false,
      "site": "00b4b9d0",
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
            "const:7b:8"
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
      "00b4bde0",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdec",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4be00",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bde0",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdec",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4be00",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9a8.md#insn-00b4b9d0) · [`00b4b9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9a8.md#insn-00b4b9d8) · [`00b4b9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9a8.md#insn-00b4b9b8)
- 新版 [`00b4bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md#insn-00b4bdf8) · [`00b4be00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md#insn-00b4be00) · [`00b4bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bdd0.md#insn-00b4bde0)

~~~diff
- 00b4b9d0 ["INT_ADD", "register:40f0:8", ["const:b4b9d0:8", "const:4:8"]]
- 00b4b9d0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bdf8 ["INT_ADD", "register:40f0:8", ["const:b4bdf8:8", "const:4:8"]]
+ 00b4bdf8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4b9d0 bytes 503c0494
+ 00b4bdf8 bytes 463c0494
- 00b4b9d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4be00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4be00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b9d8 bytes 60de03f9
+ 00b4be00 bytes 60de05f9
- 00b4b9b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
- 00b4b9b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bde0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb8:8"]]
+ 00b4bde0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b9b8 bytes 68de43f9
+ 00b4bde0 bytes 68de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b832b3b07398732079f0fc18e7db26b8"></a>

### [`00b4b9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9f8.md) → [`00b4be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md) _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4bea8",
      "incomplete_value": true,
      "site": "00b4bea8",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba80",
      "incomplete_value": true,
      "site": "00b4ba80",
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
            "const:7c0:8"
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
      "definition_site": "00b4be54",
      "incomplete_value": true,
      "site": "00b4be60",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba2c",
      "incomplete_value": true,
      "site": "00b4ba38",
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
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:7b8:8"
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
      "00b4be34",
      "READ",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4be54",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bea8",
      "WRITE",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4be34",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4be54",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bea8",
      "WRITE",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9f8.md#insn-00b4ba38) · [`00b4ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9f8.md#insn-00b4ba80) · [`00b4ba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9f8.md#insn-00b4ba0c)
- 新版 [`00b4be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md#insn-00b4be60) · [`00b4bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md#insn-00b4bea8) · [`00b4be34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4be20.md#insn-00b4be34)

~~~diff
- 00b4ba38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ba38 ["INT_ADD", "register:40f0:8", ["const:b4ba38:8", "const:4:8"]]
- 00b4ba38 ["CALLIND", null, ["register:0:8"]]
+ 00b4be60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4be60 ["INT_ADD", "register:40f0:8", ["const:b4be60:8", "const:4:8"]]
+ 00b4be60 ["CALLIND", null, ["register:0:8"]]
- 00b4ba38 bytes 00013fd6
+ 00b4be60 bytes 00013fd6
- 00b4ba80 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4ba80 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c0:8"]]
- 00b4ba80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4bea8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4bea8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bc0:8"]]
+ 00b4bea8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ba80 bytes a0021f39
+ 00b4bea8 bytes a0022f39
- 00b4ba0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7c0:8"]]
- 00b4ba0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4ba0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4be34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bc0:8"]]
+ 00b4be34 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4be34 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4ba0c bytes a8025f39
+ 00b4be34 bytes a8026f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e84150a9dc18acec83ee07cc1822628"></a>

### [`00b4ba94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4ba94.md) → [`00b4bebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md) _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4bef8",
      "incomplete_value": true,
      "site": "00b4bef8",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bad0",
      "incomplete_value": true,
      "site": "00b4bad0",
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
            "const:7c0:8"
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
      "definition_site": "00b4bf48",
      "incomplete_value": true,
      "site": "00b4bf48",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bb20",
      "incomplete_value": true,
      "site": "00b4bb20",
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
            "const:7b8:8"
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
      "definition_site": "00b4bed4",
      "incomplete_value": true,
      "site": "00b4bed4",
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
      "definition_site": "00b4baac",
      "incomplete_value": true,
      "site": "00b4baac",
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
      "00b4bed0",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bedc",
      "READ",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bef8",
      "WRITE",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bed0",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bedc",
      "READ",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bef8",
      "WRITE",
      [
        "storage",
        "01125bc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4ba94.md#insn-00b4bad0) · [`00b4bb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4ba94.md#insn-00b4bb1c) · [`00b4bb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4ba94.md#insn-00b4bb20)
- 新版 [`00b4bef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md#insn-00b4bef8) · [`00b4bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md#insn-00b4bf44) · [`00b4bf48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bebc.md#insn-00b4bf48)

~~~diff
- 00b4bad0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4bad0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4bad0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7c0:8"]]
- 00b4bad0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4bef8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4bef8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4bef8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bc0:8"]]
+ 00b4bef8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4bad0 bytes bf021f39
+ 00b4bef8 bytes bf022f39
- 00b4bb1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bb1c ["INT_ADD", "register:40f0:8", ["const:b4bb1c:8", "const:4:8"]]
- 00b4bb1c ["CALLIND", null, ["register:0:8"]]
+ 00b4bf44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bf44 ["INT_ADD", "register:40f0:8", ["const:b4bf44:8", "const:4:8"]]
+ 00b4bf44 ["CALLIND", null, ["register:0:8"]]
- 00b4bb1c bytes 00013fd6
+ 00b4bf44 bytes 00013fd6
- 00b4bb20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00b4bb20 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4bb20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bf48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00b4bf48 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bf48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4bb20 bytes 9fde03f9
+ 00b4bf48 bytes 9fde05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-780ac34994739d046d9b063202f7060f"></a>

### [`00b4bb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bb34.md) → [`00b4bf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md) _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4bf9c",
      "incomplete_value": true,
      "site": "00b4bf9c",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bb74",
      "incomplete_value": true,
      "site": "00b4bb74",
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
            "const:7b8:8"
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
      "definition_site": "00b4bf78",
      "incomplete_value": true,
      "site": "00b4bf78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bb50",
      "incomplete_value": true,
      "site": "00b4bb50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bf80",
      "incomplete_value": false,
      "site": "00b4bf94",
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
            "const:157:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bb58",
      "incomplete_value": false,
      "site": "00b4bb6c",
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
            "const:7b:8"
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
      "00b4bf70",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf80",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4bf9c",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf70",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf80",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4bf9c",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bb34.md#insn-00b4bb6c) · [`00b4bb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bb34.md#insn-00b4bb74) · [`00b4bb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bb34.md#insn-00b4bb48)
- 新版 [`00b4bf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md#insn-00b4bf94) · [`00b4bf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md#insn-00b4bf9c) · [`00b4bf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bf5c.md#insn-00b4bf70)

~~~diff
- 00b4bb6c ["INT_ADD", "register:40f0:8", ["const:b4bb6c:8", "const:4:8"]]
- 00b4bb6c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4bf94 ["INT_ADD", "register:40f0:8", ["const:b4bf94:8", "const:4:8"]]
+ 00b4bf94 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bb6c bytes e93b0494
+ 00b4bf94 bytes df3b0494
- 00b4bb74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00b4bb74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bf9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00b4bf9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bb74 bytes 80de03f9
+ 00b4bf9c bytes 80de05f9
- 00b4bb48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00b4bb48 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4bf70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00b4bf70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bb48 bytes 81de43f9
+ 00b4bf70 bytes 81de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb02b43c3993e08638e54d91f21a541"></a>

### [`00b4bba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bba4.md) → [`00b4bfcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md) _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b160.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b560.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4bfe8",
      "incomplete_value": false,
      "site": "00b4bfec",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bbc0",
      "incomplete_value": false,
      "site": "00b4bbc4",
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
            "const:29a:8"
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
      "definition_site": "00b4bff8",
      "incomplete_value": true,
      "site": "00b4c004",
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
      "definition_site": "00b4bbd0",
      "incomplete_value": true,
      "site": "00b4bbdc",
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
      "00b4bfe8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4bff8",
      "DATA",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bfe8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4bff8",
      "DATA",
      [
        "storage",
        "01125bc8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bbc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bba4.md#insn-00b4bbc4) · [`00b4bbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bba4.md#insn-00b4bbc0) · [`00b4bbcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bba4.md#insn-00b4bbcc)
- 新版 [`00b4bfec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md#insn-00b4bfec) · [`00b4bfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md#insn-00b4bfe8) · [`00b4bff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4bfcc.md#insn-00b4bff4)

~~~diff
- 00b4bbc4 ["INT_ADD", "register:40f0:8", ["const:b4bbc4:8", "const:4:8"]]
- 00b4bbc4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4bfec ["INT_ADD", "register:40f0:8", ["const:b4bfec:8", "const:4:8"]]
+ 00b4bfec ["CALL", null, ["callee:00c5b000:8"]]
- 00b4bbc4 bytes 0f3c0494
+ 00b4bfec bytes 053c0494
- 00b4bbc0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4bbc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bbc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bbc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bfe8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4bfe8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bfe8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bfe8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bbc0 bytes 00680a91
+ 00b4bfe8 bytes 009c0d91
- 00b4bbcc ["COPY", "tmp:0:8", ["const:7c8:8"]]
- 00b4bbcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bbcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bbcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4bff4 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00b4bff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4bff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4bbcc bytes 08211f91
+ 00b4bff4 bytes 08212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cf4bf1ecc35170838fce7b8d8449836"></a>

### [`00b4bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bbe0.md) → [`00b4c008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md) _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4c048",
      "incomplete_value": true,
      "site": "00b4c048",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc20",
      "incomplete_value": true,
      "site": "00b4bc20",
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
            "const:7b8:8"
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
      "definition_site": "00b4c024",
      "incomplete_value": true,
      "site": "00b4c024",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bbfc",
      "incomplete_value": true,
      "site": "00b4bbfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c02c",
      "incomplete_value": false,
      "site": "00b4c040",
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
            "const:157:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc04",
      "incomplete_value": false,
      "site": "00b4bc18",
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
            "const:7b:8"
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
      "00b4c01c",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c02c",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4c048",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c01c",
      "READ",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c02c",
      "PARAM",
      [
        "storage",
        "002a7157",
        null,
        "string"
      ]
    ],
    [
      "00b4c048",
      "WRITE",
      [
        "storage",
        "01125bb8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bbe0.md#insn-00b4bc18) · [`00b4bc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bbe0.md#insn-00b4bc20) · [`00b4bbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bbe0.md#insn-00b4bbf4)
- 新版 [`00b4c040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md#insn-00b4c040) · [`00b4c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md#insn-00b4c048) · [`00b4c01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c008.md#insn-00b4c01c)

~~~diff
- 00b4bc18 ["INT_ADD", "register:40f0:8", ["const:b4bc18:8", "const:4:8"]]
- 00b4bc18 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c040 ["INT_ADD", "register:40f0:8", ["const:b4c040:8", "const:4:8"]]
+ 00b4c040 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bc18 bytes be3b0494
+ 00b4c040 bytes b43b0494
- 00b4bc20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00b4bc20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00b4c048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bc20 bytes 80de03f9
+ 00b4c048 bytes 80de05f9
- 00b4bbf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00b4bbf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c01c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00b4c01c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bbf4 bytes 81de43f9
+ 00b4c01c bytes 81de45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53cba19c7dd859ee05870984a04f0f77"></a>

### [`00b4bc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc50.md) → [`00b4c078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md) _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4c094",
      "incomplete_value": false,
      "site": "00b4c098",
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
            "const:51e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc6c",
      "incomplete_value": false,
      "site": "00b4bc70",
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
            "const:451:8"
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
      "definition_site": "00b4c0a4",
      "incomplete_value": true,
      "site": "00b4c0b0",
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
      "definition_site": "00b4bc7c",
      "incomplete_value": true,
      "site": "00b4bc88",
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
      "00b4c094",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4c0a4",
      "DATA",
      [
        "storage",
        "011257d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c094",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4c0a4",
      "DATA",
      [
        "storage",
        "01125bd8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc50.md#insn-00b4bc70) · [`00b4bc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc50.md#insn-00b4bc6c) · [`00b4bc78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc50.md#insn-00b4bc78)
- 新版 [`00b4c098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md#insn-00b4c098) · [`00b4c094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md#insn-00b4c094) · [`00b4c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c078.md#insn-00b4c0a0)

~~~diff
- 00b4bc70 ["INT_ADD", "register:40f0:8", ["const:b4bc70:8", "const:4:8"]]
- 00b4bc70 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4c098 ["INT_ADD", "register:40f0:8", ["const:b4c098:8", "const:4:8"]]
+ 00b4c098 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4bc70 bytes e43b0494
+ 00b4c098 bytes da3b0494
- 00b4bc6c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4bc6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bc6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bc6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c094 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4c094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bc6c bytes 00441191
+ 00b4c094 bytes 00781491
- 00b4bc78 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00b4bc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c0a0 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00b4c0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4bc78 bytes 08611f91
+ 00b4c0a0 bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-542a2ef8cb4ee2a9122fb2b2b4822f79"></a>

### [`00b4bc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc8c.md) → [`00b4c0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4c0e0",
      "incomplete_value": true,
      "site": "00b4c0e0",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bcb8",
      "incomplete_value": true,
      "site": "00b4bcb8",
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
            "const:7e0:8"
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
      "definition_site": "00b4c0c8",
      "incomplete_value": true,
      "site": "00b4c0c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bca0",
      "incomplete_value": true,
      "site": "00b4bca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c0d4",
      "incomplete_value": false,
      "site": "00b4c0d8",
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
            "const:989:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bcac",
      "incomplete_value": false,
      "site": "00b4bcb0",
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
            "const:8bc:8"
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
      "00b4c0c4",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0d4",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4c0e0",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c0c4",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0d4",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c0e0",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc8c.md#insn-00b4bcb0) · [`00b4bcb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc8c.md#insn-00b4bcb8) · [`00b4bc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc8c.md#insn-00b4bc9c)
- 新版 [`00b4c0d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md#insn-00b4c0d8) · [`00b4c0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md#insn-00b4c0e0) · [`00b4c0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0b4.md#insn-00b4c0c4)

~~~diff
- 00b4bcb0 ["INT_ADD", "register:40f0:8", ["const:b4bcb0:8", "const:4:8"]]
- 00b4bcb0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c0d8 ["INT_ADD", "register:40f0:8", ["const:b4c0d8:8", "const:4:8"]]
+ 00b4c0d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bcb0 bytes 983b0494
+ 00b4c0d8 bytes 8e3b0494
- 00b4bcb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bcb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c0e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c0e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bcb8 bytes 60f203f9
+ 00b4c0e0 bytes 60f205f9
- 00b4bc9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bc9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bc9c bytes 68f243f9
+ 00b4c0c4 bytes 68f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-803a9bc8f75edbc6b4bfebf97b57cc19"></a>

### [`00b4bccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bccc.md) → [`00b4c0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4c120",
      "incomplete_value": true,
      "site": "00b4c120",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bcf8",
      "incomplete_value": true,
      "site": "00b4bcf8",
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
            "const:7e0:8"
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
      "definition_site": "00b4c108",
      "incomplete_value": true,
      "site": "00b4c108",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bce0",
      "incomplete_value": true,
      "site": "00b4bce0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c110",
      "incomplete_value": false,
      "site": "00b4c118",
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
            "const:989:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bce8",
      "incomplete_value": false,
      "site": "00b4bcf0",
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
            "const:8bc:8"
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
      "00b4c104",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c110",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4c120",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c104",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c110",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c120",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bccc.md#insn-00b4bcf0) · [`00b4bcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bccc.md#insn-00b4bcf8) · [`00b4bcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bccc.md#insn-00b4bcdc)
- 新版 [`00b4c118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md#insn-00b4c118) · [`00b4c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md#insn-00b4c120) · [`00b4c104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md#insn-00b4c104)

~~~diff
- 00b4bcf0 ["INT_ADD", "register:40f0:8", ["const:b4bcf0:8", "const:4:8"]]
- 00b4bcf0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c118 ["INT_ADD", "register:40f0:8", ["const:b4c118:8", "const:4:8"]]
+ 00b4c118 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bcf0 bytes 883b0494
+ 00b4c118 bytes 7e3b0494
- 00b4bcf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bcf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c120 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bcf8 bytes 60f203f9
+ 00b4c120 bytes 60f205f9
- 00b4bcdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bcdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bcdc bytes 68f243f9
+ 00b4c104 bytes 68f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa95ad75c918ae0f24930522f1e02e57"></a>

### [`00b4bd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd0c.md) → [`00b4c134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4c164",
      "incomplete_value": true,
      "site": "00b4c164",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd3c",
      "incomplete_value": true,
      "site": "00b4bd3c",
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
            "const:7e0:8"
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
      "definition_site": "00b4c148",
      "incomplete_value": true,
      "site": "00b4c148",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bd20",
      "incomplete_value": true,
      "site": "00b4bd20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c154",
      "incomplete_value": false,
      "site": "00b4c15c",
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
            "const:989:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd2c",
      "incomplete_value": false,
      "site": "00b4bd34",
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
            "const:8bc:8"
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
      "00b4c144",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c154",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4c164",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c144",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c154",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c164",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd0c.md#insn-00b4bd34) · [`00b4bd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd0c.md#insn-00b4bd3c) · [`00b4bd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd0c.md#insn-00b4bd1c)
- 新版 [`00b4c15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md#insn-00b4c15c) · [`00b4c164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md#insn-00b4c164) · [`00b4c144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c134.md#insn-00b4c144)

~~~diff
- 00b4bd34 ["INT_ADD", "register:40f0:8", ["const:b4bd34:8", "const:4:8"]]
- 00b4bd34 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c15c ["INT_ADD", "register:40f0:8", ["const:b4c15c:8", "const:4:8"]]
+ 00b4c15c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bd34 bytes 773b0494
+ 00b4c15c bytes 6d3b0494
- 00b4bd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bd3c bytes 60f203f9
+ 00b4c164 bytes 60f205f9
- 00b4bd1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bd1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c144 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c144 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bd1c bytes 68f243f9
+ 00b4c144 bytes 68f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2dbb5992c03b5fc3eae41e04054f637"></a>

### [`00b4bd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd50.md) → [`00b4c178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "definition_site": "00b4c1a8",
      "incomplete_value": true,
      "site": "00b4c1a8",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd80",
      "incomplete_value": true,
      "site": "00b4bd80",
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
            "const:7e0:8"
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
      "definition_site": "00b4c18c",
      "incomplete_value": true,
      "site": "00b4c18c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bd64",
      "incomplete_value": true,
      "site": "00b4bd64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c194",
      "incomplete_value": false,
      "site": "00b4c1a0",
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
            "const:989:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd6c",
      "incomplete_value": false,
      "site": "00b4bd78",
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
            "const:8bc:8"
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
      "00b4c188",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c194",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4c1a8",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c188",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c194",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c1a8",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd50.md#insn-00b4bd78) · [`00b4bd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd50.md#insn-00b4bd80) · [`00b4bd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd50.md#insn-00b4bd60)
- 新版 [`00b4c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md#insn-00b4c1a0) · [`00b4c1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md#insn-00b4c1a8) · [`00b4c188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c178.md#insn-00b4c188)

~~~diff
- 00b4bd78 ["INT_ADD", "register:40f0:8", ["const:b4bd78:8", "const:4:8"]]
- 00b4bd78 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c1a0 ["INT_ADD", "register:40f0:8", ["const:b4c1a0:8", "const:4:8"]]
+ 00b4c1a0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bd78 bytes 663b0494
+ 00b4c1a0 bytes 5c3b0494
- 00b4bd80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bd80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c1a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c1a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bd80 bytes 60f203f9
+ 00b4c1a8 bytes 60f205f9
- 00b4bd60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
- 00b4bd60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be0:8"]]
+ 00b4c188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bd60 bytes 68f243f9
+ 00b4c188 bytes 68f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34dff22df4ce9a4a84dd112b8c9f786"></a>

### [`00b4bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bda0.md) → [`00b4c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c1c8.md) _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c250",
      "incomplete_value": true,
      "site": "00b4c250",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be28",
      "incomplete_value": true,
      "site": "00b4be28",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4bde0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4c208"
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
      "00b4c1dc",
      "READ",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4bdd4",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c250",
      "WRITE",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c1dc",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c1fc",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c250",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bda0.md#insn-00b4bde0) · [`00b4be28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bda0.md#insn-00b4be28)
- 新版 [`00b4c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c1c8.md#insn-00b4c250) · [`00b4c208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c1c8.md#insn-00b4c208)

~~~diff
- 00b4bde0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bde0 ["INT_ADD", "register:40f0:8", ["const:b4bde0:8", "const:4:8"]]
- 00b4bde0 ["CALLIND", null, ["register:0:8"]]
- 00b4bde0 bytes 00013fd6
- 00b4be28 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4be28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e8:8"]]
- 00b4be28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c250 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c250 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:be8:8"]]
+ 00b4c250 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4be28 bytes a0a21f39
+ 00b4c250 bytes a0a22f39
+ 00b4c208 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c208 ["INT_ADD", "register:40f0:8", ["const:b4c208:8", "const:4:8"]]
+ 00b4c208 ["CALLIND", null, ["register:0:8"]]
+ 00b4c208 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02cd2936393f0942efd62c0482238650"></a>

### [`00b4be3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4be3c.md) → [`00b4c264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md) _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4c2a0",
      "incomplete_value": true,
      "site": "00b4c2a0",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be78",
      "incomplete_value": true,
      "site": "00b4be78",
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
            "const:7e8:8"
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
      "definition_site": "00b4c2f0",
      "incomplete_value": true,
      "site": "00b4c2f0",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bec8",
      "incomplete_value": true,
      "site": "00b4bec8",
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
            "const:7e0:8"
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
      "definition_site": "00b4c27c",
      "incomplete_value": true,
      "site": "00b4c27c",
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
      "definition_site": "00b4be54",
      "incomplete_value": true,
      "site": "00b4be54",
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
      "00b4c278",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c284",
      "READ",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c2a0",
      "WRITE",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c278",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c284",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c2a0",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4be78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4be3c.md#insn-00b4be78) · [`00b4bec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4be3c.md#insn-00b4bec4) · [`00b4bec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4be3c.md#insn-00b4bec8)
- 新版 [`00b4c2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md#insn-00b4c2a0) · [`00b4c2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md#insn-00b4c2ec) · [`00b4c2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c264.md#insn-00b4c2f0)

~~~diff
- 00b4be78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4be78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4be78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e8:8"]]
- 00b4be78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c2a0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c2a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c2a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:be8:8"]]
+ 00b4c2a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4be78 bytes bfa21f39
+ 00b4c2a0 bytes bfa22f39
- 00b4bec4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bec4 ["INT_ADD", "register:40f0:8", ["const:b4bec4:8", "const:4:8"]]
- 00b4bec4 ["CALLIND", null, ["register:0:8"]]
+ 00b4c2ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c2ec ["INT_ADD", "register:40f0:8", ["const:b4c2ec:8", "const:4:8"]]
+ 00b4c2ec ["CALLIND", null, ["register:0:8"]]
- 00b4bec4 bytes 00013fd6
+ 00b4c2ec bytes 00013fd6
- 00b4bec8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b4bec8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4bec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c2f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00b4c2f0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c2f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4bec8 bytes 9ff203f9
+ 00b4c2f0 bytes 9ff205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-335c1d1ebf98798efd62c1bd262377a5"></a>

### [`00b4bedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bedc.md) → [`00b4c304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md) _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "definition_site": "00b4c344",
      "incomplete_value": true,
      "site": "00b4c344",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bf1c",
      "incomplete_value": true,
      "site": "00b4bf1c",
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
            "const:7e0:8"
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
      "definition_site": "00b4c320",
      "incomplete_value": true,
      "site": "00b4c320",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4bef8",
      "incomplete_value": true,
      "site": "00b4bef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c328",
      "incomplete_value": false,
      "site": "00b4c33c",
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
            "const:989:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bf00",
      "incomplete_value": false,
      "site": "00b4bf14",
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
            "const:8bc:8"
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
      "00b4c318",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c328",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4c344",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c318",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c328",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ],
    [
      "00b4c344",
      "WRITE",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bedc.md#insn-00b4bf14) · [`00b4bf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bedc.md#insn-00b4bf1c) · [`00b4bef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bedc.md#insn-00b4bef0)
- 新版 [`00b4c33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md#insn-00b4c33c) · [`00b4c344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md#insn-00b4c344) · [`00b4c318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c304.md#insn-00b4c318)

~~~diff
- 00b4bf14 ["INT_ADD", "register:40f0:8", ["const:b4bf14:8", "const:4:8"]]
- 00b4bf14 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c33c ["INT_ADD", "register:40f0:8", ["const:b4c33c:8", "const:4:8"]]
+ 00b4c33c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bf14 bytes ff3a0494
+ 00b4c33c bytes f53a0494
- 00b4bf1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b4bf1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00b4c344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bf1c bytes 80f203f9
+ 00b4c344 bytes 80f205f9
- 00b4bef0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b4bef0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c318 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00b4c318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4bef0 bytes 81f243f9
+ 00b4c318 bytes 81f245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b1d82fe584b7db7dd15d93b61c07b2b"></a>

### [`00b4bf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf4c.md) → [`00b4c374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md) _ZN8firebase4util4list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b120.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b520.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4c390",
      "incomplete_value": false,
      "site": "00b4c394",
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
            "const:367:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bf68",
      "incomplete_value": false,
      "site": "00b4bf6c",
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
            "const:29a:8"
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
      "definition_site": "00b4c3a0",
      "incomplete_value": true,
      "site": "00b4c3ac",
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
      "definition_site": "00b4bf78",
      "incomplete_value": true,
      "site": "00b4bf84",
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
      "00b4c390",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4c3a0",
      "DATA",
      [
        "storage",
        "011257f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c390",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4c3a0",
      "DATA",
      [
        "storage",
        "01125bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf4c.md#insn-00b4bf6c) · [`00b4bf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf4c.md#insn-00b4bf68) · [`00b4bf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf4c.md#insn-00b4bf74)
- 新版 [`00b4c394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md#insn-00b4c394) · [`00b4c390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md#insn-00b4c390) · [`00b4c39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c374.md#insn-00b4c39c)

~~~diff
- 00b4bf6c ["INT_ADD", "register:40f0:8", ["const:b4bf6c:8", "const:4:8"]]
- 00b4bf6c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4c394 ["INT_ADD", "register:40f0:8", ["const:b4c394:8", "const:4:8"]]
+ 00b4c394 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4bf6c bytes 253b0494
+ 00b4c394 bytes 1b3b0494
- 00b4bf68 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4bf68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bf68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bf68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c390 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4c390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bf68 bytes 00680a91
+ 00b4c390 bytes 009c0d91
- 00b4bf74 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 00b4bf74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bf74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4bf74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c39c ["COPY", "tmp:0:8", ["const:bf0:8"]]
+ 00b4c39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4bf74 bytes 08c11f91
+ 00b4c39c bytes 08c12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71ada9628c3ed09770b07f493e4f46af"></a>

### [`00b4bf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf88.md) → [`00b4c3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c3b0.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4bfc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c3f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4bfa4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4bf9c",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4bfa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c3f4"
      ]
    ],
    [
      "unmatched:00b4bfac",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c3c4",
      "READ",
      [
        "storage",
        "01125be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c3cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c3f4"
      ]
    ],
    [
      "00b4c3d4",
      "PARAM",
      [
        "storage",
        "0029f989",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf88.md#insn-00b4bfa4) · [`00b4bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf88.md#insn-00b4bfc0) · [`00b4bfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf88.md#insn-00b4bfc8)
- 新版 [`00b4c3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c3b0.md#insn-00b4c3e8)

~~~diff
- 00b4bfa4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4bfa4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4bfa4 bytes 410100b5
- 00b4bfc0 ["INT_ADD", "register:40f0:8", ["const:b4bfc0:8", "const:4:8"]]
- 00b4bfc0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c3e8 ["INT_ADD", "register:40f0:8", ["const:b4c3e8:8", "const:4:8"]]
+ 00b4c3e8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4bfc0 bytes d43a0494
+ 00b4c3e8 bytes ca3a0494
- 00b4bfc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00b4bfc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bfc8 bytes 80f203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-166ade087265d53a3bf6728882b5d9f6"></a>

### [`00b4c034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c034.md) → [`00b4c45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c45c.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b4c060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c488"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c470",
      "incomplete_value": true,
      "site": "00b4c470",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b4c048",
      "incomplete_value": true,
      "site": "00b4c048",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4c46c",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4c064"
      ]
    ],
    [
      "unmatched:00b4c054",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c46c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c470",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c48c"
      ]
    ],
    [
      "00b4c47c",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c034.md#insn-00b4c058) · [`00b4c060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c034.md#insn-00b4c060) · [`00b4c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c034.md#insn-00b4c070)

~~~diff
- 00b4c058 ["INT_ADD", "register:40f0:8", ["const:b4c058:8", "const:4:8"]]
- 00b4c058 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c058 bytes ae3a0494
- 00b4c060 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b4c060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c060 bytes 600a04f9
- 00b4c070 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4c070 ["RETURN", null, ["register:0:8"]]
- 00b4c070 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

