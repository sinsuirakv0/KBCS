# v16.0.0 → v16.0.1 · 最優先の変更候補 (73)

[一覧の目次](README.md)

<a id="compare-a64be3ad2760afa3e7d0d1411a5e54fd"></a>

### [`00b4c074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c074.md) → [`00b4c49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c49c.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b4c0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c4c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c4b0",
      "incomplete_value": true,
      "site": "00b4c4b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c088",
      "incomplete_value": true,
      "site": "00b4c088",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b4c4ac",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4c0a4"
      ]
    ],
    [
      "unmatched:00b4c090",
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
      "00b4c4ac",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c4cc"
      ]
    ],
    [
      "00b4c4b8",
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

- 旧版 [`00b4c098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c074.md#insn-00b4c098) · [`00b4c0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c074.md#insn-00b4c0a0) · [`00b4c0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c074.md#insn-00b4c0b0)

~~~diff
- 00b4c098 ["INT_ADD", "register:40f0:8", ["const:b4c098:8", "const:4:8"]]
- 00b4c098 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c098 bytes 9e3a0494
- 00b4c0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b4c0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c0a0 bytes 600a04f9
- 00b4c0b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4c0b0 ["RETURN", null, ["register:0:8"]]
- 00b4c0b0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91cb9d697bc732d465578f455b3cb35e"></a>

### [`00b4c0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0b4.md) → [`00b4c4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c4dc.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4c50c",
      "incomplete_value": true,
      "site": "00b4c50c",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c0e4",
      "incomplete_value": true,
      "site": "00b4c0e4",
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
            "const:810:8"
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
      "definition_site": "00b4c4f0",
      "incomplete_value": true,
      "site": "00b4c4f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c4fc",
      "incomplete_value": false,
      "site": "00b4c504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:aac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c0d4",
      "incomplete_value": false,
      "site": "00b4c0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a6c:8"
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
      "00b4c4ec",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4fc",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c50c",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c4ec",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4fc",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ],
    [
      "00b4c50c",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0b4.md#insn-00b4c0dc) · [`00b4c0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0b4.md#insn-00b4c0e4) · [`00b4c0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0b4.md#insn-00b4c0c4)
- 新版 `00b4c504`（命令位置の公開資料なし） · `00b4c50c`（命令位置の公開資料なし） · `00b4c4ec`（命令位置の公開資料なし）

~~~diff
- 00b4c0dc ["INT_ADD", "register:40f0:8", ["const:b4c0dc:8", "const:4:8"]]
- 00b4c0dc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c504 ["INT_ADD", "register:40f0:8", ["const:b4c504:8", "const:4:8"]]
+ 00b4c504 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c0dc bytes 8d3a0494
+ 00b4c504 bytes 833a0494
- 00b4c0e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b4c0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c50c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4c50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c0e4 bytes 600a04f9
+ 00b4c50c bytes 600a06f9
- 00b4c0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b4c0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c4ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4c4ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c0c4 bytes 680a44f9
+ 00b4c4ec bytes 680a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-813c668c19b716d8de3af20b6a792809"></a>

### [`00b4c0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0f8.md) → [`00b4c520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c520.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c550",
      "incomplete_value": true,
      "site": "00b4c550",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c128",
      "incomplete_value": true,
      "site": "00b4c128",
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
            "const:810:8"
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
      "definition_site": "00b4c534",
      "incomplete_value": true,
      "site": "00b4c534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c10c",
      "incomplete_value": true,
      "site": "00b4c10c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4c53c",
      "incomplete_value": false,
      "site": "00b4c548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:aac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c114",
      "incomplete_value": false,
      "site": "00b4c120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a6c:8"
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
      "00b4c530",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c53c",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c550",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c530",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c53c",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ],
    [
      "00b4c550",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0f8.md#insn-00b4c120) · [`00b4c128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0f8.md#insn-00b4c128) · [`00b4c108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0f8.md#insn-00b4c108)
- 新版 `00b4c548`（命令位置の公開資料なし） · `00b4c550`（命令位置の公開資料なし） · `00b4c530`（命令位置の公開資料なし）

~~~diff
- 00b4c120 ["INT_ADD", "register:40f0:8", ["const:b4c120:8", "const:4:8"]]
- 00b4c120 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c548 ["INT_ADD", "register:40f0:8", ["const:b4c548:8", "const:4:8"]]
+ 00b4c548 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c120 bytes 7c3a0494
+ 00b4c548 bytes 723a0494
- 00b4c128 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b4c128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4c550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c128 bytes 600a04f9
+ 00b4c550 bytes 600a06f9
- 00b4c108 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00b4c108 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
+ 00b4c530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c108 bytes 680a44f9
+ 00b4c530 bytes 680a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceab4122cbf3fd555a2c7a9acbe0c728"></a>

### [`00b4c148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c148.md) → [`00b4c570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c570.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4c5f8",
      "incomplete_value": true,
      "site": "00b4c5f8",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c1d0",
      "incomplete_value": true,
      "site": "00b4c1d0",
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
            "const:818:8"
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
      "definition_site": "00b4c5a4",
      "incomplete_value": true,
      "site": "00b4c5b0",
      "value": [
        "LOAD",
        "8",
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
                "const:c10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c17c",
      "incomplete_value": true,
      "site": "00b4c188",
      "value": [
        "LOAD",
        "8",
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
                "const:810:8"
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
      "00b4c584",
      "READ",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c5a4",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c5f8",
      "WRITE",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c584",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c5a4",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c5f8",
      "WRITE",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c148.md#insn-00b4c188) · [`00b4c1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c148.md#insn-00b4c1d0) · [`00b4c15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c148.md#insn-00b4c15c)
- 新版 `00b4c5b0`（命令位置の公開資料なし） · `00b4c5f8`（命令位置の公開資料なし） · `00b4c584`（命令位置の公開資料なし）

~~~diff
- 00b4c188 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c188 ["INT_ADD", "register:40f0:8", ["const:b4c188:8", "const:4:8"]]
- 00b4c188 ["CALLIND", null, ["register:0:8"]]
+ 00b4c5b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c5b0 ["INT_ADD", "register:40f0:8", ["const:b4c5b0:8", "const:4:8"]]
+ 00b4c5b0 ["CALLIND", null, ["register:0:8"]]
- 00b4c188 bytes 00013fd6
+ 00b4c5b0 bytes 00013fd6
- 00b4c1d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c1d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:818:8"]]
- 00b4c1d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c5f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c5f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c18:8"]]
+ 00b4c5f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c1d0 bytes a0622039
+ 00b4c5f8 bytes a0623039
- 00b4c15c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:818:8"]]
- 00b4c15c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4c15c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4c584 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c18:8"]]
+ 00b4c584 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c584 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4c15c bytes a8626039
+ 00b4c584 bytes a8627039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ed151a9f4184029db8233cae5d29bc1"></a>

### [`00b4c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c1e4.md) → [`00b4c60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c60c.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4c648",
      "incomplete_value": true,
      "site": "00b4c648",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c220",
      "incomplete_value": true,
      "site": "00b4c220",
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
            "const:818:8"
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
      "definition_site": "00b4c698",
      "incomplete_value": true,
      "site": "00b4c698",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c270",
      "incomplete_value": true,
      "site": "00b4c270",
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
            "const:810:8"
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
      "definition_site": "00b4c624",
      "incomplete_value": true,
      "site": "00b4c624",
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
      "definition_site": "00b4c1fc",
      "incomplete_value": true,
      "site": "00b4c1fc",
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
      "00b4c620",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c62c",
      "READ",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c648",
      "WRITE",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c620",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c62c",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c648",
      "WRITE",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c1e4.md#insn-00b4c220) · [`00b4c26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c1e4.md#insn-00b4c26c) · [`00b4c270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c1e4.md#insn-00b4c270)
- 新版 `00b4c648`（命令位置の公開資料なし） · `00b4c694`（命令位置の公開資料なし） · `00b4c698`（命令位置の公開資料なし）

~~~diff
- 00b4c220 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c220 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c220 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:818:8"]]
- 00b4c220 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c648 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c648 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c648 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c18:8"]]
+ 00b4c648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c220 bytes bf622039
+ 00b4c648 bytes bf623039
- 00b4c26c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c26c ["INT_ADD", "register:40f0:8", ["const:b4c26c:8", "const:4:8"]]
- 00b4c26c ["CALLIND", null, ["register:0:8"]]
+ 00b4c694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c694 ["INT_ADD", "register:40f0:8", ["const:b4c694:8", "const:4:8"]]
+ 00b4c694 ["CALLIND", null, ["register:0:8"]]
- 00b4c26c bytes 00013fd6
+ 00b4c694 bytes 00013fd6
- 00b4c270 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b4c270 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4c270 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4c698 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4c270 bytes 9f0a04f9
+ 00b4c698 bytes 9f0a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48dd3ce292bab134edb0e20c33d2eb54"></a>

### [`00b4c284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c284.md) → [`00b4c6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c6ac.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00b4c2c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c6ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c2a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c298",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c2a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c6f0"
      ]
    ],
    [
      "unmatched:00b4c2a8",
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
      "00b4c6c0",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c6f0"
      ]
    ],
    [
      "00b4c6d0",
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

- 旧版 [`00b4c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c284.md#insn-00b4c2a0) · [`00b4c2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c284.md#insn-00b4c2bc) · [`00b4c2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c284.md#insn-00b4c2c4)
- 新版 `00b4c6e4`（命令位置の公開資料なし）

~~~diff
- 00b4c2a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c2a0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4c2a0 bytes 410100b5
- 00b4c2bc ["INT_ADD", "register:40f0:8", ["const:b4c2bc:8", "const:4:8"]]
- 00b4c2bc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c6e4 ["INT_ADD", "register:40f0:8", ["const:b4c6e4:8", "const:4:8"]]
+ 00b4c6e4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c2bc bytes 153a0494
+ 00b4c6e4 bytes 0b3a0494
- 00b4c2c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b4c2c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c2c4 bytes 800a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fad7e1beed7733555b2ec369f81d193"></a>

### [`00b4c330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c330.md) → [`00b4c758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c758.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c798",
      "incomplete_value": true,
      "site": "00b4c798",
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
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c370",
      "incomplete_value": true,
      "site": "00b4c370",
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
            "const:810:8"
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
      "definition_site": "00b4c774",
      "incomplete_value": true,
      "site": "00b4c774",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c34c",
      "incomplete_value": true,
      "site": "00b4c34c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4c77c",
      "incomplete_value": false,
      "site": "00b4c790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:aac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c354",
      "incomplete_value": false,
      "site": "00b4c368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a6c:8"
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
      "00b4c76c",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c77c",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c798",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c76c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c77c",
      "PARAM",
      [
        "storage",
        "002b8aac",
        null,
        "string"
      ]
    ],
    [
      "00b4c798",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c330.md#insn-00b4c368) · [`00b4c370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c330.md#insn-00b4c370) · [`00b4c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c330.md#insn-00b4c344)
- 新版 `00b4c790`（命令位置の公開資料なし） · `00b4c798`（命令位置の公開資料なし） · `00b4c76c`（命令位置の公開資料なし）

~~~diff
- 00b4c368 ["INT_ADD", "register:40f0:8", ["const:b4c368:8", "const:4:8"]]
- 00b4c368 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c790 ["INT_ADD", "register:40f0:8", ["const:b4c790:8", "const:4:8"]]
+ 00b4c790 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c368 bytes ea390494
+ 00b4c790 bytes e0390494
- 00b4c370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b4c370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c798 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4c798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c370 bytes 800a04f9
+ 00b4c798 bytes 800a06f9
- 00b4c344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00b4c344 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c76c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
+ 00b4c76c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c344 bytes 810a44f9
+ 00b4c76c bytes 810a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a03c1baf9e72011e72f3f29fad16be"></a>

### [`00b4c3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3a0.md) → [`00b4c7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c7c8.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4c7e4",
      "incomplete_value": false,
      "site": "00b4c7e8",
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
      "definition_site": "00b4c3bc",
      "incomplete_value": false,
      "site": "00b4c3c0",
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
      "definition_site": "00b4c7f4",
      "incomplete_value": true,
      "site": "00b4c800",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4c3cc",
      "incomplete_value": true,
      "site": "00b4c3d8",
      "value": [
        "LOAD",
        "8",
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
      "00b4c7e4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4c7f4",
      "DATA",
      [
        "storage",
        "01125830",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c7e4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4c7f4",
      "DATA",
      [
        "storage",
        "01125c30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3a0.md#insn-00b4c3c0) · [`00b4c3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3a0.md#insn-00b4c3bc) · [`00b4c3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3a0.md#insn-00b4c3c8)
- 新版 `00b4c7e8`（命令位置の公開資料なし） · `00b4c7e4`（命令位置の公開資料なし） · `00b4c7f0`（命令位置の公開資料なし）

~~~diff
- 00b4c3c0 ["INT_ADD", "register:40f0:8", ["const:b4c3c0:8", "const:4:8"]]
- 00b4c3c0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4c7e8 ["INT_ADD", "register:40f0:8", ["const:b4c7e8:8", "const:4:8"]]
+ 00b4c7e8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4c3c0 bytes 103a0494
+ 00b4c7e8 bytes 063a0494
- 00b4c3bc ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4c3bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c3bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c3bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c7e4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4c7e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c7e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c7e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c3bc bytes 00441191
+ 00b4c7e4 bytes 00781491
- 00b4c3c8 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00b4c3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4c7f0 ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 00b4c7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4c7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4c3c8 bytes 08c12091
+ 00b4c7f0 bytes 08c13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd7e4b18faa73d95cbf45f17f7420e3a"></a>

### [`00b4c3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3dc.md) → [`00b4c804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c804.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b4c830",
      "incomplete_value": true,
      "site": "00b4c830",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c408",
      "incomplete_value": true,
      "site": "00b4c408",
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
            "const:838:8"
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
      "definition_site": "00b4c818",
      "incomplete_value": true,
      "site": "00b4c818",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c3f0",
      "incomplete_value": true,
      "site": "00b4c3f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4c824",
      "incomplete_value": false,
      "site": "00b4c828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:5da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c3fc",
      "incomplete_value": false,
      "site": "00b4c400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:59a:8"
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
      "00b4c814",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c824",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c830",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c814",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c824",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4c830",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3dc.md#insn-00b4c400) · [`00b4c408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3dc.md#insn-00b4c408) · [`00b4c3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3dc.md#insn-00b4c3ec)
- 新版 `00b4c828`（命令位置の公開資料なし） · `00b4c830`（命令位置の公開資料なし） · `00b4c814`（命令位置の公開資料なし）

~~~diff
- 00b4c400 ["INT_ADD", "register:40f0:8", ["const:b4c400:8", "const:4:8"]]
- 00b4c400 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c828 ["INT_ADD", "register:40f0:8", ["const:b4c828:8", "const:4:8"]]
+ 00b4c828 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c400 bytes c4390494
+ 00b4c828 bytes ba390494
- 00b4c408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
- 00b4c408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
+ 00b4c830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c408 bytes 601e04f9
+ 00b4c830 bytes 601e06f9
- 00b4c3ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
- 00b4c3ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
+ 00b4c814 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c3ec bytes 681e44f9
+ 00b4c814 bytes 681e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfe7a9c5c5a1efa96caa18e857a8c353"></a>

### [`00b4c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c41c.md) → [`00b4c844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c844.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4c870",
      "incomplete_value": true,
      "site": "00b4c870",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c448",
      "incomplete_value": true,
      "site": "00b4c448",
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
            "const:838:8"
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
      "definition_site": "00b4c858",
      "incomplete_value": true,
      "site": "00b4c858",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c430",
      "incomplete_value": true,
      "site": "00b4c430",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4c860",
      "incomplete_value": false,
      "site": "00b4c868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:5da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c438",
      "incomplete_value": false,
      "site": "00b4c440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:59a:8"
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
      "00b4c854",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c860",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c870",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c854",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c860",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4c870",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c41c.md#insn-00b4c440) · [`00b4c448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c41c.md#insn-00b4c448) · [`00b4c42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c41c.md#insn-00b4c42c)
- 新版 `00b4c868`（命令位置の公開資料なし） · `00b4c870`（命令位置の公開資料なし） · `00b4c854`（命令位置の公開資料なし）

~~~diff
- 00b4c440 ["INT_ADD", "register:40f0:8", ["const:b4c440:8", "const:4:8"]]
- 00b4c440 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c868 ["INT_ADD", "register:40f0:8", ["const:b4c868:8", "const:4:8"]]
+ 00b4c868 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c440 bytes b4390494
+ 00b4c868 bytes aa390494
- 00b4c448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
- 00b4c448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
+ 00b4c870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c448 bytes 601e04f9
+ 00b4c870 bytes 601e06f9
- 00b4c42c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
- 00b4c42c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c854 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
+ 00b4c854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c42c bytes 681e44f9
+ 00b4c854 bytes 681e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9471e719da7a03cafff776cd96f99801"></a>

### [`00b4c45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c45c.md) → [`00b4c884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c884.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4c45c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c460"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c460"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4c460",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c894",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c884",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c888",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4c894",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c45c.md#insn-00b4c45c) · [`00b4c460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c45c.md#insn-00b4c460) · [`00b4c470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c45c.md#insn-00b4c470)
- 新版 `00b4c898`（命令位置の公開資料なし）

~~~diff
- 00b4c45c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4c45c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4c45c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4c45c bytes f30f1ef8
- 00b4c460 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4c460 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4c460 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4c460 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4c460 bytes fd7b01a9
- 00b4c470 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4c470 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4c898 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4c898 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4c470 bytes 080100b5
+ 00b4c898 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2673e25e98c5619660d366d19967d028"></a>

### [`00b4c4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4a0.md) → [`00b4c8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c8c8.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c8f8",
      "incomplete_value": true,
      "site": "00b4c8f8",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c4d0",
      "incomplete_value": true,
      "site": "00b4c4d0",
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
            "const:838:8"
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
      "definition_site": "00b4c8dc",
      "incomplete_value": true,
      "site": "00b4c8dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c4b4",
      "incomplete_value": true,
      "site": "00b4c4b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4c8e4",
      "incomplete_value": false,
      "site": "00b4c8f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:5da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c4bc",
      "incomplete_value": false,
      "site": "00b4c4c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:59a:8"
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
      "00b4c8d8",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8e4",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c8f8",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c8d8",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8e4",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ],
    [
      "00b4c8f8",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4a0.md#insn-00b4c4c8) · [`00b4c4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4a0.md#insn-00b4c4d0) · [`00b4c4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4a0.md#insn-00b4c4b0)
- 新版 `00b4c8f0`（命令位置の公開資料なし） · `00b4c8f8`（命令位置の公開資料なし） · `00b4c8d8`（命令位置の公開資料なし）

~~~diff
- 00b4c4c8 ["INT_ADD", "register:40f0:8", ["const:b4c4c8:8", "const:4:8"]]
- 00b4c4c8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4c8f0 ["INT_ADD", "register:40f0:8", ["const:b4c8f0:8", "const:4:8"]]
+ 00b4c8f0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c4c8 bytes 92390494
+ 00b4c8f0 bytes 88390494
- 00b4c4d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
- 00b4c4d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c8f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
+ 00b4c8f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c4d0 bytes 601e04f9
+ 00b4c8f8 bytes 601e06f9
- 00b4c4b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
- 00b4c4b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4c8d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c38:8"]]
+ 00b4c8d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c4b0 bytes 681e44f9
+ 00b4c8d8 bytes 681e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8170721e1129cafb391e38d092a62cbb"></a>

### [`00b4c4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4f0.md) → [`00b4c918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c918.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c9a0",
      "incomplete_value": true,
      "site": "00b4c9a0",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c578",
      "incomplete_value": true,
      "site": "00b4c578",
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
            "const:840:8"
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
      "site": "00b4c530"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c55c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c92c",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4c524",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c9a0",
      "WRITE",
      [
        "storage",
        "01125840",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c92c",
      "READ",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c94c",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c9a0",
      "WRITE",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4f0.md#insn-00b4c530) · [`00b4c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4f0.md#insn-00b4c55c) · [`00b4c578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4f0.md#insn-00b4c578)
- 新版 `00b4c9a0`（命令位置の公開資料なし）

~~~diff
- 00b4c530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c530 ["INT_ADD", "register:40f0:8", ["const:b4c530:8", "const:4:8"]]
- 00b4c530 ["CALLIND", null, ["register:0:8"]]
- 00b4c530 bytes 00013fd6
- 00b4c55c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c55c ["INT_ADD", "register:40f0:8", ["const:b4c55c:8", "const:4:8"]]
- 00b4c55c ["CALLIND", null, ["register:0:8"]]
- 00b4c55c bytes 00013fd6
- 00b4c578 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c578 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:840:8"]]
- 00b4c578 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c9a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c9a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c40:8"]]
+ 00b4c9a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c578 bytes a0022139
+ 00b4c9a0 bytes a0023139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46041c5fd3e916a6e95587a688010c7"></a>

### [`00b4c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c58c.md) → [`00b4c9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c9b4.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4c9f0",
      "incomplete_value": true,
      "site": "00b4c9f0",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5c8",
      "incomplete_value": true,
      "site": "00b4c5c8",
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
            "const:840:8"
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
      "definition_site": "00b4ca40",
      "incomplete_value": true,
      "site": "00b4ca40",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c618",
      "incomplete_value": true,
      "site": "00b4c618",
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
            "const:838:8"
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
      "definition_site": "00b4c9cc",
      "incomplete_value": true,
      "site": "00b4c9cc",
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
      "definition_site": "00b4c5a4",
      "incomplete_value": true,
      "site": "00b4c5a4",
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
      "00b4c9c8",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c9d4",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c9f0",
      "WRITE",
      [
        "storage",
        "01125840",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c9c8",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c9d4",
      "READ",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c9f0",
      "WRITE",
      [
        "storage",
        "01125c40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c58c.md#insn-00b4c5c8) · [`00b4c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c58c.md#insn-00b4c614) · [`00b4c618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c58c.md#insn-00b4c618)
- 新版 `00b4c9f0`（命令位置の公開資料なし） · `00b4ca3c`（命令位置の公開資料なし） · `00b4ca40`（命令位置の公開資料なし）

~~~diff
- 00b4c5c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c5c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c5c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:840:8"]]
- 00b4c5c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c9f0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c9f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c9f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c40:8"]]
+ 00b4c9f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c5c8 bytes bf022139
+ 00b4c9f0 bytes bf023139
- 00b4c614 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c614 ["INT_ADD", "register:40f0:8", ["const:b4c614:8", "const:4:8"]]
- 00b4c614 ["CALLIND", null, ["register:0:8"]]
+ 00b4ca3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ca3c ["INT_ADD", "register:40f0:8", ["const:b4ca3c:8", "const:4:8"]]
+ 00b4ca3c ["CALLIND", null, ["register:0:8"]]
- 00b4c614 bytes 00013fd6
+ 00b4ca3c bytes 00013fd6
- 00b4c618 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
- 00b4c618 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4c618 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4ca40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
+ 00b4ca40 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4ca40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4c618 bytes 9f1e04f9
+ 00b4ca40 bytes 9f1e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56496e8ae16941eb2fbe1acc88647f64"></a>

### [`00b4c62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c62c.md) → [`00b4ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ca54.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00b4c66c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ca94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c640",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c648",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ca98"
      ]
    ],
    [
      "unmatched:00b4c650",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca68",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ca98"
      ]
    ],
    [
      "00b4ca78",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c62c.md#insn-00b4c648) · [`00b4c664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c62c.md#insn-00b4c664) · [`00b4c66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c62c.md#insn-00b4c66c)
- 新版 `00b4ca8c`（命令位置の公開資料なし）

~~~diff
- 00b4c648 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c648 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4c648 bytes 410100b5
- 00b4c664 ["INT_ADD", "register:40f0:8", ["const:b4c664:8", "const:4:8"]]
- 00b4c664 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ca8c ["INT_ADD", "register:40f0:8", ["const:b4ca8c:8", "const:4:8"]]
+ 00b4ca8c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c664 bytes 2b390494
+ 00b4ca8c bytes 21390494
- 00b4c66c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
- 00b4c66c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c66c bytes 801e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a9002ef4deb2c2b9079ee41db09d0f"></a>

### [`00b4c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c69c.md) → [`00b4cac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cac4.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab80.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af80.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4cae0",
      "incomplete_value": false,
      "site": "00b4cae4",
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
      "definition_site": "00b4c6b8",
      "incomplete_value": false,
      "site": "00b4c6bc",
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
      "definition_site": "00b4caf0",
      "incomplete_value": true,
      "site": "00b4cafc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4c6c8",
      "incomplete_value": true,
      "site": "00b4c6d4",
      "value": [
        "LOAD",
        "8",
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
      "00b4cae0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4caf0",
      "DATA",
      [
        "storage",
        "01125848",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cae0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4caf0",
      "DATA",
      [
        "storage",
        "01125c48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c69c.md#insn-00b4c6bc) · [`00b4c6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c69c.md#insn-00b4c6b8) · [`00b4c6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c69c.md#insn-00b4c6c4)
- 新版 `00b4cae4`（命令位置の公開資料なし） · `00b4cae0`（命令位置の公開資料なし） · `00b4caec`（命令位置の公開資料なし）

~~~diff
- 00b4c6bc ["INT_ADD", "register:40f0:8", ["const:b4c6bc:8", "const:4:8"]]
- 00b4c6bc ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4cae4 ["INT_ADD", "register:40f0:8", ["const:b4cae4:8", "const:4:8"]]
+ 00b4cae4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4c6bc bytes 51390494
+ 00b4cae4 bytes 47390494
- 00b4c6b8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4c6b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c6b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c6b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cae0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4cae0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cae0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cae0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c6b8 bytes 00680a91
+ 00b4cae0 bytes 009c0d91
- 00b4c6c4 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00b4c6c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c6c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4c6c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4caec ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00b4caec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4caec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4caec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4c6c4 bytes 08212191
+ 00b4caec bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaa3974d73e01ebc3caf7a7c6646bc33"></a>

### [`00b4c6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c6d8.md) → [`00b4cb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cb00.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4c718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4cb40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c6f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c6ec",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4cb44"
      ]
    ],
    [
      "unmatched:00b4c6fc",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb14",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4cb44"
      ]
    ],
    [
      "00b4cb24",
      "PARAM",
      [
        "storage",
        "002b15da",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c6f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c6d8.md#insn-00b4c6f4) · [`00b4c710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c6d8.md#insn-00b4c710) · [`00b4c718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c6d8.md#insn-00b4c718)
- 新版 `00b4cb38`（命令位置の公開資料なし）

~~~diff
- 00b4c6f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c6f4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4c6f4 bytes 410100b5
- 00b4c710 ["INT_ADD", "register:40f0:8", ["const:b4c710:8", "const:4:8"]]
- 00b4c710 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cb38 ["INT_ADD", "register:40f0:8", ["const:b4cb38:8", "const:4:8"]]
+ 00b4cb38 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c710 bytes 00390494
+ 00b4cb38 bytes f6380494
- 00b4c718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
- 00b4c718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c718 bytes 801e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-751b5e150dd6d203a24e93946ca77c6c"></a>

### [`00b4c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c784.md) → [`00b4cbac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cbac.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00b4cbd8",
      "incomplete_value": true,
      "site": "00b4cbd8",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c7b0",
      "incomplete_value": true,
      "site": "00b4c7b0",
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
            "const:868:8"
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
      "definition_site": "00b4cbc0",
      "incomplete_value": true,
      "site": "00b4cbc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c798",
      "incomplete_value": true,
      "site": "00b4c798",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cbcc",
      "incomplete_value": false,
      "site": "00b4cbd0",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c7a4",
      "incomplete_value": false,
      "site": "00b4c7a8",
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
            "const:a62:8"
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
      "00b4cbbc",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbcc",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4cbd8",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cbbc",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbcc",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cbd8",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c784.md#insn-00b4c7a8) · [`00b4c7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c784.md#insn-00b4c7b0) · [`00b4c794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c784.md#insn-00b4c794)
- 新版 `00b4cbd0`（命令位置の公開資料なし） · `00b4cbd8`（命令位置の公開資料なし） · `00b4cbbc`（命令位置の公開資料なし）

~~~diff
- 00b4c7a8 ["INT_ADD", "register:40f0:8", ["const:b4c7a8:8", "const:4:8"]]
- 00b4c7a8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cbd0 ["INT_ADD", "register:40f0:8", ["const:b4cbd0:8", "const:4:8"]]
+ 00b4cbd0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c7a8 bytes da380494
+ 00b4cbd0 bytes d0380494
- 00b4c7b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c7b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cbd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00b4cbd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c7b0 bytes 603604f9
+ 00b4cbd8 bytes 603606f9
- 00b4c794 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cbbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00b4cbbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c794 bytes 683644f9
+ 00b4cbbc bytes 683646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2b8c122a0e9b09baa3185d3a49d4d8"></a>

### [`00b4c7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c7c4.md) → [`00b4cbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cbec.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00b4cc18",
      "incomplete_value": true,
      "site": "00b4cc18",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c7f0",
      "incomplete_value": true,
      "site": "00b4c7f0",
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
            "const:868:8"
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
      "definition_site": "00b4cc00",
      "incomplete_value": true,
      "site": "00b4cc00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c7d8",
      "incomplete_value": true,
      "site": "00b4c7d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cc08",
      "incomplete_value": false,
      "site": "00b4cc10",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c7e0",
      "incomplete_value": false,
      "site": "00b4c7e8",
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
            "const:a62:8"
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
      "00b4cbfc",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc08",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4cc18",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cbfc",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc08",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cc18",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c7c4.md#insn-00b4c7e8) · [`00b4c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c7c4.md#insn-00b4c7f0) · [`00b4c7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c7c4.md#insn-00b4c7d4)
- 新版 `00b4cc10`（命令位置の公開資料なし） · `00b4cc18`（命令位置の公開資料なし） · `00b4cbfc`（命令位置の公開資料なし）

~~~diff
- 00b4c7e8 ["INT_ADD", "register:40f0:8", ["const:b4c7e8:8", "const:4:8"]]
- 00b4c7e8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cc10 ["INT_ADD", "register:40f0:8", ["const:b4cc10:8", "const:4:8"]]
+ 00b4cc10 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c7e8 bytes ca380494
+ 00b4cc10 bytes c0380494
- 00b4c7f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cc18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00b4cc18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c7f0 bytes 603604f9
+ 00b4cc18 bytes 603606f9
- 00b4c7d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c7d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cbfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00b4cbfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c7d4 bytes 683644f9
+ 00b4cbfc bytes 683646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-209c63e84ec5e0cc88b1becb2376abf7"></a>

### [`00b4c804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c804.md) → [`00b4cc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc2c.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4c834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4cc5c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cc40",
      "incomplete_value": true,
      "site": "00b4cc40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c818",
      "incomplete_value": true,
      "site": "00b4c818",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b4cc3c",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c824",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b4c82c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5af10"
      ]
    ]
  ],
  "added": [
    [
      "00b4cc3c",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc4c",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cc54",
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

- 旧版 [`00b4c818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c804.md#insn-00b4c818) · [`00b4c82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c804.md#insn-00b4c82c) · [`00b4c834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c804.md#insn-00b4c834)
- 新版 `00b4cc40`（命令位置の公開資料なし）

~~~diff
- 00b4c818 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b4c818 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b4cc40 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4cc40 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b4c818 bytes 080100b5
+ 00b4cc40 bytes 080100b5
- 00b4c82c ["INT_ADD", "register:40f0:8", ["const:b4c82c:8", "const:4:8"]]
- 00b4c82c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c82c bytes b9380494
- 00b4c834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c834 bytes 603604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76c558236ad746cc096e5bdbc31c9d04"></a>

### [`00b4c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c848.md) → [`00b4cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cc70.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4cca0",
      "incomplete_value": true,
      "site": "00b4cca0",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c878",
      "incomplete_value": true,
      "site": "00b4c878",
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
            "const:868:8"
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
      "definition_site": "00b4cc84",
      "incomplete_value": true,
      "site": "00b4cc84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c85c",
      "incomplete_value": true,
      "site": "00b4c85c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cc8c",
      "incomplete_value": false,
      "site": "00b4cc98",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c864",
      "incomplete_value": false,
      "site": "00b4c870",
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
            "const:a62:8"
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
      "00b4cc80",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc8c",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4cca0",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cc80",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc8c",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cca0",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c848.md#insn-00b4c870) · [`00b4c878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c848.md#insn-00b4c878) · [`00b4c858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c848.md#insn-00b4c858)
- 新版 `00b4cc98`（命令位置の公開資料なし） · `00b4cca0`（命令位置の公開資料なし） · `00b4cc80`（命令位置の公開資料なし）

~~~diff
- 00b4c870 ["INT_ADD", "register:40f0:8", ["const:b4c870:8", "const:4:8"]]
- 00b4c870 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cc98 ["INT_ADD", "register:40f0:8", ["const:b4cc98:8", "const:4:8"]]
+ 00b4cc98 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4c870 bytes a8380494
+ 00b4cc98 bytes 9e380494
- 00b4c878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00b4cca0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c878 bytes 603604f9
+ 00b4cca0 bytes 603606f9
- 00b4c858 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
- 00b4c858 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cc80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c68:8"]]
+ 00b4cc80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c858 bytes 683644f9
+ 00b4cc80 bytes 683646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7617813e966aa65f5eb496e529d6a4c"></a>

### [`00b4c898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c898.md) → [`00b4ccc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ccc0.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4cd48",
      "incomplete_value": true,
      "site": "00b4cd48",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c920",
      "incomplete_value": true,
      "site": "00b4c920",
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
            "const:870:8"
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
      "definition_site": "00b4ccf4",
      "incomplete_value": true,
      "site": "00b4cd00",
      "value": [
        "LOAD",
        "8",
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
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c8cc",
      "incomplete_value": true,
      "site": "00b4c8d8",
      "value": [
        "LOAD",
        "8",
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
                "const:868:8"
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
      "00b4ccd4",
      "READ",
      [
        "storage",
        "01125870",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ccf4",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd48",
      "WRITE",
      [
        "storage",
        "01125870",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ccd4",
      "READ",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ccf4",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd48",
      "WRITE",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c898.md#insn-00b4c8d8) · [`00b4c920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c898.md#insn-00b4c920) · [`00b4c8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c898.md#insn-00b4c8ac)
- 新版 `00b4cd00`（命令位置の公開資料なし） · `00b4cd48`（命令位置の公開資料なし） · `00b4ccd4`（命令位置の公開資料なし）

~~~diff
- 00b4c8d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c8d8 ["INT_ADD", "register:40f0:8", ["const:b4c8d8:8", "const:4:8"]]
- 00b4c8d8 ["CALLIND", null, ["register:0:8"]]
+ 00b4cd00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cd00 ["INT_ADD", "register:40f0:8", ["const:b4cd00:8", "const:4:8"]]
+ 00b4cd00 ["CALLIND", null, ["register:0:8"]]
- 00b4c8d8 bytes 00013fd6
+ 00b4cd00 bytes 00013fd6
- 00b4c920 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c920 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:870:8"]]
- 00b4c920 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4cd48 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4cd48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c70:8"]]
+ 00b4cd48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c920 bytes a0c22139
+ 00b4cd48 bytes a0c23139
- 00b4c8ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:870:8"]]
- 00b4c8ac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4c8ac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4ccd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c70:8"]]
+ 00b4ccd4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ccd4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4c8ac bytes a8c26139
+ 00b4ccd4 bytes a8c27139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af4c6c9a1110e30d17b42bf142b99bf4"></a>

### [`00b4c934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c934.md) → [`00b4cd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cd5c.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 41.67% / 新版 55.56%

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
      "site": "00b4c970"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4cde8",
      "incomplete_value": true,
      "site": "00b4cde8",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c9c0",
      "incomplete_value": true,
      "site": "00b4c9c0",
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
            "const:868:8"
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
      "site": "00b4cd98"
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
      "00b4cd70",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd7c",
      "READ",
      [
        "storage",
        "01125870",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4c970",
      "WRITE",
      [
        "storage",
        "01125870",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd70",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd7c",
      "READ",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cd98",
      "WRITE",
      [
        "storage",
        "01125c70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c934.md#insn-00b4c94c) · [`00b4c96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c934.md#insn-00b4c96c) · [`00b4c970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c934.md#insn-00b4c970)
- 新版 `00b4cd74`（命令位置の公開資料なし）

~~~diff
- 00b4c94c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c94c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b4cd74 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4cd74 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b4c94c bytes c10300b4
+ 00b4cd74 bytes c10300b4
- 00b4c96c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c96c ["INT_ADD", "register:40f0:8", ["const:b4c96c:8", "const:4:8"]]
- 00b4c96c ["CALLIND", null, ["register:0:8"]]
- 00b4c96c bytes 00013fd6
- 00b4c970 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c970 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c970 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:870:8"]]
- 00b4c970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c970 bytes bfc22139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c046aa050c4b803d36af50adfd98bcac"></a>

### [`00b4c9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c9d4.md) → [`00b4cdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cdfc.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00b4ca14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ce3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4c9f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4c9e8",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4c9f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ce40"
      ]
    ],
    [
      "unmatched:00b4c9f8",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce10",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ce40"
      ]
    ],
    [
      "00b4ce20",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c9d4.md#insn-00b4c9f0) · [`00b4ca0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c9d4.md#insn-00b4ca0c) · [`00b4ca14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c9d4.md#insn-00b4ca14)
- 新版 `00b4ce34`（命令位置の公開資料なし）

~~~diff
- 00b4c9f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4c9f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4c9f0 bytes 410100b5
- 00b4ca0c ["INT_ADD", "register:40f0:8", ["const:b4ca0c:8", "const:4:8"]]
- 00b4ca0c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4ce34 ["INT_ADD", "register:40f0:8", ["const:b4ce34:8", "const:4:8"]]
+ 00b4ce34 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ca0c bytes 41380494
+ 00b4ce34 bytes 37380494
- 00b4ca14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00b4ca14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ca14 bytes 803604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27be6848ed6f528fead38c23e7efc23"></a>

### [`00b4ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca44.md) → [`00b4ce6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4ce6c.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4ce88",
      "incomplete_value": false,
      "site": "00b4ce8c",
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
      "definition_site": "00b4ca60",
      "incomplete_value": false,
      "site": "00b4ca64",
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
      "definition_site": "00b4ce98",
      "incomplete_value": true,
      "site": "00b4cea4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4ca70",
      "incomplete_value": true,
      "site": "00b4ca7c",
      "value": [
        "LOAD",
        "8",
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
      "00b4ce88",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4ce98",
      "DATA",
      [
        "storage",
        "01125878",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ce88",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4ce98",
      "DATA",
      [
        "storage",
        "01125c78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ca64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca44.md#insn-00b4ca64) · [`00b4ca60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca44.md#insn-00b4ca60) · [`00b4ca6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca44.md#insn-00b4ca6c)
- 新版 `00b4ce8c`（命令位置の公開資料なし） · `00b4ce88`（命令位置の公開資料なし） · `00b4ce94`（命令位置の公開資料なし）

~~~diff
- 00b4ca64 ["INT_ADD", "register:40f0:8", ["const:b4ca64:8", "const:4:8"]]
- 00b4ca64 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4ce8c ["INT_ADD", "register:40f0:8", ["const:b4ce8c:8", "const:4:8"]]
+ 00b4ce8c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4ca64 bytes 67380494
+ 00b4ce8c bytes 5d380494
- 00b4ca60 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4ca60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ca60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ca60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ce88 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4ce88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ce88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ce88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ca60 bytes 00680a91
+ 00b4ce88 bytes 009c0d91
- 00b4ca6c ["COPY", "tmp:0:8", ["const:878:8"]]
- 00b4ca6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ca6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ca6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4ce94 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 00b4ce94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ce94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ce94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4ca6c bytes 08e12191
+ 00b4ce94 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01b886c309febf602cf1f5f90ef2c634"></a>

### [`00b4ca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca80.md) → [`00b4cea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cea8.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4cee8",
      "incomplete_value": true,
      "site": "00b4cee8",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cac0",
      "incomplete_value": true,
      "site": "00b4cac0",
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
            "const:868:8"
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
      "definition_site": "00b4cec4",
      "incomplete_value": true,
      "site": "00b4cec4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ca9c",
      "incomplete_value": true,
      "site": "00b4ca9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cecc",
      "incomplete_value": false,
      "site": "00b4cee0",
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
            "const:b2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4caa4",
      "incomplete_value": false,
      "site": "00b4cab8",
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
            "const:a62:8"
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
      "00b4cebc",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cecc",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4cee8",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cebc",
      "READ",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cecc",
      "PARAM",
      [
        "storage",
        "002a3b2f",
        null,
        "string"
      ]
    ],
    [
      "00b4cee8",
      "WRITE",
      [
        "storage",
        "01125c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca80.md#insn-00b4cab8) · [`00b4cac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca80.md#insn-00b4cac0) · [`00b4ca94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca80.md#insn-00b4ca94)
- 新版 `00b4cee0`（命令位置の公開資料なし） · `00b4cee8`（命令位置の公開資料なし） · `00b4cebc`（命令位置の公開資料なし）

~~~diff
- 00b4cab8 ["INT_ADD", "register:40f0:8", ["const:b4cab8:8", "const:4:8"]]
- 00b4cab8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cee0 ["INT_ADD", "register:40f0:8", ["const:b4cee0:8", "const:4:8"]]
+ 00b4cee0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cab8 bytes 16380494
+ 00b4cee0 bytes 0c380494
- 00b4cac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00b4cac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cee8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00b4cee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cac0 bytes 803604f9
+ 00b4cee8 bytes 803606f9
- 00b4ca94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
- 00b4ca94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cebc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c68:8"]]
+ 00b4cebc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ca94 bytes 813644f9
+ 00b4cebc bytes 813646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3726f77bf401a3c173fbbade63c560c1"></a>

### [`00b4caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4caf0.md) → [`00b4cf18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf18.md) _ZN8firebase4util22parcel_file_descriptor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4cf34",
      "incomplete_value": false,
      "site": "00b4cf38",
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
      "definition_site": "00b4cb0c",
      "incomplete_value": false,
      "site": "00b4cb10",
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
      "definition_site": "00b4cf44",
      "incomplete_value": true,
      "site": "00b4cf50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4cb1c",
      "incomplete_value": true,
      "site": "00b4cb28",
      "value": [
        "LOAD",
        "8",
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
      "00b4cf34",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4cf44",
      "DATA",
      [
        "storage",
        "01125880",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cf34",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4cf44",
      "DATA",
      [
        "storage",
        "01125c80",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4caf0.md#insn-00b4cb10) · [`00b4cb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4caf0.md#insn-00b4cb0c) · [`00b4cb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4caf0.md#insn-00b4cb18)
- 新版 `00b4cf38`（命令位置の公開資料なし） · `00b4cf34`（命令位置の公開資料なし） · `00b4cf40`（命令位置の公開資料なし）

~~~diff
- 00b4cb10 ["INT_ADD", "register:40f0:8", ["const:b4cb10:8", "const:4:8"]]
- 00b4cb10 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4cf38 ["INT_ADD", "register:40f0:8", ["const:b4cf38:8", "const:4:8"]]
+ 00b4cf38 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4cb10 bytes 3c380494
+ 00b4cf38 bytes 32380494
- 00b4cb0c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4cb0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cb0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cb0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cf34 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4cf34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cf34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cf34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cb0c bytes 00441191
+ 00b4cf34 bytes 00781491
- 00b4cb18 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00b4cb18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4cb18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4cb18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4cf40 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 00b4cf40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cf40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4cf40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4cb18 bytes 08012291
+ 00b4cf40 bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cbc72f2529b0db0bd1994047e5a982f"></a>

### [`00b4cb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb2c.md) → [`00b4cf54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf54.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b4cf80",
      "incomplete_value": true,
      "site": "00b4cf80",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb58",
      "incomplete_value": true,
      "site": "00b4cb58",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cf68",
      "incomplete_value": true,
      "site": "00b4cf68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb40",
      "incomplete_value": true,
      "site": "00b4cb40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cf74",
      "incomplete_value": false,
      "site": "00b4cf78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb4c",
      "incomplete_value": false,
      "site": "00b4cb50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "00b4cf64",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf74",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cf80",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cf64",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf74",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4cf80",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb2c.md#insn-00b4cb50) · [`00b4cb58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb2c.md#insn-00b4cb58) · [`00b4cb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb2c.md#insn-00b4cb3c)
- 新版 `00b4cf78`（命令位置の公開資料なし） · `00b4cf80`（命令位置の公開資料なし） · `00b4cf64`（命令位置の公開資料なし）

~~~diff
- 00b4cb50 ["INT_ADD", "register:40f0:8", ["const:b4cb50:8", "const:4:8"]]
- 00b4cb50 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cf78 ["INT_ADD", "register:40f0:8", ["const:b4cf78:8", "const:4:8"]]
+ 00b4cf78 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cb50 bytes f0370494
+ 00b4cf78 bytes e6370494
- 00b4cb58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cb58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cf80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4cf80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cb58 bytes 604604f9
+ 00b4cf80 bytes 604606f9
- 00b4cb3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cb3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cf64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4cf64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cb3c bytes 684644f9
+ 00b4cf64 bytes 684646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6bcb35f375ed67bc82e109b38b304cd"></a>

### [`00b4cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb6c.md) → [`00b4cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cf94.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4cfc0",
      "incomplete_value": true,
      "site": "00b4cfc0",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb98",
      "incomplete_value": true,
      "site": "00b4cb98",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cfa8",
      "incomplete_value": true,
      "site": "00b4cfa8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb80",
      "incomplete_value": true,
      "site": "00b4cb80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cfb0",
      "incomplete_value": false,
      "site": "00b4cfb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb88",
      "incomplete_value": false,
      "site": "00b4cb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "00b4cfa4",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cfb0",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4cfc0",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cfa4",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cfb0",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4cfc0",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb6c.md#insn-00b4cb90) · [`00b4cb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb6c.md#insn-00b4cb98) · [`00b4cb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cb6c.md#insn-00b4cb7c)
- 新版 `00b4cfb8`（命令位置の公開資料なし） · `00b4cfc0`（命令位置の公開資料なし） · `00b4cfa4`（命令位置の公開資料なし）

~~~diff
- 00b4cb90 ["INT_ADD", "register:40f0:8", ["const:b4cb90:8", "const:4:8"]]
- 00b4cb90 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cfb8 ["INT_ADD", "register:40f0:8", ["const:b4cfb8:8", "const:4:8"]]
+ 00b4cfb8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cb90 bytes e0370494
+ 00b4cfb8 bytes d6370494
- 00b4cb98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cb98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cfc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4cfc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cb98 bytes 604604f9
+ 00b4cfc0 bytes 604606f9
- 00b4cb7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cb7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cfa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4cfa4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cb7c bytes 684644f9
+ 00b4cfa4 bytes 684646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ac703cff9ce4615dbb6623314b8311"></a>

### [`00b4cbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbac.md) → [`00b4cfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4cfd4.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4d004",
      "incomplete_value": true,
      "site": "00b4d004",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cbdc",
      "incomplete_value": true,
      "site": "00b4cbdc",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cfe8",
      "incomplete_value": true,
      "site": "00b4cfe8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cbc0",
      "incomplete_value": true,
      "site": "00b4cbc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4cff4",
      "incomplete_value": false,
      "site": "00b4cffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cbcc",
      "incomplete_value": false,
      "site": "00b4cbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "00b4cfe4",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cff4",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4d004",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cfe4",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cff4",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d004",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cbd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbac.md#insn-00b4cbd4) · [`00b4cbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbac.md#insn-00b4cbdc) · [`00b4cbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbac.md#insn-00b4cbbc)
- 新版 `00b4cffc`（命令位置の公開資料なし） · `00b4d004`（命令位置の公開資料なし） · `00b4cfe4`（命令位置の公開資料なし）

~~~diff
- 00b4cbd4 ["INT_ADD", "register:40f0:8", ["const:b4cbd4:8", "const:4:8"]]
- 00b4cbd4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4cffc ["INT_ADD", "register:40f0:8", ["const:b4cffc:8", "const:4:8"]]
+ 00b4cffc ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cbd4 bytes cf370494
+ 00b4cffc bytes c5370494
- 00b4cbdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4d004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cbdc bytes 604604f9
+ 00b4d004 bytes 604606f9
- 00b4cbbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cbbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4cfe4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4cfe4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cbbc bytes 684644f9
+ 00b4cfe4 bytes 684646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4c3733a7e6b8850118fb4a9c7768e6f"></a>

### [`00b4cbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbf0.md) → [`00b4d018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d018.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d048",
      "incomplete_value": true,
      "site": "00b4d048",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc20",
      "incomplete_value": true,
      "site": "00b4cc20",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d02c",
      "incomplete_value": true,
      "site": "00b4d02c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc04",
      "incomplete_value": true,
      "site": "00b4cc04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d034",
      "incomplete_value": false,
      "site": "00b4d040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc0c",
      "incomplete_value": false,
      "site": "00b4cc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "00b4d028",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d034",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4d048",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d028",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d034",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d048",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbf0.md#insn-00b4cc18) · [`00b4cc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbf0.md#insn-00b4cc20) · [`00b4cc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cbf0.md#insn-00b4cc00)
- 新版 `00b4d040`（命令位置の公開資料なし） · `00b4d048`（命令位置の公開資料なし） · `00b4d028`（命令位置の公開資料なし）

~~~diff
- 00b4cc18 ["INT_ADD", "register:40f0:8", ["const:b4cc18:8", "const:4:8"]]
- 00b4cc18 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d040 ["INT_ADD", "register:40f0:8", ["const:b4d040:8", "const:4:8"]]
+ 00b4d040 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cc18 bytes be370494
+ 00b4d040 bytes b4370494
- 00b4cc20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cc20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d048 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4d048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cc20 bytes 604604f9
+ 00b4d048 bytes 604606f9
- 00b4cc00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
- 00b4cc00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d028 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c88:8"]]
+ 00b4d028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cc00 bytes 684644f9
+ 00b4d028 bytes 684646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-884f0a55427287e1c557937a1f615ed0"></a>

### [`00b4cc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cc40.md) → [`00b4d068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d068.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4d0f0",
      "incomplete_value": true,
      "site": "00b4d0f0",
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
    "old": {
      "definition_site": "00b4ccc8",
      "incomplete_value": true,
      "site": "00b4ccc8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d09c",
      "incomplete_value": true,
      "site": "00b4d0a8",
      "value": [
        "LOAD",
        "8",
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
                "const:c88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc74",
      "incomplete_value": true,
      "site": "00b4cc80",
      "value": [
        "LOAD",
        "8",
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
                "const:888:8"
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
      "00b4d07c",
      "READ",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d09c",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0f0",
      "WRITE",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d07c",
      "READ",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d09c",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0f0",
      "WRITE",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cc40.md#insn-00b4cc80) · [`00b4ccc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cc40.md#insn-00b4ccc8) · [`00b4cc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cc40.md#insn-00b4cc54)
- 新版 `00b4d0a8`（命令位置の公開資料なし） · `00b4d0f0`（命令位置の公開資料なし） · `00b4d07c`（命令位置の公開資料なし）

~~~diff
- 00b4cc80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4cc80 ["INT_ADD", "register:40f0:8", ["const:b4cc80:8", "const:4:8"]]
- 00b4cc80 ["CALLIND", null, ["register:0:8"]]
+ 00b4d0a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d0a8 ["INT_ADD", "register:40f0:8", ["const:b4d0a8:8", "const:4:8"]]
+ 00b4d0a8 ["CALLIND", null, ["register:0:8"]]
- 00b4cc80 bytes 00013fd6
+ 00b4d0a8 bytes 00013fd6
- 00b4ccc8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4ccc8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:890:8"]]
- 00b4ccc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d0f0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d0f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c90:8"]]
+ 00b4d0f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ccc8 bytes a0422239
+ 00b4d0f0 bytes a0423239
- 00b4cc54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:890:8"]]
- 00b4cc54 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4cc54 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d07c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c90:8"]]
+ 00b4d07c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d07c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4cc54 bytes a8426239
+ 00b4d07c bytes a8427239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9447406cce23c9a79765f0724a24e446"></a>

### [`00b4ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ccdc.md) → [`00b4d104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d104.md) _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4d140",
      "incomplete_value": true,
      "site": "00b4d140",
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
    "old": {
      "definition_site": "00b4cd18",
      "incomplete_value": true,
      "site": "00b4cd18",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4d190",
      "incomplete_value": true,
      "site": "00b4d190",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd68",
      "incomplete_value": true,
      "site": "00b4cd68",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d11c",
      "incomplete_value": true,
      "site": "00b4d11c",
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
      "definition_site": "00b4ccf4",
      "incomplete_value": true,
      "site": "00b4ccf4",
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
      "00b4d118",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d124",
      "READ",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d140",
      "WRITE",
      [
        "storage",
        "01125890",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d118",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d124",
      "READ",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d140",
      "WRITE",
      [
        "storage",
        "01125c90",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ccdc.md#insn-00b4cd18) · [`00b4cd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ccdc.md#insn-00b4cd64) · [`00b4cd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ccdc.md#insn-00b4cd68)
- 新版 `00b4d140`（命令位置の公開資料なし） · `00b4d18c`（命令位置の公開資料なし） · `00b4d190`（命令位置の公開資料なし）

~~~diff
- 00b4cd18 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4cd18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4cd18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
- 00b4cd18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d140 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d140 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d140 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c90:8"]]
+ 00b4d140 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4cd18 bytes bf422239
+ 00b4d140 bytes bf423239
- 00b4cd64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4cd64 ["INT_ADD", "register:40f0:8", ["const:b4cd64:8", "const:4:8"]]
- 00b4cd64 ["CALLIND", null, ["register:0:8"]]
+ 00b4d18c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d18c ["INT_ADD", "register:40f0:8", ["const:b4d18c:8", "const:4:8"]]
+ 00b4d18c ["CALLIND", null, ["register:0:8"]]
- 00b4cd64 bytes 00013fd6
+ 00b4d18c bytes 00013fd6
- 00b4cd68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b4cd68 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4cd68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d190 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00b4d190 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4cd68 bytes 9f4604f9
+ 00b4d190 bytes 9f4606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c33b73b2ce36da92ef200708fd55ee4"></a>

### [`00b4cd7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cd7c.md) → [`00b4d1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d1a4.md) _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d1e4",
      "incomplete_value": true,
      "site": "00b4d1e4",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cdbc",
      "incomplete_value": true,
      "site": "00b4cdbc",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d1c0",
      "incomplete_value": true,
      "site": "00b4d1c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd98",
      "incomplete_value": true,
      "site": "00b4cd98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d1c8",
      "incomplete_value": false,
      "site": "00b4d1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cda0",
      "incomplete_value": false,
      "site": "00b4cdb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "00b4d1b8",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1c8",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4d1e4",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d1b8",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1c8",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d1e4",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cd7c.md#insn-00b4cdb4) · [`00b4cdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cd7c.md#insn-00b4cdbc) · [`00b4cd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cd7c.md#insn-00b4cd90)
- 新版 `00b4d1dc`（命令位置の公開資料なし） · `00b4d1e4`（命令位置の公開資料なし） · `00b4d1b8`（命令位置の公開資料なし）

~~~diff
- 00b4cdb4 ["INT_ADD", "register:40f0:8", ["const:b4cdb4:8", "const:4:8"]]
- 00b4cdb4 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d1dc ["INT_ADD", "register:40f0:8", ["const:b4d1dc:8", "const:4:8"]]
+ 00b4d1dc ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cdb4 bytes 57370494
+ 00b4d1dc bytes 4d370494
- 00b4cdbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b4cdbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d1e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00b4d1e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cdbc bytes 804604f9
+ 00b4d1e4 bytes 804606f9
- 00b4cd90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b4cd90 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d1b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00b4d1b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cd90 bytes 814644f9
+ 00b4d1b8 bytes 814646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bdf2eda5c1af23abf0e83c675a0e20f"></a>

### [`00b4cdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cdec.md) → [`00b4d214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d214.md) _ZN8firebase4util3set11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b100.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b500.md) · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

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
      "definition_site": "00b4d230",
      "incomplete_value": false,
      "site": "00b4d234",
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
      "definition_site": "00b4ce08",
      "incomplete_value": false,
      "site": "00b4ce0c",
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
      "definition_site": "00b4d240",
      "incomplete_value": true,
      "site": "00b4d24c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4ce18",
      "incomplete_value": true,
      "site": "00b4ce24",
      "value": [
        "LOAD",
        "8",
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
      "00b4d230",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4d240",
      "DATA",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d230",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4d240",
      "DATA",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ce0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cdec.md#insn-00b4ce0c) · [`00b4ce08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cdec.md#insn-00b4ce08) · [`00b4ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cdec.md#insn-00b4ce14)
- 新版 `00b4d234`（命令位置の公開資料なし） · `00b4d230`（命令位置の公開資料なし） · `00b4d23c`（命令位置の公開資料なし）

~~~diff
- 00b4ce0c ["INT_ADD", "register:40f0:8", ["const:b4ce0c:8", "const:4:8"]]
- 00b4ce0c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4d234 ["INT_ADD", "register:40f0:8", ["const:b4d234:8", "const:4:8"]]
+ 00b4d234 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4ce0c bytes 7d370494
+ 00b4d234 bytes 73370494
- 00b4ce08 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4ce08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ce08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ce08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d230 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4d230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ce08 bytes 00680a91
+ 00b4d230 bytes 009c0d91
- 00b4ce14 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00b4ce14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ce14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ce14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d23c ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00b4d23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4ce14 bytes 08612291
+ 00b4d23c bytes 08613291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d170e697acf75fa8436b12ff1a26b6e"></a>

### [`00b4ce28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce28.md) → [`00b4d250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d250.md) _ZN8firebase4util3set13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d290",
      "incomplete_value": true,
      "site": "00b4d290",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ce68",
      "incomplete_value": true,
      "site": "00b4ce68",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d26c",
      "incomplete_value": true,
      "site": "00b4d26c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ce44",
      "incomplete_value": true,
      "site": "00b4ce44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d274",
      "incomplete_value": false,
      "site": "00b4d288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:587:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ce4c",
      "incomplete_value": false,
      "site": "00b4ce60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:547:8"
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
      "00b4d264",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d274",
      "PARAM",
      [
        "storage",
        "002b0547",
        null,
        "string"
      ]
    ],
    [
      "00b4d290",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d264",
      "READ",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d274",
      "PARAM",
      [
        "storage",
        "002b0587",
        null,
        "string"
      ]
    ],
    [
      "00b4d290",
      "WRITE",
      [
        "storage",
        "01125c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ce60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce28.md#insn-00b4ce60) · [`00b4ce68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce28.md#insn-00b4ce68) · [`00b4ce3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce28.md#insn-00b4ce3c)
- 新版 `00b4d288`（命令位置の公開資料なし） · `00b4d290`（命令位置の公開資料なし） · `00b4d264`（命令位置の公開資料なし）

~~~diff
- 00b4ce60 ["INT_ADD", "register:40f0:8", ["const:b4ce60:8", "const:4:8"]]
- 00b4ce60 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d288 ["INT_ADD", "register:40f0:8", ["const:b4d288:8", "const:4:8"]]
+ 00b4d288 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ce60 bytes 2c370494
+ 00b4d288 bytes 22370494
- 00b4ce68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b4ce68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d290 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00b4d290 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ce68 bytes 804604f9
+ 00b4d290 bytes 804606f9
- 00b4ce3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
- 00b4ce3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d264 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c88:8"]]
+ 00b4d264 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ce3c bytes 814644f9
+ 00b4d264 bytes 814646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb6310df0bf3b5d4617fb8d23707d1d7"></a>

### [`00b4ce98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce98.md) → [`00b4d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2c0.md) _ZN8firebase4util3set10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4d2dc",
      "incomplete_value": false,
      "site": "00b4d2e0",
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
      "definition_site": "00b4ceb4",
      "incomplete_value": false,
      "site": "00b4ceb8",
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
      "definition_site": "00b4d2ec",
      "incomplete_value": true,
      "site": "00b4d2f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4cec4",
      "incomplete_value": true,
      "site": "00b4ced0",
      "value": [
        "LOAD",
        "8",
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
      "00b4d2dc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4d2ec",
      "DATA",
      [
        "storage",
        "011258a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d2dc",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4d2ec",
      "DATA",
      [
        "storage",
        "01125ca0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ceb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce98.md#insn-00b4ceb8) · [`00b4ceb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce98.md#insn-00b4ceb4) · [`00b4cec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ce98.md#insn-00b4cec0)
- 新版 `00b4d2e0`（命令位置の公開資料なし） · `00b4d2dc`（命令位置の公開資料なし） · `00b4d2e8`（命令位置の公開資料なし）

~~~diff
- 00b4ceb8 ["INT_ADD", "register:40f0:8", ["const:b4ceb8:8", "const:4:8"]]
- 00b4ceb8 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4d2e0 ["INT_ADD", "register:40f0:8", ["const:b4d2e0:8", "const:4:8"]]
+ 00b4d2e0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4ceb8 bytes 52370494
+ 00b4d2e0 bytes 48370494
- 00b4ceb4 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4ceb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ceb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ceb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d2dc ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4d2dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d2dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d2dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ceb4 bytes 00441191
+ 00b4d2dc bytes 00781491
- 00b4cec0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00b4cec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4cec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4cec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d2e8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00b4d2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4cec0 bytes 08812291
+ 00b4d2e8 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e55546974cad74fff291e3b1300140b8"></a>

### [`00b4ced4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ced4.md) → [`00b4d2fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d2fc.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4d328",
      "incomplete_value": true,
      "site": "00b4d328",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf00",
      "incomplete_value": true,
      "site": "00b4cf00",
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
      "definition_site": "00b4d310",
      "incomplete_value": true,
      "site": "00b4d310",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cee8",
      "incomplete_value": true,
      "site": "00b4cee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d31c",
      "incomplete_value": false,
      "site": "00b4d320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cef4",
      "incomplete_value": false,
      "site": "00b4cef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00b4d30c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d31c",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d328",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d30c",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d31c",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d328",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ced4.md#insn-00b4cef8) · [`00b4cf00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ced4.md#insn-00b4cf00) · [`00b4cee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ced4.md#insn-00b4cee4)
- 新版 `00b4d320`（命令位置の公開資料なし） · `00b4d328`（命令位置の公開資料なし） · `00b4d30c`（命令位置の公開資料なし）

~~~diff
- 00b4cef8 ["INT_ADD", "register:40f0:8", ["const:b4cef8:8", "const:4:8"]]
- 00b4cef8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d320 ["INT_ADD", "register:40f0:8", ["const:b4d320:8", "const:4:8"]]
+ 00b4d320 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cef8 bytes 06370494
+ 00b4d320 bytes fc360494
- 00b4cf00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cf00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cf00 bytes 605604f9
+ 00b4d328 bytes 605606f9
- 00b4cee4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cee4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d30c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d30c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cee4 bytes 685644f9
+ 00b4d30c bytes 685646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b30d37f6e6562a2482dcd7fe0bfc5d6"></a>

### [`00b4cf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf14.md) → [`00b4d33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d33c.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4d368",
      "incomplete_value": true,
      "site": "00b4d368",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf40",
      "incomplete_value": true,
      "site": "00b4cf40",
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
      "definition_site": "00b4d350",
      "incomplete_value": true,
      "site": "00b4d350",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf28",
      "incomplete_value": true,
      "site": "00b4cf28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d358",
      "incomplete_value": false,
      "site": "00b4d360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf30",
      "incomplete_value": false,
      "site": "00b4cf38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00b4d34c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d358",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d368",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d34c",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d358",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d368",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf14.md#insn-00b4cf38) · [`00b4cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf14.md#insn-00b4cf40) · [`00b4cf24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf14.md#insn-00b4cf24)
- 新版 `00b4d360`（命令位置の公開資料なし） · `00b4d368`（命令位置の公開資料なし） · `00b4d34c`（命令位置の公開資料なし）

~~~diff
- 00b4cf38 ["INT_ADD", "register:40f0:8", ["const:b4cf38:8", "const:4:8"]]
- 00b4cf38 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d360 ["INT_ADD", "register:40f0:8", ["const:b4d360:8", "const:4:8"]]
+ 00b4d360 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cf38 bytes f6360494
+ 00b4d360 bytes ec360494
- 00b4cf40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cf40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d368 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cf40 bytes 605604f9
+ 00b4d368 bytes 605606f9
- 00b4cf24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cf24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d34c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d34c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cf24 bytes 685644f9
+ 00b4d34c bytes 685646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b16e8891baa06bcc6c1720670832d96"></a>

### [`00b4cf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf54.md) → [`00b4d37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d37c.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4d3ac",
      "incomplete_value": true,
      "site": "00b4d3ac",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf84",
      "incomplete_value": true,
      "site": "00b4cf84",
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
      "definition_site": "00b4d390",
      "incomplete_value": true,
      "site": "00b4d390",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf68",
      "incomplete_value": true,
      "site": "00b4cf68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d39c",
      "incomplete_value": false,
      "site": "00b4d3a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf74",
      "incomplete_value": false,
      "site": "00b4cf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00b4d38c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d39c",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d3ac",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d38c",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d39c",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d3ac",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf54.md#insn-00b4cf7c) · [`00b4cf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf54.md#insn-00b4cf84) · [`00b4cf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf54.md#insn-00b4cf64)
- 新版 `00b4d3a4`（命令位置の公開資料なし） · `00b4d3ac`（命令位置の公開資料なし） · `00b4d38c`（命令位置の公開資料なし）

~~~diff
- 00b4cf7c ["INT_ADD", "register:40f0:8", ["const:b4cf7c:8", "const:4:8"]]
- 00b4cf7c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d3a4 ["INT_ADD", "register:40f0:8", ["const:b4d3a4:8", "const:4:8"]]
+ 00b4d3a4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cf7c bytes e5360494
+ 00b4d3a4 bytes db360494
- 00b4cf84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d3ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d3ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cf84 bytes 605604f9
+ 00b4d3ac bytes 605606f9
- 00b4cf64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cf64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d38c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d38c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cf64 bytes 685644f9
+ 00b4d38c bytes 685646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5abbb3fef78f4f53e36a9e196f0f56a8"></a>

### [`00b4cf98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf98.md) → [`00b4d3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d3c0.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d3f0",
      "incomplete_value": true,
      "site": "00b4d3f0",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cfc8",
      "incomplete_value": true,
      "site": "00b4cfc8",
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
      "definition_site": "00b4d3d4",
      "incomplete_value": true,
      "site": "00b4d3d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cfac",
      "incomplete_value": true,
      "site": "00b4cfac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d3dc",
      "incomplete_value": false,
      "site": "00b4d3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cfb4",
      "incomplete_value": false,
      "site": "00b4cfc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00b4d3d0",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3dc",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d3f0",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d3d0",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3dc",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d3f0",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf98.md#insn-00b4cfc0) · [`00b4cfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf98.md#insn-00b4cfc8) · [`00b4cfa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cf98.md#insn-00b4cfa8)
- 新版 `00b4d3e8`（命令位置の公開資料なし） · `00b4d3f0`（命令位置の公開資料なし） · `00b4d3d0`（命令位置の公開資料なし）

~~~diff
- 00b4cfc0 ["INT_ADD", "register:40f0:8", ["const:b4cfc0:8", "const:4:8"]]
- 00b4cfc0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d3e8 ["INT_ADD", "register:40f0:8", ["const:b4d3e8:8", "const:4:8"]]
+ 00b4d3e8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4cfc0 bytes d4360494
+ 00b4d3e8 bytes ca360494
- 00b4cfc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cfc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d3f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d3f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cfc8 bytes 605604f9
+ 00b4d3f0 bytes 605606f9
- 00b4cfa8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4cfa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d3d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca8:8"]]
+ 00b4d3d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cfa8 bytes 685644f9
+ 00b4d3d0 bytes 685646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14247b2be59f53ba66e72214cf3b1a0"></a>

### [`00b4cfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cfe8.md) → [`00b4d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d410.md) _ZN8firebase4util11short_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4d498",
      "incomplete_value": true,
      "site": "00b4d498",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d070",
      "incomplete_value": true,
      "site": "00b4d070",
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
      "definition_site": "00b4d444",
      "incomplete_value": true,
      "site": "00b4d450",
      "value": [
        "LOAD",
        "8",
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d01c",
      "incomplete_value": true,
      "site": "00b4d028",
      "value": [
        "LOAD",
        "8",
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
      "00b4d424",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d444",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d498",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d424",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d444",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d498",
      "WRITE",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cfe8.md#insn-00b4d028) · [`00b4d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cfe8.md#insn-00b4d070) · [`00b4cffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cfe8.md#insn-00b4cffc)
- 新版 `00b4d450`（命令位置の公開資料なし） · `00b4d498`（命令位置の公開資料なし） · `00b4d424`（命令位置の公開資料なし）

~~~diff
- 00b4d028 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d028 ["INT_ADD", "register:40f0:8", ["const:b4d028:8", "const:4:8"]]
- 00b4d028 ["CALLIND", null, ["register:0:8"]]
+ 00b4d450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d450 ["INT_ADD", "register:40f0:8", ["const:b4d450:8", "const:4:8"]]
+ 00b4d450 ["CALLIND", null, ["register:0:8"]]
- 00b4d028 bytes 00013fd6
+ 00b4d450 bytes 00013fd6
- 00b4d070 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d070 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b0:8"]]
- 00b4d070 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d498 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d498 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cb0:8"]]
+ 00b4d498 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d070 bytes a0c22239
+ 00b4d498 bytes a0c23239
- 00b4cffc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8b0:8"]]
- 00b4cffc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4cffc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d424 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cb0:8"]]
+ 00b4d424 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d424 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4cffc bytes a8c26239
+ 00b4d424 bytes a8c27239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743573c00a0ad9b4bfe1d2f6626877e6"></a>

### [`00b4d084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d084.md) → [`00b4d4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d4ac.md) _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4d4e8",
      "incomplete_value": true,
      "site": "00b4d4e8",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d0c0",
      "incomplete_value": true,
      "site": "00b4d0c0",
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
      "definition_site": "00b4d538",
      "incomplete_value": true,
      "site": "00b4d538",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d110",
      "incomplete_value": true,
      "site": "00b4d110",
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
      "definition_site": "00b4d4c4",
      "incomplete_value": true,
      "site": "00b4d4c4",
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
      "definition_site": "00b4d09c",
      "incomplete_value": true,
      "site": "00b4d09c",
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
      "00b4d4c0",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d4cc",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d4e8",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d4c0",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d4cc",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d4e8",
      "WRITE",
      [
        "storage",
        "01125cb0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d084.md#insn-00b4d0c0) · [`00b4d10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d084.md#insn-00b4d10c) · [`00b4d110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d084.md#insn-00b4d110)
- 新版 `00b4d4e8`（命令位置の公開資料なし） · `00b4d534`（命令位置の公開資料なし） · `00b4d538`（命令位置の公開資料なし）

~~~diff
- 00b4d0c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4d0c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4d0c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
- 00b4d0c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d4e8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d4e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d4e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cb0:8"]]
+ 00b4d4e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4d0c0 bytes bfc22239
+ 00b4d4e8 bytes bfc23239
- 00b4d10c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d10c ["INT_ADD", "register:40f0:8", ["const:b4d10c:8", "const:4:8"]]
- 00b4d10c ["CALLIND", null, ["register:0:8"]]
+ 00b4d534 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d534 ["INT_ADD", "register:40f0:8", ["const:b4d534:8", "const:4:8"]]
+ 00b4d534 ["CALLIND", null, ["register:0:8"]]
- 00b4d10c bytes 00013fd6
+ 00b4d534 bytes 00013fd6
- 00b4d110 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4d110 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4d110 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d538 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00b4d538 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4d110 bytes 9f5604f9
+ 00b4d538 bytes 9f5606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-834a28366d132ea23d7e6a83b8334e33"></a>

### [`00b4d124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d124.md) → [`00b4d54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d54c.md) _ZN8firebase4util11short_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d58c",
      "incomplete_value": true,
      "site": "00b4d58c",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d164",
      "incomplete_value": true,
      "site": "00b4d164",
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
      "definition_site": "00b4d568",
      "incomplete_value": true,
      "site": "00b4d568",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d140",
      "incomplete_value": true,
      "site": "00b4d140",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d570",
      "incomplete_value": false,
      "site": "00b4d584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d148",
      "incomplete_value": false,
      "site": "00b4d15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00b4d560",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d570",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d58c",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d560",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d570",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d58c",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d124.md#insn-00b4d15c) · [`00b4d164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d124.md#insn-00b4d164) · [`00b4d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d124.md#insn-00b4d138)
- 新版 `00b4d584`（命令位置の公開資料なし） · `00b4d58c`（命令位置の公開資料なし） · `00b4d560`（命令位置の公開資料なし）

~~~diff
- 00b4d15c ["INT_ADD", "register:40f0:8", ["const:b4d15c:8", "const:4:8"]]
- 00b4d15c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d584 ["INT_ADD", "register:40f0:8", ["const:b4d584:8", "const:4:8"]]
+ 00b4d584 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d15c bytes 6d360494
+ 00b4d584 bytes 63360494
- 00b4d164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4d164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d58c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00b4d58c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d164 bytes 805604f9
+ 00b4d58c bytes 805606f9
- 00b4d138 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4d138 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d560 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00b4d560 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d138 bytes 815644f9
+ 00b4d560 bytes 815646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79d92923a7328b5f5fc1ac968c303efc"></a>

### [`00b4d194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d194.md) → [`00b4d5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5bc.md) _ZN8firebase4util11short_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4d5d8",
      "incomplete_value": false,
      "site": "00b4d5dc",
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
      "definition_site": "00b4d1b0",
      "incomplete_value": false,
      "site": "00b4d1b4",
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
      "definition_site": "00b4d5e8",
      "incomplete_value": true,
      "site": "00b4d5f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d1c0",
      "incomplete_value": true,
      "site": "00b4d1cc",
      "value": [
        "LOAD",
        "8",
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
      "00b4d5d8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4d5e8",
      "DATA",
      [
        "storage",
        "011258b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d5d8",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4d5e8",
      "DATA",
      [
        "storage",
        "01125cb8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d194.md#insn-00b4d1b4) · [`00b4d1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d194.md#insn-00b4d1b0) · [`00b4d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d194.md#insn-00b4d1bc)
- 新版 `00b4d5dc`（命令位置の公開資料なし） · `00b4d5d8`（命令位置の公開資料なし） · `00b4d5e4`（命令位置の公開資料なし）

~~~diff
- 00b4d1b4 ["INT_ADD", "register:40f0:8", ["const:b4d1b4:8", "const:4:8"]]
- 00b4d1b4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4d5dc ["INT_ADD", "register:40f0:8", ["const:b4d5dc:8", "const:4:8"]]
+ 00b4d5dc ["CALL", null, ["callee:00c5b000:8"]]
- 00b4d1b4 bytes 93360494
+ 00b4d5dc bytes 89360494
- 00b4d1b0 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4d1b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d1b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d1b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d5d8 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4d5d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d5d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d5d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d1b0 bytes 00680a91
+ 00b4d5d8 bytes 009c0d91
- 00b4d1bc ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 00b4d1bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d1bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d1bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d5e4 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00b4d5e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d5e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d5e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d1bc bytes 08e12291
+ 00b4d5e4 bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b308af30567ba7ef23e1593a10de59f8"></a>

### [`00b4d1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d1d0.md) → [`00b4d5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d5f8.md) _ZN8firebase4util11short_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d638",
      "incomplete_value": true,
      "site": "00b4d638",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d210",
      "incomplete_value": true,
      "site": "00b4d210",
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
      "definition_site": "00b4d614",
      "incomplete_value": true,
      "site": "00b4d614",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d1ec",
      "incomplete_value": true,
      "site": "00b4d1ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d61c",
      "incomplete_value": false,
      "site": "00b4d630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:81a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d1f4",
      "incomplete_value": false,
      "site": "00b4d208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:7da:8"
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
      "00b4d60c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d61c",
      "PARAM",
      [
        "storage",
        "002bf7da",
        null,
        "string"
      ]
    ],
    [
      "00b4d638",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d60c",
      "READ",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d61c",
      "PARAM",
      [
        "storage",
        "002bf81a",
        null,
        "string"
      ]
    ],
    [
      "00b4d638",
      "WRITE",
      [
        "storage",
        "01125ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d1d0.md#insn-00b4d208) · [`00b4d210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d1d0.md#insn-00b4d210) · [`00b4d1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d1d0.md#insn-00b4d1e4)
- 新版 `00b4d630`（命令位置の公開資料なし） · `00b4d638`（命令位置の公開資料なし） · `00b4d60c`（命令位置の公開資料なし）

~~~diff
- 00b4d208 ["INT_ADD", "register:40f0:8", ["const:b4d208:8", "const:4:8"]]
- 00b4d208 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d630 ["INT_ADD", "register:40f0:8", ["const:b4d630:8", "const:4:8"]]
+ 00b4d630 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d208 bytes 42360494
+ 00b4d630 bytes 38360494
- 00b4d210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4d210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d638 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00b4d638 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d210 bytes 805604f9
+ 00b4d638 bytes 805606f9
- 00b4d1e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4d1e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d60c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00b4d60c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d1e4 bytes 815644f9
+ 00b4d60c bytes 815646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-821d6a4c6cd5dfe7f530b2509db374e2"></a>

### [`00b4d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d240.md) → [`00b4d668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d668.md) _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4d684",
      "incomplete_value": false,
      "site": "00b4d688",
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
      "definition_site": "00b4d25c",
      "incomplete_value": false,
      "site": "00b4d260",
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
      "definition_site": "00b4d694",
      "incomplete_value": true,
      "site": "00b4d6a0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d26c",
      "incomplete_value": true,
      "site": "00b4d278",
      "value": [
        "LOAD",
        "8",
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
      "00b4d684",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4d694",
      "DATA",
      [
        "storage",
        "011258c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d684",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4d694",
      "DATA",
      [
        "storage",
        "01125cc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d240.md#insn-00b4d260) · [`00b4d25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d240.md#insn-00b4d25c) · [`00b4d268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d240.md#insn-00b4d268)
- 新版 `00b4d688`（命令位置の公開資料なし） · `00b4d684`（命令位置の公開資料なし） · `00b4d690`（命令位置の公開資料なし）

~~~diff
- 00b4d260 ["INT_ADD", "register:40f0:8", ["const:b4d260:8", "const:4:8"]]
- 00b4d260 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4d688 ["INT_ADD", "register:40f0:8", ["const:b4d688:8", "const:4:8"]]
+ 00b4d688 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4d260 bytes 68360494
+ 00b4d688 bytes 5e360494
- 00b4d25c ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4d25c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d25c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d25c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d684 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4d684 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d684 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d684 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d25c bytes 00441191
+ 00b4d684 bytes 00781491
- 00b4d268 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00b4d268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d690 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 00b4d690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d268 bytes 08212391
+ 00b4d690 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be510064af586a9c3d72a16f1138ebde"></a>

### [`00b4d27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d27c.md) → [`00b4d6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6a4.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00b4d6d0",
      "incomplete_value": true,
      "site": "00b4d6d0",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d2a8",
      "incomplete_value": true,
      "site": "00b4d2a8",
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
      "definition_site": "00b4d6b8",
      "incomplete_value": true,
      "site": "00b4d6b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d290",
      "incomplete_value": true,
      "site": "00b4d290",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d6c4",
      "incomplete_value": false,
      "site": "00b4d6c8",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d29c",
      "incomplete_value": false,
      "site": "00b4d2a0",
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
            "const:a60:8"
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
      "00b4d6b4",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6c4",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d6d0",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d6b4",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6c4",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d6d0",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d27c.md#insn-00b4d2a0) · [`00b4d2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d27c.md#insn-00b4d2a8) · [`00b4d28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d27c.md#insn-00b4d28c)
- 新版 `00b4d6c8`（命令位置の公開資料なし） · `00b4d6d0`（命令位置の公開資料なし） · `00b4d6b4`（命令位置の公開資料なし）

~~~diff
- 00b4d2a0 ["INT_ADD", "register:40f0:8", ["const:b4d2a0:8", "const:4:8"]]
- 00b4d2a0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d6c8 ["INT_ADD", "register:40f0:8", ["const:b4d6c8:8", "const:4:8"]]
+ 00b4d6c8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d2a0 bytes 1c360494
+ 00b4d6c8 bytes 12360494
- 00b4d2a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d2a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d6d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d6d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d2a8 bytes 606a04f9
+ 00b4d6d0 bytes 606a06f9
- 00b4d28c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d28c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d6b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d6b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d28c bytes 686a44f9
+ 00b4d6b4 bytes 686a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a6921e4699f5cef6917377c680fabb4"></a>

### [`00b4d2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2bc.md) → [`00b4d6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d6e4.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4d710",
      "incomplete_value": true,
      "site": "00b4d710",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d2e8",
      "incomplete_value": true,
      "site": "00b4d2e8",
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
      "definition_site": "00b4d6f8",
      "incomplete_value": true,
      "site": "00b4d6f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d2d0",
      "incomplete_value": true,
      "site": "00b4d2d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d700",
      "incomplete_value": false,
      "site": "00b4d708",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d2d8",
      "incomplete_value": false,
      "site": "00b4d2e0",
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
            "const:a60:8"
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
      "00b4d6f4",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d700",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d710",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d6f4",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d700",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d710",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2bc.md#insn-00b4d2e0) · [`00b4d2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2bc.md#insn-00b4d2e8) · [`00b4d2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2bc.md#insn-00b4d2cc)
- 新版 `00b4d708`（命令位置の公開資料なし） · `00b4d710`（命令位置の公開資料なし） · `00b4d6f4`（命令位置の公開資料なし）

~~~diff
- 00b4d2e0 ["INT_ADD", "register:40f0:8", ["const:b4d2e0:8", "const:4:8"]]
- 00b4d2e0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d708 ["INT_ADD", "register:40f0:8", ["const:b4d708:8", "const:4:8"]]
+ 00b4d708 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d2e0 bytes 0c360494
+ 00b4d708 bytes 02360494
- 00b4d2e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d2e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d710 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d2e8 bytes 606a04f9
+ 00b4d710 bytes 606a06f9
- 00b4d2cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d2cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d6f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d6f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d2cc bytes 686a44f9
+ 00b4d6f4 bytes 686a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e46e6d898fe6e8585b2a5d19cef4aa3"></a>

### [`00b4d2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2fc.md) → [`00b4d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d724.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4d754",
      "incomplete_value": true,
      "site": "00b4d754",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d32c",
      "incomplete_value": true,
      "site": "00b4d32c",
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
      "definition_site": "00b4d738",
      "incomplete_value": true,
      "site": "00b4d738",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d310",
      "incomplete_value": true,
      "site": "00b4d310",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d744",
      "incomplete_value": false,
      "site": "00b4d74c",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d31c",
      "incomplete_value": false,
      "site": "00b4d324",
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
            "const:a60:8"
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
      "00b4d734",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d744",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d754",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d734",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d744",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d754",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2fc.md#insn-00b4d324) · [`00b4d32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2fc.md#insn-00b4d32c) · [`00b4d30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d2fc.md#insn-00b4d30c)
- 新版 `00b4d74c`（命令位置の公開資料なし） · `00b4d754`（命令位置の公開資料なし） · `00b4d734`（命令位置の公開資料なし）

~~~diff
- 00b4d324 ["INT_ADD", "register:40f0:8", ["const:b4d324:8", "const:4:8"]]
- 00b4d324 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d74c ["INT_ADD", "register:40f0:8", ["const:b4d74c:8", "const:4:8"]]
+ 00b4d74c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d324 bytes fb350494
+ 00b4d74c bytes f1350494
- 00b4d32c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d32c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d754 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d754 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d32c bytes 606a04f9
+ 00b4d754 bytes 606a06f9
- 00b4d30c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d30c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d734 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d734 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d30c bytes 686a44f9
+ 00b4d734 bytes 686a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7dffdf70bfd58e4bb0d604db2d890cd"></a>

### [`00b4d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d340.md) → [`00b4d768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d768.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d798",
      "incomplete_value": true,
      "site": "00b4d798",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d370",
      "incomplete_value": true,
      "site": "00b4d370",
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
      "definition_site": "00b4d77c",
      "incomplete_value": true,
      "site": "00b4d77c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d354",
      "incomplete_value": true,
      "site": "00b4d354",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d784",
      "incomplete_value": false,
      "site": "00b4d790",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d35c",
      "incomplete_value": false,
      "site": "00b4d368",
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
            "const:a60:8"
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
      "00b4d778",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d784",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d798",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d778",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d784",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d798",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d340.md#insn-00b4d368) · [`00b4d370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d340.md#insn-00b4d370) · [`00b4d350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d340.md#insn-00b4d350)
- 新版 `00b4d790`（命令位置の公開資料なし） · `00b4d798`（命令位置の公開資料なし） · `00b4d778`（命令位置の公開資料なし）

~~~diff
- 00b4d368 ["INT_ADD", "register:40f0:8", ["const:b4d368:8", "const:4:8"]]
- 00b4d368 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d790 ["INT_ADD", "register:40f0:8", ["const:b4d790:8", "const:4:8"]]
+ 00b4d790 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d368 bytes ea350494
+ 00b4d790 bytes e0350494
- 00b4d370 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d798 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d370 bytes 606a04f9
+ 00b4d798 bytes 606a06f9
- 00b4d350 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d0:8"]]
- 00b4d350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d778 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d778 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d350 bytes 686a44f9
+ 00b4d778 bytes 686a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd7ecab77fe3f9046573d59b96ec32fe"></a>

### [`00b4d390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d390.md) → [`00b4d7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d7b8.md) _ZN8firebase4util6string15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4d840",
      "incomplete_value": true,
      "site": "00b4d840",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d418",
      "incomplete_value": true,
      "site": "00b4d418",
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
      "definition_site": "00b4d7ec",
      "incomplete_value": true,
      "site": "00b4d7f8",
      "value": [
        "LOAD",
        "8",
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d3c4",
      "incomplete_value": true,
      "site": "00b4d3d0",
      "value": [
        "LOAD",
        "8",
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
      "00b4d7cc",
      "READ",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d7ec",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d840",
      "WRITE",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d7cc",
      "READ",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d7ec",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d840",
      "WRITE",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d390.md#insn-00b4d3d0) · [`00b4d418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d390.md#insn-00b4d418) · [`00b4d3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d390.md#insn-00b4d3a4)
- 新版 `00b4d7f8`（命令位置の公開資料なし） · `00b4d840`（命令位置の公開資料なし） · `00b4d7cc`（命令位置の公開資料なし）

~~~diff
- 00b4d3d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d3d0 ["INT_ADD", "register:40f0:8", ["const:b4d3d0:8", "const:4:8"]]
- 00b4d3d0 ["CALLIND", null, ["register:0:8"]]
+ 00b4d7f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d7f8 ["INT_ADD", "register:40f0:8", ["const:b4d7f8:8", "const:4:8"]]
+ 00b4d7f8 ["CALLIND", null, ["register:0:8"]]
- 00b4d3d0 bytes 00013fd6
+ 00b4d7f8 bytes 00013fd6
- 00b4d418 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d418 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d8:8"]]
- 00b4d418 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d840 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d840 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cd8:8"]]
+ 00b4d840 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d418 bytes a0622339
+ 00b4d840 bytes a0623339
- 00b4d3a4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d8:8"]]
- 00b4d3a4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d3a4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d7cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cd8:8"]]
+ 00b4d7cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d7cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d3a4 bytes a8626339
+ 00b4d7cc bytes a8627339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04237fdaf4b3a85ec11cff9b77c6b8b9"></a>

### [`00b4d42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d42c.md) → [`00b4d854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d854.md) _ZN8firebase4util6string12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4d890",
      "incomplete_value": true,
      "site": "00b4d890",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d468",
      "incomplete_value": true,
      "site": "00b4d468",
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
      "definition_site": "00b4d8e0",
      "incomplete_value": true,
      "site": "00b4d8e0",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d4b8",
      "incomplete_value": true,
      "site": "00b4d4b8",
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
      "definition_site": "00b4d86c",
      "incomplete_value": true,
      "site": "00b4d86c",
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
      "definition_site": "00b4d444",
      "incomplete_value": true,
      "site": "00b4d444",
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
      "00b4d868",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d874",
      "READ",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d890",
      "WRITE",
      [
        "storage",
        "011258d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d868",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d874",
      "READ",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d890",
      "WRITE",
      [
        "storage",
        "01125cd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d42c.md#insn-00b4d468) · [`00b4d4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d42c.md#insn-00b4d4b4) · [`00b4d4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d42c.md#insn-00b4d4b8)
- 新版 `00b4d890`（命令位置の公開資料なし） · `00b4d8dc`（命令位置の公開資料なし） · `00b4d8e0`（命令位置の公開資料なし）

~~~diff
- 00b4d468 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4d468 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4d468 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d8:8"]]
- 00b4d468 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d890 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d890 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d890 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cd8:8"]]
+ 00b4d890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4d468 bytes bf622339
+ 00b4d890 bytes bf623339
- 00b4d4b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d4b4 ["INT_ADD", "register:40f0:8", ["const:b4d4b4:8", "const:4:8"]]
- 00b4d4b4 ["CALLIND", null, ["register:0:8"]]
+ 00b4d8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d8dc ["INT_ADD", "register:40f0:8", ["const:b4d8dc:8", "const:4:8"]]
+ 00b4d8dc ["CALLIND", null, ["register:0:8"]]
- 00b4d4b4 bytes 00013fd6
+ 00b4d8dc bytes 00013fd6
- 00b4d4b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b4d4b8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4d4b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d8e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d8e0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d8e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4d4b8 bytes 9f6a04f9
+ 00b4d8e0 bytes 9f6a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d03357bb3d0ca853356debbc73afd2db"></a>

### [`00b4d4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d4cc.md) → [`00b4d8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d8f4.md) _ZN8firebase4util6string14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d934",
      "incomplete_value": true,
      "site": "00b4d934",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d50c",
      "incomplete_value": true,
      "site": "00b4d50c",
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
      "definition_site": "00b4d910",
      "incomplete_value": true,
      "site": "00b4d910",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d4e8",
      "incomplete_value": true,
      "site": "00b4d4e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d918",
      "incomplete_value": false,
      "site": "00b4d92c",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d4f0",
      "incomplete_value": false,
      "site": "00b4d504",
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
            "const:a60:8"
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
      "00b4d908",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d918",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d934",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d908",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d918",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d934",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d4cc.md#insn-00b4d504) · [`00b4d50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d4cc.md#insn-00b4d50c) · [`00b4d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d4cc.md#insn-00b4d4e0)
- 新版 `00b4d92c`（命令位置の公開資料なし） · `00b4d934`（命令位置の公開資料なし） · `00b4d908`（命令位置の公開資料なし）

~~~diff
- 00b4d504 ["INT_ADD", "register:40f0:8", ["const:b4d504:8", "const:4:8"]]
- 00b4d504 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d92c ["INT_ADD", "register:40f0:8", ["const:b4d92c:8", "const:4:8"]]
+ 00b4d92c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d504 bytes 83350494
+ 00b4d92c bytes 79350494
- 00b4d50c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b4d50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d934 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d50c bytes 806a04f9
+ 00b4d934 bytes 806a06f9
- 00b4d4e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b4d4e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d908 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d908 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d4e0 bytes 816a44f9
+ 00b4d908 bytes 816a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5219eb7dee4a069b299bd98bc97cd81c"></a>

### [`00b4d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d53c.md) → [`00b4d964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d964.md) _ZN8firebase4util6string11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4d980",
      "incomplete_value": false,
      "site": "00b4d984",
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
      "definition_site": "00b4d558",
      "incomplete_value": false,
      "site": "00b4d55c",
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
      "definition_site": "00b4d990",
      "incomplete_value": true,
      "site": "00b4d99c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d568",
      "incomplete_value": true,
      "site": "00b4d574",
      "value": [
        "LOAD",
        "8",
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
      "00b4d980",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4d990",
      "DATA",
      [
        "storage",
        "011258e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d980",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4d990",
      "DATA",
      [
        "storage",
        "01125ce0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d53c.md#insn-00b4d55c) · [`00b4d558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d53c.md#insn-00b4d558) · [`00b4d564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d53c.md#insn-00b4d564)
- 新版 `00b4d984`（命令位置の公開資料なし） · `00b4d980`（命令位置の公開資料なし） · `00b4d98c`（命令位置の公開資料なし）

~~~diff
- 00b4d55c ["INT_ADD", "register:40f0:8", ["const:b4d55c:8", "const:4:8"]]
- 00b4d55c ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4d984 ["INT_ADD", "register:40f0:8", ["const:b4d984:8", "const:4:8"]]
+ 00b4d984 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4d55c bytes a9350494
+ 00b4d984 bytes 9f350494
- 00b4d558 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4d558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d980 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4d980 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d980 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d980 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d558 bytes 00680a91
+ 00b4d980 bytes 009c0d91
- 00b4d564 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00b4d564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4d98c ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00b4d98c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d98c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4d98c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d564 bytes 08812391
+ 00b4d98c bytes 08813391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f24c1aca16204e899bf952b89e01f90"></a>

### [`00b4d578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d578.md) → [`00b4d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4d9a0.md) _ZN8firebase4util6string13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d9e0",
      "incomplete_value": true,
      "site": "00b4d9e0",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d5b8",
      "incomplete_value": true,
      "site": "00b4d5b8",
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
      "definition_site": "00b4d9bc",
      "incomplete_value": true,
      "site": "00b4d9bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d594",
      "incomplete_value": true,
      "site": "00b4d594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4d9c4",
      "incomplete_value": false,
      "site": "00b4d9d8",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d59c",
      "incomplete_value": false,
      "site": "00b4d5b0",
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
            "const:a60:8"
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
      "00b4d9b4",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d9c4",
      "PARAM",
      [
        "storage",
        "002aea60",
        null,
        "string"
      ]
    ],
    [
      "00b4d9e0",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d9b4",
      "READ",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d9c4",
      "PARAM",
      [
        "storage",
        "002aeaa0",
        null,
        "string"
      ]
    ],
    [
      "00b4d9e0",
      "WRITE",
      [
        "storage",
        "01125cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d578.md#insn-00b4d5b0) · [`00b4d5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d578.md#insn-00b4d5b8) · [`00b4d58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d578.md#insn-00b4d58c)
- 新版 `00b4d9d8`（命令位置の公開資料なし） · `00b4d9e0`（命令位置の公開資料なし） · `00b4d9b4`（命令位置の公開資料なし）

~~~diff
- 00b4d5b0 ["INT_ADD", "register:40f0:8", ["const:b4d5b0:8", "const:4:8"]]
- 00b4d5b0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4d9d8 ["INT_ADD", "register:40f0:8", ["const:b4d9d8:8", "const:4:8"]]
+ 00b4d9d8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d5b0 bytes 58350494
+ 00b4d9d8 bytes 4e350494
- 00b4d5b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b4d5b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d9e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d9e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d5b8 bytes 806a04f9
+ 00b4d9e0 bytes 806a06f9
- 00b4d58c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d0:8"]]
- 00b4d58c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d9b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d9b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d58c bytes 816a44f9
+ 00b4d9b4 bytes 816a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-987c95a495222784f533c24a4ea49b60"></a>

### [`00b4d5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d5e8.md) → [`00b4da10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da10.md) _ZN8firebase4util6string10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4da2c",
      "incomplete_value": false,
      "site": "00b4da30",
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
      "definition_site": "00b4d604",
      "incomplete_value": false,
      "site": "00b4d608",
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
      "definition_site": "00b4da3c",
      "incomplete_value": true,
      "site": "00b4da48",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d614",
      "incomplete_value": true,
      "site": "00b4d620",
      "value": [
        "LOAD",
        "8",
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
      "00b4da2c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4da3c",
      "DATA",
      [
        "storage",
        "011258e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4da2c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4da3c",
      "DATA",
      [
        "storage",
        "01125ce8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d5e8.md#insn-00b4d608) · [`00b4d604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d5e8.md#insn-00b4d604) · [`00b4d610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d5e8.md#insn-00b4d610)
- 新版 `00b4da30`（命令位置の公開資料なし） · `00b4da2c`（命令位置の公開資料なし） · `00b4da38`（命令位置の公開資料なし）

~~~diff
- 00b4d608 ["INT_ADD", "register:40f0:8", ["const:b4d608:8", "const:4:8"]]
- 00b4d608 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4da30 ["INT_ADD", "register:40f0:8", ["const:b4da30:8", "const:4:8"]]
+ 00b4da30 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4d608 bytes 7e350494
+ 00b4da30 bytes 74350494
- 00b4d604 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4d604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4da2c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4da2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4da2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4da2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d604 bytes 00441191
+ 00b4da2c bytes 00781491
- 00b4d610 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00b4d610 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d610 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d610 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4da38 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00b4da38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4da38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4da38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d610 bytes 08a12391
+ 00b4da38 bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e085ccb08a00e49327e79a32e97a0e5f"></a>

### [`00b4d624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d624.md) → [`00b4da4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da4c.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

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
      "definition_site": "00b4da78",
      "incomplete_value": true,
      "site": "00b4da78",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d650",
      "incomplete_value": true,
      "site": "00b4d650",
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
            "const:8f0:8"
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
      "definition_site": "00b4da60",
      "incomplete_value": true,
      "site": "00b4da60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d638",
      "incomplete_value": true,
      "site": "00b4d638",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4da6c",
      "incomplete_value": false,
      "site": "00b4da70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:9ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d644",
      "incomplete_value": false,
      "site": "00b4d648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:96d:8"
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
      "00b4da5c",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da6c",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4da78",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4da5c",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da6c",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4da78",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d624.md#insn-00b4d648) · [`00b4d650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d624.md#insn-00b4d650) · [`00b4d634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d624.md#insn-00b4d634)
- 新版 `00b4da70`（命令位置の公開資料なし） · `00b4da78`（命令位置の公開資料なし） · `00b4da5c`（命令位置の公開資料なし）

~~~diff
- 00b4d648 ["INT_ADD", "register:40f0:8", ["const:b4d648:8", "const:4:8"]]
- 00b4d648 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4da70 ["INT_ADD", "register:40f0:8", ["const:b4da70:8", "const:4:8"]]
+ 00b4da70 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d648 bytes 32350494
+ 00b4da70 bytes 28350494
- 00b4d650 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4da78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4da78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d650 bytes 607a04f9
+ 00b4da78 bytes 607a06f9
- 00b4d634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4da5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4da5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d634 bytes 687a44f9
+ 00b4da5c bytes 687a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a73ebbc00479ffaf7f02425b1361100e"></a>

### [`00b4d664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d664.md) → [`00b4da8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4da8c.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4dab8",
      "incomplete_value": true,
      "site": "00b4dab8",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d690",
      "incomplete_value": true,
      "site": "00b4d690",
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
            "const:8f0:8"
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
      "definition_site": "00b4daa0",
      "incomplete_value": true,
      "site": "00b4daa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d678",
      "incomplete_value": true,
      "site": "00b4d678",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4daa8",
      "incomplete_value": false,
      "site": "00b4dab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:9ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d680",
      "incomplete_value": false,
      "site": "00b4d688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:96d:8"
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
      "00b4da9c",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4daa8",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4dab8",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4da9c",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4daa8",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4dab8",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d664.md#insn-00b4d688) · [`00b4d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d664.md#insn-00b4d690) · [`00b4d674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d664.md#insn-00b4d674)
- 新版 `00b4dab0`（命令位置の公開資料なし） · `00b4dab8`（命令位置の公開資料なし） · `00b4da9c`（命令位置の公開資料なし）

~~~diff
- 00b4d688 ["INT_ADD", "register:40f0:8", ["const:b4d688:8", "const:4:8"]]
- 00b4d688 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4dab0 ["INT_ADD", "register:40f0:8", ["const:b4dab0:8", "const:4:8"]]
+ 00b4dab0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d688 bytes 22350494
+ 00b4dab0 bytes 18350494
- 00b4d690 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dab8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4dab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d690 bytes 607a04f9
+ 00b4dab8 bytes 607a06f9
- 00b4d674 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d674 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4da9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4da9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d674 bytes 687a44f9
+ 00b4da9c bytes 687a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42440bac0ec50d13ef2e965605269c9a"></a>

### [`00b4d6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6a4.md) → [`00b4dacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dacc.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4dafc",
      "incomplete_value": true,
      "site": "00b4dafc",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d6d4",
      "incomplete_value": true,
      "site": "00b4d6d4",
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
            "const:8f0:8"
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
      "definition_site": "00b4dae0",
      "incomplete_value": true,
      "site": "00b4dae0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d6b8",
      "incomplete_value": true,
      "site": "00b4d6b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4daec",
      "incomplete_value": false,
      "site": "00b4daf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:9ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d6c4",
      "incomplete_value": false,
      "site": "00b4d6cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:96d:8"
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
      "00b4dadc",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4daec",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4dafc",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dadc",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4daec",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4dafc",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6a4.md#insn-00b4d6cc) · [`00b4d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6a4.md#insn-00b4d6d4) · [`00b4d6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6a4.md#insn-00b4d6b4)
- 新版 `00b4daf4`（命令位置の公開資料なし） · `00b4dafc`（命令位置の公開資料なし） · `00b4dadc`（命令位置の公開資料なし）

~~~diff
- 00b4d6cc ["INT_ADD", "register:40f0:8", ["const:b4d6cc:8", "const:4:8"]]
- 00b4d6cc ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4daf4 ["INT_ADD", "register:40f0:8", ["const:b4daf4:8", "const:4:8"]]
+ 00b4daf4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d6cc bytes 11350494
+ 00b4daf4 bytes 07350494
- 00b4d6d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d6d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dafc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4dafc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d6d4 bytes 607a04f9
+ 00b4dafc bytes 607a06f9
- 00b4d6b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d6b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dadc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4dadc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d6b4 bytes 687a44f9
+ 00b4dadc bytes 687a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c52450aae0787a43e4984059f9261da9"></a>

### [`00b4d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6e8.md) → [`00b4db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db10.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4db40",
      "incomplete_value": true,
      "site": "00b4db40",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d718",
      "incomplete_value": true,
      "site": "00b4d718",
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
            "const:8f0:8"
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
      "definition_site": "00b4db24",
      "incomplete_value": true,
      "site": "00b4db24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d6fc",
      "incomplete_value": true,
      "site": "00b4d6fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4db2c",
      "incomplete_value": false,
      "site": "00b4db38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:9ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d704",
      "incomplete_value": false,
      "site": "00b4d710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:96d:8"
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
      "00b4db20",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db2c",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4db40",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4db20",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db2c",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4db40",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6e8.md#insn-00b4d710) · [`00b4d718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6e8.md#insn-00b4d718) · [`00b4d6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d6e8.md#insn-00b4d6f8)
- 新版 `00b4db38`（命令位置の公開資料なし） · `00b4db40`（命令位置の公開資料なし） · `00b4db20`（命令位置の公開資料なし）

~~~diff
- 00b4d710 ["INT_ADD", "register:40f0:8", ["const:b4d710:8", "const:4:8"]]
- 00b4d710 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4db38 ["INT_ADD", "register:40f0:8", ["const:b4db38:8", "const:4:8"]]
+ 00b4db38 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d710 bytes 00350494
+ 00b4db38 bytes f6340494
- 00b4d718 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4db40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4db40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d718 bytes 607a04f9
+ 00b4db40 bytes 607a06f9
- 00b4d6f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
- 00b4d6f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4db20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf0:8"]]
+ 00b4db20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d6f8 bytes 687a44f9
+ 00b4db20 bytes 687a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2898030eeb8ec33851c733aaeef8a1b2"></a>

### [`00b4d738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d738.md) → [`00b4db60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4db60.md) _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4dbe8",
      "incomplete_value": true,
      "site": "00b4dbe8",
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
    "old": {
      "definition_site": "00b4d7c0",
      "incomplete_value": true,
      "site": "00b4d7c0",
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
            "const:8f8:8"
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
      "definition_site": "00b4db94",
      "incomplete_value": true,
      "site": "00b4dba0",
      "value": [
        "LOAD",
        "8",
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d76c",
      "incomplete_value": true,
      "site": "00b4d778",
      "value": [
        "LOAD",
        "8",
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
                "const:8f0:8"
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
      "00b4db74",
      "READ",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4db94",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dbe8",
      "WRITE",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4db74",
      "READ",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4db94",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dbe8",
      "WRITE",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d738.md#insn-00b4d778) · [`00b4d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d738.md#insn-00b4d7c0) · [`00b4d74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d738.md#insn-00b4d74c)
- 新版 `00b4dba0`（命令位置の公開資料なし） · `00b4dbe8`（命令位置の公開資料なし） · `00b4db74`（命令位置の公開資料なし）

~~~diff
- 00b4d778 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d778 ["INT_ADD", "register:40f0:8", ["const:b4d778:8", "const:4:8"]]
- 00b4d778 ["CALLIND", null, ["register:0:8"]]
+ 00b4dba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dba0 ["INT_ADD", "register:40f0:8", ["const:b4dba0:8", "const:4:8"]]
+ 00b4dba0 ["CALLIND", null, ["register:0:8"]]
- 00b4d778 bytes 00013fd6
+ 00b4dba0 bytes 00013fd6
- 00b4d7c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d7c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f8:8"]]
- 00b4d7c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4dbe8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4dbe8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cf8:8"]]
+ 00b4dbe8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d7c0 bytes a0e22339
+ 00b4dbe8 bytes a0e23339
- 00b4d74c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f8:8"]]
- 00b4d74c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d74c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4db74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:cf8:8"]]
+ 00b4db74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4db74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d74c bytes a8e26339
+ 00b4db74 bytes a8e27339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc46992222a99f331d9ec53ebdbae5f0"></a>

### [`00b4d7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d7d4.md) → [`00b4dbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dbfc.md) _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4dc38",
      "incomplete_value": true,
      "site": "00b4dc38",
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
    "old": {
      "definition_site": "00b4d810",
      "incomplete_value": true,
      "site": "00b4d810",
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
            "const:8f8:8"
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
      "definition_site": "00b4dc88",
      "incomplete_value": true,
      "site": "00b4dc88",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d860",
      "incomplete_value": true,
      "site": "00b4d860",
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
            "const:8f0:8"
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
      "definition_site": "00b4dc14",
      "incomplete_value": true,
      "site": "00b4dc14",
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
      "definition_site": "00b4d7ec",
      "incomplete_value": true,
      "site": "00b4d7ec",
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
      "00b4dc10",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc1c",
      "READ",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dc38",
      "WRITE",
      [
        "storage",
        "011258f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4dc10",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc1c",
      "READ",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dc38",
      "WRITE",
      [
        "storage",
        "01125cf8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d7d4.md#insn-00b4d810) · [`00b4d85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d7d4.md#insn-00b4d85c) · [`00b4d860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d7d4.md#insn-00b4d860)
- 新版 `00b4dc38`（命令位置の公開資料なし） · `00b4dc84`（命令位置の公開資料なし） · `00b4dc88`（命令位置の公開資料なし）

~~~diff
- 00b4d810 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4d810 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4d810 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f8:8"]]
- 00b4d810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4dc38 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4dc38 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4dc38 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cf8:8"]]
+ 00b4dc38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4d810 bytes bfe22339
+ 00b4dc38 bytes bfe23339
- 00b4d85c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d85c ["INT_ADD", "register:40f0:8", ["const:b4d85c:8", "const:4:8"]]
- 00b4d85c ["CALLIND", null, ["register:0:8"]]
+ 00b4dc84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dc84 ["INT_ADD", "register:40f0:8", ["const:b4dc84:8", "const:4:8"]]
+ 00b4dc84 ["CALLIND", null, ["register:0:8"]]
- 00b4d85c bytes 00013fd6
+ 00b4dc84 bytes 00013fd6
- 00b4d860 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00b4d860 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4d860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4dc88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00b4dc88 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4dc88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4d860 bytes 9f7a04f9
+ 00b4dc88 bytes 9f7a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c6e70c6b0efd6431f2f40a344ccff9a"></a>

### [`00b4d874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d874.md) → [`00b4dc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dc9c.md) _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4dcdc",
      "incomplete_value": true,
      "site": "00b4dcdc",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d8b4",
      "incomplete_value": true,
      "site": "00b4d8b4",
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
            "const:8f0:8"
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
      "definition_site": "00b4dcb8",
      "incomplete_value": true,
      "site": "00b4dcb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d890",
      "incomplete_value": true,
      "site": "00b4d890",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4dcc0",
      "incomplete_value": false,
      "site": "00b4dcd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:9ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d898",
      "incomplete_value": false,
      "site": "00b4d8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:96d:8"
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
      "00b4dcb0",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcc0",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4dcdc",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dcb0",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcc0",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4dcdc",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d874.md#insn-00b4d8ac) · [`00b4d8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d874.md#insn-00b4d8b4) · [`00b4d888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d874.md#insn-00b4d888)
- 新版 `00b4dcd4`（命令位置の公開資料なし） · `00b4dcdc`（命令位置の公開資料なし） · `00b4dcb0`（命令位置の公開資料なし）

~~~diff
- 00b4d8ac ["INT_ADD", "register:40f0:8", ["const:b4d8ac:8", "const:4:8"]]
- 00b4d8ac ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4dcd4 ["INT_ADD", "register:40f0:8", ["const:b4dcd4:8", "const:4:8"]]
+ 00b4dcd4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d8ac bytes 99340494
+ 00b4dcd4 bytes 8f340494
- 00b4d8b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00b4d8b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dcdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00b4dcdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d8b4 bytes 807a04f9
+ 00b4dcdc bytes 807a06f9
- 00b4d888 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00b4d888 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dcb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00b4dcb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d888 bytes 817a44f9
+ 00b4dcb0 bytes 817a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce8a95d109074fbb00a710e891df70e"></a>

### [`00b4d8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d8e4.md) → [`00b4dd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd0c.md) _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4dd28",
      "incomplete_value": false,
      "site": "00b4dd2c",
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
      "definition_site": "00b4d900",
      "incomplete_value": false,
      "site": "00b4d904",
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
      "definition_site": "00b4dd38",
      "incomplete_value": true,
      "site": "00b4dd44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d910",
      "incomplete_value": true,
      "site": "00b4d91c",
      "value": [
        "LOAD",
        "8",
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
      "00b4dd28",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4dd38",
      "DATA",
      [
        "storage",
        "01125900",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd28",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4dd38",
      "DATA",
      [
        "storage",
        "01125d00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d8e4.md#insn-00b4d904) · [`00b4d900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d8e4.md#insn-00b4d900) · [`00b4d90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d8e4.md#insn-00b4d90c)
- 新版 `00b4dd2c`（命令位置の公開資料なし） · `00b4dd28`（命令位置の公開資料なし） · `00b4dd34`（命令位置の公開資料なし）

~~~diff
- 00b4d904 ["INT_ADD", "register:40f0:8", ["const:b4d904:8", "const:4:8"]]
- 00b4d904 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4dd2c ["INT_ADD", "register:40f0:8", ["const:b4dd2c:8", "const:4:8"]]
+ 00b4dd2c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4d904 bytes bf340494
+ 00b4dd2c bytes b5340494
- 00b4d900 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4d900 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d900 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d900 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4dd28 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4dd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d900 bytes 00680a91
+ 00b4dd28 bytes 009c0d91
- 00b4d90c ["COPY", "tmp:0:8", ["const:900:8"]]
- 00b4d90c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d90c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d90c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4dd34 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00b4dd34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4dd34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4dd34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d90c bytes 08012491
+ 00b4dd34 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-656eb3c6f210f1efe3894c54d2462543"></a>

### [`00b4d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d920.md) → [`00b4dd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dd48.md) _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4dd88",
      "incomplete_value": true,
      "site": "00b4dd88",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d960",
      "incomplete_value": true,
      "site": "00b4d960",
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
            "const:8f0:8"
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
      "definition_site": "00b4dd64",
      "incomplete_value": true,
      "site": "00b4dd64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d93c",
      "incomplete_value": true,
      "site": "00b4d93c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4dd6c",
      "incomplete_value": false,
      "site": "00b4dd80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:9ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d944",
      "incomplete_value": false,
      "site": "00b4d958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:96d:8"
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
      "00b4dd5c",
      "READ",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd6c",
      "PARAM",
      [
        "storage",
        "002b996d",
        null,
        "string"
      ]
    ],
    [
      "00b4dd88",
      "WRITE",
      [
        "storage",
        "011258f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd5c",
      "READ",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd6c",
      "PARAM",
      [
        "storage",
        "002b99ad",
        null,
        "string"
      ]
    ],
    [
      "00b4dd88",
      "WRITE",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d920.md#insn-00b4d958) · [`00b4d960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d920.md#insn-00b4d960) · [`00b4d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d920.md#insn-00b4d934)
- 新版 `00b4dd80`（命令位置の公開資料なし） · `00b4dd88`（命令位置の公開資料なし） · `00b4dd5c`（命令位置の公開資料なし）

~~~diff
- 00b4d958 ["INT_ADD", "register:40f0:8", ["const:b4d958:8", "const:4:8"]]
- 00b4d958 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4dd80 ["INT_ADD", "register:40f0:8", ["const:b4dd80:8", "const:4:8"]]
+ 00b4dd80 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d958 bytes 6e340494
+ 00b4dd80 bytes 64340494
- 00b4d960 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00b4d960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dd88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00b4dd88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d960 bytes 807a04f9
+ 00b4dd88 bytes 807a06f9
- 00b4d934 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00b4d934 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dd5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00b4dd5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d934 bytes 817a44f9
+ 00b4dd5c bytes 817a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-136b169b65e1cc5149e50902cd36ef57"></a>

### [`00b4d990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d990.md) → [`00b4ddb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddb8.md) _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4ddd4",
      "incomplete_value": false,
      "site": "00b4ddd8",
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
      "definition_site": "00b4d9ac",
      "incomplete_value": false,
      "site": "00b4d9b0",
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
      "definition_site": "00b4dde4",
      "incomplete_value": true,
      "site": "00b4ddf0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4d9bc",
      "incomplete_value": true,
      "site": "00b4d9c8",
      "value": [
        "LOAD",
        "8",
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
      "00b4ddd4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4dde4",
      "DATA",
      [
        "storage",
        "01125918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ddd4",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4dde4",
      "DATA",
      [
        "storage",
        "01125d18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d990.md#insn-00b4d9b0) · [`00b4d9ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d990.md#insn-00b4d9ac) · [`00b4d9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d990.md#insn-00b4d9b8)
- 新版 `00b4ddd8`（命令位置の公開資料なし） · `00b4ddd4`（命令位置の公開資料なし） · `00b4dde0`（命令位置の公開資料なし）

~~~diff
- 00b4d9b0 ["INT_ADD", "register:40f0:8", ["const:b4d9b0:8", "const:4:8"]]
- 00b4d9b0 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4ddd8 ["INT_ADD", "register:40f0:8", ["const:b4ddd8:8", "const:4:8"]]
+ 00b4ddd8 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4d9b0 bytes 94340494
+ 00b4ddd8 bytes 8a340494
- 00b4d9ac ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4d9ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d9ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4d9ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ddd4 ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4ddd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ddd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ddd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4d9ac bytes 00441191
+ 00b4ddd4 bytes 00781491
- 00b4d9b8 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00b4d9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4d9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4dde0 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00b4dde0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4dde0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4dde0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4d9b8 bytes 08612491
+ 00b4dde0 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac13c422762529f3ed0f34521f06febc"></a>

### [`00b4d9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d9cc.md) → [`00b4ddf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4ddf4.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b4de20",
      "incomplete_value": true,
      "site": "00b4de20",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d9f8",
      "incomplete_value": true,
      "site": "00b4d9f8",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4de08",
      "incomplete_value": true,
      "site": "00b4de08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d9e0",
      "incomplete_value": true,
      "site": "00b4d9e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4de14",
      "incomplete_value": false,
      "site": "00b4de18",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d9ec",
      "incomplete_value": false,
      "site": "00b4d9f0",
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
            "const:99:8"
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
      "00b4de04",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de14",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4de20",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4de04",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de14",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4de20",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d9cc.md#insn-00b4d9f0) · [`00b4d9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d9cc.md#insn-00b4d9f8) · [`00b4d9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4d9cc.md#insn-00b4d9dc)
- 新版 `00b4de18`（命令位置の公開資料なし） · `00b4de20`（命令位置の公開資料なし） · `00b4de04`（命令位置の公開資料なし）

~~~diff
- 00b4d9f0 ["INT_ADD", "register:40f0:8", ["const:b4d9f0:8", "const:4:8"]]
- 00b4d9f0 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4de18 ["INT_ADD", "register:40f0:8", ["const:b4de18:8", "const:4:8"]]
+ 00b4de18 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4d9f0 bytes 48340494
+ 00b4de18 bytes 3e340494
- 00b4d9f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4d9f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4de20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4de20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d9f8 bytes 609204f9
+ 00b4de20 bytes 609206f9
- 00b4d9dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4d9dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4de04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4de04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d9dc bytes 689244f9
+ 00b4de04 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4fd4422c3bdbe524ad52b92c71a79d7"></a>

### [`00b4da0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da0c.md) → [`00b4de34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de34.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4de60",
      "incomplete_value": true,
      "site": "00b4de60",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da38",
      "incomplete_value": true,
      "site": "00b4da38",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4de48",
      "incomplete_value": true,
      "site": "00b4de48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da20",
      "incomplete_value": true,
      "site": "00b4da20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4de50",
      "incomplete_value": false,
      "site": "00b4de58",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da28",
      "incomplete_value": false,
      "site": "00b4da30",
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
            "const:99:8"
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
      "00b4de44",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de50",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4de60",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4de44",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de50",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4de60",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4da30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da0c.md#insn-00b4da30) · [`00b4da38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da0c.md#insn-00b4da38) · [`00b4da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da0c.md#insn-00b4da1c)
- 新版 `00b4de58`（命令位置の公開資料なし） · `00b4de60`（命令位置の公開資料なし） · `00b4de44`（命令位置の公開資料なし）

~~~diff
- 00b4da30 ["INT_ADD", "register:40f0:8", ["const:b4da30:8", "const:4:8"]]
- 00b4da30 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4de58 ["INT_ADD", "register:40f0:8", ["const:b4de58:8", "const:4:8"]]
+ 00b4de58 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4da30 bytes 38340494
+ 00b4de58 bytes 2e340494
- 00b4da38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4da38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4de60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4de60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4da38 bytes 609204f9
+ 00b4de60 bytes 609206f9
- 00b4da1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4da1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4de44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4de44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4da1c bytes 689244f9
+ 00b4de44 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc120d7226e9df092ca00ea04d19bbd"></a>

### [`00b4da4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da4c.md) → [`00b4de74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4de74.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4dea4",
      "incomplete_value": true,
      "site": "00b4dea4",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da7c",
      "incomplete_value": true,
      "site": "00b4da7c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4de88",
      "incomplete_value": true,
      "site": "00b4de88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da60",
      "incomplete_value": true,
      "site": "00b4da60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4de94",
      "incomplete_value": false,
      "site": "00b4de9c",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4da6c",
      "incomplete_value": false,
      "site": "00b4da74",
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
            "const:99:8"
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
      "00b4de84",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de94",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4dea4",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4de84",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de94",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4dea4",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4da74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da4c.md#insn-00b4da74) · [`00b4da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da4c.md#insn-00b4da7c) · [`00b4da5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da4c.md#insn-00b4da5c)
- 新版 `00b4de9c`（命令位置の公開資料なし） · `00b4dea4`（命令位置の公開資料なし） · `00b4de84`（命令位置の公開資料なし）

~~~diff
- 00b4da74 ["INT_ADD", "register:40f0:8", ["const:b4da74:8", "const:4:8"]]
- 00b4da74 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4de9c ["INT_ADD", "register:40f0:8", ["const:b4de9c:8", "const:4:8"]]
+ 00b4de9c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4da74 bytes 27340494
+ 00b4de9c bytes 1d340494
- 00b4da7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4da7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dea4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4dea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4da7c bytes 609204f9
+ 00b4dea4 bytes 609206f9
- 00b4da5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4da5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4de84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4de84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4da5c bytes 689244f9
+ 00b4de84 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc4bb30ce99f80f8ba8702c04eb7eb9"></a>

### [`00b4da90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da90.md) → [`00b4deb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4deb8.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4dee8",
      "incomplete_value": true,
      "site": "00b4dee8",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dac0",
      "incomplete_value": true,
      "site": "00b4dac0",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4decc",
      "incomplete_value": true,
      "site": "00b4decc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4daa4",
      "incomplete_value": true,
      "site": "00b4daa4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4ded4",
      "incomplete_value": false,
      "site": "00b4dee0",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4daac",
      "incomplete_value": false,
      "site": "00b4dab8",
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
            "const:99:8"
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
      "00b4dec8",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ded4",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4dee8",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dec8",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ded4",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4dee8",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da90.md#insn-00b4dab8) · [`00b4dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da90.md#insn-00b4dac0) · [`00b4daa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4da90.md#insn-00b4daa0)
- 新版 `00b4dee0`（命令位置の公開資料なし） · `00b4dee8`（命令位置の公開資料なし） · `00b4dec8`（命令位置の公開資料なし）

~~~diff
- 00b4dab8 ["INT_ADD", "register:40f0:8", ["const:b4dab8:8", "const:4:8"]]
- 00b4dab8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4dee0 ["INT_ADD", "register:40f0:8", ["const:b4dee0:8", "const:4:8"]]
+ 00b4dee0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4dab8 bytes 16340494
+ 00b4dee0 bytes 0c340494
- 00b4dac0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4dac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4dee8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dac0 bytes 609204f9
+ 00b4dee8 bytes 609206f9
- 00b4daa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00b4daa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dec8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d20:8"]]
+ 00b4dec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4daa0 bytes 689244f9
+ 00b4dec8 bytes 689246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c167b7961d0ff0b12a83e6a630280a20"></a>

### [`00b4dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dae0.md) → [`00b4df08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4df08.md) _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4df90",
      "incomplete_value": true,
      "site": "00b4df90",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4db68",
      "incomplete_value": true,
      "site": "00b4db68",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4df3c",
      "incomplete_value": true,
      "site": "00b4df48",
      "value": [
        "LOAD",
        "8",
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4db14",
      "incomplete_value": true,
      "site": "00b4db20",
      "value": [
        "LOAD",
        "8",
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
                "const:920:8"
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
      "00b4df1c",
      "READ",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4df3c",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df90",
      "WRITE",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4df1c",
      "READ",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4df3c",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df90",
      "WRITE",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4db20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dae0.md#insn-00b4db20) · [`00b4db68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dae0.md#insn-00b4db68) · [`00b4daf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dae0.md#insn-00b4daf4)
- 新版 `00b4df48`（命令位置の公開資料なし） · `00b4df90`（命令位置の公開資料なし） · `00b4df1c`（命令位置の公開資料なし）

~~~diff
- 00b4db20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4db20 ["INT_ADD", "register:40f0:8", ["const:b4db20:8", "const:4:8"]]
- 00b4db20 ["CALLIND", null, ["register:0:8"]]
+ 00b4df48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4df48 ["INT_ADD", "register:40f0:8", ["const:b4df48:8", "const:4:8"]]
+ 00b4df48 ["CALLIND", null, ["register:0:8"]]
- 00b4db20 bytes 00013fd6
+ 00b4df48 bytes 00013fd6
- 00b4db68 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4db68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
- 00b4db68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4df90 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4df90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d28:8"]]
+ 00b4df90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4db68 bytes a0a22439
+ 00b4df90 bytes a0a23439
- 00b4daf4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:928:8"]]
- 00b4daf4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4daf4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4df1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
+ 00b4df1c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4df1c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4daf4 bytes a8a26439
+ 00b4df1c bytes a8a27439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19b57520b0e8ebbc8d628e1665e1cd8"></a>

### [`00b4db7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4db7c.md) → [`00b4dfa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4d/00b4dfa4.md) _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4dfe0",
      "incomplete_value": true,
      "site": "00b4dfe0",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dbb8",
      "incomplete_value": true,
      "site": "00b4dbb8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4e030",
      "incomplete_value": true,
      "site": "00b4e030",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dc08",
      "incomplete_value": true,
      "site": "00b4dc08",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dfbc",
      "incomplete_value": true,
      "site": "00b4dfbc",
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
      "definition_site": "00b4db94",
      "incomplete_value": true,
      "site": "00b4db94",
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
      "00b4dfb8",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dfc4",
      "READ",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dfe0",
      "WRITE",
      [
        "storage",
        "01125928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4dfb8",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dfc4",
      "READ",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dfe0",
      "WRITE",
      [
        "storage",
        "01125d28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dbb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4db7c.md#insn-00b4dbb8) · [`00b4dc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4db7c.md#insn-00b4dc04) · [`00b4dc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4db7c.md#insn-00b4dc08)
- 新版 `00b4dfe0`（命令位置の公開資料なし） · `00b4e02c`（命令位置の公開資料なし） · `00b4e030`（命令位置の公開資料なし）

~~~diff
- 00b4dbb8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4dbb8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4dbb8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
- 00b4dbb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4dfe0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4dfe0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4dfe0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d28:8"]]
+ 00b4dfe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4dbb8 bytes bfa22439
+ 00b4dfe0 bytes bfa23439
- 00b4dc04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4dc04 ["INT_ADD", "register:40f0:8", ["const:b4dc04:8", "const:4:8"]]
- 00b4dc04 ["CALLIND", null, ["register:0:8"]]
+ 00b4e02c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4e02c ["INT_ADD", "register:40f0:8", ["const:b4e02c:8", "const:4:8"]]
+ 00b4e02c ["CALLIND", null, ["register:0:8"]]
- 00b4dc04 bytes 00013fd6
+ 00b4e02c bytes 00013fd6
- 00b4dc08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b4dc08 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4dc08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4e030 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00b4e030 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4e030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4dc08 bytes 9f9204f9
+ 00b4e030 bytes 9f9206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5591e82565d4b4db3a8d1bc192caf77b"></a>

### [`00b4dc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc1c.md) → [`00b4e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e044.md) _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4e084",
      "incomplete_value": true,
      "site": "00b4e084",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dc5c",
      "incomplete_value": true,
      "site": "00b4dc5c",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e060",
      "incomplete_value": true,
      "site": "00b4e060",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dc38",
      "incomplete_value": true,
      "site": "00b4dc38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4e068",
      "incomplete_value": false,
      "site": "00b4e07c",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dc40",
      "incomplete_value": false,
      "site": "00b4dc54",
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
            "const:99:8"
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
      "00b4e058",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e068",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4e084",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e058",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e068",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4e084",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc1c.md#insn-00b4dc54) · [`00b4dc5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc1c.md#insn-00b4dc5c) · [`00b4dc30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc1c.md#insn-00b4dc30)
- 新版 `00b4e07c`（命令位置の公開資料なし） · `00b4e084`（命令位置の公開資料なし） · `00b4e058`（命令位置の公開資料なし）

~~~diff
- 00b4dc54 ["INT_ADD", "register:40f0:8", ["const:b4dc54:8", "const:4:8"]]
- 00b4dc54 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e07c ["INT_ADD", "register:40f0:8", ["const:b4e07c:8", "const:4:8"]]
+ 00b4e07c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4dc54 bytes af330494
+ 00b4e07c bytes a5330494
- 00b4dc5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b4dc5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e084 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00b4e084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dc5c bytes 809204f9
+ 00b4e084 bytes 809206f9
- 00b4dc30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b4dc30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e058 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00b4e058 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dc30 bytes 819244f9
+ 00b4e058 bytes 819246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d9929e1b9d123129275e9a9e1aeced"></a>

### [`00b4dc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc8c.md) → [`00b4e0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0b4.md) _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4e0d0",
      "incomplete_value": false,
      "site": "00b4e0d4",
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
      "definition_site": "00b4dca8",
      "incomplete_value": false,
      "site": "00b4dcac",
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
      "definition_site": "00b4e0e0",
      "incomplete_value": true,
      "site": "00b4e0ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4dcb8",
      "incomplete_value": true,
      "site": "00b4dcc4",
      "value": [
        "LOAD",
        "8",
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
      "00b4e0d0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4e0e0",
      "DATA",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e0d0",
      "PARAM",
      [
        "storage",
        "002a8367",
        null,
        "string"
      ]
    ],
    [
      "00b4e0e0",
      "DATA",
      [
        "storage",
        "01125d30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dcac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc8c.md#insn-00b4dcac) · [`00b4dca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc8c.md#insn-00b4dca8) · [`00b4dcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dc8c.md#insn-00b4dcb4)
- 新版 `00b4e0d4`（命令位置の公開資料なし） · `00b4e0d0`（命令位置の公開資料なし） · `00b4e0dc`（命令位置の公開資料なし）

~~~diff
- 00b4dcac ["INT_ADD", "register:40f0:8", ["const:b4dcac:8", "const:4:8"]]
- 00b4dcac ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4e0d4 ["INT_ADD", "register:40f0:8", ["const:b4e0d4:8", "const:4:8"]]
+ 00b4e0d4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4dcac bytes d5330494
+ 00b4e0d4 bytes cb330494
- 00b4dca8 ["COPY", "tmp:0:8", ["const:29a:8"]]
- 00b4dca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4dca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4dca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4e0d0 ["COPY", "tmp:0:8", ["const:367:8"]]
+ 00b4e0d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e0d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e0d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4dca8 bytes 00680a91
+ 00b4e0d0 bytes 009c0d91
- 00b4dcb4 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00b4dcb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dcb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dcb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4e0dc ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00b4e0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4dcb4 bytes 08c12491
+ 00b4e0dc bytes 08c13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85dd8ae55dcc4d520ff911ab2819dc48"></a>

### [`00b4dcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dcc8.md) → [`00b4e0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e0f0.md) _ZN8firebase4util3uri13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4e130",
      "incomplete_value": true,
      "site": "00b4e130",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd08",
      "incomplete_value": true,
      "site": "00b4dd08",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e10c",
      "incomplete_value": true,
      "site": "00b4e10c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dce4",
      "incomplete_value": true,
      "site": "00b4dce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4e114",
      "incomplete_value": false,
      "site": "00b4e128",
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
            "const:175:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dcec",
      "incomplete_value": false,
      "site": "00b4dd00",
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
            "const:99:8"
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
      "00b4e104",
      "READ",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e114",
      "PARAM",
      [
        "storage",
        "002a7099",
        null,
        "string"
      ]
    ],
    [
      "00b4e130",
      "WRITE",
      [
        "storage",
        "01125920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e104",
      "READ",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e114",
      "PARAM",
      [
        "storage",
        "002a7175",
        null,
        "string"
      ]
    ],
    [
      "00b4e130",
      "WRITE",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dcc8.md#insn-00b4dd00) · [`00b4dd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dcc8.md#insn-00b4dd08) · [`00b4dcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dcc8.md#insn-00b4dcdc)
- 新版 `00b4e128`（命令位置の公開資料なし） · `00b4e130`（命令位置の公開資料なし） · `00b4e104`（命令位置の公開資料なし）

~~~diff
- 00b4dd00 ["INT_ADD", "register:40f0:8", ["const:b4dd00:8", "const:4:8"]]
- 00b4dd00 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e128 ["INT_ADD", "register:40f0:8", ["const:b4e128:8", "const:4:8"]]
+ 00b4e128 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4dd00 bytes 84330494
+ 00b4e128 bytes 7a330494
- 00b4dd08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b4dd08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e130 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00b4e130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dd08 bytes 809204f9
+ 00b4e130 bytes 809206f9
- 00b4dcdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00b4dcdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e104 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00b4e104 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dcdc bytes 819244f9
+ 00b4e104 bytes 819246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eb6219590eb599b772a857e80736468"></a>

### [`00b4dd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd38.md) → [`00b4e160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e160.md) _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4e17c",
      "incomplete_value": false,
      "site": "00b4e180",
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
      "definition_site": "00b4dd54",
      "incomplete_value": false,
      "site": "00b4dd58",
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
      "definition_site": "00b4e18c",
      "incomplete_value": true,
      "site": "00b4e198",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b4dd64",
      "incomplete_value": true,
      "site": "00b4dd70",
      "value": [
        "LOAD",
        "8",
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
      "00b4e17c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4e18c",
      "DATA",
      [
        "storage",
        "01125940",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4e17c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b4e18c",
      "DATA",
      [
        "storage",
        "01125d40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd38.md#insn-00b4dd58) · [`00b4dd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd38.md#insn-00b4dd54) · [`00b4dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd38.md#insn-00b4dd60)
- 新版 `00b4e180`（命令位置の公開資料なし） · `00b4e17c`（命令位置の公開資料なし） · `00b4e188`（命令位置の公開資料なし）

~~~diff
- 00b4dd58 ["INT_ADD", "register:40f0:8", ["const:b4dd58:8", "const:4:8"]]
- 00b4dd58 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b4e180 ["INT_ADD", "register:40f0:8", ["const:b4e180:8", "const:4:8"]]
+ 00b4e180 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4dd58 bytes aa330494
+ 00b4e180 bytes a0330494
- 00b4dd54 ["COPY", "tmp:0:8", ["const:451:8"]]
- 00b4dd54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4dd54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4dd54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4e17c ["COPY", "tmp:0:8", ["const:51e:8"]]
+ 00b4e17c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e17c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4e17c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4dd54 bytes 00441191
+ 00b4e17c bytes 00781491
- 00b4dd60 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00b4dd60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dd60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4dd60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4e188 ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 00b4e188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4e188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4dd60 bytes 08012591
+ 00b4e188 bytes 08013591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3577143c160f40f6414838b70e43fe1a"></a>

### [`00b4dd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd74.md) → [`00b4e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e19c.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00b4e1c8",
      "incomplete_value": true,
      "site": "00b4e1c8",
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
    "old": {
      "definition_site": "00b4dda0",
      "incomplete_value": true,
      "site": "00b4dda0",
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
            "const:948:8"
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
      "definition_site": "00b4e1b0",
      "incomplete_value": true,
      "site": "00b4e1b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd88",
      "incomplete_value": true,
      "site": "00b4dd88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4e1bc",
      "incomplete_value": false,
      "site": "00b4e1c0",
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
            "const:151:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd94",
      "incomplete_value": false,
      "site": "00b4dd98",
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
            "const:111:8"
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
      "00b4e1ac",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e1bc",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4e1c8",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e1ac",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e1bc",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e1c8",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd74.md#insn-00b4dd98) · [`00b4dda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd74.md#insn-00b4dda0) · [`00b4dd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dd74.md#insn-00b4dd84)
- 新版 `00b4e1c0`（命令位置の公開資料なし） · `00b4e1c8`（命令位置の公開資料なし） · `00b4e1ac`（命令位置の公開資料なし）

~~~diff
- 00b4dd98 ["INT_ADD", "register:40f0:8", ["const:b4dd98:8", "const:4:8"]]
- 00b4dd98 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e1c0 ["INT_ADD", "register:40f0:8", ["const:b4e1c0:8", "const:4:8"]]
+ 00b4e1c0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4dd98 bytes 5e330494
+ 00b4e1c0 bytes 54330494
- 00b4dda0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4dda0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e1c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e1c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dda0 bytes 60a604f9
+ 00b4e1c8 bytes 60a606f9
- 00b4dd84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4dd84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e1ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e1ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dd84 bytes 68a644f9
+ 00b4e1ac bytes 68a646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5541e5e759c39ebba30ad813a22160a5"></a>

### [`00b4ddb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddb4.md) → [`00b4e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e1dc.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4e208",
      "incomplete_value": true,
      "site": "00b4e208",
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
    "old": {
      "definition_site": "00b4dde0",
      "incomplete_value": true,
      "site": "00b4dde0",
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
            "const:948:8"
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
      "definition_site": "00b4e1f0",
      "incomplete_value": true,
      "site": "00b4e1f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ddc8",
      "incomplete_value": true,
      "site": "00b4ddc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4e1f8",
      "incomplete_value": false,
      "site": "00b4e200",
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
            "const:151:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ddd0",
      "incomplete_value": false,
      "site": "00b4ddd8",
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
            "const:111:8"
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
      "00b4e1ec",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e1f8",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4e208",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e1ec",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e1f8",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e208",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ddd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddb4.md#insn-00b4ddd8) · [`00b4dde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddb4.md#insn-00b4dde0) · [`00b4ddc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddb4.md#insn-00b4ddc4)
- 新版 `00b4e200`（命令位置の公開資料なし） · `00b4e208`（命令位置の公開資料なし） · `00b4e1ec`（命令位置の公開資料なし）

~~~diff
- 00b4ddd8 ["INT_ADD", "register:40f0:8", ["const:b4ddd8:8", "const:4:8"]]
- 00b4ddd8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e200 ["INT_ADD", "register:40f0:8", ["const:b4e200:8", "const:4:8"]]
+ 00b4e200 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4ddd8 bytes 4e330494
+ 00b4e200 bytes 44330494
- 00b4dde0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4dde0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4dde0 bytes 60a604f9
+ 00b4e208 bytes 60a606f9
- 00b4ddc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4ddc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e1ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e1ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ddc4 bytes 68a644f9
+ 00b4e1ec bytes 68a646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea64f70266f1cbebce521b1b052ca2a2"></a>

### [`00b4ddf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddf4.md) → [`00b4e21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e21c.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4e24c",
      "incomplete_value": true,
      "site": "00b4e24c",
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
    "old": {
      "definition_site": "00b4de24",
      "incomplete_value": true,
      "site": "00b4de24",
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
            "const:948:8"
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
      "definition_site": "00b4e230",
      "incomplete_value": true,
      "site": "00b4e230",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de08",
      "incomplete_value": true,
      "site": "00b4de08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4e23c",
      "incomplete_value": false,
      "site": "00b4e244",
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
            "const:151:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de14",
      "incomplete_value": false,
      "site": "00b4de1c",
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
            "const:111:8"
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
      "00b4e22c",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e23c",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4e24c",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e22c",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e23c",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e24c",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4de1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddf4.md#insn-00b4de1c) · [`00b4de24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddf4.md#insn-00b4de24) · [`00b4de04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4ddf4.md#insn-00b4de04)
- 新版 `00b4e244`（命令位置の公開資料なし） · `00b4e24c`（命令位置の公開資料なし） · `00b4e22c`（命令位置の公開資料なし）

~~~diff
- 00b4de1c ["INT_ADD", "register:40f0:8", ["const:b4de1c:8", "const:4:8"]]
- 00b4de1c ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e244 ["INT_ADD", "register:40f0:8", ["const:b4e244:8", "const:4:8"]]
+ 00b4e244 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4de1c bytes 3d330494
+ 00b4e244 bytes 33330494
- 00b4de24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4de24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e24c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e24c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4de24 bytes 60a604f9
+ 00b4e24c bytes 60a606f9
- 00b4de04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4de04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e22c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e22c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4de04 bytes 68a644f9
+ 00b4e22c bytes 68a646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944bc621f65fcc059a420031b64fae8a"></a>

### [`00b4de38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de38.md) → [`00b4e260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e260.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4e290",
      "incomplete_value": true,
      "site": "00b4e290",
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
    "old": {
      "definition_site": "00b4de68",
      "incomplete_value": true,
      "site": "00b4de68",
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
            "const:948:8"
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
      "definition_site": "00b4e274",
      "incomplete_value": true,
      "site": "00b4e274",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de4c",
      "incomplete_value": true,
      "site": "00b4de4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4e27c",
      "incomplete_value": false,
      "site": "00b4e288",
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
            "const:151:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de54",
      "incomplete_value": false,
      "site": "00b4de60",
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
            "const:111:8"
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
      "00b4e270",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e27c",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ],
    [
      "00b4e290",
      "WRITE",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e270",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e27c",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ],
    [
      "00b4e290",
      "WRITE",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4de60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de38.md#insn-00b4de60) · [`00b4de68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de38.md#insn-00b4de68) · [`00b4de48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de38.md#insn-00b4de48)
- 新版 `00b4e288`（命令位置の公開資料なし） · `00b4e290`（命令位置の公開資料なし） · `00b4e270`（命令位置の公開資料なし）

~~~diff
- 00b4de60 ["INT_ADD", "register:40f0:8", ["const:b4de60:8", "const:4:8"]]
- 00b4de60 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e288 ["INT_ADD", "register:40f0:8", ["const:b4e288:8", "const:4:8"]]
+ 00b4e288 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4de60 bytes 2c330494
+ 00b4e288 bytes 22330494
- 00b4de68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4de68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e290 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4de68 bytes 60a604f9
+ 00b4e290 bytes 60a606f9
- 00b4de48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:948:8"]]
- 00b4de48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e270 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4de48 bytes 68a644f9
+ 00b4e270 bytes 68a646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e2445edf811bf7c125139bc721323ce"></a>

### [`00b4de88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de88.md) → [`00b4e2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e2b0.md) _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4df10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4e338"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e2e4",
      "incomplete_value": true,
      "site": "00b4e2f0",
      "value": [
        "LOAD",
        "8",
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4debc",
      "incomplete_value": true,
      "site": "00b4dec8",
      "value": [
        "LOAD",
        "8",
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
                "const:948:8"
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
      "00b4e2c4",
      "READ",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e2d0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4df14"
      ]
    ],
    [
      "00b4e2e4",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e2c4",
      "READ",
      [
        "storage",
        "01125d50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e2d0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e33c"
      ]
    ],
    [
      "00b4e2e4",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de88.md#insn-00b4dec8) · [`00b4df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de88.md#insn-00b4df10) · [`00b4df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4de88.md#insn-00b4df20)
- 新版 `00b4e2f0`（命令位置の公開資料なし）

~~~diff
- 00b4dec8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4dec8 ["INT_ADD", "register:40f0:8", ["const:b4dec8:8", "const:4:8"]]
- 00b4dec8 ["CALLIND", null, ["register:0:8"]]
+ 00b4e2f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4e2f0 ["INT_ADD", "register:40f0:8", ["const:b4e2f0:8", "const:4:8"]]
+ 00b4e2f0 ["CALLIND", null, ["register:0:8"]]
- 00b4dec8 bytes 00013fd6
+ 00b4e2f0 bytes 00013fd6
- 00b4df10 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4df10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:950:8"]]
- 00b4df10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4df10 bytes a0422539
- 00b4df20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4df20 ["RETURN", null, ["register:0:8"]]
- 00b4df20 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ffe7c4e20a329417ae6214a802924d4"></a>

### [`00b4df24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4df24.md) → [`00b4e34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e34c.md) _ZN8firebase4util6object12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

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
      "site": "00b4df60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4e3d8",
      "incomplete_value": true,
      "site": "00b4e3d8",
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
    "old": {
      "definition_site": "00b4dfb0",
      "incomplete_value": true,
      "site": "00b4dfb0",
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
            "const:948:8"
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
      "site": "00b4e388"
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
      "00b4e360",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4df44",
      "READ",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4df60",
      "WRITE",
      [
        "storage",
        "01125950",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4e360",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e36c",
      "READ",
      [
        "storage",
        "01125d50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e388",
      "WRITE",
      [
        "storage",
        "01125d50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4df3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4df24.md#insn-00b4df3c) · [`00b4df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4df24.md#insn-00b4df60) · [`00b4df98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4df24.md#insn-00b4df98)
- 新版 `00b4e364`（命令位置の公開資料なし）

~~~diff
- 00b4df3c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4df3c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b4e364 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4e364 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b4df3c bytes c10300b4
+ 00b4e364 bytes c10300b4
- 00b4df60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4df60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4df60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:950:8"]]
- 00b4df60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4df60 bytes bf422539
- 00b4df98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4df98 ["INT_ADD", "register:40f0:8", ["const:b4df98:8", "const:4:8"]]
- 00b4df98 ["CALLIND", null, ["register:0:8"]]
- 00b4df98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e700bde4793562524e013be250e868b"></a>

### [`00b4dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dfc4.md) → [`00b4e3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e3ec.md) _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

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
      "site": "00b4dfc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dfc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4dfc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4dfc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dfc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4dfd8",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e3ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4e3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4e400",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dfc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dfc4.md#insn-00b4dfc4) · [`00b4dfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dfc4.md#insn-00b4dfc8) · [`00b4dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dfc4.md#insn-00b4dfe0)

~~~diff
- 00b4dfc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4dfc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4dfc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4dfc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4dfc4 bytes f44fbea9
- 00b4dfc8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4dfc8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4dfc8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4dfc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4dfc8 bytes fd7b01a9
- 00b4dfe0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4dfe0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4dfe0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab90980d24c15eb7df5b372fbba8e5cb"></a>

### [`00b4e070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e070.md) → [`00b4e498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e498.md) _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aef0.md) [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

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
      "site": "00b4e0b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4e4d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e08c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4e084",
      "READ",
      [
        "storage",
        "01125948",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4e08c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e4dc"
      ]
    ],
    [
      "unmatched:00b4e094",
      "PARAM",
      [
        "storage",
        "002ae111",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4e4ac",
      "READ",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e4b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e4dc"
      ]
    ],
    [
      "00b4e4bc",
      "PARAM",
      [
        "storage",
        "002ae151",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e070.md#insn-00b4e08c) · [`00b4e0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e070.md#insn-00b4e0a8) · [`00b4e0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e070.md#insn-00b4e0b0)
- 新版 `00b4e4d0`（命令位置の公開資料なし）

~~~diff
- 00b4e08c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4e08c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4e08c bytes 410100b5
- 00b4e0a8 ["INT_ADD", "register:40f0:8", ["const:b4e0a8:8", "const:4:8"]]
- 00b4e0a8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b4e4d0 ["INT_ADD", "register:40f0:8", ["const:b4e4d0:8", "const:4:8"]]
+ 00b4e4d0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b4e0a8 bytes 9a320494
+ 00b4e4d0 bytes 90320494
- 00b4e0b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:948:8"]]
- 00b4e0b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e0b0 bytes 80a604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d31692e49f46d41fa5841e775b96672c"></a>

### [`00b4e11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md) → [`00b4e544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md) _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0f0.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00b4e68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e68c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5b4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4f0.md) · 呼出先 9件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00b4eab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 28.57% / 新版 32.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 1件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 8件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4e570",
      "incomplete_value": true,
      "site": "00b4e570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e148",
      "incomplete_value": true,
      "site": "00b4e148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:968:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e18c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e1e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e564",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e570",
      "WRITE",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e588",
      "READ",
      [
        "storage",
        "011253c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e564",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e570",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e588",
      "READ",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md#insn-00b4e148) · [`00b4e168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md#insn-00b4e168) · [`00b4e18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md#insn-00b4e18c)
- 新版 `00b4e570`（命令位置の公開資料なし） · `00b4e590`（命令位置の公開資料なし）

~~~diff
- 00b4e148 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:968:8"]]
- 00b4e148 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b4e570 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d68:8"]]
+ 00b4e570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b4e148 bytes e86a09b9
+ 00b4e570 bytes e86a0db9
- 00b4e168 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4e168 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b4e590 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4e590 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b4e168 bytes 410100b5
+ 00b4e590 bytes 410100b5
- 00b4e18c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:3c8:8"]]
- 00b4e18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e18c bytes c0e601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb636736ab4f4ba2ece385aae223e373"></a>

### [`00b4e4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e4dc.md) → [`00b4e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e904.md) _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b0e0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b4e0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 36.11% / 新版 36.11%

CFGの説明率　旧版 29.73% / 新版 28.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e590"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e918",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e920",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4e50c"
      ]
    ],
    [
      "unmatched:00b4e500",
      "PARAM",
      [
        "storage",
        "002bd0be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4e918",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4e920",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4e934"
      ]
    ],
    [
      "00b4e928",
      "PARAM",
      [
        "storage",
        "002bd0fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e4dc.md#insn-00b4e504) · [`00b4e510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e4dc.md#insn-00b4e510) · [`00b4e52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e4dc.md#insn-00b4e52c)

~~~diff
- 00b4e504 ["INT_ADD", "register:40f0:8", ["const:b4e504:8", "const:4:8"]]
- 00b4e504 ["CALL", null, ["callee:00c5b000:8"]]
- 00b4e504 bytes bf310494
- 00b4e510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00b4e510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b4e510 bytes 886a09b9
- 00b4e52c ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b4e52c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b4e52c bytes c8000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7eeac79cfc409e2eb2a85642d980a06"></a>

### [`00b4e68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e68c.md) → [`00b4eab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eab4.md) FUN_00b4eab4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4e11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e11c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00b4e544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4e544.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, constant, control_flow, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 61.54% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4eb30",
      "incomplete_value": true,
      "site": "00b4eb30",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e708",
      "incomplete_value": true,
      "site": "00b4e708",
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ead8",
      "incomplete_value": true,
      "site": "00b4eadc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00b4e6b0",
      "incomplete_value": true,
      "site": "00b4e6b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4eb04",
      "incomplete_value": true,
      "site": "00b4eb04",
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
    "old": {
      "definition_site": "00b4e6dc",
      "incomplete_value": true,
      "site": "00b4e6dc",
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
      "00b4eac8",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eaf8",
      "READ",
      [
        "storage",
        "01125970",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4e6fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57eb0"
      ]
    ]
  ],
  "added": [
    [
      "00b4eac8",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eaf8",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eb1c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57eb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e68c.md#insn-00b4e6fc) · [`00b4e708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e68c.md#insn-00b4e708)
- 新版 `00b4eb30`（命令位置の公開資料なし） · `00b4eb1c`（命令位置の公開資料なし）

~~~diff
- 00b4e6fc ["INT_ADD", "register:40f0:8", ["const:b4e6fc:8", "const:4:8"]]
- 00b4e6fc ["CALL", null, ["callee:00c57eb0:8"]]
- 00b4e6fc bytes ed240494
- 00b4e708 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
- 00b4e708 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4e708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4eb30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d70:8"]]
+ 00b4eb30 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4eb30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4e708 bytes bfba04f9
+ 00b4eb30 bytes bfba06f9
+ 00b4eb1c ["INT_ADD", "register:40f0:8", ["const:b4eb1c:8", "const:4:8"]]
+ 00b4eb1c ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b4eb1c bytes e5240494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c10cb948fa2c335102f165b50039d0d"></a>

### [`00b4e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md) → [`00b4eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md) _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5aaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaa0.md) · 呼出先 13件 [`00b4f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md) [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aea0.md) · 呼出先 13件 [`00b4fbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md) [`00b50de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 26.87% / 新版 26.87%

CFGの説明率　旧版 23.18% / 新版 23.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件, `store_destination` 11件, `unresolved_branch_alignment` 61件, `unresolved_call_alignment` 63件, `unresolved_store_alignment` 35件

アドレスに依存する影響 `branch_value` 5件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4eb74",
      "incomplete_value": true,
      "site": "00b4eb74",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e74c",
      "incomplete_value": true,
      "site": "00b4e74c",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4e7ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4eb68",
      "READ",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4eb74",
      "WRITE",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4eb94",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4eb68",
      "READ",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4eb74",
      "WRITE",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b4eb94",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md#insn-00b4e74c) · [`00b4e794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md#insn-00b4e794) · [`00b4e7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md#insn-00b4e7ec)
- 新版 `00b4eb74`（命令位置の公開資料なし）

~~~diff
- 00b4e74c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
- 00b4e74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b4eb74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
+ 00b4eb74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b4e74c bytes a87a09b9
+ 00b4eb74 bytes a87a0db9
- 00b4e794 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:430:8"]]
- 00b4e794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e794 bytes c01a02f9
- 00b4e7ec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:460:8"]]
- 00b4e7ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4e7ec bytes c03202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74c602a9775412686c961d4fa5b614ab"></a>

### [`00b4f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md) → [`00b4fbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md) FUN_00b4fbc0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md) [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) · 呼出先 1件 [`00c5af80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af80.md)
- 新版 呼出元 2件 [`00b4eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md) [`00b50de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md) · 呼出先 1件 [`00c5b380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b380.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 4.74% / 新版 4.74%

CFGの説明率　旧版 2.66% / 新版 2.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 105件, `unresolved_call_alignment` 180件, `unresolved_store_alignment` 73件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f7d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f824"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4f850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4fbd4",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4fbdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4f828"
      ]
    ],
    [
      "00b4fbe4",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4fbd4",
      "READ",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4fbdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4fc50"
      ]
    ],
    [
      "00b4fbe4",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4f7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md#insn-00b4f7d4) · [`00b4f824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md#insn-00b4f824) · [`00b4f850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md#insn-00b4f850)

~~~diff
- 00b4f7d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4f7d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4f7d4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:468:8"]]
- 00b4f7d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4f7d4 bytes bfa21139
- 00b4f824 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
- 00b4f824 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4f824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4f824 bytes 9f3202f9
- 00b4f850 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4f850 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4f850 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:438:8"]]
- 00b4f850 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4f850 bytes bfe21039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d1b08a4e15dad7a8cfbbb513bb75cfd"></a>

### [`00b509bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md) → [`00b50de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50de4.md) _ZN8firebase4util9TerminateEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b4e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4e/00b4e714.md) [`00c5abd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abd0.md) · 呼出先 10件 [`00b4f798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4f/00b4f798.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md) [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md)
- 新版 呼出元 2件 [`00b4eb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4e/00b4eb3c.md) [`00c5afd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afd0.md) · 呼出先 10件 [`00b4fbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4f/00b4fbc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md) [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.14% / 新版 87.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b50e18",
      "incomplete_value": true,
      "site": "00b50e18",
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
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b509f0",
      "incomplete_value": true,
      "site": "00b509f0",
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
            "const:978:8"
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
      "definition_site": "00b50e7c",
      "incomplete_value": true,
      "site": "00b50e7c",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50a54",
      "incomplete_value": true,
      "site": "00b50a54",
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
            "const:980:8"
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
      "definition_site": "00b50e38",
      "incomplete_value": true,
      "site": "00b50e38",
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
      "definition_site": "00b50a10",
      "incomplete_value": true,
      "site": "00b50a10",
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
    "ordinal": 2,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b50df8",
      "READ",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ],
    [
      "00b50e08",
      "PARAM",
      [
        "storage",
        "002a09eb",
        null,
        "string"
      ]
    ],
    [
      "00b50e10",
      "READ",
      [
        "storage",
        "01125978",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b50df8",
      "READ",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00b50e08",
      "PARAM",
      [
        "storage",
        "002a0ab8",
        null,
        "string"
      ]
    ],
    [
      "00b50e10",
      "READ",
      [
        "storage",
        "01125d78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b509e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md#insn-00b509e4) · [`00b509f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md#insn-00b509f0) · [`00b50a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b509bc.md#insn-00b50a28)
- 新版 `00b50e0c`（命令位置の公開資料なし） · `00b50e18`（命令位置の公開資料なし） · `00b50e50`（命令位置の公開資料なし）

~~~diff
- 00b509e4 ["INT_ADD", "register:40f0:8", ["const:b509e4:8", "const:4:8"]]
- 00b509e4 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b50e0c ["INT_ADD", "register:40f0:8", ["const:b50e0c:8", "const:4:8"]]
+ 00b50e0c ["CALL", null, ["callee:00c5b000:8"]]
- 00b509e4 bytes 87280494
+ 00b50e0c bytes 7d280494
- 00b509f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
- 00b509f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b50e18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
+ 00b50e18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b509f0 bytes 887a09b9
+ 00b50e18 bytes 887a0db9
- 00b50a28 ["INT_ADD", "register:40f0:8", ["const:b50a28:8", "const:4:8"]]
- 00b50a28 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00b50e50 ["INT_ADD", "register:40f0:8", ["const:b50e50:8", "const:4:8"]]
+ 00b50e50 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00b50a28 bytes 1e2a0494
+ 00b50e50 bytes 142a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1b0201564360d058bc4b8481612f61"></a>

### [`00b50ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50ad4.md) → [`00b50efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b50/00b50efc.md) _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5afa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5afa0.md) · 呼出先 6件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 1件 [`00c5b3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b3a0.md) · 呼出先 6件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b50f20",
      "incomplete_value": true,
      "site": "00b50f28",
      "value": [
        "LOAD",
        "8",
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
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50af8",
      "incomplete_value": true,
      "site": "00b50b00",
      "value": [
        "LOAD",
        "8",
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
                "const:3e0:8"
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
      "definition_site": "00b50f80",
      "incomplete_value": false,
      "site": "00b50f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:4ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50b58",
      "incomplete_value": false,
      "site": "00b50b5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:46e:8"
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
      "definition_site": "00b50fa0",
      "incomplete_value": true,
      "site": "00b50fbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b50b78",
      "incomplete_value": true,
      "site": "00b50b94",
      "value": [
        "LOAD",
        "8",
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
      "00b50f20",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b50f80",
      "PARAM",
      [
        "storage",
        "002b346e",
        null,
        "string"
      ]
    ],
    [
      "00b50fa0",
      "READ",
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
      "00b50f20",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b50f80",
      "PARAM",
      [
        "storage",
        "002b34ae",
        null,
        "string"
      ]
    ],
    [
      "00b50fa0",
      "READ",
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

- 旧版 [`00b50b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50ad4.md#insn-00b50b00) · [`00b50b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50ad4.md#insn-00b50b14) · [`00b50b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50ad4.md#insn-00b50b5c)
- 新版 `00b50f28`（命令位置の公開資料なし） · `00b50f3c`（命令位置の公開資料なし） · `00b50f84`（命令位置の公開資料なし）

~~~diff
- 00b50b00 ["INT_ADD", "register:40f0:8", ["const:b50b00:8", "const:4:8"]]
- 00b50b00 ["CALL", null, ["callee:00497834:8"]]
+ 00b50f28 ["INT_ADD", "register:40f0:8", ["const:b50f28:8", "const:4:8"]]
+ 00b50f28 ["CALL", null, ["callee:00497834:8"]]
- 00b50b00 bytes 3d1be597
+ 00b50f28 bytes 431ae597
- 00b50b14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b50b14 ["INT_ADD", "register:40f0:8", ["const:b50b14:8", "const:4:8"]]
- 00b50b14 ["CALLIND", null, ["register:0:8"]]
+ 00b50f3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b50f3c ["INT_ADD", "register:40f0:8", ["const:b50f3c:8", "const:4:8"]]
+ 00b50f3c ["CALLIND", null, ["register:0:8"]]
- 00b50b14 bytes 00013fd6
+ 00b50f3c bytes 00013fd6
- 00b50b5c ["INT_ADD", "register:40f0:8", ["const:b50b5c:8", "const:4:8"]]
- 00b50b5c ["CALL", null, ["callee:00c5b130:8"]]
+ 00b50f84 ["INT_ADD", "register:40f0:8", ["const:b50f84:8", "const:4:8"]]
+ 00b50f84 ["CALL", null, ["callee:00c5b130:8"]]
- 00b50b5c bytes 75280494
+ 00b50f84 bytes 6b280494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe06fa4f538c912879c36dee1caed439"></a>

### [`00b50f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50f74.md) → [`00b5139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b5139c.md) _ZN8firebase4util17JavaThreadContext10InitializeEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af50.md) · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)
- 新版 呼出元 1件 [`00c5b350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b350.md) · 呼出先 2件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md) [`00c5af30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 83.87% / 新版 83.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `store_condition` 1件, `store_destination` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b513e8",
      "incomplete_value": true,
      "site": "00b513e8",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b50fc0",
      "incomplete_value": true,
      "site": "00b50fc0",
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
            "const:278:8"
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
      "definition_site": "00b51488",
      "incomplete_value": true,
      "site": "00b51488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51060",
      "incomplete_value": true,
      "site": "00b51060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b514d4",
      "incomplete_value": true,
      "site": "00b514d4",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b510ac",
      "incomplete_value": true,
      "site": "00b510ac",
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
            "const:2b0:8"
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
      "00b513b8",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b513cc",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ],
    [
      "00b513e8",
      "WRITE",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b513b8",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b513cc",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ],
    [
      "00b513e8",
      "WRITE",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b50fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50f74.md#insn-00b50fb8) · [`00b50fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50f74.md#insn-00b50fc0) · [`00b50fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b50/00b50f74.md#insn-00b50fe8)
- 新版 `00b513e0`（命令位置の公開資料なし） · `00b513e8`（命令位置の公開資料なし） · `00b51410`（命令位置の公開資料なし）

~~~diff
- 00b50fb8 ["INT_ADD", "register:40f0:8", ["const:b50fb8:8", "const:4:8"]]
- 00b50fb8 ["CALL", null, ["callee:00c5af10:8"]]
+ 00b513e0 ["INT_ADD", "register:40f0:8", ["const:b513e0:8", "const:4:8"]]
+ 00b513e0 ["CALL", null, ["callee:00c5af10:8"]]
- 00b50fb8 bytes d6260494
+ 00b513e0 bytes cc260494
- 00b50fc0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:278:8"]]
- 00b50fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b513e8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:678:8"]]
+ 00b513e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b50fc0 bytes c03e01f9
+ 00b513e8 bytes c03e03f9
- 00b50fe8 ["INT_ADD", "register:40f0:8", ["const:b50fe8:8", "const:4:8"]]
- 00b50fe8 ["CALL", null, ["callee:00c5af30:8"]]
+ 00b51410 ["INT_ADD", "register:40f0:8", ["const:b51410:8", "const:4:8"]]
+ 00b51410 ["CALL", null, ["callee:00c5af30:8"]]
- 00b50fe8 bytes d2260494
+ 00b51410 bytes c8260494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67accc106ed9de636f87ff68f40dd6c4"></a>

### [`00b510e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b510e8.md) → [`00b51510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51510.md) _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ab00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab00.md) · 呼出先 7件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad30.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md) [`00c5b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b200.md)
- 新版 呼出元 1件 [`00c5af00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af00.md) · 呼出先 7件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b130.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md) [`00c5b600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b600.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.80% / 新版 92.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51548",
      "incomplete_value": true,
      "site": "00b5154c",
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
            "const:79c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51120",
      "incomplete_value": true,
      "site": "00b51124",
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
            "const:75c:8"
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
      "definition_site": "00b51694",
      "incomplete_value": true,
      "site": "00b516a0",
      "value": [
        "LOAD",
        "8",
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
                "register:40c8:8"
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
    "old": {
      "definition_site": "00b5126c",
      "incomplete_value": true,
      "site": "00b51278",
      "value": [
        "LOAD",
        "8",
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:268:8"
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
      "00b51544",
      "PARAM",
      [
        "storage",
        "002bd0db",
        null,
        "string"
      ]
    ],
    [
      "00b51548",
      "PARAM",
      [
        "storage",
        "002bf75c",
        null,
        "string"
      ]
    ],
    [
      "00b51578",
      "PARAM",
      [
        "storage",
        "01125988",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b51544",
      "PARAM",
      [
        "storage",
        "002bd11b",
        null,
        "string"
      ]
    ],
    [
      "00b51548",
      "PARAM",
      [
        "storage",
        "002bf79c",
        null,
        "string"
      ]
    ],
    [
      "00b51578",
      "PARAM",
      [
        "storage",
        "01125d88",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b510e8.md#insn-00b51124) · [`00b51278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b510e8.md#insn-00b51278) · [`00b5110c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b510e8.md#insn-00b5110c)
- 新版 `00b5154c`（命令位置の公開資料なし） · `00b516a0`（命令位置の公開資料なし） · `00b51534`（命令位置の公開資料なし）

~~~diff
- 00b51124 ["INT_ADD", "register:40f0:8", ["const:b51124:8", "const:4:8"]]
- 00b51124 ["CALL", null, ["callee:00c5b130:8"]]
+ 00b5154c ["INT_ADD", "register:40f0:8", ["const:b5154c:8", "const:4:8"]]
+ 00b5154c ["CALL", null, ["callee:00c5b130:8"]]
- 00b51124 bytes 03270494
+ 00b5154c bytes f9260494
- 00b51278 ["INT_ADD", "register:40f0:8", ["const:b51278:8", "const:4:8"]]
- 00b51278 ["CALL", null, ["callee:00574cec:8"]]
+ 00b516a0 ["INT_ADD", "register:40f0:8", ["const:b516a0:8", "const:4:8"]]
+ 00b516a0 ["CALL", null, ["callee:00574cec:8"]]
- 00b51278 bytes 8d8ee897
+ 00b516a0 bytes 938de897
- 00b5110c ["COPY", "tmp:0:8", ["const:db:8"]]
- 00b5110c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5110c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5110c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b51534 ["COPY", "tmp:0:8", ["const:11b:8"]]
+ 00b51534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b51534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b51534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5110c bytes 086d0391
+ 00b51534 bytes 086d0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-830414fc38ed978de523e6fc93cc9a25"></a>

### [`00b512dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md) → [`00b51704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51704.md) _ZN7_JNIEnv20CallStaticVoidMethodEP7_jclassP10_jmethodIDz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ae40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae40.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c5b240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b240.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

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
      "site": "00b5132c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b51330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b51330"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5132c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b51330",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b51334",
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
      "00b51754",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b51758",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b5175c",
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

- 旧版 [`00b5132c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md#insn-00b5132c) · [`00b51330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md#insn-00b51330) · [`00b51334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b512dc.md#insn-00b51334)

~~~diff
- 00b5132c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b5132c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b5132c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b5132c bytes ab831ef8
- 00b51330 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b51330 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b51330 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00b51330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b51330 bytes a9a33da9
- 00b51334 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00b51334 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b51334 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00b51334 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b51334 bytes acab3ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d00395ab0f3396384e0764ae54db29f"></a>

### [`00b51410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51410.md) → [`00b51838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51838.md) _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b020.md) · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)
- 新版 呼出元 1件 [`00c5b420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b420.md) · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5185c",
      "incomplete_value": true,
      "site": "00b51868",
      "value": [
        "LOAD",
        "8",
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51434",
      "incomplete_value": true,
      "site": "00b51440",
      "value": [
        "LOAD",
        "8",
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
                "const:430:8"
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
      "definition_site": "00b51860",
      "incomplete_value": true,
      "site": "00b51868",
      "value": [
        "LOAD",
        "8",
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
                "const:840:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51438",
      "incomplete_value": true,
      "site": "00b51440",
      "value": [
        "LOAD",
        "8",
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
                "const:440:8"
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
      "00b5185c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51860",
      "READ",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5187c",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5185c",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51860",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5187c",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51410.md#insn-00b51440) · [`00b5142c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51410.md#insn-00b5142c) · [`00b51434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51410.md#insn-00b51434)
- 新版 `00b51868`（命令位置の公開資料なし） · `00b51854`（命令位置の公開資料なし） · `00b5185c`（命令位置の公開資料なし）

~~~diff
- 00b51440 ["INT_ADD", "register:40f0:8", ["const:b51440:8", "const:4:8"]]
- 00b51440 ["CALL", null, ["callee:005896f4:8"]]
+ 00b51868 ["INT_ADD", "register:40f0:8", ["const:b51868:8", "const:4:8"]]
+ 00b51868 ["CALL", null, ["callee:005896f4:8"]]
- 00b51440 bytes 9de0e897
+ 00b51868 bytes a3dfe897
- 00b5142c ["COPY", "tmp:0:8", ["const:440:8"]]
- 00b5142c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00b5142c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00b5142c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00b51854 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00b51854 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00b51854 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00b51854 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00b5142c bytes d6021191
+ 00b51854 bytes d6022191
- 00b51434 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
- 00b51434 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5185c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:830:8"]]
+ 00b5185c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b51434 bytes 011942f9
+ 00b5185c bytes 011944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e28a6564a6dd769c747af97483854944"></a>

### [`00b51518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51518.md) → [`00b51940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51940.md) _ZN8firebase4util25StdUnorderedSetToJavaListEP7_JNIEnvRKNSt6__ndk113unordered_setINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 71.43% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51964",
      "incomplete_value": true,
      "site": "00b51970",
      "value": [
        "LOAD",
        "8",
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
                "const:830:8"
              ]
            ]
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
      "definition_site": "00b51968",
      "incomplete_value": true,
      "site": "00b51970",
      "value": [
        "LOAD",
        "8",
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
                "const:840:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5153c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b51540",
      "READ",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51980",
      "READ",
      [
        "storage",
        "01125450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51964",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51968",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51980",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51518.md#insn-00b51548) · [`00b51534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51518.md#insn-00b51534) · [`00b51538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51518.md#insn-00b51538)
- 新版 `00b51970`（命令位置の公開資料なし）

~~~diff
- 00b51548 ["INT_ADD", "register:40f0:8", ["const:b51548:8", "const:4:8"]]
- 00b51548 ["CALL", null, ["callee:005896f4:8"]]
+ 00b51970 ["INT_ADD", "register:40f0:8", ["const:b51970:8", "const:4:8"]]
+ 00b51970 ["CALL", null, ["callee:005896f4:8"]]
- 00b51548 bytes 5be0e897
+ 00b51970 bytes 61dfe897
- 00b51534 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00b51534 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00b51534 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00b51534 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00b51534 bytes b5021191
- 00b51538 ["COPY", "register:40a0:8", ["register:4008:8"]]
- 00b51538 bytes f40301aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85390e8547de2093500714c57152e401"></a>

### [`00b51610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51610.md) → [`00b51a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51a38.md) _ZN8firebase4util19VariantMapToJavaMapEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b030.md) · 呼出先 3件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b040.md)
- 新版 呼出元 1件 [`00c5b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b430.md) · 呼出先 3件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5b440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.85% / 新版 97.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51a5c",
      "incomplete_value": true,
      "site": "00b51a68",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b51634",
      "incomplete_value": true,
      "site": "00b51640",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51a60",
      "incomplete_value": true,
      "site": "00b51a68",
      "value": [
        "LOAD",
        "8",
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51638",
      "incomplete_value": true,
      "site": "00b51640",
      "value": [
        "LOAD",
        "8",
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
                "const:720:8"
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
      "00b51a5c",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a60",
      "READ",
      [
        "storage",
        "01125720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a70",
      "READ",
      [
        "storage",
        "01125848",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51a5c",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a60",
      "READ",
      [
        "storage",
        "01125b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51a70",
      "READ",
      [
        "storage",
        "01125c48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51610.md#insn-00b51640) · [`00b51634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51610.md#insn-00b51634) · [`00b51638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51610.md#insn-00b51638)
- 新版 `00b51a68`（命令位置の公開資料なし） · `00b51a5c`（命令位置の公開資料なし） · `00b51a60`（命令位置の公開資料なし）

~~~diff
- 00b51640 ["INT_ADD", "register:40f0:8", ["const:b51640:8", "const:4:8"]]
- 00b51640 ["CALL", null, ["callee:005896f4:8"]]
+ 00b51a68 ["INT_ADD", "register:40f0:8", ["const:b51a68:8", "const:4:8"]]
+ 00b51a68 ["CALL", null, ["callee:005896f4:8"]]
- 00b51640 bytes 1de0e897
+ 00b51a68 bytes 23dfe897
- 00b51634 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:710:8"]]
- 00b51634 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b51a5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
+ 00b51a5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b51634 bytes 018943f9
+ 00b51a5c bytes 018945f9
- 00b51638 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:720:8"]]
- 00b51638 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b51a60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b20:8"]]
+ 00b51a60 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b51638 bytes 229143f9
+ 00b51a60 bytes 229145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec524393fe9ac4fc6e009ef22ef9d864"></a>

### [`00b51784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51784.md) → [`00b51bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b51/00b51bac.md) _ZN8firebase4util19VariantToJavaObjectEP7_JNIEnvRKNS_7VariantE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5b040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b040.md) · 呼出先 7件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a700.md) [`00c5a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a720.md) [`00c5a9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9e0.md) [`00c5b030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b030.md)
- 新版 呼出元 1件 [`00c5b440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b440.md) · 呼出先 7件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5ab00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab00.md) [`00c5ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab20.md) [`00c5ade0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ade0.md) [`00c5b430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b51db8",
      "incomplete_value": false,
      "site": "00b51dbc",
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
            "const:3a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51990",
      "incomplete_value": false,
      "site": "00b51994",
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
            "const:2da:8"
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
      "00b51bdc",
      "DATA",
      [
        "storage",
        "0030b5ba",
        "switchD_00b517c0::switchdataD_0030b5ba",
        "byte"
      ]
    ],
    [
      "00b51c30",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51c34",
      "READ",
      [
        "storage",
        "01125820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b51bdc",
      "DATA",
      [
        "storage",
        "0030b5fa",
        "switchD_00b51be8::switchdataD_0030b5fa",
        "byte"
      ]
    ],
    [
      "00b51c30",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b51c34",
      "READ",
      [
        "storage",
        "01125c20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b51994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51784.md#insn-00b51994) · [`00b517ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51784.md#insn-00b517ac) · [`00b517b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51784.md#insn-00b517b0)
- 新版 `00b51dbc`（命令位置の公開資料なし） · `00b51bd4`（命令位置の公開資料なし）

~~~diff
- 00b51994 ["INT_ADD", "register:40f0:8", ["const:b51994:8", "const:4:8"]]
- 00b51994 ["CALL", null, ["callee:00c5ade0:8"]]
+ 00b51dbc ["INT_ADD", "register:40f0:8", ["const:b51dbc:8", "const:4:8"]]
+ 00b51dbc ["CALL", null, ["callee:00c5ade0:8"]]
- 00b51994 bytes 13240494
+ 00b51dbc bytes 09240494
- 00b517ac ["COPY", "tmp:0:8", ["const:5ba:8"]]
- 00b517ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b517ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b517ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b51bd4 ["COPY", "tmp:0:8", ["const:5fa:8"]]
+ 00b51bd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b51bd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b51bd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b517ac bytes 29e91691
+ 00b51bd4 bytes 29e91791
- 00b517b0 ["COPY", "register:4050:8", ["const:b517c4:8"]]
- 00b517b0 bytes aa000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f563f02fb95fb2354916f96cfa84f24"></a>

### [`00b51cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51cb0.md) → [`00b520d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b52/00b520d8.md) _ZN8firebase4util15JavaMapToStdMapEP7_JNIEnvPNSt6__ndk13mapINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEESA_NS3_4lessISA_EEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.74% / 新版 92.74%

CFGの説明率　旧版 83.56% / 新版 84.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b51e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b52268"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b52118",
      "incomplete_value": true,
      "site": "00b52120",
      "value": [
        "LOAD",
        "8",
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b51cf0",
      "incomplete_value": true,
      "site": "00b51cf8",
      "value": [
        "LOAD",
        "8",
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
                "const:858:8"
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
      "00b52118",
      "READ",
      [
        "storage",
        "01125858",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52164",
      "READ",
      [
        "storage",
        "01125898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b521b4",
      "READ",
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
      "00b52118",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52164",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b521b4",
      "READ",
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

- 旧版 [`00b51cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51cb0.md#insn-00b51cf8) · [`00b51d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51cb0.md#insn-00b51d48) · [`00b51d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b51/00b51cb0.md#insn-00b51d9c)
- 新版 `00b52120`（命令位置の公開資料なし） · `00b52170`（命令位置の公開資料なし） · `00b521c4`（命令位置の公開資料なし）

~~~diff
- 00b51cf8 ["INT_ADD", "register:40f0:8", ["const:b51cf8:8", "const:4:8"]]
- 00b51cf8 ["CALL", null, ["callee:00497834:8"]]
+ 00b52120 ["INT_ADD", "register:40f0:8", ["const:b52120:8", "const:4:8"]]
+ 00b52120 ["CALL", null, ["callee:00497834:8"]]
- 00b51cf8 bytes bf16e597
+ 00b52120 bytes c515e597
- 00b51d48 ["INT_ADD", "register:40f0:8", ["const:b51d48:8", "const:4:8"]]
- 00b51d48 ["CALL", null, ["callee:00497834:8"]]
+ 00b52170 ["INT_ADD", "register:40f0:8", ["const:b52170:8", "const:4:8"]]
+ 00b52170 ["CALL", null, ["callee:00497834:8"]]
- 00b51d48 bytes ab16e597
+ 00b52170 bytes b115e597
- 00b51d9c ["INT_ADD", "register:40f0:8", ["const:b51d9c:8", "const:4:8"]]
- 00b51d9c ["CALL", null, ["callee:00497a48:8"]]
+ 00b521c4 ["INT_ADD", "register:40f0:8", ["const:b521c4:8", "const:4:8"]]
+ 00b521c4 ["CALL", null, ["callee:00497a48:8"]]
- 00b51d9c bytes 1b17e597
+ 00b521c4 bytes 2116e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

