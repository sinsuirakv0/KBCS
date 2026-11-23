# v15.7.2 → v15.7.3 · 最優先の変更候補 (70)

[一覧の目次](README.md)

<a id="compare-f7d17d4bc4a4e11fbec0d225f37bc0dc"></a>

### [`00b6127c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6127c.md) → [`00b61344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61344.md) _ZN8firebase4auth20additional_user_info13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b612bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61384"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61290",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61298",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61388"
      ]
    ],
    [
      "unmatched:00b612a0",
      "PARAM",
      [
        "storage",
        "0029bfe9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b61358",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61388"
      ]
    ],
    [
      "00b61368",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6127c.md#insn-00b61298) · [`00b612b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6127c.md#insn-00b612b4) · [`00b612bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6127c.md#insn-00b612bc)
- 新版 [`00b6137c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61344.md#insn-00b6137c)

~~~diff
- 00b61298 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61298 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61298 bytes 410100b5
- 00b612b4 ["INT_ADD", "register:40f0:8", ["const:b612b4:8", "const:4:8"]]
- 00b612b4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6137c ["INT_ADD", "register:40f0:8", ["const:b6137c:8", "const:4:8"]]
+ 00b6137c ["CALL", null, ["callee:00bde040:8"]]
- 00b612b4 bytes 37f30194
+ 00b6137c bytes 31f30194
- 00b612bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:470:8"]]
- 00b612bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b612bc bytes 803a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6b7f78527ca621e67303ecc3b8c04cb"></a>

### [`00b612ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b612ec.md) → [`00b613b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md) _ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b613d0",
      "incomplete_value": false,
      "site": "00b613d4",
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
      "definition_site": "00b61308",
      "incomplete_value": false,
      "site": "00b6130c",
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
      "definition_site": "00b613e0",
      "incomplete_value": true,
      "site": "00b613ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61318",
      "incomplete_value": true,
      "site": "00b61324",
      "value": [
        "LOAD",
        "8",
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
      "00b613d0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b613e0",
      "DATA",
      [
        "storage",
        "010a1498",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b613d0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b613e0",
      "DATA",
      [
        "storage",
        "010a1558",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6130c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b612ec.md#insn-00b6130c) · [`00b61308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b612ec.md#insn-00b61308) · [`00b61314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b612ec.md#insn-00b61314)
- 新版 [`00b613d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md#insn-00b613d4) · [`00b613d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md#insn-00b613d0) · [`00b613dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md#insn-00b613dc)

~~~diff
- 00b6130c ["INT_ADD", "register:40f0:8", ["const:b6130c:8", "const:4:8"]]
- 00b6130c ["CALL", null, ["callee:00bde130:8"]]
+ 00b613d4 ["INT_ADD", "register:40f0:8", ["const:b613d4:8", "const:4:8"]]
+ 00b613d4 ["CALL", null, ["callee:00bde130:8"]]
- 00b6130c bytes 5df30194
+ 00b613d4 bytes 57f30194
- 00b61308 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b61308 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61308 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61308 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b613d0 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b613d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b613d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b613d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61308 bytes 00c81791
+ 00b613d0 bytes 00fc1991
- 00b61314 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00b61314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b613dc ["COPY", "tmp:0:8", ["const:558:8"]]
+ 00b613dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b613dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b613dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61314 bytes 08611291
+ 00b613dc bytes 08611591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2003afabbe28ef242ea8ace75315e058"></a>

### [`00b61328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61328.md) → [`00b613f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b6141c",
      "incomplete_value": true,
      "site": "00b6141c",
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
      "definition_site": "00b61354",
      "incomplete_value": true,
      "site": "00b61354",
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
      "definition_site": "00b61404",
      "incomplete_value": true,
      "site": "00b61404",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6133c",
      "incomplete_value": true,
      "site": "00b6133c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61410",
      "incomplete_value": false,
      "site": "00b61414",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61348",
      "incomplete_value": false,
      "site": "00b6134c",
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
            "const:739:8"
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
      "00b61400",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61410",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b6141c",
      "WRITE",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61400",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61410",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b6141c",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6134c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61328.md#insn-00b6134c) · [`00b61354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61328.md#insn-00b61354) · [`00b61338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61328.md#insn-00b61338)
- 新版 [`00b61414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md#insn-00b61414) · [`00b6141c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md#insn-00b6141c) · [`00b61400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md#insn-00b61400)

~~~diff
- 00b6134c ["INT_ADD", "register:40f0:8", ["const:b6134c:8", "const:4:8"]]
- 00b6134c ["CALL", null, ["callee:00bde040:8"]]
+ 00b61414 ["INT_ADD", "register:40f0:8", ["const:b61414:8", "const:4:8"]]
+ 00b61414 ["CALL", null, ["callee:00bde040:8"]]
- 00b6134c bytes 11f30194
+ 00b61414 bytes 0bf30194
- 00b61354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b61354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6141c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b6141c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61354 bytes 605202f9
+ 00b6141c bytes 60b202f9
- 00b61338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b61338 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b61400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61338 bytes 685242f9
+ 00b61400 bytes 68b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69ebd590d18998f042c22a143efa5b83"></a>

### [`00b61368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61368.md) → [`00b61430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b6145c",
      "incomplete_value": true,
      "site": "00b6145c",
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
      "definition_site": "00b61394",
      "incomplete_value": true,
      "site": "00b61394",
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
      "definition_site": "00b61444",
      "incomplete_value": true,
      "site": "00b61444",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6137c",
      "incomplete_value": true,
      "site": "00b6137c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6144c",
      "incomplete_value": false,
      "site": "00b61454",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61384",
      "incomplete_value": false,
      "site": "00b6138c",
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
            "const:739:8"
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
      "00b61440",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6144c",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b6145c",
      "WRITE",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61440",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6144c",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b6145c",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6138c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61368.md#insn-00b6138c) · [`00b61394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61368.md#insn-00b61394) · [`00b61378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61368.md#insn-00b61378)
- 新版 [`00b61454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md#insn-00b61454) · [`00b6145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md#insn-00b6145c) · [`00b61440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md#insn-00b61440)

~~~diff
- 00b6138c ["INT_ADD", "register:40f0:8", ["const:b6138c:8", "const:4:8"]]
- 00b6138c ["CALL", null, ["callee:00bde040:8"]]
+ 00b61454 ["INT_ADD", "register:40f0:8", ["const:b61454:8", "const:4:8"]]
+ 00b61454 ["CALL", null, ["callee:00bde040:8"]]
- 00b6138c bytes 01f30194
+ 00b61454 bytes fbf20194
- 00b61394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b61394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6145c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b6145c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61394 bytes 605202f9
+ 00b6145c bytes 60b202f9
- 00b61378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b61378 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b61440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61378 bytes 685242f9
+ 00b61440 bytes 68b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5df9b1f4d8a7b3aea6e392906bc022c2"></a>

### [`00b613a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613a8.md) → [`00b61470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b614a0",
      "incomplete_value": true,
      "site": "00b614a0",
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
      "definition_site": "00b613d8",
      "incomplete_value": true,
      "site": "00b613d8",
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
      "definition_site": "00b61484",
      "incomplete_value": true,
      "site": "00b61484",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b613bc",
      "incomplete_value": true,
      "site": "00b613bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61490",
      "incomplete_value": false,
      "site": "00b61498",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b613c8",
      "incomplete_value": false,
      "site": "00b613d0",
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
            "const:739:8"
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
      "00b61480",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61490",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b614a0",
      "WRITE",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61480",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61490",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b614a0",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b613d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613a8.md#insn-00b613d0) · [`00b613d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613a8.md#insn-00b613d8) · [`00b613b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613a8.md#insn-00b613b8)
- 新版 [`00b61498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md#insn-00b61498) · [`00b614a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md#insn-00b614a0) · [`00b61480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md#insn-00b61480)

~~~diff
- 00b613d0 ["INT_ADD", "register:40f0:8", ["const:b613d0:8", "const:4:8"]]
- 00b613d0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61498 ["INT_ADD", "register:40f0:8", ["const:b61498:8", "const:4:8"]]
+ 00b61498 ["CALL", null, ["callee:00bde040:8"]]
- 00b613d0 bytes f0f20194
+ 00b61498 bytes eaf20194
- 00b613d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b613d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b614a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b614a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b613d8 bytes 605202f9
+ 00b614a0 bytes 60b202f9
- 00b613b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b613b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b61480 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b613b8 bytes 685242f9
+ 00b61480 bytes 68b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9896c9e3d3728f16790891ec21fa5a2"></a>

### [`00b613ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613ec.md) → [`00b614b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b614e4",
      "incomplete_value": true,
      "site": "00b614e4",
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
      "definition_site": "00b6141c",
      "incomplete_value": true,
      "site": "00b6141c",
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
      "definition_site": "00b614c8",
      "incomplete_value": true,
      "site": "00b614c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61400",
      "incomplete_value": true,
      "site": "00b61400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b614d0",
      "incomplete_value": false,
      "site": "00b614dc",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61408",
      "incomplete_value": false,
      "site": "00b61414",
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
            "const:739:8"
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
      "00b614c4",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b614d0",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b614e4",
      "WRITE",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b614c4",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b614d0",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b614e4",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61414`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613ec.md#insn-00b61414) · [`00b6141c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613ec.md#insn-00b6141c) · [`00b613fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b613ec.md#insn-00b613fc)
- 新版 [`00b614dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md#insn-00b614dc) · [`00b614e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md#insn-00b614e4) · [`00b614c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md#insn-00b614c4)

~~~diff
- 00b61414 ["INT_ADD", "register:40f0:8", ["const:b61414:8", "const:4:8"]]
- 00b61414 ["CALL", null, ["callee:00bde040:8"]]
+ 00b614dc ["INT_ADD", "register:40f0:8", ["const:b614dc:8", "const:4:8"]]
+ 00b614dc ["CALL", null, ["callee:00bde040:8"]]
- 00b61414 bytes dff20194
+ 00b614dc bytes d9f20194
- 00b6141c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b6141c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b614e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b614e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6141c bytes 605202f9
+ 00b614e4 bytes 60b202f9
- 00b613fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a0:8"]]
- 00b613fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b614c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
+ 00b614c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b613fc bytes 685242f9
+ 00b614c4 bytes 68b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdf12897431cb4dbdae9040c0390a209"></a>

### [`00b6143c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6143c.md) → [`00b61504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md) _ZN8firebase4auth27api_not_available_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6155c",
      "incomplete_value": true,
      "site": "00b6155c",
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
      "definition_site": "00b61494",
      "incomplete_value": true,
      "site": "00b61494",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b61538",
      "incomplete_value": true,
      "site": "00b61544",
      "value": [
        "LOAD",
        "8",
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
                "const:560:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61470",
      "incomplete_value": true,
      "site": "00b6147c",
      "value": [
        "LOAD",
        "8",
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
                "const:4a0:8"
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
      "00b61518",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61538",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6155c",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61518",
      "READ",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61538",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6155c",
      "WRITE",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6147c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6143c.md#insn-00b6147c) · [`00b61494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6143c.md#insn-00b61494) · [`00b61450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6143c.md#insn-00b61450)
- 新版 [`00b61544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md#insn-00b61544) · [`00b6155c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md#insn-00b6155c) · [`00b61518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md#insn-00b61518)

~~~diff
- 00b6147c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6147c ["INT_ADD", "register:40f0:8", ["const:b6147c:8", "const:4:8"]]
- 00b6147c ["CALLIND", null, ["register:0:8"]]
+ 00b61544 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61544 ["INT_ADD", "register:40f0:8", ["const:b61544:8", "const:4:8"]]
+ 00b61544 ["CALLIND", null, ["register:0:8"]]
- 00b6147c bytes 00013fd6
+ 00b61544 bytes 00013fd6
- 00b61494 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61494 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4a8:8"]]
- 00b61494 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6155c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6155c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:568:8"]]
+ 00b6155c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61494 bytes a0a21239
+ 00b6155c bytes a0a21539
- 00b61450 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4a8:8"]]
- 00b61450 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61450 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b61518 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
+ 00b61518 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b61518 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61450 bytes a8a25239
+ 00b61518 bytes a8a25539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64a9ce8e20e4a1f9e4c61c69d3fc10f"></a>

### [`00b614a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b614a8.md) → [`00b61570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md) _ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b615ac",
      "incomplete_value": true,
      "site": "00b615ac",
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
      "definition_site": "00b614e4",
      "incomplete_value": true,
      "site": "00b614e4",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b615cc",
      "incomplete_value": true,
      "site": "00b615cc",
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
      "definition_site": "00b61504",
      "incomplete_value": true,
      "site": "00b61504",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61588",
      "incomplete_value": true,
      "site": "00b61588",
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
      "definition_site": "00b614c0",
      "incomplete_value": true,
      "site": "00b614c0",
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
      "00b61584",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61590",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b615ac",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61584",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61590",
      "READ",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ],
    [
      "00b615ac",
      "WRITE",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b614e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b614a8.md#insn-00b614e4) · [`00b61500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b614a8.md#insn-00b61500) · [`00b61504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b614a8.md#insn-00b61504)
- 新版 [`00b615ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md#insn-00b615ac) · [`00b615c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md#insn-00b615c8) · [`00b615cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md#insn-00b615cc)

~~~diff
- 00b614e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b614e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b614e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4a8:8"]]
- 00b614e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b615ac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b615ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b615ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:568:8"]]
+ 00b615ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b614e4 bytes bfa21239
+ 00b615ac bytes bfa21539
- 00b61500 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61500 ["INT_ADD", "register:40f0:8", ["const:b61500:8", "const:4:8"]]
- 00b61500 ["CALLIND", null, ["register:0:8"]]
+ 00b615c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b615c8 ["INT_ADD", "register:40f0:8", ["const:b615c8:8", "const:4:8"]]
+ 00b615c8 ["CALLIND", null, ["register:0:8"]]
- 00b61500 bytes 00013fd6
+ 00b615c8 bytes 00013fd6
- 00b61504 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b61504 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b61504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b615cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00b615cc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b615cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b61504 bytes 9f5202f9
+ 00b615cc bytes 9fb202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c102a4088eb196e455b9b22ee471ac9"></a>

### [`00b61518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61518.md) → [`00b615e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md) _ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b61620",
      "incomplete_value": true,
      "site": "00b61620",
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
      "definition_site": "00b61558",
      "incomplete_value": true,
      "site": "00b61558",
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
      "definition_site": "00b615fc",
      "incomplete_value": true,
      "site": "00b615fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61534",
      "incomplete_value": true,
      "site": "00b61534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61604",
      "incomplete_value": false,
      "site": "00b61618",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6153c",
      "incomplete_value": false,
      "site": "00b61550",
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
            "const:739:8"
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
      "00b615f4",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61604",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b61620",
      "WRITE",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b615f4",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61604",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b61620",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61518.md#insn-00b61550) · [`00b61558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61518.md#insn-00b61558) · [`00b6152c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61518.md#insn-00b6152c)
- 新版 [`00b61618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md#insn-00b61618) · [`00b61620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md#insn-00b61620) · [`00b615f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md#insn-00b615f4)

~~~diff
- 00b61550 ["INT_ADD", "register:40f0:8", ["const:b61550:8", "const:4:8"]]
- 00b61550 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61618 ["INT_ADD", "register:40f0:8", ["const:b61618:8", "const:4:8"]]
+ 00b61618 ["CALL", null, ["callee:00bde040:8"]]
- 00b61550 bytes 90f20194
+ 00b61618 bytes 8af20194
- 00b61558 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b61558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61620 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00b61620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61558 bytes 805202f9
+ 00b61620 bytes 80b202f9
- 00b6152c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b6152c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b615f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00b615f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6152c bytes 815242f9
+ 00b615f4 bytes 81b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-821727c81d0eed69fa5d12d3b78c8a64"></a>

### [`00b615c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b615c4.md) → [`00b6168c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md) _ZN8firebase4auth27api_not_available_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b616cc",
      "incomplete_value": true,
      "site": "00b616cc",
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
      "definition_site": "00b61604",
      "incomplete_value": true,
      "site": "00b61604",
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
      "definition_site": "00b616a8",
      "incomplete_value": true,
      "site": "00b616a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b615e0",
      "incomplete_value": true,
      "site": "00b615e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b616b0",
      "incomplete_value": false,
      "site": "00b616c4",
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
            "const:7c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b615e8",
      "incomplete_value": false,
      "site": "00b615fc",
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
            "const:739:8"
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
      "00b616a0",
      "READ",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b616b0",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b616cc",
      "WRITE",
      [
        "storage",
        "010a14a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b616a0",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b616b0",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b616cc",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b615fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b615c4.md#insn-00b615fc) · [`00b61604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b615c4.md#insn-00b61604) · [`00b615d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b615c4.md#insn-00b615d8)
- 新版 [`00b616c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md#insn-00b616c4) · [`00b616cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md#insn-00b616cc) · [`00b616a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md#insn-00b616a0)

~~~diff
- 00b615fc ["INT_ADD", "register:40f0:8", ["const:b615fc:8", "const:4:8"]]
- 00b615fc ["CALL", null, ["callee:00bde040:8"]]
+ 00b616c4 ["INT_ADD", "register:40f0:8", ["const:b616c4:8", "const:4:8"]]
+ 00b616c4 ["CALL", null, ["callee:00bde040:8"]]
- 00b615fc bytes 65f20194
+ 00b616c4 bytes 5ff20194
- 00b61604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b61604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b616cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00b616cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61604 bytes 805202f9
+ 00b616cc bytes 80b202f9
- 00b615d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00b615d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b616a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
+ 00b616a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b615d8 bytes 815242f9
+ 00b616a0 bytes 81b242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0878c569c4e2853ec8f34d33d77a73d"></a>

### [`00b61634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61634.md) → [`00b616fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md) _ZN8firebase4auth27api_not_available_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b61718",
      "incomplete_value": false,
      "site": "00b6171c",
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
      "definition_site": "00b61650",
      "incomplete_value": false,
      "site": "00b61654",
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
      "definition_site": "00b61728",
      "incomplete_value": true,
      "site": "00b61734",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61660",
      "incomplete_value": true,
      "site": "00b6166c",
      "value": [
        "LOAD",
        "8",
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
      "00b61718",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b61728",
      "DATA",
      [
        "storage",
        "010a14b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61718",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61728",
      "DATA",
      [
        "storage",
        "010a1578",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61634.md#insn-00b61654) · [`00b61650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61634.md#insn-00b61650) · [`00b6165c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61634.md#insn-00b6165c)
- 新版 [`00b6171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md#insn-00b6171c) · [`00b61718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md#insn-00b61718) · [`00b61724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md#insn-00b61724)

~~~diff
- 00b61654 ["INT_ADD", "register:40f0:8", ["const:b61654:8", "const:4:8"]]
- 00b61654 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6171c ["INT_ADD", "register:40f0:8", ["const:b6171c:8", "const:4:8"]]
+ 00b6171c ["CALL", null, ["callee:00bde130:8"]]
- 00b61654 bytes 8bf20194
+ 00b6171c bytes 85f20194
- 00b61650 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b61650 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61650 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61650 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61718 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b61718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61650 bytes 00c81791
+ 00b61718 bytes 00fc1991
- 00b6165c ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00b6165c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6165c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6165c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61724 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00b61724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6165c bytes 08e11291
+ 00b61724 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26dbd57edd6aa89ebf34cc307f411ed4"></a>

### [`00b61670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61670.md) → [`00b61738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61738.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 33.33% / 新版 20.00%

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
      "site": "00b6169c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61764"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6174c",
      "incomplete_value": true,
      "site": "00b6174c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61684",
      "incomplete_value": true,
      "site": "00b61684",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b61748",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61690",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61694",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b61748",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61758",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b6175c",
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

- 旧版 [`00b61684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61670.md#insn-00b61684) · [`00b61694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61670.md#insn-00b61694) · [`00b6169c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61670.md#insn-00b6169c)
- 新版 [`00b6174c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61738.md#insn-00b6174c)

~~~diff
- 00b61684 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61684 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6174c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6174c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b61684 bytes e80000b5
+ 00b6174c bytes e80000b5
- 00b61694 ["INT_ADD", "register:40f0:8", ["const:b61694:8", "const:4:8"]]
- 00b61694 ["CALL", null, ["callee:00bde040:8"]]
- 00b61694 bytes 3ff20194
- 00b6169c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00b6169c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6169c bytes 606202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d82e102f06665f045735ff767ed6d6e"></a>

### [`00b616b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616b0.md) → [`00b61778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b617a4",
      "incomplete_value": true,
      "site": "00b617a4",
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
      "definition_site": "00b616dc",
      "incomplete_value": true,
      "site": "00b616dc",
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
      "definition_site": "00b6178c",
      "incomplete_value": true,
      "site": "00b6178c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b616c4",
      "incomplete_value": true,
      "site": "00b616c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61794",
      "incomplete_value": false,
      "site": "00b6179c",
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
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b616cc",
      "incomplete_value": false,
      "site": "00b616d4",
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
            "const:4fa:8"
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
      "00b61788",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61794",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b617a4",
      "WRITE",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61788",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61794",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b617a4",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b616d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616b0.md#insn-00b616d4) · [`00b616dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616b0.md#insn-00b616dc) · [`00b616c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616b0.md#insn-00b616c0)
- 新版 [`00b6179c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md#insn-00b6179c) · [`00b617a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md#insn-00b617a4) · [`00b61788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md#insn-00b61788)

~~~diff
- 00b616d4 ["INT_ADD", "register:40f0:8", ["const:b616d4:8", "const:4:8"]]
- 00b616d4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6179c ["INT_ADD", "register:40f0:8", ["const:b6179c:8", "const:4:8"]]
+ 00b6179c ["CALL", null, ["callee:00bde040:8"]]
- 00b616d4 bytes 2ff20194
+ 00b6179c bytes 29f20194
- 00b616dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00b616dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b617a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00b617a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b616dc bytes 606202f9
+ 00b617a4 bytes 60c202f9
- 00b616c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00b616c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00b61788 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b616c0 bytes 686242f9
+ 00b61788 bytes 68c242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4777ec2c5d37ead23e35371694bc0b8"></a>

### [`00b616f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616f0.md) → [`00b617b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b617e8",
      "incomplete_value": true,
      "site": "00b617e8",
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
      "definition_site": "00b61720",
      "incomplete_value": true,
      "site": "00b61720",
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
      "definition_site": "00b617cc",
      "incomplete_value": true,
      "site": "00b617cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61704",
      "incomplete_value": true,
      "site": "00b61704",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b617d8",
      "incomplete_value": false,
      "site": "00b617e0",
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
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61710",
      "incomplete_value": false,
      "site": "00b61718",
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
            "const:4fa:8"
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
      "00b617c8",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b617d8",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b617e8",
      "WRITE",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b617c8",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b617d8",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b617e8",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616f0.md#insn-00b61718) · [`00b61720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616f0.md#insn-00b61720) · [`00b61700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b616f0.md#insn-00b61700)
- 新版 [`00b617e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md#insn-00b617e0) · [`00b617e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md#insn-00b617e8) · [`00b617c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md#insn-00b617c8)

~~~diff
- 00b61718 ["INT_ADD", "register:40f0:8", ["const:b61718:8", "const:4:8"]]
- 00b61718 ["CALL", null, ["callee:00bde040:8"]]
+ 00b617e0 ["INT_ADD", "register:40f0:8", ["const:b617e0:8", "const:4:8"]]
+ 00b617e0 ["CALL", null, ["callee:00bde040:8"]]
- 00b61718 bytes 1ef20194
+ 00b617e0 bytes 18f20194
- 00b61720 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00b61720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b617e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00b617e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61720 bytes 606202f9
+ 00b617e8 bytes 60c202f9
- 00b61700 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00b61700 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b617c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00b617c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61700 bytes 686242f9
+ 00b617c8 bytes 68c242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1065d3a10ed01c5b31ccfd30bbbed3c1"></a>

### [`00b61734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61734.md) → [`00b617fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 20.00% / 新版 33.33%

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
      "site": "00b61764"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6182c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61810",
      "incomplete_value": true,
      "site": "00b61810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61748",
      "incomplete_value": true,
      "site": "00b61748",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b6180c",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61750",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61764",
      "WRITE",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6180c",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61818",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b6182c",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61734.md#insn-00b61748) · [`00b6175c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61734.md#insn-00b6175c) · [`00b61764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61734.md#insn-00b61764)
- 新版 [`00b61810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md#insn-00b61810) · [`00b61824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md#insn-00b61824)

~~~diff
- 00b61748 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61748 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b61810 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b61810 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61748 bytes 080100b5
+ 00b61810 bytes 080100b5
- 00b6175c ["INT_ADD", "register:40f0:8", ["const:b6175c:8", "const:4:8"]]
- 00b6175c ["CALL", null, ["callee:00bde040:8"]]
+ 00b61824 ["INT_ADD", "register:40f0:8", ["const:b61824:8", "const:4:8"]]
+ 00b61824 ["CALL", null, ["callee:00bde040:8"]]
- 00b6175c bytes 0df20194
+ 00b61824 bytes 07f20194
- 00b61764 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
- 00b61764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61764 bytes 606202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f79d695570d05c4aeb58cacbed93549"></a>

### [`00b617f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b617f0.md) → [`00b618b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md) _ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b618f4",
      "incomplete_value": true,
      "site": "00b618f4",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6182c",
      "incomplete_value": true,
      "site": "00b6182c",
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
            "const:4c8:8"
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
      "definition_site": "00b61914",
      "incomplete_value": true,
      "site": "00b61914",
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
      "definition_site": "00b6184c",
      "incomplete_value": true,
      "site": "00b6184c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b618d0",
      "incomplete_value": true,
      "site": "00b618d0",
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
      "definition_site": "00b61808",
      "incomplete_value": true,
      "site": "00b61808",
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
      "00b618cc",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b618d8",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b618f4",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b618cc",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b618d8",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b618f4",
      "WRITE",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6182c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b617f0.md#insn-00b6182c) · [`00b61848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b617f0.md#insn-00b61848) · [`00b6184c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b617f0.md#insn-00b6184c)
- 新版 [`00b618f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md#insn-00b618f4) · [`00b61910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md#insn-00b61910) · [`00b61914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md#insn-00b61914)

~~~diff
- 00b6182c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6182c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6182c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4c8:8"]]
- 00b6182c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b618f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b618f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b618f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:588:8"]]
+ 00b618f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6182c bytes bf221339
+ 00b618f4 bytes bf221639
- 00b61848 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61848 ["INT_ADD", "register:40f0:8", ["const:b61848:8", "const:4:8"]]
- 00b61848 ["CALLIND", null, ["register:0:8"]]
+ 00b61910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61910 ["INT_ADD", "register:40f0:8", ["const:b61910:8", "const:4:8"]]
+ 00b61910 ["CALLIND", null, ["register:0:8"]]
- 00b61848 bytes 00013fd6
+ 00b61910 bytes 00013fd6
- 00b6184c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00b6184c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6184c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b61914 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
+ 00b61914 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b61914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6184c bytes 9f6202f9
+ 00b61914 bytes 9fc202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e85764b173e2fa6c3a10bc876855abd2"></a>

### [`00b61860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61860.md) → [`00b61928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61928.md) _ZN8firebase4auth21action_code_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00b618a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61968"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6187c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61874",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6187c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6196c"
      ]
    ],
    [
      "unmatched:00b61884",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6193c",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61944",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6196c"
      ]
    ],
    [
      "00b6194c",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6187c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61860.md#insn-00b6187c) · [`00b61898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61860.md#insn-00b61898) · [`00b618a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61860.md#insn-00b618a0)
- 新版 [`00b61960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61928.md#insn-00b61960)

~~~diff
- 00b6187c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6187c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6187c bytes 410100b5
- 00b61898 ["INT_ADD", "register:40f0:8", ["const:b61898:8", "const:4:8"]]
- 00b61898 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61960 ["INT_ADD", "register:40f0:8", ["const:b61960:8", "const:4:8"]]
+ 00b61960 ["CALL", null, ["callee:00bde040:8"]]
- 00b61898 bytes bef10194
+ 00b61960 bytes b8f10194
- 00b618a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00b618a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b618a0 bytes 806202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f578a826ac8515948e141c01af21c964"></a>

### [`00b618d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b618d0.md) → [`00b61998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md) _ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b619b4",
      "incomplete_value": false,
      "site": "00b619b8",
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
      "definition_site": "00b618ec",
      "incomplete_value": false,
      "site": "00b618f0",
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
      "definition_site": "00b619c4",
      "incomplete_value": true,
      "site": "00b619d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b618fc",
      "incomplete_value": true,
      "site": "00b61908",
      "value": [
        "LOAD",
        "8",
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
      "00b619b4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b619c4",
      "DATA",
      [
        "storage",
        "010a14d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b619b4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b619c4",
      "DATA",
      [
        "storage",
        "010a1590",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b618f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b618d0.md#insn-00b618f0) · [`00b618ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b618d0.md#insn-00b618ec) · [`00b618f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b618d0.md#insn-00b618f8)
- 新版 [`00b619b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md#insn-00b619b8) · [`00b619b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md#insn-00b619b4) · [`00b619c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md#insn-00b619c0)

~~~diff
- 00b618f0 ["INT_ADD", "register:40f0:8", ["const:b618f0:8", "const:4:8"]]
- 00b618f0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b619b8 ["INT_ADD", "register:40f0:8", ["const:b619b8:8", "const:4:8"]]
+ 00b619b8 ["CALL", null, ["callee:00bde130:8"]]
- 00b618f0 bytes e4f10194
+ 00b619b8 bytes def10194
- 00b618ec ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b618ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b618ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b618ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b619b4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b619b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b619b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b619b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b618ec bytes 001c1591
+ 00b619b4 bytes 00501791
- 00b618f8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 00b618f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b618f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b618f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b619c0 ["COPY", "tmp:0:8", ["const:590:8"]]
+ 00b619c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b619c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b619c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b618f8 bytes 08411391
+ 00b619c0 bytes 08411691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1edfaea4bc611b528c34d1ec1d06caec"></a>

### [`00b6190c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6190c.md) → [`00b619d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b619d4.md) _ZN8firebase4auth21action_code_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00b6194c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61a14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61928"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61920",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61a18"
      ]
    ],
    [
      "unmatched:00b61930",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b619e8",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b619f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61a18"
      ]
    ],
    [
      "00b619f8",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6190c.md#insn-00b61928) · [`00b61944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6190c.md#insn-00b61944) · [`00b6194c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b6190c.md#insn-00b6194c)
- 新版 [`00b61a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b619d4.md#insn-00b61a0c)

~~~diff
- 00b61928 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61928 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61928 bytes 410100b5
- 00b61944 ["INT_ADD", "register:40f0:8", ["const:b61944:8", "const:4:8"]]
- 00b61944 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61a0c ["INT_ADD", "register:40f0:8", ["const:b61a0c:8", "const:4:8"]]
+ 00b61a0c ["CALL", null, ["callee:00bde040:8"]]
- 00b61944 bytes 93f10194
+ 00b61a0c bytes 8df10194
- 00b6194c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
- 00b6194c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6194c bytes 806202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ddf584081fa6235c93b587389414a65"></a>

### [`00b619b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619b8.md) → [`00b61a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a80.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "site": "00b619e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61aac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61a94",
      "incomplete_value": true,
      "site": "00b61a94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b619cc",
      "incomplete_value": true,
      "site": "00b619cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b61a90",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b619d8",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b619dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b61a90",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61aa0",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61aa4",
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

- 旧版 [`00b619cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619b8.md#insn-00b619cc) · [`00b619dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619b8.md#insn-00b619dc) · [`00b619e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619b8.md#insn-00b619e4)
- 新版 [`00b61a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a80.md#insn-00b61a94)

~~~diff
- 00b619cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b619cc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b61a94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b61a94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b619cc bytes e80000b5
+ 00b61a94 bytes e80000b5
- 00b619dc ["INT_ADD", "register:40f0:8", ["const:b619dc:8", "const:4:8"]]
- 00b619dc ["CALL", null, ["callee:00bde040:8"]]
- 00b619dc bytes 6df10194
- 00b619e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e0:8"]]
- 00b619e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b619e4 bytes 607202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27e26b29dac364e37107198c9d88ec74"></a>

### [`00b619f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619f8.md) → [`00b61ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

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
      "definition_site": "00b61aec",
      "incomplete_value": true,
      "site": "00b61aec",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61a24",
      "incomplete_value": true,
      "site": "00b61a24",
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
            "const:4e0:8"
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
      "definition_site": "00b61ad4",
      "incomplete_value": true,
      "site": "00b61ad4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61a0c",
      "incomplete_value": true,
      "site": "00b61a0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61adc",
      "incomplete_value": false,
      "site": "00b61ae4",
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
            "const:534:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61a14",
      "incomplete_value": false,
      "site": "00b61a1c",
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
            "const:4a7:8"
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
      "00b61ad0",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61adc",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "00b61aec",
      "WRITE",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61ad0",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61adc",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ],
    [
      "00b61aec",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619f8.md#insn-00b61a1c) · [`00b61a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619f8.md#insn-00b61a24) · [`00b61a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b619f8.md#insn-00b61a08)
- 新版 [`00b61ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md#insn-00b61ae4) · [`00b61aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md#insn-00b61aec) · [`00b61ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61ac0.md#insn-00b61ad0)

~~~diff
- 00b61a1c ["INT_ADD", "register:40f0:8", ["const:b61a1c:8", "const:4:8"]]
- 00b61a1c ["CALL", null, ["callee:00bde040:8"]]
+ 00b61ae4 ["INT_ADD", "register:40f0:8", ["const:b61ae4:8", "const:4:8"]]
+ 00b61ae4 ["CALL", null, ["callee:00bde040:8"]]
- 00b61a1c bytes 5df10194
+ 00b61ae4 bytes 57f10194
- 00b61a24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e0:8"]]
- 00b61a24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61aec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61aec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61a24 bytes 607202f9
+ 00b61aec bytes 60d202f9
- 00b61a08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e0:8"]]
- 00b61a08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61ad0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61ad0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61a08 bytes 687242f9
+ 00b61ad0 bytes 68d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b907b5ce48a534e902b770d079e8c6ac"></a>

### [`00b61a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a38.md) → [`00b61b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b00.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b61a68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61b30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61b14",
      "incomplete_value": true,
      "site": "00b61b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61a4c",
      "incomplete_value": true,
      "site": "00b61a4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b61b10",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61a6c"
      ]
    ],
    [
      "unmatched:00b61a58",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b61b10",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61b34"
      ]
    ],
    [
      "00b61b20",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a38.md#insn-00b61a4c) · [`00b61a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a38.md#insn-00b61a60) · [`00b61a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a38.md#insn-00b61a68)
- 新版 [`00b61b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b00.md#insn-00b61b14)

~~~diff
- 00b61a4c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61a4c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b61b14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b61b14 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61a4c bytes 080100b5
+ 00b61b14 bytes 080100b5
- 00b61a60 ["INT_ADD", "register:40f0:8", ["const:b61a60:8", "const:4:8"]]
- 00b61a60 ["CALL", null, ["callee:00bde040:8"]]
- 00b61a60 bytes 4cf10194
- 00b61a68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e0:8"]]
- 00b61a68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61a68 bytes 607202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a04ce84a922d007fd67c0d83152a3da5"></a>

### [`00b61a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a7c.md) → [`00b61b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b61b74",
      "incomplete_value": true,
      "site": "00b61b74",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61aac",
      "incomplete_value": true,
      "site": "00b61aac",
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
            "const:4e0:8"
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
      "unmatched:00b61a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b61b54",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61a98",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b61b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b61b54",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61b60",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a7c.md#insn-00b61a80) · [`00b61aa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a7c.md#insn-00b61aa4) · [`00b61aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61a7c.md#insn-00b61aac)
- 新版 [`00b61b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md#insn-00b61b6c) · [`00b61b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b44.md#insn-00b61b74)

~~~diff
- 00b61a80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61a80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61a80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61a80 bytes fd7b01a9
- 00b61aa4 ["INT_ADD", "register:40f0:8", ["const:b61aa4:8", "const:4:8"]]
- 00b61aa4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61b6c ["INT_ADD", "register:40f0:8", ["const:b61b6c:8", "const:4:8"]]
+ 00b61b6c ["CALL", null, ["callee:00bde040:8"]]
- 00b61aa4 bytes 3bf10194
+ 00b61b6c bytes 35f10194
- 00b61aac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e0:8"]]
- 00b61aac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61aac bytes 607202f9
+ 00b61b74 bytes 60d202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c602414b79021760b45d63277b16272b"></a>

### [`00b61acc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61acc.md) → [`00b61b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md) _ZN8firebase4auth15email_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b61bec",
      "incomplete_value": true,
      "site": "00b61bec",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b24",
      "incomplete_value": true,
      "site": "00b61b24",
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
            "const:4e8:8"
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
      "definition_site": "00b61bc8",
      "incomplete_value": true,
      "site": "00b61bd4",
      "value": [
        "LOAD",
        "8",
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
                "const:5a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61b00",
      "incomplete_value": true,
      "site": "00b61b0c",
      "value": [
        "LOAD",
        "8",
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
                "const:4e0:8"
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
      "00b61ba8",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61bc8",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61bec",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61ba8",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61bc8",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61bec",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61acc.md#insn-00b61b0c) · [`00b61b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61acc.md#insn-00b61b24) · [`00b61ae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61acc.md#insn-00b61ae0)
- 新版 [`00b61bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md#insn-00b61bd4) · [`00b61bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md#insn-00b61bec) · [`00b61ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61b94.md#insn-00b61ba8)

~~~diff
- 00b61b0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61b0c ["INT_ADD", "register:40f0:8", ["const:b61b0c:8", "const:4:8"]]
- 00b61b0c ["CALLIND", null, ["register:0:8"]]
+ 00b61bd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61bd4 ["INT_ADD", "register:40f0:8", ["const:b61bd4:8", "const:4:8"]]
+ 00b61bd4 ["CALLIND", null, ["register:0:8"]]
- 00b61b0c bytes 00013fd6
+ 00b61bd4 bytes 00013fd6
- 00b61b24 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61b24 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4e8:8"]]
- 00b61b24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b61bec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b61bec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b61bec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61b24 bytes a0a21339
+ 00b61bec bytes a0a21639
- 00b61ae0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4e8:8"]]
- 00b61ae0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61ae0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b61ba8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b61ba8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b61ba8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61ae0 bytes a8a25339
+ 00b61ba8 bytes a8a25639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b0d7a232cb156be823f6e3f3dc28329"></a>

### [`00b61ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ba8.md) → [`00b61c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c70.md) _ZN8firebase4auth15email_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00b61be8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61cb0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61bc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61bbc",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61bc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61cb4"
      ]
    ],
    [
      "unmatched:00b61bcc",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b61c84",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61c8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61cb4"
      ]
    ],
    [
      "00b61c94",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ba8.md#insn-00b61bc4) · [`00b61be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ba8.md#insn-00b61be0) · [`00b61be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ba8.md#insn-00b61be8)
- 新版 [`00b61ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61c70.md#insn-00b61ca8)

~~~diff
- 00b61bc4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61bc4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61bc4 bytes 410100b5
- 00b61be0 ["INT_ADD", "register:40f0:8", ["const:b61be0:8", "const:4:8"]]
- 00b61be0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61ca8 ["INT_ADD", "register:40f0:8", ["const:b61ca8:8", "const:4:8"]]
+ 00b61ca8 ["CALL", null, ["callee:00bde040:8"]]
- 00b61be0 bytes ecf00194
+ 00b61ca8 bytes e6f00194
- 00b61be8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e0:8"]]
- 00b61be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61be8 bytes 807202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec7a2692c19cbe8944dcb5391c57feed"></a>

### [`00b61c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c54.md) → [`00b61d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d1c.md) _ZN8firebase4auth15email_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00b61c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61d5c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61c68",
      "READ",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61c70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61d60"
      ]
    ],
    [
      "unmatched:00b61c78",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b61d30",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61d60"
      ]
    ],
    [
      "00b61d40",
      "PARAM",
      [
        "storage",
        "00292534",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c54.md#insn-00b61c70) · [`00b61c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c54.md#insn-00b61c8c) · [`00b61c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61c54.md#insn-00b61c94)
- 新版 [`00b61d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61d1c.md#insn-00b61d54)

~~~diff
- 00b61c70 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61c70 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61c70 bytes 410100b5
- 00b61c8c ["INT_ADD", "register:40f0:8", ["const:b61c8c:8", "const:4:8"]]
- 00b61c8c ["CALL", null, ["callee:00bde040:8"]]
+ 00b61d54 ["INT_ADD", "register:40f0:8", ["const:b61d54:8", "const:4:8"]]
+ 00b61d54 ["CALL", null, ["callee:00bde040:8"]]
- 00b61c8c bytes c1f00194
+ 00b61d54 bytes bbf00194
- 00b61c94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e0:8"]]
- 00b61c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61c94 bytes 807202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a070910650c2967a15467d01bc12a1b2"></a>

### [`00b61d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d00.md) → [`00b61dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b61df4",
      "incomplete_value": true,
      "site": "00b61df4",
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
    "old": {
      "definition_site": "00b61d2c",
      "incomplete_value": true,
      "site": "00b61d2c",
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
            "const:500:8"
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
      "definition_site": "00b61ddc",
      "incomplete_value": true,
      "site": "00b61ddc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61d14",
      "incomplete_value": true,
      "site": "00b61d14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61de8",
      "incomplete_value": false,
      "site": "00b61dec",
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
            "const:8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61d20",
      "incomplete_value": false,
      "site": "00b61d24",
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
            "const:fff:8"
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
      "00b61dd8",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61de8",
      "PARAM",
      [
        "storage",
        "0029efff",
        null,
        "string"
      ]
    ],
    [
      "00b61df4",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61dd8",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61de8",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61df4",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d00.md#insn-00b61d24) · [`00b61d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d00.md#insn-00b61d2c) · [`00b61d10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d00.md#insn-00b61d10)
- 新版 [`00b61dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md#insn-00b61dec) · [`00b61df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md#insn-00b61df4) · [`00b61dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61dc8.md#insn-00b61dd8)

~~~diff
- 00b61d24 ["INT_ADD", "register:40f0:8", ["const:b61d24:8", "const:4:8"]]
- 00b61d24 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61dec ["INT_ADD", "register:40f0:8", ["const:b61dec:8", "const:4:8"]]
+ 00b61dec ["CALL", null, ["callee:00bde040:8"]]
- 00b61d24 bytes 9bf00194
+ 00b61dec bytes 95f00194
- 00b61d2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61df4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61d2c bytes 608202f9
+ 00b61df4 bytes 60e202f9
- 00b61d10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61d10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61d10 bytes 688242f9
+ 00b61dd8 bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80e59bbb57bd0408fae07fc3b548ef55"></a>

### [`00b61d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d40.md) → [`00b61e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b61e34",
      "incomplete_value": true,
      "site": "00b61e34",
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
    "old": {
      "definition_site": "00b61d6c",
      "incomplete_value": true,
      "site": "00b61d6c",
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
            "const:500:8"
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
      "definition_site": "00b61e1c",
      "incomplete_value": true,
      "site": "00b61e1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61d54",
      "incomplete_value": true,
      "site": "00b61d54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61e24",
      "incomplete_value": false,
      "site": "00b61e2c",
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
            "const:8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61d5c",
      "incomplete_value": false,
      "site": "00b61d64",
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
            "const:fff:8"
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
      "00b61e18",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e24",
      "PARAM",
      [
        "storage",
        "0029efff",
        null,
        "string"
      ]
    ],
    [
      "00b61e34",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61e18",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e24",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61e34",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d40.md#insn-00b61d64) · [`00b61d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d40.md#insn-00b61d6c) · [`00b61d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d40.md#insn-00b61d50)
- 新版 [`00b61e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md#insn-00b61e2c) · [`00b61e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md#insn-00b61e34) · [`00b61e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e08.md#insn-00b61e18)

~~~diff
- 00b61d64 ["INT_ADD", "register:40f0:8", ["const:b61d64:8", "const:4:8"]]
- 00b61d64 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61e2c ["INT_ADD", "register:40f0:8", ["const:b61e2c:8", "const:4:8"]]
+ 00b61e2c ["CALL", null, ["callee:00bde040:8"]]
- 00b61d64 bytes 8bf00194
+ 00b61e2c bytes 85f00194
- 00b61d6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61d6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61d6c bytes 608202f9
+ 00b61e34 bytes 60e202f9
- 00b61d50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61d50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61e18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61e18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61d50 bytes 688242f9
+ 00b61e18 bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3b7bdfa4e0a4f9c2b285bd658a86e9"></a>

### [`00b61d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d80.md) → [`00b61e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e48.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00b61db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61e78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b61e5c",
      "incomplete_value": true,
      "site": "00b61e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61d94",
      "incomplete_value": true,
      "site": "00b61d94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b61e58",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61da0",
      "PARAM",
      [
        "storage",
        "0029efff",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61da8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b61e58",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61e68",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61e70",
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

- 旧版 [`00b61d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d80.md#insn-00b61d94) · [`00b61da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d80.md#insn-00b61da8) · [`00b61db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61d80.md#insn-00b61db0)
- 新版 [`00b61e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e48.md#insn-00b61e5c)

~~~diff
- 00b61d94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61d94 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b61e5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b61e5c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61d94 bytes 080100b5
+ 00b61e5c bytes 080100b5
- 00b61da8 ["INT_ADD", "register:40f0:8", ["const:b61da8:8", "const:4:8"]]
- 00b61da8 ["CALL", null, ["callee:00bde040:8"]]
- 00b61da8 bytes 7af00194
- 00b61db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61db0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61db0 bytes 608202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad85bb1c9005ff1ade730fb0610ddccc"></a>

### [`00b61dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61dc4.md) → [`00b61e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61ebc",
      "incomplete_value": true,
      "site": "00b61ebc",
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
    "old": {
      "definition_site": "00b61df4",
      "incomplete_value": true,
      "site": "00b61df4",
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
            "const:500:8"
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
      "definition_site": "00b61ea0",
      "incomplete_value": true,
      "site": "00b61ea0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61dd8",
      "incomplete_value": true,
      "site": "00b61dd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61ea8",
      "incomplete_value": false,
      "site": "00b61eb4",
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
            "const:8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61de0",
      "incomplete_value": false,
      "site": "00b61dec",
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
            "const:fff:8"
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
      "00b61e9c",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61ea8",
      "PARAM",
      [
        "storage",
        "0029efff",
        null,
        "string"
      ]
    ],
    [
      "00b61ebc",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61e9c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61ea8",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61ebc",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61dc4.md#insn-00b61dec) · [`00b61df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61dc4.md#insn-00b61df4) · [`00b61dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61dc4.md#insn-00b61dd4)
- 新版 [`00b61eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md#insn-00b61eb4) · [`00b61ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md#insn-00b61ebc) · [`00b61e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61e8c.md#insn-00b61e9c)

~~~diff
- 00b61dec ["INT_ADD", "register:40f0:8", ["const:b61dec:8", "const:4:8"]]
- 00b61dec ["CALL", null, ["callee:00bde040:8"]]
+ 00b61eb4 ["INT_ADD", "register:40f0:8", ["const:b61eb4:8", "const:4:8"]]
+ 00b61eb4 ["CALL", null, ["callee:00bde040:8"]]
- 00b61dec bytes 69f00194
+ 00b61eb4 bytes 63f00194
- 00b61df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61df4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61ebc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61ebc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61df4 bytes 608202f9
+ 00b61ebc bytes 60e202f9
- 00b61dd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b61dd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61e9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61dd4 bytes 688242f9
+ 00b61e9c bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b74b917c3962c5f7d824ae0fed0535d"></a>

### [`00b61e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e14.md) → [`00b61edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md) _ZN8firebase4auth23weak_password_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b61f34",
      "incomplete_value": true,
      "site": "00b61f34",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e6c",
      "incomplete_value": true,
      "site": "00b61e6c",
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
            "const:508:8"
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
      "definition_site": "00b61f10",
      "incomplete_value": true,
      "site": "00b61f1c",
      "value": [
        "LOAD",
        "8",
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e48",
      "incomplete_value": true,
      "site": "00b61e54",
      "value": [
        "LOAD",
        "8",
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
                "const:500:8"
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
      "00b61ef0",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61f10",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61f34",
      "WRITE",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61ef0",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61f10",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61f34",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e14.md#insn-00b61e54) · [`00b61e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e14.md#insn-00b61e6c) · [`00b61e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e14.md#insn-00b61e28)
- 新版 [`00b61f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md#insn-00b61f1c) · [`00b61f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md#insn-00b61f34) · [`00b61ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61edc.md#insn-00b61ef0)

~~~diff
- 00b61e54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61e54 ["INT_ADD", "register:40f0:8", ["const:b61e54:8", "const:4:8"]]
- 00b61e54 ["CALLIND", null, ["register:0:8"]]
+ 00b61f1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61f1c ["INT_ADD", "register:40f0:8", ["const:b61f1c:8", "const:4:8"]]
+ 00b61f1c ["CALLIND", null, ["register:0:8"]]
- 00b61e54 bytes 00013fd6
+ 00b61f1c bytes 00013fd6
- 00b61e6c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61e6c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:508:8"]]
- 00b61e6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b61f34 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b61f34 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b61f34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61e6c bytes a0221439
+ 00b61f34 bytes a0221739
- 00b61e28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
- 00b61e28 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61e28 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b61ef0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b61ef0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b61ef0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61e28 bytes a8225439
+ 00b61ef0 bytes a8225739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7401414526d7f69ebce203ab266083ec"></a>

### [`00b61e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e80.md) → [`00b61f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61f48.md) _ZN8firebase4auth23weak_password_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 33.33% / 新版 28.57%

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
      "site": "00b61ebc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61edc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b61f84"
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
      "00b61f5c",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61f68",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61ec0"
      ]
    ]
  ],
  "added": [
    [
      "00b61f5c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61f68",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b61f88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e80.md#insn-00b61e98) · [`00b61ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e80.md#insn-00b61ebc) · [`00b61ec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61e80.md#insn-00b61ec4)
- 新版 [`00b61f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61f48.md#insn-00b61f60)

~~~diff
- 00b61e98 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61e98 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b61f60 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b61f60 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b61e98 bytes 410200b4
+ 00b61f60 bytes 410200b4
- 00b61ebc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61ebc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61ebc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:508:8"]]
- 00b61ebc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61ebc bytes bf221439
- 00b61ec4 ["INT_ADD", "register:40f0:8", ["const:b61ec4:8", "const:4:8"]]
- 00b61ec4 ["CALL", null, ["callee:00bde090:8"]]
- 00b61ec4 bytes 47f00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f09b447d695d07e51706c44ba14b629"></a>

### [`00b61ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ef0.md) → [`00b61fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md) _ZN8firebase4auth23weak_password_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61ff8",
      "incomplete_value": true,
      "site": "00b61ff8",
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
    "old": {
      "definition_site": "00b61f30",
      "incomplete_value": true,
      "site": "00b61f30",
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
            "const:500:8"
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
      "definition_site": "00b61fd4",
      "incomplete_value": true,
      "site": "00b61fd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61f0c",
      "incomplete_value": true,
      "site": "00b61f0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b61fdc",
      "incomplete_value": false,
      "site": "00b61ff0",
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
            "const:8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61f14",
      "incomplete_value": false,
      "site": "00b61f28",
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
            "const:fff:8"
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
      "00b61fcc",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61fdc",
      "PARAM",
      [
        "storage",
        "0029efff",
        null,
        "string"
      ]
    ],
    [
      "00b61ff8",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61fcc",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61fdc",
      "PARAM",
      [
        "storage",
        "0029f08c",
        null,
        "string"
      ]
    ],
    [
      "00b61ff8",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ef0.md#insn-00b61f28) · [`00b61f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ef0.md#insn-00b61f30) · [`00b61f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61ef0.md#insn-00b61f04)
- 新版 [`00b61ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md#insn-00b61ff0) · [`00b61ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md#insn-00b61ff8) · [`00b61fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61fb8.md#insn-00b61fcc)

~~~diff
- 00b61f28 ["INT_ADD", "register:40f0:8", ["const:b61f28:8", "const:4:8"]]
- 00b61f28 ["CALL", null, ["callee:00bde040:8"]]
+ 00b61ff0 ["INT_ADD", "register:40f0:8", ["const:b61ff0:8", "const:4:8"]]
+ 00b61ff0 ["CALL", null, ["callee:00bde040:8"]]
- 00b61f28 bytes 1af00194
+ 00b61ff0 bytes 14f00194
- 00b61f30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b61f30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61ff8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b61ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61f30 bytes 808202f9
+ 00b61ff8 bytes 80e202f9
- 00b61f04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b61f04 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61fcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b61fcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61f04 bytes 818242f9
+ 00b61fcc bytes 81e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da2141f4cd79e8c2fbb0f321d595cba7"></a>

### [`00b61f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f60.md) → [`00b62028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md) _ZN8firebase4auth23weak_password_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62044",
      "incomplete_value": false,
      "site": "00b62048",
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
      "definition_site": "00b61f7c",
      "incomplete_value": false,
      "site": "00b61f80",
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
      "definition_site": "00b62054",
      "incomplete_value": true,
      "site": "00b62060",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61f8c",
      "incomplete_value": true,
      "site": "00b61f98",
      "value": [
        "LOAD",
        "8",
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
      "00b62044",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62054",
      "DATA",
      [
        "storage",
        "010a1510",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62044",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62054",
      "DATA",
      [
        "storage",
        "010a15d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f60.md#insn-00b61f80) · [`00b61f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f60.md#insn-00b61f7c) · [`00b61f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f60.md#insn-00b61f88)
- 新版 [`00b62048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md#insn-00b62048) · [`00b62044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md#insn-00b62044) · [`00b62050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62028.md#insn-00b62050)

~~~diff
- 00b61f80 ["INT_ADD", "register:40f0:8", ["const:b61f80:8", "const:4:8"]]
- 00b61f80 ["CALL", null, ["callee:00bde130:8"]]
+ 00b62048 ["INT_ADD", "register:40f0:8", ["const:b62048:8", "const:4:8"]]
+ 00b62048 ["CALL", null, ["callee:00bde130:8"]]
- 00b61f80 bytes 40f00194
+ 00b62048 bytes 3af00194
- 00b61f7c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b61f7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61f7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61f7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62044 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b62044 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62044 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62044 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61f7c bytes 001c1591
+ 00b62044 bytes 00501791
- 00b61f88 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00b61f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62050 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00b62050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61f88 bytes 08411491
+ 00b62050 bytes 08411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-850782e55365dfcc15f80410f5b47b19"></a>

### [`00b61f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f9c.md) → [`00b62064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62064.md) _ZN8firebase4auth23weak_password_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b61f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61f9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61fa0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61fb0",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62064",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b62068",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62078",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61f9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f9c.md#insn-00b61f9c) · [`00b61fa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f9c.md#insn-00b61fa0) · [`00b61fb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b61/00b61f9c.md#insn-00b61fb8)

~~~diff
- 00b61f9c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61f9c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61f9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b61f9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61f9c bytes f44fbea9
- 00b61fa0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61fa0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61fa0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61fa0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61fa0 bytes fd7b01a9
- 00b61fb8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61fb8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61fb8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d0496abd258d82e26e38c3d68ce9505"></a>

### [`00b62048`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62048.md) → [`00b62110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62110.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b62074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6213c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62124",
      "incomplete_value": true,
      "site": "00b62124",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6205c",
      "incomplete_value": true,
      "site": "00b6205c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62120",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b62078"
      ]
    ],
    [
      "unmatched:00b62068",
      "PARAM",
      [
        "storage",
        "002a8fb1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b62120",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62124",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62140"
      ]
    ],
    [
      "00b62130",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6206c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62048.md#insn-00b6206c) · [`00b62074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62048.md#insn-00b62074) · [`00b62084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62048.md#insn-00b62084)

~~~diff
- 00b6206c ["INT_ADD", "register:40f0:8", ["const:b6206c:8", "const:4:8"]]
- 00b6206c ["CALL", null, ["callee:00bde040:8"]]
- 00b6206c bytes c9ef0194
- 00b62074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:520:8"]]
- 00b62074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62074 bytes 609202f9
- 00b62084 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b62084 ["RETURN", null, ["register:0:8"]]
- 00b62084 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1612231661597a80e265c501c885a511"></a>

### [`00b62088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62088.md) → [`00b62150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62150.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b62088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6208c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6208c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62088",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6208c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62160",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62150",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b62154",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b62160",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62088.md#insn-00b62088) · [`00b6208c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62088.md#insn-00b6208c) · [`00b6209c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62088.md#insn-00b6209c)
- 新版 [`00b62164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62150.md#insn-00b62164)

~~~diff
- 00b62088 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b62088 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b62088 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b62088 bytes f30f1ef8
- 00b6208c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6208c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6208c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6208c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6208c bytes fd7b01a9
- 00b6209c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6209c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b62164 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b62164 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6209c bytes e80000b5
+ 00b62164 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19ede2cb84968321442561f88caa7584"></a>

### [`00b6210c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6210c.md) → [`00b621d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b6213c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b62204"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b621e8",
      "incomplete_value": true,
      "site": "00b621e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62120",
      "incomplete_value": true,
      "site": "00b62120",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b621e4",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62128",
      "PARAM",
      [
        "storage",
        "002a8fb1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6213c",
      "WRITE",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b621e4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b621f0",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62204",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6210c.md#insn-00b62120) · [`00b62134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6210c.md#insn-00b62134) · [`00b6213c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6210c.md#insn-00b6213c)
- 新版 [`00b621e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md#insn-00b621e8) · [`00b621fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b621d4.md#insn-00b621fc)

~~~diff
- 00b62120 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62120 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b621e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b621e8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b62120 bytes 080100b5
+ 00b621e8 bytes 080100b5
- 00b62134 ["INT_ADD", "register:40f0:8", ["const:b62134:8", "const:4:8"]]
- 00b62134 ["CALL", null, ["callee:00bde040:8"]]
+ 00b621fc ["INT_ADD", "register:40f0:8", ["const:b621fc:8", "const:4:8"]]
+ 00b621fc ["CALL", null, ["callee:00bde040:8"]]
- 00b62134 bytes 97ef0194
+ 00b621fc bytes 91ef0194
- 00b6213c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:520:8"]]
- 00b6213c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6213c bytes 609202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f7e7454d7c60be854c85ce6e51fa12"></a>

### [`00b62238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62238.md) → [`00b62300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md) _ZN8firebase4auth29invalid_credentials_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b62340",
      "incomplete_value": true,
      "site": "00b62340",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62278",
      "incomplete_value": true,
      "site": "00b62278",
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
            "const:520:8"
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
      "definition_site": "00b6231c",
      "incomplete_value": true,
      "site": "00b6231c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62254",
      "incomplete_value": true,
      "site": "00b62254",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62260",
      "incomplete_value": true,
      "site": "00b62270",
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
      "00b62314",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6225c",
      "PARAM",
      [
        "storage",
        "002a8fb1",
        null,
        "string"
      ]
    ],
    [
      "00b62340",
      "WRITE",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62314",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62324",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ],
    [
      "00b62340",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62238.md#insn-00b62270) · [`00b62278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62238.md#insn-00b62278) · [`00b6224c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62238.md#insn-00b6224c)
- 新版 [`00b62338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md#insn-00b62338) · [`00b62340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md#insn-00b62340) · [`00b62314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62300.md#insn-00b62314)

~~~diff
- 00b62270 ["INT_ADD", "register:40f0:8", ["const:b62270:8", "const:4:8"]]
- 00b62270 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62338 ["INT_ADD", "register:40f0:8", ["const:b62338:8", "const:4:8"]]
+ 00b62338 ["CALL", null, ["callee:00bde040:8"]]
- 00b62270 bytes 48ef0194
+ 00b62338 bytes 42ef0194
- 00b62278 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
- 00b62278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62340 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b62340 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62278 bytes 809202f9
+ 00b62340 bytes 80f202f9
- 00b6224c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
- 00b6224c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62314 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
+ 00b62314 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6224c bytes 819242f9
+ 00b62314 bytes 81f242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b407c34055cd5c959f5eccd1075f8b98"></a>

### [`00b622e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622e4.md) → [`00b623ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b623ac.md) _ZN8firebase4auth29invalid_credentials_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b62324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b623ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62300"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b622f8",
      "READ",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62300",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b623f0"
      ]
    ],
    [
      "unmatched:00b62308",
      "PARAM",
      [
        "storage",
        "002a8fb1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b623c0",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b623c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b623f0"
      ]
    ],
    [
      "00b623d0",
      "PARAM",
      [
        "storage",
        "002a8f1d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622e4.md#insn-00b62300) · [`00b6231c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622e4.md#insn-00b6231c) · [`00b62324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b622e4.md#insn-00b62324)
- 新版 [`00b623e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b623ac.md#insn-00b623e4)

~~~diff
- 00b62300 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b62300 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62300 bytes 410100b5
- 00b6231c ["INT_ADD", "register:40f0:8", ["const:b6231c:8", "const:4:8"]]
- 00b6231c ["CALL", null, ["callee:00bde040:8"]]
+ 00b623e4 ["INT_ADD", "register:40f0:8", ["const:b623e4:8", "const:4:8"]]
+ 00b623e4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6231c bytes 1def0194
+ 00b623e4 bytes 17ef0194
- 00b62324 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:520:8"]]
- 00b62324 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62324 bytes 809202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1670a8b0a1482e36db0da81384695371"></a>

### [`00b62390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62390.md) → [`00b62458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00b62484",
      "incomplete_value": true,
      "site": "00b62484",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b623bc",
      "incomplete_value": true,
      "site": "00b623bc",
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
            "const:540:8"
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
      "definition_site": "00b6246c",
      "incomplete_value": true,
      "site": "00b6246c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b623a4",
      "incomplete_value": true,
      "site": "00b623a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62478",
      "incomplete_value": false,
      "site": "00b6247c",
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
    "old": {
      "definition_site": "00b623b0",
      "incomplete_value": false,
      "site": "00b623b4",
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
            "const:4df:8"
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
      "00b62468",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62478",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00b62484",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62468",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62478",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ],
    [
      "00b62484",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b623b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62390.md#insn-00b623b4) · [`00b623bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62390.md#insn-00b623bc) · [`00b623a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62390.md#insn-00b623a0)
- 新版 [`00b6247c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md#insn-00b6247c) · [`00b62484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md#insn-00b62484) · [`00b62468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62458.md#insn-00b62468)

~~~diff
- 00b623b4 ["INT_ADD", "register:40f0:8", ["const:b623b4:8", "const:4:8"]]
- 00b623b4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6247c ["INT_ADD", "register:40f0:8", ["const:b6247c:8", "const:4:8"]]
+ 00b6247c ["CALL", null, ["callee:00bde040:8"]]
- 00b623b4 bytes f7ee0194
+ 00b6247c bytes f1ee0194
- 00b623bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b623bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b62484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b623bc bytes 60a202f9
+ 00b62484 bytes 600203f9
- 00b623a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b623a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
+ 00b62468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b623a0 bytes 68a242f9
+ 00b62468 bytes 680243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-172a2716ed58249db135857299b45586"></a>

### [`00b623d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b623d0.md) → [`00b62498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62498.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "site": "00b623d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b623d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b623d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b623d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b623d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b624a8",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62498",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6249c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b624a8",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b623d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b623d0.md#insn-00b623d0) · [`00b623d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b623d0.md#insn-00b623d4) · [`00b623e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b623d0.md#insn-00b623e4)
- 新版 [`00b624ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62498.md#insn-00b624ac)

~~~diff
- 00b623d0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b623d0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b623d0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b623d0 bytes f30f1ef8
- 00b623d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b623d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b623d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b623d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b623d4 bytes fd7b01a9
- 00b623e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b623e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b624ac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b624ac ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b623e4 bytes e80000b5
+ 00b624ac bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b1c436e961b65d75955519cce93ae6b"></a>

### [`00b62454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62454.md) → [`00b6251c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6251c.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b62484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6254c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62468"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6252c",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62550"
      ]
    ],
    [
      "unmatched:00b62470",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6252c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62530",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62550"
      ]
    ],
    [
      "00b62538",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62454.md#insn-00b62468) · [`00b6247c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62454.md#insn-00b6247c) · [`00b62484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62454.md#insn-00b62484)
- 新版 [`00b62544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6251c.md#insn-00b62544)

~~~diff
- 00b62468 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62468 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b62468 bytes 080100b5
- 00b6247c ["INT_ADD", "register:40f0:8", ["const:b6247c:8", "const:4:8"]]
- 00b6247c ["CALL", null, ["callee:00bde040:8"]]
+ 00b62544 ["INT_ADD", "register:40f0:8", ["const:b62544:8", "const:4:8"]]
+ 00b62544 ["CALL", null, ["callee:00bde040:8"]]
- 00b6247c bytes c5ee0194
+ 00b62544 bytes bfee0194
- 00b62484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b62484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62484 bytes 60a202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89d7be1bcdd477140e40634fda778bd8"></a>

### [`00b624a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b624a4.md) → [`00b6256c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md) _ZN8firebase4auth22invalid_user_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "site": "00b624fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b625c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b625a0",
      "incomplete_value": true,
      "site": "00b625ac",
      "value": [
        "LOAD",
        "8",
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
                "const:600:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624d8",
      "incomplete_value": true,
      "site": "00b624e4",
      "value": [
        "LOAD",
        "8",
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
                "const:540:8"
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
      "00b62580",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b624d8",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b624fc",
      "WRITE",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62580",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b625a0",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b625c4",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b624e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b624a4.md#insn-00b624e4) · [`00b624fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b624a4.md#insn-00b624fc)
- 新版 [`00b625ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md#insn-00b625ac) · [`00b625c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b6256c.md#insn-00b625c4)

~~~diff
- 00b624e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b624e4 ["INT_ADD", "register:40f0:8", ["const:b624e4:8", "const:4:8"]]
- 00b624e4 ["CALLIND", null, ["register:0:8"]]
+ 00b625ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b625ac ["INT_ADD", "register:40f0:8", ["const:b625ac:8", "const:4:8"]]
+ 00b625ac ["CALLIND", null, ["register:0:8"]]
- 00b624e4 bytes 00013fd6
+ 00b625ac bytes 00013fd6
- 00b624fc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b624fc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:548:8"]]
- 00b624fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b624fc bytes a0221539
+ 00b625c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b625c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:608:8"]]
+ 00b625c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b625c4 bytes a0221839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2d03b89a7c30c640c7d4b859ffa13f8"></a>

### [`00b62510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62510.md) → [`00b625d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md) _ZN8firebase4auth22invalid_user_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 28.57% / 新版 33.33%

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
      "site": "00b6254c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b62634",
      "incomplete_value": true,
      "site": "00b62634",
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
            "const:600:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6256c",
      "incomplete_value": true,
      "site": "00b6256c",
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
            "const:540:8"
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
      "site": "00b62614"
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
      "00b625ec",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62530",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b6254c",
      "WRITE",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b625ec",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b625f8",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62614",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62510.md#insn-00b62528) · [`00b6254c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62510.md#insn-00b6254c) · [`00b62568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62510.md#insn-00b62568)
- 新版 [`00b625f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md#insn-00b625f0) · [`00b62630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b625d8.md#insn-00b62630)

~~~diff
- 00b62528 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b62528 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b625f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b625f0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b62528 bytes 410200b4
+ 00b625f0 bytes 410200b4
- 00b6254c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6254c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6254c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:548:8"]]
- 00b6254c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6254c bytes bf221539
- 00b62568 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62568 ["INT_ADD", "register:40f0:8", ["const:b62568:8", "const:4:8"]]
- 00b62568 ["CALLIND", null, ["register:0:8"]]
+ 00b62630 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62630 ["INT_ADD", "register:40f0:8", ["const:b62630:8", "const:4:8"]]
+ 00b62630 ["CALLIND", null, ["register:0:8"]]
- 00b62568 bytes 00013fd6
+ 00b62630 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73d0e0a9a8f6a1c83905ecc4f23916ec"></a>

### [`00b62580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62580.md) → [`00b62648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62648.md) _ZN8firebase4auth22invalid_user_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b62580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62580"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62584"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62580",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62584",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62594",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62648",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6264c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6265c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62580.md#insn-00b62580) · [`00b62584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62580.md#insn-00b62584) · [`00b6259c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62580.md#insn-00b6259c)

~~~diff
- 00b62580 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b62580 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b62580 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b62580 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b62580 bytes f44fbea9
- 00b62584 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62584 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62584 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b62584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62584 bytes fd7b01a9
- 00b6259c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6259c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6259c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2ada6aec112701a0ec2cfdbea828abf"></a>

### [`00b625f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b625f0.md) → [`00b626b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md) _ZN8firebase4auth22invalid_user_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b626d4",
      "incomplete_value": false,
      "site": "00b626d8",
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
      "definition_site": "00b6260c",
      "incomplete_value": false,
      "site": "00b62610",
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
      "definition_site": "00b626e4",
      "incomplete_value": true,
      "site": "00b626f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6261c",
      "incomplete_value": true,
      "site": "00b62628",
      "value": [
        "LOAD",
        "8",
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
      "00b626d4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b626e4",
      "DATA",
      [
        "storage",
        "010a1550",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b626d4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b626e4",
      "DATA",
      [
        "storage",
        "010a1610",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b625f0.md#insn-00b62610) · [`00b6260c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b625f0.md#insn-00b6260c) · [`00b62618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b625f0.md#insn-00b62618)
- 新版 [`00b626d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md#insn-00b626d8) · [`00b626d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md#insn-00b626d4) · [`00b626e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626b8.md#insn-00b626e0)

~~~diff
- 00b62610 ["INT_ADD", "register:40f0:8", ["const:b62610:8", "const:4:8"]]
- 00b62610 ["CALL", null, ["callee:00bde130:8"]]
+ 00b626d8 ["INT_ADD", "register:40f0:8", ["const:b626d8:8", "const:4:8"]]
+ 00b626d8 ["CALL", null, ["callee:00bde130:8"]]
- 00b62610 bytes 9cee0194
+ 00b626d8 bytes 96ee0194
- 00b6260c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6260c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6260c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6260c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b626d4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b626d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b626d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b626d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6260c bytes 001c1591
+ 00b626d4 bytes 00501791
- 00b62618 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00b62618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b626e0 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 00b626e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b626e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b626e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62618 bytes 08411591
+ 00b626e0 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b837054268a651ac602cdcb2c56ec04"></a>

### [`00b6262c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6262c.md) → [`00b626f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626f4.md) _ZN8firebase4auth22invalid_user_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b6266c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b62734"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62640",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62738"
      ]
    ],
    [
      "unmatched:00b62650",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b62708",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62738"
      ]
    ],
    [
      "00b62718",
      "PARAM",
      [
        "storage",
        "0029256c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6262c.md#insn-00b62648) · [`00b62664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6262c.md#insn-00b62664) · [`00b6266c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6262c.md#insn-00b6266c)
- 新版 [`00b6272c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b626f4.md#insn-00b6272c)

~~~diff
- 00b62648 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b62648 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b62648 bytes 410100b5
- 00b62664 ["INT_ADD", "register:40f0:8", ["const:b62664:8", "const:4:8"]]
- 00b62664 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6272c ["INT_ADD", "register:40f0:8", ["const:b6272c:8", "const:4:8"]]
+ 00b6272c ["CALL", null, ["callee:00bde040:8"]]
- 00b62664 bytes 4bee0194
+ 00b6272c bytes 45ee0194
- 00b6266c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:540:8"]]
- 00b6266c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6266c bytes 80a202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-148e84abceec52eef9d65bff07748cab"></a>

### [`00b626d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b626d8.md) → [`00b627a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627a0.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "site": "00b626d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b626dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b626d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b626dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b627b0",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b627a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b627a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b627b0",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b626d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b626d8.md#insn-00b626d8) · [`00b626dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b626d8.md#insn-00b626dc) · [`00b626ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b626d8.md#insn-00b626ec)
- 新版 [`00b627b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627a0.md#insn-00b627b4)

~~~diff
- 00b626d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b626d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b626d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b626d8 bytes f30f1ef8
- 00b626dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b626dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b626dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b626dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b626dc bytes fd7b01a9
- 00b626ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b626ec ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b627b4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b627b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b626ec bytes e80000b5
+ 00b627b4 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-732480f71336db1693d61399e2005bba"></a>

### [`00b62718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62718.md) → [`00b627e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627e0.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "site": "00b62744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6280c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b627f4",
      "incomplete_value": true,
      "site": "00b627f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6272c",
      "incomplete_value": true,
      "site": "00b6272c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b627f0",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62734",
      "PARAM",
      [
        "storage",
        "002ab1d7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6273c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b627f0",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b627fc",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00b62804",
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

- 旧版 [`00b6272c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62718.md#insn-00b6272c) · [`00b6273c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62718.md#insn-00b6273c) · [`00b62744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62718.md#insn-00b62744)
- 新版 [`00b627f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b627e0.md#insn-00b627f4)

~~~diff
- 00b6272c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6272c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b627f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b627f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6272c bytes e80000b5
+ 00b627f4 bytes e80000b5
- 00b6273c ["INT_ADD", "register:40f0:8", ["const:b6273c:8", "const:4:8"]]
- 00b6273c ["CALL", null, ["callee:00bde040:8"]]
- 00b6273c bytes 15ee0194
- 00b62744 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b62744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62744 bytes 60b202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa33fff3f9e18de8689c296b4a56077"></a>

### [`00b62758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62758.md) → [`00b62820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62850",
      "incomplete_value": true,
      "site": "00b62850",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62788",
      "incomplete_value": true,
      "site": "00b62788",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62834",
      "incomplete_value": true,
      "site": "00b62834",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6276c",
      "incomplete_value": true,
      "site": "00b6276c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62840",
      "incomplete_value": false,
      "site": "00b62848",
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
            "const:1dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62778",
      "incomplete_value": false,
      "site": "00b62780",
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
            "const:1d7:8"
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
      "00b62830",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62840",
      "PARAM",
      [
        "storage",
        "002ab1d7",
        null,
        "string"
      ]
    ],
    [
      "00b62850",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62830",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62840",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00b62850",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62758.md#insn-00b62780) · [`00b62788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62758.md#insn-00b62788) · [`00b62768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62758.md#insn-00b62768)
- 新版 [`00b62848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md#insn-00b62848) · [`00b62850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md#insn-00b62850) · [`00b62830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62820.md#insn-00b62830)

~~~diff
- 00b62780 ["INT_ADD", "register:40f0:8", ["const:b62780:8", "const:4:8"]]
- 00b62780 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62848 ["INT_ADD", "register:40f0:8", ["const:b62848:8", "const:4:8"]]
+ 00b62848 ["CALL", null, ["callee:00bde040:8"]]
- 00b62780 bytes 04ee0194
+ 00b62848 bytes feed0194
- 00b62788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b62788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62788 bytes 60b202f9
+ 00b62850 bytes 601203f9
- 00b62768 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b62768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
+ 00b62830 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62768 bytes 68b242f9
+ 00b62830 bytes 681243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c57cd605b826da45a47b595e3272deda"></a>

### [`00b6279c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6279c.md) → [`00b62864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62864.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "site": "00b627cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b62894"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62878",
      "incomplete_value": true,
      "site": "00b62878",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b627b0",
      "incomplete_value": true,
      "site": "00b627b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62874",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b627d0"
      ]
    ],
    [
      "unmatched:00b627b8",
      "PARAM",
      [
        "storage",
        "002ab1d7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b62874",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b62898"
      ]
    ],
    [
      "00b62880",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b627c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6279c.md#insn-00b627c4) · [`00b627cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6279c.md#insn-00b627cc) · [`00b627dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b6279c.md#insn-00b627dc)
- 新版 [`00b6288c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62864.md#insn-00b6288c)

~~~diff
- 00b627c4 ["INT_ADD", "register:40f0:8", ["const:b627c4:8", "const:4:8"]]
- 00b627c4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6288c ["INT_ADD", "register:40f0:8", ["const:b6288c:8", "const:4:8"]]
+ 00b6288c ["CALL", null, ["callee:00bde040:8"]]
- 00b627c4 bytes f3ed0194
+ 00b6288c bytes eded0194
- 00b627cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b627cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b627cc bytes 60b202f9
- 00b627dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b627dc ["RETURN", null, ["register:0:8"]]
- 00b627dc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e22d71887387064cc351e7b4879319"></a>

### [`00b627ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b627ec.md) → [`00b628b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md) _ZN8firebase4auth31recent_login_required_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6290c",
      "incomplete_value": true,
      "site": "00b6290c",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62844",
      "incomplete_value": true,
      "site": "00b62844",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b628e8",
      "incomplete_value": true,
      "site": "00b628f4",
      "value": [
        "LOAD",
        "8",
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62820",
      "incomplete_value": true,
      "site": "00b6282c",
      "value": [
        "LOAD",
        "8",
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
                "const:560:8"
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
      "00b628c8",
      "READ",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ],
    [
      "00b628e8",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6290c",
      "WRITE",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b628c8",
      "READ",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ],
    [
      "00b628e8",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6290c",
      "WRITE",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6282c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b627ec.md#insn-00b6282c) · [`00b62844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b627ec.md#insn-00b62844) · [`00b62800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b627ec.md#insn-00b62800)
- 新版 [`00b628f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md#insn-00b628f4) · [`00b6290c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md#insn-00b6290c) · [`00b628c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b628b4.md#insn-00b628c8)

~~~diff
- 00b6282c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6282c ["INT_ADD", "register:40f0:8", ["const:b6282c:8", "const:4:8"]]
- 00b6282c ["CALLIND", null, ["register:0:8"]]
+ 00b628f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b628f4 ["INT_ADD", "register:40f0:8", ["const:b628f4:8", "const:4:8"]]
+ 00b628f4 ["CALLIND", null, ["register:0:8"]]
- 00b6282c bytes 00013fd6
+ 00b628f4 bytes 00013fd6
- 00b62844 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62844 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:568:8"]]
- 00b62844 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6290c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6290c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:628:8"]]
+ 00b6290c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62844 bytes a0a21539
+ 00b6290c bytes a0a21839
- 00b62800 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
- 00b62800 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62800 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b628c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:628:8"]]
+ 00b628c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b628c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62800 bytes a8a25539
+ 00b628c8 bytes a8a25839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65f65d491a17665ebebaa543c95f504d"></a>

### [`00b62858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62858.md) → [`00b62920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62920.md) _ZN8firebase4auth31recent_login_required_exception12ReleaseClassEP7_JNIEnv

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
      "site": "00b62858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6285c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6285c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62858",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6285c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62860",
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
      "00b62920",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b62924",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b62928",
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

- 旧版 [`00b62858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62858.md#insn-00b62858) · [`00b6285c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62858.md#insn-00b6285c) · [`00b62860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62858.md#insn-00b62860)

~~~diff
- 00b62858 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b62858 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b62858 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b62858 bytes f50f1df8
- 00b6285c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6285c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6285c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6285c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6285c bytes f44f01a9
- 00b62860 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62860 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62860 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b62860 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62860 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb92ae3a6731d29dff509702098a182c"></a>

### [`00b628c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b628c8.md) → [`00b62990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md) _ZN8firebase4auth31recent_login_required_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b629d0",
      "incomplete_value": true,
      "site": "00b629d0",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62908",
      "incomplete_value": true,
      "site": "00b62908",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b629ac",
      "incomplete_value": true,
      "site": "00b629ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b628e4",
      "incomplete_value": true,
      "site": "00b628e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b629b4",
      "incomplete_value": false,
      "site": "00b629c8",
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
            "const:1dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b628ec",
      "incomplete_value": false,
      "site": "00b62900",
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
            "const:1d7:8"
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
      "00b629a4",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b629b4",
      "PARAM",
      [
        "storage",
        "002ab1d7",
        null,
        "string"
      ]
    ],
    [
      "00b629d0",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b629a4",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b629b4",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00b629d0",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b628c8.md#insn-00b62900) · [`00b62908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b628c8.md#insn-00b62908) · [`00b628dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b628c8.md#insn-00b628dc)
- 新版 [`00b629c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md#insn-00b629c8) · [`00b629d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md#insn-00b629d0) · [`00b629a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62990.md#insn-00b629a4)

~~~diff
- 00b62900 ["INT_ADD", "register:40f0:8", ["const:b62900:8", "const:4:8"]]
- 00b62900 ["CALL", null, ["callee:00bde040:8"]]
+ 00b629c8 ["INT_ADD", "register:40f0:8", ["const:b629c8:8", "const:4:8"]]
+ 00b629c8 ["CALL", null, ["callee:00bde040:8"]]
- 00b62900 bytes a4ed0194
+ 00b629c8 bytes 9eed0194
- 00b62908 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b62908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b629d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b629d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62908 bytes 80b202f9
+ 00b629d0 bytes 801203f9
- 00b628dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b628dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b629a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b629a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b628dc bytes 81b242f9
+ 00b629a4 bytes 811243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b4275a9e79ab9754b18ae8eadfb4382"></a>

### [`00b62938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62938.md) → [`00b62a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md) _ZN8firebase4auth31recent_login_required_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62a1c",
      "incomplete_value": false,
      "site": "00b62a20",
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
      "definition_site": "00b62954",
      "incomplete_value": false,
      "site": "00b62958",
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
      "definition_site": "00b62a2c",
      "incomplete_value": true,
      "site": "00b62a38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62964",
      "incomplete_value": true,
      "site": "00b62970",
      "value": [
        "LOAD",
        "8",
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
      "00b62a1c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62a2c",
      "DATA",
      [
        "storage",
        "010a1570",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62a1c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62a2c",
      "DATA",
      [
        "storage",
        "010a1630",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62938.md#insn-00b62958) · [`00b62954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62938.md#insn-00b62954) · [`00b62960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62938.md#insn-00b62960)
- 新版 [`00b62a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md#insn-00b62a20) · [`00b62a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md#insn-00b62a1c) · [`00b62a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a00.md#insn-00b62a28)

~~~diff
- 00b62958 ["INT_ADD", "register:40f0:8", ["const:b62958:8", "const:4:8"]]
- 00b62958 ["CALL", null, ["callee:00bde130:8"]]
+ 00b62a20 ["INT_ADD", "register:40f0:8", ["const:b62a20:8", "const:4:8"]]
+ 00b62a20 ["CALL", null, ["callee:00bde130:8"]]
- 00b62958 bytes caed0194
+ 00b62a20 bytes c4ed0194
- 00b62954 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62a1c ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b62a1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62a1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62a1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62954 bytes 001c1591
+ 00b62a1c bytes 00501791
- 00b62960 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00b62960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62a28 ["COPY", "tmp:0:8", ["const:630:8"]]
+ 00b62a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62960 bytes 08c11591
+ 00b62a28 bytes 08c11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ad6ceafbd758415b76efe732167cadf"></a>

### [`00b62974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62974.md) → [`00b62a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md) _ZN8firebase4auth31recent_login_required_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62a7c",
      "incomplete_value": true,
      "site": "00b62a7c",
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
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629b4",
      "incomplete_value": true,
      "site": "00b629b4",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62a58",
      "incomplete_value": true,
      "site": "00b62a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62990",
      "incomplete_value": true,
      "site": "00b62990",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62a60",
      "incomplete_value": false,
      "site": "00b62a74",
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
            "const:1dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62998",
      "incomplete_value": false,
      "site": "00b629ac",
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
            "const:1d7:8"
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
      "00b62a50",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62a60",
      "PARAM",
      [
        "storage",
        "002ab1d7",
        null,
        "string"
      ]
    ],
    [
      "00b62a7c",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62a50",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62a60",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00b62a7c",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b629ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62974.md#insn-00b629ac) · [`00b629b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62974.md#insn-00b629b4) · [`00b62988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62974.md#insn-00b62988)
- 新版 [`00b62a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md#insn-00b62a74) · [`00b62a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md#insn-00b62a7c) · [`00b62a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62a3c.md#insn-00b62a50)

~~~diff
- 00b629ac ["INT_ADD", "register:40f0:8", ["const:b629ac:8", "const:4:8"]]
- 00b629ac ["CALL", null, ["callee:00bde040:8"]]
+ 00b62a74 ["INT_ADD", "register:40f0:8", ["const:b62a74:8", "const:4:8"]]
+ 00b62a74 ["CALL", null, ["callee:00bde040:8"]]
- 00b629ac bytes 79ed0194
+ 00b62a74 bytes 73ed0194
- 00b629b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b629b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b62a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b629b4 bytes 80b202f9
+ 00b62a7c bytes 801203f9
- 00b62988 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b62988 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
+ 00b62a50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62988 bytes 81b242f9
+ 00b62a50 bytes 811243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c2197a7f419b29f8b312e5ceaf689e8"></a>

### [`00b629e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b629e4.md) → [`00b62aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md) _ZN8firebase4auth31recent_login_required_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b62ac8",
      "incomplete_value": false,
      "site": "00b62acc",
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
      "definition_site": "00b62a00",
      "incomplete_value": false,
      "site": "00b62a04",
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
      "definition_site": "00b62ad8",
      "incomplete_value": true,
      "site": "00b62ae4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62a10",
      "incomplete_value": true,
      "site": "00b62a1c",
      "value": [
        "LOAD",
        "8",
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
      "00b62ac8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b62ad8",
      "DATA",
      [
        "storage",
        "010a1578",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62ac8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b62ad8",
      "DATA",
      [
        "storage",
        "010a1638",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b629e4.md#insn-00b62a04) · [`00b62a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b629e4.md#insn-00b62a00) · [`00b62a0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b629e4.md#insn-00b62a0c)
- 新版 [`00b62acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md#insn-00b62acc) · [`00b62ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md#insn-00b62ac8) · [`00b62ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62aac.md#insn-00b62ad4)

~~~diff
- 00b62a04 ["INT_ADD", "register:40f0:8", ["const:b62a04:8", "const:4:8"]]
- 00b62a04 ["CALL", null, ["callee:00bde130:8"]]
+ 00b62acc ["INT_ADD", "register:40f0:8", ["const:b62acc:8", "const:4:8"]]
+ 00b62acc ["CALL", null, ["callee:00bde130:8"]]
- 00b62a04 bytes 9fed0194
+ 00b62acc bytes 99ed0194
- 00b62a00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b62a00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62a00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62a00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62ac8 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b62ac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62ac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62ac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62a00 bytes 00c81791
+ 00b62ac8 bytes 00fc1991
- 00b62a0c ["COPY", "tmp:0:8", ["const:578:8"]]
- 00b62a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62ad4 ["COPY", "tmp:0:8", ["const:638:8"]]
+ 00b62ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62a0c bytes 08e11591
+ 00b62ad4 bytes 08e11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c556cff267a7d05e205044afc2245189"></a>

### [`00b62a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a20.md) → [`00b62ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

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
      "definition_site": "00b62b14",
      "incomplete_value": true,
      "site": "00b62b14",
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
    "old": {
      "definition_site": "00b62a4c",
      "incomplete_value": true,
      "site": "00b62a4c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62afc",
      "incomplete_value": true,
      "site": "00b62afc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62a34",
      "incomplete_value": true,
      "site": "00b62a34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62b08",
      "incomplete_value": false,
      "site": "00b62b0c",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a40",
      "incomplete_value": false,
      "site": "00b62a44",
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
            "const:443:8"
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
      "00b62af8",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b08",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62b14",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62af8",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b08",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62b14",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a20.md#insn-00b62a44) · [`00b62a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a20.md#insn-00b62a4c) · [`00b62a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a20.md#insn-00b62a30)
- 新版 [`00b62b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md#insn-00b62b0c) · [`00b62b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md#insn-00b62b14) · [`00b62af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ae8.md#insn-00b62af8)

~~~diff
- 00b62a44 ["INT_ADD", "register:40f0:8", ["const:b62a44:8", "const:4:8"]]
- 00b62a44 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62b0c ["INT_ADD", "register:40f0:8", ["const:b62b0c:8", "const:4:8"]]
+ 00b62b0c ["CALL", null, ["callee:00bde040:8"]]
- 00b62a44 bytes 53ed0194
+ 00b62b0c bytes 4ded0194
- 00b62a4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62a4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62a4c bytes 60c202f9
+ 00b62b14 bytes 602203f9
- 00b62a30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62a30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62af8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62a30 bytes 68c242f9
+ 00b62af8 bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92dfbc06a9f165d78be08de340e02e51"></a>

### [`00b62a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a60.md) → [`00b62b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

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
      "definition_site": "00b62b54",
      "incomplete_value": true,
      "site": "00b62b54",
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
    "old": {
      "definition_site": "00b62a8c",
      "incomplete_value": true,
      "site": "00b62a8c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62b3c",
      "incomplete_value": true,
      "site": "00b62b3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62a74",
      "incomplete_value": true,
      "site": "00b62a74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62b44",
      "incomplete_value": false,
      "site": "00b62b4c",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a7c",
      "incomplete_value": false,
      "site": "00b62a84",
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
            "const:443:8"
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
      "00b62b38",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b44",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62b54",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62b38",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b44",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62b54",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a60.md#insn-00b62a84) · [`00b62a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a60.md#insn-00b62a8c) · [`00b62a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62a60.md#insn-00b62a70)
- 新版 [`00b62b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md#insn-00b62b4c) · [`00b62b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md#insn-00b62b54) · [`00b62b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b28.md#insn-00b62b38)

~~~diff
- 00b62a84 ["INT_ADD", "register:40f0:8", ["const:b62a84:8", "const:4:8"]]
- 00b62a84 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62b4c ["INT_ADD", "register:40f0:8", ["const:b62b4c:8", "const:4:8"]]
+ 00b62b4c ["CALL", null, ["callee:00bde040:8"]]
- 00b62a84 bytes 43ed0194
+ 00b62b4c bytes 3ded0194
- 00b62a8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62a8c bytes 60c202f9
+ 00b62b54 bytes 602203f9
- 00b62a70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62a70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62b38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62b38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62a70 bytes 68c242f9
+ 00b62b38 bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60d68af5686ab15c87a27d0cf3d29042"></a>

### [`00b62aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62aa0.md) → [`00b62b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62b98",
      "incomplete_value": true,
      "site": "00b62b98",
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
    "old": {
      "definition_site": "00b62ad0",
      "incomplete_value": true,
      "site": "00b62ad0",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62b7c",
      "incomplete_value": true,
      "site": "00b62b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62ab4",
      "incomplete_value": true,
      "site": "00b62ab4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62b88",
      "incomplete_value": false,
      "site": "00b62b90",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ac0",
      "incomplete_value": false,
      "site": "00b62ac8",
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
            "const:443:8"
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
      "00b62b78",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b88",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62b98",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62b78",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62b88",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62b98",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62aa0.md#insn-00b62ac8) · [`00b62ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62aa0.md#insn-00b62ad0) · [`00b62ab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62aa0.md#insn-00b62ab0)
- 新版 [`00b62b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md#insn-00b62b90) · [`00b62b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md#insn-00b62b98) · [`00b62b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62b68.md#insn-00b62b78)

~~~diff
- 00b62ac8 ["INT_ADD", "register:40f0:8", ["const:b62ac8:8", "const:4:8"]]
- 00b62ac8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62b90 ["INT_ADD", "register:40f0:8", ["const:b62b90:8", "const:4:8"]]
+ 00b62b90 ["CALL", null, ["callee:00bde040:8"]]
- 00b62ac8 bytes 32ed0194
+ 00b62b90 bytes 2ced0194
- 00b62ad0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62b98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62ad0 bytes 60c202f9
+ 00b62b98 bytes 602203f9
- 00b62ab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62ab0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62b78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62ab0 bytes 68c242f9
+ 00b62b78 bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93fd0767ded74186f0a67dbe498fb0fd"></a>

### [`00b62ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ae4.md) → [`00b62bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62bdc",
      "incomplete_value": true,
      "site": "00b62bdc",
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
    "old": {
      "definition_site": "00b62b14",
      "incomplete_value": true,
      "site": "00b62b14",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62bc0",
      "incomplete_value": true,
      "site": "00b62bc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62af8",
      "incomplete_value": true,
      "site": "00b62af8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62bc8",
      "incomplete_value": false,
      "site": "00b62bd4",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b00",
      "incomplete_value": false,
      "site": "00b62b0c",
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
            "const:443:8"
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
      "00b62bbc",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62bc8",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62bdc",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62bbc",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62bc8",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62bdc",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ae4.md#insn-00b62b0c) · [`00b62b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ae4.md#insn-00b62b14) · [`00b62af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ae4.md#insn-00b62af4)
- 新版 [`00b62bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md#insn-00b62bd4) · [`00b62bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md#insn-00b62bdc) · [`00b62bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bac.md#insn-00b62bbc)

~~~diff
- 00b62b0c ["INT_ADD", "register:40f0:8", ["const:b62b0c:8", "const:4:8"]]
- 00b62b0c ["CALL", null, ["callee:00bde040:8"]]
+ 00b62bd4 ["INT_ADD", "register:40f0:8", ["const:b62bd4:8", "const:4:8"]]
+ 00b62bd4 ["CALL", null, ["callee:00bde040:8"]]
- 00b62b0c bytes 21ed0194
+ 00b62bd4 bytes 1bed0194
- 00b62b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62bdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62b14 bytes 60c202f9
+ 00b62bdc bytes 602203f9
- 00b62af4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b62af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b62bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62af4 bytes 68c242f9
+ 00b62bbc bytes 682243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5090c1f6c7728010595277835bccc4e4"></a>

### [`00b62b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62b34.md) → [`00b62bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md) _ZN8firebase4auth24user_collision_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b62c54",
      "incomplete_value": true,
      "site": "00b62c54",
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
    "old": {
      "definition_site": "00b62b8c",
      "incomplete_value": true,
      "site": "00b62b8c",
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
            "const:588:8"
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
      "definition_site": "00b62c30",
      "incomplete_value": true,
      "site": "00b62c3c",
      "value": [
        "LOAD",
        "8",
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
                "const:640:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b68",
      "incomplete_value": true,
      "site": "00b62b74",
      "value": [
        "LOAD",
        "8",
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
                "const:580:8"
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
      "00b62c10",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62c30",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c54",
      "WRITE",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62c10",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62c30",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c54",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62b34.md#insn-00b62b74) · [`00b62b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62b34.md#insn-00b62b8c) · [`00b62b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62b34.md#insn-00b62b48)
- 新版 [`00b62c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md#insn-00b62c3c) · [`00b62c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md#insn-00b62c54) · [`00b62c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62bfc.md#insn-00b62c10)

~~~diff
- 00b62b74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62b74 ["INT_ADD", "register:40f0:8", ["const:b62b74:8", "const:4:8"]]
- 00b62b74 ["CALLIND", null, ["register:0:8"]]
+ 00b62c3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62c3c ["INT_ADD", "register:40f0:8", ["const:b62c3c:8", "const:4:8"]]
+ 00b62c3c ["CALLIND", null, ["register:0:8"]]
- 00b62b74 bytes 00013fd6
+ 00b62c3c bytes 00013fd6
- 00b62b8c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62b8c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:588:8"]]
- 00b62b8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b62c54 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b62c54 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
+ 00b62c54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62b8c bytes a0221639
+ 00b62c54 bytes a0221939
- 00b62b48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
- 00b62b48 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62b48 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b62c10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
+ 00b62c10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b62c10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62b48 bytes a8225639
+ 00b62c10 bytes a8225939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84623de9c38254ecaf81de2f6c0750e8"></a>

### [`00b62ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ba0.md) → [`00b62c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md) _ZN8firebase4auth24user_collision_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b62ca4",
      "incomplete_value": true,
      "site": "00b62ca4",
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
    "old": {
      "definition_site": "00b62bdc",
      "incomplete_value": true,
      "site": "00b62bdc",
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
            "const:588:8"
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
      "definition_site": "00b62cc4",
      "incomplete_value": true,
      "site": "00b62cc4",
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
    "old": {
      "definition_site": "00b62bfc",
      "incomplete_value": true,
      "site": "00b62bfc",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62c80",
      "incomplete_value": true,
      "site": "00b62c80",
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
      "definition_site": "00b62bb8",
      "incomplete_value": true,
      "site": "00b62bb8",
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
      "00b62c7c",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c88",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62ca4",
      "WRITE",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62c7c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62c88",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62ca4",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ba0.md#insn-00b62bdc) · [`00b62bf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ba0.md#insn-00b62bf8) · [`00b62bfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ba0.md#insn-00b62bfc)
- 新版 [`00b62ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md#insn-00b62ca4) · [`00b62cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md#insn-00b62cc0) · [`00b62cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62c68.md#insn-00b62cc4)

~~~diff
- 00b62bdc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62bdc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62bdc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:588:8"]]
- 00b62bdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b62ca4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b62ca4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b62ca4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
+ 00b62ca4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62bdc bytes bf221639
+ 00b62ca4 bytes bf221939
- 00b62bf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62bf8 ["INT_ADD", "register:40f0:8", ["const:b62bf8:8", "const:4:8"]]
- 00b62bf8 ["CALLIND", null, ["register:0:8"]]
+ 00b62cc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62cc0 ["INT_ADD", "register:40f0:8", ["const:b62cc0:8", "const:4:8"]]
+ 00b62cc0 ["CALLIND", null, ["register:0:8"]]
- 00b62bf8 bytes 00013fd6
+ 00b62cc0 bytes 00013fd6
- 00b62bfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b62bfc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b62bfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b62cc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62cc4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b62cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b62bfc bytes 9fc202f9
+ 00b62cc4 bytes 9f2203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5bfc5758b3002147c82a8c0ff7130d"></a>

### [`00b62c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c10.md) → [`00b62cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md) _ZN8firebase4auth24user_collision_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b62d18",
      "incomplete_value": true,
      "site": "00b62d18",
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
    "old": {
      "definition_site": "00b62c50",
      "incomplete_value": true,
      "site": "00b62c50",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62cf4",
      "incomplete_value": true,
      "site": "00b62cf4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62c2c",
      "incomplete_value": true,
      "site": "00b62c2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62cfc",
      "incomplete_value": false,
      "site": "00b62d10",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62c34",
      "incomplete_value": false,
      "site": "00b62c48",
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
            "const:443:8"
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
      "00b62cec",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62cfc",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62d18",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62cec",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62cfc",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62d18",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c10.md#insn-00b62c48) · [`00b62c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c10.md#insn-00b62c50) · [`00b62c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c10.md#insn-00b62c24)
- 新版 [`00b62d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md#insn-00b62d10) · [`00b62d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md#insn-00b62d18) · [`00b62cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62cd8.md#insn-00b62cec)

~~~diff
- 00b62c48 ["INT_ADD", "register:40f0:8", ["const:b62c48:8", "const:4:8"]]
- 00b62c48 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62d10 ["INT_ADD", "register:40f0:8", ["const:b62d10:8", "const:4:8"]]
+ 00b62d10 ["CALL", null, ["callee:00bde040:8"]]
- 00b62c48 bytes d2ec0194
+ 00b62d10 bytes ccec0194
- 00b62c50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b62c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62d18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62d18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62c50 bytes 80c202f9
+ 00b62d18 bytes 802203f9
- 00b62c24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b62c24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62cec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62cec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62c24 bytes 81c242f9
+ 00b62cec bytes 812243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b78e82c30802932fed7760bc8e943ac"></a>

### [`00b62c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c80.md) → [`00b62d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md) _ZN8firebase4auth24user_collision_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b62d64",
      "incomplete_value": false,
      "site": "00b62d68",
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
      "definition_site": "00b62c9c",
      "incomplete_value": false,
      "site": "00b62ca0",
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
      "definition_site": "00b62d74",
      "incomplete_value": true,
      "site": "00b62d80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62cac",
      "incomplete_value": true,
      "site": "00b62cb8",
      "value": [
        "LOAD",
        "8",
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
      "00b62d64",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b62d74",
      "DATA",
      [
        "storage",
        "010a1590",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62d64",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b62d74",
      "DATA",
      [
        "storage",
        "010a1650",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c80.md#insn-00b62ca0) · [`00b62c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c80.md#insn-00b62c9c) · [`00b62ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62c80.md#insn-00b62ca8)
- 新版 [`00b62d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md#insn-00b62d68) · [`00b62d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md#insn-00b62d64) · [`00b62d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d48.md#insn-00b62d70)

~~~diff
- 00b62ca0 ["INT_ADD", "register:40f0:8", ["const:b62ca0:8", "const:4:8"]]
- 00b62ca0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b62d68 ["INT_ADD", "register:40f0:8", ["const:b62d68:8", "const:4:8"]]
+ 00b62d68 ["CALL", null, ["callee:00bde130:8"]]
- 00b62ca0 bytes f8ec0194
+ 00b62d68 bytes f2ec0194
- 00b62c9c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62c9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62c9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62c9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62d64 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b62d64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62d64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62d64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62c9c bytes 001c1591
+ 00b62d64 bytes 00501791
- 00b62ca8 ["COPY", "tmp:0:8", ["const:590:8"]]
- 00b62ca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62ca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62ca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62d70 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00b62d70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62d70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62d70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62ca8 bytes 08411691
+ 00b62d70 bytes 08411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc82508f977959fefd645a9d58e9e47d"></a>

### [`00b62cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62cbc.md) → [`00b62d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md) _ZN8firebase4auth24user_collision_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62dc4",
      "incomplete_value": true,
      "site": "00b62dc4",
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
    "old": {
      "definition_site": "00b62cfc",
      "incomplete_value": true,
      "site": "00b62cfc",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b62da0",
      "incomplete_value": true,
      "site": "00b62da0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62cd8",
      "incomplete_value": true,
      "site": "00b62cd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62da8",
      "incomplete_value": false,
      "site": "00b62dbc",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ce0",
      "incomplete_value": false,
      "site": "00b62cf4",
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
            "const:443:8"
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
      "00b62d98",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62da8",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00b62dc4",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62d98",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62da8",
      "PARAM",
      [
        "storage",
        "002934d0",
        null,
        "string"
      ]
    ],
    [
      "00b62dc4",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62cbc.md#insn-00b62cf4) · [`00b62cfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62cbc.md#insn-00b62cfc) · [`00b62cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62cbc.md#insn-00b62cd0)
- 新版 [`00b62dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md#insn-00b62dbc) · [`00b62dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md#insn-00b62dc4) · [`00b62d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62d84.md#insn-00b62d98)

~~~diff
- 00b62cf4 ["INT_ADD", "register:40f0:8", ["const:b62cf4:8", "const:4:8"]]
- 00b62cf4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62dbc ["INT_ADD", "register:40f0:8", ["const:b62dbc:8", "const:4:8"]]
+ 00b62dbc ["CALL", null, ["callee:00bde040:8"]]
- 00b62cf4 bytes a7ec0194
+ 00b62dbc bytes a1ec0194
- 00b62cfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b62cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62dc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62cfc bytes 80c202f9
+ 00b62dc4 bytes 802203f9
- 00b62cd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b62cd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62d98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b62d98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62cd0 bytes 81c242f9
+ 00b62d98 bytes 812243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23e4125081bbd681425448303ec79e3d"></a>

### [`00b62d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d2c.md) → [`00b62df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md) _ZN8firebase4auth24user_collision_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b62e10",
      "incomplete_value": false,
      "site": "00b62e14",
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
      "definition_site": "00b62d48",
      "incomplete_value": false,
      "site": "00b62d4c",
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
      "definition_site": "00b62e20",
      "incomplete_value": true,
      "site": "00b62e2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62d58",
      "incomplete_value": true,
      "site": "00b62d64",
      "value": [
        "LOAD",
        "8",
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
      "00b62e10",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b62e20",
      "DATA",
      [
        "storage",
        "010a1598",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b62e10",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b62e20",
      "DATA",
      [
        "storage",
        "010a1658",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d2c.md#insn-00b62d4c) · [`00b62d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d2c.md#insn-00b62d48) · [`00b62d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d2c.md#insn-00b62d54)
- 新版 [`00b62e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md#insn-00b62e14) · [`00b62e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md#insn-00b62e10) · [`00b62e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62df4.md#insn-00b62e1c)

~~~diff
- 00b62d4c ["INT_ADD", "register:40f0:8", ["const:b62d4c:8", "const:4:8"]]
- 00b62d4c ["CALL", null, ["callee:00bde130:8"]]
+ 00b62e14 ["INT_ADD", "register:40f0:8", ["const:b62e14:8", "const:4:8"]]
+ 00b62e14 ["CALL", null, ["callee:00bde130:8"]]
- 00b62d4c bytes cdec0194
+ 00b62e14 bytes c7ec0194
- 00b62d48 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b62d48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62d48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62d48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b62e10 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b62e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b62e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62d48 bytes 00c81791
+ 00b62e10 bytes 00fc1991
- 00b62d54 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00b62d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b62e1c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 00b62e1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62e1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b62e1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62d54 bytes 08611691
+ 00b62e1c bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05006e163f898be26365fc10babc7d7f"></a>

### [`00b62d68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d68.md) → [`00b62e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b62e5c",
      "incomplete_value": true,
      "site": "00b62e5c",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62d94",
      "incomplete_value": true,
      "site": "00b62d94",
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
            "const:5a0:8"
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
      "definition_site": "00b62e44",
      "incomplete_value": true,
      "site": "00b62e44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62d7c",
      "incomplete_value": true,
      "site": "00b62d7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00b62d7c"
      ],
      [
        "FALL_THROUGH",
        "00b62e44"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62e44",
      "incomplete_value": true,
      "site": "00b62e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62d7c",
      "incomplete_value": true,
      "site": "00b62d94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62e40",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62e5c",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62e40",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62e5c",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d68.md#insn-00b62d94) · [`00b62d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d68.md#insn-00b62d78) · [`00b62d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62d68.md#insn-00b62d8c)
- 新版 [`00b62e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md#insn-00b62e5c) · [`00b62e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md#insn-00b62e40) · [`00b62e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e30.md#insn-00b62e54)

~~~diff
- 00b62d94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62d94 bytes 60d202f9
+ 00b62e5c bytes 603203f9
- 00b62d78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62d78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62e40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62d78 bytes 68d242f9
+ 00b62e40 bytes 683243f9
- 00b62d8c ["INT_ADD", "register:40f0:8", ["const:b62d8c:8", "const:4:8"]]
- 00b62d8c ["CALL", null, ["callee:00bde040:8"]]
+ 00b62e54 ["INT_ADD", "register:40f0:8", ["const:b62e54:8", "const:4:8"]]
+ 00b62e54 ["CALL", null, ["callee:00bde040:8"]]
- 00b62d8c bytes 81ec0194
+ 00b62e54 bytes 7bec0194
~~~


<a id="compare-3a81c81fc788c12421df7dcd15d97c18"></a>

### [`00b62da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62da8.md) → [`00b62e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b62e9c",
      "incomplete_value": true,
      "site": "00b62e9c",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62dd4",
      "incomplete_value": true,
      "site": "00b62dd4",
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
            "const:5a0:8"
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
      "definition_site": "00b62e84",
      "incomplete_value": true,
      "site": "00b62e84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62dbc",
      "incomplete_value": true,
      "site": "00b62dbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00b62dbc"
      ],
      [
        "FALL_THROUGH",
        "00b62e84"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62e84",
      "incomplete_value": true,
      "site": "00b62e9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62dbc",
      "incomplete_value": true,
      "site": "00b62dd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62e80",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62e9c",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62e80",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62e9c",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62da8.md#insn-00b62dd4) · [`00b62db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62da8.md#insn-00b62db8) · [`00b62dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62da8.md#insn-00b62dcc)
- 新版 [`00b62e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md#insn-00b62e9c) · [`00b62e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md#insn-00b62e80) · [`00b62e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62e70.md#insn-00b62e94)

~~~diff
- 00b62dd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62dd4 bytes 60d202f9
+ 00b62e9c bytes 603203f9
- 00b62db8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62db8 bytes 68d242f9
+ 00b62e80 bytes 683243f9
- 00b62dcc ["INT_ADD", "register:40f0:8", ["const:b62dcc:8", "const:4:8"]]
- 00b62dcc ["CALL", null, ["callee:00bde040:8"]]
+ 00b62e94 ["INT_ADD", "register:40f0:8", ["const:b62e94:8", "const:4:8"]]
+ 00b62e94 ["CALL", null, ["callee:00bde040:8"]]
- 00b62dcc bytes 71ec0194
+ 00b62e94 bytes 6bec0194
~~~


<a id="compare-4fbcc3893c86eda7cdb199afe7e5cc69"></a>

### [`00b62de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62de8.md) → [`00b62eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b62ee0",
      "incomplete_value": true,
      "site": "00b62ee0",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e18",
      "incomplete_value": true,
      "site": "00b62e18",
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
            "const:5a0:8"
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
      "definition_site": "00b62ec4",
      "incomplete_value": true,
      "site": "00b62ec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62dfc",
      "incomplete_value": true,
      "site": "00b62dfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00b62dfc"
      ],
      [
        "FALL_THROUGH",
        "00b62ec4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62ec4",
      "incomplete_value": true,
      "site": "00b62ee0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62dfc",
      "incomplete_value": true,
      "site": "00b62e18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62ec0",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ee0",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62ec0",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62ee0",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62de8.md#insn-00b62e18) · [`00b62df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62de8.md#insn-00b62df8) · [`00b62e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62de8.md#insn-00b62e10)
- 新版 [`00b62ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md#insn-00b62ee0) · [`00b62ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md#insn-00b62ec0) · [`00b62ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62eb0.md#insn-00b62ed8)

~~~diff
- 00b62e18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62e18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62ee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62e18 bytes 60d202f9
+ 00b62ee0 bytes 603203f9
- 00b62df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62df8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62df8 bytes 68d242f9
+ 00b62ec0 bytes 683243f9
- 00b62e10 ["INT_ADD", "register:40f0:8", ["const:b62e10:8", "const:4:8"]]
- 00b62e10 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62ed8 ["INT_ADD", "register:40f0:8", ["const:b62ed8:8", "const:4:8"]]
+ 00b62ed8 ["CALL", null, ["callee:00bde040:8"]]
- 00b62e10 bytes 60ec0194
+ 00b62ed8 bytes 5aec0194
~~~


<a id="compare-2dbd1989c076a7b05d0ec32848f4705d"></a>

### [`00b62e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e2c.md) → [`00b62ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b62f24",
      "incomplete_value": true,
      "site": "00b62f24",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e5c",
      "incomplete_value": true,
      "site": "00b62e5c",
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
            "const:5a0:8"
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
      "definition_site": "00b62f08",
      "incomplete_value": true,
      "site": "00b62f08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62e40",
      "incomplete_value": true,
      "site": "00b62e40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00b62e40"
      ],
      [
        "FALL_THROUGH",
        "00b62f08"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b62f08",
      "incomplete_value": true,
      "site": "00b62f24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62e40",
      "incomplete_value": true,
      "site": "00b62e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b62f04",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f24",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b62f04",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f24",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e2c.md#insn-00b62e5c) · [`00b62e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e2c.md#insn-00b62e3c) · [`00b62e54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e2c.md#insn-00b62e54)
- 新版 [`00b62f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md#insn-00b62f24) · [`00b62f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md#insn-00b62f04) · [`00b62f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62ef4.md#insn-00b62f1c)

~~~diff
- 00b62e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b62f24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62e5c bytes 60d202f9
+ 00b62f24 bytes 603203f9
- 00b62e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b62e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b62f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
+ 00b62f04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62e3c bytes 68d242f9
+ 00b62f04 bytes 683243f9
- 00b62e54 ["INT_ADD", "register:40f0:8", ["const:b62e54:8", "const:4:8"]]
- 00b62e54 ["CALL", null, ["callee:00bde040:8"]]
+ 00b62f1c ["INT_ADD", "register:40f0:8", ["const:b62f1c:8", "const:4:8"]]
+ 00b62f1c ["CALL", null, ["callee:00bde040:8"]]
- 00b62e54 bytes 4fec0194
+ 00b62f1c bytes 49ec0194
~~~


<a id="compare-15876443181ba98222b8badb1661490a"></a>

### [`00b62e7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e7c.md) → [`00b62f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md) _ZN8firebase4auth21android_web_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b62f9c",
      "incomplete_value": true,
      "site": "00b62f9c",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ed4",
      "incomplete_value": true,
      "site": "00b62ed4",
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
            "const:5a8:8"
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
      "definition_site": "00b62f78",
      "incomplete_value": true,
      "site": "00b62f84",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00b62eb0",
      "incomplete_value": true,
      "site": "00b62ebc",
      "value": [
        "LOAD",
        "8",
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
                "const:5a0:8"
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
      "00b62f58",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62f78",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f9c",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62f58",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62f78",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62f9c",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e7c.md#insn-00b62ebc) · [`00b62ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e7c.md#insn-00b62ed4) · [`00b62e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62e7c.md#insn-00b62e90)
- 新版 [`00b62f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md#insn-00b62f84) · [`00b62f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md#insn-00b62f9c) · [`00b62f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62f44.md#insn-00b62f58)

~~~diff
- 00b62ebc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62ebc ["INT_ADD", "register:40f0:8", ["const:b62ebc:8", "const:4:8"]]
- 00b62ebc ["CALLIND", null, ["register:0:8"]]
+ 00b62f84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b62f84 ["INT_ADD", "register:40f0:8", ["const:b62f84:8", "const:4:8"]]
+ 00b62f84 ["CALLIND", null, ["register:0:8"]]
- 00b62ebc bytes 00013fd6
+ 00b62f84 bytes 00013fd6
- 00b62ed4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62ed4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
- 00b62ed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b62f9c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b62f9c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:668:8"]]
+ 00b62f9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62ed4 bytes a0a21639
+ 00b62f9c bytes a0a21939
- 00b62e90 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
- 00b62e90 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b62e90 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b62f58 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:668:8"]]
+ 00b62f58 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b62f58 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b62e90 bytes a8a25639
+ 00b62f58 bytes a8a25939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22e8138664b347983ba5f61a621c9abb"></a>

### [`00b62ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ee8.md) → [`00b62fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md) _ZN8firebase4auth21android_web_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b62fec",
      "incomplete_value": true,
      "site": "00b62fec",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f24",
      "incomplete_value": true,
      "site": "00b62f24",
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
            "const:5a8:8"
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
      "definition_site": "00b6300c",
      "incomplete_value": true,
      "site": "00b6300c",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f44",
      "incomplete_value": true,
      "site": "00b62f44",
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
            "const:5a0:8"
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
      "definition_site": "00b62fc8",
      "incomplete_value": true,
      "site": "00b62fc8",
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
      "definition_site": "00b62f00",
      "incomplete_value": true,
      "site": "00b62f00",
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
      "00b62fc4",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62fd0",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62fec",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b62fc4",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b62fd0",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b62fec",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ee8.md#insn-00b62f24) · [`00b62f40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ee8.md#insn-00b62f40) · [`00b62f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62ee8.md#insn-00b62f44)
- 新版 [`00b62fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md#insn-00b62fec) · [`00b63008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md#insn-00b63008) · [`00b6300c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b62/00b62fb0.md#insn-00b6300c)

~~~diff
- 00b62f24 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62f24 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
- 00b62f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b62fec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b62fec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b62fec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:668:8"]]
+ 00b62fec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62f24 bytes bfa21639
+ 00b62fec bytes bfa21939
- 00b62f40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62f40 ["INT_ADD", "register:40f0:8", ["const:b62f40:8", "const:4:8"]]
- 00b62f40 ["CALLIND", null, ["register:0:8"]]
+ 00b63008 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63008 ["INT_ADD", "register:40f0:8", ["const:b63008:8", "const:4:8"]]
+ 00b63008 ["CALLIND", null, ["register:0:8"]]
- 00b62f40 bytes 00013fd6
+ 00b63008 bytes 00013fd6
- 00b62f44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b62f44 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b62f44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b6300c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b6300c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b6300c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b62f44 bytes 9fd202f9
+ 00b6300c bytes 9f3203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ce5136500882fe8977135df579fba52"></a>

### [`00b62f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62f58.md) → [`00b63020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md) _ZN8firebase4auth21android_web_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b63060",
      "incomplete_value": true,
      "site": "00b63060",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f98",
      "incomplete_value": true,
      "site": "00b62f98",
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
            "const:5a0:8"
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
      "definition_site": "00b6303c",
      "incomplete_value": true,
      "site": "00b6303c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62f74",
      "incomplete_value": true,
      "site": "00b62f74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00b62f74"
      ],
      [
        "FALL_THROUGH",
        "00b6303c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b6303c",
      "incomplete_value": true,
      "site": "00b63060",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b62f74",
      "incomplete_value": true,
      "site": "00b62f98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b63034",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63060",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63078",
      "PARAM",
      [
        "storage",
        "010a15b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63034",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63060",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63078",
      "PARAM",
      [
        "storage",
        "010a1670",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62f58.md#insn-00b62f98) · [`00b62f6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62f58.md#insn-00b62f6c) · [`00b62f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62f58.md#insn-00b62f90)
- 新版 [`00b63060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md#insn-00b63060) · [`00b63034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md#insn-00b63034) · [`00b63058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63020.md#insn-00b63058)

~~~diff
- 00b62f98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b62f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63060 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b63060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62f98 bytes 80d202f9
+ 00b63060 bytes 803203f9
- 00b62f6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b62f6c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63034 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b63034 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b62f6c bytes 81d242f9
+ 00b63034 bytes 813243f9
- 00b62f90 ["INT_ADD", "register:40f0:8", ["const:b62f90:8", "const:4:8"]]
- 00b62f90 ["CALL", null, ["callee:00bde040:8"]]
+ 00b63058 ["INT_ADD", "register:40f0:8", ["const:b63058:8", "const:4:8"]]
+ 00b63058 ["CALL", null, ["callee:00bde040:8"]]
- 00b62f90 bytes 00ec0194
+ 00b63058 bytes faeb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4389fc531301090458faebc107f01f54"></a>

### [`00b62fc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62fc8.md) → [`00b63090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md) _ZN8firebase4auth21android_web_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b630ac",
      "incomplete_value": false,
      "site": "00b630b0",
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
      "definition_site": "00b62fe4",
      "incomplete_value": false,
      "site": "00b62fe8",
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
      "definition_site": "00b630bc",
      "incomplete_value": true,
      "site": "00b630c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62ff4",
      "incomplete_value": true,
      "site": "00b63000",
      "value": [
        "LOAD",
        "8",
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
      "00b630ac",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b630bc",
      "DATA",
      [
        "storage",
        "010a15b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b630ac",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b630bc",
      "DATA",
      [
        "storage",
        "010a1670",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62fc8.md#insn-00b62fe8) · [`00b62fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62fc8.md#insn-00b62fe4) · [`00b62ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b62/00b62fc8.md#insn-00b62ff0)
- 新版 [`00b630b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md#insn-00b630b0) · [`00b630ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md#insn-00b630ac) · [`00b630b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63090.md#insn-00b630b8)

~~~diff
- 00b62fe8 ["INT_ADD", "register:40f0:8", ["const:b62fe8:8", "const:4:8"]]
- 00b62fe8 ["CALL", null, ["callee:00bde130:8"]]
+ 00b630b0 ["INT_ADD", "register:40f0:8", ["const:b630b0:8", "const:4:8"]]
+ 00b630b0 ["CALL", null, ["callee:00bde130:8"]]
- 00b62fe8 bytes 26ec0194
+ 00b630b0 bytes 20ec0194
- 00b62fe4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62fe4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62fe4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62fe4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b630ac ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b630ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b630ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b630ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62fe4 bytes 001c1591
+ 00b630ac bytes 00501791
- 00b62ff0 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 00b62ff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b62ff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b62ff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b630b8 ["COPY", "tmp:0:8", ["const:670:8"]]
+ 00b630b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b630b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b630b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b62ff0 bytes 08c11691
+ 00b630b8 bytes 08c11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fca747c56604fa33030ded933adf53b"></a>

### [`00b63004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63004.md) → [`00b630cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md) _ZN8firebase4auth21android_web_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6310c",
      "incomplete_value": true,
      "site": "00b6310c",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63044",
      "incomplete_value": true,
      "site": "00b63044",
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
            "const:5a0:8"
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
      "definition_site": "00b630e8",
      "incomplete_value": true,
      "site": "00b630e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63020",
      "incomplete_value": true,
      "site": "00b63020",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00b63020"
      ],
      [
        "FALL_THROUGH",
        "00b630e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b630e8",
      "incomplete_value": true,
      "site": "00b6310c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63020",
      "incomplete_value": true,
      "site": "00b63044",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b630e0",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6310c",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63124",
      "PARAM",
      [
        "storage",
        "010a15b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b630e0",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6310c",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63124",
      "PARAM",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63004.md#insn-00b63044) · [`00b63018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63004.md#insn-00b63018) · [`00b6303c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63004.md#insn-00b6303c)
- 新版 [`00b6310c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md#insn-00b6310c) · [`00b630e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md#insn-00b630e0) · [`00b63104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b630cc.md#insn-00b63104)

~~~diff
- 00b63044 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b63044 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6310c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b6310c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63044 bytes 80d202f9
+ 00b6310c bytes 803203f9
- 00b63018 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b63018 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b630e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
+ 00b630e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63018 bytes 81d242f9
+ 00b630e0 bytes 813243f9
- 00b6303c ["INT_ADD", "register:40f0:8", ["const:b6303c:8", "const:4:8"]]
- 00b6303c ["CALL", null, ["callee:00bde040:8"]]
+ 00b63104 ["INT_ADD", "register:40f0:8", ["const:b63104:8", "const:4:8"]]
+ 00b63104 ["CALL", null, ["callee:00bde040:8"]]
- 00b6303c bytes d5eb0194
+ 00b63104 bytes cfeb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53757196adba7c45202f7eeea4ec5ea6"></a>

### [`00b63074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63074.md) → [`00b6313c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md) _ZN8firebase4auth21android_web_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b63158",
      "incomplete_value": false,
      "site": "00b6315c",
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
      "definition_site": "00b63090",
      "incomplete_value": false,
      "site": "00b63094",
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
      "definition_site": "00b63168",
      "incomplete_value": true,
      "site": "00b63174",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b630a0",
      "incomplete_value": true,
      "site": "00b630ac",
      "value": [
        "LOAD",
        "8",
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
      "00b63158",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b63168",
      "DATA",
      [
        "storage",
        "010a15b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63158",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b63168",
      "DATA",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63074.md#insn-00b63094) · [`00b63090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63074.md#insn-00b63090) · [`00b6309c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63074.md#insn-00b6309c)
- 新版 [`00b6315c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md#insn-00b6315c) · [`00b63158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md#insn-00b63158) · [`00b63164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6313c.md#insn-00b63164)

~~~diff
- 00b63094 ["INT_ADD", "register:40f0:8", ["const:b63094:8", "const:4:8"]]
- 00b63094 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6315c ["INT_ADD", "register:40f0:8", ["const:b6315c:8", "const:4:8"]]
+ 00b6315c ["CALL", null, ["callee:00bde130:8"]]
- 00b63094 bytes fbeb0194
+ 00b6315c bytes f5eb0194
- 00b63090 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b63090 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63090 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63090 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63158 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b63158 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63158 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63158 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63090 bytes 00c81791
+ 00b63158 bytes 00fc1991
- 00b6309c ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00b6309c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6309c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6309c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63164 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00b63164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6309c bytes 08e11691
+ 00b63164 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa2b794ad028a58d4ce713800abca193"></a>

### [`00b630b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630b0.md) → [`00b63178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b631a4",
      "incomplete_value": true,
      "site": "00b631a4",
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
      "definition_site": "00b630dc",
      "incomplete_value": true,
      "site": "00b630dc",
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
      "definition_site": "00b6318c",
      "incomplete_value": true,
      "site": "00b6318c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b630c4",
      "incomplete_value": true,
      "site": "00b630c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63198",
      "incomplete_value": false,
      "site": "00b6319c",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b630d0",
      "incomplete_value": false,
      "site": "00b630d4",
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
            "const:570:8"
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
      "00b63188",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63198",
      "PARAM",
      [
        "storage",
        "002ad570",
        null,
        "string"
      ]
    ],
    [
      "00b631a4",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63188",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63198",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00b631a4",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b630d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630b0.md#insn-00b630d4) · [`00b630dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630b0.md#insn-00b630dc) · [`00b630c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630b0.md#insn-00b630c0)
- 新版 [`00b6319c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md#insn-00b6319c) · [`00b631a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md#insn-00b631a4) · [`00b63188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63178.md#insn-00b63188)

~~~diff
- 00b630d4 ["INT_ADD", "register:40f0:8", ["const:b630d4:8", "const:4:8"]]
- 00b630d4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6319c ["INT_ADD", "register:40f0:8", ["const:b6319c:8", "const:4:8"]]
+ 00b6319c ["CALL", null, ["callee:00bde040:8"]]
- 00b630d4 bytes afeb0194
+ 00b6319c bytes a9eb0194
- 00b630dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b630dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b631a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b631a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b630dc bytes 60e202f9
+ 00b631a4 bytes 604203f9
- 00b630c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b630c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b63188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b630c0 bytes 68e242f9
+ 00b63188 bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b0c992b681b4fb62220b8109db25e5"></a>

### [`00b630f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630f0.md) → [`00b631b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00b631e4",
      "incomplete_value": true,
      "site": "00b631e4",
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
      "definition_site": "00b6311c",
      "incomplete_value": true,
      "site": "00b6311c",
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
      "definition_site": "00b631cc",
      "incomplete_value": true,
      "site": "00b631cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63104",
      "incomplete_value": true,
      "site": "00b63104",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b631d4",
      "incomplete_value": false,
      "site": "00b631dc",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6310c",
      "incomplete_value": false,
      "site": "00b63114",
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
            "const:570:8"
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
      "00b631c8",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b631d4",
      "PARAM",
      [
        "storage",
        "002ad570",
        null,
        "string"
      ]
    ],
    [
      "00b631e4",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b631c8",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b631d4",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00b631e4",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630f0.md#insn-00b63114) · [`00b6311c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630f0.md#insn-00b6311c) · [`00b63100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b630f0.md#insn-00b63100)
- 新版 [`00b631dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md#insn-00b631dc) · [`00b631e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md#insn-00b631e4) · [`00b631c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631b8.md#insn-00b631c8)

~~~diff
- 00b63114 ["INT_ADD", "register:40f0:8", ["const:b63114:8", "const:4:8"]]
- 00b63114 ["CALL", null, ["callee:00bde040:8"]]
+ 00b631dc ["INT_ADD", "register:40f0:8", ["const:b631dc:8", "const:4:8"]]
+ 00b631dc ["CALL", null, ["callee:00bde040:8"]]
- 00b63114 bytes 9feb0194
+ 00b631dc bytes 99eb0194
- 00b6311c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b6311c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b631e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b631e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6311c bytes 60e202f9
+ 00b631e4 bytes 604203f9
- 00b63100 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b63100 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b631c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b631c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63100 bytes 68e242f9
+ 00b631c8 bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9729253dab31114c83663d6e114e43d"></a>

### [`00b63130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63130.md) → [`00b631f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b63228",
      "incomplete_value": true,
      "site": "00b63228",
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
      "definition_site": "00b63160",
      "incomplete_value": true,
      "site": "00b63160",
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
      "definition_site": "00b6320c",
      "incomplete_value": true,
      "site": "00b6320c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63144",
      "incomplete_value": true,
      "site": "00b63144",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63218",
      "incomplete_value": false,
      "site": "00b63220",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63150",
      "incomplete_value": false,
      "site": "00b63158",
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
            "const:570:8"
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
      "00b63208",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63218",
      "PARAM",
      [
        "storage",
        "002ad570",
        null,
        "string"
      ]
    ],
    [
      "00b63228",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63208",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63218",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00b63228",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63130.md#insn-00b63158) · [`00b63160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63130.md#insn-00b63160) · [`00b63140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63130.md#insn-00b63140)
- 新版 [`00b63220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md#insn-00b63220) · [`00b63228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md#insn-00b63228) · [`00b63208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b631f8.md#insn-00b63208)

~~~diff
- 00b63158 ["INT_ADD", "register:40f0:8", ["const:b63158:8", "const:4:8"]]
- 00b63158 ["CALL", null, ["callee:00bde040:8"]]
+ 00b63220 ["INT_ADD", "register:40f0:8", ["const:b63220:8", "const:4:8"]]
+ 00b63220 ["CALL", null, ["callee:00bde040:8"]]
- 00b63158 bytes 8eeb0194
+ 00b63220 bytes 88eb0194
- 00b63160 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b63160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b63228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63160 bytes 60e202f9
+ 00b63228 bytes 604203f9
- 00b63140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b63140 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b63208 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63140 bytes 68e242f9
+ 00b63208 bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f66ce633a7001c1755f0cef80199f74"></a>

### [`00b63174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63174.md) → [`00b6323c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6326c",
      "incomplete_value": true,
      "site": "00b6326c",
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
      "definition_site": "00b631a4",
      "incomplete_value": true,
      "site": "00b631a4",
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
      "definition_site": "00b63250",
      "incomplete_value": true,
      "site": "00b63250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63188",
      "incomplete_value": true,
      "site": "00b63188",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63258",
      "incomplete_value": false,
      "site": "00b63264",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63190",
      "incomplete_value": false,
      "site": "00b6319c",
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
            "const:570:8"
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
      "00b6324c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63258",
      "PARAM",
      [
        "storage",
        "002ad570",
        null,
        "string"
      ]
    ],
    [
      "00b6326c",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6324c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63258",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00b6326c",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6319c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63174.md#insn-00b6319c) · [`00b631a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63174.md#insn-00b631a4) · [`00b63184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63174.md#insn-00b63184)
- 新版 [`00b63264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md#insn-00b63264) · [`00b6326c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md#insn-00b6326c) · [`00b6324c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6323c.md#insn-00b6324c)

~~~diff
- 00b6319c ["INT_ADD", "register:40f0:8", ["const:b6319c:8", "const:4:8"]]
- 00b6319c ["CALL", null, ["callee:00bde040:8"]]
+ 00b63264 ["INT_ADD", "register:40f0:8", ["const:b63264:8", "const:4:8"]]
+ 00b63264 ["CALL", null, ["callee:00bde040:8"]]
- 00b6319c bytes 7deb0194
+ 00b63264 bytes 77eb0194
- 00b631a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b631a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6326c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b6326c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b631a4 bytes 60e202f9
+ 00b6326c bytes 604203f9
- 00b63184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b63184 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6324c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
+ 00b6324c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63184 bytes 68e242f9
+ 00b6324c bytes 684243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca84696285adc516d1a60ede1e01b199"></a>

### [`00b631c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b631c4.md) → [`00b6328c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md) _ZN8firebase4auth23firebase_auth_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b632e4",
      "incomplete_value": true,
      "site": "00b632e4",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6321c",
      "incomplete_value": true,
      "site": "00b6321c",
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
            "const:5c8:8"
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
      "definition_site": "00b632c0",
      "incomplete_value": true,
      "site": "00b632cc",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00b631f8",
      "incomplete_value": true,
      "site": "00b63204",
      "value": [
        "LOAD",
        "8",
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
                "const:5c0:8"
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
      "00b632a0",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b632c0",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b632e4",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b632a0",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b632c0",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b632e4",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b631c4.md#insn-00b63204) · [`00b6321c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b631c4.md#insn-00b6321c) · [`00b631d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b631c4.md#insn-00b631d8)
- 新版 [`00b632cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md#insn-00b632cc) · [`00b632e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md#insn-00b632e4) · [`00b632a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6328c.md#insn-00b632a0)

~~~diff
- 00b63204 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63204 ["INT_ADD", "register:40f0:8", ["const:b63204:8", "const:4:8"]]
- 00b63204 ["CALLIND", null, ["register:0:8"]]
+ 00b632cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b632cc ["INT_ADD", "register:40f0:8", ["const:b632cc:8", "const:4:8"]]
+ 00b632cc ["CALLIND", null, ["register:0:8"]]
- 00b63204 bytes 00013fd6
+ 00b632cc bytes 00013fd6
- 00b6321c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6321c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
- 00b6321c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b632e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b632e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
+ 00b632e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6321c bytes a0221739
+ 00b632e4 bytes a0221a39
- 00b631d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
- 00b631d8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b631d8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b632a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
+ 00b632a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b632a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b631d8 bytes a8225739
+ 00b632a0 bytes a8225a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577c76c294769af012be8f7eeaba36f4"></a>

### [`00b63230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63230.md) → [`00b632f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md) _ZN8firebase4auth23firebase_auth_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b63334",
      "incomplete_value": true,
      "site": "00b63334",
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
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6326c",
      "incomplete_value": true,
      "site": "00b6326c",
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
            "const:5c8:8"
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
      "definition_site": "00b63354",
      "incomplete_value": true,
      "site": "00b63354",
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
      "definition_site": "00b6328c",
      "incomplete_value": true,
      "site": "00b6328c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63310",
      "incomplete_value": true,
      "site": "00b63310",
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
      "definition_site": "00b63248",
      "incomplete_value": true,
      "site": "00b63248",
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
      "00b6330c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63318",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63334",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6330c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63318",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63334",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6326c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63230.md#insn-00b6326c) · [`00b63288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63230.md#insn-00b63288) · [`00b6328c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63230.md#insn-00b6328c)
- 新版 [`00b63334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md#insn-00b63334) · [`00b63350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md#insn-00b63350) · [`00b63354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b632f8.md#insn-00b63354)

~~~diff
- 00b6326c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6326c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6326c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
- 00b6326c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b63334 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b63334 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b63334 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
+ 00b63334 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6326c bytes bf221739
+ 00b63334 bytes bf221a39
- 00b63288 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63288 ["INT_ADD", "register:40f0:8", ["const:b63288:8", "const:4:8"]]
- 00b63288 ["CALLIND", null, ["register:0:8"]]
+ 00b63350 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63350 ["INT_ADD", "register:40f0:8", ["const:b63350:8", "const:4:8"]]
+ 00b63350 ["CALLIND", null, ["register:0:8"]]
- 00b63288 bytes 00013fd6
+ 00b63350 bytes 00013fd6
- 00b6328c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b6328c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6328c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b63354 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b63354 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b63354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6328c bytes 9fe202f9
+ 00b63354 bytes 9f4203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9358f8a4d97d805cbf7dab5587bc26b4"></a>

### [`00b632a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b632a0.md) → [`00b63368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md) _ZN8firebase4auth23firebase_auth_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b633a8",
      "incomplete_value": true,
      "site": "00b633a8",
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
      "definition_site": "00b632e0",
      "incomplete_value": true,
      "site": "00b632e0",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63384",
      "incomplete_value": true,
      "site": "00b63384",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b632bc",
      "incomplete_value": true,
      "site": "00b632bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6338c",
      "incomplete_value": false,
      "site": "00b633a0",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b632c4",
      "incomplete_value": false,
      "site": "00b632d8",
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
            "const:570:8"
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
      "00b6337c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6338c",
      "PARAM",
      [
        "storage",
        "002ad570",
        null,
        "string"
      ]
    ],
    [
      "00b633a8",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6337c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6338c",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00b633a8",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b632d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b632a0.md#insn-00b632d8) · [`00b632e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b632a0.md#insn-00b632e0) · [`00b632b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b632a0.md#insn-00b632b4)
- 新版 [`00b633a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md#insn-00b633a0) · [`00b633a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md#insn-00b633a8) · [`00b6337c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63368.md#insn-00b6337c)

~~~diff
- 00b632d8 ["INT_ADD", "register:40f0:8", ["const:b632d8:8", "const:4:8"]]
- 00b632d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b633a0 ["INT_ADD", "register:40f0:8", ["const:b633a0:8", "const:4:8"]]
+ 00b633a0 ["CALL", null, ["callee:00bde040:8"]]
- 00b632d8 bytes 2eeb0194
+ 00b633a0 bytes 28eb0194
- 00b632e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b632e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b633a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b633a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b632e0 bytes 80e202f9
+ 00b633a8 bytes 804203f9
- 00b632b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b632b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6337c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b6337c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b632b4 bytes 81e242f9
+ 00b6337c bytes 814243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230afa49a190ac73f305a274fc88e3ea"></a>

### [`00b63310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63310.md) → [`00b633d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md) _ZN8firebase4auth23firebase_auth_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b633f4",
      "incomplete_value": false,
      "site": "00b633f8",
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
      "definition_site": "00b6332c",
      "incomplete_value": false,
      "site": "00b63330",
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
      "definition_site": "00b63404",
      "incomplete_value": true,
      "site": "00b63410",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6333c",
      "incomplete_value": true,
      "site": "00b63348",
      "value": [
        "LOAD",
        "8",
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
      "00b633f4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63404",
      "DATA",
      [
        "storage",
        "010a15d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b633f4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63404",
      "DATA",
      [
        "storage",
        "010a1690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63310.md#insn-00b63330) · [`00b6332c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63310.md#insn-00b6332c) · [`00b63338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63310.md#insn-00b63338)
- 新版 [`00b633f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md#insn-00b633f8) · [`00b633f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md#insn-00b633f4) · [`00b63400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b633d8.md#insn-00b63400)

~~~diff
- 00b63330 ["INT_ADD", "register:40f0:8", ["const:b63330:8", "const:4:8"]]
- 00b63330 ["CALL", null, ["callee:00bde130:8"]]
+ 00b633f8 ["INT_ADD", "register:40f0:8", ["const:b633f8:8", "const:4:8"]]
+ 00b633f8 ["CALL", null, ["callee:00bde130:8"]]
- 00b63330 bytes 54eb0194
+ 00b633f8 bytes 4eeb0194
- 00b6332c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6332c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6332c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6332c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b633f4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b633f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b633f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b633f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6332c bytes 001c1591
+ 00b633f4 bytes 00501791
- 00b63338 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00b63338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63400 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00b63400 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63400 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63400 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63338 bytes 08411791
+ 00b63400 bytes 08411a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f923b3fc67728efda80a5c27024771"></a>

### [`00b6334c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6334c.md) → [`00b63414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md) _ZN8firebase4auth23firebase_auth_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b63454",
      "incomplete_value": true,
      "site": "00b63454",
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
      "definition_site": "00b6338c",
      "incomplete_value": true,
      "site": "00b6338c",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63430",
      "incomplete_value": true,
      "site": "00b63430",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63368",
      "incomplete_value": true,
      "site": "00b63368",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63438",
      "incomplete_value": false,
      "site": "00b6344c",
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
            "const:567:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63370",
      "incomplete_value": false,
      "site": "00b63384",
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
            "const:570:8"
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
      "00b63428",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63438",
      "PARAM",
      [
        "storage",
        "002ad570",
        null,
        "string"
      ]
    ],
    [
      "00b63454",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63428",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63438",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00b63454",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6334c.md#insn-00b63384) · [`00b6338c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6334c.md#insn-00b6338c) · [`00b63360`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6334c.md#insn-00b63360)
- 新版 [`00b6344c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md#insn-00b6344c) · [`00b63454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md#insn-00b63454) · [`00b63428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63414.md#insn-00b63428)

~~~diff
- 00b63384 ["INT_ADD", "register:40f0:8", ["const:b63384:8", "const:4:8"]]
- 00b63384 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6344c ["INT_ADD", "register:40f0:8", ["const:b6344c:8", "const:4:8"]]
+ 00b6344c ["CALL", null, ["callee:00bde040:8"]]
- 00b63384 bytes 03eb0194
+ 00b6344c bytes fdea0194
- 00b6338c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b6338c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63454 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b63454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6338c bytes 80e202f9
+ 00b63454 bytes 804203f9
- 00b63360 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b63360 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63428 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
+ 00b63428 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63360 bytes 81e242f9
+ 00b63428 bytes 814243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73e960ace9d5913b48951a5dc89a921f"></a>

### [`00b633bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633bc.md) → [`00b63484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md) _ZN8firebase4auth23firebase_auth_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b634a0",
      "incomplete_value": false,
      "site": "00b634a4",
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
      "definition_site": "00b633d8",
      "incomplete_value": false,
      "site": "00b633dc",
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
      "definition_site": "00b634b0",
      "incomplete_value": true,
      "site": "00b634bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b633e8",
      "incomplete_value": true,
      "site": "00b633f4",
      "value": [
        "LOAD",
        "8",
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
      "00b634a0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b634b0",
      "DATA",
      [
        "storage",
        "010a15d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b634a0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b634b0",
      "DATA",
      [
        "storage",
        "010a1698",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b633dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633bc.md#insn-00b633dc) · [`00b633d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633bc.md#insn-00b633d8) · [`00b633e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633bc.md#insn-00b633e4)
- 新版 [`00b634a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md#insn-00b634a4) · [`00b634a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md#insn-00b634a0) · [`00b634ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63484.md#insn-00b634ac)

~~~diff
- 00b633dc ["INT_ADD", "register:40f0:8", ["const:b633dc:8", "const:4:8"]]
- 00b633dc ["CALL", null, ["callee:00bde130:8"]]
+ 00b634a4 ["INT_ADD", "register:40f0:8", ["const:b634a4:8", "const:4:8"]]
+ 00b634a4 ["CALL", null, ["callee:00bde130:8"]]
- 00b633dc bytes 29eb0194
+ 00b634a4 bytes 23eb0194
- 00b633d8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b633d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b633d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b633d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b634a0 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b634a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b634a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b634a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b633d8 bytes 00c81791
+ 00b634a0 bytes 00fc1991
- 00b633e4 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 00b633e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b633e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b633e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b634ac ["COPY", "tmp:0:8", ["const:698:8"]]
+ 00b634ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b634ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b634ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b633e4 bytes 08611791
+ 00b634ac bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-012a1070407b741c592e8b83425975ed"></a>

### [`00b633f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633f8.md) → [`00b634c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00b634ec",
      "incomplete_value": true,
      "site": "00b634ec",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63424",
      "incomplete_value": true,
      "site": "00b63424",
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
            "const:5e0:8"
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
      "definition_site": "00b634d4",
      "incomplete_value": true,
      "site": "00b634d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6340c",
      "incomplete_value": true,
      "site": "00b6340c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b634e0",
      "incomplete_value": false,
      "site": "00b634e4",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63418",
      "incomplete_value": false,
      "site": "00b6341c",
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
            "const:5c7:8"
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
      "00b634d0",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b634e0",
      "PARAM",
      [
        "storage",
        "002ae5c7",
        null,
        "string"
      ]
    ],
    [
      "00b634ec",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b634d0",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b634e0",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00b634ec",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6341c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633f8.md#insn-00b6341c) · [`00b63424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633f8.md#insn-00b63424) · [`00b63408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b633f8.md#insn-00b63408)
- 新版 [`00b634e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md#insn-00b634e4) · [`00b634ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md#insn-00b634ec) · [`00b634d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b634c0.md#insn-00b634d0)

~~~diff
- 00b6341c ["INT_ADD", "register:40f0:8", ["const:b6341c:8", "const:4:8"]]
- 00b6341c ["CALL", null, ["callee:00bde040:8"]]
+ 00b634e4 ["INT_ADD", "register:40f0:8", ["const:b634e4:8", "const:4:8"]]
+ 00b634e4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6341c bytes ddea0194
+ 00b634e4 bytes d7ea0194
- 00b63424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b63424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b634ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b634ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63424 bytes 60f202f9
+ 00b634ec bytes 605203f9
- 00b63408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b63408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b634d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b634d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63408 bytes 68f242f9
+ 00b634d0 bytes 685243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bdc7e8a5c3199f2fd6ac2ff925985ff"></a>

### [`00b63438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63438.md) → [`00b63500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00b6352c",
      "incomplete_value": true,
      "site": "00b6352c",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63464",
      "incomplete_value": true,
      "site": "00b63464",
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
            "const:5e0:8"
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
      "definition_site": "00b63514",
      "incomplete_value": true,
      "site": "00b63514",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6344c",
      "incomplete_value": true,
      "site": "00b6344c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6351c",
      "incomplete_value": false,
      "site": "00b63524",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63454",
      "incomplete_value": false,
      "site": "00b6345c",
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
            "const:5c7:8"
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
      "00b63510",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6351c",
      "PARAM",
      [
        "storage",
        "002ae5c7",
        null,
        "string"
      ]
    ],
    [
      "00b6352c",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63510",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6351c",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00b6352c",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6345c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63438.md#insn-00b6345c) · [`00b63464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63438.md#insn-00b63464) · [`00b63448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63438.md#insn-00b63448)
- 新版 [`00b63524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md#insn-00b63524) · [`00b6352c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md#insn-00b6352c) · [`00b63510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63500.md#insn-00b63510)

~~~diff
- 00b6345c ["INT_ADD", "register:40f0:8", ["const:b6345c:8", "const:4:8"]]
- 00b6345c ["CALL", null, ["callee:00bde040:8"]]
+ 00b63524 ["INT_ADD", "register:40f0:8", ["const:b63524:8", "const:4:8"]]
+ 00b63524 ["CALL", null, ["callee:00bde040:8"]]
- 00b6345c bytes cdea0194
+ 00b63524 bytes c7ea0194
- 00b63464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b63464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6352c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b6352c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63464 bytes 60f202f9
+ 00b6352c bytes 605203f9
- 00b63448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b63448 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63510 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b63510 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63448 bytes 68f242f9
+ 00b63510 bytes 685243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3003a0bda2cf038050e26db0d951e1df"></a>

### [`00b63478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63478.md) → [`00b63540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b63570",
      "incomplete_value": true,
      "site": "00b63570",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b634a8",
      "incomplete_value": true,
      "site": "00b634a8",
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
            "const:5e0:8"
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
      "definition_site": "00b63554",
      "incomplete_value": true,
      "site": "00b63554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b6348c",
      "incomplete_value": true,
      "site": "00b6348c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63560",
      "incomplete_value": false,
      "site": "00b63568",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63498",
      "incomplete_value": false,
      "site": "00b634a0",
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
            "const:5c7:8"
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
      "00b63550",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63560",
      "PARAM",
      [
        "storage",
        "002ae5c7",
        null,
        "string"
      ]
    ],
    [
      "00b63570",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63550",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63560",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00b63570",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b634a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63478.md#insn-00b634a0) · [`00b634a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63478.md#insn-00b634a8) · [`00b63488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63478.md#insn-00b63488)
- 新版 [`00b63568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md#insn-00b63568) · [`00b63570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md#insn-00b63570) · [`00b63550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63540.md#insn-00b63550)

~~~diff
- 00b634a0 ["INT_ADD", "register:40f0:8", ["const:b634a0:8", "const:4:8"]]
- 00b634a0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b63568 ["INT_ADD", "register:40f0:8", ["const:b63568:8", "const:4:8"]]
+ 00b63568 ["CALL", null, ["callee:00bde040:8"]]
- 00b634a0 bytes bcea0194
+ 00b63568 bytes b6ea0194
- 00b634a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b634a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b63570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b634a8 bytes 60f202f9
+ 00b63570 bytes 605203f9
- 00b63488 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b63488 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b63550 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63488 bytes 68f242f9
+ 00b63550 bytes 685243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f0d2b5edbcb93c31e547c3a9867412"></a>

### [`00b634bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b634bc.md) → [`00b63584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b635b4",
      "incomplete_value": true,
      "site": "00b635b4",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b634ec",
      "incomplete_value": true,
      "site": "00b634ec",
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
            "const:5e0:8"
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
      "definition_site": "00b63598",
      "incomplete_value": true,
      "site": "00b63598",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b634d0",
      "incomplete_value": true,
      "site": "00b634d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b635a0",
      "incomplete_value": false,
      "site": "00b635ac",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b634d8",
      "incomplete_value": false,
      "site": "00b634e4",
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
            "const:5c7:8"
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
      "00b63594",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b635a0",
      "PARAM",
      [
        "storage",
        "002ae5c7",
        null,
        "string"
      ]
    ],
    [
      "00b635b4",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63594",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b635a0",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00b635b4",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b634e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b634bc.md#insn-00b634e4) · [`00b634ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b634bc.md#insn-00b634ec) · [`00b634cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b634bc.md#insn-00b634cc)
- 新版 [`00b635ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md#insn-00b635ac) · [`00b635b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md#insn-00b635b4) · [`00b63594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63584.md#insn-00b63594)

~~~diff
- 00b634e4 ["INT_ADD", "register:40f0:8", ["const:b634e4:8", "const:4:8"]]
- 00b634e4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b635ac ["INT_ADD", "register:40f0:8", ["const:b635ac:8", "const:4:8"]]
+ 00b635ac ["CALL", null, ["callee:00bde040:8"]]
- 00b634e4 bytes abea0194
+ 00b635ac bytes a5ea0194
- 00b634ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b634ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b635b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b635b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b634ec bytes 60f202f9
+ 00b635b4 bytes 605203f9
- 00b634cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b634cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
+ 00b63594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b634cc bytes 68f242f9
+ 00b63594 bytes 685243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5b0d09e212cf486fe00c8db3aaae43c"></a>

### [`00b6350c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6350c.md) → [`00b635d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md) _ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b6362c",
      "incomplete_value": true,
      "site": "00b6362c",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63564",
      "incomplete_value": true,
      "site": "00b63564",
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
            "const:5e8:8"
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
      "definition_site": "00b63608",
      "incomplete_value": true,
      "site": "00b63614",
      "value": [
        "LOAD",
        "8",
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63540",
      "incomplete_value": true,
      "site": "00b6354c",
      "value": [
        "LOAD",
        "8",
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
                "const:5e0:8"
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
      "00b635e8",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63608",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6362c",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b635e8",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63608",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6362c",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6354c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6350c.md#insn-00b6354c) · [`00b63564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6350c.md#insn-00b63564) · [`00b63520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b6350c.md#insn-00b63520)
- 新版 [`00b63614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md#insn-00b63614) · [`00b6362c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md#insn-00b6362c) · [`00b635e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b635d4.md#insn-00b635e8)

~~~diff
- 00b6354c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6354c ["INT_ADD", "register:40f0:8", ["const:b6354c:8", "const:4:8"]]
- 00b6354c ["CALLIND", null, ["register:0:8"]]
+ 00b63614 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63614 ["INT_ADD", "register:40f0:8", ["const:b63614:8", "const:4:8"]]
+ 00b63614 ["CALLIND", null, ["register:0:8"]]
- 00b6354c bytes 00013fd6
+ 00b63614 bytes 00013fd6
- 00b63564 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63564 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5e8:8"]]
- 00b63564 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6362c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6362c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a8:8"]]
+ 00b6362c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63564 bytes a0a21739
+ 00b6362c bytes a0a21a39
- 00b63520 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5e8:8"]]
- 00b63520 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b63520 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b635e8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a8:8"]]
+ 00b635e8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b635e8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b63520 bytes a8a25739
+ 00b635e8 bytes a8a25a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a100c3ac1cacc8abe2d32dd81a7024b7"></a>

### [`00b63578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63578.md) → [`00b63640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md) _ZN8firebase4auth26firebase_network_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b6367c",
      "incomplete_value": true,
      "site": "00b6367c",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b635b4",
      "incomplete_value": true,
      "site": "00b635b4",
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
            "const:5e8:8"
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
      "definition_site": "00b6369c",
      "incomplete_value": true,
      "site": "00b6369c",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b635d4",
      "incomplete_value": true,
      "site": "00b635d4",
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
            "const:5e0:8"
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
      "definition_site": "00b63658",
      "incomplete_value": true,
      "site": "00b63658",
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
      "definition_site": "00b63590",
      "incomplete_value": true,
      "site": "00b63590",
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
      "00b63654",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63660",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6367c",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63654",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63660",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6367c",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b635b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63578.md#insn-00b635b4) · [`00b635d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63578.md#insn-00b635d0) · [`00b635d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63578.md#insn-00b635d4)
- 新版 [`00b6367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md#insn-00b6367c) · [`00b63698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md#insn-00b63698) · [`00b6369c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63640.md#insn-00b6369c)

~~~diff
- 00b635b4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b635b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b635b4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5e8:8"]]
- 00b635b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6367c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6367c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6367c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a8:8"]]
+ 00b6367c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b635b4 bytes bfa21739
+ 00b6367c bytes bfa21a39
- 00b635d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b635d0 ["INT_ADD", "register:40f0:8", ["const:b635d0:8", "const:4:8"]]
- 00b635d0 ["CALLIND", null, ["register:0:8"]]
+ 00b63698 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63698 ["INT_ADD", "register:40f0:8", ["const:b63698:8", "const:4:8"]]
+ 00b63698 ["CALLIND", null, ["register:0:8"]]
- 00b635d0 bytes 00013fd6
+ 00b63698 bytes 00013fd6
- 00b635d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b635d4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b635d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b6369c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b6369c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b6369c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b635d4 bytes 9ff202f9
+ 00b6369c bytes 9f5203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f30286fd466a7eea9cb65a667bd1dda"></a>

### [`00b635e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b635e8.md) → [`00b636b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md) _ZN8firebase4auth26firebase_network_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b636f0",
      "incomplete_value": true,
      "site": "00b636f0",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63628",
      "incomplete_value": true,
      "site": "00b63628",
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
            "const:5e0:8"
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
      "definition_site": "00b636cc",
      "incomplete_value": true,
      "site": "00b636cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63604",
      "incomplete_value": true,
      "site": "00b63604",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b636d4",
      "incomplete_value": false,
      "site": "00b636e8",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6360c",
      "incomplete_value": false,
      "site": "00b63620",
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
            "const:5c7:8"
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
      "00b636c4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b636d4",
      "PARAM",
      [
        "storage",
        "002ae5c7",
        null,
        "string"
      ]
    ],
    [
      "00b636f0",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b636c4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b636d4",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00b636f0",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b635e8.md#insn-00b63620) · [`00b63628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b635e8.md#insn-00b63628) · [`00b635fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b635e8.md#insn-00b635fc)
- 新版 [`00b636e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md#insn-00b636e8) · [`00b636f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md#insn-00b636f0) · [`00b636c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b636b0.md#insn-00b636c4)

~~~diff
- 00b63620 ["INT_ADD", "register:40f0:8", ["const:b63620:8", "const:4:8"]]
- 00b63620 ["CALL", null, ["callee:00bde040:8"]]
+ 00b636e8 ["INT_ADD", "register:40f0:8", ["const:b636e8:8", "const:4:8"]]
+ 00b636e8 ["CALL", null, ["callee:00bde040:8"]]
- 00b63620 bytes 5cea0194
+ 00b636e8 bytes 56ea0194
- 00b63628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b63628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b636f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b636f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63628 bytes 80f202f9
+ 00b636f0 bytes 805203f9
- 00b635fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b635fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b636c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b636c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b635fc bytes 81f242f9
+ 00b636c4 bytes 815243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60fcd324e0778938ef83cfdd53d3f4e4"></a>

### [`00b63658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63658.md) → [`00b63720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md) _ZN8firebase4auth26firebase_network_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b6373c",
      "incomplete_value": false,
      "site": "00b63740",
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
      "definition_site": "00b63674",
      "incomplete_value": false,
      "site": "00b63678",
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
      "definition_site": "00b6374c",
      "incomplete_value": true,
      "site": "00b63758",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63684",
      "incomplete_value": true,
      "site": "00b63690",
      "value": [
        "LOAD",
        "8",
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
      "00b6373c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6374c",
      "DATA",
      [
        "storage",
        "010a15f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6373c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6374c",
      "DATA",
      [
        "storage",
        "010a16b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63658.md#insn-00b63678) · [`00b63674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63658.md#insn-00b63674) · [`00b63680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63658.md#insn-00b63680)
- 新版 [`00b63740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md#insn-00b63740) · [`00b6373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md#insn-00b6373c) · [`00b63748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63720.md#insn-00b63748)

~~~diff
- 00b63678 ["INT_ADD", "register:40f0:8", ["const:b63678:8", "const:4:8"]]
- 00b63678 ["CALL", null, ["callee:00bde130:8"]]
+ 00b63740 ["INT_ADD", "register:40f0:8", ["const:b63740:8", "const:4:8"]]
+ 00b63740 ["CALL", null, ["callee:00bde130:8"]]
- 00b63678 bytes 82ea0194
+ 00b63740 bytes 7cea0194
- 00b63674 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b63674 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63674 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63674 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6373c ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b6373c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6373c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6373c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63674 bytes 001c1591
+ 00b6373c bytes 00501791
- 00b63680 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 00b63680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63748 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00b63748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63680 bytes 08c11791
+ 00b63748 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-434385c396d8a0caea1b04e027b5cc11"></a>

### [`00b63694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63694.md) → [`00b6375c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md) _ZN8firebase4auth26firebase_network_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6379c",
      "incomplete_value": true,
      "site": "00b6379c",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b636d4",
      "incomplete_value": true,
      "site": "00b636d4",
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
            "const:5e0:8"
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
      "definition_site": "00b63778",
      "incomplete_value": true,
      "site": "00b63778",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b636b0",
      "incomplete_value": true,
      "site": "00b636b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63780",
      "incomplete_value": false,
      "site": "00b63794",
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
            "const:533:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b636b8",
      "incomplete_value": false,
      "site": "00b636cc",
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
            "const:5c7:8"
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
      "00b63770",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63780",
      "PARAM",
      [
        "storage",
        "002ae5c7",
        null,
        "string"
      ]
    ],
    [
      "00b6379c",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63770",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63780",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00b6379c",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b636cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63694.md#insn-00b636cc) · [`00b636d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63694.md#insn-00b636d4) · [`00b636a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63694.md#insn-00b636a8)
- 新版 [`00b63794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md#insn-00b63794) · [`00b6379c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md#insn-00b6379c) · [`00b63770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6375c.md#insn-00b63770)

~~~diff
- 00b636cc ["INT_ADD", "register:40f0:8", ["const:b636cc:8", "const:4:8"]]
- 00b636cc ["CALL", null, ["callee:00bde040:8"]]
+ 00b63794 ["INT_ADD", "register:40f0:8", ["const:b63794:8", "const:4:8"]]
+ 00b63794 ["CALL", null, ["callee:00bde040:8"]]
- 00b636cc bytes 31ea0194
+ 00b63794 bytes 2bea0194
- 00b636d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b636d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6379c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b6379c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b636d4 bytes 80f202f9
+ 00b6379c bytes 805203f9
- 00b636a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b636a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63770 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
+ 00b63770 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b636a8 bytes 81f242f9
+ 00b63770 bytes 815243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11b4c21da252c785778729985403d8eb"></a>

### [`00b63704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63704.md) → [`00b637cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md) _ZN8firebase4auth26firebase_network_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b637e8",
      "incomplete_value": false,
      "site": "00b637ec",
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
      "definition_site": "00b63720",
      "incomplete_value": false,
      "site": "00b63724",
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
      "definition_site": "00b637f8",
      "incomplete_value": true,
      "site": "00b63804",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63730",
      "incomplete_value": true,
      "site": "00b6373c",
      "value": [
        "LOAD",
        "8",
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
      "00b637e8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b637f8",
      "DATA",
      [
        "storage",
        "010a15f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b637e8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b637f8",
      "DATA",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63704.md#insn-00b63724) · [`00b63720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63704.md#insn-00b63720) · [`00b6372c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63704.md#insn-00b6372c)
- 新版 [`00b637ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md#insn-00b637ec) · [`00b637e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md#insn-00b637e8) · [`00b637f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b637cc.md#insn-00b637f4)

~~~diff
- 00b63724 ["INT_ADD", "register:40f0:8", ["const:b63724:8", "const:4:8"]]
- 00b63724 ["CALL", null, ["callee:00bde130:8"]]
+ 00b637ec ["INT_ADD", "register:40f0:8", ["const:b637ec:8", "const:4:8"]]
+ 00b637ec ["CALL", null, ["callee:00bde130:8"]]
- 00b63724 bytes 57ea0194
+ 00b637ec bytes 51ea0194
- 00b63720 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b63720 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63720 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63720 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b637e8 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b637e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b637e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b637e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63720 bytes 00c81791
+ 00b637e8 bytes 00fc1991
- 00b6372c ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00b6372c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6372c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6372c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b637f4 ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 00b637f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b637f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b637f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6372c bytes 08e11791
+ 00b637f4 bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6f6e9bda4e962ac59755d0116eef9c4"></a>

### [`00b63740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63740.md) → [`00b63808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b63834",
      "incomplete_value": true,
      "site": "00b63834",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6376c",
      "incomplete_value": true,
      "site": "00b6376c",
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
            "const:600:8"
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
      "definition_site": "00b6381c",
      "incomplete_value": true,
      "site": "00b6381c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63754",
      "incomplete_value": true,
      "site": "00b63754",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63828",
      "incomplete_value": false,
      "site": "00b6382c",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63760",
      "incomplete_value": false,
      "site": "00b63764",
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
            "const:127:8"
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
      "00b63818",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63828",
      "PARAM",
      [
        "storage",
        "002a5127",
        null,
        "string"
      ]
    ],
    [
      "00b63834",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63818",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63828",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63834",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63740.md#insn-00b63764) · [`00b6376c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63740.md#insn-00b6376c) · [`00b63750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63740.md#insn-00b63750)
- 新版 [`00b6382c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md#insn-00b6382c) · [`00b63834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md#insn-00b63834) · [`00b63818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63808.md#insn-00b63818)

~~~diff
- 00b63764 ["INT_ADD", "register:40f0:8", ["const:b63764:8", "const:4:8"]]
- 00b63764 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6382c ["INT_ADD", "register:40f0:8", ["const:b6382c:8", "const:4:8"]]
+ 00b6382c ["CALL", null, ["callee:00bde040:8"]]
- 00b63764 bytes 0bea0194
+ 00b6382c bytes 05ea0194
- 00b6376c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b6376c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6376c bytes 600203f9
+ 00b63834 bytes 606203f9
- 00b63750 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b63750 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63818 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63818 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63750 bytes 680243f9
+ 00b63818 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84a4b32438e500c5b6b779ceb0e9424f"></a>

### [`00b63780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63780.md) → [`00b63848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b63874",
      "incomplete_value": true,
      "site": "00b63874",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b637ac",
      "incomplete_value": true,
      "site": "00b637ac",
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
            "const:600:8"
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
      "definition_site": "00b6385c",
      "incomplete_value": true,
      "site": "00b6385c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63794",
      "incomplete_value": true,
      "site": "00b63794",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b63864",
      "incomplete_value": false,
      "site": "00b6386c",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6379c",
      "incomplete_value": false,
      "site": "00b637a4",
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
            "const:127:8"
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
      "00b63858",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63864",
      "PARAM",
      [
        "storage",
        "002a5127",
        null,
        "string"
      ]
    ],
    [
      "00b63874",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63858",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63864",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63874",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b637a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63780.md#insn-00b637a4) · [`00b637ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63780.md#insn-00b637ac) · [`00b63790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63780.md#insn-00b63790)
- 新版 [`00b6386c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md#insn-00b6386c) · [`00b63874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md#insn-00b63874) · [`00b63858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63848.md#insn-00b63858)

~~~diff
- 00b637a4 ["INT_ADD", "register:40f0:8", ["const:b637a4:8", "const:4:8"]]
- 00b637a4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6386c ["INT_ADD", "register:40f0:8", ["const:b6386c:8", "const:4:8"]]
+ 00b6386c ["CALL", null, ["callee:00bde040:8"]]
- 00b637a4 bytes fbe90194
+ 00b6386c bytes f5e90194
- 00b637ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b637ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b637ac bytes 600203f9
+ 00b63874 bytes 606203f9
- 00b63790 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b63790 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63858 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63790 bytes 680243f9
+ 00b63858 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

