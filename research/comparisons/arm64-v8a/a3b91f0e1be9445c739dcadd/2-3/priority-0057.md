# v15.7.4 → v16.0.0 · 最優先の変更候補 (57)

[一覧の目次](README.md)

<a id="compare-fffde8a61ecbd01685ac4ff6d8670c40"></a>

### [`00ae78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md) → [`00b4762c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b4762c.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde030.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5aab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aab0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b47648",
      "incomplete_value": false,
      "site": "00b4764c",
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
    "old": {
      "definition_site": "00ae78c4",
      "incomplete_value": false,
      "site": "00ae78c8",
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
      "definition_site": "00b47658",
      "incomplete_value": true,
      "site": "00b47664",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae78d4",
      "incomplete_value": true,
      "site": "00ae78e0",
      "value": [
        "LOAD",
        "8",
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
      "00b47648",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b47658",
      "DATA",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47648",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b47658",
      "DATA",
      [
        "storage",
        "01125440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae78c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md#insn-00ae78c8) · [`00ae78c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md#insn-00ae78c0) · [`00ae78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md#insn-00ae78c4)
- 新版 `00b4764c`（命令位置の公開資料なし） · `00b47644`（命令位置の公開資料なし） · `00b47648`（命令位置の公開資料なし）

~~~diff
- 00ae78c8 ["INT_ADD", "register:40f0:8", ["const:ae78c8:8", "const:4:8"]]
- 00ae78c8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4764c ["INT_ADD", "register:40f0:8", ["const:b4764c:8", "const:4:8"]]
+ 00b4764c ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae78c8 bytes 2eda0394
+ 00b4764c bytes 6d4d0494
- 00ae78c0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b47644 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae78c0 bytes 80bdffb0
+ 00b47644 bytes 00bbffb0
- 00ae78c4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae78c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae78c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae78c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47648 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b47648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae78c4 bytes 001c1591
+ 00b47648 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b820f3166f52c798492248c754a8949"></a>

### [`00ae78e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md) → [`00b47668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47668.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae7924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b476a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae78f8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b476ac"
      ]
    ],
    [
      "unmatched:00ae7908",
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
      "00b4767c",
      "READ",
      [
        "storage",
        "01125430",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b476ac"
      ]
    ],
    [
      "00b4768c",
      "PARAM",
      [
        "storage",
        "002a7038",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md#insn-00ae7900) · [`00ae791c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md#insn-00ae791c) · [`00ae7924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md#insn-00ae7924)
- 新版 `00b476a0`（命令位置の公開資料なし）

~~~diff
- 00ae7900 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7900 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7900 bytes 410100b5
- 00ae791c ["INT_ADD", "register:40f0:8", ["const:ae791c:8", "const:4:8"]]
- 00ae791c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b476a0 ["INT_ADD", "register:40f0:8", ["const:b476a0:8", "const:4:8"]]
+ 00b476a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae791c bytes ddd90394
+ 00b476a0 bytes 1c4d0494
- 00ae7924 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00ae7924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7924 bytes 80ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70edab1b946572456fd1a014a933a137"></a>

### [`00ae7954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md) → [`00b476d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b476d8.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b476f4",
      "incomplete_value": false,
      "site": "00b476f8",
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
    "old": {
      "definition_site": "00ae7970",
      "incomplete_value": false,
      "site": "00ae7974",
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
      "definition_site": "00b47704",
      "incomplete_value": true,
      "site": "00b47710",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7980",
      "incomplete_value": true,
      "site": "00ae798c",
      "value": [
        "LOAD",
        "8",
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
      "00b476f4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b47704",
      "DATA",
      [
        "storage",
        "010a0598",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b476f4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b47704",
      "DATA",
      [
        "storage",
        "01125458",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md#insn-00ae7974) · [`00ae796c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md#insn-00ae796c) · [`00ae7970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md#insn-00ae7970)
- 新版 `00b476f8`（命令位置の公開資料なし） · `00b476f0`（命令位置の公開資料なし） · `00b476f4`（命令位置の公開資料なし）

~~~diff
- 00ae7974 ["INT_ADD", "register:40f0:8", ["const:ae7974:8", "const:4:8"]]
- 00ae7974 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b476f8 ["INT_ADD", "register:40f0:8", ["const:b476f8:8", "const:4:8"]]
+ 00b476f8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae7974 bytes 03da0394
+ 00b476f8 bytes 424d0494
- 00ae796c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b476f0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae796c bytes 80bdffd0
+ 00b476f0 bytes 00bbffd0
- 00ae7970 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7970 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7970 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7970 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b476f4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b476f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b476f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b476f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7970 bytes 00c81791
+ 00b476f4 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b5f2e3c58c7dcece2a9b354731e551c"></a>

### [`00ae7990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md) → [`00b47714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47714.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b47740",
      "incomplete_value": true,
      "site": "00b47740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79bc",
      "incomplete_value": true,
      "site": "00ae79bc",
      "value": [
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
      "definition_site": "00b47728",
      "incomplete_value": true,
      "site": "00b47728",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79a4",
      "incomplete_value": true,
      "site": "00ae79a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b47734",
      "incomplete_value": false,
      "site": "00b47738",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79b0",
      "incomplete_value": false,
      "site": "00ae79b4",
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
      "00b47724",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47734",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      "00b47740",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47724",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47734",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47740",
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae79b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md#insn-00ae79b4) · [`00ae79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md#insn-00ae79bc) · [`00ae799c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md#insn-00ae799c)
- 新版 `00b47738`（命令位置の公開資料なし） · `00b47740`（命令位置の公開資料なし） · `00b47720`（命令位置の公開資料なし）

~~~diff
- 00ae79b4 ["INT_ADD", "register:40f0:8", ["const:ae79b4:8", "const:4:8"]]
- 00ae79b4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47738 ["INT_ADD", "register:40f0:8", ["const:b47738:8", "const:4:8"]]
+ 00b47738 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae79b4 bytes b7d90394
+ 00b47738 bytes f64c0494
- 00ae79bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae79bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:460:8"]]
+ 00b47740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae79bc bytes 60d202f9
+ 00b47740 bytes 603202f9
- 00ae799c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b47720 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae799c bytes d32d00b0
+ 00b47720 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f217b337eafec4cd4c264d452dbf38d4"></a>

### [`00ae79d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md) → [`00b47754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47754.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae79fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47780"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47768",
      "incomplete_value": true,
      "site": "00b47768",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79e4",
      "incomplete_value": true,
      "site": "00ae79e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b47764",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae79ec",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae79f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b47764",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47770",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47778",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae79e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md#insn-00ae79e4) · [`00ae79f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md#insn-00ae79f4) · [`00ae79fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md#insn-00ae79fc)
- 新版 `00b47768`（命令位置の公開資料なし）

~~~diff
- 00ae79e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae79e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47768 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47768 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae79e4 bytes e80000b5
+ 00b47768 bytes e80000b5
- 00ae79f4 ["INT_ADD", "register:40f0:8", ["const:ae79f4:8", "const:4:8"]]
- 00ae79f4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae79f4 bytes a7d90394
- 00ae79fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae79fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae79fc bytes 60d202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-883b71f967cf90ae9e758cf807418b51"></a>

### [`00ae7a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md) → [`00b477d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b477d8.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae7a84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47808"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7a68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b477e8",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4780c"
      ]
    ],
    [
      "unmatched:00ae7a70",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b477e8",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4780c"
      ]
    ],
    [
      "00b477f4",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md#insn-00ae7a68) · [`00ae7a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md#insn-00ae7a7c) · [`00ae7a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md#insn-00ae7a84)
- 新版 `00b47800`（命令位置の公開資料なし）

~~~diff
- 00ae7a68 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7a68 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae7a68 bytes 080100b5
- 00ae7a7c ["INT_ADD", "register:40f0:8", ["const:ae7a7c:8", "const:4:8"]]
- 00ae7a7c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47800 ["INT_ADD", "register:40f0:8", ["const:b47800:8", "const:4:8"]]
+ 00b47800 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7a7c bytes 85d90394
+ 00b47800 bytes c44c0494
- 00ae7a84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00ae7a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7a84 bytes 60d202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4967b9ab3805bb4701b41b4d3303653"></a>

### [`00ae7aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md) → [`00b47828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47828.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b478b0",
      "incomplete_value": true,
      "site": "00b478b0",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b2c",
      "incomplete_value": true,
      "site": "00ae7b2c",
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7b00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b47884"
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
      "00b4783c",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae7ad8",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7b00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b478a8"
      ]
    ]
  ],
  "added": [
    [
      "00b4783c",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4785c",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47884",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b478a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md#insn-00ae7ae4) · [`00ae7b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md#insn-00ae7b00) · [`00ae7b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md#insn-00ae7b2c)
- 新版 `00b47868`（命令位置の公開資料なし） · `00b478b0`（命令位置の公開資料なし）

~~~diff
- 00ae7ae4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7ae4 ["INT_ADD", "register:40f0:8", ["const:ae7ae4:8", "const:4:8"]]
- 00ae7ae4 ["CALLIND", null, ["register:0:8"]]
+ 00b47868 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47868 ["INT_ADD", "register:40f0:8", ["const:b47868:8", "const:4:8"]]
+ 00b47868 ["CALLIND", null, ["register:0:8"]]
- 00ae7ae4 bytes 00013fd6
+ 00b47868 bytes 00013fd6
- 00ae7b00 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00ae7b00 bytes 20010054
- 00ae7b2c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7b2c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
- 00ae7b2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b478b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b478b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:468:8"]]
+ 00b478b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7b2c bytes a0a21639
+ 00b478b0 bytes a0a21139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a492eeee0cc155c0357477a6f73c15fc"></a>

### [`00ae7b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md) → [`00b478c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b478c4.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 63.64% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47900",
      "incomplete_value": true,
      "site": "00b47900",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b7c",
      "incomplete_value": true,
      "site": "00ae7b7c",
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
      "definition_site": "00b47950",
      "incomplete_value": true,
      "site": "00b47950",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7bcc",
      "incomplete_value": true,
      "site": "00ae7bcc",
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
      "definition_site": "00b478dc",
      "incomplete_value": true,
      "site": "00b478dc",
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
      "definition_site": "00ae7b58",
      "incomplete_value": true,
      "site": "00ae7b58",
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
      "00b478d8",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b478e4",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47900",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b478d8",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b478e4",
      "READ",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47900",
      "WRITE",
      [
        "storage",
        "01125468",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md#insn-00ae7b58) · [`00ae7b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md#insn-00ae7b7c) · [`00ae7bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md#insn-00ae7bb4)
- 新版 `00b478dc`（命令位置の公開資料なし） · `00b47900`（命令位置の公開資料なし）

~~~diff
- 00ae7b58 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7b58 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b478dc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b478dc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae7b58 bytes c10300b4
+ 00b478dc bytes c10300b4
- 00ae7b7c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7b7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7b7c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
- 00ae7b7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47900 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47900 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47900 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:468:8"]]
+ 00b47900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7b7c bytes bfa21639
+ 00b47900 bytes bfa21139
- 00ae7bb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7bb4 ["INT_ADD", "register:40f0:8", ["const:ae7bb4:8", "const:4:8"]]
- 00ae7bb4 ["CALLIND", null, ["register:0:8"]]
- 00ae7bb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeeeace802cd95554b7f11bbba1abb33"></a>

### [`00ae7be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md) → [`00b47964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47964.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae7c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b479a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7bfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7bf4",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b479a8"
      ]
    ],
    [
      "unmatched:00ae7c04",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47978",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47980",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b479a8"
      ]
    ],
    [
      "00b47988",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md#insn-00ae7bfc) · [`00ae7c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md#insn-00ae7c18) · [`00ae7c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md#insn-00ae7c20)
- 新版 `00b4799c`（命令位置の公開資料なし）

~~~diff
- 00ae7bfc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7bfc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7bfc bytes 410100b5
- 00ae7c18 ["INT_ADD", "register:40f0:8", ["const:ae7c18:8", "const:4:8"]]
- 00ae7c18 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4799c ["INT_ADD", "register:40f0:8", ["const:b4799c:8", "const:4:8"]]
+ 00b4799c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7c18 bytes 1ed90394
+ 00b4799c bytes 5d4c0494
- 00ae7c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00ae7c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7c20 bytes 80d202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-154259c99d7ae5d8fdda67e6c98802c9"></a>

### [`00ae7c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md) → [`00b479d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b479d4.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b479f0",
      "incomplete_value": false,
      "site": "00b479f4",
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
    "old": {
      "definition_site": "00ae7c6c",
      "incomplete_value": false,
      "site": "00ae7c70",
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
      "definition_site": "00b47a00",
      "incomplete_value": true,
      "site": "00b47a0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7c7c",
      "incomplete_value": true,
      "site": "00ae7c88",
      "value": [
        "LOAD",
        "8",
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
      "00b479f0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b47a00",
      "DATA",
      [
        "storage",
        "010a05b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b479f0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b47a00",
      "DATA",
      [
        "storage",
        "01125470",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md#insn-00ae7c70) · [`00ae7c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md#insn-00ae7c68) · [`00ae7c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md#insn-00ae7c6c)
- 新版 `00b479f4`（命令位置の公開資料なし） · `00b479ec`（命令位置の公開資料なし） · `00b479f0`（命令位置の公開資料なし）

~~~diff
- 00ae7c70 ["INT_ADD", "register:40f0:8", ["const:ae7c70:8", "const:4:8"]]
- 00ae7c70 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b479f4 ["INT_ADD", "register:40f0:8", ["const:b479f4:8", "const:4:8"]]
+ 00b479f4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae7c70 bytes 44d90394
+ 00b479f4 bytes 834c0494
- 00ae7c68 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b479ec ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae7c68 bytes 80bdffb0
+ 00b479ec bytes 00bbffb0
- 00ae7c6c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae7c6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7c6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7c6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b479f0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b479f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b479f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b479f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7c6c bytes 001c1591
+ 00b479f0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b4cb7c08e799f24d0108cef0b7159b2"></a>

### [`00ae7c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md) → [`00b47a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a10.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b47a50",
      "incomplete_value": true,
      "site": "00b47a50",
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
            "const:460:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ccc",
      "incomplete_value": true,
      "site": "00ae7ccc",
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
      "definition_site": "00b47a2c",
      "incomplete_value": true,
      "site": "00b47a2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ca8",
      "incomplete_value": true,
      "site": "00ae7ca8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b47a34",
      "incomplete_value": false,
      "site": "00b47a48",
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
            "const:77e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7cb0",
      "incomplete_value": false,
      "site": "00ae7cc4",
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
      "00b47a24",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a34",
      "PARAM",
      [
        "storage",
        "002ae339",
        null,
        "string"
      ]
    ],
    [
      "00b47a50",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47a24",
      "READ",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a34",
      "PARAM",
      [
        "storage",
        "002bf77e",
        null,
        "string"
      ]
    ],
    [
      "00b47a50",
      "WRITE",
      [
        "storage",
        "01125460",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md#insn-00ae7cc4) · [`00ae7ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md#insn-00ae7ccc) · [`00ae7c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md#insn-00ae7c98)
- 新版 `00b47a48`（命令位置の公開資料なし） · `00b47a50`（命令位置の公開資料なし） · `00b47a1c`（命令位置の公開資料なし）

~~~diff
- 00ae7cc4 ["INT_ADD", "register:40f0:8", ["const:ae7cc4:8", "const:4:8"]]
- 00ae7cc4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47a48 ["INT_ADD", "register:40f0:8", ["const:b47a48:8", "const:4:8"]]
+ 00b47a48 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7cc4 bytes f3d80394
+ 00b47a48 bytes 324c0494
- 00ae7ccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00ae7ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47a50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:460:8"]]
+ 00b47a50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7ccc bytes 80d202f9
+ 00b47a50 bytes 803202f9
- 00ae7c98 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47a1c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae7c98 bytes d42d00b0
+ 00b47a1c bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d87ee475194c3ae6f87bc9e20552e5b1"></a>

### [`00ae7cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md) → [`00b47a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47a80.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b47a9c",
      "incomplete_value": false,
      "site": "00b47aa0",
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
    "old": {
      "definition_site": "00ae7d18",
      "incomplete_value": false,
      "site": "00ae7d1c",
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
      "definition_site": "00b47aac",
      "incomplete_value": true,
      "site": "00b47ab8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7d28",
      "incomplete_value": true,
      "site": "00ae7d34",
      "value": [
        "LOAD",
        "8",
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
      "00b47a9c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b47aac",
      "DATA",
      [
        "storage",
        "010a05b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47a9c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b47aac",
      "DATA",
      [
        "storage",
        "01125478",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md#insn-00ae7d1c) · [`00ae7d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md#insn-00ae7d14) · [`00ae7d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md#insn-00ae7d18)
- 新版 `00b47aa0`（命令位置の公開資料なし） · `00b47a98`（命令位置の公開資料なし） · `00b47a9c`（命令位置の公開資料なし）

~~~diff
- 00ae7d1c ["INT_ADD", "register:40f0:8", ["const:ae7d1c:8", "const:4:8"]]
- 00ae7d1c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b47aa0 ["INT_ADD", "register:40f0:8", ["const:b47aa0:8", "const:4:8"]]
+ 00b47aa0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae7d1c bytes 19d90394
+ 00b47aa0 bytes 584c0494
- 00ae7d14 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b47a98 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae7d14 bytes 80bdffd0
+ 00b47a98 bytes 00bbffd0
- 00ae7d18 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae7d18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7d18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7d18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47a9c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b47a9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47a9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47a9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7d18 bytes 00c81791
+ 00b47a9c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaaa4b06bee1981a0a2b3b6814236a9"></a>

### [`00ae7db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md) → [`00b47b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b3c.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae7de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47b6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47b50",
      "incomplete_value": true,
      "site": "00b47b50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7dcc",
      "incomplete_value": true,
      "site": "00ae7dcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b47b4c",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae7dd8",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae7de0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b47b4c",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b5c",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b47b64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md#insn-00ae7dcc) · [`00ae7de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md#insn-00ae7de0) · [`00ae7de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md#insn-00ae7de8)
- 新版 `00b47b50`（命令位置の公開資料なし）

~~~diff
- 00ae7dcc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7dcc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47b50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47b50 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7dcc bytes 080100b5
+ 00b47b50 bytes 080100b5
- 00ae7de0 ["INT_ADD", "register:40f0:8", ["const:ae7de0:8", "const:4:8"]]
- 00ae7de0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7de0 bytes acd80394
- 00ae7de8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00ae7de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7de8 bytes 60e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3032ea55a395446a8256eae0b89fd4f4"></a>

### [`00ae7dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md) → [`00b47b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47b80.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00ae7dfc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7e00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7e00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae7e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b47b90",
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
      "00b47b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b47b84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b47b90",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md#insn-00ae7dfc) · [`00ae7e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md#insn-00ae7e00) · [`00ae7e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md#insn-00ae7e10)
- 新版 `00b47b94`（命令位置の公開資料なし）

~~~diff
- 00ae7dfc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae7dfc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae7dfc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae7dfc bytes f30f1ef8
- 00ae7e00 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae7e00 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae7e00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae7e00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae7e00 bytes fd7b01a9
- 00ae7e10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae7e10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47b94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47b94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae7e10 bytes 080100b5
+ 00b47b94 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f1ed9b01d5c3fd37759c411e2e80b5d"></a>

### [`00ae7e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md) → [`00b47bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47bd0.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 79.49% / 新版 79.49%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47c58",
      "incomplete_value": true,
      "site": "00b47c58",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ed4",
      "incomplete_value": true,
      "site": "00ae7ed4",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7e8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7eb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae7e60",
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae7e80",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c58",
      "WRITE",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47be4",
      "READ",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47c04",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c58",
      "WRITE",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md#insn-00ae7e8c) · [`00ae7eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md#insn-00ae7eb8) · [`00ae7ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md#insn-00ae7ed4)
- 新版 `00b47c58`（命令位置の公開資料なし）

~~~diff
- 00ae7e8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7e8c ["INT_ADD", "register:40f0:8", ["const:ae7e8c:8", "const:4:8"]]
- 00ae7e8c ["CALLIND", null, ["register:0:8"]]
- 00ae7e8c bytes 00013fd6
- 00ae7eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7eb8 ["INT_ADD", "register:40f0:8", ["const:ae7eb8:8", "const:4:8"]]
- 00ae7eb8 ["CALLIND", null, ["register:0:8"]]
- 00ae7eb8 bytes 00013fd6
- 00ae7ed4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7ed4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
- 00ae7ed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47c58 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47c58 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:488:8"]]
+ 00b47c58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7ed4 bytes a0221739
+ 00b47c58 bytes a0221239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8615cc4ed4612b1cbd9c59f1380f0e79"></a>

### [`00ae7ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md) → [`00b47c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47c6c.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 16.67% / 新版 20.00%

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
      "site": "00ae7f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae7f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47ca8"
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
      "00b47c80",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae7f78"
      ]
    ],
    [
      "00b47c8c",
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47c80",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47c84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47cfc"
      ]
    ],
    [
      "00b47c8c",
      "READ",
      [
        "storage",
        "01125488",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md#insn-00ae7f00) · [`00ae7f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md#insn-00ae7f20) · [`00ae7f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md#insn-00ae7f24)
- 新版 `00b47c84`（命令位置の公開資料なし）

~~~diff
- 00ae7f00 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae7f00 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00b47c84 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b47c84 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae7f00 bytes c10300b4
+ 00b47c84 bytes c10300b4
- 00ae7f20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7f20 ["INT_ADD", "register:40f0:8", ["const:ae7f20:8", "const:4:8"]]
- 00ae7f20 ["CALLIND", null, ["register:0:8"]]
- 00ae7f20 bytes 00013fd6
- 00ae7f24 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7f24 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
- 00ae7f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7f24 bytes bf221739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45db51fdcd784d4afa14d350653cd3b9"></a>

### [`00ae7f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md) → [`00b47d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d0c.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00b47d4c",
      "incomplete_value": true,
      "site": "00b47d4c",
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
      "definition_site": "00ae7fc8",
      "incomplete_value": true,
      "site": "00ae7fc8",
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
      "definition_site": "00b47d28",
      "incomplete_value": true,
      "site": "00b47d28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7fa4",
      "incomplete_value": true,
      "site": "00ae7fa4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b47d30",
      "incomplete_value": false,
      "site": "00b47d44",
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
            "const:32f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7fac",
      "incomplete_value": false,
      "site": "00ae7fc0",
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
      "00b47d20",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d30",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00b47d4c",
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
      "00b47d20",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d30",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ],
    [
      "00b47d4c",
      "WRITE",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md#insn-00ae7fc0) · [`00ae7fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md#insn-00ae7fc8) · [`00ae7f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md#insn-00ae7f94)
- 新版 `00b47d44`（命令位置の公開資料なし） · `00b47d4c`（命令位置の公開資料なし） · `00b47d18`（命令位置の公開資料なし）

~~~diff
- 00ae7fc0 ["INT_ADD", "register:40f0:8", ["const:ae7fc0:8", "const:4:8"]]
- 00ae7fc0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47d44 ["INT_ADD", "register:40f0:8", ["const:b47d44:8", "const:4:8"]]
+ 00b47d44 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae7fc0 bytes 34d80394
+ 00b47d44 bytes 734b0494
- 00ae7fc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae7fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47d4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
+ 00b47d4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7fc8 bytes 80e202f9
+ 00b47d4c bytes 804202f9
- 00ae7f94 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b47d18 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae7f94 bytes d42d00b0
+ 00b47d18 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-924be131d07652087dd54e711d3a1097"></a>

### [`00ae7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md) → [`00b47d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47d7c.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde440.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5aec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aec0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b47d98",
      "incomplete_value": false,
      "site": "00b47d9c",
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
    "old": {
      "definition_site": "00ae8014",
      "incomplete_value": false,
      "site": "00ae8018",
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
      "definition_site": "00b47da8",
      "incomplete_value": true,
      "site": "00b47db4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8024",
      "incomplete_value": true,
      "site": "00ae8030",
      "value": [
        "LOAD",
        "8",
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
      "00b47d98",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b47da8",
      "DATA",
      [
        "storage",
        "010a05d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47d98",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b47da8",
      "DATA",
      [
        "storage",
        "01125490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md#insn-00ae8018) · [`00ae8010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md#insn-00ae8010) · [`00ae8014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md#insn-00ae8014)
- 新版 `00b47d9c`（命令位置の公開資料なし） · `00b47d94`（命令位置の公開資料なし） · `00b47d98`（命令位置の公開資料なし）

~~~diff
- 00ae8018 ["INT_ADD", "register:40f0:8", ["const:ae8018:8", "const:4:8"]]
- 00ae8018 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b47d9c ["INT_ADD", "register:40f0:8", ["const:b47d9c:8", "const:4:8"]]
+ 00b47d9c ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae8018 bytes 5ad80394
+ 00b47d9c bytes 994b0494
- 00ae8010 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b47d94 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae8010 bytes 80bdff90
+ 00b47d94 bytes 00bbffb0
- 00ae8014 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae8014 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8014 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8014 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47d98 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b47d98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47d98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47d98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae8014 bytes 001c1591
+ 00b47d98 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-283758e0ec9b6f59d93059f9755f7639"></a>

### [`00ae8034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md) → [`00b47db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47db8.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47df8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8050"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8048",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47dfc"
      ]
    ],
    [
      "unmatched:00ae8058",
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
      "00b47dcc",
      "READ",
      [
        "storage",
        "01125480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47dd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47dfc"
      ]
    ],
    [
      "00b47ddc",
      "PARAM",
      [
        "storage",
        "002a832f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md#insn-00ae8050) · [`00ae806c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md#insn-00ae806c) · [`00ae8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md#insn-00ae8074)
- 新版 `00b47df0`（命令位置の公開資料なし）

~~~diff
- 00ae8050 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8050 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8050 bytes 410100b5
- 00ae806c ["INT_ADD", "register:40f0:8", ["const:ae806c:8", "const:4:8"]]
- 00ae806c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47df0 ["INT_ADD", "register:40f0:8", ["const:b47df0:8", "const:4:8"]]
+ 00b47df0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae806c bytes 09d80394
+ 00b47df0 bytes 484b0494
- 00ae8074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00ae8074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8074 bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2df060556d4b9e5e89451e3d8b148f98"></a>

### [`00ae8120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md) → [`00b47ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ea4.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae814c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47ed0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47eb8",
      "incomplete_value": true,
      "site": "00b47eb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8134",
      "incomplete_value": true,
      "site": "00ae8134",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b47eb4",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae813c",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae8144",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b47eb4",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ec0",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      "00b47ec8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md#insn-00ae8134) · [`00ae8144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md#insn-00ae8144) · [`00ae814c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md#insn-00ae814c)
- 新版 `00b47eb8`（命令位置の公開資料なし）

~~~diff
- 00ae8134 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8134 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b47eb8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47eb8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8134 bytes e80000b5
+ 00b47eb8 bytes e80000b5
- 00ae8144 ["INT_ADD", "register:40f0:8", ["const:ae8144:8", "const:4:8"]]
- 00ae8144 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8144 bytes d3d70394
- 00ae814c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae814c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae814c bytes 60f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d67328caae280ca70b493933e19d009"></a>

### [`00ae8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md) → [`00b47ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47ee4.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8190"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47f14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47ef8",
      "incomplete_value": true,
      "site": "00b47ef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b47ef4",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8194"
      ]
    ],
    [
      "unmatched:00ae8180",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b47ef4",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b47f18"
      ]
    ],
    [
      "00b47f04",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md#insn-00ae8174) · [`00ae8188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md#insn-00ae8188) · [`00ae8190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md#insn-00ae8190)
- 新版 `00b47ef8`（命令位置の公開資料なし）

~~~diff
- 00ae8174 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8174 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47ef8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47ef8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8174 bytes 080100b5
+ 00b47ef8 bytes 080100b5
- 00ae8188 ["INT_ADD", "register:40f0:8", ["const:ae8188:8", "const:4:8"]]
- 00ae8188 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8188 bytes c2d70394
- 00ae8190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae8190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8190 bytes 60f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87228aee2df4386cdcbad8a2748e846b"></a>

### [`00ae81a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md) → [`00b47f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f28.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae81d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b47f58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47f3c",
      "incomplete_value": true,
      "site": "00b47f3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae81b8",
      "incomplete_value": true,
      "site": "00ae81b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b47f38",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae81c0",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae81d4",
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
      "00b47f38",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47f44",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      "00b47f58",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae81b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md#insn-00ae81b8) · [`00ae81cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md#insn-00ae81cc) · [`00ae81d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md#insn-00ae81d4)
- 新版 `00b47f3c`（命令位置の公開資料なし） · `00b47f50`（命令位置の公開資料なし）

~~~diff
- 00ae81b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae81b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b47f3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b47f3c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae81b8 bytes 080100b5
+ 00b47f3c bytes 080100b5
- 00ae81cc ["INT_ADD", "register:40f0:8", ["const:ae81cc:8", "const:4:8"]]
- 00ae81cc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b47f50 ["INT_ADD", "register:40f0:8", ["const:b47f50:8", "const:4:8"]]
+ 00b47f50 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae81cc bytes b1d70394
+ 00b47f50 bytes f04a0494
- 00ae81d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
- 00ae81d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae81d4 bytes 60f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ece1041ea96460aa6ece8c45eb4ca5"></a>

### [`00ae81f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md) → [`00b47f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b47/00b47f78.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b48000",
      "incomplete_value": true,
      "site": "00b48000",
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
      "definition_site": "00ae827c",
      "incomplete_value": true,
      "site": "00ae827c",
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
      "definition_site": "00b47fac",
      "incomplete_value": true,
      "site": "00b47fb8",
      "value": [
        "LOAD",
        "8",
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
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8228",
      "incomplete_value": true,
      "site": "00ae8234",
      "value": [
        "LOAD",
        "8",
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
      "00b47f8c",
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47fac",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48000",
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
      "00b47f8c",
      "READ",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47fac",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48000",
      "WRITE",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md#insn-00ae8234) · [`00ae827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md#insn-00ae827c) · [`00ae8204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md#insn-00ae8204)
- 新版 `00b47fb8`（命令位置の公開資料なし） · `00b48000`（命令位置の公開資料なし） · `00b47f88`（命令位置の公開資料なし）

~~~diff
- 00ae8234 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8234 ["INT_ADD", "register:40f0:8", ["const:ae8234:8", "const:4:8"]]
- 00ae8234 ["CALLIND", null, ["register:0:8"]]
+ 00b47fb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47fb8 ["INT_ADD", "register:40f0:8", ["const:b47fb8:8", "const:4:8"]]
+ 00b47fb8 ["CALLIND", null, ["register:0:8"]]
- 00ae8234 bytes 00013fd6
+ 00b47fb8 bytes 00013fd6
- 00ae827c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae827c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae827c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48000 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48000 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4b0:8"]]
+ 00b48000 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae827c bytes a0c21739
+ 00b48000 bytes a0c21239
- 00ae8204 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b47f88 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00ae8204 bytes d52d0090
+ 00b47f88 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-729396ad1bb31d59b7c1beedbb0403b0"></a>

### [`00ae8290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md) → [`00b48014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48014.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b48050",
      "incomplete_value": true,
      "site": "00b48050",
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
      "definition_site": "00ae82cc",
      "incomplete_value": true,
      "site": "00ae82cc",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b480a0",
      "incomplete_value": true,
      "site": "00b480a0",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae831c",
      "incomplete_value": true,
      "site": "00ae831c",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4802c",
      "incomplete_value": true,
      "site": "00b4802c",
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
      "definition_site": "00ae82a8",
      "incomplete_value": true,
      "site": "00ae82a8",
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
      "00b48028",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48034",
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48050",
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
      "00b48028",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48034",
      "READ",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48050",
      "WRITE",
      [
        "storage",
        "011254b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae82cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md#insn-00ae82cc) · [`00ae8318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md#insn-00ae8318) · [`00ae831c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md#insn-00ae831c)
- 新版 `00b48050`（命令位置の公開資料なし） · `00b4809c`（命令位置の公開資料なし） · `00b480a0`（命令位置の公開資料なし）

~~~diff
- 00ae82cc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae82cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae82cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5f0:8"]]
- 00ae82cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48050 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48050 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48050 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
+ 00b48050 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae82cc bytes bfc21739
+ 00b48050 bytes bfc21239
- 00ae8318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8318 ["INT_ADD", "register:40f0:8", ["const:ae8318:8", "const:4:8"]]
- 00ae8318 ["CALLIND", null, ["register:0:8"]]
+ 00b4809c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4809c ["INT_ADD", "register:40f0:8", ["const:b4809c:8", "const:4:8"]]
+ 00b4809c ["CALLIND", null, ["register:0:8"]]
- 00ae8318 bytes 00013fd6
+ 00b4809c bytes 00013fd6
- 00ae831c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae831c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae831c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b480a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00b480a0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b480a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae831c bytes 9ff602f9
+ 00b480a0 bytes 9f5602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f520d9a5bdb690f6e6de17343705527c"></a>

### [`00ae8330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md) → [`00b480b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b480b4.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

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
      "definition_site": "00b480f4",
      "incomplete_value": true,
      "site": "00b480f4",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8370",
      "incomplete_value": true,
      "site": "00ae8370",
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
      "definition_site": "00b480d0",
      "incomplete_value": true,
      "site": "00b480d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae834c",
      "incomplete_value": true,
      "site": "00ae834c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b480d8",
      "incomplete_value": false,
      "site": "00b480ec",
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
            "const:95b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8354",
      "incomplete_value": false,
      "site": "00ae8368",
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
            "const:c92:8"
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
      "00b480c8",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b480d8",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00b480f4",
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
      "00b480c8",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b480d8",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ],
    [
      "00b480f4",
      "WRITE",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md#insn-00ae8368) · [`00ae8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md#insn-00ae8370) · [`00ae833c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md#insn-00ae833c)
- 新版 `00b480ec`（命令位置の公開資料なし） · `00b480f4`（命令位置の公開資料なし） · `00b480c0`（命令位置の公開資料なし）

~~~diff
- 00ae8368 ["INT_ADD", "register:40f0:8", ["const:ae8368:8", "const:4:8"]]
- 00ae8368 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b480ec ["INT_ADD", "register:40f0:8", ["const:b480ec:8", "const:4:8"]]
+ 00b480ec ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8368 bytes 4ad70394
+ 00b480ec bytes 894a0494
- 00ae8370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae8370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b480f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00b480f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8370 bytes 80f602f9
+ 00b480f4 bytes 805602f9
- 00ae833c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b480c0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae833c bytes d42d0090
+ 00b480c0 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b6a1bb825d76b93ea176c271395d05c"></a>

### [`00ae83dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md) → [`00b48160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48160.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 20.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae841c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b481a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae83f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae83f0",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae83f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b481a4"
      ]
    ],
    [
      "unmatched:00ae8400",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48174",
      "READ",
      [
        "storage",
        "011254a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4817c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b481a4"
      ]
    ],
    [
      "00b48184",
      "PARAM",
      [
        "storage",
        "002b995b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae83f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md#insn-00ae83f8) · [`00ae8414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md#insn-00ae8414) · [`00ae841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md#insn-00ae841c)
- 新版 `00b48198`（命令位置の公開資料なし）

~~~diff
- 00ae83f8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae83f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae83f8 bytes 410100b5
- 00ae8414 ["INT_ADD", "register:40f0:8", ["const:ae8414:8", "const:4:8"]]
- 00ae8414 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48198 ["INT_ADD", "register:40f0:8", ["const:b48198:8", "const:4:8"]]
+ 00b48198 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8414 bytes 1fd70394
+ 00b48198 bytes 5e4a0494
- 00ae841c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
- 00ae841c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae841c bytes 80f602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9ac53b7f3e105c3ebd9e93bfb87004a"></a>

### [`00ae844c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md) → [`00b481d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b481d0.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

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
      "site": "00ae8460"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b481e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b481ec",
      "incomplete_value": false,
      "site": "00b481f0",
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
    "old": {
      "definition_site": "00ae8468",
      "incomplete_value": false,
      "site": "00ae846c",
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
      "unmatched:00ae8460",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b481f4"
      ]
    ],
    [
      "00b481ec",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b481fc",
      "DATA",
      [
        "storage",
        "010a0640",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b481e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b481f4"
      ]
    ],
    [
      "00b481ec",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b481fc",
      "DATA",
      [
        "storage",
        "01125500",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md#insn-00ae8460) · [`00ae846c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md#insn-00ae846c)
- 新版 `00b481f0`（命令位置の公開資料なし） · `00b481e4`（命令位置の公開資料なし）

~~~diff
- 00ae8460 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae8460 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae8460 bytes 8b000054
- 00ae846c ["INT_ADD", "register:40f0:8", ["const:ae846c:8", "const:4:8"]]
- 00ae846c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b481f0 ["INT_ADD", "register:40f0:8", ["const:b481f0:8", "const:4:8"]]
+ 00b481f0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae846c bytes 45d70394
+ 00b481f0 bytes 844a0494
+ 00b481e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b481e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b481e4 bytes 8b000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c128928d2e4e417d3e2476d365785270"></a>

### [`00ae8488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md) → [`00b4820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4820c.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b48238",
      "incomplete_value": true,
      "site": "00b48238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84b4",
      "incomplete_value": true,
      "site": "00ae84b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00b48220",
      "incomplete_value": true,
      "site": "00b48220",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae849c",
      "incomplete_value": true,
      "site": "00ae849c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4822c",
      "incomplete_value": false,
      "site": "00b48230",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84a8",
      "incomplete_value": false,
      "site": "00ae84ac",
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
            "const:459:8"
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
      "00b4821c",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4822c",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00b48238",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4821c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4822c",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "00b48238",
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae84ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md#insn-00ae84ac) · [`00ae84b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md#insn-00ae84b4) · [`00ae8494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md#insn-00ae8494)
- 新版 `00b48230`（命令位置の公開資料なし） · `00b48238`（命令位置の公開資料なし） · `00b48218`（命令位置の公開資料なし）

~~~diff
- 00ae84ac ["INT_ADD", "register:40f0:8", ["const:ae84ac:8", "const:4:8"]]
- 00ae84ac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48230 ["INT_ADD", "register:40f0:8", ["const:b48230:8", "const:4:8"]]
+ 00b48230 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae84ac bytes f9d60394
+ 00b48230 bytes 384a0494
- 00ae84b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae84b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48238 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b48238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae84b4 bytes 602603f9
+ 00b48238 bytes 608602f9
- 00ae8494 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b48218 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae8494 bytes d32d0090
+ 00b48218 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87f158bb37b77c81f6c12cb8f243370f"></a>

### [`00ae84c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md) → [`00b4824c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4824c.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b48278",
      "incomplete_value": true,
      "site": "00b48278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84f4",
      "incomplete_value": true,
      "site": "00ae84f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00b48260",
      "incomplete_value": true,
      "site": "00b48260",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84dc",
      "incomplete_value": true,
      "site": "00ae84dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b48268",
      "incomplete_value": false,
      "site": "00b48270",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae84e4",
      "incomplete_value": false,
      "site": "00ae84ec",
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
            "const:459:8"
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
      "00b4825c",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48268",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00b48278",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4825c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48268",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "00b48278",
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae84ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md#insn-00ae84ec) · [`00ae84f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md#insn-00ae84f4) · [`00ae84d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae84c8.md#insn-00ae84d4)
- 新版 `00b48270`（命令位置の公開資料なし） · `00b48278`（命令位置の公開資料なし） · `00b48258`（命令位置の公開資料なし）

~~~diff
- 00ae84ec ["INT_ADD", "register:40f0:8", ["const:ae84ec:8", "const:4:8"]]
- 00ae84ec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48270 ["INT_ADD", "register:40f0:8", ["const:b48270:8", "const:4:8"]]
+ 00b48270 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae84ec bytes e9d60394
+ 00b48270 bytes 284a0494
- 00ae84f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae84f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b48278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae84f4 bytes 602603f9
+ 00b48278 bytes 608602f9
- 00ae84d4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b48258 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae84d4 bytes d32d0090
+ 00b48258 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-967b5d39f87ee9ce36313de0158b0ea3"></a>

### [`00ae8508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md) → [`00b4828c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4828c.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b482bc",
      "incomplete_value": true,
      "site": "00b482bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8538",
      "incomplete_value": true,
      "site": "00ae8538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "definition_site": "00b482a0",
      "incomplete_value": true,
      "site": "00b482a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b482ac",
      "incomplete_value": false,
      "site": "00b482b4",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8528",
      "incomplete_value": false,
      "site": "00ae8530",
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
            "const:459:8"
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
      "00b4829c",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482ac",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00b482bc",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4829c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482ac",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ],
    [
      "00b482bc",
      "WRITE",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md#insn-00ae8530) · [`00ae8538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md#insn-00ae8538) · [`00ae8514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8508.md#insn-00ae8514)
- 新版 `00b482b4`（命令位置の公開資料なし） · `00b482bc`（命令位置の公開資料なし） · `00b48298`（命令位置の公開資料なし）

~~~diff
- 00ae8530 ["INT_ADD", "register:40f0:8", ["const:ae8530:8", "const:4:8"]]
- 00ae8530 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b482b4 ["INT_ADD", "register:40f0:8", ["const:b482b4:8", "const:4:8"]]
+ 00b482b4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8530 bytes d8d60394
+ 00b482b4 bytes 174a0494
- 00ae8538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
- 00ae8538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b482bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00b482bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8538 bytes 602603f9
+ 00b482bc bytes 608602f9
- 00ae8514 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b48298 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae8514 bytes d32d0090
+ 00b48298 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21be419c632b9d4d4aef0a34aa2a4a4"></a>

### [`00ae854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md) → [`00b482d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b482d0.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae854c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8550"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae854c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8550",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b482e0",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b482d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b482d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b482e0",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md#insn-00ae854c) · [`00ae8550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md#insn-00ae8550) · [`00ae8560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae854c.md#insn-00ae8560)
- 新版 `00b482e4`（命令位置の公開資料なし）

~~~diff
- 00ae854c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae854c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae854c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae854c bytes f30f1ef8
- 00ae8550 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8550 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8550 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8550 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8550 bytes fd7b01a9
- 00ae8560 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8560 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b482e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b482e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8560 bytes 080100b5
+ 00b482e4 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7060264517871b780b33ad2909ff549"></a>

### [`00ae8638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md) → [`00b483bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b483bc.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 4件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae86c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b483f8"
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
      "00b483d0",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00b483dc",
      "READ",
      [
        "storage",
        "010a0650",
        null,
        "undefined1"
      ]
    ],
    [
      "00b483e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8678"
      ]
    ]
  ],
  "added": [
    [
      "00b483d0",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b483dc",
      "READ",
      [
        "storage",
        "01125510",
        null,
        "undefined1"
      ]
    ],
    [
      "00b483e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b483fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md#insn-00ae8650) · [`00ae8674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md#insn-00ae8674) · [`00ae8684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8638.md#insn-00ae8684)
- 新版 `00b483d4`（命令位置の公開資料なし）

~~~diff
- 00ae8650 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8650 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b483d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b483d4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae8650 bytes c10300b4
+ 00b483d4 bytes c10300b4
- 00ae8674 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae8674 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae8674 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:650:8"]]
- 00ae8674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae8674 bytes bf421939
- 00ae8684 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae8684 ["INT_ADD", "register:40f0:8", ["const:ae8684:8", "const:4:8"]]
- 00ae8684 ["CALLIND", null, ["register:0:8"]]
- 00ae8684 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b85880f3daccfcb888a75cda5f15f0"></a>

### [`00ae86d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md) → [`00b4845c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4845c.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae8718"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4849c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae86f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae86ec",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae86f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b484a0"
      ]
    ],
    [
      "unmatched:00ae86fc",
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
      "00b48470",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b484a0"
      ]
    ],
    [
      "00b48480",
      "PARAM",
      [
        "storage",
        "002a5f6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae86f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md#insn-00ae86f4) · [`00ae8710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md#insn-00ae8710) · [`00ae8718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae86d8.md#insn-00ae8718)
- 新版 `00b48494`（命令位置の公開資料なし）

~~~diff
- 00ae86f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae86f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae86f4 bytes 410100b5
- 00ae8710 ["INT_ADD", "register:40f0:8", ["const:ae8710:8", "const:4:8"]]
- 00ae8710 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48494 ["INT_ADD", "register:40f0:8", ["const:b48494:8", "const:4:8"]]
+ 00b48494 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8710 bytes 60d60394
+ 00b48494 bytes 9f490494
- 00ae8718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
- 00ae8718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8718 bytes 802603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c137d00428f6839caedf2507a408e19b"></a>

### [`00ae8784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md) → [`00b48508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48508.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8788"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8784",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8788",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8798",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4850c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4851c",
      "READ",
      [
        "storage",
        "01125508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md#insn-00ae8784) · [`00ae8788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md#insn-00ae8788) · [`00ae87a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8784.md#insn-00ae87a0)

~~~diff
- 00ae8784 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae8784 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae8784 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8784 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8784 bytes f44fbea9
- 00ae8788 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8788 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8788 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8788 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8788 bytes fd7b01a9
- 00ae87a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae87a0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00ae87a0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2f2f4025976d7e9f79a545930c2b290"></a>

### [`00ae8870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md) → [`00b485f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b485f4.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8874"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8870",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae8874",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48604",
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
      "00b485f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b485f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b48604",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md#insn-00ae8870) · [`00ae8874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md#insn-00ae8874) · [`00ae8884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8870.md#insn-00ae8884)
- 新版 `00b48608`（命令位置の公開資料なし）

~~~diff
- 00ae8870 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ae8870 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ae8870 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae8870 bytes f30f1ef8
- 00ae8874 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae8874 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae8874 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae8874 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae8874 bytes fd7b01a9
- 00ae8884 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8884 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b48608 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b48608 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8884 bytes e80000b5
+ 00b48608 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8ea9543cf44b8b2525641303390fb1"></a>

### [`00ae88f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md) → [`00b48678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48678.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 40.00% / 新版 50.00%

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
      "site": "00ae8924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b486a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4868c",
      "incomplete_value": true,
      "site": "00b4868c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8908",
      "incomplete_value": true,
      "site": "00ae8908",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b48688",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8910",
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae8924",
      "WRITE",
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
      "00b48688",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48694",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ],
    [
      "00b486a8",
      "WRITE",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md#insn-00ae8908) · [`00ae891c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md#insn-00ae891c) · [`00ae8924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae88f4.md#insn-00ae8924)
- 新版 `00b4868c`（命令位置の公開資料なし） · `00b486a0`（命令位置の公開資料なし）

~~~diff
- 00ae8908 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae8908 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4868c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4868c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae8908 bytes 080100b5
+ 00b4868c bytes 080100b5
- 00ae891c ["INT_ADD", "register:40f0:8", ["const:ae891c:8", "const:4:8"]]
- 00ae891c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b486a0 ["INT_ADD", "register:40f0:8", ["const:b486a0:8", "const:4:8"]]
+ 00b486a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae891c bytes ddd50394
+ 00b486a0 bytes 1c490494
- 00ae8924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:670:8"]]
- 00ae8924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8924 bytes 603a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94457d4ac643056b010c31725eacca1"></a>

### [`00ae89e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md) → [`00b48764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48764.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.50% / 新版 67.50%

CFGの説明率　旧版 6.67% / 新版 11.11%

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
      "site": "00ae89e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae89e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae89e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae89e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae89e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae89e8",
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
      "00b48764",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b48768",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4876c",
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

- 旧版 [`00ae89e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md#insn-00ae89e0) · [`00ae89e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md#insn-00ae89e4) · [`00ae89e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae89e0.md#insn-00ae89e8)

~~~diff
- 00ae89e0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae89e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae89e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae89e0 bytes f50f1df8
- 00ae89e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae89e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae89e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae89e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae89e4 bytes f44f01a9
- 00ae89e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae89e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae89e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae89e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae89e8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06f1ee2d4721d2fedc356eba58413c34"></a>

### [`00ae8a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md) → [`00b48804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48804.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae8ac0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48844"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8a9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8a94",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8a9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48848"
      ]
    ],
    [
      "unmatched:00ae8aa4",
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48818",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48848"
      ]
    ],
    [
      "00b48828",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md#insn-00ae8a9c) · [`00ae8ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md#insn-00ae8ab8) · [`00ae8ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8a80.md#insn-00ae8ac0)
- 新版 `00b4883c`（命令位置の公開資料なし）

~~~diff
- 00ae8a9c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8a9c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae8a9c bytes 410100b5
- 00ae8ab8 ["INT_ADD", "register:40f0:8", ["const:ae8ab8:8", "const:4:8"]]
- 00ae8ab8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4883c ["INT_ADD", "register:40f0:8", ["const:b4883c:8", "const:4:8"]]
+ 00b4883c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8ab8 bytes 76d50394
+ 00b4883c bytes b5480494
- 00ae8ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
- 00ae8ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8ac0 bytes 803a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6accd49e658a5a3e169aa5056b9fb8f4"></a>

### [`00ae8b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md) → [`00b488b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b488b0.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae8b6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b488f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8b48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8b40",
      "READ",
      [
        "storage",
        "010a0670",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8b48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b488f4"
      ]
    ],
    [
      "unmatched:00ae8b50",
      "PARAM",
      [
        "storage",
        "002aaff0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b488c4",
      "READ",
      [
        "storage",
        "01125530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b488cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b488f4"
      ]
    ],
    [
      "00b488d4",
      "PARAM",
      [
        "storage",
        "002bbdb9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md#insn-00ae8b48) · [`00ae8b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md#insn-00ae8b64) · [`00ae8b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8b2c.md#insn-00ae8b6c)
- 新版 `00b488e8`（命令位置の公開資料なし）

~~~diff
- 00ae8b48 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8b48 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae8b48 bytes 410100b5
- 00ae8b64 ["INT_ADD", "register:40f0:8", ["const:ae8b64:8", "const:4:8"]]
- 00ae8b64 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b488e8 ["INT_ADD", "register:40f0:8", ["const:b488e8:8", "const:4:8"]]
+ 00b488e8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8b64 bytes 4bd50394
+ 00b488e8 bytes 8a480494
- 00ae8b6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:670:8"]]
- 00ae8b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8b6c bytes 803a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39954deb67958f76836ad7968dce7a47"></a>

### [`00ae8bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md) → [`00b4895c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b4895c.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8c04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48988"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48970",
      "incomplete_value": true,
      "site": "00b48970",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8bec",
      "incomplete_value": true,
      "site": "00ae8bec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b4896c",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48970",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8c08"
      ]
    ],
    [
      "unmatched:00ae8bf8",
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
      "00b4896c",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48970",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4898c"
      ]
    ],
    [
      "00b4897c",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md#insn-00ae8bfc) · [`00ae8c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md#insn-00ae8c04) · [`00ae8c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8bd8.md#insn-00ae8c14)

~~~diff
- 00ae8bfc ["INT_ADD", "register:40f0:8", ["const:ae8bfc:8", "const:4:8"]]
- 00ae8bfc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8bfc bytes 25d50394
- 00ae8c04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00ae8c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8c04 bytes 604e03f9
- 00ae8c14 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae8c14 ["RETURN", null, ["register:0:8"]]
- 00ae8c14 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc52e53de81829a521c08b4a9801b73"></a>

### [`00ae8c9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md) → [`00b48a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a20.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48a50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48a34",
      "incomplete_value": true,
      "site": "00b48a34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8cb0",
      "incomplete_value": true,
      "site": "00ae8cb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b48a30",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8cd0"
      ]
    ],
    [
      "unmatched:00ae8cb8",
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
      "00b48a30",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48a54"
      ]
    ],
    [
      "00b48a3c",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md#insn-00ae8cc4) · [`00ae8ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md#insn-00ae8ccc) · [`00ae8cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8c9c.md#insn-00ae8cdc)
- 新版 `00b48a48`（命令位置の公開資料なし）

~~~diff
- 00ae8cc4 ["INT_ADD", "register:40f0:8", ["const:ae8cc4:8", "const:4:8"]]
- 00ae8cc4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48a48 ["INT_ADD", "register:40f0:8", ["const:b48a48:8", "const:4:8"]]
+ 00b48a48 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8cc4 bytes f3d40394
+ 00b48a48 bytes 32480494
- 00ae8ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:698:8"]]
- 00ae8ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8ccc bytes 604e03f9
- 00ae8cdc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae8cdc ["RETURN", null, ["register:0:8"]]
- 00ae8cdc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e87c8c959e8f21a7fc8d038381361f31"></a>

### [`00ae8e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md) → [`00b48bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48bac.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48bec",
      "incomplete_value": true,
      "site": "00b48bec",
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
            "const:558:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e68",
      "incomplete_value": true,
      "site": "00ae8e68",
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
            "const:698:8"
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
      "definition_site": "00b48bc8",
      "incomplete_value": true,
      "site": "00b48bc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8e44",
      "incomplete_value": true,
      "site": "00ae8e44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00ae8e50",
      "incomplete_value": true,
      "site": "00ae8e60",
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
      "00b48bc0",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8e4c",
      "PARAM",
      [
        "storage",
        "002985ee",
        null,
        "string"
      ]
    ],
    [
      "00b48bec",
      "WRITE",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48bc0",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48bd0",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ],
    [
      "00b48bec",
      "WRITE",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md#insn-00ae8e60) · [`00ae8e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md#insn-00ae8e68) · [`00ae8e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8e28.md#insn-00ae8e34)
- 新版 `00b48be4`（命令位置の公開資料なし） · `00b48bec`（命令位置の公開資料なし） · `00b48bb8`（命令位置の公開資料なし）

~~~diff
- 00ae8e60 ["INT_ADD", "register:40f0:8", ["const:ae8e60:8", "const:4:8"]]
- 00ae8e60 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48be4 ["INT_ADD", "register:40f0:8", ["const:b48be4:8", "const:4:8"]]
+ 00b48be4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8e60 bytes 8cd40394
+ 00b48be4 bytes cb470494
- 00ae8e68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00ae8e68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48bec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:558:8"]]
+ 00b48bec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8e68 bytes 804e03f9
+ 00b48bec bytes 80ae02f9
- 00ae8e34 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b48bb8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae8e34 bytes d42d0090
+ 00b48bb8 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aae4b8839aa14bff50228c036d97364"></a>

### [`00ae8ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md) → [`00b48c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48c58.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48c98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae8ef0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae8ee8",
      "READ",
      [
        "storage",
        "010a0698",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae8ef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48c9c"
      ]
    ],
    [
      "unmatched:00ae8ef8",
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
      "00b48c6c",
      "READ",
      [
        "storage",
        "01125558",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48c9c"
      ]
    ],
    [
      "00b48c7c",
      "PARAM",
      [
        "storage",
        "002a8341",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md#insn-00ae8ef0) · [`00ae8f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md#insn-00ae8f0c) · [`00ae8f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8ed4.md#insn-00ae8f14)
- 新版 `00b48c90`（命令位置の公開資料なし）

~~~diff
- 00ae8ef0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae8ef0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae8ef0 bytes 410100b5
- 00ae8f0c ["INT_ADD", "register:40f0:8", ["const:ae8f0c:8", "const:4:8"]]
- 00ae8f0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48c90 ["INT_ADD", "register:40f0:8", ["const:b48c90:8", "const:4:8"]]
+ 00b48c90 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8f0c bytes 61d40394
+ 00b48c90 bytes a0470494
- 00ae8f14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:698:8"]]
- 00ae8f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8f14 bytes 804e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa610ae97cc34a0c3734498927860904"></a>

### [`00ae8f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md) → [`00b48d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d04.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b48d30",
      "incomplete_value": true,
      "site": "00b48d30",
      "value": [
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
      "definition_site": "00ae8fac",
      "incomplete_value": true,
      "site": "00ae8fac",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48d18",
      "incomplete_value": true,
      "site": "00b48d18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8f94",
      "incomplete_value": true,
      "site": "00ae8f94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b48d24",
      "incomplete_value": false,
      "site": "00b48d28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:2ff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8fa0",
      "incomplete_value": false,
      "site": "00ae8fa4",
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
            "const:edc:8"
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
      "00b48d14",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d24",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00b48d30",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48d14",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d24",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      "00b48d30",
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md#insn-00ae8fa4) · [`00ae8fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md#insn-00ae8fac) · [`00ae8f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8f80.md#insn-00ae8f8c)
- 新版 `00b48d28`（命令位置の公開資料なし） · `00b48d30`（命令位置の公開資料なし） · `00b48d10`（命令位置の公開資料なし）

~~~diff
- 00ae8fa4 ["INT_ADD", "register:40f0:8", ["const:ae8fa4:8", "const:4:8"]]
- 00ae8fa4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48d28 ["INT_ADD", "register:40f0:8", ["const:b48d28:8", "const:4:8"]]
+ 00b48d28 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8fa4 bytes 3bd40394
+ 00b48d28 bytes 7a470494
- 00ae8fac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae8fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48d30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00b48d30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8fac bytes 606203f9
+ 00b48d30 bytes 60c202f9
- 00ae8f8c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b48d10 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae8f8c bytes d32d0090
+ 00b48d10 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50c9c102662fd0f81bca773aba5b5472"></a>

### [`00ae8fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md) → [`00b48d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48d44.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae8fec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48d70"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48d58",
      "incomplete_value": true,
      "site": "00b48d58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8fd4",
      "incomplete_value": true,
      "site": "00ae8fd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b48d54",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae8ff0"
      ]
    ],
    [
      "unmatched:00ae8fdc",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48d54",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48d74"
      ]
    ],
    [
      "00b48d60",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md#insn-00ae8fe4) · [`00ae8fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md#insn-00ae8fec) · [`00ae8ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8fc0.md#insn-00ae8ffc)

~~~diff
- 00ae8fe4 ["INT_ADD", "register:40f0:8", ["const:ae8fe4:8", "const:4:8"]]
- 00ae8fe4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae8fe4 bytes 2bd40394
- 00ae8fec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae8fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8fec bytes 606203f9
- 00ae8ffc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae8ffc ["RETURN", null, ["register:0:8"]]
- 00ae8ffc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ac7a08031bcc17edb1a6376c39412d"></a>

### [`00ae9044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md) → [`00b48dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48dc8.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b48df8",
      "incomplete_value": true,
      "site": "00b48df8",
      "value": [
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
      "definition_site": "00ae9074",
      "incomplete_value": true,
      "site": "00ae9074",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48ddc",
      "incomplete_value": true,
      "site": "00b48ddc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9058",
      "incomplete_value": true,
      "site": "00ae9058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b48de4",
      "incomplete_value": false,
      "site": "00b48df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:2ff:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9060",
      "incomplete_value": false,
      "site": "00ae906c",
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
            "const:edc:8"
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
      "00b48dd8",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48de4",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ],
    [
      "00b48df8",
      "WRITE",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48dd8",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48de4",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ],
    [
      "00b48df8",
      "WRITE",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae906c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md#insn-00ae906c) · [`00ae9074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md#insn-00ae9074) · [`00ae9050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9044.md#insn-00ae9050)
- 新版 `00b48df0`（命令位置の公開資料なし） · `00b48df8`（命令位置の公開資料なし） · `00b48dd4`（命令位置の公開資料なし）

~~~diff
- 00ae906c ["INT_ADD", "register:40f0:8", ["const:ae906c:8", "const:4:8"]]
- 00ae906c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48df0 ["INT_ADD", "register:40f0:8", ["const:b48df0:8", "const:4:8"]]
+ 00b48df0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae906c bytes 09d40394
+ 00b48df0 bytes 48470494
- 00ae9074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00ae9074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
+ 00b48df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9074 bytes 606203f9
+ 00b48df8 bytes 60c202f9
- 00ae9050 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b48dd4 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae9050 bytes b32d00f0
+ 00b48dd4 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec9654ce2961921a30ed1c57e6dfd658"></a>

### [`00ae9094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9094.md) → [`00b48e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48e18.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

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
      "definition_site": "00b48ea0",
      "incomplete_value": true,
      "site": "00b48ea0",
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
      "definition_site": "00ae911c",
      "incomplete_value": true,
      "site": "00ae911c",
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
            "const:6c8:8"
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
      "site": "00ae90d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b48e58"
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
      "00b48e2c",
      "READ",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae90c8",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ea0",
      "WRITE",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48e2c",
      "READ",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48e4c",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ea0",
      "WRITE",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae90d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9094.md#insn-00ae90d4) · [`00ae911c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9094.md#insn-00ae911c)
- 新版 `00b48ea0`（命令位置の公開資料なし） · `00b48e58`（命令位置の公開資料なし）

~~~diff
- 00ae90d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae90d4 ["INT_ADD", "register:40f0:8", ["const:ae90d4:8", "const:4:8"]]
- 00ae90d4 ["CALLIND", null, ["register:0:8"]]
- 00ae90d4 bytes 00013fd6
- 00ae911c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae911c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
- 00ae911c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48ea0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48ea0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:588:8"]]
+ 00b48ea0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae911c bytes a0221b39
+ 00b48ea0 bytes a0221639
+ 00b48e58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48e58 ["INT_ADD", "register:40f0:8", ["const:b48e58:8", "const:4:8"]]
+ 00b48e58 ["CALLIND", null, ["register:0:8"]]
+ 00b48e58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-982f500a7dd2fb6312e15e3dc037bd9f"></a>

### [`00ae9130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md) → [`00b48eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48eb4.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 27.27% / 新版 33.33%

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
      "site": "00ae916c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48f40",
      "incomplete_value": true,
      "site": "00b48f40",
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
      "definition_site": "00ae91bc",
      "incomplete_value": true,
      "site": "00ae91bc",
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
            "const:6c0:8"
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
      "site": "00b48ef0"
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
      "00b48ec8",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ed4",
      "READ",
      [
        "storage",
        "010a06c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48edc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae9170"
      ]
    ]
  ],
  "added": [
    [
      "00b48ec8",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ed4",
      "READ",
      [
        "storage",
        "01125588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48edc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48ef4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md#insn-00ae9148) · [`00ae916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md#insn-00ae916c) · [`00ae917c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9130.md#insn-00ae917c)
- 新版 `00b48ecc`（命令位置の公開資料なし）

~~~diff
- 00ae9148 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9148 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b48ecc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b48ecc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae9148 bytes c10300b4
+ 00b48ecc bytes c10300b4
- 00ae916c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae916c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae916c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
- 00ae916c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae916c bytes bf221b39
- 00ae917c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae917c ["INT_ADD", "register:40f0:8", ["const:ae917c:8", "const:4:8"]]
- 00ae917c ["CALLIND", null, ["register:0:8"]]
- 00ae917c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e949767e221ea0afba00f8515d9fd6a2"></a>

### [`00ae91d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md) → [`00b48f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48f54.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae9210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b48f94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae91ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae91e4",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae91ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48f98"
      ]
    ],
    [
      "unmatched:00ae91f4",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b48f68",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b48f98"
      ]
    ],
    [
      "00b48f78",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae91ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md#insn-00ae91ec) · [`00ae9208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md#insn-00ae9208) · [`00ae9210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae91d0.md#insn-00ae9210)
- 新版 `00b48f8c`（命令位置の公開資料なし）

~~~diff
- 00ae91ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae91ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae91ec bytes 410100b5
- 00ae9208 ["INT_ADD", "register:40f0:8", ["const:ae9208:8", "const:4:8"]]
- 00ae9208 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b48f8c ["INT_ADD", "register:40f0:8", ["const:b48f8c:8", "const:4:8"]]
+ 00b48f8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9208 bytes a2d30394
+ 00b48f8c bytes e1460494
- 00ae9210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00ae9210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9210 bytes 806203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99800ac0c54b42da56643d291329a9d6"></a>

### [`00ae9240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md) → [`00b48fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48fc4.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b48fe0",
      "incomplete_value": false,
      "site": "00b48fe4",
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
    "old": {
      "definition_site": "00ae925c",
      "incomplete_value": false,
      "site": "00ae9260",
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
      "definition_site": "00b48ff0",
      "incomplete_value": true,
      "site": "00b48ffc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae926c",
      "incomplete_value": true,
      "site": "00ae9278",
      "value": [
        "LOAD",
        "8",
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
      "00b48fe0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b48ff0",
      "DATA",
      [
        "storage",
        "010a06d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48fe0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b48ff0",
      "DATA",
      [
        "storage",
        "01125590",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md#insn-00ae9260) · [`00ae9258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md#insn-00ae9258) · [`00ae925c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9240.md#insn-00ae925c)
- 新版 `00b48fe4`（命令位置の公開資料なし） · `00b48fdc`（命令位置の公開資料なし） · `00b48fe0`（命令位置の公開資料なし）

~~~diff
- 00ae9260 ["INT_ADD", "register:40f0:8", ["const:ae9260:8", "const:4:8"]]
- 00ae9260 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b48fe4 ["INT_ADD", "register:40f0:8", ["const:b48fe4:8", "const:4:8"]]
+ 00b48fe4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae9260 bytes c8d30394
+ 00b48fe4 bytes 07470494
- 00ae9258 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b48fdc ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae9258 bytes 60bdfff0
+ 00b48fdc bytes 00bbff90
- 00ae925c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae925c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae925c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae925c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48fe0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b48fe0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48fe0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48fe0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae925c bytes 001c1591
+ 00b48fe0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42d67c99efcab8778d095c11c905e8df"></a>

### [`00ae927c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md) → [`00b49000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49000.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae92bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49040"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9290",
      "READ",
      [
        "storage",
        "010a06c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9298",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49044"
      ]
    ],
    [
      "unmatched:00ae92a0",
      "PARAM",
      [
        "storage",
        "0029eedc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49014",
      "READ",
      [
        "storage",
        "01125580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4901c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49044"
      ]
    ],
    [
      "00b49024",
      "PARAM",
      [
        "storage",
        "002af2ff",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md#insn-00ae9298) · [`00ae92b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md#insn-00ae92b4) · [`00ae92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae927c.md#insn-00ae92bc)
- 新版 `00b49038`（命令位置の公開資料なし）

~~~diff
- 00ae9298 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9298 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9298 bytes 410100b5
- 00ae92b4 ["INT_ADD", "register:40f0:8", ["const:ae92b4:8", "const:4:8"]]
- 00ae92b4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49038 ["INT_ADD", "register:40f0:8", ["const:b49038:8", "const:4:8"]]
+ 00b49038 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae92b4 bytes 77d30394
+ 00b49038 bytes b6460494
- 00ae92bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00ae92bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae92bc bytes 806203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-194e87e22ab7b0fdaa9aa08b19b08041"></a>

### [`00ae9328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md) → [`00b490ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ac.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae9354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b490d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b490c0",
      "incomplete_value": true,
      "site": "00b490c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae933c",
      "incomplete_value": true,
      "site": "00ae933c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b490bc",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9348",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae934c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b490bc",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b490cc",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b490d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae933c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md#insn-00ae933c) · [`00ae934c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md#insn-00ae934c) · [`00ae9354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9328.md#insn-00ae9354)
- 新版 `00b490c0`（命令位置の公開資料なし）

~~~diff
- 00ae933c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ae933c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b490c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b490c0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae933c bytes e80000b5
+ 00b490c0 bytes e80000b5
- 00ae934c ["INT_ADD", "register:40f0:8", ["const:ae934c:8", "const:4:8"]]
- 00ae934c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae934c bytes 51d30394
- 00ae9354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae9354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9354 bytes 607603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-226216334acce4cc411f9bcfd935497f"></a>

### [`00ae9368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md) → [`00b490ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b490ec.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b49118",
      "incomplete_value": true,
      "site": "00b49118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "definition_site": "00b49100",
      "incomplete_value": true,
      "site": "00b49100",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae937c",
      "incomplete_value": true,
      "site": "00ae937c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49108",
      "incomplete_value": false,
      "site": "00b49110",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:ddf:8"
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
      "00b490fc",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49108",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00b49118",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b490fc",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49108",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b49118",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae938c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md#insn-00ae938c) · [`00ae9394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md#insn-00ae9394) · [`00ae9374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9368.md#insn-00ae9374)
- 新版 `00b49110`（命令位置の公開資料なし） · `00b49118`（命令位置の公開資料なし） · `00b490f8`（命令位置の公開資料なし）

~~~diff
- 00ae938c ["INT_ADD", "register:40f0:8", ["const:ae938c:8", "const:4:8"]]
- 00ae938c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49110 ["INT_ADD", "register:40f0:8", ["const:b49110:8", "const:4:8"]]
+ 00b49110 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae938c bytes 41d30394
+ 00b49110 bytes 80460494
- 00ae9394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae9394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00b49118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9394 bytes 607603f9
+ 00b49118 bytes 60d602f9
- 00ae9374 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b490f8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae9374 bytes b32d00f0
+ 00b490f8 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce2f815d28903d13cc2281a9c17d80d"></a>

### [`00ae93a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md) → [`00b4912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4912c.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b4915c",
      "incomplete_value": true,
      "site": "00b4915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93d8",
      "incomplete_value": true,
      "site": "00ae93d8",
      "value": [
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
      "definition_site": "00b49140",
      "incomplete_value": true,
      "site": "00b49140",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4914c",
      "incomplete_value": false,
      "site": "00b49154",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae93c8",
      "incomplete_value": false,
      "site": "00ae93d0",
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
            "const:ddf:8"
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
      "00b4913c",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4914c",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00b4915c",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4913c",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4914c",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b4915c",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae93d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md#insn-00ae93d0) · [`00ae93d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md#insn-00ae93d8) · [`00ae93b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93a8.md#insn-00ae93b4)
- 新版 `00b49154`（命令位置の公開資料なし） · `00b4915c`（命令位置の公開資料なし） · `00b49138`（命令位置の公開資料なし）

~~~diff
- 00ae93d0 ["INT_ADD", "register:40f0:8", ["const:ae93d0:8", "const:4:8"]]
- 00ae93d0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49154 ["INT_ADD", "register:40f0:8", ["const:b49154:8", "const:4:8"]]
+ 00b49154 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae93d0 bytes 30d30394
+ 00b49154 bytes 6f460494
- 00ae93d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae93d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4915c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00b4915c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae93d8 bytes 607603f9
+ 00b4915c bytes 60d602f9
- 00ae93b4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49138 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae93b4 bytes b32d00f0
+ 00b49138 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbc5e7a6aee1cbd3f9d5de5f2846d964"></a>

### [`00ae93ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md) → [`00b49170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49170.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b491a0",
      "incomplete_value": true,
      "site": "00b491a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae941c",
      "incomplete_value": true,
      "site": "00ae941c",
      "value": [
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
      "definition_site": "00b49184",
      "incomplete_value": true,
      "site": "00b49184",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9400",
      "incomplete_value": true,
      "site": "00ae9400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b4918c",
      "incomplete_value": false,
      "site": "00b49198",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9408",
      "incomplete_value": false,
      "site": "00ae9414",
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
            "const:ddf:8"
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
      "00b49180",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4918c",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00b491a0",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49180",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4918c",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b491a0",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md#insn-00ae9414) · [`00ae941c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md#insn-00ae941c) · [`00ae93f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae93ec.md#insn-00ae93f8)
- 新版 `00b49198`（命令位置の公開資料なし） · `00b491a0`（命令位置の公開資料なし） · `00b4917c`（命令位置の公開資料なし）

~~~diff
- 00ae9414 ["INT_ADD", "register:40f0:8", ["const:ae9414:8", "const:4:8"]]
- 00ae9414 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49198 ["INT_ADD", "register:40f0:8", ["const:b49198:8", "const:4:8"]]
+ 00b49198 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9414 bytes 1fd30394
+ 00b49198 bytes 5e460494
- 00ae941c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
- 00ae941c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b491a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00b491a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae941c bytes 607603f9
+ 00b491a0 bytes 60d602f9
- 00ae93f8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4917c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae93f8 bytes b32d00f0
+ 00b4917c bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8789a66c3a66e8140424339dd6e17ad4"></a>

### [`00ae943c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae943c.md) → [`00b491c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b491c0.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49248",
      "incomplete_value": true,
      "site": "00b49248",
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
      "definition_site": "00ae94c4",
      "incomplete_value": true,
      "site": "00ae94c4",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae947c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b49200"
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
      "00b491d4",
      "READ",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9470",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49248",
      "WRITE",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b491d4",
      "READ",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b491f4",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49248",
      "WRITE",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae947c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae943c.md#insn-00ae947c) · [`00ae94c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae943c.md#insn-00ae94c4)
- 新版 `00b49248`（命令位置の公開資料なし） · `00b49200`（命令位置の公開資料なし）

~~~diff
- 00ae947c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae947c ["INT_ADD", "register:40f0:8", ["const:ae947c:8", "const:4:8"]]
- 00ae947c ["CALLIND", null, ["register:0:8"]]
- 00ae947c bytes 00013fd6
- 00ae94c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae94c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6f0:8"]]
- 00ae94c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49248 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49248 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5b0:8"]]
+ 00b49248 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae94c4 bytes a0c21b39
+ 00b49248 bytes a0c21639
+ 00b49200 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49200 ["INT_ADD", "register:40f0:8", ["const:b49200:8", "const:4:8"]]
+ 00b49200 ["CALLIND", null, ["register:0:8"]]
+ 00b49200 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed3b8c4f6614eb8a2b36787920c95e44"></a>

### [`00ae94d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md) → [`00b4925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4925c.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 50.00% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49298",
      "incomplete_value": true,
      "site": "00b49298",
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
      "definition_site": "00ae9514",
      "incomplete_value": true,
      "site": "00ae9514",
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9564"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b492e8"
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
      "00b49270",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4927c",
      "READ",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49298",
      "WRITE",
      [
        "storage",
        "010a06f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49270",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4927c",
      "READ",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49298",
      "WRITE",
      [
        "storage",
        "011255b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md#insn-00ae94f0) · [`00ae9514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md#insn-00ae9514) · [`00ae953c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae94d8.md#insn-00ae953c)
- 新版 `00b49274`（命令位置の公開資料なし） · `00b49298`（命令位置の公開資料なし）

~~~diff
- 00ae94f0 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae94f0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b49274 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b49274 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ae94f0 bytes c10300b4
+ 00b49274 bytes c10300b4
- 00ae9514 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae9514 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae9514 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
- 00ae9514 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b49298 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b49298 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b49298 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5b0:8"]]
+ 00b49298 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae9514 bytes bfc21b39
+ 00b49298 bytes bfc21639
- 00ae953c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae953c ["INT_ADD", "register:40f0:8", ["const:ae953c:8", "const:4:8"]]
- 00ae953c ["CALLIND", null, ["register:0:8"]]
- 00ae953c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26972c1cb99e35a94963e49cff526fd8"></a>

### [`00ae9578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9578.md) → [`00b492fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b492fc.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00b4933c",
      "incomplete_value": true,
      "site": "00b4933c",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae95b8",
      "incomplete_value": true,
      "site": "00ae95b8",
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
      "definition_site": "00b49318",
      "incomplete_value": true,
      "site": "00b49318",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9594",
      "incomplete_value": true,
      "site": "00ae9594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49320",
      "incomplete_value": false,
      "site": "00b49334",
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
            "const:f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae959c",
      "incomplete_value": false,
      "site": "00ae95b0",
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
            "const:ddf:8"
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
      "00b49310",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49320",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ],
    [
      "00b4933c",
      "WRITE",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49310",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49320",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ],
    [
      "00b4933c",
      "WRITE",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae95b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9578.md#insn-00ae95b0) · [`00ae95b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9578.md#insn-00ae95b8) · [`00ae9584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9578.md#insn-00ae9584)
- 新版 `00b49334`（命令位置の公開資料なし） · `00b4933c`（命令位置の公開資料なし） · `00b49308`（命令位置の公開資料なし）

~~~diff
- 00ae95b0 ["INT_ADD", "register:40f0:8", ["const:ae95b0:8", "const:4:8"]]
- 00ae95b0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49334 ["INT_ADD", "register:40f0:8", ["const:b49334:8", "const:4:8"]]
+ 00b49334 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae95b0 bytes b8d20394
+ 00b49334 bytes f7450494
- 00ae95b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00ae95b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4933c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00b4933c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae95b8 bytes 807603f9
+ 00b4933c bytes 80d602f9
- 00ae9584 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49308 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00ae9584 bytes b42d00f0
+ 00b49308 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36efb59e698999822346c6183f30b8ab"></a>

### [`00ae95e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae95e8.md) → [`00b4936c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4936c.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6c0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b140.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b49388",
      "incomplete_value": false,
      "site": "00b4938c",
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
    "old": {
      "definition_site": "00ae9604",
      "incomplete_value": false,
      "site": "00ae9608",
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
      "definition_site": "00b49398",
      "incomplete_value": true,
      "site": "00b493a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9614",
      "incomplete_value": true,
      "site": "00ae9620",
      "value": [
        "LOAD",
        "8",
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
      "00b49388",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b49398",
      "DATA",
      [
        "storage",
        "010a06f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49388",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b49398",
      "DATA",
      [
        "storage",
        "011255b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae95e8.md#insn-00ae9608) · [`00ae9600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae95e8.md#insn-00ae9600) · [`00ae9604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae95e8.md#insn-00ae9604)
- 新版 `00b4938c`（命令位置の公開資料なし） · `00b49384`（命令位置の公開資料なし） · `00b49388`（命令位置の公開資料なし）

~~~diff
- 00ae9608 ["INT_ADD", "register:40f0:8", ["const:ae9608:8", "const:4:8"]]
- 00ae9608 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4938c ["INT_ADD", "register:40f0:8", ["const:b4938c:8", "const:4:8"]]
+ 00b4938c ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae9608 bytes ded20394
+ 00b4938c bytes 1d460494
- 00ae9600 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b49384 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae9600 bytes 60bdfff0
+ 00b49384 bytes e0bafff0
- 00ae9604 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae9604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49388 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b49388 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49388 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49388 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9604 bytes 001c1591
+ 00b49388 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c0658ffa024ace1f6241391e08ccaed"></a>

### [`00ae9624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9624.md) → [`00b493a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b493a8.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae9664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b493e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9638",
      "READ",
      [
        "storage",
        "010a06e8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b493ec"
      ]
    ],
    [
      "unmatched:00ae9648",
      "PARAM",
      [
        "storage",
        "0029dddf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b493bc",
      "READ",
      [
        "storage",
        "011255a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b493c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b493ec"
      ]
    ],
    [
      "00b493cc",
      "PARAM",
      [
        "storage",
        "002ae0f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9624.md#insn-00ae9640) · [`00ae965c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9624.md#insn-00ae965c) · [`00ae9664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9624.md#insn-00ae9664)
- 新版 `00b493e0`（命令位置の公開資料なし）

~~~diff
- 00ae9640 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9640 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00ae9640 bytes 410100b5
- 00ae965c ["INT_ADD", "register:40f0:8", ["const:ae965c:8", "const:4:8"]]
- 00ae965c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b493e0 ["INT_ADD", "register:40f0:8", ["const:b493e0:8", "const:4:8"]]
+ 00b493e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae965c bytes 8dd20394
+ 00b493e0 bytes cc450494
- 00ae9664 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
- 00ae9664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9664 bytes 807603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-995853c1260128381028dfc0c214d9fd"></a>

### [`00ae9694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9694.md) → [`00b49418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49418.md) _ZN8firebase4util7context10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b49434",
      "incomplete_value": false,
      "site": "00b49438",
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
    "old": {
      "definition_site": "00ae96b0",
      "incomplete_value": false,
      "site": "00ae96b4",
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
      "definition_site": "00b49444",
      "incomplete_value": true,
      "site": "00b49450",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae96c0",
      "incomplete_value": true,
      "site": "00ae96cc",
      "value": [
        "LOAD",
        "8",
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
      "00b49434",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b49444",
      "DATA",
      [
        "storage",
        "010a0710",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49434",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b49444",
      "DATA",
      [
        "storage",
        "011255d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae96b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9694.md#insn-00ae96b4) · [`00ae96ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9694.md#insn-00ae96ac) · [`00ae96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9694.md#insn-00ae96b0)
- 新版 `00b49438`（命令位置の公開資料なし） · `00b49430`（命令位置の公開資料なし） · `00b49434`（命令位置の公開資料なし）

~~~diff
- 00ae96b4 ["INT_ADD", "register:40f0:8", ["const:ae96b4:8", "const:4:8"]]
- 00ae96b4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b49438 ["INT_ADD", "register:40f0:8", ["const:b49438:8", "const:4:8"]]
+ 00b49438 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae96b4 bytes b3d20394
+ 00b49438 bytes f2450494
- 00ae96ac ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b49430 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae96ac bytes 80bdff90
+ 00b49430 bytes 00bbff90
- 00ae96b0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae96b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae96b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae96b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49434 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b49434 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49434 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49434 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae96b0 bytes 00c81791
+ 00b49434 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac4d779bf2305373076ce087a15deda"></a>

### [`00ae96d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae96d0.md) → [`00b49454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49454.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b49480",
      "incomplete_value": true,
      "site": "00b49480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96fc",
      "incomplete_value": true,
      "site": "00ae96fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00b49468",
      "incomplete_value": true,
      "site": "00b49468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96e4",
      "incomplete_value": true,
      "site": "00ae96e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49474",
      "incomplete_value": false,
      "site": "00b49478",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae96f0",
      "incomplete_value": false,
      "site": "00ae96f4",
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
      "00b49464",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49474",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00b49480",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49464",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49474",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b49480",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae96f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae96d0.md#insn-00ae96f4) · [`00ae96fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae96d0.md#insn-00ae96fc) · [`00ae96dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae96d0.md#insn-00ae96dc)
- 新版 `00b49478`（命令位置の公開資料なし） · `00b49480`（命令位置の公開資料なし） · `00b49460`（命令位置の公開資料なし）

~~~diff
- 00ae96f4 ["INT_ADD", "register:40f0:8", ["const:ae96f4:8", "const:4:8"]]
- 00ae96f4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49478 ["INT_ADD", "register:40f0:8", ["const:b49478:8", "const:4:8"]]
+ 00b49478 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae96f4 bytes 67d20394
+ 00b49478 bytes a6450494
- 00ae96fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
- 00ae96fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
+ 00b49480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae96fc bytes 608e03f9
+ 00b49480 bytes 60ee02f9
- 00ae96dc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49460 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae96dc bytes b32d00f0
+ 00b49460 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-896e78e92f110f100fc74b54f9ea245f"></a>

### [`00ae9710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9710.md) → [`00b49494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49494.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b494c0",
      "incomplete_value": true,
      "site": "00b494c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:718:8"
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
      "definition_site": "00b494a8",
      "incomplete_value": true,
      "site": "00b494a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9724",
      "incomplete_value": true,
      "site": "00ae9724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b494b0",
      "incomplete_value": false,
      "site": "00b494b8",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b494a4",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494b0",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00b494c0",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b494a4",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494b0",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b494c0",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9710.md#insn-00ae9734) · [`00ae973c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9710.md#insn-00ae973c) · [`00ae971c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9710.md#insn-00ae971c)
- 新版 `00b494b8`（命令位置の公開資料なし） · `00b494c0`（命令位置の公開資料なし） · `00b494a0`（命令位置の公開資料なし）

~~~diff
- 00ae9734 ["INT_ADD", "register:40f0:8", ["const:ae9734:8", "const:4:8"]]
- 00ae9734 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b494b8 ["INT_ADD", "register:40f0:8", ["const:b494b8:8", "const:4:8"]]
+ 00b494b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9734 bytes 57d20394
+ 00b494b8 bytes 96450494
- 00ae973c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
- 00ae973c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b494c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
+ 00b494c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae973c bytes 608e03f9
+ 00b494c0 bytes 60ee02f9
- 00ae971c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b494a0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae971c bytes b32d00f0
+ 00b494a0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39170ff5e72110ad376981fcdad6f891"></a>

### [`00ae9750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9750.md) → [`00b494d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b494d4.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b49504",
      "incomplete_value": true,
      "site": "00b49504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
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
            "const:718:8"
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
      "definition_site": "00b494e8",
      "incomplete_value": true,
      "site": "00b494e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b494f4",
      "incomplete_value": false,
      "site": "00b494fc",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9770",
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
      "00b494e4",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494f4",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00b49504",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b494e4",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494f4",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b49504",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9750.md#insn-00ae9778) · [`00ae9780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9750.md#insn-00ae9780) · [`00ae975c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9750.md#insn-00ae975c)
- 新版 `00b494fc`（命令位置の公開資料なし） · `00b49504`（命令位置の公開資料なし） · `00b494e0`（命令位置の公開資料なし）

~~~diff
- 00ae9778 ["INT_ADD", "register:40f0:8", ["const:ae9778:8", "const:4:8"]]
- 00ae9778 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b494fc ["INT_ADD", "register:40f0:8", ["const:b494fc:8", "const:4:8"]]
+ 00b494fc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9778 bytes 46d20394
+ 00b494fc bytes 85450494
- 00ae9780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
- 00ae9780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
+ 00b49504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9780 bytes 608e03f9
+ 00b49504 bytes 60ee02f9
- 00ae975c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b494e0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae975c bytes b32d00f0
+ 00b494e0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-090e5ced45e9fe82eed3277dda3f2509"></a>

### [`00ae9794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9794.md) → [`00b49518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49518.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b49548",
      "incomplete_value": true,
      "site": "00b49548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97c4",
      "incomplete_value": true,
      "site": "00ae97c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:718:8"
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
      "definition_site": "00b4952c",
      "incomplete_value": true,
      "site": "00b4952c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97a8",
      "incomplete_value": true,
      "site": "00ae97a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49534",
      "incomplete_value": false,
      "site": "00b49540",
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
            "const:a4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae97b0",
      "incomplete_value": false,
      "site": "00ae97bc",
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
      "00b49528",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49534",
      "PARAM",
      [
        "storage",
        "002941bb",
        null,
        "string"
      ]
    ],
    [
      "00b49548",
      "WRITE",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49528",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49534",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ],
    [
      "00b49548",
      "WRITE",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae97bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9794.md#insn-00ae97bc) · [`00ae97c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9794.md#insn-00ae97c4) · [`00ae97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9794.md#insn-00ae97a0)
- 新版 `00b49540`（命令位置の公開資料なし） · `00b49548`（命令位置の公開資料なし） · `00b49524`（命令位置の公開資料なし）

~~~diff
- 00ae97bc ["INT_ADD", "register:40f0:8", ["const:ae97bc:8", "const:4:8"]]
- 00ae97bc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49540 ["INT_ADD", "register:40f0:8", ["const:b49540:8", "const:4:8"]]
+ 00b49540 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae97bc bytes 35d20394
+ 00b49540 bytes 74450494
- 00ae97c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:718:8"]]
- 00ae97c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49548 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5d8:8"]]
+ 00b49548 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae97c4 bytes 608e03f9
+ 00b49548 bytes 60ee02f9
- 00ae97a0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49524 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae97a0 bytes b32d00f0
+ 00b49524 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92efdcaf97e53d496b472e364d82b003"></a>

### [`00ae97e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae97e4.md) → [`00b49568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49568.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b495f0",
      "incomplete_value": true,
      "site": "00b495f0",
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
            "const:5e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae986c",
      "incomplete_value": true,
      "site": "00ae986c",
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
            "const:720:8"
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
      "definition_site": "00b4959c",
      "incomplete_value": true,
      "site": "00b495a8",
      "value": [
        "LOAD",
        "8",
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
                "const:5d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9818",
      "incomplete_value": true,
      "site": "00ae9824",
      "value": [
        "LOAD",
        "8",
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
                "const:718:8"
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
      "00b4957c",
      "READ",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4959c",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00b495f0",
      "WRITE",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4957c",
      "READ",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4959c",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b495f0",
      "WRITE",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae97e4.md#insn-00ae9824) · [`00ae986c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae97e4.md#insn-00ae986c) · [`00ae97f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae97e4.md#insn-00ae97f4)
- 新版 `00b495a8`（命令位置の公開資料なし） · `00b495f0`（命令位置の公開資料なし） · `00b49578`（命令位置の公開資料なし）

~~~diff
- 00ae9824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9824 ["INT_ADD", "register:40f0:8", ["const:ae9824:8", "const:4:8"]]
- 00ae9824 ["CALLIND", null, ["register:0:8"]]
+ 00b495a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b495a8 ["INT_ADD", "register:40f0:8", ["const:b495a8:8", "const:4:8"]]
+ 00b495a8 ["CALLIND", null, ["register:0:8"]]
- 00ae9824 bytes 00013fd6
+ 00b495a8 bytes 00013fd6
- 00ae986c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae986c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:720:8"]]
- 00ae986c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b495f0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b495f0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5e0:8"]]
+ 00b495f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae986c bytes a0821c39
+ 00b495f0 bytes a0821739
- 00ae97f4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b49578 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00ae97f4 bytes b52d00f0
+ 00b49578 bytes f52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b36d4353fd6189df1755aa46a2797507"></a>

### [`00ae9880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9880.md) → [`00b49604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49604.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00ae98bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae990c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49640"
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
      "00b49618",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4961c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae9910"
      ]
    ],
    [
      "unmatched:00ae98a0",
      "READ",
      [
        "storage",
        "010a0720",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49618",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4961c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49694"
      ]
    ],
    [
      "00b49624",
      "READ",
      [
        "storage",
        "011255e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9880.md#insn-00ae9898) · [`00ae98bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9880.md#insn-00ae98bc) · [`00ae98e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9880.md#insn-00ae98e4)
- 新版 `00b4961c`（命令位置の公開資料なし）

~~~diff
- 00ae9898 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9898 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b4961c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4961c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00ae9898 bytes c10300b4
+ 00b4961c bytes c10300b4
- 00ae98bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae98bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae98bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:720:8"]]
- 00ae98bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae98bc bytes bf821c39
- 00ae98e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae98e4 ["INT_ADD", "register:40f0:8", ["const:ae98e4:8", "const:4:8"]]
- 00ae98e4 ["CALLIND", null, ["register:0:8"]]
- 00ae98e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8000f883b7ca0ef8beaaad0f9230e337"></a>

### [`00ae9920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9920.md) → [`00b496a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b496a4.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00ae9960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b496e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae993c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9934",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae993c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b496e8"
      ]
    ],
    [
      "unmatched:00ae9944",
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
      "00b496b8",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b496c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b496e8"
      ]
    ],
    [
      "00b496c8",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae993c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9920.md#insn-00ae993c) · [`00ae9958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9920.md#insn-00ae9958) · [`00ae9960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9920.md#insn-00ae9960)
- 新版 `00b496dc`（命令位置の公開資料なし）

~~~diff
- 00ae993c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae993c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae993c bytes 410100b5
- 00ae9958 ["INT_ADD", "register:40f0:8", ["const:ae9958:8", "const:4:8"]]
- 00ae9958 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b496dc ["INT_ADD", "register:40f0:8", ["const:b496dc:8", "const:4:8"]]
+ 00b496dc ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9958 bytes ced10394
+ 00b496dc bytes 0d450494
- 00ae9960 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
- 00ae9960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9960 bytes 808e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6940ada69e7b64ec9a0b20b86f8b543c"></a>

### [`00ae9990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9990.md) → [`00b49714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49714.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b49730",
      "incomplete_value": false,
      "site": "00b49734",
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
    "old": {
      "definition_site": "00ae99ac",
      "incomplete_value": false,
      "site": "00ae99b0",
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
      "definition_site": "00b49740",
      "incomplete_value": true,
      "site": "00b4974c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae99bc",
      "incomplete_value": true,
      "site": "00ae99c8",
      "value": [
        "LOAD",
        "8",
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
      "00b49730",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b49740",
      "DATA",
      [
        "storage",
        "010a0728",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49730",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b49740",
      "DATA",
      [
        "storage",
        "011255e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae99b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9990.md#insn-00ae99b0) · [`00ae99a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9990.md#insn-00ae99a8) · [`00ae99ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9990.md#insn-00ae99ac)
- 新版 `00b49734`（命令位置の公開資料なし） · `00b4972c`（命令位置の公開資料なし） · `00b49730`（命令位置の公開資料なし）

~~~diff
- 00ae99b0 ["INT_ADD", "register:40f0:8", ["const:ae99b0:8", "const:4:8"]]
- 00ae99b0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b49734 ["INT_ADD", "register:40f0:8", ["const:b49734:8", "const:4:8"]]
+ 00b49734 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae99b0 bytes f4d10394
+ 00b49734 bytes 33450494
- 00ae99a8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4972c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00ae99a8 bytes 60bdfff0
+ 00b4972c bytes e0bafff0
- 00ae99ac ["COPY", "tmp:0:8", ["const:547:8"]]
- 00ae99ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae99ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae99ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49730 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b49730 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49730 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49730 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae99ac bytes 001c1591
+ 00b49730 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6cd53ea769b01c54722abb4bdd27e1b"></a>

### [`00ae99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae99cc.md) → [`00b49750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49750.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae9a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49790"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae99e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae99e0",
      "READ",
      [
        "storage",
        "010a0718",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae99e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49794"
      ]
    ],
    [
      "unmatched:00ae99f0",
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
      "00b49764",
      "READ",
      [
        "storage",
        "011255d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4976c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49794"
      ]
    ],
    [
      "00b49774",
      "PARAM",
      [
        "storage",
        "002a3a4a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae99e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae99cc.md#insn-00ae99e8) · [`00ae9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae99cc.md#insn-00ae9a04) · [`00ae9a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae99cc.md#insn-00ae9a0c)
- 新版 `00b49788`（命令位置の公開資料なし）

~~~diff
- 00ae99e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae99e8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ae99e8 bytes 410100b5
- 00ae9a04 ["INT_ADD", "register:40f0:8", ["const:ae9a04:8", "const:4:8"]]
- 00ae9a04 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49788 ["INT_ADD", "register:40f0:8", ["const:b49788:8", "const:4:8"]]
+ 00b49788 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9a04 bytes a3d10394
+ 00b49788 bytes e2440494
- 00ae9a0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:718:8"]]
- 00ae9a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9a0c bytes 808e03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2311053409fc707720cb34dd9f013935"></a>

### [`00ae9a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a3c.md) → [`00b497c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497c0.md) _ZN8firebase4util6cursor10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b497dc",
      "incomplete_value": false,
      "site": "00b497e0",
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
    "old": {
      "definition_site": "00ae9a58",
      "incomplete_value": false,
      "site": "00ae9a5c",
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
      "definition_site": "00b497ec",
      "incomplete_value": true,
      "site": "00b497f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae9a68",
      "incomplete_value": true,
      "site": "00ae9a74",
      "value": [
        "LOAD",
        "8",
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
      "00b497dc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b497ec",
      "DATA",
      [
        "storage",
        "010a0748",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b497dc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b497ec",
      "DATA",
      [
        "storage",
        "01125608",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a3c.md#insn-00ae9a5c) · [`00ae9a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a3c.md#insn-00ae9a54) · [`00ae9a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a3c.md#insn-00ae9a58)
- 新版 `00b497e0`（命令位置の公開資料なし） · `00b497d8`（命令位置の公開資料なし） · `00b497dc`（命令位置の公開資料なし）

~~~diff
- 00ae9a5c ["INT_ADD", "register:40f0:8", ["const:ae9a5c:8", "const:4:8"]]
- 00ae9a5c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b497e0 ["INT_ADD", "register:40f0:8", ["const:b497e0:8", "const:4:8"]]
+ 00b497e0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae9a5c bytes c9d10394
+ 00b497e0 bytes 08450494
- 00ae9a54 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b497d8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae9a54 bytes 80bdff90
+ 00b497d8 bytes 00bbff90
- 00ae9a58 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae9a58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9a58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9a58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b497dc ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b497dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b497dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b497dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9a58 bytes 00c81791
+ 00b497dc bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77f50538cbf433a5880cb28f8bac512b"></a>

### [`00ae9a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a78.md) → [`00b497fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b497fc.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae9aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49828"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49810",
      "incomplete_value": true,
      "site": "00b49810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9a8c",
      "incomplete_value": true,
      "site": "00ae9a8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b4980c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae9aa8"
      ]
    ],
    [
      "unmatched:00ae9a98",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4980c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4982c"
      ]
    ],
    [
      "00b4981c",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a78.md#insn-00ae9a9c) · [`00ae9aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a78.md#insn-00ae9aa4) · [`00ae9ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9a78.md#insn-00ae9ab4)

~~~diff
- 00ae9a9c ["INT_ADD", "register:40f0:8", ["const:ae9a9c:8", "const:4:8"]]
- 00ae9a9c ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9a9c bytes 7dd10394
- 00ae9aa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00ae9aa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9aa4 bytes 60aa03f9
- 00ae9ab4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae9ab4 ["RETURN", null, ["register:0:8"]]
- 00ae9ab4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-940cf46d760eba4f333fd031d297f537"></a>

### [`00ae9ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ab8.md) → [`00b4983c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b4983c.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b49868",
      "incomplete_value": true,
      "site": "00b49868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ae4",
      "incomplete_value": true,
      "site": "00ae9ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00b49850",
      "incomplete_value": true,
      "site": "00b49850",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9acc",
      "incomplete_value": true,
      "site": "00ae9acc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b49858",
      "incomplete_value": false,
      "site": "00b49860",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9ad4",
      "incomplete_value": false,
      "site": "00ae9adc",
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
            "const:5fe:8"
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
      "00b4984c",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49858",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00b49868",
      "WRITE",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4984c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49858",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      "00b49868",
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ab8.md#insn-00ae9adc) · [`00ae9ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ab8.md#insn-00ae9ae4) · [`00ae9ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ab8.md#insn-00ae9ac4)
- 新版 `00b49860`（命令位置の公開資料なし） · `00b49868`（命令位置の公開資料なし） · `00b49848`（命令位置の公開資料なし）

~~~diff
- 00ae9adc ["INT_ADD", "register:40f0:8", ["const:ae9adc:8", "const:4:8"]]
- 00ae9adc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49860 ["INT_ADD", "register:40f0:8", ["const:b49860:8", "const:4:8"]]
+ 00b49860 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9adc bytes 6dd10394
+ 00b49860 bytes ac440494
- 00ae9ae4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00ae9ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
+ 00b49868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9ae4 bytes 60aa03f9
+ 00b49868 bytes 600a03f9
- 00ae9ac4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49848 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae9ac4 bytes b32d00f0
+ 00b49848 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31d0efeff67e624bb5593b04987aa4b0"></a>

### [`00ae9b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b3c.md) → [`00b498c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b498c0.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00b498f0",
      "incomplete_value": true,
      "site": "00b498f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b6c",
      "incomplete_value": true,
      "site": "00ae9b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "definition_site": "00b498d4",
      "incomplete_value": true,
      "site": "00b498d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b50",
      "incomplete_value": true,
      "site": "00ae9b50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b498dc",
      "incomplete_value": false,
      "site": "00b498e8",
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
            "const:351:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9b58",
      "incomplete_value": false,
      "site": "00ae9b64",
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
            "const:5fe:8"
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
      "00b498d0",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b498dc",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ],
    [
      "00b498f0",
      "WRITE",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b498d0",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b498dc",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ],
    [
      "00b498f0",
      "WRITE",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b3c.md#insn-00ae9b64) · [`00ae9b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b3c.md#insn-00ae9b6c) · [`00ae9b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b3c.md#insn-00ae9b48)
- 新版 `00b498e8`（命令位置の公開資料なし） · `00b498f0`（命令位置の公開資料なし） · `00b498cc`（命令位置の公開資料なし）

~~~diff
- 00ae9b64 ["INT_ADD", "register:40f0:8", ["const:ae9b64:8", "const:4:8"]]
- 00ae9b64 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b498e8 ["INT_ADD", "register:40f0:8", ["const:b498e8:8", "const:4:8"]]
+ 00b498e8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9b64 bytes 4bd10394
+ 00b498e8 bytes 8a440494
- 00ae9b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00ae9b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b498f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:610:8"]]
+ 00b498f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9b6c bytes 60aa03f9
+ 00b498f0 bytes 600a03f9
- 00ae9b48 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b498cc ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae9b48 bytes b32d00f0
+ 00b498cc bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d96b05cc187de2fe3cc7e816032350"></a>

### [`00ae9b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b8c.md) → [`00b49910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49910.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49998",
      "incomplete_value": true,
      "site": "00b49998",
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
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9c14",
      "incomplete_value": true,
      "site": "00ae9c14",
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
            "const:758:8"
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
      "definition_site": "00b49944",
      "incomplete_value": true,
      "site": "00b49950",
      "value": [
        "LOAD",
        "8",
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
                "const:610:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae9bc0",
      "incomplete_value": true,
      "site": "00ae9bcc",
      "value": [
        "LOAD",
        "8",
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
                "const:750:8"
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
      "site": "00ae9be0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49924",
      "READ",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9bc0",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49998",
      "WRITE",
      [
        "storage",
        "010a0758",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49924",
      "READ",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49944",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49998",
      "WRITE",
      [
        "storage",
        "01125618",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b8c.md#insn-00ae9bcc) · [`00ae9be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b8c.md#insn-00ae9be0) · [`00ae9c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9b8c.md#insn-00ae9c14)
- 新版 `00b49950`（命令位置の公開資料なし） · `00b49998`（命令位置の公開資料なし）

~~~diff
- 00ae9bcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9bcc ["INT_ADD", "register:40f0:8", ["const:ae9bcc:8", "const:4:8"]]
- 00ae9bcc ["CALLIND", null, ["register:0:8"]]
+ 00b49950 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49950 ["INT_ADD", "register:40f0:8", ["const:b49950:8", "const:4:8"]]
+ 00b49950 ["CALLIND", null, ["register:0:8"]]
- 00ae9bcc bytes 00013fd6
+ 00b49950 bytes 00013fd6
- 00ae9be0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9be0 ["INT_ADD", "register:40f0:8", ["const:ae9be0:8", "const:4:8"]]
- 00ae9be0 ["CALLIND", null, ["register:0:8"]]
- 00ae9be0 bytes 00013fd6
- 00ae9c14 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9c14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:758:8"]]
- 00ae9c14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49998 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49998 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:618:8"]]
+ 00b49998 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9c14 bytes a0621d39
+ 00b49998 bytes a0621839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c395b8335696fa316c2fa22ee6edb73"></a>

### [`00ae9c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9c28.md) → [`00b499ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b499ac.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 18.18% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9c28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9c2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9c2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae9c2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae9c30",
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
      "00b499ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b499b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b499b4",
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

- 旧版 [`00ae9c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9c28.md#insn-00ae9c28) · [`00ae9c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9c28.md#insn-00ae9c2c) · [`00ae9c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9c28.md#insn-00ae9c30)

~~~diff
- 00ae9c28 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ae9c28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ae9c28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ae9c28 bytes f50f1df8
- 00ae9c2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae9c2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae9c2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ae9c2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae9c2c bytes f44f01a9
- 00ae9c30 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae9c30 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae9c30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ae9c30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae9c30 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab663eb33b263b5ea80138d49bdf879"></a>

### [`00ae9cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9cc8.md) → [`00b49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49a4c.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00ae9d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49a8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9ce4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9cdc",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49a90"
      ]
    ],
    [
      "unmatched:00ae9cec",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49a60",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49a90"
      ]
    ],
    [
      "00b49a70",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9cc8.md#insn-00ae9ce4) · [`00ae9d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9cc8.md#insn-00ae9d00) · [`00ae9d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9cc8.md#insn-00ae9d08)
- 新版 `00b49a84`（命令位置の公開資料なし）

~~~diff
- 00ae9ce4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9ce4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ae9ce4 bytes 410100b5
- 00ae9d00 ["INT_ADD", "register:40f0:8", ["const:ae9d00:8", "const:4:8"]]
- 00ae9d00 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49a84 ["INT_ADD", "register:40f0:8", ["const:b49a84:8", "const:4:8"]]
+ 00b49a84 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9d00 bytes e4d00394
+ 00b49a84 bytes 23440494
- 00ae9d08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00ae9d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9d08 bytes 80aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8513a4a07b17f12c70275d56c388c092"></a>

### [`00ae9d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d74.md) → [`00b49af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49af8.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae9db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49b38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9d90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9d88",
      "READ",
      [
        "storage",
        "010a0750",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9d90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49b3c"
      ]
    ],
    [
      "unmatched:00ae9d98",
      "PARAM",
      [
        "storage",
        "002985fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49b0c",
      "READ",
      [
        "storage",
        "01125610",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49b3c"
      ]
    ],
    [
      "00b49b1c",
      "PARAM",
      [
        "storage",
        "002a8351",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d74.md#insn-00ae9d90) · [`00ae9dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d74.md#insn-00ae9dac) · [`00ae9db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9d74.md#insn-00ae9db4)
- 新版 `00b49b30`（命令位置の公開資料なし）

~~~diff
- 00ae9d90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9d90 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00ae9d90 bytes 410100b5
- 00ae9dac ["INT_ADD", "register:40f0:8", ["const:ae9dac:8", "const:4:8"]]
- 00ae9dac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49b30 ["INT_ADD", "register:40f0:8", ["const:b49b30:8", "const:4:8"]]
+ 00b49b30 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9dac bytes b9d00394
+ 00b49b30 bytes f8430494
- 00ae9db4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:750:8"]]
- 00ae9db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9db4 bytes 80aa03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d08557ffb8790c2388d1fe0eec872c66"></a>

### [`00ae9de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9de4.md) → [`00b49b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49b68.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
    "old": {
      "definition_site": "00ae9e00",
      "incomplete_value": false,
      "site": "00ae9e04",
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
    "old": {
      "definition_site": "00ae9e10",
      "incomplete_value": true,
      "site": "00ae9e1c",
      "value": [
        "LOAD",
        "8",
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
      "00b49b84",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b49b94",
      "DATA",
      [
        "storage",
        "010a0778",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49b84",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b49b94",
      "DATA",
      [
        "storage",
        "01125638",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9de4.md#insn-00ae9e04) · [`00ae9dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9de4.md#insn-00ae9dfc) · [`00ae9e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9de4.md#insn-00ae9e00)
- 新版 `00b49b88`（命令位置の公開資料なし） · `00b49b80`（命令位置の公開資料なし） · `00b49b84`（命令位置の公開資料なし）

~~~diff
- 00ae9e04 ["INT_ADD", "register:40f0:8", ["const:ae9e04:8", "const:4:8"]]
- 00ae9e04 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b49b88 ["INT_ADD", "register:40f0:8", ["const:b49b88:8", "const:4:8"]]
+ 00b49b88 ["CALL", null, ["callee:00c5ac00:8"]]
- 00ae9e04 bytes dfd00394
+ 00b49b88 bytes 1e440494
- 00ae9dfc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b49b80 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00ae9dfc bytes 80bdff90
+ 00b49b80 bytes 00bbff90
- 00ae9e00 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00ae9e00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9e00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae9e00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49b84 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b49b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae9e00 bytes 00c81791
+ 00b49b84 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8272bbd12c93e00f827cc999348221cc"></a>

### [`00ae9e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md) → [`00b49ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ba4.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00ae9e4c",
      "incomplete_value": true,
      "site": "00ae9e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:780:8"
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
    "old": {
      "definition_site": "00ae9e34",
      "incomplete_value": true,
      "site": "00ae9e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00ae9e40",
      "incomplete_value": false,
      "site": "00ae9e44",
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
            "const:c5:8"
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
      "00b49bb4",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49bc4",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00b49bd0",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49bb4",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49bc4",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b49bd0",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md#insn-00ae9e44) · [`00ae9e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md#insn-00ae9e4c) · [`00ae9e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e20.md#insn-00ae9e2c)
- 新版 `00b49bc8`（命令位置の公開資料なし） · `00b49bd0`（命令位置の公開資料なし） · `00b49bb0`（命令位置の公開資料なし）

~~~diff
- 00ae9e44 ["INT_ADD", "register:40f0:8", ["const:ae9e44:8", "const:4:8"]]
- 00ae9e44 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49bc8 ["INT_ADD", "register:40f0:8", ["const:b49bc8:8", "const:4:8"]]
+ 00b49bc8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9e44 bytes 93d00394
+ 00b49bc8 bytes d2430494
- 00ae9e4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00ae9e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49bd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b49bd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9e4c bytes 60c203f9
+ 00b49bd0 bytes 602203f9
- 00ae9e2c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49bb0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae9e2c bytes b32d00f0
+ 00b49bb0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-accb49065df7c68586dd9c2a410cc037"></a>

### [`00ae9e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e60.md) → [`00b49be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49be4.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00ae9e8c",
      "incomplete_value": true,
      "site": "00ae9e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:780:8"
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
    "old": {
      "definition_site": "00ae9e74",
      "incomplete_value": true,
      "site": "00ae9e74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00ae9e7c",
      "incomplete_value": false,
      "site": "00ae9e84",
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
            "const:c5:8"
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
      "00b49bf4",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c00",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00b49c10",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49bf4",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c00",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b49c10",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e60.md#insn-00ae9e84) · [`00ae9e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e60.md#insn-00ae9e8c) · [`00ae9e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9e60.md#insn-00ae9e6c)
- 新版 `00b49c08`（命令位置の公開資料なし） · `00b49c10`（命令位置の公開資料なし） · `00b49bf0`（命令位置の公開資料なし）

~~~diff
- 00ae9e84 ["INT_ADD", "register:40f0:8", ["const:ae9e84:8", "const:4:8"]]
- 00ae9e84 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49c08 ["INT_ADD", "register:40f0:8", ["const:b49c08:8", "const:4:8"]]
+ 00b49c08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9e84 bytes 83d00394
+ 00b49c08 bytes c2430494
- 00ae9e8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00ae9e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b49c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9e8c bytes 60c203f9
+ 00b49c10 bytes 602203f9
- 00ae9e6c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49bf0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00ae9e6c bytes b32d00f0
+ 00b49bf0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ce99b3b95611810bb70b86a5abaf37"></a>

### [`00ae9ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ea0.md) → [`00b49c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c24.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call, call_count, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_call_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49c54",
      "incomplete_value": true,
      "site": "00b49c54",
      "value": [
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
      "definition_site": "00ae9ed0",
      "incomplete_value": true,
      "site": "00ae9ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:780:8"
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
    "old": {
      "definition_site": "00ae9eb4",
      "incomplete_value": true,
      "site": "00ae9eb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9ec8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49c34",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c44",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ae9ec8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b49c34",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c44",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b49c4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ea0.md#insn-00ae9ec8) · [`00ae9ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ea0.md#insn-00ae9ed0)
- 新版 `00b49c54`（命令位置の公開資料なし） · `00b49c4c`（命令位置の公開資料なし）

~~~diff
- 00ae9ec8 ["INT_ADD", "register:40f0:8", ["const:ae9ec8:8", "const:4:8"]]
- 00ae9ec8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9ec8 bytes 72d00394
- 00ae9ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00ae9ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
+ 00b49c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9ed0 bytes 60c203f9
+ 00b49c54 bytes 602203f9
+ 00b49c4c ["INT_ADD", "register:40f0:8", ["const:b49c4c:8", "const:4:8"]]
+ 00b49c4c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49c4c bytes b1430494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b024ada18790c90061a87d7d82ceb74"></a>

### [`00ae9ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ee4.md) → [`00b49c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49c68.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00ae9f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49c98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00ae9ef8",
      "incomplete_value": true,
      "site": "00ae9ef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b49c78",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae9f18"
      ]
    ],
    [
      "unmatched:00ae9f00",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b49c78",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b49c9c"
      ]
    ],
    [
      "00b49c84",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ee4.md#insn-00ae9f0c) · [`00ae9f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ee4.md#insn-00ae9f14) · [`00ae9f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9ee4.md#insn-00ae9f24)
- 新版 `00b49c90`（命令位置の公開資料なし）

~~~diff
- 00ae9f0c ["INT_ADD", "register:40f0:8", ["const:ae9f0c:8", "const:4:8"]]
- 00ae9f0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49c90 ["INT_ADD", "register:40f0:8", ["const:b49c90:8", "const:4:8"]]
+ 00b49c90 ["CALL", null, ["callee:00c5ab10:8"]]
- 00ae9f0c bytes 61d00394
+ 00b49c90 bytes a0430494
- 00ae9f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00ae9f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae9f14 bytes 60c203f9
- 00ae9f24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ae9f24 ["RETURN", null, ["register:0:8"]]
- 00ae9f24 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59eb5a515ad1669cacd8699922b5ff04"></a>

### [`00ae9f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9f34.md) → [`00b49cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49cb8.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9fbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b49d40"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00ae9f68",
      "incomplete_value": true,
      "site": "00ae9f74",
      "value": [
        "LOAD",
        "8",
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
                "const:780:8"
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
      "00b49ccc",
      "READ",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ae9f68",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ae9fbc",
      "WRITE",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49ccc",
      "READ",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49cec",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d40",
      "WRITE",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9f34.md#insn-00ae9f74) · [`00ae9fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9f34.md#insn-00ae9fbc)
- 新版 `00b49cf8`（命令位置の公開資料なし） · `00b49d40`（命令位置の公開資料なし）

~~~diff
- 00ae9f74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae9f74 ["INT_ADD", "register:40f0:8", ["const:ae9f74:8", "const:4:8"]]
- 00ae9f74 ["CALLIND", null, ["register:0:8"]]
+ 00b49cf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49cf8 ["INT_ADD", "register:40f0:8", ["const:b49cf8:8", "const:4:8"]]
+ 00b49cf8 ["CALLIND", null, ["register:0:8"]]
- 00ae9f74 bytes 00013fd6
+ 00b49cf8 bytes 00013fd6
- 00ae9fbc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae9fbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
- 00ae9fbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae9fbc bytes a0221e39
+ 00b49d40 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49d40 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
+ 00b49d40 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49d40 bytes a0221939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a532e3204f180e8225d129e4591315fb"></a>

### [`00ae9fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9fd0.md) → [`00b49d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49d54.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "site": "00aea00c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aea05c",
      "incomplete_value": true,
      "site": "00aea05c",
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
            "const:780:8"
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
      "site": "00b49d90"
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
      "00b49d68",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d74",
      "READ",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aea00c",
      "WRITE",
      [
        "storage",
        "010a0788",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49d68",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d74",
      "READ",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49d90",
      "WRITE",
      [
        "storage",
        "01125648",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae9fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9fd0.md#insn-00ae9fe8) · [`00aea00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9fd0.md#insn-00aea00c) · [`00aea058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae9/00ae9fd0.md#insn-00aea058)
- 新版 `00b49d6c`（命令位置の公開資料なし） · `00b49ddc`（命令位置の公開資料なし）

~~~diff
- 00ae9fe8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00ae9fe8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b49d6c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b49d6c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00ae9fe8 bytes c10300b4
+ 00b49d6c bytes c10300b4
- 00aea00c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea00c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea00c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
- 00aea00c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea00c bytes bf221e39
- 00aea058 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea058 ["INT_ADD", "register:40f0:8", ["const:aea058:8", "const:4:8"]]
- 00aea058 ["CALLIND", null, ["register:0:8"]]
+ 00b49ddc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49ddc ["INT_ADD", "register:40f0:8", ["const:b49ddc:8", "const:4:8"]]
+ 00b49ddc ["CALLIND", null, ["register:0:8"]]
- 00aea058 bytes 00013fd6
+ 00b49ddc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eb8e08cfe694147eca2bb6033e85d30"></a>

### [`00aea070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea070.md) → [`00b49df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49df4.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
    "old": {
      "definition_site": "00aea0b0",
      "incomplete_value": true,
      "site": "00aea0b0",
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
            "const:780:8"
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
    "old": {
      "definition_site": "00aea08c",
      "incomplete_value": true,
      "site": "00aea08c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea094",
      "incomplete_value": false,
      "site": "00aea0a8",
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
            "const:c5:8"
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
      "00b49e08",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e18",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00b49e34",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49e08",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e18",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b49e34",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea070.md#insn-00aea0a8) · [`00aea0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea070.md#insn-00aea0b0) · [`00aea07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea070.md#insn-00aea07c)
- 新版 `00b49e2c`（命令位置の公開資料なし） · `00b49e34`（命令位置の公開資料なし） · `00b49e00`（命令位置の公開資料なし）

~~~diff
- 00aea0a8 ["INT_ADD", "register:40f0:8", ["const:aea0a8:8", "const:4:8"]]
- 00aea0a8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49e2c ["INT_ADD", "register:40f0:8", ["const:b49e2c:8", "const:4:8"]]
+ 00b49e2c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea0a8 bytes facf0394
+ 00b49e2c bytes 39430494
- 00aea0b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00aea0b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49e34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b49e34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea0b0 bytes 80c203f9
+ 00b49e34 bytes 802203f9
- 00aea07c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49e00 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea07c bytes b42d00d0
+ 00b49e00 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec8744baacdec6a07044d2c77b24627f"></a>

### [`00aea0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea0e0.md) → [`00b49e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49e64.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde410.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5ae90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae90.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
    "old": {
      "definition_site": "00aea0fc",
      "incomplete_value": false,
      "site": "00aea100",
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
    "old": {
      "definition_site": "00aea10c",
      "incomplete_value": true,
      "site": "00aea118",
      "value": [
        "LOAD",
        "8",
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
      "00b49e80",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b49e90",
      "DATA",
      [
        "storage",
        "010a0790",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49e80",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b49e90",
      "DATA",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea0e0.md#insn-00aea100) · [`00aea0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea0e0.md#insn-00aea0f8) · [`00aea0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea0e0.md#insn-00aea0fc)
- 新版 `00b49e84`（命令位置の公開資料なし） · `00b49e7c`（命令位置の公開資料なし） · `00b49e80`（命令位置の公開資料なし）

~~~diff
- 00aea100 ["INT_ADD", "register:40f0:8", ["const:aea100:8", "const:4:8"]]
- 00aea100 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b49e84 ["INT_ADD", "register:40f0:8", ["const:b49e84:8", "const:4:8"]]
+ 00b49e84 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aea100 bytes 20d00394
+ 00b49e84 bytes 5f430494
- 00aea0f8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b49e7c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aea0f8 bytes 60bdffd0
+ 00b49e7c bytes e0bafff0
- 00aea0fc ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aea0fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea0fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea0fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49e80 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b49e80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49e80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49e80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea0fc bytes 001c1591
+ 00b49e80 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b6baac861fd35e3559fa3e150ddadc"></a>

### [`00aea11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea11c.md) → [`00b49ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49ea0.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea15c",
      "incomplete_value": true,
      "site": "00aea15c",
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
            "const:780:8"
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
    "old": {
      "definition_site": "00aea138",
      "incomplete_value": true,
      "site": "00aea138",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea140",
      "incomplete_value": false,
      "site": "00aea154",
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
            "const:c5:8"
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
      "00b49eb4",
      "READ",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ec4",
      "PARAM",
      [
        "storage",
        "002a70c5",
        null,
        "string"
      ]
    ],
    [
      "00b49ee0",
      "WRITE",
      [
        "storage",
        "010a0780",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49eb4",
      "READ",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ec4",
      "PARAM",
      [
        "storage",
        "002b7c34",
        null,
        "string"
      ]
    ],
    [
      "00b49ee0",
      "WRITE",
      [
        "storage",
        "01125640",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea11c.md#insn-00aea154) · [`00aea15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea11c.md#insn-00aea15c) · [`00aea128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea11c.md#insn-00aea128)
- 新版 `00b49ed8`（命令位置の公開資料なし） · `00b49ee0`（命令位置の公開資料なし） · `00b49eac`（命令位置の公開資料なし）

~~~diff
- 00aea154 ["INT_ADD", "register:40f0:8", ["const:aea154:8", "const:4:8"]]
- 00aea154 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49ed8 ["INT_ADD", "register:40f0:8", ["const:b49ed8:8", "const:4:8"]]
+ 00b49ed8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea154 bytes cfcf0394
+ 00b49ed8 bytes 0e430494
- 00aea15c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00aea15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
+ 00b49ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea15c bytes 80c203f9
+ 00b49ee0 bytes 802203f9
- 00aea128 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b49eac ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea128 bytes b42d00d0
+ 00b49eac bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fad9b884364e26e52f803664dde10e55"></a>

### [`00aea18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea18c.md) → [`00b49f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f10.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
    "old": {
      "definition_site": "00aea1a8",
      "incomplete_value": false,
      "site": "00aea1ac",
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
    "old": {
      "definition_site": "00aea1b8",
      "incomplete_value": true,
      "site": "00aea1c4",
      "value": [
        "LOAD",
        "8",
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
      "00b49f2c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b49f3c",
      "DATA",
      [
        "storage",
        "010a07a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49f2c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b49f3c",
      "DATA",
      [
        "storage",
        "01125660",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea18c.md#insn-00aea1ac) · [`00aea1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea18c.md#insn-00aea1a4) · [`00aea1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea18c.md#insn-00aea1a8)
- 新版 `00b49f30`（命令位置の公開資料なし） · `00b49f28`（命令位置の公開資料なし） · `00b49f2c`（命令位置の公開資料なし）

~~~diff
- 00aea1ac ["INT_ADD", "register:40f0:8", ["const:aea1ac:8", "const:4:8"]]
- 00aea1ac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b49f30 ["INT_ADD", "register:40f0:8", ["const:b49f30:8", "const:4:8"]]
+ 00b49f30 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aea1ac bytes f5cf0394
+ 00b49f30 bytes 34430494
- 00aea1a4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b49f28 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aea1a4 bytes 60bdfff0
+ 00b49f28 bytes 00bbff90
- 00aea1a8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aea1a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea1a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea1a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49f2c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b49f2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49f2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49f2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea1a8 bytes 00c81791
+ 00b49f2c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f61d5414a7e56c26a072d0e1ad0caf81"></a>

### [`00aea1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea1c8.md) → [`00b49f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f4c.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea1f4",
      "incomplete_value": true,
      "site": "00aea1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
    "old": {
      "definition_site": "00aea1dc",
      "incomplete_value": true,
      "site": "00aea1dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea1e8",
      "incomplete_value": false,
      "site": "00aea1ec",
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
            "const:4bb:8"
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
      "00b49f5c",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49f6c",
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      "00b49f78",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49f5c",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49f6c",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b49f78",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea1c8.md#insn-00aea1ec) · [`00aea1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea1c8.md#insn-00aea1f4) · [`00aea1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea1c8.md#insn-00aea1d4)
- 新版 `00b49f70`（命令位置の公開資料なし） · `00b49f78`（命令位置の公開資料なし） · `00b49f58`（命令位置の公開資料なし）

~~~diff
- 00aea1ec ["INT_ADD", "register:40f0:8", ["const:aea1ec:8", "const:4:8"]]
- 00aea1ec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49f70 ["INT_ADD", "register:40f0:8", ["const:b49f70:8", "const:4:8"]]
+ 00b49f70 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea1ec bytes a9cf0394
+ 00b49f70 bytes e8420494
- 00aea1f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00aea1f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00b49f78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea1f4 bytes 60d603f9
+ 00b49f78 bytes 603603f9
- 00aea1d4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49f58 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea1d4 bytes b32d00d0
+ 00b49f58 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac4c09f149a15092418dd087d58a0ec"></a>

### [`00aea208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea208.md) → [`00b49f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49f8c.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea234",
      "incomplete_value": true,
      "site": "00aea234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
    "old": {
      "definition_site": "00aea21c",
      "incomplete_value": true,
      "site": "00aea21c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea224",
      "incomplete_value": false,
      "site": "00aea22c",
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
            "const:4bb:8"
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
      "00b49f9c",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fa8",
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      "00b49fb8",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49f9c",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fa8",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b49fb8",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea208.md#insn-00aea22c) · [`00aea234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea208.md#insn-00aea234) · [`00aea214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea208.md#insn-00aea214)
- 新版 `00b49fb0`（命令位置の公開資料なし） · `00b49fb8`（命令位置の公開資料なし） · `00b49f98`（命令位置の公開資料なし）

~~~diff
- 00aea22c ["INT_ADD", "register:40f0:8", ["const:aea22c:8", "const:4:8"]]
- 00aea22c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49fb0 ["INT_ADD", "register:40f0:8", ["const:b49fb0:8", "const:4:8"]]
+ 00b49fb0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea22c bytes 99cf0394
+ 00b49fb0 bytes d8420494
- 00aea234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00aea234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49fb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00b49fb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea234 bytes 60d603f9
+ 00b49fb8 bytes 603603f9
- 00aea214 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49f98 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea214 bytes b32d00d0
+ 00b49f98 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbe4859b8ff432ca22eefce5e12faadd"></a>

### [`00aea248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea248.md) → [`00b49fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b49/00b49fcc.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea278",
      "incomplete_value": true,
      "site": "00aea278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "definition_site": "00aea25c",
      "incomplete_value": true,
      "site": "00aea25c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea268",
      "incomplete_value": false,
      "site": "00aea270",
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
            "const:4bb:8"
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
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fec",
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      "00b49ffc",
      "WRITE",
      [
        "storage",
        "010a07a8",
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
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fec",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b49ffc",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea248.md#insn-00aea270) · [`00aea278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea248.md#insn-00aea278) · [`00aea254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea248.md#insn-00aea254)
- 新版 `00b49ff4`（命令位置の公開資料なし） · `00b49ffc`（命令位置の公開資料なし） · `00b49fd8`（命令位置の公開資料なし）

~~~diff
- 00aea270 ["INT_ADD", "register:40f0:8", ["const:aea270:8", "const:4:8"]]
- 00aea270 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b49ff4 ["INT_ADD", "register:40f0:8", ["const:b49ff4:8", "const:4:8"]]
+ 00b49ff4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea270 bytes 88cf0394
+ 00b49ff4 bytes c7420494
- 00aea278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00aea278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49ffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00b49ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea278 bytes 60d603f9
+ 00b49ffc bytes 603603f9
- 00aea254 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b49fd8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea254 bytes b32d00d0
+ 00b49fd8 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31326d740b3b1eade6e187f68b294c25"></a>

### [`00aea28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea28c.md) → [`00b4a010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a010.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea2bc",
      "incomplete_value": true,
      "site": "00aea2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
    "old": {
      "definition_site": "00aea2a0",
      "incomplete_value": true,
      "site": "00aea2a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea2a8",
      "incomplete_value": false,
      "site": "00aea2b4",
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
            "const:4bb:8"
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
      "00b4a020",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a02c",
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      "00b4a040",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a020",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a02c",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a040",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea28c.md#insn-00aea2b4) · [`00aea2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea28c.md#insn-00aea2bc) · [`00aea298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea28c.md#insn-00aea298)
- 新版 `00b4a038`（命令位置の公開資料なし） · `00b4a040`（命令位置の公開資料なし） · `00b4a01c`（命令位置の公開資料なし）

~~~diff
- 00aea2b4 ["INT_ADD", "register:40f0:8", ["const:aea2b4:8", "const:4:8"]]
- 00aea2b4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a038 ["INT_ADD", "register:40f0:8", ["const:b4a038:8", "const:4:8"]]
+ 00b4a038 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea2b4 bytes 77cf0394
+ 00b4a038 bytes b6420494
- 00aea2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a8:8"]]
- 00aea2bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00b4a040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea2bc bytes 60d603f9
+ 00b4a040 bytes 603603f9
- 00aea298 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a01c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea298 bytes b32d00d0
+ 00b4a01c bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5bcdb2578c32b98eb5a58f42a8b783b"></a>

### [`00aea2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea2dc.md) → [`00b4a060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a060.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aea364",
      "incomplete_value": true,
      "site": "00aea364",
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
            "const:7b0:8"
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
    "old": {
      "definition_site": "00aea310",
      "incomplete_value": true,
      "site": "00aea31c",
      "value": [
        "LOAD",
        "8",
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
                "const:7a8:8"
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
      "00b4a074",
      "READ",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a094",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a0e8",
      "WRITE",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a074",
      "READ",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a094",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a0e8",
      "WRITE",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea2dc.md#insn-00aea31c) · [`00aea364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea2dc.md#insn-00aea364) · [`00aea2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea2dc.md#insn-00aea2ec)
- 新版 `00b4a0a0`（命令位置の公開資料なし） · `00b4a0e8`（命令位置の公開資料なし） · `00b4a070`（命令位置の公開資料なし）

~~~diff
- 00aea31c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea31c ["INT_ADD", "register:40f0:8", ["const:aea31c:8", "const:4:8"]]
- 00aea31c ["CALLIND", null, ["register:0:8"]]
+ 00b4a0a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a0a0 ["INT_ADD", "register:40f0:8", ["const:b4a0a0:8", "const:4:8"]]
+ 00b4a0a0 ["CALLIND", null, ["register:0:8"]]
- 00aea31c bytes 00013fd6
+ 00b4a0a0 bytes 00013fd6
- 00aea364 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea364 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7b0:8"]]
- 00aea364 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a0e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a0e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:670:8"]]
+ 00b4a0e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea364 bytes a0c21e39
+ 00b4a0e8 bytes a0c21939
- 00aea2ec ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4a070 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aea2ec bytes b52d00d0
+ 00b4a070 bytes d52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7ae8ef358074a0b497a01823fe85997"></a>

### [`00aea378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea378.md) → [`00b4a0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a0fc.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aea3b4",
      "incomplete_value": true,
      "site": "00aea3b4",
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
            "const:7b0:8"
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
    "old": {
      "definition_site": "00aea404",
      "incomplete_value": true,
      "site": "00aea404",
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
            "const:7a8:8"
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
    "old": {
      "definition_site": "00aea390",
      "incomplete_value": true,
      "site": "00aea390",
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
      "00b4a110",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a11c",
      "READ",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a138",
      "WRITE",
      [
        "storage",
        "010a07b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a110",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a11c",
      "READ",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a138",
      "WRITE",
      [
        "storage",
        "01125670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea378.md#insn-00aea3b4) · [`00aea400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea378.md#insn-00aea400) · [`00aea404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea378.md#insn-00aea404)
- 新版 `00b4a138`（命令位置の公開資料なし） · `00b4a184`（命令位置の公開資料なし） · `00b4a188`（命令位置の公開資料なし）

~~~diff
- 00aea3b4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea3b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea3b4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7b0:8"]]
- 00aea3b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a138 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a138 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a138 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:670:8"]]
+ 00b4a138 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea3b4 bytes bfc21e39
+ 00b4a138 bytes bfc21939
- 00aea400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea400 ["INT_ADD", "register:40f0:8", ["const:aea400:8", "const:4:8"]]
- 00aea400 ["CALLIND", null, ["register:0:8"]]
+ 00b4a184 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a184 ["INT_ADD", "register:40f0:8", ["const:b4a184:8", "const:4:8"]]
+ 00b4a184 ["CALLIND", null, ["register:0:8"]]
- 00aea400 bytes 00013fd6
+ 00b4a184 bytes 00013fd6
- 00aea404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00aea404 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a188 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
+ 00b4a188 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea404 bytes 9fd603f9
+ 00b4a188 bytes 9f3603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d114f58aaec0267b37173a2c3a2e5562"></a>

### [`00aea418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea418.md) → [`00b4a19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a19c.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
    "old": {
      "definition_site": "00aea458",
      "incomplete_value": true,
      "site": "00aea458",
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
            "const:7a8:8"
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
    "old": {
      "definition_site": "00aea434",
      "incomplete_value": true,
      "site": "00aea434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea43c",
      "incomplete_value": false,
      "site": "00aea450",
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
            "const:4bb:8"
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
      "00b4a1b0",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a1c0",
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      "00b4a1dc",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a1b0",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a1c0",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a1dc",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea418.md#insn-00aea450) · [`00aea458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea418.md#insn-00aea458) · [`00aea424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea418.md#insn-00aea424)
- 新版 `00b4a1d4`（命令位置の公開資料なし） · `00b4a1dc`（命令位置の公開資料なし） · `00b4a1a8`（命令位置の公開資料なし）

~~~diff
- 00aea450 ["INT_ADD", "register:40f0:8", ["const:aea450:8", "const:4:8"]]
- 00aea450 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a1d4 ["INT_ADD", "register:40f0:8", ["const:b4a1d4:8", "const:4:8"]]
+ 00b4a1d4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea450 bytes 10cf0394
+ 00b4a1d4 bytes 4f420494
- 00aea458 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00aea458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a1dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
+ 00b4a1dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea458 bytes 80d603f9
+ 00b4a1dc bytes 803603f9
- 00aea424 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a1a8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea424 bytes b42d00d0
+ 00b4a1a8 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e60c8bdbd752cbe033237b30cf37cb"></a>

### [`00aea488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea488.md) → [`00b4a20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a20c.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
    "old": {
      "definition_site": "00aea4a4",
      "incomplete_value": false,
      "site": "00aea4a8",
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
    "old": {
      "definition_site": "00aea4b4",
      "incomplete_value": true,
      "site": "00aea4c0",
      "value": [
        "LOAD",
        "8",
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
      "00b4a228",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4a238",
      "DATA",
      [
        "storage",
        "010a07b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a228",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4a238",
      "DATA",
      [
        "storage",
        "01125678",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea488.md#insn-00aea4a8) · [`00aea4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea488.md#insn-00aea4a0) · [`00aea4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea488.md#insn-00aea4a4)
- 新版 `00b4a22c`（命令位置の公開資料なし） · `00b4a224`（命令位置の公開資料なし） · `00b4a228`（命令位置の公開資料なし）

~~~diff
- 00aea4a8 ["INT_ADD", "register:40f0:8", ["const:aea4a8:8", "const:4:8"]]
- 00aea4a8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4a22c ["INT_ADD", "register:40f0:8", ["const:b4a22c:8", "const:4:8"]]
+ 00b4a22c ["CALL", null, ["callee:00c5ac00:8"]]
- 00aea4a8 bytes 36cf0394
+ 00b4a22c bytes 75420494
- 00aea4a0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4a224 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aea4a0 bytes 60bdffd0
+ 00b4a224 bytes e0baffd0
- 00aea4a4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aea4a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea4a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea4a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a228 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4a228 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a228 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a228 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea4a4 bytes 001c1591
+ 00b4a228 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b55716dd7816930b43bec3af060be71"></a>

### [`00aea4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea4c4.md) → [`00b4a248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a248.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea504",
      "incomplete_value": true,
      "site": "00aea504",
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
            "const:7a8:8"
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
    "old": {
      "definition_site": "00aea4e0",
      "incomplete_value": true,
      "site": "00aea4e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea4e8",
      "incomplete_value": false,
      "site": "00aea4fc",
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
            "const:4bb:8"
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
      "00b4a25c",
      "READ",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a26c",
      "PARAM",
      [
        "storage",
        "002b04bb",
        null,
        "string"
      ]
    ],
    [
      "00b4a288",
      "WRITE",
      [
        "storage",
        "010a07a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a25c",
      "READ",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a26c",
      "PARAM",
      [
        "storage",
        "002c1ad1",
        null,
        "string"
      ]
    ],
    [
      "00b4a288",
      "WRITE",
      [
        "storage",
        "01125668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea4c4.md#insn-00aea4fc) · [`00aea504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea4c4.md#insn-00aea504) · [`00aea4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea4c4.md#insn-00aea4d0)
- 新版 `00b4a280`（命令位置の公開資料なし） · `00b4a288`（命令位置の公開資料なし） · `00b4a254`（命令位置の公開資料なし）

~~~diff
- 00aea4fc ["INT_ADD", "register:40f0:8", ["const:aea4fc:8", "const:4:8"]]
- 00aea4fc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a280 ["INT_ADD", "register:40f0:8", ["const:b4a280:8", "const:4:8"]]
+ 00b4a280 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea4fc bytes e5ce0394
+ 00b4a280 bytes 24420494
- 00aea504 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00aea504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
+ 00b4a288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea504 bytes 80d603f9
+ 00b4a288 bytes 803603f9
- 00aea4d0 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a254 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea4d0 bytes b42d00d0
+ 00b4a254 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2969c1fdad172614bc35bafedc8f089e"></a>

### [`00aea534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea534.md) → [`00b4a2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2b8.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
    "old": {
      "definition_site": "00aea550",
      "incomplete_value": false,
      "site": "00aea554",
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
    "old": {
      "definition_site": "00aea560",
      "incomplete_value": true,
      "site": "00aea56c",
      "value": [
        "LOAD",
        "8",
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
      "00b4a2d4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4a2e4",
      "DATA",
      [
        "storage",
        "010a07c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a2d4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4a2e4",
      "DATA",
      [
        "storage",
        "01125688",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea534.md#insn-00aea554) · [`00aea54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea534.md#insn-00aea54c) · [`00aea550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea534.md#insn-00aea550)
- 新版 `00b4a2d8`（命令位置の公開資料なし） · `00b4a2d0`（命令位置の公開資料なし） · `00b4a2d4`（命令位置の公開資料なし）

~~~diff
- 00aea554 ["INT_ADD", "register:40f0:8", ["const:aea554:8", "const:4:8"]]
- 00aea554 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4a2d8 ["INT_ADD", "register:40f0:8", ["const:b4a2d8:8", "const:4:8"]]
+ 00b4a2d8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aea554 bytes 0bcf0394
+ 00b4a2d8 bytes 4a420494
- 00aea54c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4a2d0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aea54c bytes 60bdfff0
+ 00b4a2d0 bytes e0bafff0
- 00aea550 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aea550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a2d4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4a2d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a2d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a2d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea550 bytes 00c81791
+ 00b4a2d4 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62af181ace2faec4ce6b0bf5c28a9097"></a>

### [`00aea570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea570.md) → [`00b4a2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a2f4.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
    "old": {
      "definition_site": "00aea59c",
      "incomplete_value": true,
      "site": "00aea59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
    "old": {
      "definition_site": "00aea584",
      "incomplete_value": true,
      "site": "00aea584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
    "old": {
      "definition_site": "00aea590",
      "incomplete_value": false,
      "site": "00aea594",
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
            "const:172:8"
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
      "00b4a304",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a314",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00b4a320",
      "WRITE",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a304",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a314",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a320",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea570.md#insn-00aea594) · [`00aea59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea570.md#insn-00aea59c) · [`00aea57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea570.md#insn-00aea57c)
- 新版 `00b4a318`（命令位置の公開資料なし） · `00b4a320`（命令位置の公開資料なし） · `00b4a300`（命令位置の公開資料なし）

~~~diff
- 00aea594 ["INT_ADD", "register:40f0:8", ["const:aea594:8", "const:4:8"]]
- 00aea594 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a318 ["INT_ADD", "register:40f0:8", ["const:b4a318:8", "const:4:8"]]
+ 00b4a318 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea594 bytes bfce0394
+ 00b4a318 bytes fe410494
- 00aea59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00aea59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a320 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
+ 00b4a320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea59c bytes 60ea03f9
+ 00b4a320 bytes 604a03f9
- 00aea57c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a300 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea57c bytes b32d00d0
+ 00b4a300 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

