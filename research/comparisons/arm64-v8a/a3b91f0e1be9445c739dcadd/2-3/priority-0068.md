# v15.7.4 → v16.0.0 · 最優先の変更候補 (68)

[一覧の目次](README.md)

<a id="compare-2aebcac1be1cac7b26dfb07bb2108c43"></a>

### [`00b62b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md) → [`00bd206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd206c.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b62b98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2098"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2080",
      "incomplete_value": true,
      "site": "00bd2080",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b80",
      "incomplete_value": true,
      "site": "00b62b80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd207c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62b88",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b62b90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd207c",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2088",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd2090",
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

- 旧版 [`00b62b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md#insn-00b62b80) · [`00b62b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md#insn-00b62b90) · [`00b62b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b6c.md#insn-00b62b98)
- 新版 `00bd2080`（命令位置の公開資料なし）

~~~diff
- 00b62b80 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62b80 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd2080 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd2080 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b62b80 bytes e80000b5
+ 00bd2080 bytes e80000b5
- 00b62b90 ["INT_ADD", "register:40f0:8", ["const:b62b90:8", "const:4:8"]]
- 00b62b90 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62b90 bytes 40ed0194
- 00b62b98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b62b98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62b98 bytes 604203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eed79be818ea8d240e395c7af9ea64a5"></a>

### [`00b62bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md) → [`00bd20ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20ac.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd20dc",
      "incomplete_value": true,
      "site": "00bd20dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:588:8"
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
            "register:4098:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00bd20c0",
      "incomplete_value": true,
      "site": "00bd20c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd20cc",
      "incomplete_value": false,
      "site": "00bd20d4",
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
            "const:c2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62bcc",
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
      "00bd20bc",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd20cc",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00bd20dc",
      "WRITE",
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
      "00bd20bc",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd20cc",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd20dc",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md#insn-00b62bd4) · [`00b62bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md#insn-00b62bdc) · [`00b62bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bac.md#insn-00b62bb8)
- 新版 `00bd20d4`（命令位置の公開資料なし） · `00bd20dc`（命令位置の公開資料なし） · `00bd20b8`（命令位置の公開資料なし）

~~~diff
- 00b62bd4 ["INT_ADD", "register:40f0:8", ["const:b62bd4:8", "const:4:8"]]
- 00b62bd4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd20d4 ["INT_ADD", "register:40f0:8", ["const:bd20d4:8", "const:4:8"]]
+ 00bd20d4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62bd4 bytes 2fed0194
+ 00bd20d4 bytes 8f220294
- 00b62bdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b62bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd20dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
+ 00bd20dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62bdc bytes 604203f9
+ 00bd20dc bytes 60c602f9
- 00b62bb8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd20b8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62bb8 bytes f32900f0
+ 00bd20b8 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddf25c0d05c9cfe91d3b263ff32fcf2f"></a>

### [`00b62bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md) → [`00bd20f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd20f0.md) _ZN8firebase4auth24user_collision_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b62c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2120"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2104",
      "incomplete_value": true,
      "site": "00bd2104",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62c04",
      "incomplete_value": true,
      "site": "00b62c04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd2100",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62c0c",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b62c20",
      "WRITE",
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
      "00bd2100",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd210c",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd2120",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md#insn-00b62c04) · [`00b62c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md#insn-00b62c18) · [`00b62c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62bf0.md#insn-00b62c20)
- 新版 `00bd2104`（命令位置の公開資料なし） · `00bd2118`（命令位置の公開資料なし）

~~~diff
- 00b62c04 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62c04 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd2104 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd2104 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b62c04 bytes 080100b5
+ 00bd2104 bytes 080100b5
- 00b62c18 ["INT_ADD", "register:40f0:8", ["const:b62c18:8", "const:4:8"]]
- 00b62c18 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2118 ["INT_ADD", "register:40f0:8", ["const:bd2118:8", "const:4:8"]]
+ 00bd2118 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62c18 bytes 1eed0194
+ 00bd2118 bytes 7e220294
- 00b62c20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b62c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62c20 bytes 604203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dae8f215ee2c68e5f5b3cf36168a3ed2"></a>

### [`00b62c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md) → [`00bd2140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2140.md) _ZN8firebase4auth24user_collision_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62c98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2198"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2174",
      "incomplete_value": true,
      "site": "00bd2180",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:588:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62c74",
      "incomplete_value": true,
      "site": "00b62c80",
      "value": [
        "LOAD",
        "8",
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
      "00bd2154",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b62c74",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62c98",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2154",
      "READ",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2174",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2198",
      "WRITE",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md#insn-00b62c80) · [`00b62c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62c40.md#insn-00b62c98)
- 新版 `00bd2180`（命令位置の公開資料なし） · `00bd2198`（命令位置の公開資料なし）

~~~diff
- 00b62c80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62c80 ["INT_ADD", "register:40f0:8", ["const:b62c80:8", "const:4:8"]]
- 00b62c80 ["CALLIND", null, ["register:0:8"]]
+ 00bd2180 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2180 ["INT_ADD", "register:40f0:8", ["const:bd2180:8", "const:4:8"]]
+ 00bd2180 ["CALLIND", null, ["register:0:8"]]
- 00b62c80 bytes 00013fd6
+ 00bd2180 bytes 00013fd6
- 00b62c98 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62c98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
- 00b62c98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62c98 bytes a0221a39
+ 00bd2198 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2198 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:590:8"]]
+ 00bd2198 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2198 bytes a0421639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24d60b58302429036c9778c992af2d02"></a>

### [`00b62cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md) → [`00bd21ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd21ac.md) _ZN8firebase4auth24user_collision_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd21e8",
      "incomplete_value": true,
      "site": "00bd21e8",
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
            "const:590:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ce8",
      "incomplete_value": true,
      "site": "00b62ce8",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd2208",
      "incomplete_value": true,
      "site": "00bd2208",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62d08",
      "incomplete_value": true,
      "site": "00b62d08",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd21c4",
      "incomplete_value": true,
      "site": "00bd21c4",
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
      "definition_site": "00b62cc4",
      "incomplete_value": true,
      "site": "00b62cc4",
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
      "00bd21c0",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd21cc",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd21e8",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd21c0",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd21cc",
      "READ",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd21e8",
      "WRITE",
      [
        "storage",
        "01126590",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md#insn-00b62ce8) · [`00b62d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md#insn-00b62d04) · [`00b62d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62cac.md#insn-00b62d08)
- 新版 `00bd21e8`（命令位置の公開資料なし） · `00bd2204`（命令位置の公開資料なし） · `00bd2208`（命令位置の公開資料なし）

~~~diff
- 00b62ce8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62ce8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62ce8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
- 00b62ce8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd21e8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd21e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd21e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:590:8"]]
+ 00bd21e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62ce8 bytes bf221a39
+ 00bd21e8 bytes bf421639
- 00b62d04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62d04 ["INT_ADD", "register:40f0:8", ["const:b62d04:8", "const:4:8"]]
- 00b62d04 ["CALLIND", null, ["register:0:8"]]
+ 00bd2204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2204 ["INT_ADD", "register:40f0:8", ["const:bd2204:8", "const:4:8"]]
+ 00bd2204 ["CALLIND", null, ["register:0:8"]]
- 00b62d04 bytes 00013fd6
+ 00bd2204 bytes 00013fd6
- 00b62d08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b62d08 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b62d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd2208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:588:8"]]
+ 00bd2208 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd2208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b62d08 bytes 9f4203f9
+ 00bd2208 bytes 9fc602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2195826c984e3b82cfb12ff6d7a85a8d"></a>

### [`00b62d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md) → [`00bd221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd221c.md) _ZN8firebase4auth24user_collision_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd225c",
      "incomplete_value": true,
      "site": "00bd225c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62d5c",
      "incomplete_value": true,
      "site": "00b62d5c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2238",
      "incomplete_value": true,
      "site": "00bd2238",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62d38",
      "incomplete_value": true,
      "site": "00b62d38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2240",
      "incomplete_value": false,
      "site": "00bd2254",
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
            "const:c2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62d40",
      "incomplete_value": false,
      "site": "00b62d54",
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
      "00bd2230",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2240",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00bd225c",
      "WRITE",
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
      "00bd2230",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2240",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd225c",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md#insn-00b62d54) · [`00b62d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md#insn-00b62d5c) · [`00b62d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d1c.md#insn-00b62d28)
- 新版 `00bd2254`（命令位置の公開資料なし） · `00bd225c`（命令位置の公開資料なし） · `00bd2228`（命令位置の公開資料なし）

~~~diff
- 00b62d54 ["INT_ADD", "register:40f0:8", ["const:b62d54:8", "const:4:8"]]
- 00b62d54 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2254 ["INT_ADD", "register:40f0:8", ["const:bd2254:8", "const:4:8"]]
+ 00bd2254 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62d54 bytes cfec0194
+ 00bd2254 bytes 2f220294
- 00b62d5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b62d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd225c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:588:8"]]
+ 00bd225c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62d5c bytes 804203f9
+ 00bd225c bytes 80c602f9
- 00b62d28 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd2228 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b62d28 bytes f42900f0
+ 00bd2228 bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7897ec1868a51061ca9f34c8521bb613"></a>

### [`00b62d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md) → [`00bd228c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd228c.md) _ZN8firebase4auth24user_collision_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd22a8",
      "incomplete_value": false,
      "site": "00bd22ac",
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
      "definition_site": "00b62da8",
      "incomplete_value": false,
      "site": "00b62dac",
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
      "definition_site": "00bd22b8",
      "incomplete_value": true,
      "site": "00bd22c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62db8",
      "incomplete_value": true,
      "site": "00b62dc4",
      "value": [
        "LOAD",
        "8",
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
      "00bd22a8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd22b8",
      "DATA",
      [
        "storage",
        "010a1690",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd22a8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd22b8",
      "DATA",
      [
        "storage",
        "01126598",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md#insn-00b62dac) · [`00b62da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md#insn-00b62da4) · [`00b62da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62d8c.md#insn-00b62da8)
- 新版 `00bd22ac`（命令位置の公開資料なし） · `00bd22a4`（命令位置の公開資料なし） · `00bd22a8`（命令位置の公開資料なし）

~~~diff
- 00b62dac ["INT_ADD", "register:40f0:8", ["const:b62dac:8", "const:4:8"]]
- 00b62dac ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd22ac ["INT_ADD", "register:40f0:8", ["const:bd22ac:8", "const:4:8"]]
+ 00bd22ac ["CALL", null, ["callee:00c5ac00:8"]]
- 00b62dac bytes f5ec0194
+ 00bd22ac bytes 55220294
- 00b62da4 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd22a4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b62da4 bytes a0b9ffd0
+ 00bd22a4 bytes a0b6ffd0
- 00b62da8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62da8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62da8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62da8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd22a8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd22a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd22a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd22a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62da8 bytes 001c1591
+ 00bd22a8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55765a475700e2dcc6c39cc4ce177409"></a>

### [`00b62dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md) → [`00bd22c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd22c8.md) _ZN8firebase4auth24user_collision_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2308",
      "incomplete_value": true,
      "site": "00bd2308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e08",
      "incomplete_value": true,
      "site": "00b62e08",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd22e4",
      "incomplete_value": true,
      "site": "00bd22e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62de4",
      "incomplete_value": true,
      "site": "00b62de4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd22ec",
      "incomplete_value": false,
      "site": "00bd2300",
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
            "const:c2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62dec",
      "incomplete_value": false,
      "site": "00b62e00",
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
      "00bd22dc",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd22ec",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00bd2308",
      "WRITE",
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
      "00bd22dc",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd22ec",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd2308",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md#insn-00b62e00) · [`00b62e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md#insn-00b62e08) · [`00b62dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62dc8.md#insn-00b62dd4)
- 新版 `00bd2300`（命令位置の公開資料なし） · `00bd2308`（命令位置の公開資料なし） · `00bd22d4`（命令位置の公開資料なし）

~~~diff
- 00b62e00 ["INT_ADD", "register:40f0:8", ["const:b62e00:8", "const:4:8"]]
- 00b62e00 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2300 ["INT_ADD", "register:40f0:8", ["const:bd2300:8", "const:4:8"]]
+ 00bd2300 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62e00 bytes a4ec0194
+ 00bd2300 bytes 04220294
- 00b62e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b62e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:588:8"]]
+ 00bd2308 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62e08 bytes 804203f9
+ 00bd2308 bytes 80c602f9
- 00b62dd4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd22d4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b62dd4 bytes f42900f0
+ 00bd22d4 bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b2eeaeac5b7c1fe9c97c1fbb587248f"></a>

### [`00b62e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md) → [`00bd2338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2338.md) _ZN8firebase4auth24user_collision_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2354",
      "incomplete_value": false,
      "site": "00bd2358",
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
      "definition_site": "00b62e54",
      "incomplete_value": false,
      "site": "00b62e58",
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
      "definition_site": "00bd2364",
      "incomplete_value": true,
      "site": "00bd2370",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62e64",
      "incomplete_value": true,
      "site": "00b62e70",
      "value": [
        "LOAD",
        "8",
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
      "00bd2354",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd2364",
      "DATA",
      [
        "storage",
        "010a1698",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2354",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd2364",
      "DATA",
      [
        "storage",
        "011265a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md#insn-00b62e58) · [`00b62e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md#insn-00b62e50) · [`00b62e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e38.md#insn-00b62e54)
- 新版 `00bd2358`（命令位置の公開資料なし） · `00bd2350`（命令位置の公開資料なし） · `00bd2354`（命令位置の公開資料なし）

~~~diff
- 00b62e58 ["INT_ADD", "register:40f0:8", ["const:b62e58:8", "const:4:8"]]
- 00b62e58 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd2358 ["INT_ADD", "register:40f0:8", ["const:bd2358:8", "const:4:8"]]
+ 00bd2358 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b62e58 bytes caec0194
+ 00bd2358 bytes 2a220294
- 00b62e50 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd2350 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b62e50 bytes a0b9fff0
+ 00bd2350 bytes a0b6fff0
- 00b62e54 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b62e54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62e54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62e54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2354 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd2354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62e54 bytes 00c81791
+ 00bd2354 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121253d551bd558988a030f75a60d598"></a>

### [`00b62e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md) → [`00bd2374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2374.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd23a0",
      "incomplete_value": true,
      "site": "00bd23a0",
      "value": [
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
      "definition_site": "00b62ea0",
      "incomplete_value": true,
      "site": "00b62ea0",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2388",
      "incomplete_value": true,
      "site": "00bd2388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e88",
      "incomplete_value": true,
      "site": "00b62e88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2394",
      "incomplete_value": false,
      "site": "00bd2398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62e94",
      "incomplete_value": false,
      "site": "00b62e98",
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
            "const:66f:8"
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
      "00bd2384",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2394",
      "PARAM",
      [
        "storage",
        "0029166f",
        null,
        "string"
      ]
    ],
    [
      "00bd23a0",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2384",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2394",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd23a0",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md#insn-00b62e98) · [`00b62ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md#insn-00b62ea0) · [`00b62e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62e74.md#insn-00b62e80)
- 新版 `00bd2398`（命令位置の公開資料なし） · `00bd23a0`（命令位置の公開資料なし） · `00bd2380`（命令位置の公開資料なし）

~~~diff
- 00b62e98 ["INT_ADD", "register:40f0:8", ["const:b62e98:8", "const:4:8"]]
- 00b62e98 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2398 ["INT_ADD", "register:40f0:8", ["const:bd2398:8", "const:4:8"]]
+ 00bd2398 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62e98 bytes 7eec0194
+ 00bd2398 bytes de210294
- 00b62ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b62ea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd23a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00bd23a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62ea0 bytes 605203f9
+ 00bd23a0 bytes 60d602f9
- 00b62e80 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2380 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62e80 bytes f32900f0
+ 00bd2380 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f35a9b1c1483f7be5f3adab4904b377"></a>

### [`00b62eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md) → [`00bd23b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23b4.md) _ZN8firebase4auth21android_web_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b62eb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62eb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62eb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62eb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd23c4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd23b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd23b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd23c4",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md#insn-00b62eb4) · [`00b62eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md#insn-00b62eb8) · [`00b62ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62eb4.md#insn-00b62ec8)
- 新版 `00bd23c8`（命令位置の公開資料なし）

~~~diff
- 00b62eb4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b62eb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b62eb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b62eb4 bytes f30f1ef8
- 00b62eb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62eb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62eb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b62eb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62eb8 bytes fd7b01a9
- 00b62ec8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62ec8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd23c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd23c8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62ec8 bytes e80000b5
+ 00bd23c8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e36dbe92d774f14ed63d44a07211b88"></a>

### [`00b62ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md) → [`00bd23f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd23f4.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2424",
      "incomplete_value": true,
      "site": "00bd2424",
      "value": [
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
            "const:6a0:8"
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
      "definition_site": "00bd2408",
      "incomplete_value": true,
      "site": "00bd2408",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2414",
      "incomplete_value": false,
      "site": "00bd241c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f14",
      "incomplete_value": false,
      "site": "00b62f1c",
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
            "const:66f:8"
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
      "00bd2404",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2414",
      "PARAM",
      [
        "storage",
        "0029166f",
        null,
        "string"
      ]
    ],
    [
      "00bd2424",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2404",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2414",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd2424",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md#insn-00b62f1c) · [`00b62f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md#insn-00b62f24) · [`00b62f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ef4.md#insn-00b62f00)
- 新版 `00bd241c`（命令位置の公開資料なし） · `00bd2424`（命令位置の公開資料なし） · `00bd2400`（命令位置の公開資料なし）

~~~diff
- 00b62f1c ["INT_ADD", "register:40f0:8", ["const:b62f1c:8", "const:4:8"]]
- 00b62f1c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd241c ["INT_ADD", "register:40f0:8", ["const:bd241c:8", "const:4:8"]]
+ 00bd241c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62f1c bytes 5dec0194
+ 00bd241c bytes bd210294
- 00b62f24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b62f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00bd2424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62f24 bytes 605203f9
+ 00bd2424 bytes 60d602f9
- 00b62f00 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2400 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62f00 bytes f32900f0
+ 00bd2400 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbe1d01f53fe67595809a338ae9090d8"></a>

### [`00b62f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md) → [`00bd2438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2438.md) _ZN8firebase4auth21android_web_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2468",
      "incomplete_value": true,
      "site": "00bd2468",
      "value": [
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
      "definition_site": "00b62f68",
      "incomplete_value": true,
      "site": "00b62f68",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd244c",
      "incomplete_value": true,
      "site": "00bd244c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f4c",
      "incomplete_value": true,
      "site": "00b62f4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2454",
      "incomplete_value": false,
      "site": "00bd2460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62f54",
      "incomplete_value": false,
      "site": "00b62f60",
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
            "const:66f:8"
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
      "00bd2448",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2454",
      "PARAM",
      [
        "storage",
        "0029166f",
        null,
        "string"
      ]
    ],
    [
      "00bd2468",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2448",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2454",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd2468",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md#insn-00b62f60) · [`00b62f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md#insn-00b62f68) · [`00b62f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f38.md#insn-00b62f44)
- 新版 `00bd2460`（命令位置の公開資料なし） · `00bd2468`（命令位置の公開資料なし） · `00bd2444`（命令位置の公開資料なし）

~~~diff
- 00b62f60 ["INT_ADD", "register:40f0:8", ["const:b62f60:8", "const:4:8"]]
- 00b62f60 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2460 ["INT_ADD", "register:40f0:8", ["const:bd2460:8", "const:4:8"]]
+ 00bd2460 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62f60 bytes 4cec0194
+ 00bd2460 bytes ac210294
- 00b62f68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b62f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2468 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
+ 00bd2468 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62f68 bytes 605203f9
+ 00bd2468 bytes 60d602f9
- 00b62f44 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2444 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62f44 bytes f32900f0
+ 00bd2444 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46b20e0387ff08f059be408365f9993d"></a>

### [`00b62f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md) → [`00bd2488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2488.md) _ZN8firebase4auth21android_web_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd24e0",
      "incomplete_value": true,
      "site": "00bd24e0",
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
      "definition_site": "00b62fe0",
      "incomplete_value": true,
      "site": "00b62fe0",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd24bc",
      "incomplete_value": true,
      "site": "00bd24c8",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
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
      "definition_site": "00b62fbc",
      "incomplete_value": true,
      "site": "00b62fc8",
      "value": [
        "LOAD",
        "8",
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
      "00bd249c",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd24bc",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd24e0",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd249c",
      "READ",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd24bc",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd24e0",
      "WRITE",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md#insn-00b62fc8) · [`00b62fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md#insn-00b62fe0) · [`00b62f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62f88.md#insn-00b62f98)
- 新版 `00bd24c8`（命令位置の公開資料なし） · `00bd24e0`（命令位置の公開資料なし） · `00bd2498`（命令位置の公開資料なし）

~~~diff
- 00b62fc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62fc8 ["INT_ADD", "register:40f0:8", ["const:b62fc8:8", "const:4:8"]]
- 00b62fc8 ["CALLIND", null, ["register:0:8"]]
+ 00bd24c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd24c8 ["INT_ADD", "register:40f0:8", ["const:bd24c8:8", "const:4:8"]]
+ 00bd24c8 ["CALLIND", null, ["register:0:8"]]
- 00b62fc8 bytes 00013fd6
+ 00bd24c8 bytes 00013fd6
- 00b62fe0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62fe0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a8:8"]]
- 00b62fe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd24e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd24e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5b0:8"]]
+ 00bd24e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62fe0 bytes a0a21a39
+ 00bd24e0 bytes a0c21639
- 00b62f98 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd2498 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b62f98 bytes f52900f0
+ 00bd2498 bytes b52a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52b4d24543071ce7d6e9ee6c95fd3a87"></a>

### [`00b62ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md) → [`00bd24f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd24f4.md) _ZN8firebase4auth21android_web_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd2530",
      "incomplete_value": true,
      "site": "00bd2530",
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
      "definition_site": "00b63030",
      "incomplete_value": true,
      "site": "00b63030",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd2550",
      "incomplete_value": true,
      "site": "00bd2550",
      "value": [
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
      "definition_site": "00b63050",
      "incomplete_value": true,
      "site": "00b63050",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd250c",
      "incomplete_value": true,
      "site": "00bd250c",
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
      "definition_site": "00b6300c",
      "incomplete_value": true,
      "site": "00b6300c",
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
      "00bd2508",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2514",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2530",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2508",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2514",
      "READ",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2530",
      "WRITE",
      [
        "storage",
        "011265b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md#insn-00b63030) · [`00b6304c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md#insn-00b6304c) · [`00b63050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62ff4.md#insn-00b63050)
- 新版 `00bd2530`（命令位置の公開資料なし） · `00bd254c`（命令位置の公開資料なし） · `00bd2550`（命令位置の公開資料なし）

~~~diff
- 00b63030 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b63030 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b63030 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a8:8"]]
- 00b63030 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd2530 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd2530 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd2530 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5b0:8"]]
+ 00bd2530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b63030 bytes bfa21a39
+ 00bd2530 bytes bfc21639
- 00b6304c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6304c ["INT_ADD", "register:40f0:8", ["const:b6304c:8", "const:4:8"]]
- 00b6304c ["CALLIND", null, ["register:0:8"]]
+ 00bd254c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd254c ["INT_ADD", "register:40f0:8", ["const:bd254c:8", "const:4:8"]]
+ 00bd254c ["CALLIND", null, ["register:0:8"]]
- 00b6304c bytes 00013fd6
+ 00bd254c bytes 00013fd6
- 00b63050 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b63050 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b63050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd2550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00bd2550 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd2550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b63050 bytes 9f5203f9
+ 00bd2550 bytes 9fd602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ddf1857bbac55fd3bc37fe246a322e1"></a>

### [`00b63064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md) → [`00bd2564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2564.md) _ZN8firebase4auth21android_web_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd25a4",
      "incomplete_value": true,
      "site": "00bd25a4",
      "value": [
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
      "definition_site": "00b630a4",
      "incomplete_value": true,
      "site": "00b630a4",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2580",
      "incomplete_value": true,
      "site": "00bd2580",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63080",
      "incomplete_value": true,
      "site": "00b63080",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2588",
      "incomplete_value": false,
      "site": "00bd259c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63088",
      "incomplete_value": false,
      "site": "00b6309c",
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
            "const:66f:8"
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
      "00bd2578",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2588",
      "PARAM",
      [
        "storage",
        "0029166f",
        null,
        "string"
      ]
    ],
    [
      "00bd25a4",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2578",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2588",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd25a4",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6309c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md#insn-00b6309c) · [`00b630a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md#insn-00b630a4) · [`00b63070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63064.md#insn-00b63070)
- 新版 `00bd259c`（命令位置の公開資料なし） · `00bd25a4`（命令位置の公開資料なし） · `00bd2570`（命令位置の公開資料なし）

~~~diff
- 00b6309c ["INT_ADD", "register:40f0:8", ["const:b6309c:8", "const:4:8"]]
- 00b6309c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd259c ["INT_ADD", "register:40f0:8", ["const:bd259c:8", "const:4:8"]]
+ 00bd259c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6309c bytes fdeb0194
+ 00bd259c bytes 5d210294
- 00b630a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b630a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd25a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00bd25a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b630a4 bytes 805203f9
+ 00bd25a4 bytes 80d602f9
- 00b63070 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd2570 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b63070 bytes f42900d0
+ 00bd2570 bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-341a49da64ff14f4554831d7b731cc49"></a>

### [`00b630d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md) → [`00bd25d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd25d4.md) _ZN8firebase4auth21android_web_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd25f0",
      "incomplete_value": false,
      "site": "00bd25f4",
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
      "definition_site": "00b630f0",
      "incomplete_value": false,
      "site": "00b630f4",
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
      "definition_site": "00bd2600",
      "incomplete_value": true,
      "site": "00bd260c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63100",
      "incomplete_value": true,
      "site": "00b6310c",
      "value": [
        "LOAD",
        "8",
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
      "00bd25f0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd2600",
      "DATA",
      [
        "storage",
        "010a16b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd25f0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd2600",
      "DATA",
      [
        "storage",
        "011265b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b630f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md#insn-00b630f4) · [`00b630ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md#insn-00b630ec) · [`00b630f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b630d4.md#insn-00b630f0)
- 新版 `00bd25f4`（命令位置の公開資料なし） · `00bd25ec`（命令位置の公開資料なし） · `00bd25f0`（命令位置の公開資料なし）

~~~diff
- 00b630f4 ["INT_ADD", "register:40f0:8", ["const:b630f4:8", "const:4:8"]]
- 00b630f4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd25f4 ["INT_ADD", "register:40f0:8", ["const:bd25f4:8", "const:4:8"]]
+ 00bd25f4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b630f4 bytes 23ec0194
+ 00bd25f4 bytes 83210294
- 00b630ec ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd25ec ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b630ec bytes a0b9ffb0
+ 00bd25ec bytes a0b6ffd0
- 00b630f0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b630f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b630f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b630f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd25f0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd25f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd25f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd25f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b630f0 bytes 001c1591
+ 00bd25f0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a03e275f253905aa3b2ddf3f3825b26a"></a>

### [`00b63110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md) → [`00bd2610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2610.md) _ZN8firebase4auth21android_web_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2650",
      "incomplete_value": true,
      "site": "00bd2650",
      "value": [
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
      "definition_site": "00b63150",
      "incomplete_value": true,
      "site": "00b63150",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd262c",
      "incomplete_value": true,
      "site": "00bd262c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6312c",
      "incomplete_value": true,
      "site": "00b6312c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2634",
      "incomplete_value": false,
      "site": "00bd2648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a0000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63134",
      "incomplete_value": false,
      "site": "00b63148",
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
            "const:66f:8"
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
      "00bd2624",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2634",
      "PARAM",
      [
        "storage",
        "0029166f",
        null,
        "string"
      ]
    ],
    [
      "00bd2650",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2624",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2634",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ],
    [
      "00bd2650",
      "WRITE",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md#insn-00b63148) · [`00b63150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md#insn-00b63150) · [`00b6311c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63110.md#insn-00b6311c)
- 新版 `00bd2648`（命令位置の公開資料なし） · `00bd2650`（命令位置の公開資料なし） · `00bd261c`（命令位置の公開資料なし）

~~~diff
- 00b63148 ["INT_ADD", "register:40f0:8", ["const:b63148:8", "const:4:8"]]
- 00b63148 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2648 ["INT_ADD", "register:40f0:8", ["const:bd2648:8", "const:4:8"]]
+ 00bd2648 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63148 bytes d2eb0194
+ 00bd2648 bytes 32210294
- 00b63150 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b63150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2650 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
+ 00bd2650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63150 bytes 805203f9
+ 00bd2650 bytes 80d602f9
- 00b6311c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd261c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6311c bytes f42900d0
+ 00bd261c bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0407627b1c7dcf3872ba5b30d9ac4d54"></a>

### [`00b63180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md) → [`00bd2680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2680.md) _ZN8firebase4auth21android_web_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd269c",
      "incomplete_value": false,
      "site": "00bd26a0",
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
      "definition_site": "00b6319c",
      "incomplete_value": false,
      "site": "00b631a0",
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
      "definition_site": "00bd26ac",
      "incomplete_value": true,
      "site": "00bd26b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b631ac",
      "incomplete_value": true,
      "site": "00b631b8",
      "value": [
        "LOAD",
        "8",
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
      "00bd269c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd26ac",
      "DATA",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd269c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd26ac",
      "DATA",
      [
        "storage",
        "011265c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b631a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md#insn-00b631a0) · [`00b63198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md#insn-00b63198) · [`00b6319c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63180.md#insn-00b6319c)
- 新版 `00bd26a0`（命令位置の公開資料なし） · `00bd2698`（命令位置の公開資料なし） · `00bd269c`（命令位置の公開資料なし）

~~~diff
- 00b631a0 ["INT_ADD", "register:40f0:8", ["const:b631a0:8", "const:4:8"]]
- 00b631a0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd26a0 ["INT_ADD", "register:40f0:8", ["const:bd26a0:8", "const:4:8"]]
+ 00bd26a0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b631a0 bytes f8eb0194
+ 00bd26a0 bytes 58210294
- 00b63198 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd2698 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b63198 bytes a0b9ffd0
+ 00bd2698 bytes a0b6fff0
- 00b6319c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6319c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6319c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6319c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd269c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd269c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd269c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd269c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6319c bytes 00c81791
+ 00bd269c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f562e58667fcba512d061caad58e51f1"></a>

### [`00b631bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md) → [`00bd26bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26bc.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd26e8",
      "incomplete_value": true,
      "site": "00bd26e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631e8",
      "incomplete_value": true,
      "site": "00b631e8",
      "value": [
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
      "definition_site": "00bd26d0",
      "incomplete_value": true,
      "site": "00bd26d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631d0",
      "incomplete_value": true,
      "site": "00b631d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd26dc",
      "incomplete_value": false,
      "site": "00bd26e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:88d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b631dc",
      "incomplete_value": false,
      "site": "00b631e0",
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
      "00bd26cc",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd26dc",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00bd26e8",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd26cc",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd26dc",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "00bd26e8",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b631e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md#insn-00b631e0) · [`00b631e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md#insn-00b631e8) · [`00b631c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631bc.md#insn-00b631c8)
- 新版 `00bd26e0`（命令位置の公開資料なし） · `00bd26e8`（命令位置の公開資料なし） · `00bd26c8`（命令位置の公開資料なし）

~~~diff
- 00b631e0 ["INT_ADD", "register:40f0:8", ["const:b631e0:8", "const:4:8"]]
- 00b631e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd26e0 ["INT_ADD", "register:40f0:8", ["const:bd26e0:8", "const:4:8"]]
+ 00bd26e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b631e0 bytes aceb0194
+ 00bd26e0 bytes 0c210294
- 00b631e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b631e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd26e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
+ 00bd26e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b631e8 bytes 606203f9
+ 00bd26e8 bytes 60e602f9
- 00b631c8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd26c8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b631c8 bytes f32900d0
+ 00bd26c8 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6616332db7163a37c7249e7fc03aef8b"></a>

### [`00b631fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md) → [`00bd26fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd26fc.md) _ZN8firebase4auth23firebase_auth_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2728",
      "incomplete_value": true,
      "site": "00bd2728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "definition_site": "00bd2710",
      "incomplete_value": true,
      "site": "00bd2710",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63210",
      "incomplete_value": true,
      "site": "00b63210",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2718",
      "incomplete_value": false,
      "site": "00bd2720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:88d:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd270c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2718",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00bd2728",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd270c",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2718",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "00bd2728",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md#insn-00b63220) · [`00b63228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md#insn-00b63228) · [`00b63208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b631fc.md#insn-00b63208)
- 新版 `00bd2720`（命令位置の公開資料なし） · `00bd2728`（命令位置の公開資料なし） · `00bd2708`（命令位置の公開資料なし）

~~~diff
- 00b63220 ["INT_ADD", "register:40f0:8", ["const:b63220:8", "const:4:8"]]
- 00b63220 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2720 ["INT_ADD", "register:40f0:8", ["const:bd2720:8", "const:4:8"]]
+ 00bd2720 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63220 bytes 9ceb0194
+ 00bd2720 bytes fc200294
- 00b63228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b63228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2728 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
+ 00bd2728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63228 bytes 606203f9
+ 00bd2728 bytes 60e602f9
- 00b63208 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2708 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63208 bytes f32900d0
+ 00bd2708 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0778ec9ed213df875abcc39aaeda290"></a>

### [`00b6323c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md) → [`00bd273c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd273c.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd276c",
      "incomplete_value": true,
      "site": "00bd276c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "definition_site": "00bd2750",
      "incomplete_value": true,
      "site": "00bd2750",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd275c",
      "incomplete_value": false,
      "site": "00bd2764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:88d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6325c",
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
      "00bd274c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd275c",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00bd276c",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd274c",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd275c",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "00bd276c",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md#insn-00b63264) · [`00b6326c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md#insn-00b6326c) · [`00b63248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6323c.md#insn-00b63248)
- 新版 `00bd2764`（命令位置の公開資料なし） · `00bd276c`（命令位置の公開資料なし） · `00bd2748`（命令位置の公開資料なし）

~~~diff
- 00b63264 ["INT_ADD", "register:40f0:8", ["const:b63264:8", "const:4:8"]]
- 00b63264 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2764 ["INT_ADD", "register:40f0:8", ["const:bd2764:8", "const:4:8"]]
+ 00bd2764 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63264 bytes 8beb0194
+ 00bd2764 bytes eb200294
- 00b6326c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b6326c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd276c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
+ 00bd276c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6326c bytes 606203f9
+ 00bd276c bytes 60e602f9
- 00b63248 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2748 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63248 bytes f32900d0
+ 00bd2748 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3aac57da1d4afc3299ce56a5eafa532"></a>

### [`00b63280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md) → [`00bd2780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2780.md) _ZN8firebase4auth23firebase_auth_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd27b0",
      "incomplete_value": true,
      "site": "00bd27b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b632b0",
      "incomplete_value": true,
      "site": "00b632b0",
      "value": [
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
      "definition_site": "00bd2794",
      "incomplete_value": true,
      "site": "00bd2794",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63294",
      "incomplete_value": true,
      "site": "00b63294",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd279c",
      "incomplete_value": false,
      "site": "00bd27a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:88d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6329c",
      "incomplete_value": false,
      "site": "00b632a8",
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
      "00bd2790",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd279c",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ],
    [
      "00bd27b0",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2790",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd279c",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ],
    [
      "00bd27b0",
      "WRITE",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b632a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md#insn-00b632a8) · [`00b632b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md#insn-00b632b0) · [`00b6328c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63280.md#insn-00b6328c)
- 新版 `00bd27a8`（命令位置の公開資料なし） · `00bd27b0`（命令位置の公開資料なし） · `00bd278c`（命令位置の公開資料なし）

~~~diff
- 00b632a8 ["INT_ADD", "register:40f0:8", ["const:b632a8:8", "const:4:8"]]
- 00b632a8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd27a8 ["INT_ADD", "register:40f0:8", ["const:bd27a8:8", "const:4:8"]]
+ 00bd27a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b632a8 bytes 7aeb0194
+ 00bd27a8 bytes da200294
- 00b632b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b632b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd27b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c8:8"]]
+ 00bd27b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b632b0 bytes 606203f9
+ 00bd27b0 bytes 60e602f9
- 00b6328c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd278c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6328c bytes f32900d0
+ 00bd278c bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8033e5b19aacd11b3a8d7f2c93097567"></a>

### [`00b632d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md) → [`00bd27d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd27d0.md) _ZN8firebase4auth23firebase_auth_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd2828",
      "incomplete_value": true,
      "site": "00bd2828",
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
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63328",
      "incomplete_value": true,
      "site": "00b63328",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2804",
      "incomplete_value": true,
      "site": "00bd2810",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:5c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63304",
      "incomplete_value": true,
      "site": "00b63310",
      "value": [
        "LOAD",
        "8",
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
      "00bd27e4",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2804",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2828",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd27e4",
      "READ",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2804",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2828",
      "WRITE",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md#insn-00b63310) · [`00b63328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md#insn-00b63328) · [`00b632e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b632d0.md#insn-00b632e0)
- 新版 `00bd2810`（命令位置の公開資料なし） · `00bd2828`（命令位置の公開資料なし） · `00bd27e0`（命令位置の公開資料なし）

~~~diff
- 00b63310 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63310 ["INT_ADD", "register:40f0:8", ["const:b63310:8", "const:4:8"]]
- 00b63310 ["CALLIND", null, ["register:0:8"]]
+ 00bd2810 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2810 ["INT_ADD", "register:40f0:8", ["const:bd2810:8", "const:4:8"]]
+ 00bd2810 ["CALLIND", null, ["register:0:8"]]
- 00b63310 bytes 00013fd6
+ 00bd2810 bytes 00013fd6
- 00b63328 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63328 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
- 00b63328 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2828 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2828 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5d0:8"]]
+ 00bd2828 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63328 bytes a0221b39
+ 00bd2828 bytes a0421739
- 00b632e0 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd27e0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b632e0 bytes f52900d0
+ 00bd27e0 bytes b52a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9af10b9909f6c9acdf40f5be2f29a48"></a>

### [`00b6333c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md) → [`00bd283c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd283c.md) _ZN8firebase4auth23firebase_auth_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd2878",
      "incomplete_value": true,
      "site": "00bd2878",
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
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63378",
      "incomplete_value": true,
      "site": "00b63378",
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd2898",
      "incomplete_value": true,
      "site": "00bd2898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63398",
      "incomplete_value": true,
      "site": "00b63398",
      "value": [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd2854",
      "incomplete_value": true,
      "site": "00bd2854",
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
      "definition_site": "00b63354",
      "incomplete_value": true,
      "site": "00b63354",
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
      "00bd2850",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd285c",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2878",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2850",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd285c",
      "READ",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2878",
      "WRITE",
      [
        "storage",
        "011265d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md#insn-00b63378) · [`00b63394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md#insn-00b63394) · [`00b63398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6333c.md#insn-00b63398)
- 新版 `00bd2878`（命令位置の公開資料なし） · `00bd2894`（命令位置の公開資料なし） · `00bd2898`（命令位置の公開資料なし）

~~~diff
- 00b63378 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b63378 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b63378 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
- 00b63378 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd2878 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd2878 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd2878 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5d0:8"]]
+ 00bd2878 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b63378 bytes bf221b39
+ 00bd2878 bytes bf421739
- 00b63394 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63394 ["INT_ADD", "register:40f0:8", ["const:b63394:8", "const:4:8"]]
- 00b63394 ["CALLIND", null, ["register:0:8"]]
+ 00bd2894 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2894 ["INT_ADD", "register:40f0:8", ["const:bd2894:8", "const:4:8"]]
+ 00bd2894 ["CALLIND", null, ["register:0:8"]]
- 00b63394 bytes 00013fd6
+ 00bd2894 bytes 00013fd6
- 00b63398 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b63398 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b63398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd2898 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c8:8"]]
+ 00bd2898 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd2898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b63398 bytes 9f6203f9
+ 00bd2898 bytes 9fe602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10799a07e14e77117fff9ed53c751548"></a>

### [`00b633ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md) → [`00bd28ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd28ac.md) _ZN8firebase4auth23firebase_auth_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b633ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd28ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b633c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b633c0",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b633c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd28f0"
      ]
    ],
    [
      "unmatched:00b633d0",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd28c0",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd28c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd28f0"
      ]
    ],
    [
      "00bd28d0",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b633c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md#insn-00b633c8) · [`00b633e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md#insn-00b633e4) · [`00b633ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b633ac.md#insn-00b633ec)
- 新版 `00bd28e4`（命令位置の公開資料なし）

~~~diff
- 00b633c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b633c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b633c8 bytes 410100b5
- 00b633e4 ["INT_ADD", "register:40f0:8", ["const:b633e4:8", "const:4:8"]]
- 00b633e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd28e4 ["INT_ADD", "register:40f0:8", ["const:bd28e4:8", "const:4:8"]]
+ 00bd28e4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b633e4 bytes 2beb0194
+ 00bd28e4 bytes 8b200294
- 00b633ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b633ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b633ec bytes 806203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31847e620a40367be8d93773b007f7f6"></a>

### [`00b63458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md) → [`00bd2958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2958.md) _ZN8firebase4auth23firebase_auth_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b63498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2998"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63474"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6346c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b63474",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd299c"
      ]
    ],
    [
      "unmatched:00b6347c",
      "PARAM",
      [
        "storage",
        "002ad567",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd296c",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd299c"
      ]
    ],
    [
      "00bd297c",
      "PARAM",
      [
        "storage",
        "002be88d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md#insn-00b63474) · [`00b63490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md#insn-00b63490) · [`00b63498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63458.md#insn-00b63498)
- 新版 `00bd2990`（命令位置の公開資料なし）

~~~diff
- 00b63474 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63474 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b63474 bytes 410100b5
- 00b63490 ["INT_ADD", "register:40f0:8", ["const:b63490:8", "const:4:8"]]
- 00b63490 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2990 ["INT_ADD", "register:40f0:8", ["const:bd2990:8", "const:4:8"]]
+ 00bd2990 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63490 bytes 00eb0194
+ 00bd2990 bytes 60200294
- 00b63498 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b63498 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63498 bytes 806203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36245d1c319af1a3176fbb26637de2d5"></a>

### [`00b634c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md) → [`00bd29c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd29c8.md) _ZN8firebase4auth23firebase_auth_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd29e4",
      "incomplete_value": false,
      "site": "00bd29e8",
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
      "definition_site": "00b634e4",
      "incomplete_value": false,
      "site": "00b634e8",
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
      "definition_site": "00bd29f4",
      "incomplete_value": true,
      "site": "00bd2a00",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b634f4",
      "incomplete_value": true,
      "site": "00b63500",
      "value": [
        "LOAD",
        "8",
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
      "00bd29e4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd29f4",
      "DATA",
      [
        "storage",
        "010a16d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd29e4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd29f4",
      "DATA",
      [
        "storage",
        "011265e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b634e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md#insn-00b634e8) · [`00b634e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md#insn-00b634e0) · [`00b634e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b634c8.md#insn-00b634e4)
- 新版 `00bd29e8`（命令位置の公開資料なし） · `00bd29e0`（命令位置の公開資料なし） · `00bd29e4`（命令位置の公開資料なし）

~~~diff
- 00b634e8 ["INT_ADD", "register:40f0:8", ["const:b634e8:8", "const:4:8"]]
- 00b634e8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd29e8 ["INT_ADD", "register:40f0:8", ["const:bd29e8:8", "const:4:8"]]
+ 00bd29e8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b634e8 bytes 26eb0194
+ 00bd29e8 bytes 86200294
- 00b634e0 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd29e0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b634e0 bytes a0b9ffd0
+ 00bd29e0 bytes a0b6fff0
- 00b634e4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b634e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b634e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b634e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd29e4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd29e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd29e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd29e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b634e4 bytes 00c81791
+ 00bd29e4 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-818de8ff3013c1a1ff76289a366150b3"></a>

### [`00b63504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md) → [`00bd2a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a04.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2a30",
      "incomplete_value": true,
      "site": "00bd2a30",
      "value": [
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
    "old": {
      "definition_site": "00b63530",
      "incomplete_value": true,
      "site": "00b63530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00bd2a18",
      "incomplete_value": true,
      "site": "00bd2a18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63518",
      "incomplete_value": true,
      "site": "00b63518",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2a24",
      "incomplete_value": false,
      "site": "00bd2a28",
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
            "const:a17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63524",
      "incomplete_value": false,
      "site": "00b63528",
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
      "00bd2a14",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2a24",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00bd2a30",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2a14",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2a24",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2a30",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md#insn-00b63528) · [`00b63530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md#insn-00b63530) · [`00b63510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63504.md#insn-00b63510)
- 新版 `00bd2a28`（命令位置の公開資料なし） · `00bd2a30`（命令位置の公開資料なし） · `00bd2a10`（命令位置の公開資料なし）

~~~diff
- 00b63528 ["INT_ADD", "register:40f0:8", ["const:b63528:8", "const:4:8"]]
- 00b63528 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2a28 ["INT_ADD", "register:40f0:8", ["const:bd2a28:8", "const:4:8"]]
+ 00bd2a28 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63528 bytes daea0194
+ 00bd2a28 bytes 3a200294
- 00b63530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63530 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2a30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00bd2a30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63530 bytes 607203f9
+ 00bd2a30 bytes 60f602f9
- 00b63510 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2a10 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63510 bytes f32900d0
+ 00bd2a10 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4352f368866b6c9944c8c636fd03ba87"></a>

### [`00b63544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md) → [`00bd2a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a44.md) _ZN8firebase4auth26firebase_network_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2a70",
      "incomplete_value": true,
      "site": "00bd2a70",
      "value": [
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
    "old": {
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
            "const:6e0:8"
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
      "definition_site": "00bd2a58",
      "incomplete_value": true,
      "site": "00bd2a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63558",
      "incomplete_value": true,
      "site": "00b63558",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2a60",
      "incomplete_value": false,
      "site": "00bd2a68",
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
            "const:a17:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00bd2a54",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2a60",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00bd2a70",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2a54",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2a60",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2a70",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md#insn-00b63568) · [`00b63570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md#insn-00b63570) · [`00b63550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63544.md#insn-00b63550)
- 新版 `00bd2a68`（命令位置の公開資料なし） · `00bd2a70`（命令位置の公開資料なし） · `00bd2a50`（命令位置の公開資料なし）

~~~diff
- 00b63568 ["INT_ADD", "register:40f0:8", ["const:b63568:8", "const:4:8"]]
- 00b63568 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2a68 ["INT_ADD", "register:40f0:8", ["const:bd2a68:8", "const:4:8"]]
+ 00bd2a68 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63568 bytes caea0194
+ 00bd2a68 bytes 2a200294
- 00b63570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b63570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2a70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00bd2a70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63570 bytes 607203f9
+ 00bd2a70 bytes 60f602f9
- 00b63550 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2a50 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63550 bytes f32900d0
+ 00bd2a50 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4366ad62866624a226ed2e2a1a4b44c1"></a>

### [`00b63584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md) → [`00bd2a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2a84.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2ab4",
      "incomplete_value": true,
      "site": "00bd2ab4",
      "value": [
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
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00bd2a98",
      "incomplete_value": true,
      "site": "00bd2a98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd2aa4",
      "incomplete_value": false,
      "site": "00bd2aac",
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
            "const:a17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b635a4",
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
      "00bd2a94",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2aa4",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00bd2ab4",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2a94",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2aa4",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2ab4",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b635ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md#insn-00b635ac) · [`00b635b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md#insn-00b635b4) · [`00b63590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63584.md#insn-00b63590)
- 新版 `00bd2aac`（命令位置の公開資料なし） · `00bd2ab4`（命令位置の公開資料なし） · `00bd2a90`（命令位置の公開資料なし）

~~~diff
- 00b635ac ["INT_ADD", "register:40f0:8", ["const:b635ac:8", "const:4:8"]]
- 00b635ac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2aac ["INT_ADD", "register:40f0:8", ["const:bd2aac:8", "const:4:8"]]
+ 00bd2aac ["CALL", null, ["callee:00c5ab10:8"]]
- 00b635ac bytes b9ea0194
+ 00bd2aac bytes 19200294
- 00b635b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b635b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2ab4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00bd2ab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b635b4 bytes 607203f9
+ 00bd2ab4 bytes 60f602f9
- 00b63590 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2a90 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63590 bytes f32900d0
+ 00bd2a90 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d5873741ae192913e7c9f29840e5cc"></a>

### [`00b635c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md) → [`00bd2ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ac8.md) _ZN8firebase4auth26firebase_network_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2af8",
      "incomplete_value": true,
      "site": "00bd2af8",
      "value": [
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
    "old": {
      "definition_site": "00b635f8",
      "incomplete_value": true,
      "site": "00b635f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00bd2adc",
      "incomplete_value": true,
      "site": "00bd2adc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b635dc",
      "incomplete_value": true,
      "site": "00b635dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2ae4",
      "incomplete_value": false,
      "site": "00bd2af0",
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
            "const:a17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b635e4",
      "incomplete_value": false,
      "site": "00b635f0",
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
      "00bd2ad8",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2ae4",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00bd2af8",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2ad8",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2ae4",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2af8",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b635f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md#insn-00b635f0) · [`00b635f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md#insn-00b635f8) · [`00b635d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b635c8.md#insn-00b635d4)
- 新版 `00bd2af0`（命令位置の公開資料なし） · `00bd2af8`（命令位置の公開資料なし） · `00bd2ad4`（命令位置の公開資料なし）

~~~diff
- 00b635f0 ["INT_ADD", "register:40f0:8", ["const:b635f0:8", "const:4:8"]]
- 00b635f0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2af0 ["INT_ADD", "register:40f0:8", ["const:bd2af0:8", "const:4:8"]]
+ 00bd2af0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b635f0 bytes a8ea0194
+ 00bd2af0 bytes 08200294
- 00b635f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b635f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2af8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00bd2af8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b635f8 bytes 607203f9
+ 00bd2af8 bytes 60f602f9
- 00b635d4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2ad4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b635d4 bytes f32900d0
+ 00bd2ad4 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a56d31d2eb78420839848d949484ea"></a>

### [`00b63618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md) → [`00bd2b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b18.md) _ZN8firebase4auth26firebase_network_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd2b70",
      "incomplete_value": true,
      "site": "00bd2b70",
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
    "old": {
      "definition_site": "00b63670",
      "incomplete_value": true,
      "site": "00b63670",
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
            "const:6e8:8"
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
      "definition_site": "00bd2b4c",
      "incomplete_value": true,
      "site": "00bd2b58",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
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
    "old": {
      "definition_site": "00b6364c",
      "incomplete_value": true,
      "site": "00b63658",
      "value": [
        "LOAD",
        "8",
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
      "00bd2b2c",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2b4c",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2b70",
      "WRITE",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2b2c",
      "READ",
      [
        "storage",
        "011265f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2b4c",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2b70",
      "WRITE",
      [
        "storage",
        "011265f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md#insn-00b63658) · [`00b63670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md#insn-00b63670) · [`00b63628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63618.md#insn-00b63628)
- 新版 `00bd2b58`（命令位置の公開資料なし） · `00bd2b70`（命令位置の公開資料なし） · `00bd2b28`（命令位置の公開資料なし）

~~~diff
- 00b63658 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63658 ["INT_ADD", "register:40f0:8", ["const:b63658:8", "const:4:8"]]
- 00b63658 ["CALLIND", null, ["register:0:8"]]
+ 00bd2b58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2b58 ["INT_ADD", "register:40f0:8", ["const:bd2b58:8", "const:4:8"]]
+ 00bd2b58 ["CALLIND", null, ["register:0:8"]]
- 00b63658 bytes 00013fd6
+ 00bd2b58 bytes 00013fd6
- 00b63670 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63670 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e8:8"]]
- 00b63670 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2b70 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2b70 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5f0:8"]]
+ 00bd2b70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63670 bytes a0a21b39
+ 00bd2b70 bytes a0c21739
- 00b63628 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd2b28 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b63628 bytes f52900d0
+ 00bd2b28 bytes b52a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2c288a23f31ef176aed20a570275d62"></a>

### [`00b63684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md) → [`00bd2b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2b84.md) _ZN8firebase4auth26firebase_network_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "site": "00b63684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63684",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63688",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6368c",
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
      "00bd2b84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd2b88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd2b8c",
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

- 旧版 [`00b63684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md#insn-00b63684) · [`00b63688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md#insn-00b63688) · [`00b6368c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63684.md#insn-00b6368c)

~~~diff
- 00b63684 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b63684 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b63684 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b63684 bytes f50f1df8
- 00b63688 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b63688 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b63688 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b63688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63688 bytes f44f01a9
- 00b6368c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6368c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6368c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6368c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6368c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74121d293e1647e94f57bb5a13ed344"></a>

### [`00b636f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md) → [`00bd2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2bf4.md) _ZN8firebase4auth26firebase_network_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b63734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd2c34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63710"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63708",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b63710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2c38"
      ]
    ],
    [
      "unmatched:00b63718",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd2c08",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2c10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd2c38"
      ]
    ],
    [
      "00bd2c18",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md#insn-00b63710) · [`00b6372c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md#insn-00b6372c) · [`00b63734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b636f4.md#insn-00b63734)
- 新版 `00bd2c2c`（命令位置の公開資料なし）

~~~diff
- 00b63710 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63710 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b63710 bytes 410100b5
- 00b6372c ["INT_ADD", "register:40f0:8", ["const:b6372c:8", "const:4:8"]]
- 00b6372c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2c2c ["INT_ADD", "register:40f0:8", ["const:bd2c2c:8", "const:4:8"]]
+ 00bd2c2c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6372c bytes 59ea0194
+ 00bd2c2c bytes b91f0294
- 00b63734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b63734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63734 bytes 807203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d168fc62ebe220e80be449ef7b79b628"></a>

### [`00b63764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md) → [`00bd2c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2c64.md) _ZN8firebase4auth26firebase_network_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2c80",
      "incomplete_value": false,
      "site": "00bd2c84",
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
      "definition_site": "00b63780",
      "incomplete_value": false,
      "site": "00b63784",
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
      "definition_site": "00bd2c90",
      "incomplete_value": true,
      "site": "00bd2c9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63790",
      "incomplete_value": true,
      "site": "00b6379c",
      "value": [
        "LOAD",
        "8",
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
      "00bd2c80",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd2c90",
      "DATA",
      [
        "storage",
        "010a16f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2c80",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd2c90",
      "DATA",
      [
        "storage",
        "011265f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md#insn-00b63784) · [`00b6377c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md#insn-00b6377c) · [`00b63780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63764.md#insn-00b63780)
- 新版 `00bd2c84`（命令位置の公開資料なし） · `00bd2c7c`（命令位置の公開資料なし） · `00bd2c80`（命令位置の公開資料なし）

~~~diff
- 00b63784 ["INT_ADD", "register:40f0:8", ["const:b63784:8", "const:4:8"]]
- 00b63784 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd2c84 ["INT_ADD", "register:40f0:8", ["const:bd2c84:8", "const:4:8"]]
+ 00bd2c84 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b63784 bytes 7fea0194
+ 00bd2c84 bytes df1f0294
- 00b6377c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd2c7c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b6377c bytes a0b9ffb0
+ 00bd2c7c bytes a0b6ffd0
- 00b63780 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b63780 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63780 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63780 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2c80 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd2c80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2c80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2c80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63780 bytes 001c1591
+ 00bd2c80 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-382a917053cfc60ce8b4bde037a1c139"></a>

### [`00b637a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md) → [`00bd2ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ca0.md) _ZN8firebase4auth26firebase_network_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2ce0",
      "incomplete_value": true,
      "site": "00bd2ce0",
      "value": [
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
    "old": {
      "definition_site": "00b637e0",
      "incomplete_value": true,
      "site": "00b637e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00bd2cbc",
      "incomplete_value": true,
      "site": "00bd2cbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b637bc",
      "incomplete_value": true,
      "site": "00b637bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2cc4",
      "incomplete_value": false,
      "site": "00bd2cd8",
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
            "const:a17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b637c4",
      "incomplete_value": false,
      "site": "00b637d8",
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
      "00bd2cb4",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2cc4",
      "PARAM",
      [
        "storage",
        "002ae533",
        null,
        "string"
      ]
    ],
    [
      "00bd2ce0",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd2cb4",
      "READ",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2cc4",
      "PARAM",
      [
        "storage",
        "002bfa17",
        null,
        "string"
      ]
    ],
    [
      "00bd2ce0",
      "WRITE",
      [
        "storage",
        "011265e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b637d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md#insn-00b637d8) · [`00b637e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md#insn-00b637e0) · [`00b637ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b637a0.md#insn-00b637ac)
- 新版 `00bd2cd8`（命令位置の公開資料なし） · `00bd2ce0`（命令位置の公開資料なし） · `00bd2cac`（命令位置の公開資料なし）

~~~diff
- 00b637d8 ["INT_ADD", "register:40f0:8", ["const:b637d8:8", "const:4:8"]]
- 00b637d8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2cd8 ["INT_ADD", "register:40f0:8", ["const:bd2cd8:8", "const:4:8"]]
+ 00bd2cd8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b637d8 bytes 2eea0194
+ 00bd2cd8 bytes 8e1f0294
- 00b637e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b637e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2ce0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00bd2ce0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b637e0 bytes 807203f9
+ 00bd2ce0 bytes 80f602f9
- 00b637ac ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd2cac ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b637ac bytes f42900d0
+ 00bd2cac bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ccb4433d4b35de9313c1d4b94cd8f31"></a>

### [`00b63810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md) → [`00bd2d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d10.md) _ZN8firebase4auth26firebase_network_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2d2c",
      "incomplete_value": false,
      "site": "00bd2d30",
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
      "definition_site": "00b6382c",
      "incomplete_value": false,
      "site": "00b63830",
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
      "definition_site": "00bd2d3c",
      "incomplete_value": true,
      "site": "00bd2d48",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6383c",
      "incomplete_value": true,
      "site": "00b63848",
      "value": [
        "LOAD",
        "8",
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
      "00bd2d2c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd2d3c",
      "DATA",
      [
        "storage",
        "010a16f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2d2c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd2d3c",
      "DATA",
      [
        "storage",
        "01126600",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md#insn-00b63830) · [`00b63828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md#insn-00b63828) · [`00b6382c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63810.md#insn-00b6382c)
- 新版 `00bd2d30`（命令位置の公開資料なし） · `00bd2d28`（命令位置の公開資料なし） · `00bd2d2c`（命令位置の公開資料なし）

~~~diff
- 00b63830 ["INT_ADD", "register:40f0:8", ["const:b63830:8", "const:4:8"]]
- 00b63830 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd2d30 ["INT_ADD", "register:40f0:8", ["const:bd2d30:8", "const:4:8"]]
+ 00bd2d30 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b63830 bytes 54ea0194
+ 00bd2d30 bytes b41f0294
- 00b63828 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd2d28 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b63828 bytes a0b9ffd0
+ 00bd2d28 bytes a0b6fff0
- 00b6382c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6382c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6382c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6382c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2d2c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd2d2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2d2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2d2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6382c bytes 00c81791
+ 00bd2d2c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac7cd5ef15a1c207860921969d345deb"></a>

### [`00b6384c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md) → [`00bd2d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d4c.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2d78",
      "incomplete_value": true,
      "site": "00bd2d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63878",
      "incomplete_value": true,
      "site": "00b63878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd2d60",
      "incomplete_value": true,
      "site": "00bd2d60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63860",
      "incomplete_value": true,
      "site": "00b63860",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2d6c",
      "incomplete_value": false,
      "site": "00bd2d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:bd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6386c",
      "incomplete_value": false,
      "site": "00b63870",
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
            "const:1ab:8"
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
      "00bd2d5c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2d6c",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00bd2d78",
      "WRITE",
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
      "00bd2d5c",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2d6c",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd2d78",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md#insn-00b63870) · [`00b63878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md#insn-00b63878) · [`00b63858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6384c.md#insn-00b63858)
- 新版 `00bd2d70`（命令位置の公開資料なし） · `00bd2d78`（命令位置の公開資料なし） · `00bd2d58`（命令位置の公開資料なし）

~~~diff
- 00b63870 ["INT_ADD", "register:40f0:8", ["const:b63870:8", "const:4:8"]]
- 00b63870 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2d70 ["INT_ADD", "register:40f0:8", ["const:bd2d70:8", "const:4:8"]]
+ 00bd2d70 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63870 bytes 08ea0194
+ 00bd2d70 bytes 681f0294
- 00b63878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b63878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2d78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00bd2d78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63878 bytes 608203f9
+ 00bd2d78 bytes 600603f9
- 00b63858 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2d58 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63858 bytes f32900d0
+ 00bd2d58 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2409a75be533b961de9ecc706057a448"></a>

### [`00b6388c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md) → [`00bd2d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2d8c.md) _ZN8firebase4auth27too_many_requests_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2db8",
      "incomplete_value": true,
      "site": "00bd2db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638b8",
      "incomplete_value": true,
      "site": "00b638b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd2da0",
      "incomplete_value": true,
      "site": "00bd2da0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638a0",
      "incomplete_value": true,
      "site": "00b638a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2da8",
      "incomplete_value": false,
      "site": "00bd2db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:bd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638a8",
      "incomplete_value": false,
      "site": "00b638b0",
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
            "const:1ab:8"
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
      "00bd2d9c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2da8",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00bd2db8",
      "WRITE",
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
      "00bd2d9c",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2da8",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd2db8",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b638b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md#insn-00b638b0) · [`00b638b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md#insn-00b638b8) · [`00b63898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b6388c.md#insn-00b63898)
- 新版 `00bd2db0`（命令位置の公開資料なし） · `00bd2db8`（命令位置の公開資料なし） · `00bd2d98`（命令位置の公開資料なし）

~~~diff
- 00b638b0 ["INT_ADD", "register:40f0:8", ["const:b638b0:8", "const:4:8"]]
- 00b638b0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2db0 ["INT_ADD", "register:40f0:8", ["const:bd2db0:8", "const:4:8"]]
+ 00bd2db0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b638b0 bytes f8e90194
+ 00bd2db0 bytes 581f0294
- 00b638b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b638b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2db8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00bd2db8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b638b8 bytes 608203f9
+ 00bd2db8 bytes 600603f9
- 00b63898 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2d98 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63898 bytes f32900d0
+ 00bd2d98 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d9d6c7fd09916f91e80e2fb409aaa3f"></a>

### [`00b638cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md) → [`00bd2dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2dcc.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2dfc",
      "incomplete_value": true,
      "site": "00bd2dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638fc",
      "incomplete_value": true,
      "site": "00b638fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd2de0",
      "incomplete_value": true,
      "site": "00bd2de0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638e0",
      "incomplete_value": true,
      "site": "00b638e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2dec",
      "incomplete_value": false,
      "site": "00bd2df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:bd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638ec",
      "incomplete_value": false,
      "site": "00b638f4",
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
            "const:1ab:8"
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
      "00bd2ddc",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2dec",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00bd2dfc",
      "WRITE",
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
      "00bd2ddc",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2dec",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd2dfc",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b638f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md#insn-00b638f4) · [`00b638fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md#insn-00b638fc) · [`00b638d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b638cc.md#insn-00b638d8)
- 新版 `00bd2df4`（命令位置の公開資料なし） · `00bd2dfc`（命令位置の公開資料なし） · `00bd2dd8`（命令位置の公開資料なし）

~~~diff
- 00b638f4 ["INT_ADD", "register:40f0:8", ["const:b638f4:8", "const:4:8"]]
- 00b638f4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2df4 ["INT_ADD", "register:40f0:8", ["const:bd2df4:8", "const:4:8"]]
+ 00bd2df4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b638f4 bytes e7e90194
+ 00bd2df4 bytes 471f0294
- 00b638fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b638fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2dfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00bd2dfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b638fc bytes 608203f9
+ 00bd2dfc bytes 600603f9
- 00b638d8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2dd8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b638d8 bytes f32900d0
+ 00bd2dd8 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1fff032f14481abd98b05059bb396c0"></a>

### [`00b63910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md) → [`00bd2e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e10.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2e40",
      "incomplete_value": true,
      "site": "00bd2e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63940",
      "incomplete_value": true,
      "site": "00b63940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd2e24",
      "incomplete_value": true,
      "site": "00bd2e24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63924",
      "incomplete_value": true,
      "site": "00b63924",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2e2c",
      "incomplete_value": false,
      "site": "00bd2e38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:bd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6392c",
      "incomplete_value": false,
      "site": "00b63938",
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
            "const:1ab:8"
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
      "00bd2e20",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2e2c",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00bd2e40",
      "WRITE",
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
      "00bd2e20",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2e2c",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd2e40",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md#insn-00b63938) · [`00b63940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md#insn-00b63940) · [`00b6391c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63910.md#insn-00b6391c)
- 新版 `00bd2e38`（命令位置の公開資料なし） · `00bd2e40`（命令位置の公開資料なし） · `00bd2e1c`（命令位置の公開資料なし）

~~~diff
- 00b63938 ["INT_ADD", "register:40f0:8", ["const:b63938:8", "const:4:8"]]
- 00b63938 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2e38 ["INT_ADD", "register:40f0:8", ["const:bd2e38:8", "const:4:8"]]
+ 00bd2e38 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63938 bytes d6e90194
+ 00bd2e38 bytes 361f0294
- 00b63940 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b63940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
+ 00bd2e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63940 bytes 608203f9
+ 00bd2e40 bytes 600603f9
- 00b6391c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2e1c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6391c bytes f32900d0
+ 00bd2e1c bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69ec1b2e829d3a40487bc2e3085b27a2"></a>

### [`00b63960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md) → [`00bd2e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2e60.md) _ZN8firebase4auth27too_many_requests_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd2eb8",
      "incomplete_value": true,
      "site": "00bd2eb8",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b639b8",
      "incomplete_value": true,
      "site": "00b639b8",
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
            "const:708:8"
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
      "definition_site": "00bd2e94",
      "incomplete_value": true,
      "site": "00bd2ea0",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:608:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63994",
      "incomplete_value": true,
      "site": "00b639a0",
      "value": [
        "LOAD",
        "8",
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
      "00bd2e74",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2e94",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2eb8",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2e74",
      "READ",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2e94",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2eb8",
      "WRITE",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b639a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md#insn-00b639a0) · [`00b639b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md#insn-00b639b8) · [`00b63970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63960.md#insn-00b63970)
- 新版 `00bd2ea0`（命令位置の公開資料なし） · `00bd2eb8`（命令位置の公開資料なし） · `00bd2e70`（命令位置の公開資料なし）

~~~diff
- 00b639a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b639a0 ["INT_ADD", "register:40f0:8", ["const:b639a0:8", "const:4:8"]]
- 00b639a0 ["CALLIND", null, ["register:0:8"]]
+ 00bd2ea0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2ea0 ["INT_ADD", "register:40f0:8", ["const:bd2ea0:8", "const:4:8"]]
+ 00bd2ea0 ["CALLIND", null, ["register:0:8"]]
- 00b639a0 bytes 00013fd6
+ 00bd2ea0 bytes 00013fd6
- 00b639b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b639b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:708:8"]]
- 00b639b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd2eb8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd2eb8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:610:8"]]
+ 00bd2eb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b639b8 bytes a0221c39
+ 00bd2eb8 bytes a0421839
- 00b63970 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd2e70 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b63970 bytes f52900d0
+ 00bd2e70 bytes b52a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0522441de8e741d525357ad492e40381"></a>

### [`00b639cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md) → [`00bd2ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2ecc.md) _ZN8firebase4auth27too_many_requests_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd2f08",
      "incomplete_value": true,
      "site": "00bd2f08",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a08",
      "incomplete_value": true,
      "site": "00b63a08",
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
            "const:708:8"
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
      "definition_site": "00bd2f28",
      "incomplete_value": true,
      "site": "00bd2f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a28",
      "incomplete_value": true,
      "site": "00b63a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd2ee4",
      "incomplete_value": true,
      "site": "00bd2ee4",
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
      "definition_site": "00b639e4",
      "incomplete_value": true,
      "site": "00b639e4",
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
      "00bd2ee0",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2eec",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2f08",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd2ee0",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2eec",
      "READ",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd2f08",
      "WRITE",
      [
        "storage",
        "01126610",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md#insn-00b63a08) · [`00b63a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md#insn-00b63a24) · [`00b63a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b639cc.md#insn-00b63a28)
- 新版 `00bd2f08`（命令位置の公開資料なし） · `00bd2f24`（命令位置の公開資料なし） · `00bd2f28`（命令位置の公開資料なし）

~~~diff
- 00b63a08 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b63a08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b63a08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:708:8"]]
- 00b63a08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd2f08 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd2f08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd2f08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:610:8"]]
+ 00bd2f08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b63a08 bytes bf221c39
+ 00bd2f08 bytes bf421839
- 00b63a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63a24 ["INT_ADD", "register:40f0:8", ["const:b63a24:8", "const:4:8"]]
- 00b63a24 ["CALLIND", null, ["register:0:8"]]
+ 00bd2f24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd2f24 ["INT_ADD", "register:40f0:8", ["const:bd2f24:8", "const:4:8"]]
+ 00bd2f24 ["CALLIND", null, ["register:0:8"]]
- 00b63a24 bytes 00013fd6
+ 00bd2f24 bytes 00013fd6
- 00b63a28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b63a28 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b63a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd2f28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
+ 00bd2f28 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd2f28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b63a28 bytes 9f8203f9
+ 00bd2f28 bytes 9f0603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bdf2d734a4d8f1ef315eaf6fbc581b4"></a>

### [`00b63a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md) → [`00bd2f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2f3c.md) _ZN8firebase4auth27too_many_requests_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2f7c",
      "incomplete_value": true,
      "site": "00bd2f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a7c",
      "incomplete_value": true,
      "site": "00b63a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd2f58",
      "incomplete_value": true,
      "site": "00bd2f58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a58",
      "incomplete_value": true,
      "site": "00b63a58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd2f60",
      "incomplete_value": false,
      "site": "00bd2f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:bd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a60",
      "incomplete_value": false,
      "site": "00b63a74",
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
            "const:1ab:8"
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
      "00bd2f50",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2f60",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00bd2f7c",
      "WRITE",
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
      "00bd2f50",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd2f60",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd2f7c",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md#insn-00b63a74) · [`00b63a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md#insn-00b63a7c) · [`00b63a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63a3c.md#insn-00b63a48)
- 新版 `00bd2f74`（命令位置の公開資料なし） · `00bd2f7c`（命令位置の公開資料なし） · `00bd2f48`（命令位置の公開資料なし）

~~~diff
- 00b63a74 ["INT_ADD", "register:40f0:8", ["const:b63a74:8", "const:4:8"]]
- 00b63a74 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2f74 ["INT_ADD", "register:40f0:8", ["const:bd2f74:8", "const:4:8"]]
+ 00bd2f74 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63a74 bytes 87e90194
+ 00bd2f74 bytes e71e0294
- 00b63a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b63a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2f7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
+ 00bd2f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63a7c bytes 808203f9
+ 00bd2f7c bytes 800603f9
- 00b63a48 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd2f48 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b63a48 bytes f42900d0
+ 00bd2f48 bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6146ab326c3a54a8c9b34a0f8213a804"></a>

### [`00b63aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md) → [`00bd2fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fac.md) _ZN8firebase4auth27too_many_requests_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd2fc8",
      "incomplete_value": false,
      "site": "00bd2fcc",
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
      "definition_site": "00b63ac8",
      "incomplete_value": false,
      "site": "00b63acc",
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
      "definition_site": "00bd2fd8",
      "incomplete_value": true,
      "site": "00bd2fe4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63ad8",
      "incomplete_value": true,
      "site": "00b63ae4",
      "value": [
        "LOAD",
        "8",
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
      "00bd2fc8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd2fd8",
      "DATA",
      [
        "storage",
        "010a1710",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd2fc8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd2fd8",
      "DATA",
      [
        "storage",
        "01126618",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md#insn-00b63acc) · [`00b63ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md#insn-00b63ac4) · [`00b63ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63aac.md#insn-00b63ac8)
- 新版 `00bd2fcc`（命令位置の公開資料なし） · `00bd2fc4`（命令位置の公開資料なし） · `00bd2fc8`（命令位置の公開資料なし）

~~~diff
- 00b63acc ["INT_ADD", "register:40f0:8", ["const:b63acc:8", "const:4:8"]]
- 00b63acc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd2fcc ["INT_ADD", "register:40f0:8", ["const:bd2fcc:8", "const:4:8"]]
+ 00bd2fcc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b63acc bytes ade90194
+ 00bd2fcc bytes 0d1f0294
- 00b63ac4 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd2fc4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b63ac4 bytes a0b9ffb0
+ 00bd2fc4 bytes a0b6ffd0
- 00b63ac8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b63ac8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63ac8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63ac8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd2fc8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd2fc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2fc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd2fc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63ac8 bytes 001c1591
+ 00bd2fc8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d041898a9dd427e302dd44a7d3e7410a"></a>

### [`00b63ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md) → [`00bd2fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd2fe8.md) _ZN8firebase4auth27too_many_requests_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd3028",
      "incomplete_value": true,
      "site": "00bd3028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b28",
      "incomplete_value": true,
      "site": "00b63b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00bd3004",
      "incomplete_value": true,
      "site": "00bd3004",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b04",
      "incomplete_value": true,
      "site": "00b63b04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd300c",
      "incomplete_value": false,
      "site": "00bd3020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:bd9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b0c",
      "incomplete_value": false,
      "site": "00b63b20",
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
            "const:1ab:8"
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
      "00bd2ffc",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd300c",
      "PARAM",
      [
        "storage",
        "002a51ab",
        null,
        "string"
      ]
    ],
    [
      "00bd3028",
      "WRITE",
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
      "00bd2ffc",
      "READ",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd300c",
      "PARAM",
      [
        "storage",
        "002b5bd9",
        null,
        "string"
      ]
    ],
    [
      "00bd3028",
      "WRITE",
      [
        "storage",
        "01126608",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md#insn-00b63b20) · [`00b63b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md#insn-00b63b28) · [`00b63af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ae8.md#insn-00b63af4)
- 新版 `00bd3020`（命令位置の公開資料なし） · `00bd3028`（命令位置の公開資料なし） · `00bd2ff4`（命令位置の公開資料なし）

~~~diff
- 00b63b20 ["INT_ADD", "register:40f0:8", ["const:b63b20:8", "const:4:8"]]
- 00b63b20 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd3020 ["INT_ADD", "register:40f0:8", ["const:bd3020:8", "const:4:8"]]
+ 00bd3020 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63b20 bytes 5ce90194
+ 00bd3020 bytes bc1e0294
- 00b63b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b63b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3028 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:608:8"]]
+ 00bd3028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63b28 bytes 808203f9
+ 00bd3028 bytes 800603f9
- 00b63af4 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd2ff4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b63af4 bytes f42900d0
+ 00bd2ff4 bytes b42a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ee97468bb14d281ffd9160c151dc44"></a>

### [`00b63b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63b94.md) → [`00bd3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3094.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd30c0",
      "incomplete_value": true,
      "site": "00bd30c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63bc0",
      "incomplete_value": true,
      "site": "00b63bc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00bd30a8",
      "incomplete_value": true,
      "site": "00bd30a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63ba8",
      "incomplete_value": true,
      "site": "00b63ba8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd30b4",
      "incomplete_value": false,
      "site": "00bd30b8",
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
            "const:c6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63bb4",
      "incomplete_value": false,
      "site": "00b63bb8",
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
            "const:483:8"
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
      "00bd30a4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd30b4",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00bd30c0",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd30a4",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd30b4",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ],
    [
      "00bd30c0",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63b94.md#insn-00b63bb8) · [`00b63bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63b94.md#insn-00b63bc0) · [`00b63ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63b94.md#insn-00b63ba0)
- 新版 `00bd30b8`（命令位置の公開資料なし） · `00bd30c0`（命令位置の公開資料なし） · `00bd30a0`（命令位置の公開資料なし）

~~~diff
- 00b63bb8 ["INT_ADD", "register:40f0:8", ["const:b63bb8:8", "const:4:8"]]
- 00b63bb8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd30b8 ["INT_ADD", "register:40f0:8", ["const:bd30b8:8", "const:4:8"]]
+ 00bd30b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63bb8 bytes 36e90194
+ 00bd30b8 bytes 961e0294
- 00b63bc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b63bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd30c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
+ 00bd30c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63bc0 bytes 609203f9
+ 00bd30c0 bytes 601603f9
- 00b63ba0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd30a0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63ba0 bytes f32900d0
+ 00bd30a0 bytes 932a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87c9aacedb7bc3326b7994142318c421"></a>

### [`00b63bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63bd4.md) → [`00bd30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd30d4.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd3100",
      "incomplete_value": true,
      "site": "00bd3100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63c00",
      "incomplete_value": true,
      "site": "00b63c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00bd30e8",
      "incomplete_value": true,
      "site": "00bd30e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63be8",
      "incomplete_value": true,
      "site": "00b63be8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd30f0",
      "incomplete_value": false,
      "site": "00bd30f8",
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
            "const:c6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63bf0",
      "incomplete_value": false,
      "site": "00b63bf8",
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
            "const:483:8"
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
      "00bd30e4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd30f0",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00bd3100",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd30e4",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd30f0",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ],
    [
      "00bd3100",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63bd4.md#insn-00b63bf8) · [`00b63c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63bd4.md#insn-00b63c00) · [`00b63be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63bd4.md#insn-00b63be0)
- 新版 `00bd30f8`（命令位置の公開資料なし） · `00bd3100`（命令位置の公開資料なし） · `00bd30e0`（命令位置の公開資料なし）

~~~diff
- 00b63bf8 ["INT_ADD", "register:40f0:8", ["const:b63bf8:8", "const:4:8"]]
- 00b63bf8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd30f8 ["INT_ADD", "register:40f0:8", ["const:bd30f8:8", "const:4:8"]]
+ 00bd30f8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63bf8 bytes 26e90194
+ 00bd30f8 bytes 861e0294
- 00b63c00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b63c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3100 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
+ 00bd3100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63c00 bytes 609203f9
+ 00bd3100 bytes 601603f9
- 00b63be0 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd30e0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63be0 bytes f32900d0
+ 00bd30e0 bytes 932a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353909009887a482ba2eb81c24103a08"></a>

### [`00b63c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63c58.md) → [`00bd3158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3158.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd3188",
      "incomplete_value": true,
      "site": "00bd3188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63c88",
      "incomplete_value": true,
      "site": "00b63c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00bd316c",
      "incomplete_value": true,
      "site": "00bd316c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63c6c",
      "incomplete_value": true,
      "site": "00b63c6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd3174",
      "incomplete_value": false,
      "site": "00bd3180",
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
            "const:c6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63c74",
      "incomplete_value": false,
      "site": "00b63c80",
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
            "const:483:8"
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
      "00bd3168",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3174",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00bd3188",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3168",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3174",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ],
    [
      "00bd3188",
      "WRITE",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63c58.md#insn-00b63c80) · [`00b63c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63c58.md#insn-00b63c88) · [`00b63c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63c58.md#insn-00b63c64)
- 新版 `00bd3180`（命令位置の公開資料なし） · `00bd3188`（命令位置の公開資料なし） · `00bd3164`（命令位置の公開資料なし）

~~~diff
- 00b63c80 ["INT_ADD", "register:40f0:8", ["const:b63c80:8", "const:4:8"]]
- 00b63c80 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd3180 ["INT_ADD", "register:40f0:8", ["const:bd3180:8", "const:4:8"]]
+ 00bd3180 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63c80 bytes 04e90194
+ 00bd3180 bytes 641e0294
- 00b63c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b63c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd3188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:628:8"]]
+ 00bd3188 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63c88 bytes 609203f9
+ 00bd3188 bytes 601603f9
- 00b63c64 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd3164 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b63c64 bytes f32900d0
+ 00bd3164 bytes 932a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a570d5da2831b3e825a7d6669ea188e"></a>

### [`00b63ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ca8.md) → [`00bd31a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd31a8.md) _ZN8firebase4auth18firebase_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd3200",
      "incomplete_value": true,
      "site": "00bd3200",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63d00",
      "incomplete_value": true,
      "site": "00b63d00",
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
            "const:728:8"
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
      "definition_site": "00bd31dc",
      "incomplete_value": true,
      "site": "00bd31e8",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:628:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63cdc",
      "incomplete_value": true,
      "site": "00b63ce8",
      "value": [
        "LOAD",
        "8",
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
      "00bd31bc",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd31dc",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3200",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd31bc",
      "READ",
      [
        "storage",
        "01126630",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd31dc",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3200",
      "WRITE",
      [
        "storage",
        "01126630",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ca8.md#insn-00b63ce8) · [`00b63d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ca8.md#insn-00b63d00) · [`00b63cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ca8.md#insn-00b63cb8)
- 新版 `00bd31e8`（命令位置の公開資料なし） · `00bd3200`（命令位置の公開資料なし） · `00bd31b8`（命令位置の公開資料なし）

~~~diff
- 00b63ce8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63ce8 ["INT_ADD", "register:40f0:8", ["const:b63ce8:8", "const:4:8"]]
- 00b63ce8 ["CALLIND", null, ["register:0:8"]]
+ 00bd31e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd31e8 ["INT_ADD", "register:40f0:8", ["const:bd31e8:8", "const:4:8"]]
+ 00bd31e8 ["CALLIND", null, ["register:0:8"]]
- 00b63ce8 bytes 00013fd6
+ 00bd31e8 bytes 00013fd6
- 00b63d00 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63d00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:728:8"]]
- 00b63d00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd3200 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd3200 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:630:8"]]
+ 00bd3200 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63d00 bytes a0a21c39
+ 00bd3200 bytes a0c21839
- 00b63cb8 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd31b8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b63cb8 bytes f52900d0
+ 00bd31b8 bytes 952a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fb6b7304dbc18dd83717bee726482a7"></a>

### [`00b63d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d14.md) → [`00bd3214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3214.md) _ZN8firebase4auth18firebase_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "site": "00b63d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63d1c",
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
      "00bd3214",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd3218",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd321c",
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

- 旧版 [`00b63d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d14.md#insn-00b63d14) · [`00b63d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d14.md#insn-00b63d18) · [`00b63d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d14.md#insn-00b63d1c)

~~~diff
- 00b63d14 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b63d14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b63d14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b63d14 bytes f50f1df8
- 00b63d18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b63d18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b63d18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b63d18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63d18 bytes f44f01a9
- 00b63d1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b63d1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b63d1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b63d1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63d1c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e913d3aef58c6acbacc824a8cafe566c"></a>

### [`00b63d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d84.md) → [`00bd3284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3284.md) _ZN8firebase4auth18firebase_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b63d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63d88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63d98",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3284",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd3288",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd3298",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d84.md#insn-00b63d84) · [`00b63d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d84.md#insn-00b63d88) · [`00b63da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63d84.md#insn-00b63da0)

~~~diff
- 00b63d84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b63d84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b63d84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b63d84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b63d84 bytes f44fbea9
- 00b63d88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b63d88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b63d88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b63d88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63d88 bytes fd7b01a9
- 00b63da0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63da0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b63da0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-565480ca088d6c26e70fb7c2c5de04ef"></a>

### [`00b63e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63e30.md) → [`00bd3330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3330.md) _ZN8firebase4auth18firebase_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b63e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd3370"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63e4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63e44",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b63e4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3374"
      ]
    ],
    [
      "unmatched:00b63e54",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd3344",
      "READ",
      [
        "storage",
        "01126628",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd334c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3374"
      ]
    ],
    [
      "00bd3354",
      "PARAM",
      [
        "storage",
        "002a2c6a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63e30.md#insn-00b63e4c) · [`00b63e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63e30.md#insn-00b63e68) · [`00b63e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63e30.md#insn-00b63e70)
- 新版 `00bd3368`（命令位置の公開資料なし）

~~~diff
- 00b63e4c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63e4c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b63e4c bytes 410100b5
- 00b63e68 ["INT_ADD", "register:40f0:8", ["const:b63e68:8", "const:4:8"]]
- 00b63e68 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd3368 ["INT_ADD", "register:40f0:8", ["const:bd3368:8", "const:4:8"]]
+ 00bd3368 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b63e68 bytes 8ae80194
+ 00bd3368 bytes ea1d0294
- 00b63e70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b63e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63e70 bytes 809203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc50f9935f335cc83a9cbce0bb76b972"></a>

### [`00b63ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ea0.md) → [`00bd33a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33a0.md) _ZN8firebase4auth18firebase_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd33bc",
      "incomplete_value": false,
      "site": "00bd33c0",
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
      "definition_site": "00b63ebc",
      "incomplete_value": false,
      "site": "00b63ec0",
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
      "definition_site": "00bd33cc",
      "incomplete_value": true,
      "site": "00bd33d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63ecc",
      "incomplete_value": true,
      "site": "00b63ed8",
      "value": [
        "LOAD",
        "8",
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
      "00bd33bc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd33cc",
      "DATA",
      [
        "storage",
        "010a1738",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd33bc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd33cc",
      "DATA",
      [
        "storage",
        "01126640",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ea0.md#insn-00b63ec0) · [`00b63eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ea0.md#insn-00b63eb8) · [`00b63ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63ea0.md#insn-00b63ebc)
- 新版 `00bd33c0`（命令位置の公開資料なし） · `00bd33b8`（命令位置の公開資料なし） · `00bd33bc`（命令位置の公開資料なし）

~~~diff
- 00b63ec0 ["INT_ADD", "register:40f0:8", ["const:b63ec0:8", "const:4:8"]]
- 00b63ec0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd33c0 ["INT_ADD", "register:40f0:8", ["const:bd33c0:8", "const:4:8"]]
+ 00bd33c0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b63ec0 bytes b0e80194
+ 00bd33c0 bytes 101e0294
- 00b63eb8 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd33b8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b63eb8 bytes a0b9ffd0
+ 00bd33b8 bytes a0b6ffd0
- 00b63ebc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b63ebc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63ebc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63ebc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd33bc ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd33bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd33bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd33bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63ebc bytes 00c81791
+ 00bd33bc bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be579357985a99a85bc756343eea0a5a"></a>

### [`00b63edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63edc.md) → [`00bd33dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd33dc.md) _ZN8firebase4auth20CacheCommonMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c90.md) · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 1件 [`00c5d890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d890.md) · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 11.66% / 新版 11.66%

CFGの説明率　旧版 1.14% / 新版 1.20%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 26件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63fd0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63ef4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b63efc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3428"
      ]
    ],
    [
      "unmatched:00b63f04",
      "PARAM",
      [
        "storage",
        "0029166f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd33f4",
      "READ",
      [
        "storage",
        "011265a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd33fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd3428"
      ]
    ],
    [
      "00bd3404",
      "PARAM",
      [
        "storage",
        "002a0c88",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63edc.md#insn-00b63efc) · [`00b63f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63edc.md#insn-00b63f20) · [`00b63f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b63/00b63edc.md#insn-00b63f54)

~~~diff
- 00b63efc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63efc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b63efc bytes 610100b5
- 00b63f20 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a0:8"]]
- 00b63f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63f20 bytes a05203f9
- 00b63f54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63f54 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b63f54 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efdf226929255ca5dd9a8e43b7b62cc0"></a>

### [`00b64438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64438.md) → [`00bd3938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3938.md) _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ca0.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8a0.md) · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 5.44% / 新版 5.44%

CFGの説明率　旧版 1.02% / 新版 1.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 45件, `unresolved_store_alignment` 35件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64438"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6443c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6443c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b64438",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6443c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b64440",
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
      "00bd3938",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd393c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd3940",
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

- 旧版 [`00b64438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64438.md#insn-00b64438) · [`00b6443c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64438.md#insn-00b6443c) · [`00b64440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64438.md#insn-00b64440)

~~~diff
- 00b64438 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b64438 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b64438 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b64438 bytes f50f1df8
- 00b6443c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6443c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6443c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6443c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6443c bytes f44f01a9
- 00b64440 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b64440 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b64440 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b64440 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b64440 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7f13ee8b24371d278a9fa61fc0de731"></a>

### [`00b648d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b648d0.md) → [`00bd3dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd3/00bd3dd0.md) _ZN8firebase4auth22ErrorCodeFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d80.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00c5d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d980.md) · 呼出先 10件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.83% / 新版 72.83%

CFGの説明率　旧版 66.67% / 新版 60.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 24件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b648fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64a54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64a54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b648fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00bd3e14",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3e34",
      "READ",
      [
        "storage",
        "010a16d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd3dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00bd3e14",
      "READ",
      [
        "storage",
        "011265c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd3e34",
      "READ",
      [
        "storage",
        "011265d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b648fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b648d0.md#insn-00b648fc) · [`00b64a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b648d0.md#insn-00b64a54) · [`00b64a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b648d0.md#insn-00b64a80)

~~~diff
- 00b648fc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b648fc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b648fc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b648fc bytes a8031af8
- 00b64a54 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b64a54 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00b64a54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b64a54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b64a54 bytes ea2f05a9
- 00b64a80 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b64a80 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b64a80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:98:8"]]
- 00b64a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b64a80 bytes ed8309a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97cc8ce8ccdd8d2ceed0e1be51b263f"></a>

### [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) → [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) _ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 11件 [`00b5e7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md) [`00b5ef68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md) [`00b5f1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md) [`00b5f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md) [`00b5f5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md) · 呼出先 11件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00bddbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbc0.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md)
- 新版 呼出元 11件 [`00bcdca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdca0.md) [`00bce468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md) [`00bce6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md) [`00bce864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) [`00bceaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md) · 呼出先 11件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a630.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.27% / 新版 93.27%

CFGの説明率　旧版 60.00% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4434"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b64f5c",
      "incomplete_value": true,
      "site": "00b64f64",
      "value": [
        "live",
        "register:40a8:8"
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
      "unmatched:00b64f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bd4458",
      "READ",
      [
        "storage",
        "010a1550",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd44e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddbe0"
      ]
    ]
  ],
  "added": [
    [
      "00bd4434",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bd4458",
      "READ",
      [
        "storage",
        "01126458",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd44e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a650"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md#insn-00b64f34) · [`00b64f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md#insn-00b64f64) · [`00b64f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md#insn-00b64f8c)
- 新版 `00bd4464`（命令位置の公開資料なし）

~~~diff
- 00b64f34 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b64f34 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb8:8"]]
- 00b64f34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b64f34 bytes a8831bf8
- 00b64f64 ["INT_ADD", "register:40f0:8", ["const:b64f64:8", "const:4:8"]]
- 00b64f64 ["CALL", null, ["callee:004977f4:8"]]
+ 00bd4464 ["INT_ADD", "register:40f0:8", ["const:bd4464:8", "const:4:8"]]
+ 00bd4464 ["CALL", null, ["callee:004977f4:8"]]
- 00b64f64 bytes 7e3ee497
+ 00bd4464 bytes e40ce397
- 00b64f8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b64f8c ["INT_ADD", "register:40f0:8", ["const:b64f8c:8", "const:4:8"]]
- 00b64f8c ["CALLIND", null, ["register:0:8"]]
- 00b64f8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a78ad6ecd0193b395e5f2ffb332bff35"></a>

### [`00b650cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b650cc.md) → [`00bd45cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd45cc.md) _ZN8firebase4auth22ReadAdditionalUserInfoEP7_JNIEnvP8_jobjectPNS0_18AdditionalUserInfoE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d90.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 1件 [`00c5d990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d990.md) · 呼出先 9件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 53.57% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b650d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b650d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b650d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b650d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b650d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b650d8",
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
      "00bd45d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd45d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd45d8",
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

- 旧版 [`00b650d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b650cc.md#insn-00b650d0) · [`00b650d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b650cc.md#insn-00b650d4) · [`00b650d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b650cc.md#insn-00b650d8)

~~~diff
- 00b650d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:80:8"]]
- 00b650d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00b650d0 bytes f94300f9
- 00b650d4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b650d4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b650d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 00b650d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b650d4 bytes f85f09a9
- 00b650d8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b650d8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b650d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00b650d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b650d8 bytes f6570aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ec30d9ac528da137b081e959195f4be"></a>

### [`00b65314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65314.md) → [`00bd4814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4814.md) _ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b5ebb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md) [`00b708dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbc0.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 2件 [`00bce0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce0b4.md) [`00bdfddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md) · 呼出先 7件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a630.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 53.33% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd4854",
      "incomplete_value": true,
      "site": "00bd4858",
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
      "definition_site": "00b65354",
      "incomplete_value": true,
      "site": "00b65358",
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
    "new": {
      "definition_site": "00bd4868",
      "incomplete_value": true,
      "site": "00bd4874",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65368",
      "incomplete_value": true,
      "site": "00b65374",
      "value": [
        "LOAD",
        "8",
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
                "const:550:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b653d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd4868",
      "READ",
      [
        "storage",
        "010a1550",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd48f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddbe0"
      ]
    ],
    [
      "unmatched:00b653d0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd4868",
      "READ",
      [
        "storage",
        "01126458",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd48f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a650"
      ]
    ],
    [
      "00bd48d0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65314.md#insn-00b65358) · [`00b65374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65314.md#insn-00b65374) · [`00b653d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65314.md#insn-00b653d0)
- 新版 `00bd4858`（命令位置の公開資料なし） · `00bd4874`（命令位置の公開資料なし）

~~~diff
- 00b65358 ["INT_ADD", "register:40f0:8", ["const:b65358:8", "const:4:8"]]
- 00b65358 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bd4858 ["INT_ADD", "register:40f0:8", ["const:bd4858:8", "const:4:8"]]
+ 00bd4858 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b65358 bytes aae30194
+ 00bd4858 bytes 0a190294
- 00b65374 ["INT_ADD", "register:40f0:8", ["const:b65374:8", "const:4:8"]]
- 00b65374 ["CALL", null, ["callee:004977f4:8"]]
+ 00bd4874 ["INT_ADD", "register:40f0:8", ["const:bd4874:8", "const:4:8"]]
+ 00bd4874 ["CALL", null, ["callee:004977f4:8"]]
- 00b65374 bytes 7a3de497
+ 00bd4874 bytes e00be397
- 00b653d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b653d0 ["INT_ADD", "register:40f0:8", ["const:b653d0:8", "const:4:8"]]
- 00b653d0 ["CALLIND", null, ["register:0:8"]]
- 00b653d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d61e927edfe7842c65a2438a57992a16"></a>

### [`00b65558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65558.md) → [`00bd4a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a58.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b65584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4a84"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd4a6c",
      "incomplete_value": true,
      "site": "00bd4a6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6556c",
      "incomplete_value": true,
      "site": "00b6556c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd4a68",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4a6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65588"
      ]
    ],
    [
      "unmatched:00b65578",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd4a68",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4a6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd4a88"
      ]
    ],
    [
      "00bd4a78",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6556c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65558.md#insn-00b6556c) · [`00b6557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65558.md#insn-00b6557c) · [`00b65584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65558.md#insn-00b65584)
- 新版 `00bd4a6c`（命令位置の公開資料なし）

~~~diff
- 00b6556c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6556c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd4a6c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd4a6c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6556c bytes e80000b5
+ 00bd4a6c bytes e80000b5
- 00b6557c ["INT_ADD", "register:40f0:8", ["const:b6557c:8", "const:4:8"]]
- 00b6557c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6557c bytes c5e20194
- 00b65584 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65584 bytes 60a203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74fbeb0dbbe7c8d8cca0943fb247c1d4"></a>

### [`00b65598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65598.md) → [`00bd4a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4a98.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd4ac4",
      "incomplete_value": true,
      "site": "00bd4ac4",
      "value": [
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
    "old": {
      "definition_site": "00b655c4",
      "incomplete_value": true,
      "site": "00b655c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      "definition_site": "00bd4aac",
      "incomplete_value": true,
      "site": "00bd4aac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655ac",
      "incomplete_value": true,
      "site": "00b655ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd4ab4",
      "incomplete_value": false,
      "site": "00bd4abc",
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
            "const:cdc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655b4",
      "incomplete_value": false,
      "site": "00b655bc",
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
            "const:45:8"
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
      "00bd4aa8",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4ab4",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00bd4ac4",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4aa8",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4ab4",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4ac4",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b655bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65598.md#insn-00b655bc) · [`00b655c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65598.md#insn-00b655c4) · [`00b655a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65598.md#insn-00b655a4)
- 新版 `00bd4abc`（命令位置の公開資料なし） · `00bd4ac4`（命令位置の公開資料なし） · `00bd4aa4`（命令位置の公開資料なし）

~~~diff
- 00b655bc ["INT_ADD", "register:40f0:8", ["const:b655bc:8", "const:4:8"]]
- 00b655bc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4abc ["INT_ADD", "register:40f0:8", ["const:bd4abc:8", "const:4:8"]]
+ 00bd4abc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b655bc bytes b5e20194
+ 00bd4abc bytes 15180294
- 00b655c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b655c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4ac4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00bd4ac4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b655c4 bytes 60a203f9
+ 00bd4ac4 bytes 602603f9
- 00b655a4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd4aa4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b655a4 bytes f3290090
+ 00bd4aa4 bytes 932a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b321731c87d4d7f25d9ea760239fd964"></a>

### [`00b655d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b655d8.md) → [`00bd4ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4ad8.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b65608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4b08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd4aec",
      "incomplete_value": true,
      "site": "00bd4aec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655ec",
      "incomplete_value": true,
      "site": "00b655ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd4ae8",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b655f8",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65600",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd4ae8",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4af8",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4b00",
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

- 旧版 [`00b655ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b655d8.md#insn-00b655ec) · [`00b65600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b655d8.md#insn-00b65600) · [`00b65608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b655d8.md#insn-00b65608)
- 新版 `00bd4aec`（命令位置の公開資料なし）

~~~diff
- 00b655ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b655ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd4aec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd4aec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b655ec bytes 080100b5
+ 00bd4aec bytes 080100b5
- 00b65600 ["INT_ADD", "register:40f0:8", ["const:b65600:8", "const:4:8"]]
- 00b65600 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65600 bytes a4e20194
- 00b65608 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b65608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65608 bytes 60a203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30b5792aed7a858a73b0cca6fb35932"></a>

### [`00b6561c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6561c.md) → [`00bd4b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b1c.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b6564c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4b4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd4b30",
      "incomplete_value": true,
      "site": "00bd4b30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65630",
      "incomplete_value": true,
      "site": "00b65630",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd4b2c",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65638",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6564c",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4b2c",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4b38",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4b4c",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6561c.md#insn-00b65630) · [`00b65644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6561c.md#insn-00b65644) · [`00b6564c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6561c.md#insn-00b6564c)
- 新版 `00bd4b30`（命令位置の公開資料なし） · `00bd4b44`（命令位置の公開資料なし）

~~~diff
- 00b65630 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65630 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd4b30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd4b30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65630 bytes 080100b5
+ 00bd4b30 bytes 080100b5
- 00b65644 ["INT_ADD", "register:40f0:8", ["const:b65644:8", "const:4:8"]]
- 00b65644 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4b44 ["INT_ADD", "register:40f0:8", ["const:bd4b44:8", "const:4:8"]]
+ 00bd4b44 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65644 bytes 93e20194
+ 00bd4b44 bytes f3170294
- 00b6564c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
- 00b6564c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6564c bytes 60a203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c93a8412626d0959aad95d49b8ee57c"></a>

### [`00b6566c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6566c.md) → [`00bd4b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4b6c.md) _ZN8firebase4auth10credential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd4bc4",
      "incomplete_value": true,
      "site": "00bd4bc4",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b656c4",
      "incomplete_value": true,
      "site": "00b656c4",
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
            "const:748:8"
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
      "definition_site": "00bd4ba0",
      "incomplete_value": true,
      "site": "00bd4bac",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:648:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b656a0",
      "incomplete_value": true,
      "site": "00b656ac",
      "value": [
        "LOAD",
        "8",
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
      "00bd4b80",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4ba0",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4bc4",
      "WRITE",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd4b80",
      "READ",
      [
        "storage",
        "01126650",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4ba0",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4bc4",
      "WRITE",
      [
        "storage",
        "01126650",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b656ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6566c.md#insn-00b656ac) · [`00b656c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6566c.md#insn-00b656c4) · [`00b6567c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b6566c.md#insn-00b6567c)
- 新版 `00bd4bac`（命令位置の公開資料なし） · `00bd4bc4`（命令位置の公開資料なし） · `00bd4b7c`（命令位置の公開資料なし）

~~~diff
- 00b656ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b656ac ["INT_ADD", "register:40f0:8", ["const:b656ac:8", "const:4:8"]]
- 00b656ac ["CALLIND", null, ["register:0:8"]]
+ 00bd4bac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4bac ["INT_ADD", "register:40f0:8", ["const:bd4bac:8", "const:4:8"]]
+ 00bd4bac ["CALLIND", null, ["register:0:8"]]
- 00b656ac bytes 00013fd6
+ 00bd4bac bytes 00013fd6
- 00b656c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b656c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:748:8"]]
- 00b656c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd4bc4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd4bc4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:650:8"]]
+ 00bd4bc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b656c4 bytes a0221d39
+ 00bd4bc4 bytes a0421939
- 00b6567c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd4b7c ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b6567c bytes f5290090
+ 00bd4b7c bytes 952a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-961edc58f5226caf4cc6123ebe774b14"></a>

### [`00b656d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b656d8.md) → [`00bd4bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4bd8.md) _ZN8firebase4auth10credential12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 14.29% / 新版 16.67%

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
      "site": "00b65714"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4c14"
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
      "00bd4bec",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4bf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65738"
      ]
    ],
    [
      "00bd4bf8",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd4bec",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4bf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd4c38"
      ]
    ],
    [
      "00bd4bf8",
      "READ",
      [
        "storage",
        "01126650",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b656d8.md#insn-00b65714) · [`00b6571c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b656d8.md#insn-00b6571c) · [`00b65730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b656d8.md#insn-00b65730)

~~~diff
- 00b65714 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65714 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65714 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:748:8"]]
- 00b65714 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65714 bytes bf221d39
- 00b6571c ["INT_ADD", "register:40f0:8", ["const:b6571c:8", "const:4:8"]]
- 00b6571c ["CALL", null, ["callee:00c5ab60:8"]]
- 00b6571c bytes 71e20194
- 00b65730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65730 ["INT_ADD", "register:40f0:8", ["const:b65730:8", "const:4:8"]]
- 00b65730 ["CALLIND", null, ["register:0:8"]]
- 00b65730 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2ca4dfdc9b3355237ad8217dbc4c45b"></a>

### [`00b65748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65748.md) → [`00bd4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4c48.md) _ZN8firebase4auth10credential14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd4c88",
      "incomplete_value": true,
      "site": "00bd4c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65788",
      "incomplete_value": true,
      "site": "00b65788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      "definition_site": "00bd4c64",
      "incomplete_value": true,
      "site": "00bd4c64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65764",
      "incomplete_value": true,
      "site": "00b65764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd4c6c",
      "incomplete_value": false,
      "site": "00bd4c80",
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
            "const:cdc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6576c",
      "incomplete_value": false,
      "site": "00b65780",
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
            "const:45:8"
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
      "00bd4c5c",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4c6c",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00bd4c88",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4c5c",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4c6c",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4c88",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65748.md#insn-00b65780) · [`00b65788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65748.md#insn-00b65788) · [`00b65754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65748.md#insn-00b65754)
- 新版 `00bd4c80`（命令位置の公開資料なし） · `00bd4c88`（命令位置の公開資料なし） · `00bd4c54`（命令位置の公開資料なし）

~~~diff
- 00b65780 ["INT_ADD", "register:40f0:8", ["const:b65780:8", "const:4:8"]]
- 00b65780 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4c80 ["INT_ADD", "register:40f0:8", ["const:bd4c80:8", "const:4:8"]]
+ 00bd4c80 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65780 bytes 44e20194
+ 00bd4c80 bytes a4170294
- 00b65788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00bd4c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65788 bytes 80a203f9
+ 00bd4c88 bytes 802603f9
- 00b65754 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd4c54 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65754 bytes f4290090
+ 00bd4c54 bytes 942a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc2db1fb926354e644796f501ce6e472"></a>

### [`00b657b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657b8.md) → [`00bd4cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cb8.md) _ZN8firebase4auth10credential11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd4cd4",
      "incomplete_value": false,
      "site": "00bd4cd8",
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
      "definition_site": "00b657d4",
      "incomplete_value": false,
      "site": "00b657d8",
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
      "definition_site": "00bd4ce4",
      "incomplete_value": true,
      "site": "00bd4cf0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b657e4",
      "incomplete_value": true,
      "site": "00b657f0",
      "value": [
        "LOAD",
        "8",
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
      "00bd4cd4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd4ce4",
      "DATA",
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
      "00bd4cd4",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd4ce4",
      "DATA",
      [
        "storage",
        "01126658",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b657d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657b8.md#insn-00b657d8) · [`00b657d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657b8.md#insn-00b657d0) · [`00b657d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657b8.md#insn-00b657d4)
- 新版 `00bd4cd8`（命令位置の公開資料なし） · `00bd4cd0`（命令位置の公開資料なし） · `00bd4cd4`（命令位置の公開資料なし）

~~~diff
- 00b657d8 ["INT_ADD", "register:40f0:8", ["const:b657d8:8", "const:4:8"]]
- 00b657d8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd4cd8 ["INT_ADD", "register:40f0:8", ["const:bd4cd8:8", "const:4:8"]]
+ 00bd4cd8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b657d8 bytes 6ae20194
+ 00bd4cd8 bytes ca170294
- 00b657d0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd4cd0 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b657d0 bytes 80b9fff0
+ 00bd4cd0 bytes a0b6ff90
- 00b657d4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b657d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b657d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b657d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd4cd4 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd4cd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd4cd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd4cd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b657d4 bytes 001c1591
+ 00bd4cd4 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb119a6c08c61dae9179467e0f71ade"></a>

### [`00b657f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657f4.md) → [`00bd4cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4cf4.md) _ZN8firebase4auth10credential13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd4d34",
      "incomplete_value": true,
      "site": "00bd4d34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65834",
      "incomplete_value": true,
      "site": "00b65834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      "definition_site": "00bd4d10",
      "incomplete_value": true,
      "site": "00bd4d10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65810",
      "incomplete_value": true,
      "site": "00b65810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd4d18",
      "incomplete_value": false,
      "site": "00bd4d2c",
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
            "const:cdc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65818",
      "incomplete_value": false,
      "site": "00b6582c",
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
            "const:45:8"
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
      "00bd4d08",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4d18",
      "PARAM",
      [
        "storage",
        "002a9045",
        null,
        "string"
      ]
    ],
    [
      "00bd4d34",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4d08",
      "READ",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4d18",
      "PARAM",
      [
        "storage",
        "002b9cdc",
        null,
        "string"
      ]
    ],
    [
      "00bd4d34",
      "WRITE",
      [
        "storage",
        "01126648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6582c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657f4.md#insn-00b6582c) · [`00b65834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657f4.md#insn-00b65834) · [`00b65800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b657f4.md#insn-00b65800)
- 新版 `00bd4d2c`（命令位置の公開資料なし） · `00bd4d34`（命令位置の公開資料なし） · `00bd4d00`（命令位置の公開資料なし）

~~~diff
- 00b6582c ["INT_ADD", "register:40f0:8", ["const:b6582c:8", "const:4:8"]]
- 00b6582c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4d2c ["INT_ADD", "register:40f0:8", ["const:bd4d2c:8", "const:4:8"]]
+ 00bd4d2c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6582c bytes 19e20194
+ 00bd4d2c bytes 79170294
- 00b65834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00b65834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4d34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:648:8"]]
+ 00bd4d34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65834 bytes 80a203f9
+ 00bd4d34 bytes 802603f9
- 00b65800 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd4d00 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b65800 bytes f4290090
+ 00bd4d00 bytes 942a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0748935ffa987a08ed330ae064fa3e5"></a>

### [`00b658a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658a0.md) → [`00bd4da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4da0.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd4dcc",
      "incomplete_value": true,
      "site": "00bd4dcc",
      "value": [
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
      "definition_site": "00b658cc",
      "incomplete_value": true,
      "site": "00b658cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "definition_site": "00bd4db4",
      "incomplete_value": true,
      "site": "00bd4db4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658b4",
      "incomplete_value": true,
      "site": "00b658b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd4dc0",
      "incomplete_value": false,
      "site": "00bd4dc4",
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
            "const:3b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658c0",
      "incomplete_value": false,
      "site": "00b658c4",
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
            "const:18d:8"
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
      "00bd4db0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4dc0",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00bd4dcc",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4db0",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4dc0",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      "00bd4dcc",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b658c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658a0.md#insn-00b658c4) · [`00b658cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658a0.md#insn-00b658cc) · [`00b658ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658a0.md#insn-00b658ac)
- 新版 `00bd4dc4`（命令位置の公開資料なし） · `00bd4dcc`（命令位置の公開資料なし） · `00bd4dac`（命令位置の公開資料なし）

~~~diff
- 00b658c4 ["INT_ADD", "register:40f0:8", ["const:b658c4:8", "const:4:8"]]
- 00b658c4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4dc4 ["INT_ADD", "register:40f0:8", ["const:bd4dc4:8", "const:4:8"]]
+ 00bd4dc4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b658c4 bytes f3e10194
+ 00bd4dc4 bytes 53170294
- 00b658cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b658cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4dcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bd4dcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b658cc bytes 60b203f9
+ 00bd4dcc bytes 603603f9
- 00b658ac ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd4dac ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b658ac bytes f3290090
+ 00bd4dac bytes 932a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7125f78fae015bc753e3e9624bac955"></a>

### [`00b658e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658e0.md) → [`00bd4de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4de0.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b6590c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4e0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd4df4",
      "incomplete_value": true,
      "site": "00bd4df4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b658f4",
      "incomplete_value": true,
      "site": "00b658f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd4df0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65910"
      ]
    ],
    [
      "unmatched:00b658fc",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd4df0",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd4e10"
      ]
    ],
    [
      "00bd4dfc",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658e0.md#insn-00b65904) · [`00b6590c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658e0.md#insn-00b6590c) · [`00b6591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b658e0.md#insn-00b6591c)

~~~diff
- 00b65904 ["INT_ADD", "register:40f0:8", ["const:b65904:8", "const:4:8"]]
- 00b65904 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65904 bytes e3e10194
- 00b6590c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b6590c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6590c bytes 60b203f9
- 00b6591c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6591c ["RETURN", null, ["register:0:8"]]
- 00b6591c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9255c967f148a28609fd1f21b9744fce"></a>

### [`00b65920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65920.md) → [`00bd4e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e20.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd4e50",
      "incomplete_value": true,
      "site": "00bd4e50",
      "value": [
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
      "definition_site": "00b65950",
      "incomplete_value": true,
      "site": "00b65950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "definition_site": "00bd4e34",
      "incomplete_value": true,
      "site": "00bd4e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65934",
      "incomplete_value": true,
      "site": "00b65934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd4e40",
      "incomplete_value": false,
      "site": "00bd4e48",
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
            "const:3b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65940",
      "incomplete_value": false,
      "site": "00b65948",
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
            "const:18d:8"
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
      "00bd4e30",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4e40",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "00bd4e50",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4e30",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4e40",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      "00bd4e50",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65920.md#insn-00b65948) · [`00b65950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65920.md#insn-00b65950) · [`00b6592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65920.md#insn-00b6592c)
- 新版 `00bd4e48`（命令位置の公開資料なし） · `00bd4e50`（命令位置の公開資料なし） · `00bd4e2c`（命令位置の公開資料なし）

~~~diff
- 00b65948 ["INT_ADD", "register:40f0:8", ["const:b65948:8", "const:4:8"]]
- 00b65948 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4e48 ["INT_ADD", "register:40f0:8", ["const:bd4e48:8", "const:4:8"]]
+ 00bd4e48 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65948 bytes d2e10194
+ 00bd4e48 bytes 32170294
- 00b65950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd4e50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:668:8"]]
+ 00bd4e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65950 bytes 60b203f9
+ 00bd4e50 bytes 603603f9
- 00b6592c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd4e2c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b6592c bytes f3290090
+ 00bd4e2c bytes 932a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d39e6c8c19f2de427ae56889c333664"></a>

### [`00b65964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65964.md) → [`00bd4e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4e64.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b65994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4e94"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd4e78",
      "incomplete_value": true,
      "site": "00bd4e78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65978",
      "incomplete_value": true,
      "site": "00b65978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd4e74",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65980",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65994",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd4e74",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4e80",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ],
    [
      "00bd4e94",
      "WRITE",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65964.md#insn-00b65978) · [`00b6598c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65964.md#insn-00b6598c) · [`00b65994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65964.md#insn-00b65994)
- 新版 `00bd4e78`（命令位置の公開資料なし） · `00bd4e8c`（命令位置の公開資料なし）

~~~diff
- 00b65978 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65978 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd4e78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd4e78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65978 bytes 080100b5
+ 00bd4e78 bytes 080100b5
- 00b6598c ["INT_ADD", "register:40f0:8", ["const:b6598c:8", "const:4:8"]]
- 00b6598c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4e8c ["INT_ADD", "register:40f0:8", ["const:bd4e8c:8", "const:4:8"]]
+ 00bd4e8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6598c bytes c1e10194
+ 00bd4e8c bytes 21170294
- 00b65994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
- 00b65994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65994 bytes 60b203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48d381878540bd6fe256daa056eddee6"></a>

### [`00b659b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b659b4.md) → [`00bd4eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4eb4.md) _ZN8firebase4auth9emailcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "site": "00b65a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4f0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd4ee8",
      "incomplete_value": true,
      "site": "00bd4ef4",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
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
      "definition_site": "00b659e8",
      "incomplete_value": true,
      "site": "00b659f4",
      "value": [
        "LOAD",
        "8",
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
                "const:760:8"
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
      "00bd4ec8",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b659e8",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65a0c",
      "WRITE",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd4ec8",
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4ee8",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4f0c",
      "WRITE",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b659f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b659b4.md#insn-00b659f4) · [`00b65a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b659b4.md#insn-00b65a0c)
- 新版 `00bd4ef4`（命令位置の公開資料なし） · `00bd4f0c`（命令位置の公開資料なし）

~~~diff
- 00b659f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b659f4 ["INT_ADD", "register:40f0:8", ["const:b659f4:8", "const:4:8"]]
- 00b659f4 ["CALLIND", null, ["register:0:8"]]
+ 00bd4ef4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4ef4 ["INT_ADD", "register:40f0:8", ["const:bd4ef4:8", "const:4:8"]]
+ 00bd4ef4 ["CALLIND", null, ["register:0:8"]]
- 00b659f4 bytes 00013fd6
+ 00bd4ef4 bytes 00013fd6
- 00b65a0c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65a0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:768:8"]]
- 00b65a0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65a0c bytes a0a21d39
+ 00bd4f0c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd4f0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:670:8"]]
+ 00bd4f0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd4f0c bytes a0c21939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9cff1d53dc3c78c7bae09ab24ecc09"></a>

### [`00b65a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a20.md) → [`00bd4f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f20.md) _ZN8firebase4auth9emailcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd4f5c",
      "incomplete_value": true,
      "site": "00bd4f5c",
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
      "definition_site": "00b65a5c",
      "incomplete_value": true,
      "site": "00b65a5c",
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
            "const:768:8"
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
      "definition_site": "00bd4f7c",
      "incomplete_value": true,
      "site": "00bd4f7c",
      "value": [
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
      "definition_site": "00b65a7c",
      "incomplete_value": true,
      "site": "00b65a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:760:8"
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
      "definition_site": "00bd4f38",
      "incomplete_value": true,
      "site": "00bd4f38",
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
      "definition_site": "00b65a38",
      "incomplete_value": true,
      "site": "00b65a38",
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
      "00bd4f34",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4f40",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4f5c",
      "WRITE",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd4f34",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4f40",
      "READ",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd4f5c",
      "WRITE",
      [
        "storage",
        "01126670",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a20.md#insn-00b65a5c) · [`00b65a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a20.md#insn-00b65a78) · [`00b65a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a20.md#insn-00b65a7c)
- 新版 `00bd4f5c`（命令位置の公開資料なし） · `00bd4f78`（命令位置の公開資料なし） · `00bd4f7c`（命令位置の公開資料なし）

~~~diff
- 00b65a5c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65a5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65a5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:768:8"]]
- 00b65a5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd4f5c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd4f5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd4f5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:670:8"]]
+ 00bd4f5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65a5c bytes bfa21d39
+ 00bd4f5c bytes bfc21939
- 00b65a78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65a78 ["INT_ADD", "register:40f0:8", ["const:b65a78:8", "const:4:8"]]
- 00b65a78 ["CALLIND", null, ["register:0:8"]]
+ 00bd4f78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd4f78 ["INT_ADD", "register:40f0:8", ["const:bd4f78:8", "const:4:8"]]
+ 00bd4f78 ["CALLIND", null, ["register:0:8"]]
- 00b65a78 bytes 00013fd6
+ 00bd4f78 bytes 00013fd6
- 00b65a7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b65a7c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd4f7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:668:8"]]
+ 00bd4f7c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd4f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65a7c bytes 9fb203f9
+ 00bd4f7c bytes 9f3603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7c45ab018f1c1103de1f54f61125afd"></a>

### [`00b65a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a90.md) → [`00bd4f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4f90.md) _ZN8firebase4auth9emailcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b65ad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd4fd0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65aac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65aa4",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65aac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd4fd4"
      ]
    ],
    [
      "unmatched:00b65ab4",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd4fa4",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd4fac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd4fd4"
      ]
    ],
    [
      "00bd4fb4",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a90.md#insn-00b65aac) · [`00b65ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a90.md#insn-00b65ac8) · [`00b65ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65a90.md#insn-00b65ad0)
- 新版 `00bd4fc8`（命令位置の公開資料なし）

~~~diff
- 00b65aac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65aac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65aac bytes 410100b5
- 00b65ac8 ["INT_ADD", "register:40f0:8", ["const:b65ac8:8", "const:4:8"]]
- 00b65ac8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd4fc8 ["INT_ADD", "register:40f0:8", ["const:bd4fc8:8", "const:4:8"]]
+ 00bd4fc8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65ac8 bytes 72e10194
+ 00bd4fc8 bytes d2160294
- 00b65ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b65ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65ad0 bytes 80b203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c26cd2cfb31d3389a863130c92da5604"></a>

### [`00b65b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b00.md) → [`00bd5000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5000.md) _ZN8firebase4auth9emailcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd501c",
      "incomplete_value": false,
      "site": "00bd5020",
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
      "definition_site": "00b65b1c",
      "incomplete_value": false,
      "site": "00b65b20",
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
      "definition_site": "00bd502c",
      "incomplete_value": true,
      "site": "00bd5038",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65b2c",
      "incomplete_value": true,
      "site": "00b65b38",
      "value": [
        "LOAD",
        "8",
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
      "00bd501c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd502c",
      "DATA",
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
      "00bd501c",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd502c",
      "DATA",
      [
        "storage",
        "01126678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b00.md#insn-00b65b20) · [`00b65b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b00.md#insn-00b65b18) · [`00b65b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b00.md#insn-00b65b1c)
- 新版 `00bd5020`（命令位置の公開資料なし） · `00bd5018`（命令位置の公開資料なし） · `00bd501c`（命令位置の公開資料なし）

~~~diff
- 00b65b20 ["INT_ADD", "register:40f0:8", ["const:b65b20:8", "const:4:8"]]
- 00b65b20 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd5020 ["INT_ADD", "register:40f0:8", ["const:bd5020:8", "const:4:8"]]
+ 00bd5020 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b65b20 bytes 98e10194
+ 00bd5020 bytes f8160294
- 00b65b18 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd5018 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b65b18 bytes 80b9fff0
+ 00bd5018 bytes 80b6fff0
- 00b65b1c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b65b1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65b1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd501c ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd501c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd501c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd501c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65b1c bytes 001c1591
+ 00bd501c bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff50774e3e9a0523352fb073d5968dc8"></a>

### [`00b65b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b3c.md) → [`00bd503c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd503c.md) _ZN8firebase4auth9emailcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b65b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd507c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65b58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65b50",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65b58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5080"
      ]
    ],
    [
      "unmatched:00b65b60",
      "PARAM",
      [
        "storage",
        "0029c18d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5050",
      "READ",
      [
        "storage",
        "01126668",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5080"
      ]
    ],
    [
      "00bd5060",
      "PARAM",
      [
        "storage",
        "002ac3b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b3c.md#insn-00b65b58) · [`00b65b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b3c.md#insn-00b65b74) · [`00b65b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65b3c.md#insn-00b65b7c)
- 新版 `00bd5074`（命令位置の公開資料なし）

~~~diff
- 00b65b58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65b58 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65b58 bytes 410100b5
- 00b65b74 ["INT_ADD", "register:40f0:8", ["const:b65b74:8", "const:4:8"]]
- 00b65b74 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5074 ["INT_ADD", "register:40f0:8", ["const:bd5074:8", "const:4:8"]]
+ 00bd5074 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65b74 bytes 47e10194
+ 00bd5074 bytes a7160294
- 00b65b7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
- 00b65b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b7c bytes 80b203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d943c5f6144af4360e605de7a7f2e19a"></a>

### [`00b65bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65bac.md) → [`00bd50ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50ac.md) _ZN8firebase4auth9emailcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd50c8",
      "incomplete_value": false,
      "site": "00bd50cc",
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
      "definition_site": "00b65bc8",
      "incomplete_value": false,
      "site": "00b65bcc",
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
      "definition_site": "00bd50d8",
      "incomplete_value": true,
      "site": "00bd50e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65bd8",
      "incomplete_value": true,
      "site": "00b65be4",
      "value": [
        "LOAD",
        "8",
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
      "00bd50c8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd50d8",
      "DATA",
      [
        "storage",
        "010a1778",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd50c8",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd50d8",
      "DATA",
      [
        "storage",
        "01126680",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65bac.md#insn-00b65bcc) · [`00b65bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65bac.md#insn-00b65bc4) · [`00b65bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65bac.md#insn-00b65bc8)
- 新版 `00bd50cc`（命令位置の公開資料なし） · `00bd50c4`（命令位置の公開資料なし） · `00bd50c8`（命令位置の公開資料なし）

~~~diff
- 00b65bcc ["INT_ADD", "register:40f0:8", ["const:b65bcc:8", "const:4:8"]]
- 00b65bcc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd50cc ["INT_ADD", "register:40f0:8", ["const:bd50cc:8", "const:4:8"]]
+ 00bd50cc ["CALL", null, ["callee:00c5ac00:8"]]
- 00b65bcc bytes 6de10194
+ 00bd50cc bytes cd160294
- 00b65bc4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd50c4 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b65bc4 bytes a0b9ff90
+ 00bd50c4 bytes a0b6ff90
- 00b65bc8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b65bc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65bc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65bc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd50c8 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd50c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd50c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd50c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65bc8 bytes 00c81791
+ 00bd50c8 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f50d16b3594008b030ca55343492cc3e"></a>

### [`00b65be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65be8.md) → [`00bd50e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd50e8.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd5114",
      "incomplete_value": true,
      "site": "00bd5114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c14",
      "incomplete_value": true,
      "site": "00b65c14",
      "value": [
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
      "definition_site": "00bd50fc",
      "incomplete_value": true,
      "site": "00bd50fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bfc",
      "incomplete_value": true,
      "site": "00b65bfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd5108",
      "incomplete_value": false,
      "site": "00bd510c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c08",
      "incomplete_value": false,
      "site": "00b65c0c",
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
            "const:3e1:8"
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
      "00bd50f8",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5108",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00bd5114",
      "WRITE",
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
      "00bd50f8",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5108",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      "00bd5114",
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65be8.md#insn-00b65c0c) · [`00b65c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65be8.md#insn-00b65c14) · [`00b65bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65be8.md#insn-00b65bf4)
- 新版 `00bd510c`（命令位置の公開資料なし） · `00bd5114`（命令位置の公開資料なし） · `00bd50f4`（命令位置の公開資料なし）

~~~diff
- 00b65c0c ["INT_ADD", "register:40f0:8", ["const:b65c0c:8", "const:4:8"]]
- 00b65c0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd510c ["INT_ADD", "register:40f0:8", ["const:bd510c:8", "const:4:8"]]
+ 00bd510c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65c0c bytes 21e10194
+ 00bd510c bytes 81160294
- 00b65c14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b65c14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5114 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:688:8"]]
+ 00bd5114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c14 bytes 60c203f9
+ 00bd5114 bytes 604603f9
- 00b65bf4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd50f4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65bf4 bytes f3290090
+ 00bd50f4 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4da8c5c6075e51ce3efc363c49eb009"></a>

### [`00b65c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c28.md) → [`00bd5128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5128.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00b65c54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5154"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd513c",
      "incomplete_value": true,
      "site": "00bd513c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c3c",
      "incomplete_value": true,
      "site": "00b65c3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd5138",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65c44",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65c4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd5138",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5144",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      "00bd514c",
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

- 旧版 [`00b65c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c28.md#insn-00b65c3c) · [`00b65c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c28.md#insn-00b65c4c) · [`00b65c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65c28.md#insn-00b65c54)
- 新版 `00bd513c`（命令位置の公開資料なし）

~~~diff
- 00b65c3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65c3c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd513c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd513c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65c3c bytes e80000b5
+ 00bd513c bytes e80000b5
- 00b65c4c ["INT_ADD", "register:40f0:8", ["const:b65c4c:8", "const:4:8"]]
- 00b65c4c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65c4c bytes 11e10194
- 00b65c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b65c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65c54 bytes 60c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a4096953763958af2d1f92e2b6536e1"></a>

### [`00b65cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cac.md) → [`00bd51ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd51ac.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b65cdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd51dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd51c0",
      "incomplete_value": true,
      "site": "00bd51c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cc0",
      "incomplete_value": true,
      "site": "00b65cc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd51bc",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65cc8",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65cdc",
      "WRITE",
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
      "00bd51bc",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd51c8",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ],
    [
      "00bd51dc",
      "WRITE",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cac.md#insn-00b65cc0) · [`00b65cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cac.md#insn-00b65cd4) · [`00b65cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65cac.md#insn-00b65cdc)
- 新版 `00bd51c0`（命令位置の公開資料なし） · `00bd51d4`（命令位置の公開資料なし）

~~~diff
- 00b65cc0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65cc0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd51c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd51c0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b65cc0 bytes 080100b5
+ 00bd51c0 bytes 080100b5
- 00b65cd4 ["INT_ADD", "register:40f0:8", ["const:b65cd4:8", "const:4:8"]]
- 00b65cd4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd51d4 ["INT_ADD", "register:40f0:8", ["const:bd51d4:8", "const:4:8"]]
+ 00bd51d4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65cd4 bytes efe00194
+ 00bd51d4 bytes 4f160294
- 00b65cdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
- 00b65cdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65cdc bytes 60c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b271f19ab2c211129f32548ceab36a83"></a>

### [`00b65d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65d68.md) → [`00bd5268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5268.md) _ZN8firebase4auth12facebookcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "site": "00b65da4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd52a4"
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
      "00bd527c",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5288",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65da8"
      ]
    ]
  ],
  "added": [
    [
      "00bd527c",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5288",
      "READ",
      [
        "storage",
        "01126690",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd5290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd52a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65d68.md#insn-00b65d80) · [`00b65da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65d68.md#insn-00b65da4) · [`00b65dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65d68.md#insn-00b65dac)
- 新版 `00bd5280`（命令位置の公開資料なし）

~~~diff
- 00b65d80 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65d80 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd5280 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd5280 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b65d80 bytes 410200b4
+ 00bd5280 bytes 410200b4
- 00b65da4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65da4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65da4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:788:8"]]
- 00b65da4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65da4 bytes bf221e39
- 00b65dac ["INT_ADD", "register:40f0:8", ["const:b65dac:8", "const:4:8"]]
- 00b65dac ["CALL", null, ["callee:00c5ab60:8"]]
- 00b65dac bytes cde00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c76c176379254b395f47fce31e71e3ca"></a>

### [`00b65dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65dd8.md) → [`00bd52d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd52d8.md) _ZN8firebase4auth12facebookcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b65e18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5318"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65df4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65dec",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd531c"
      ]
    ],
    [
      "unmatched:00b65dfc",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd52ec",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd52f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd531c"
      ]
    ],
    [
      "00bd52fc",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65dd8.md#insn-00b65df4) · [`00b65e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65dd8.md#insn-00b65e10) · [`00b65e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65dd8.md#insn-00b65e18)
- 新版 `00bd5310`（命令位置の公開資料なし）

~~~diff
- 00b65df4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65df4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65df4 bytes 410100b5
- 00b65e10 ["INT_ADD", "register:40f0:8", ["const:b65e10:8", "const:4:8"]]
- 00b65e10 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5310 ["INT_ADD", "register:40f0:8", ["const:bd5310:8", "const:4:8"]]
+ 00bd5310 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65e10 bytes a0e00194
+ 00bd5310 bytes 00160294
- 00b65e18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b65e18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65e18 bytes 80c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72ae11de498c193901ec26e6969762ce"></a>

### [`00b65e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e84.md) → [`00bd5384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5384.md) _ZN8firebase4auth12facebookcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b65ec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd53c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65ea0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65e98",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd53c8"
      ]
    ],
    [
      "unmatched:00b65ea8",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5398",
      "READ",
      [
        "storage",
        "01126688",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd53a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd53c8"
      ]
    ],
    [
      "00bd53a8",
      "PARAM",
      [
        "storage",
        "002bd459",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e84.md#insn-00b65ea0) · [`00b65ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e84.md#insn-00b65ebc) · [`00b65ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65e84.md#insn-00b65ec4)
- 新版 `00bd53bc`（命令位置の公開資料なし）

~~~diff
- 00b65ea0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65ea0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65ea0 bytes 410100b5
- 00b65ebc ["INT_ADD", "register:40f0:8", ["const:b65ebc:8", "const:4:8"]]
- 00b65ebc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd53bc ["INT_ADD", "register:40f0:8", ["const:bd53bc:8", "const:4:8"]]
+ 00bd53bc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65ebc bytes 75e00194
+ 00bd53bc bytes d5150294
- 00b65ec4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
- 00b65ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65ec4 bytes 80c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a08818cef80e2c62f4050d3aa4ea775"></a>

### [`00b65f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f70.md) → [`00bd5470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5470.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd549c",
      "incomplete_value": true,
      "site": "00bd549c",
      "value": [
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
      "definition_site": "00b65f9c",
      "incomplete_value": true,
      "site": "00b65f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "definition_site": "00bd5484",
      "incomplete_value": true,
      "site": "00bd5484",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f84",
      "incomplete_value": true,
      "site": "00b65f84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd548c",
      "incomplete_value": false,
      "site": "00bd5494",
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
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f8c",
      "incomplete_value": false,
      "site": "00b65f94",
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
            "const:7f9:8"
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
      "00bd5480",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd548c",
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      "00bd549c",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5480",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd548c",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      "00bd549c",
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f70.md#insn-00b65f94) · [`00b65f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f70.md#insn-00b65f9c) · [`00b65f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65f70.md#insn-00b65f7c)
- 新版 `00bd5494`（命令位置の公開資料なし） · `00bd549c`（命令位置の公開資料なし） · `00bd547c`（命令位置の公開資料なし）

~~~diff
- 00b65f94 ["INT_ADD", "register:40f0:8", ["const:b65f94:8", "const:4:8"]]
- 00b65f94 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5494 ["INT_ADD", "register:40f0:8", ["const:bd5494:8", "const:4:8"]]
+ 00bd5494 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65f94 bytes 3fe00194
+ 00bd5494 bytes 9f150294
- 00b65f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b65f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd549c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00bd549c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f9c bytes 60d203f9
+ 00bd549c bytes 605603f9
- 00b65f7c ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd547c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65f7c bytes f3290090
+ 00bd547c bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484eea49ccf28abee28e1588653c5f8b"></a>

### [`00b65fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65fb0.md) → [`00bd54b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54b0.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd54e0",
      "incomplete_value": true,
      "site": "00bd54e0",
      "value": [
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
      "definition_site": "00b65fe0",
      "incomplete_value": true,
      "site": "00b65fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "definition_site": "00bd54c4",
      "incomplete_value": true,
      "site": "00bd54c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fc4",
      "incomplete_value": true,
      "site": "00b65fc4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd54d0",
      "incomplete_value": false,
      "site": "00bd54d8",
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
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65fd0",
      "incomplete_value": false,
      "site": "00b65fd8",
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
            "const:7f9:8"
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
      "00bd54c0",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd54d0",
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      "00bd54e0",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd54c0",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd54d0",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      "00bd54e0",
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65fb0.md#insn-00b65fd8) · [`00b65fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65fb0.md#insn-00b65fe0) · [`00b65fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65fb0.md#insn-00b65fbc)
- 新版 `00bd54d8`（命令位置の公開資料なし） · `00bd54e0`（命令位置の公開資料なし） · `00bd54bc`（命令位置の公開資料なし）

~~~diff
- 00b65fd8 ["INT_ADD", "register:40f0:8", ["const:b65fd8:8", "const:4:8"]]
- 00b65fd8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd54d8 ["INT_ADD", "register:40f0:8", ["const:bd54d8:8", "const:4:8"]]
+ 00bd54d8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b65fd8 bytes 2ee00194
+ 00bd54d8 bytes 8e150294
- 00b65fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b65fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd54e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a8:8"]]
+ 00bd54e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65fe0 bytes 60d203f9
+ 00bd54e0 bytes 605603f9
- 00b65fbc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd54bc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b65fbc bytes f3290090
+ 00bd54bc bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7883298cc69151b419b46fbf4fc38c45"></a>

### [`00b65ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ff4.md) → [`00bd54f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd54f4.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66024"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5524"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd5508",
      "incomplete_value": true,
      "site": "00bd5508",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66008",
      "incomplete_value": true,
      "site": "00b66008",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00bd5504",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5508",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66028"
      ]
    ],
    [
      "unmatched:00b66010",
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5504",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5508",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5528"
      ]
    ],
    [
      "00bd5510",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ff4.md#insn-00b66008) · [`00b6601c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ff4.md#insn-00b6601c) · [`00b66024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65ff4.md#insn-00b66024)
- 新版 `00bd5508`（命令位置の公開資料なし） · `00bd551c`（命令位置の公開資料なし）

~~~diff
- 00b66008 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b66008 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd5508 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd5508 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b66008 bytes 080100b5
+ 00bd5508 bytes 080100b5
- 00b6601c ["INT_ADD", "register:40f0:8", ["const:b6601c:8", "const:4:8"]]
- 00b6601c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd551c ["INT_ADD", "register:40f0:8", ["const:bd551c:8", "const:4:8"]]
+ 00bd551c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6601c bytes 1de00194
+ 00bd551c bytes 7d150294
- 00b66024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
- 00b66024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66024 bytes 60d203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1e018e2173390e15eb671ff19482051"></a>

### [`00b660b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b660b0.md) → [`00bd55b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd55b0.md) _ZN8firebase4auth10githubcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "site": "00b660ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6610c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd55ec"
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
      "00bd55c4",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd55d0",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd55d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b660f0"
      ]
    ]
  ],
  "added": [
    [
      "00bd55c4",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd55d0",
      "READ",
      [
        "storage",
        "011266b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd55d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd55f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b660c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b660b0.md#insn-00b660c8) · [`00b660ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b660b0.md#insn-00b660ec) · [`00b660f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b660b0.md#insn-00b660f4)
- 新版 `00bd55c8`（命令位置の公開資料なし）

~~~diff
- 00b660c8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b660c8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd55c8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd55c8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b660c8 bytes 410200b4
+ 00bd55c8 bytes 410200b4
- 00b660ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b660ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b660ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7a8:8"]]
- 00b660ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b660ec bytes bfa21e39
- 00b660f4 ["INT_ADD", "register:40f0:8", ["const:b660f4:8", "const:4:8"]]
- 00b660f4 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b660f4 bytes fbdf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-309e2cef625ca09dae8c34e274abdd21"></a>

### [`00b66120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66120.md) → [`00bd5620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5620.md) _ZN8firebase4auth10githubcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd5660",
      "incomplete_value": true,
      "site": "00bd5660",
      "value": [
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
      "definition_site": "00b66160",
      "incomplete_value": true,
      "site": "00b66160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7a0:8"
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
      "definition_site": "00bd563c",
      "incomplete_value": true,
      "site": "00bd563c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6613c",
      "incomplete_value": true,
      "site": "00b6613c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd5644",
      "incomplete_value": false,
      "site": "00bd5658",
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
            "const:da2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66144",
      "incomplete_value": false,
      "site": "00b66158",
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
            "const:7f9:8"
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
      "00bd5634",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5644",
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ],
    [
      "00bd5660",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5634",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5644",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ],
    [
      "00bd5660",
      "WRITE",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66120.md#insn-00b66158) · [`00b66160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66120.md#insn-00b66160) · [`00b6612c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66120.md#insn-00b6612c)
- 新版 `00bd5658`（命令位置の公開資料なし） · `00bd5660`（命令位置の公開資料なし） · `00bd562c`（命令位置の公開資料なし）

~~~diff
- 00b66158 ["INT_ADD", "register:40f0:8", ["const:b66158:8", "const:4:8"]]
- 00b66158 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5658 ["INT_ADD", "register:40f0:8", ["const:bd5658:8", "const:4:8"]]
+ 00bd5658 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66158 bytes cedf0194
+ 00bd5658 bytes 2e150294
- 00b66160 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b66160 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5660 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a8:8"]]
+ 00bd5660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66160 bytes 80d203f9
+ 00bd5660 bytes 805603f9
- 00b6612c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd562c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b6612c bytes d42900f0
+ 00bd562c bytes 942a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18a2bf5133a8d4885f531daed9b157cb"></a>

### [`00b661cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b661cc.md) → [`00bd56cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd56cc.md) _ZN8firebase4auth10githubcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b6620c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd570c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b661e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b661e0",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b661e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5710"
      ]
    ],
    [
      "unmatched:00b661f0",
      "PARAM",
      [
        "storage",
        "002b07f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd56e0",
      "READ",
      [
        "storage",
        "011266a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd56e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5710"
      ]
    ],
    [
      "00bd56f0",
      "PARAM",
      [
        "storage",
        "002c1da2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b661e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b661cc.md#insn-00b661e8) · [`00b66204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b661cc.md#insn-00b66204) · [`00b6620c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b661cc.md#insn-00b6620c)
- 新版 `00bd5704`（命令位置の公開資料なし）

~~~diff
- 00b661e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b661e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b661e8 bytes 410100b5
- 00b66204 ["INT_ADD", "register:40f0:8", ["const:b66204:8", "const:4:8"]]
- 00b66204 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5704 ["INT_ADD", "register:40f0:8", ["const:bd5704:8", "const:4:8"]]
+ 00bd5704 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66204 bytes a3df0194
+ 00bd5704 bytes 03150294
- 00b6620c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
- 00b6620c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6620c bytes 80d203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbbd3670a1c701a46a97c0c19ad5c8e9"></a>

### [`00b66278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66278.md) → [`00bd5778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5778.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd57a4",
      "incomplete_value": true,
      "site": "00bd57a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662a4",
      "incomplete_value": true,
      "site": "00b662a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "00bd578c",
      "incomplete_value": true,
      "site": "00bd578c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6628c",
      "incomplete_value": true,
      "site": "00b6628c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd5798",
      "incomplete_value": false,
      "site": "00bd579c",
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
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66298",
      "incomplete_value": false,
      "site": "00b6629c",
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
            "const:829:8"
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
      "00bd5788",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5798",
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      "00bd57a4",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5788",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5798",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      "00bd57a4",
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6629c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66278.md#insn-00b6629c) · [`00b662a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66278.md#insn-00b662a4) · [`00b66284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66278.md#insn-00b66284)
- 新版 `00bd579c`（命令位置の公開資料なし） · `00bd57a4`（命令位置の公開資料なし） · `00bd5784`（命令位置の公開資料なし）

~~~diff
- 00b6629c ["INT_ADD", "register:40f0:8", ["const:b6629c:8", "const:4:8"]]
- 00b6629c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd579c ["INT_ADD", "register:40f0:8", ["const:bd579c:8", "const:4:8"]]
+ 00bd579c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6629c bytes 7ddf0194
+ 00bd579c bytes dd140294
- 00b662a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b662a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd57a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
+ 00bd57a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b662a4 bytes 60e203f9
+ 00bd57a4 bytes 606603f9
- 00b66284 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5784 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66284 bytes d32900f0
+ 00bd5784 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a25b66f2f2f90d7a693c81134267102c"></a>

### [`00b662b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662b8.md) → [`00bd57b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57b8.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd57e4",
      "incomplete_value": true,
      "site": "00bd57e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662e4",
      "incomplete_value": true,
      "site": "00b662e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "00bd57cc",
      "incomplete_value": true,
      "site": "00bd57cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662cc",
      "incomplete_value": true,
      "site": "00b662cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd57d4",
      "incomplete_value": false,
      "site": "00bd57dc",
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
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662d4",
      "incomplete_value": false,
      "site": "00b662dc",
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
            "const:829:8"
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
      "00bd57c8",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd57d4",
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      "00bd57e4",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd57c8",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd57d4",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      "00bd57e4",
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b662dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662b8.md#insn-00b662dc) · [`00b662e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662b8.md#insn-00b662e4) · [`00b662c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662b8.md#insn-00b662c4)
- 新版 `00bd57dc`（命令位置の公開資料なし） · `00bd57e4`（命令位置の公開資料なし） · `00bd57c4`（命令位置の公開資料なし）

~~~diff
- 00b662dc ["INT_ADD", "register:40f0:8", ["const:b662dc:8", "const:4:8"]]
- 00b662dc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd57dc ["INT_ADD", "register:40f0:8", ["const:bd57dc:8", "const:4:8"]]
+ 00bd57dc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b662dc bytes 6ddf0194
+ 00bd57dc bytes cd140294
- 00b662e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b662e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd57e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
+ 00bd57e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b662e4 bytes 60e203f9
+ 00bd57e4 bytes 606603f9
- 00b662c4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd57c4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b662c4 bytes d32900f0
+ 00bd57c4 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5967bf91bb7c78fd669ba821b256bd9b"></a>

### [`00b662f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662f8.md) → [`00bd57f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd57f8.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00bd5828",
      "incomplete_value": true,
      "site": "00bd5828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66328",
      "incomplete_value": true,
      "site": "00b66328",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "definition_site": "00bd580c",
      "incomplete_value": true,
      "site": "00bd580c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6630c",
      "incomplete_value": true,
      "site": "00b6630c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00bd5818",
      "incomplete_value": false,
      "site": "00bd5820",
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
            "const:dd2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66318",
      "incomplete_value": false,
      "site": "00b66320",
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
            "const:829:8"
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
      "00bd5808",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5818",
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ],
    [
      "00bd5828",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd5808",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5818",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ],
    [
      "00bd5828",
      "WRITE",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662f8.md#insn-00b66320) · [`00b66328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662f8.md#insn-00b66328) · [`00b66304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b662f8.md#insn-00b66304)
- 新版 `00bd5820`（命令位置の公開資料なし） · `00bd5828`（命令位置の公開資料なし） · `00bd5804`（命令位置の公開資料なし）

~~~diff
- 00b66320 ["INT_ADD", "register:40f0:8", ["const:b66320:8", "const:4:8"]]
- 00b66320 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5820 ["INT_ADD", "register:40f0:8", ["const:bd5820:8", "const:4:8"]]
+ 00bd5820 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b66320 bytes 5cdf0194
+ 00bd5820 bytes bc140294
- 00b66328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
- 00b66328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd5828 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c8:8"]]
+ 00bd5828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66328 bytes 60e203f9
+ 00bd5828 bytes 606603f9
- 00b66304 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd5804 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b66304 bytes d32900f0
+ 00bd5804 bytes 932a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79ce83ccf1ca5a8fb238a1142c6de811"></a>

### [`00b6633c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6633c.md) → [`00bd583c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd583c.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6633c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66340"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66340"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6633c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66340",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6634c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd583c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5840",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd584c",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6633c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6633c.md#insn-00b6633c) · [`00b66340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6633c.md#insn-00b66340) · [`00b66350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6633c.md#insn-00b66350)

~~~diff
- 00b6633c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6633c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6633c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6633c bytes f30f1ef8
- 00b66340 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66340 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66340 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b66340 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66340 bytes fd7b01a9
- 00b66350 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b66350 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66350 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed755c41b2d6ab320749acc2b4532ac1"></a>

### [`00b6638c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6638c.md) → [`00bd588c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd588c.md) _ZN8firebase4auth10googlecred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "definition_site": "00bd58e4",
      "incomplete_value": true,
      "site": "00bd58e4",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b663e4",
      "incomplete_value": true,
      "site": "00b663e4",
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
            "const:7c8:8"
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
      "definition_site": "00bd58c0",
      "incomplete_value": true,
      "site": "00bd58cc",
      "value": [
        "LOAD",
        "8",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:6c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b663c0",
      "incomplete_value": true,
      "site": "00b663cc",
      "value": [
        "LOAD",
        "8",
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
      "00bd58a0",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd58c0",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd58e4",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd58a0",
      "READ",
      [
        "storage",
        "011266d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd58c0",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd58e4",
      "WRITE",
      [
        "storage",
        "011266d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b663cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6638c.md#insn-00b663cc) · [`00b663e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6638c.md#insn-00b663e4) · [`00b6639c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b6638c.md#insn-00b6639c)
- 新版 `00bd58cc`（命令位置の公開資料なし） · `00bd58e4`（命令位置の公開資料なし） · `00bd589c`（命令位置の公開資料なし）

~~~diff
- 00b663cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b663cc ["INT_ADD", "register:40f0:8", ["const:b663cc:8", "const:4:8"]]
- 00b663cc ["CALLIND", null, ["register:0:8"]]
+ 00bd58cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd58cc ["INT_ADD", "register:40f0:8", ["const:bd58cc:8", "const:4:8"]]
+ 00bd58cc ["CALLIND", null, ["register:0:8"]]
- 00b663cc bytes 00013fd6
+ 00bd58cc bytes 00013fd6
- 00b663e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b663e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c8:8"]]
- 00b663e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd58e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd58e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6d0:8"]]
+ 00bd58e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b663e4 bytes a0221f39
+ 00bd58e4 bytes a0421b39
- 00b6639c ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd589c ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b6639c bytes d52900f0
+ 00bd589c bytes 952a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a54808a5860eb9c96805eab5df552b2"></a>

### [`00b663f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b663f8.md) → [`00bd58f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd58f8.md) _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

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
      "site": "00b663f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b663fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b663fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b663f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b663fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66400",
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
      "00bd58f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd58fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd5900",
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

- 旧版 [`00b663f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b663f8.md#insn-00b663f8) · [`00b663fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b663f8.md#insn-00b663fc) · [`00b66400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b663f8.md#insn-00b66400)

~~~diff
- 00b663f8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b663f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b663f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b663f8 bytes f50f1df8
- 00b663fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b663fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b663fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b663fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b663fc bytes f44f01a9
- 00b66400 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66400 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66400 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b66400 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66400 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab9fd04252a6c72e1a770db0fb6392d"></a>

### [`00b66468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66468.md) → [`00bd5968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5968.md) _ZN8firebase4auth10googlecred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b664a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd59a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66484"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6647c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66484",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd59ac"
      ]
    ],
    [
      "unmatched:00b6648c",
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd597c",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd59ac"
      ]
    ],
    [
      "00bd598c",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66468.md#insn-00b66484) · [`00b664a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66468.md#insn-00b664a0) · [`00b664a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66468.md#insn-00b664a8)
- 新版 `00bd59a0`（命令位置の公開資料なし）

~~~diff
- 00b66484 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66484 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66484 bytes 410100b5
- 00b664a0 ["INT_ADD", "register:40f0:8", ["const:b664a0:8", "const:4:8"]]
- 00b664a0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd59a0 ["INT_ADD", "register:40f0:8", ["const:bd59a0:8", "const:4:8"]]
+ 00bd59a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b664a0 bytes fcde0194
+ 00bd59a0 bytes 5c140294
- 00b664a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b664a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b664a8 bytes 80e203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bea15f05351398c904fa4d196780ae5"></a>

### [`00b66514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66514.md) → [`00bd5a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd5/00bd5a14.md) _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00b66554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd5a54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66530"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66528",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66530",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5a58"
      ]
    ],
    [
      "unmatched:00b66538",
      "PARAM",
      [
        "storage",
        "002b0829",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd5a28",
      "READ",
      [
        "storage",
        "011266c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd5a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd5a58"
      ]
    ],
    [
      "00bd5a38",
      "PARAM",
      [
        "storage",
        "002c1dd2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66514.md#insn-00b66530) · [`00b6654c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66514.md#insn-00b6654c) · [`00b66554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b66514.md#insn-00b66554)
- 新版 `00bd5a4c`（命令位置の公開資料なし）

~~~diff
- 00b66530 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66530 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66530 bytes 410100b5
- 00b6654c ["INT_ADD", "register:40f0:8", ["const:b6654c:8", "const:4:8"]]
- 00b6654c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd5a4c ["INT_ADD", "register:40f0:8", ["const:bd5a4c:8", "const:4:8"]]
+ 00bd5a4c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6654c bytes d1de0194
+ 00bd5a4c bytes 31140294
- 00b66554 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
- 00b66554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66554 bytes 80e203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

